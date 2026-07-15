# IPI Architecture

This document describes the target IPI system and the boundaries contributors
must preserve. It is not a claim that every component is complete or public.
Current maturity is recorded separately from the target architecture.

## System intent

IPI connects protocol settlement to independently verifiable digital and
physical commerce. A user should be able to hold a key, sign through a wallet
or terminal, verify the network through a node they choose, and verify product
or receipt claims without trusting one project-operated web service.

## Target layers

~~~text
People and independent operators
        |
        | sign, query, verify, operate
        v
Wallets · Terminal · Explorer · Node CLI · External applications
        |
        | RPC · REST · gRPC · EVM JSON-RPC · events
        v
Protocol and application state
Accounts · Settlement · EVM · CosmWasm · Products · Chips · Checkout
        |
        | deterministic state transitions
        v
Cosmos SDK · CometBFT consensus · storage · peer-to-peer network
        |
        +---------------- IBC and explicitly modeled external verification

Optional services: indexer · faucet · monitoring · attestation verifier
                   anchoring · notification and routing adapters
~~~

Optional services must not silently become the only verification path. Their
outputs should be derivable from, authenticated by, or explicitly separated
from protocol state.

## Component boundaries

### Protocol node

The node is responsible for deterministic validation and state transitions.
The engineering baseline combines Cosmos SDK and CometBFT with EVM and
CosmWasm execution. Consensus-critical dependencies, activation, genesis, and
upgrades require versioned specifications and compatibility tests.

### Accounts, keys, and wallets

Users control signing authority. Wallets must verify network identity, show the
action being authorized, and avoid depending on a single project RPC. Native
secp256k1 and P-256/R1 paths must have explicit compatibility and hardware
threat models.

### Products, chips, and attestations

Public state can record identifiers, issuers, bindings, lifecycle, and
revocation. Symmetric chip secrets and private business or personal data must
not be published on-chain. Secure-chip verification belongs behind a specified
attestation boundary with replay protection, issuer rotation, and failure
handling.

### Checkout and receipts

Checkout is a deterministic application flow, not a second source of monetary
truth. Cart, pricing, authorization, settlement, and receipt state transitions
must be separately testable. Terminals must continue to provide a safe,
explainable result when the network or an optional service is unavailable.

### Explorers, indexers, and public APIs

These components make authenticated protocol data usable; they do not define
canonical state. Responses should expose network identity, height, provenance,
and enough information to repeat important queries against another provider or
local node.

### Interoperability and anchoring

IBC, anchoring, bridges, wrapped assets, routing, custody, and external oracles
introduce different trust boundaries. Each integration needs its own IPI,
threat model, accounting invariants, key-holder disclosure, independent
verification method, and shutdown or migration path.

## Current maturity

| Capability | Current evidence | Public milestone |
| --- | --- | --- |
| Cosmos SDK / CometBFT node | Active integration baseline has built and produced blocks | Consolidated source and reproducible public build |
| EVM execution | Native value transfer and a demonstration contract have been exercised | Published compatibility tests and release artifacts |
| CosmWasm execution | A demonstration contract has been uploaded and executed | Published compatibility matrix and deterministic test suite |
| Wallet, explorer, faucet, status | Testnet-facing implementations exist | Versioned source, threat models, and independent deployment |
| Terminal and ordinary NFC checkout | Local application flow and physical tag tests exist | Public source, reproducible build, and end-to-end protocol integration |
| Product and secure-chip identity | Separate experimental work exists | Reviewed specifications, test vectors, and integrated module |
| IBC interoperability | Part of the protocol direction | Public end-to-end compatibility evidence |
| Bitcoin anchoring, wrapping, and routing | Planned research | Separate accepted IPIs before production implementation |

Evidence from a private or local integration is useful engineering input but not
a public release. The [roadmap](ROADMAP.md) defines the gates for changing these
labels.

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
6. **Prefer replaceable services.** Hosted convenience must have an independent
   provider or local-operation path.
7. **Design the exit before the launch.** Recovery, migration, shutdown, and
   continuity are protocol requirements.

## Change control

Material changes to these boundaries require an
[IPI Improvement Proposal](ipi/README.md). An implementation pull request must
link the proposal and cannot silently redefine its normative behavior.
