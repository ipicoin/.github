# IPI — Independent Protocol Infrastructure

### Infrastructure for systems that can be independently operated, verified, and extended.

**Fast finality is not proof of independence.** We have not found a generally
applicable, independently reproducible basis for treating a low finality number
as evidence that a network is operationally independent. Finality describes how
quickly a network reaches a decision; it does not, by itself, reveal who can
verify that decision, who controls upgrades, where the infrastructure runs, or
whether users can leave without permission.

IPI is being built around a harder standard:

> **Independence must be observable, reproducible, and open to challenge.**

## What IPI is building

IPI is an open protocol stack for verifiable digital commerce and coordination.
The goal is to let communities and organizations run their own infrastructure,
hold their own keys, verify their own state, and extend the system through open
interfaces.

The intended result is not another hosted chain that users must trust from the
outside. It is a complete verification path — from node and wallet to product,
chip, checkout, payment, and receipt — that others can reproduce and operate
without IPI's permission.

The current engineering direction includes:

- native settlement on a Cosmos SDK and CometBFT protocol with EVM and CosmWasm
  execution;
- IBC interoperability and open RPC, REST, gRPC, and EVM interfaces;
- native account and key paths, including secp256k1 and P-256/R1 use cases;
- verifiable product passports, chip identities, attestations, and checkout;
- independently deployable node, wallet, explorer, faucet, indexer, monitoring,
  and terminal components; and
- transparent protocol change control through IPI Improvement Proposals.

This is an early-stage project. Public repositories currently contain a mix of
IPI code, active migrations, experiments, and attributed upstream forks. They
must not be treated as production-ready until a release is explicitly marked,
reproducibly built, tested, and documented as such.

## The independence standard

IPI evaluates independence across multiple dimensions instead of hiding it
behind one performance metric:

| Dimension | The question that must be answerable |
| --- | --- |
| Verification | Can an independent operator verify state from public data? |
| Control | Who holds keys and can change code, parameters, or access? |
| Operation | Can the system run without a mandatory private coordinator? |
| Reproducibility | Can a release be rebuilt and its provenance checked? |
| Governance | Are decisions, authority, and emergency powers visible? |
| Exit | Can users export, migrate, continue, or fork without permission? |
| Diversity | Are critical operators, implementations, and providers independent? |

The first specification of this model is
[IPI-0001: Verifiable Independence](/ipicoin/.github/blob/main/ipi/IPI-0001.md).

## Start here

- Understand the [target architecture and current maturity](/ipicoin/.github/blob/main/ARCHITECTURE.md).
- Read the [roadmap](/ipicoin/.github/blob/main/ROADMAP.md).
- See [how to contribute](/ipicoin/.github/blob/main/CONTRIBUTING.md).
- Propose a protocol change through the
  [IPI process](/ipicoin/.github/tree/main/ipi).
- Join an architectural or product conversation in
  [GitHub Discussions](https://github.com/orgs/ipicoin/discussions).
- Find issues marked
  [good first issue](https://github.com/search?q=org%3Aipicoin+label%3A%22good+first+issue%22+is%3Aopen&type=issues)
  or [help wanted](https://github.com/search?q=org%3Aipicoin+label%3A%22help+wanted%22+is%3Aopen&type=issues).
- Report vulnerabilities through the private process in
  [SECURITY.md](/ipicoin/.github/blob/main/SECURITY.md).

## Project map

| Area | Repository | Maturity |
| --- | --- | --- |
| Protocol node | [independency-daemon](https://github.com/ipicoin/independency-daemon) | Upstream-based; IPI consolidation in progress |
| Network configuration | [chainconfig](https://github.com/ipicoin/chainconfig) | Incubating |
| JavaScript wallet core | [wallet-core.js](https://github.com/ipicoin/wallet-core.js) | Experimental |
| Mobile wallet | [protocolix](https://github.com/ipicoin/protocolix) | Experimental |
| RPC services | [ipi-rpc](https://github.com/ipicoin/ipi-rpc) | Experimental |
| Explorer | [scan.ipi.io](https://github.com/ipicoin/scan.ipi.io) | Incubating |
| Community and governance | [.github](https://github.com/ipicoin/.github) | Active |

Repository maturity labels are deliberately conservative and will change only
with public evidence. The [roadmap](/ipicoin/.github/blob/main/ROADMAP.md)
defines the exit criteria for each major stage.

## How we work

We verify claims, build in public, preserve upstream attribution, document trust
assumptions, and prefer changes that make the system easier to reproduce and
operate independently. Architecture and governance changes are discussed before
they are standardized.

[Website](https://ipi.io) ·
[Discussions](https://github.com/orgs/ipicoin/discussions) ·
[Governance](/ipicoin/.github/blob/main/GOVERNANCE.md) ·
[IPI proposals](/ipicoin/.github/tree/main/ipi) ·
[Licensing](/ipicoin/.github/blob/main/LICENSING.md) ·
[Trademarks](/ipicoin/.github/blob/main/TRADEMARKS.md)
