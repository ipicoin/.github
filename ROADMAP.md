# IPI Roadmap

IPI's goal is a protocol stack for digital systems that can be independently
operated, verified, and extended. This roadmap separates that goal from the
evidence currently available.

It is a sequence of verification gates, not a promise of dates, token value,
performance, or production readiness. Priorities can change through issues and
[IPI Improvement Proposals](ipi/README.md).

## Stage 0 — Make the project legible

**Objective:** a new contributor can understand what exists, what is inherited,
what is planned, and how decisions are made.

- Publish community, security, governance, and contribution standards.
- Establish the IPI proposal process.
- Inventory repositories as active, experimental, upstream fork, archived, or
  license pending.
- Preserve upstream provenance and resolve licenses for original work.
- Publish a canonical architecture and repository map.

**Exit evidence:** every highlighted repository has an owner, maturity label,
license status, build instructions, security contact, and issue tracker.

## Stage 1 — Reproducible protocol baseline

**Objective:** consolidate the active IPI node into a reviewable public
baseline.

- Document the Cosmos SDK, CometBFT, Cosmos EVM, CosmWasm, and IBC compatibility
  matrix.
- Reproduce clean genesis, node build, startup, state verification, and upgrade
  procedures.
- Define chain identity, account formats, native key paths, and public
  interfaces.
- Separate upstream code from IPI-specific modules and changes.
- Add deterministic tests, dependency scanning, release artifacts, checksums,
  and software-bill-of-materials generation.

**Exit evidence:** an independent contributor can build the same source, start a
node from documented public data, verify network identity, and reproduce the
required compatibility tests.

## Stage 2 — Verifiable commerce primitives

**Objective:** make physical and digital commerce claims independently
verifiable without placing secret material on-chain.

- Specify product passports, product and chip registries, issuers, revocation,
  and lifecycle rules.
- Define P-256/R1 and hardware-backed identity use cases and their threat models.
- Build checkout, receipts, wallet signing, and terminal flows around explicit
  state transitions.
- Specify privacy boundaries and the separation between public proofs and
  private business or personal data.
- Test ordinary NFC tags before introducing secure-chip attestation paths.

**Exit evidence:** public specifications, test vectors, threat models, and
end-to-end tests demonstrate the same result across independently implemented
clients.

## Stage 3 — Independent operation

**Objective:** remove hidden operational dependencies.

- Publish node, wallet, explorer, faucet, indexer, terminal, monitoring, snapshot,
  and recovery procedures.
- Support independent bootstrap and state verification.
- Document all privileged keys, coordinators, infrastructure providers, and
  emergency controls.
- Measure operator and provider diversity without converting it into a single
  misleading score.
- Exercise backup, restore, migration, degraded-mode, and exit procedures.

**Exit evidence:** at least two unrelated operators reproduce the deployment
from public documentation and can continue verification through a simulated
loss of one project-operated service.

## Stage 4 — Interoperability with explicit trust

**Objective:** connect systems without hiding new trust assumptions.

- Harden IBC paths and cross-system identity.
- Specify Bitcoin anchoring and independently verify inclusion and continuity.
- Evaluate asset wrapping, routing, and liquidity only with public threat models,
  custody models, accounting invariants, and failure procedures.
- Reject “trustless” or “independent” labels that are not supported by
  reproducible evidence.

**Exit evidence:** each integration publishes its trust boundaries, key holders,
failure modes, verification procedure, and safe shutdown or migration path.

## Stage 5 — Community-operated releases

**Objective:** make IPI maintainable without dependence on one person or
organization.

- Grow independent maintainers and component reviewers.
- Run public release candidates and an externally operated testnet.
- Commission security reviews for production-bound components.
- Publish reproducible governance, release, incident, and upgrade records.
- Establish a stable compatibility policy and long-term maintenance process.

**Exit evidence:** releases receive independent review, multiple operators and
implementations verify the network, governance records are public, and no
single undocumented service is required for normal operation.

## Current focus

The immediate focus is Stage 0 and Stage 1. Work from later stages can remain in
experiments, but it must not be marketed as accepted or production-ready before
its earlier dependencies and exit evidence are complete.
