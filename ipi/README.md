# IPI Improvement Proposals

An **IPI Improvement Proposal** is a versioned design document for changes that
affect the IPI protocol, public interfaces, compatibility, security model,
governance, or multiple repositories.

Proposal identifiers use **IPI-####**. “IPI” in this context means
**IPI Improvement Proposal**.

## Read first

- [IPI-0000 — IPI Improvement Proposal Process](IPI-0000.md)
- [IPI-0001 — Verifiable Independence](IPI-0001.md)
- [IPI proposal template](IPI-template.md)

## When an IPI is required

Use an IPI for:

- consensus, state-machine, transaction, account, or cryptographic changes;
- stable RPC, API, data-format, wallet, contract, or interoperability changes;
- network upgrades and compatibility policy;
- new trust assumptions, privileged roles, or security boundaries;
- project-wide governance and release policy; or
- a coordinated change spanning multiple repositories.

An ordinary issue or pull request is usually enough for a local bug fix,
refactor, test, documentation correction, or implementation of an already
accepted proposal.

## Proposal index

| IPI | Title | Type | Status |
| ---: | --- | --- | --- |
| [0000](IPI-0000.md) | IPI Improvement Proposal Process | Process | Active (bootstrap) |
| [0001](IPI-0001.md) | Verifiable Independence | Standards Track / Core | Draft |

## Contributing a proposal

1. Start a focused
   [GitHub Discussion](https://github.com/ipicoin/.github/discussions) describing
   the problem, constraints, and alternatives.
2. Establish that an IPI is the right level of change and identify affected
   maintainers.
3. Copy [IPI-template.md](IPI-template.md) to a draft named
   <code>IPI-draft-short-title.md</code>.
4. Complete the motivation, specification, security, compatibility, test,
   operational, and independence sections.
5. Open a pull request and link the Discussion.
6. An editor assigns the next number when the proposal meets the minimum
   editorial requirements. A number does not mean acceptance.

The repository history, proposal metadata, linked Discussion, and implementation
pull requests together form the public decision record.
