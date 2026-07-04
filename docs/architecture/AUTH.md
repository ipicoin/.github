# Architektura tożsamości i uwierzytelniania IPI

> **DRAFT architektury — do review.**
> Dokument fundamentowy [Fala 0] roadmapy IPI. Wyznacza kierunek, nie jest jeszcze specyfikacją wdrożeniową.
> Realizuje `ipicoin/.github#1`, część roadmapy `ipicoin/universal-independency-declaration#1`.

## 1. Cel i zasady

Celem jest jednolity model tożsamości i uwierzytelniania dla całego ekosystemu **Independent Protocol Infrastructure (IPI)**, obejmujący trzy główne scenariusze użycia:

- **Wallet** — logowanie i zarządzanie portfelem IPI (`wallet-core.js`, aplikacja `protocolix`).
- **Głosowanie DAO** — uwierzytelnianie propozycji i głosów (`Ivote`), gdzie liczy się niezaprzeczalność.
- **Karty cheers** — płatności prepaid na eventach federacji DAO (`cheers-protocol`, terminal `cheer-gear`).

Zasady projektowe:

1. **Klucz prywatny nie opuszcza sprzętu.** Podpis powstaje na urządzeniu (authenticator / Yubikey / karta), nigdy przez eksport klucza.
2. **Phishing-resistant domyślnie.** Uwierzytelnianie web oparte o WebAuthn (origin-bound), bez haseł współdzielonych.
3. **Minimalizacja zaufania do serwera.** Serwer weryfikuje podpisy i wyzwania; nie przechowuje sekretów zdolnych do podszycia się pod użytkownika.
4. **Warstwowość i degradacja.** Różne warstwy dla różnych poziomów ryzyka — logowanie web, podpis transakcji, płatność offline NFC.
5. **Jedna tożsamość, wiele czynników.** Konto = zbiór zarejestrowanych kluczy publicznych mapowanych na jeden DID/adres.

## 2. Warstwy uwierzytelniania

### (a) WebAuthn / passkeys — logowanie web

