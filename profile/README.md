# IPI — Independent Protocol Infrastructure

**A public, multi-layer protocol infrastructure ecosystem connecting network
state, open APIs, self-custody clients, independent verification, governance,
and physical/digital commerce integration.**

IPI organizes public engineering across blockchain and network foundations,
wallet and key infrastructure, a block explorer, RPC clients, node and validator
integration, EVM and CosmWasm interfaces, governance and security processes,
product identity and secure-element research, checkout/payment architecture,
and independently operable infrastructure.

The repositories are parts of one verification path: protocol state is exposed
through open interfaces, clients authorize or inspect changes, and governance
and evidence specifications make control and trust boundaries explicit.

## Engineering Evidence

| Layer | Publicly verifiable implementation | Strongest evidence | Current role |
| --- | --- | --- | --- |
| Explorer | Browser code for blocks, transactions, accounts, validators, search, and native Cosmos queries | [`explorer.js`](https://github.com/ipicoin/scan.ipi.io/blob/main/explorer.js) | Implemented and publicly tested |
| EVM inspection | EVM JSON-RPC query, transaction, receipt, address, balance, nonce, and bytecode inspection | [`explorer.js`](https://github.com/ipicoin/scan.ipi.io/blob/main/explorer.js), [`evm.html`](https://github.com/ipicoin/scan.ipi.io/blob/main/evm.html) | Implemented explorer integration |
| Wallet core | Wallet, address, request, transaction, and contract models plus configurable Bech32 validation | [`src/models`](https://github.com/ipicoin/wallet-core.js/tree/main/src/models), [`tests`](https://github.com/ipicoin/wallet-core.js/tree/main/tests) | Tested JavaScript model layer |
| Mobile environment | Checked-in Capacitor Android and iOS application projects with IPI package identities | [`android`](https://github.com/ipicoin/protocolix/tree/main/android), [`ios`](https://github.com/ipicoin/protocolix/tree/main/ios) | Cross-platform integration environment |
| RPC/API clients | Cosmos, IBC, Tendermint, and CosmWasm protobuf inputs, code generators, and two generated TypeScript client trees | [`proto`](https://github.com/ipicoin/ipi-rpc/tree/main/proto), [`gRPC-Web`](https://github.com/ipicoin/ipi-rpc/tree/main/codegen_grpc_web), [`gRPC-Gateway`](https://github.com/ipicoin/ipi-rpc/tree/main/codegen_grpc_gateway) | RPC transport research workspace |
| CosmWasm surface | Generated CosmWasm query/transaction clients and an attributed `wasmd` node foundation | [`CosmWasm clients`](https://github.com/ipicoin/ipi-rpc/tree/main/codegen_grpc_web/cosmwasm), [`independency-daemon`](https://github.com/ipicoin/independency-daemon) | Client integration and node-foundation work |
| Network configuration | Coherent IPI chain, denomination, Bech32, and wallet metadata with an automated test | [`config.json`](https://github.com/ipicoin/chainconfig/blob/main/config.json), [`config.test.js`](https://github.com/ipicoin/chainconfig/blob/main/test/config.test.js) | Historical network configuration evidence |
| Governance and security | Public architecture, security policy, change control, roadmap, and validated IPI Improvement Proposal framework | [`GOVERNANCE.md`](https://github.com/ipicoin/.github/blob/main/GOVERNANCE.md), [`SECURITY.md`](https://github.com/ipicoin/.github/blob/main/SECURITY.md), [`IPI-0000`](https://github.com/ipicoin/.github/blob/main/ipi/IPI-0000.md) | Active public framework |
| Product identity and hardware keys | Specified boundaries for P-256/R1, WebAuthn, NFC, secure elements, attestation, privacy, and replay protection | [`ARCHITECTURE.md`](https://github.com/ipicoin/.github/blob/main/ARCHITECTURE.md), [`NTAG 424 reference`](https://github.com/ipicoin/nikeee___node-ntag424) | Hardware-backed identity research direction |

## What Exists Today

| Area | Repository | Current role |
| --- | --- | --- |
| Governance and architecture | [`.github`](https://github.com/ipicoin/.github) | Public architecture, security, governance, roadmap, and IPI proposal framework |
| Explorer | [`scan.ipi.io`](https://github.com/ipicoin/scan.ipi.io) | IPI block, transaction, account, validator, native Cosmos, and EVM inspection interface |
| Wallet core | [`wallet-core.js`](https://github.com/ipicoin/wallet-core.js) | JavaScript wallet/account models and configurable Cosmos-compatible address validation |
| Mobile wallet environment | [`protocolix`](https://github.com/ipicoin/protocolix) | Capacitor Android/iOS application environment for future wallet and hardware-key integration |
| RPC tooling | [`ipi-rpc`](https://github.com/ipicoin/ipi-rpc) | gRPC-Web and gRPC-Gateway client-generation workspace for IPI RPC/API integration research |
| Network configuration | [`chainconfig`](https://github.com/ipicoin/chainconfig) | Tested IPI wallet/chain metadata retained as a historical network configuration record |
| Protocol node foundation | [`independency-daemon`](https://github.com/ipicoin/independency-daemon) | Cosmos SDK, CometBFT, IBC, and CosmWasm upstream foundation used to define the IPI node integration boundary |
| Website and documentation | [`www.ipi.io`](https://github.com/ipicoin/www.ipi.io) | Astro website and Starlight documentation source for public IPI interfaces and concepts |

## Architecture

### Demonstrated in public repositories today

```text
Attributed Cosmos / CometBFT / CosmWasm node foundation
                         ↓
Generated RPC clients + direct Cosmos / CometBFT / EVM query paths
                         ↓
Explorer + tested wallet models + Android/iOS application projects
                         ↓
Public governance + security + evidence specifications
```

This is a map of public components, not a claim that every layer already forms
a released end-to-end system. The explorer, wallet model tests, generated RPC
surfaces, native application projects, and governance framework can be inspected
today; their integration maturity is recorded below.

### Target architecture

```text
Protocol / Node
→ EVM + CosmWasm execution
→ RPC / REST / gRPC / EVM JSON-RPC
→ Wallet + Explorer
→ Product Identity / P-256 / NFC / Secure Element
→ Checkout / Payment / Receipt
→ Independent Verification
```

These layers belong together because consensus produces state, open APIs expose
it, wallets authorize changes, explorers enable independent inspection,
hardware and product interfaces bind external events to explicit attestations,
and checkout/receipt flows can turn settlement into a checkable record. The
[architecture document](https://github.com/ipicoin/.github/blob/main/ARCHITECTURE.md)
separates current implementation from target interfaces in detail.

## More Than a Token Layer

The public organization contains separate repositories for protocol and network
foundations, wallet software, native mobile projects, explorer code, RPC/API
client generation, governance and security, and hardware-backed product-identity
research. Much of the low-level protocol foundation is established upstream
open source; the broader public system and its IPI-specific boundaries are not
equivalent to a token contract plus a website.

## Engineering thesis

IPI is designed around infrastructure that others can inspect, replace, and
operate:

- **Independence:** a hosted endpoint or organization account must not silently
  become the only way to operate or verify the system.
- **Self-custody:** keys and signing intent belong at the user-controlled edge.
- **Independent operation:** nodes, clients, explorers, and optional services
  need documented deployment, recovery, and exit paths.
- **Reproducibility:** protocol claims should resolve to source revisions,
  dependency locks, build procedures, tests, and observable evidence.
- **Open interfaces:** RPC, REST, gRPC, EVM JSON-RPC, events, and portable data
  formats are boundaries that independent implementations can reproduce.
- **Transparent governance:** protocol and trust changes belong in public,
  versioned proposals with security and compatibility analysis.
- **Hardware-backed identity direction:** P-256/R1, NFC, and secure-element work
  is treated as a separate attestation and privacy problem, with secrets kept
  off-chain.

## Upstream foundations

IPI deliberately evaluates established open-source foundations including
Cosmos SDK, CometBFT, CosmWasm, `wasmd`, Ethereum tooling, WebAuthn, and secure
hardware libraries. Their use provides reviewed interfaces, interoperability,
and visible development history. Licenses and provenance remain explicit; IPI
does not claim upstream code as original work.

The public audit found that most forks have no IPI commits. The node tracking
fork currently adds provenance documentation and CI hardening rather than an
IPI consensus or application delta. IPI-specific public evidence is concentrated
in the explorer, wallet models and tests, governance and architecture, network
configuration, website, and integration work. See the
[complete repository audit](https://github.com/ipicoin/.github/blob/main/REPOSITORY_AUDIT.md)
for the per-repository boundary.

## Development Status

This is an early-stage project. Public repositories currently contain a mix of
IPI code, active migrations, experiments, and attributed upstream forks. They
must not be treated as production-ready until a release is explicitly marked,
reproducibly built, tested, and documented as such.

Precise current classifications:

- `scan.ipi.io` is an implemented explorer under active development.
- `wallet-core.js` is a tested model/validation layer; signing, transaction,
  fee, and recovery workflows remain incomplete.
- `protocolix` is a cross-platform prototype scaffold; wallet, NFC, and
  secure-key behavior is not implemented in its public source.
- `ipi-rpc` is an upstream-derived RPC client-generation research workspace;
  it is not an IPI RPC server.
- `independency-daemon` is an attributed upstream node foundation; a public
  IPI-specific node release and validator/sentry deployment remain incomplete.
- `chainconfig` is tested historical metadata, not a canonical current network
  identity.
- product identity, secure-element attestation, checkout, payment, and receipt
  remain research or target-architecture layers without public IPI-specific
  implementations.

The public repositories do not yet contain a versioned, reproducible artifact
that ties IPI block production, native EVM transfers, EVM contract deployment,
or CosmWasm upload/execution to a specific public IPI node revision. Those
execution claims are therefore not presented as completed evidence here.

IPI's development record spans protocol-foundation evaluation, network
configuration, explorer and wallet work, RPC clients, governance, security,
infrastructure research, hardware/product-identity architecture, payments, and
migrations or rebuilds. This is not a claim that the current public GitHub proves
four continuous years of original blockchain-core development.

The [roadmap](https://github.com/ipicoin/.github/blob/main/ROADMAP.md) defines
the evidence required before stronger maturity claims.

## Start here

[Explorer](https://github.com/ipicoin/scan.ipi.io) ·
[Architecture](https://github.com/ipicoin/.github/blob/main/ARCHITECTURE.md) ·
[Repository audit](https://github.com/ipicoin/.github/blob/main/REPOSITORY_AUDIT.md) ·
[Governance](https://github.com/ipicoin/.github/blob/main/GOVERNANCE.md) ·
[IPI proposals](https://github.com/ipicoin/.github/tree/main/ipi) ·
[Roadmap](https://github.com/ipicoin/.github/blob/main/ROADMAP.md) ·
[Security](https://github.com/ipicoin/.github/blob/main/SECURITY.md) ·
[Website](https://ipi.io)
