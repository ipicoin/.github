# CI/CD + Security scanning org-wide (IPI)

Ten dokument opisuje, jak repozytoria organizacji **IPI** (`ipicoin`) podpinają
współdzielone (reusable) workflowy CI/CD i skanowania bezpieczeństwa
utrzymywane centralnie w repozytorium `ipicoin/.github`.

Zamiast kopiować konfiguracje do każdego repo, każde repo wywołuje workflowy
przez `uses:`. Dzięki temu aktualizacja logiki (np. podbicie wersji akcji,
nowe reguły skanowania) w jednym miejscu propaguje się na całą organizację.

## Dostępne reusable workflows

| Workflow | Plik | Co robi |
| --- | --- | --- |
| CI | `.github/workflows/reusable-ci.yml` | Build + test + lint. Matryca Node / Python / Go / Rust, uruchamiana **warunkowo** wg obecności pliku manifestu (`package.json`, `requirements.txt`/`pyproject.toml`, `go.mod`, `Cargo.toml`). |
| CodeQL | `.github/workflows/reusable-codeql.yml` | Skan bezpieczeństwa CodeQL (na wzór `ipicoin/protocolix`). |
| Security | `.github/workflows/reusable-security.yml` | Dependency review + secret scan (gitleaks) + opcjonalny SonarCloud. |

## Szybki start

Najprościej: w nowym repo wejdź w zakładkę **Actions → New workflow** i wybierz
starter **„IPI CI/CD + Security"** (dostarczany z tego repo przez
`workflow-templates/`). Alternatywnie utwórz ręcznie plik
`.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  ci:
    uses: ipicoin/.github/.github/workflows/reusable-ci.yml@main

  codeql:
    uses: ipicoin/.github/.github/workflows/reusable-codeql.yml@main
    permissions:
      security-events: write
      packages: read
      actions: read
      contents: read
    with:
      languages: '["javascript-typescript"]'

  security:
    uses: ipicoin/.github/.github/workflows/reusable-security.yml@main
    with:
      enable-dependency-review: true
      enable-secret-scan: true
      enable-sonar: false
```

> Uwaga: składnia ścieżki to `ipicoin/.github/.github/workflows/<plik>@<ref>`.
> Podwójne `.github/.github` jest poprawne — pierwsze to nazwa repo,
> drugie to katalog workflow.

## reusable-ci.yml — parametry (`with:`)

| Input | Domyślnie | Opis |
| --- | --- | --- |
| `node-version` | `20` | Wersja Node.js. |
| `python-version` | `3.12` | Wersja Pythona. |
| `go-version` | `1.22` | Wersja Go. |
| `rust-toolchain` | `stable` | Toolchain Rust. |
| `working-directory` | `.` | Katalog roboczy dla komend build/test. |

Zadania językowe uruchamiają się tylko, gdy wykryty zostanie odpowiedni
manifest. Repo bez `go.mod` nie uruchomi joba Go itd. Lint jest częścią joba
danego języka (`npm run lint`, `ruff`, `go vet`, `clippy`).

## reusable-codeql.yml — parametry (`with:`)

| Input | Domyślnie | Opis |
| --- | --- | --- |
| `languages` | `'["javascript-typescript"]'` | JSON-owa tablica języków CodeQL. |
| `build-mode` | `none` | `none`, `autobuild` lub `manual`. |
| `queries` | `""` | Opcjonalne pakiety zapytań, np. `security-extended,security-and-quality`. |

Wywołanie **musi** nadać uprawnienia `security-events: write` (patrz przykład
wyżej), inaczej wgranie wyników do zakładki Security się nie powiedzie.

Obsługiwane wartości `languages`: `actions`, `c-cpp`, `csharp`, `go`,
`java-kotlin`, `javascript-typescript`, `python`, `ruby`, `rust`, `swift`.

## reusable-security.yml — parametry (`with:` / `secrets:`)

| Input | Domyślnie | Opis |
| --- | --- | --- |
| `enable-dependency-review` | `true` | Dependency review (działa tylko na `pull_request`). |
| `enable-secret-scan` | `true` | Skan sekretów gitleaks. |
| `enable-sonar` | `false` | Analiza SonarCloud (wymaga `SONAR_TOKEN`). |
| `sonar-project-key` | `""` | Klucz projektu SonarCloud. |
| `sonar-organization` | `""` | Klucz organizacji SonarCloud. |

| Secret | Wymagany | Opis |
| --- | --- | --- |
| `SONAR_TOKEN` | tylko gdy `enable-sonar: true` | Token SonarCloud. |
| `GITLEAKS_LICENSE` | nie | Licencja gitleaks (dla użycia org-wide). |

Aby włączyć Sonar:

```yaml
  security:
    uses: ipicoin/.github/.github/workflows/reusable-security.yml@main
    with:
      enable-sonar: true
      sonar-project-key: moje-repo
      sonar-organization: ipicoin
    secrets:
      SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

## Wersjonowanie (`@ref`)

- `@main` — zawsze najnowsza wersja (wygodne, ale zmienne).
- `@v1` / `@<sha>` — przypięcie do konkretnej wersji/commita dla stabilności.

Zalecenie dla repo produkcyjnych: przypinać do taga lub SHA.

## Powiązania

- Konfiguracje wzorcowe (single-repo): `ipicoin/protocolix/.github/workflows`
  (`codeql.yml`, `sonarcloud.yml`, `sonarqube.yml`, `fortify.yml`).
- Deklaracja: `universal-independency-declaration#1`.
- Issue: `ipicoin/.github#2` — [Fala 5] CI/CD + security scanning org-wide.
