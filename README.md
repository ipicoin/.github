# IPI community standards

This repository is the public entry point for the
[IPI GitHub organization](https://github.com/ipicoin). It contains the
organization profile, contributor standards, governance rules, security policy,
roadmap, and the IPI Improvement Proposal process.

GitHub automatically uses supported community-health files from this repository
as defaults for organization repositories that do not define their own.
Repository-specific instructions always take precedence.

## Documentation

| Document | Purpose |
| --- | --- |
| [Organization profile](profile/README.md) | Public mission, project map, and entry points |
| [Architecture](ARCHITECTURE.md) | Target layers, trust boundaries, and current maturity |
| [Contributing](CONTRIBUTING.md) | How to discuss, build, test, and submit changes |
| [Code of Conduct](CODE_OF_CONDUCT.md) | Expected community behavior |
| [Security](SECURITY.md) | Private vulnerability reporting |
| [Support](SUPPORT.md) | Where to ask questions and report problems |
| [Governance](GOVERNANCE.md) | Roles and decision-making |
| [Maintainers](MAINTAINERS.md) | Access, review, and stewardship expectations |
| [Roadmap](ROADMAP.md) | Milestones and public exit criteria |
| [Licensing](LICENSING.md) | Licensing and upstream-attribution policy |
| [IPI proposals](ipi/README.md) | Protocol and governance proposal process |

## Proposal naming

An **IPI Improvement Proposal** uses the identifier
**IPI-####**. The process definition is [IPI-0000](ipi/IPI-0000.md), the first
technical principles proposal is [IPI-0001](ipi/IPI-0001.md), and new proposals
start from [the template](ipi/IPI-template.md).

## Project status

IPI is under active development and is not yet a production-ready public
network. A repository, endpoint, or testnet must not be presented as a stable
release unless its documentation explicitly says so and provides reproducible
verification evidence.

## Existing legal documents

Files under [statements/](statements/) and [translations/](translations/) are
preserved separately from the technical and community standards in this
repository. Their presence does not make them a current protocol specification
or a substitute for qualified legal review. Changes to those files require an
explicit legal review process.

## Historical and incubating material

The [knowledge/](knowledge/) tree and the root-level [workflows/](workflows/)
directory predate this community baseline and are preserved for traceability.
They are not canonical protocol specifications or active GitHub Actions.
Executable organization workflows live only under [.github/workflows/](.github/workflows/).
New normative protocol work belongs in an IPI proposal and an identified
implementation repository.