Rejestracja i logowanie do interfejsów web (portal wallet, panel DAO) w oparciu o standard [W3C WebAuthn](https://github.com/ipicoin/w3c___webauthn) (fork org).

- **Rejestracja:** przeglądarka generuje parę kluczy dla `rp.id` (domena IPI); klucz publiczny + `credentialId` trafiają do konta.
- **Uwierzytelnianie:** serwer wysyła losowe `challenge`; authenticator podpisuje je kluczem prywatnym; podpis jest origin-bound (odporny na phishing).
- **Passkeys** (rezydentne poświadczenia synchronizowane) dla wygody kont konsumenckich; **klucze sprzętowe** (Yubikey jako authenticator WebAuthn/FIDO2) dla kont wysokiego ryzyka.
- Weryfikacja `attestation` przy rejestracji kluczy sprzętowych pozwala wymusić politykę autoryzowanych urządzeń dla ról administracyjnych DAO.

> **Uwaga (patrz §2e).** WebAuthn nadaje się do **logowania web** (origin-bound challenge). Użycie WebAuthn do **podpisu transakcji on-chain e2e** nie jest transparentne: authenticator podpisuje `authenticatorData || SHA256(clientDataJSON)`, a **nie** surowy `SignDoc` transakcji Cosmos. E2e podpis wymaga modułu chain-side, który zrekonstruuje i zweryfikuje ten payload (§2e) — sam wallet nie zamyka tej ścieżki.

### (b) Yubikey PIV — sprzętowy podpis transakcji

Dla operacji o wysokiej wartości (podpis transakcji on-chain, autoryzacja propozycji DAO) używamy apletu **PIV** Yubikey, obsługiwanego przez forki org:

- [`Yubico/yubico-piv-tool`](https://github.com/ipicoin/Yubico___yubico-piv-tool) — narzędzie CLI + libykpiv (provisioning, generowanie kluczy w slotach PIV).
- [`agco/yubikey-piv-node`](https://github.com/ipicoin/agco___yubikey-piv-node) — dostęp do funkcji PIV z poziomu Node.js (integracja z `wallet-core.js`).

Model:

- Klucz prywatny transakcji generowany **w slocie PIV** (np. `9c` / Digital Signature); nie da się go wyeksportować.
- Podpis transakcji IPI wymaga fizycznej obecności klucza + PIN PIV (dwa czynniki: posiadanie + wiedza).
- Klucz publiczny ze slotu jest mapowany na adres IPI (patrz §2d), więc podpis PIV = podpis transakcji z danego adresu.

> **Uwaga (krytyczna, patrz §2e).** Aplet PIV YubiKey podpisuje krzywą **P-256 (secp256r1)**, a nie **secp256k1** używaną domyślnie przez Cosmos SDK. Sam portfel z YubiKey PIV **nie wystarczy** — łańcuch musi obsłużyć niestandardowy typ klucza publicznego (`secp256r1`) i weryfikować taki podpis. To zakres chain-side (§2e), nie samego walleta.

### (c) NTAG424 DNA — karty NFC (prepaid / event)

Karty NFC oparte o **NXP NTAG424 DNA**, obsługiwane przez fork [`nikeee/node-ntag424`](https://github.com/ipicoin/nikeee___node-ntag424), zasilają scenariusze prepaid/event w `cheers-protocol` i terminalu `cheer-gear`.

Kluczowe własności NTAG424:

- **SUN (Secure Unique NFC) + CMAC** — przy każdym tapnięciu karta generuje unikalny, kryptograficznie uwierzytelniony URL/payload (rosnący licznik `read counter` + podpis CMAC). Uniemożliwia to prosty replay skopiowanego identyfikatora.
- **Klucze symetryczne AES-128** w bezpiecznej pamięci karty; diversyfikacja klucza per-karta z klucza master (nie przechowujemy klucza master na kartach).
- Karta = **nosiciel salda prepaid / uprawnienia event**, powiązana z tożsamością IPI (adres/DID) po stronie backendu.

> Uwaga: NTAG424 operuje na kryptografii symetrycznej (AES/CMAC). Ścieżka do bezpieczeństwa asymetrycznego w tanich tagach NFC — istotna dla systemów transakcyjnych — opisana jest w pracy referencyjnej z README `protocolix` (patrz §5). Kierunek docelowy: karta autoryzuje płatność offline (SUN/CMAC), a rozliczenie on-chain podpisywane jest asymetrycznie po stronie portfela/terminala.

### (d) Mapowanie tożsamości → DID / adres bech32 `ipi`

Wszystkie warstwy zbiegają się w jednej tożsamości:

- **Konto IPI = DID** agregujący zarejestrowane klucze publiczne (WebAuthn credential, klucz PIV, powiązania kart NTAG424).
- Adres on-chain w formacie **bech32 z prefiksem `ipi`** (środowisko Cosmos, zgodnie z `chain-registry` / `chainconfig`), wyprowadzany z klucza publicznego zdolnego do podpisu transakcji (typowo klucz PIV lub klucz portfela).
- Dokument DID wiąże metody weryfikacji: `webauthn` (logowanie), `piv` (podpis tx), `ntag424` (uprawnienie karty) — dzięki czemu jeden użytkownik ma spójną tożsamość niezależnie od warstwy.

```
                        DID: did:ipi:<...>  ──►  adres bech32: ipi1...
                        ┌───────────────┬──────────────┬──────────────┐
   logowanie web ──►    │  WebAuthn     │              │              │
   podpis tx     ──►    │               │  Yubikey PIV │              │
   płatność NFC  ──►    │               │              │  NTAG424 DNA │
                        └───────────────┴──────────────┴──────────────┘
```

### (e) Wymagania chain-side (KRYTYCZNE — bez tego wallet sam nie wystarczy)

Kluczowe ograniczenie fundamentowe: **WebAuthn i YubiKey PIV nie dają samodzielnie podpisu transakcji on-chain akceptowanego przez łańcuch IPI.** Oba mechanizmy wymagają wsparcia po stronie łańcucha (`independency-daemon`), którego dziś nie ma. Ten dokument nie obiecuje, że sam wallet zamknie ścieżkę e2e — poniższe pozycje to jawny zakres Fali 0/1.

**1. Niedopasowanie krzywej (PIV).** Aplet PIV YubiKey operuje na krzywej **P-256 = secp256r1** (NIST). Cosmos SDK domyślnie weryfikuje **secp256k1** (i ed25519 dla walidatorów). Podpis ze slotu PIV `9c` jest więc **nie do zweryfikowania** przez standardowy AnteHandler bez rozszerzenia.

**2. Format podpisu WebAuthn ≠ SignDoc.** Authenticator WebAuthn/FIDO2 nie podpisuje surowego `SignDoc` (ani `SIGN_MODE_DIRECT` bytes, ani amino). Podpisuje konkatenację:

```text
signature = Sign( authenticatorData || SHA256(clientDataJSON) )
```

gdzie `challenge` transakcji jest osadzone wewnątrz `clientDataJSON`. Łańcuch, aby zweryfikować taki podpis, musi:
- odtworzyć `clientDataJSON` (z osadzonym challenge = hash SignDoc),
- policzyć `SHA256(clientDataJSON)`,
- złożyć `authenticatorData || SHA256(clientDataJSON)`,
- zweryfikować podpis P-256 nad tą wartością.

Standardowy verifier Cosmos tego nie robi — dostaje surowy podpis i surowy SignDoc.

**3. Wymagany moduł w `independency-daemon`.** Aby oba czynniki działały e2e, w daemonie trzeba wdrożyć:
- **Custom pubkey type** `secp256r1` (własny typ w `cryptotypes.PubKey`, rejestracja w codec/interface registry) — obsługa krzywej P-256.
- **Verifier / AnteHandler** rozpoznający sygnaturę P-256 oraz — dla ścieżki WebAuthn — dekodujący i rekonstruujący payload `authenticatorData || SHA256(clientDataJSON)` przed weryfikacją (analogicznie do rozwiązań typu WebAuthn-on-chain / EIP-7212 w innych ekosystemach).
- Ewentualnie osobny **SignMode** / dekorator ante dla transakcji podpisanych sprzętowo.

Bez tych elementów `PivSigner` / `WebAuthnSigner` z §3 (wallet-core.js) produkują podpisy, których **łańcuch odrzuci**.

**4. NTAG424 — poza tym ograniczeniem (kryptografia symetryczna, poprawnie).** Warstwa NTAG424 (§2c) opiera się o **AES-128 / CMAC (symetryczne)** i **nie** jest podpisem transakcji on-chain. Autoryzacja SUN/CMAC jest weryfikowana po stronie backendu/terminala, a rozliczenie on-chain podpisywane jest osobno asymetrycznym kluczem portfela. NTAG424 nie wymaga zmian w łańcuchu i tu żadnej rozbieżności krzywych nie ma.

**Zakres.** Punkty 1–3 są warunkiem koniecznym dla „hardware-key signing" i muszą trafić do zakresu **Fali 0/1** (moduł chain-side), zanim `wallet-core.js` (Fala 2) będzie mógł realnie delegować podpis do YubiKey/WebAuthn. Do czasu ich wdrożenia dokument traktuje e2e podpis WebAuthn/PIV jako **niewykonalny samym walletem**.

## 3. Integracja z ekosystemem

### wallet-core.js (Fala 2 — hardware-key signing)

- `wallet-core.js` deleguje podpis transakcji do warstwy sprzętowej zamiast trzymać klucz w pamięci procesu.
- Punkt integracji: adapter podpisu wołający `yubikey-piv-node` (slot PIV) lub authenticator WebAuthn; wynik to podpis akceptowany przez łańcuch IPI.
- Wymaganie dla Fali 2: interfejs `signer` z implementacjami `PivSigner` / `WebAuthnSigner`, tak by portfel nie znał materiału klucza.
- **Zależność blokująca:** `PivSigner` / `WebAuthnSigner` mają sens dopiero po wdrożeniu modułu chain-side (§2e — custom pubkey `secp256r1` + verifier/AnteHandler). Bez niego łańcuch odrzuci produkowane podpisy; Fala 2 nie jest samowystarczalna po stronie walleta.

### cheers-protocol (Fala 4 — prepaid RFID / 3DS)

- Karty NTAG424 = fizyczny nośnik prepaid dla eventów federacji DAO.
- Terminal `cheer-gear` czyta payload SUN/CMAC (`node-ntag424`), weryfikuje CMAC + licznik, autoryzuje płatność, a rozliczenie kieruje do `cheers-protocol` (model inspirowany 3DS: rozdzielenie autoryzacji od rozliczenia).
- Powiązanie karty z tożsamością IPI (§2d) pozwala doładowywać/rozliczać saldo względem adresu `ipi`.

## 4. Model zagrożeń (skrót)

| Zagrożenie | Wektor | Mitigacja |
|---|---|---|
| **Kradzież klucza** | wyciek klucza prywatnego portfela | klucz nie opuszcza sprzętu (PIV slot / authenticator); brak eksportu |
| **Phishing** | fałszywa domena zbiera poświadczenia | WebAuthn origin-bound — podpis związany z `rp.id`, bezużyteczny na innej domenie |
| **Replay NFC** | skopiowanie/odtworzenie tapnięcia karty | SUN + CMAC + rosnący licznik odczytu — każdy payload unikalny i uwierzytelniony; serwer odrzuca powtórzony/cofnięty licznik |
| **Utrata karty** | fizyczna utrata karty prepaid | limit salda prepaid; rewokacja powiązania karta↔DID; wymóg PIN dla wyższych kwot; brak klucza master na karcie |
| **Utrata Yubikey** | utrata sprzętowego signera | rejestracja ≥2 kluczy per konto; procedura rewokacji klucza publicznego w DID; social/threshold recovery na poziomie DAO |
| **Podszycie pod urządzenie** | nieautoryzowany authenticator dla roli admin | wymuszenie `attestation` przy rejestracji dla ról administracyjnych |

## 5. Odniesienia

Forki organizacji IPI stanowiące bazę techniczną:

- [`ipicoin/Yubico___yubico-piv-tool`](https://github.com/ipicoin/Yubico___yubico-piv-tool) — CLI i biblioteka PIV dla YubiKey.
- [`ipicoin/agco___yubikey-piv-node`](https://github.com/ipicoin/agco___yubikey-piv-node) — PIV z poziomu Node.js.
- [`ipicoin/w3c___webauthn`](https://github.com/ipicoin/w3c___webauthn) — standard WebAuthn.
- [`ipicoin/nikeee___node-ntag424`](https://github.com/ipicoin/nikeee___node-ntag424) — interop z NTAG 424 DNA (SUN/CMAC).

Materiał merytoryczny:

- Artykuł o **asymetrycznym bezpieczeństwie w NFC** w systemach transakcyjnych (referencja z README `ipicoin/protocolix`): _Security-Enabled Near-Field Communication Tag With Flexible Architecture Supporting Asymmetric Cryptography_ — https://www.researchgate.net/publication/260655435_Security-Enabled_Near-Field_Communication_Tag_With_Flexible_Architecture_Supporting_Asymmetric_Cryptography

Powiązane repozytoria ekosystemu: `wallet-core.js`, `protocolix`, `cheers-protocol`, `cheer-gear`, `Ivote`, `chain-registry`, `chainconfig`.

---
_Status: DRAFT — otwarty na uwagi. Kolejne fale (2 — hardware-key signing w wallet-core.js; 4 — cheers-protocol) doprecyzują interfejsy `signer` i przepływ SUN/CMAC → rozliczenie on-chain._
