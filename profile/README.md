# IPI — Independent Protocol Infrastructure

**A public, multi-layer protocol infrastructure ecosystem connecting network
state, open APIs, self-custody clients, independent verification, governance,
and physical/digital commerce integration.**

IPI organizes public engineering across blockchain and network foundations,
wallet and key infrastructure, a block explorer, RPC clients, node and validator
integration, EVM and CosmWasm interfaces, governance and security processes,
product identity and secure-element research, checkout/payment architecture,
and independently operable infrastructure. Together these layers define a path
from protocol state to user authorization, external-product verification, and
independently checkable outcomes.

Start with the implemented and tested components below. Every primary capability
links directly to its code, tests, or governing technical document; integration
and research work is labeled separately.

## What Exists Today

- **A zero-dependency Cosmos/EVM testnet explorer.**
  [`explorer.js`](https://github.com/ipicoin/scan.ipi.io/blob/main/explorer.js)
  implements block, transaction, account, validator, native Cosmos, and EVM
  JSON-RPC inspection in browser JavaScript. The repository also contains a
  [local API proxy](https://github.com/ipicoin/scan.ipi.io/blob/main/dev-server.mjs),
  a dedicated [EVM diagnostic view](https://github.com/ipicoin/scan.ipi.io/blob/main/evm.html),
  and passing public CI.
- **A tested JavaScript wallet model layer.**
  [`wallet-core.js`](https://github.com/ipicoin/wallet-core.js) contains
  [wallet, address, request, transaction, and contract models](https://github.com/ipicoin/wallet-core.js/tree/main/src/models)
  plus configurable Bech32 validation. Its
  [seven test files](https://github.com/ipicoin/wallet-core.js/tree/main/tests)
  contain eleven passing tests; signing and transfer operations remain
  incomplete.
- **Cosmos RPC transport and client-generation research.**
  [`ipi-rpc`](https://github.com/ipicoin/ipi-rpc) contains
  [Cosmos, IBC, Tendermint, and CosmWasm protobuf inputs](https://github.com/ipicoin/ipi-rpc/tree/main/proto),
  generated TypeScript clients for
  [gRPC-Web](https://github.com/ipicoin/ipi-rpc/tree/main/codegen_grpc_web) and
  [gRPC-Gateway](https://github.com/ipicoin/ipi-rpc/tree/main/codegen_grpc_gateway),
  and browser comparison pages. It is an upstream-derived integration sandbox,
  not an RPC server.
- **A public protocol-change and governance process.**
  [`.github`](https://github.com/ipicoin/.github) contains the
  [architecture](https://github.com/ipicoin/.github/blob/main/ARCHITECTURE.md),
  [security policy](https://github.com/ipicoin/.github/blob/main/SECURITY.md),
  [governance rules](https://github.com/ipicoin/.github/blob/main/GOVERNANCE.md),
  roadmap, and IPI Improvement Proposal process.
  [IPI-0000](https://github.com/ipicoin/.github/blob/main/ipi/IPI-0000.md)
  defines the process; [IPI-0001](https://github.com/ipicoin/.github/blob/main/ipi/IPI-0001.md)
  is a draft evidence model for verifiable independence.
- **A public node foundation with explicit provenance.**
  [`independency-daemon`](https://github.com/ipicoin/independency-daemon) tracks
  CosmWasm `wasmd`, built on Cosmos SDK and CometBFT. Current IPI changes are
  provenance documentation and CI hardening; an IPI node release is not yet
  implemented in that fork. The exact boundary is recorded in
  [`IPI_FORK_STATUS.md`](https://github.com/ipicoin/independency-daemon/blob/main/IPI_FORK_STATUS.md).
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

| Layer | What exists | Evidence | Status |
| --- | --- | --- | --- |
| Explorer | Native blocks, transactions, accounts, validators, search, and EVM diagnostics | [`explorer.js`](https://github.com/ipicoin/scan.ipi.io/blob/main/explorer.js) | Active development; implemented and publicly tested |
| EVM interface | JSON-RPC transaction, block, address, balance, nonce, and bytecode inspection | [`explorer.js`](https://github.com/ipicoin/scan.ipi.io/blob/main/explorer.js), [`evm.html`](https://github.com/ipicoin/scan.ipi.io/blob/main/evm.html) | Query integration demonstrated; IPI EVM execution suite not public |
| CosmWasm interface | Protobuf/query client surface plus inherited `wasmd` execution foundation | [`ipi-rpc` CosmWasm clients](https://github.com/ipicoin/ipi-rpc/tree/main/codegen_grpc_web/cosmwasm), [`independency-daemon`](https://github.com/ipicoin/independency-daemon) | Upstream foundation and client integration research; IPI execution suite not public |
| Wallet core | Wallet, address, request, transaction, and contract models; Bech32 validation | [`src/models`](https://github.com/ipicoin/wallet-core.js/tree/main/src/models), [`tests`](https://github.com/ipicoin/wallet-core.js/tree/main/tests) | Active development; eleven tests pass, signing/transfer incomplete |
| RPC/API clients | Cosmos/IBC/CosmWasm protobuf inputs and two generated TypeScript transport trees | [`proto`](https://github.com/ipicoin/ipi-rpc/tree/main/proto), [`gRPC-Web`](https://github.com/ipicoin/ipi-rpc/tree/main/codegen_grpc_web), [`gRPC-Gateway`](https://github.com/ipicoin/ipi-rpc/tree/main/codegen_grpc_gateway) | Integration research; upstream-derived, no IPI endpoint binding |
| Protocol/node | Buildable Cosmos SDK, CometBFT, IBC, and CosmWasm application foundation | [`independency-daemon`](https://github.com/ipicoin/independency-daemon), [fork boundary](https://github.com/ipicoin/independency-daemon/blob/main/IPI_FORK_STATUS.md) | Upstream foundation; IPI consensus/application delta not public |
| Mobile client | Capacitor Android/iOS project trees and browser shell | [`protocolix`](https://github.com/ipicoin/protocolix) | Prototype scaffold; wallet behavior not implemented |
| Network metadata | Tested historical Cosmos wallet configuration | [`config.json`](https://github.com/ipicoin/chainconfig/blob/main/config.json), [`test/config.test.js`](https://github.com/ipicoin/chainconfig/blob/main/test/config.test.js) | Verified legacy record; not canonical current identity |
| Governance/security | Architecture, security policy, public change control, and automated document validation | [`.github`](https://github.com/ipicoin/.github), [IPI proposals](https://github.com/ipicoin/.github/tree/main/ipi) | Active public bootstrap process |
| Website/docs | Astro landing and Starlight documentation source | [`www.ipi.io`](https://github.com/ipicoin/www.ipi.io) | Active development; public build CI passes |
| Independent infrastructure | Self-hosted service and Compose research structure | [`hq-spacecraft`](https://github.com/ipicoin/hq-spacecraft) | Prototype scaffold; most compositions are placeholders |
| Product identity / secure element | Architecture boundary and attributed NTAG 424 reference | [architecture](https://github.com/ipicoin/.github/blob/main/ARCHITECTURE.md), [`node-ntag424` reference](https://github.com/ipicoin/nikeee___node-ntag424) | Research direction; no IPI-specific implementation |
| Checkout/payment/receipt | Roadmap boundary and attributed terminal hardware scaffold | [roadmap](https://github.com/ipicoin/.github/blob/main/ROADMAP.md), [`cheer-gear` reference](https://github.com/ipicoin/cheer-gear) | Concept stage; no executable IPI integration |

## Why This Is Not Just a Token Project

The distinction is architectural and verifiable in source. A token-only project
can stop at an asset definition, marketing site, and third-party wallet link.
IPI's public organization separately exposes:

- a native Cosmos and EVM inspection surface;
- wallet/account models and validation tests;
- protobuf inputs and generated RPC client transports;
- an attributed node/execution foundation;
- public governance, security, architecture, and change control;
- independently operable infrastructure research; and
- explicit hardware identity, product verification, and payment boundaries.

These layers are not equally mature, but they form one protocol-infrastructure
architecture rather than a website wrapped around a token contract.

## Engineering Thesis

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

## Project Scope and Continuity

IPI development is broader than the history of a single daemon repository. Its
public record is distributed across protocol-foundation evaluation, explorer
implementation, wallet models, RPC clients, network configuration, governance,
security, independent-infrastructure research, and hardware/product/payment
architecture. Some repositories were imported, rebuilt, or created at different
stages and therefore have different histories.

This is not a claim that IPI spent four continuous years writing a blockchain
core from zero. It is the narrower, verifiable claim that IPI is being developed
as a multi-component system, and that repository age or inherited history must
not be substituted for evidence of IPI-specific work.

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
