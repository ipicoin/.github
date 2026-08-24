# IPI — Independent Protocol Infrastructure

**A multi-layer protocol infrastructure program connecting network state, open
APIs, self-custody clients, independent verification, and physical/digital
commerce research.**

IPI is not organized as a token-only repository or a single web application.
Its architecture and public work are organized across blockchain and network
foundations, wallet and key infrastructure, a block explorer, RPC client
research, node and validator integration, EVM and CosmWasm integration
directions, governance and security processes, product-identity and
secure-element research, checkout/payment concepts, and independently operable
infrastructure.

The public repositories contain different levels of evidence across those
layers. The strongest implemented components are linked first below; integration
and research work is labeled separately.

## What Exists Today

- **A zero-dependency Cosmos/EVM testnet explorer.**
  [`scan.ipi.io`](https://github.com/ipicoin/scan.ipi.io) implements block,
  transaction, account, validator, native Cosmos, and EVM JSON-RPC inspection in
  browser JavaScript, with same-origin API routing and passing public CI.
- **A tested JavaScript wallet model layer.**
  [`wallet-core.js`](https://github.com/ipicoin/wallet-core.js) contains wallet,
  address, request, transaction, and contract models plus Bech32 validation.
  Eleven model/configuration tests pass; signing and transfer operations remain
  incomplete.
- **Cosmos RPC transport and client-generation research.**
  [`ipi-rpc`](https://github.com/ipicoin/ipi-rpc) contains protobuf inputs,
  generated TypeScript clients, and comparison pages for gRPC-Web and
  gRPC-Gateway. It is an upstream-derived integration sandbox, not an RPC server.
- **A public protocol-change and governance process.**
  [`.github`](https://github.com/ipicoin/.github) contains the architecture,
  security policy, governance rules, contribution standards, roadmap, and the
  IPI Improvement Proposal process. IPI-0000 defines the process; IPI-0001 is a
  draft evidence model for verifiable independence.
- **A public node foundation with explicit provenance.**
  [`independency-daemon`](https://github.com/ipicoin/independency-daemon) tracks
  CosmWasm `wasmd`, built on Cosmos SDK and CometBFT. Current IPI changes are
  provenance documentation and CI hardening; an IPI node release is not yet
  implemented in that fork.
- **Public product and documentation surfaces.**
  [`www.ipi.io`](https://github.com/ipicoin/www.ipi.io) is the Astro source for
  the website and documentation, while
  [`chainconfig`](https://github.com/ipicoin/chainconfig) preserves a tested but
  legacy Cosmos wallet configuration that is explicitly non-canonical.
- **Application integration sandboxes.**
  [`Iswap`](https://github.com/ipicoin/Iswap),
  [`Ivote`](https://github.com/ipicoin/Ivote), and
  [`ipi-nft`](https://github.com/ipicoin/ipi-nft) preserve attributed Hyperweb
  examples for swap, governance, and NFT workflow evaluation. They do not yet
  contain IPI network integration.

## Architecture

The intended verification path is broader than any one repository:

```text
Cosmos SDK / CometBFT / CosmWasm foundation
                ↓
IPI node integration · validator/network operation
                ↓
RPC · REST · gRPC · EVM JSON-RPC · events
                ↓
Explorer · wallet core · mobile approval · external clients
                ↓
Product identity / secure element → checkout / payment → receipt
                ↓
Independent operation, governance, and verification evidence
```

Today, the public explorer and governance/evidence layers are concrete; wallet
models and RPC clients are partial; the public node is still an upstream
foundation; and product identity, secure-element, checkout, and payment are
research directions without a public IPI implementation. See the
[architecture](https://github.com/ipicoin/.github/blob/main/ARCHITECTURE.md) and
[complete repository audit](https://github.com/ipicoin/.github/blob/main/REPOSITORY_AUDIT.md).

## Engineering Evidence

| Area | Public evidence | Status |
| --- | --- | --- |
| Explorer and verification UI | [`scan.ipi.io`](https://github.com/ipicoin/scan.ipi.io) | Active development; native Cosmos and EVM query paths implemented |
| Wallet and account models | [`wallet-core.js`](https://github.com/ipicoin/wallet-core.js) | Active development; model tests pass, signing/transfer incomplete |
| RPC/API clients | [`ipi-rpc`](https://github.com/ipicoin/ipi-rpc) | Integration research; upstream-derived generated-client comparison |
| Protocol/network foundation | [`independency-daemon`](https://github.com/ipicoin/independency-daemon) | Upstream foundation with IPI integration in progress |
| Mobile client | [`protocolix`](https://github.com/ipicoin/protocolix) | Capacitor Android/iOS scaffold; wallet logic not implemented |
| Network metadata | [`chainconfig`](https://github.com/ipicoin/chainconfig) | Tested legacy configuration; not canonical current identity |
| Governance and security | [`.github`](https://github.com/ipicoin/.github) | Active bootstrap process with automated document validation |
| Website and documentation | [`www.ipi.io`](https://github.com/ipicoin/www.ipi.io) | Active development; Astro static build |
| Independent infrastructure | [`hq-spacecraft`](https://github.com/ipicoin/hq-spacecraft) | Prototype scaffold; most service compositions are placeholders |
| Product identity / secure element | [architecture](https://github.com/ipicoin/.github/blob/main/ARCHITECTURE.md), [`node-ntag424` reference fork](https://github.com/ipicoin/nikeee___node-ntag424) | Research direction; no IPI-specific implementation |
| Checkout / payment / receipt | [roadmap](https://github.com/ipicoin/.github/blob/main/ROADMAP.md), [`cheer-gear` reference fork](https://github.com/ipicoin/cheer-gear) | Concept and hardware scaffold; no executable IPI integration |

## Why IPI Is Different

IPI's engineering thesis is that infrastructure should be inspectable and
replaceable at every layer:

- **Independence:** a hosted endpoint or organization account must not silently
  become the only way to operate or verify the system.
- **Self-custody:** keys and signing intent belong at the user-controlled edge;
  wallets must make network identity and authorized actions explicit.
- **Independent operation:** nodes, clients, explorers, and optional services
  should have documented deployment, recovery, and exit paths.
- **Reproducibility:** protocol claims should resolve to source revisions,
  dependency locks, build procedures, tests, and observable evidence.
- **Open interfaces:** RPC, REST, gRPC, EVM JSON-RPC, events, and portable data
  formats are boundaries that independent implementations can reproduce.
- **Transparent governance:** protocol and trust changes belong in public,
  versioned proposals with security, compatibility, and operational analysis.
- **Hardware-backed identity direction:** P-256/R1, NFC, and secure-element work
  is treated as a separate attestation and privacy problem, not as a marketing
  shortcut or a reason to put secret data on-chain.

These are design requirements and research goals, not a claim that every layer
is complete or independently operated today.

## Upstream Foundations

IPI deliberately evaluates established open-source foundations including
Cosmos SDK, CometBFT, CosmWasm, `wasmd`, Ethereum tooling, WebAuthn, and secure
hardware libraries. Using upstream infrastructure is normal protocol
engineering: it provides reviewed interfaces, interoperability, and a visible
history to build on.

Attribution is explicit. Twenty-six public IPI forks currently contain no
commits ahead of upstream. `independency-daemon` has two IPI commits limited to
fork provenance and CI hardening. These forks are research references and must
not be read as IPI-authored implementations. IPI-specific public evidence lives
in the explorer, wallet model/test work, governance and architecture,
configuration, documentation, and integration boundaries described above.

## Development Status

IPI is under active development. No public repository should be assumed safe
for production assets unless a versioned release explicitly documents its
threat model, compatibility, reproducible build, tests, security review, and
support lifecycle.

The main public evidence gaps are a consolidated IPI-specific node source and
genesis binding, public validator/deployment tooling, completed wallet signing
flows, reproducible releases, and public implementations for product identity,
secure-element attestation, checkout, payment, and receipts. The
[roadmap](https://github.com/ipicoin/.github/blob/main/ROADMAP.md) defines the
evidence expected before stronger maturity claims.

## Start Here

[Explorer](https://github.com/ipicoin/scan.ipi.io) ·
[Architecture](https://github.com/ipicoin/.github/blob/main/ARCHITECTURE.md) ·
[Repository audit](https://github.com/ipicoin/.github/blob/main/REPOSITORY_AUDIT.md) ·
[Governance](https://github.com/ipicoin/.github/blob/main/GOVERNANCE.md) ·
[IPI proposals](https://github.com/ipicoin/.github/tree/main/ipi) ·
[Roadmap](https://github.com/ipicoin/.github/blob/main/ROADMAP.md) ·
[Security](https://github.com/ipicoin/.github/blob/main/SECURITY.md) ·
[Website](https://ipi.io)
