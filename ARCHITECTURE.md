# IPI Architecture

IPI is designed as a multi-layer protocol infrastructure ecosystem. This
document separates the intended system architecture from the evidence currently
available in public repositories.

## System intent

IPI connects protocol settlement, user-controlled signing, open query
interfaces, independent operation, and verifiable digital or physical commerce.
No hosted explorer, wallet, API, issuer, terminal, or project account should
silently become the only source of truth.

## Layered system map

```text
People and independent operators
        │ sign · query · verify · deploy · recover
        ▼
Wallet · Terminal · Explorer · Node CLI · External applications
        │ RPC · REST · gRPC · EVM JSON-RPC · events
        ▼
Accounts · Settlement · EVM compatibility · CosmWasm contracts
        │ deterministic state and explicit trust boundaries
        ▼
Cosmos SDK · CometBFT · peer-to-peer network · storage
        │
        ├── IBC and separately specified external verification
        └── optional services: indexer · faucet · monitoring · routing

Product identity · chip attestation · checkout · payment · receipt
        connect through specified application interfaces;
        they are not implemented consensus claims merely because they appear here.
```

The intended end-to-end path can be summarized as:

```text
Protocol / Node → RPC/API → Wallet / Explorer
→ Product Identity / Secure Element → Checkout / Payment → Verification
```

## Current public implementation map

| Layer | Public source evidence | Current classification |
| --- | --- | --- |
| Protocol/node | [`independency-daemon`](https://github.com/ipicoin/independency-daemon) | `wasmd` tracking foundation; no IPI consensus/application changes |
| Network metadata | [`chainconfig`](https://github.com/ipicoin/chainconfig) | Tested legacy wallet configuration; not canonical current network identity |
| RPC/API clients | [`ipi-rpc`](https://github.com/ipicoin/ipi-rpc) | Upstream-derived gRPC-Web/gRPC-Gateway comparison and generated TypeScript clients |
| Explorer | [`scan.ipi.io`](https://github.com/ipicoin/scan.ipi.io) | Implemented native Cosmos and EVM query interface; public CI passes |
| Wallet model layer | [`wallet-core.js`](https://github.com/ipicoin/wallet-core.js) | Models and Bech32 validation tested; signing and transfer operations incomplete |
| Mobile client | [`protocolix`](https://github.com/ipicoin/protocolix) | Capacitor Android/iOS scaffold; wallet behavior absent |
| Governance/security | [`.github`](https://github.com/ipicoin/.github) | Public process, policies, architecture, roadmap, and automated validation |
| Independent deployment | [`hq-spacecraft`](https://github.com/ipicoin/hq-spacecraft) | Research scaffold; most Compose definitions are placeholders |
| Product/chip identity | Architecture and upstream secure-hardware reference forks | Research direction; no IPI-specific public implementation |
| Checkout/payment/receipt | Roadmap and upstream terminal concept forks | Concept stage; no executable public IPI integration |

This table is limited to public evidence. Private, local, or hosted behavior is
not promoted to an implementation claim here.

## Component boundaries

### Protocol node and validator operation

The node validates deterministic state transitions and participates in
consensus. The public research foundation is CosmWasm `wasmd`, which supplies
Cosmos SDK, CometBFT, IBC, and CosmWasm capabilities upstream. An IPI node
release still needs explicit IPI modules and parameters, canonical genesis
binding, upgrade and recovery procedures, validator/sentry topology, versioned
artifacts, and compatibility tests.

### RPC, APIs, explorer, and indexers

RPC, REST, gRPC, EVM JSON-RPC, events, and indexers expose protocol data; they do
not define canonical state. Responses should include enough network identity,
height, and provenance for a caller to repeat important queries through another
provider or a local node.

The public explorer implements direct CometBFT/Cosmos and EVM query paths. The
RPC research client compares two generated Cosmos transports. Neither is a
substitute for authenticated state verification by a node.

### Accounts, keys, and wallets

Users control signing authority. Wallets must verify network identity, display
the exact action being authorized, protect recovery material, and support
provider replacement. The public JavaScript wallet repository currently proves
only its model/configuration tests and Bech32 validation; transaction signing,
fees, endpoint verification, recovery, and release security remain unfinished.

P-256/R1, WebAuthn, NFC, and secure-element paths require separate compatibility
and hardware threat models. Reference forks are research inputs, not IPI
implementations or security attestations.

### Products, chips, and attestations

The intended application layer may record product identifiers, issuers,
bindings, lifecycle events, and revocation. Symmetric chip secrets and private
business or personal data must remain off-chain. Secure-chip verification
belongs behind a specified attestation boundary with replay protection, issuer
rotation, privacy analysis, and failure handling.

No IPI-specific product or secure-element implementation is currently public.

### Checkout, payment, and receipts

Checkout should be a deterministic application flow around explicit cart,
pricing, authorization, settlement, and receipt states. A terminal must provide
safe, explainable degraded behavior when a network or optional service is
unavailable.

Current public terminal/payment forks are concept or hardware scaffolds and do
not implement this IPI flow.

### Interoperability and external systems

IBC, anchoring, bridges, wrapped assets, routing, custody, AMMs, external
storage, and oracles introduce independent trust boundaries. Each integration
requires a versioned specification, threat model, accounting invariants,
key-holder disclosure, verification method, and shutdown or migration path.
An upstream reference fork does not establish an IPI integration.

## Upstream foundation and IPI-specific work

Using Cosmos SDK, CometBFT, CosmWasm, Ethereum tooling, and other established
open-source components provides interoperable foundations and reviewable
history. IPI preserves their licenses and does not claim their code as original.

The public organization audit found:

- 26 public forks with zero commits ahead of upstream;
- one tracking fork, `independency-daemon`, with two IPI commits limited to
  provenance and CI hardening; and
- original IPI work concentrated in the explorer, wallet model/tests,
  governance and architecture, website, configuration, and integration
  research repositories.

See [`REPOSITORY_AUDIT.md`](REPOSITORY_AUDIT.md) for the per-repository evidence.

## Design rules

1. **Verify at the edge.** A wallet, operator, or application should be able to
   check important claims without trusting the service that presented them.
2. **Keep consensus deterministic.** External calls, private services, and
   nondeterministic inputs do not belong inside consensus state transitions.
3. **Make authority explicit.** Keys, allowlists, issuers, upgrades, recovery,
   and emergency actions are documented control points.
4. **Keep secrets off-chain.** Publish proofs and lifecycle state, not signing
   secrets or unnecessary personal and commercial data.
5. **Treat interoperability as a new trust model.** A connection does not inherit
   the security or independence of either side automatically.
6. **Prefer replaceable services.** Hosted convenience needs an independent
   provider or local-operation path.
7. **Design the exit before launch.** Recovery, migration, shutdown, and
   continuity are protocol requirements.
8. **Label evidence precisely.** Implemented, inherited, generated, configured,
   tested, hosted, and planned are different claims.

## Change control

Material changes to these boundaries require an
[IPI Improvement Proposal](ipi/README.md). Implementation work may precede an
accepted proposal, but it must not silently redefine normative behavior or
claim maturity unsupported by public evidence.
