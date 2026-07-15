# Contributing to IPI

Thank you for helping build infrastructure that people can operate and verify
for themselves. Contributions are welcome across protocol engineering,
security, documentation, product design, testing, operations, and research.

IPI is early-stage. Clear problem statements, reproducible evidence, and small
reviewable changes are more valuable than broad claims or large undocumented
rewrites.

## Choose the right path

- Ask usage and architecture questions in
  [GitHub Discussions](https://github.com/orgs/ipicoin/discussions).
- Report a reproducible bug in the repository where it occurs.
- Suggest a bounded enhancement with the feature request template.
- Use an [IPI Improvement Proposal](ipi/README.md) for protocol behavior,
  compatibility, governance, security assumptions, or changes spanning multiple
  repositories.
- Follow [SECURITY.md](SECURITY.md) instead of opening a public issue for a
  suspected vulnerability.

If you are unsure where a change belongs, start a Discussion. A maintainer can
help narrow the scope before implementation work begins.

## Before writing code

1. Search existing issues, Discussions, pull requests, and IPI proposals.
2. Confirm the repository maturity and read its local contributing guide.
3. For a substantial change, agree on the problem and acceptance criteria
   before opening a large pull request.
4. Check [LICENSING.md](LICENSING.md). Do not copy code, media, or text unless
   its license is compatible and its provenance can be preserved.

## Development workflow

1. Fork the repository and branch from its current default branch.
2. Keep one logical change per branch.
3. Add or update tests for behavior changes.
4. Update user, operator, API, and migration documentation where applicable.
5. Run the repository's documented checks locally.
6. Open a pull request using the provided template and link the issue or IPI.

Use concise commit subjects in the imperative mood, for example:

~~~text
feat(wallet): verify network identity before signing
fix(node): reject inconsistent chain configuration
docs(ipi): define evidence for operator diversity
~~~

Conventional Commit prefixes are encouraged but not required. A clean,
explainable history is required.

## Pull request expectations

A reviewable pull request:

- explains the problem, not only the implementation;
- states how the result was verified;
- identifies compatibility, migration, security, and operational effects;
- avoids unrelated formatting or generated-file churn;
- contains no credentials, personal data, private endpoints, or chain keys;
- preserves copyright notices and upstream attribution; and
- does not make performance, decentralization, security, or readiness claims
  without reproducible evidence.

Draft pull requests are encouraged for early technical feedback. A pull request
is ready to merge only when its checks pass, review conversations are resolved,
and the required reviewers approve it.

## Tests and evidence

Tests should be deterministic and should fail for the behavior they protect.
Performance claims require the workload, configuration, hardware, raw result,
and reproduction procedure. Network-independence claims require evidence under
[IPI-0001](ipi/IPI-0001.md); latency alone is not sufficient.

Screenshots can support a user-interface change but do not replace behavioral
tests. For protocol changes, include upgrade and rollback considerations.

## AI-assisted contributions

The contributor remains responsible for every submitted line. Review generated
changes for correctness, licensing, security, hidden dependencies, and
unnecessary scope. State material use of generated code or content in the pull
request when it affects provenance or review.

## Review and decision-making

Maintainers evaluate correctness, safety, scope, evidence, compatibility, and
alignment with the accepted roadmap. Review is technical, not personal.
Maintainers may ask that a broad pull request be split or moved into an IPI.

Submitting a contribution does not guarantee acceptance. Decisions follow
[GOVERNANCE.md](GOVERNANCE.md), and conduct follows
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Licensing of contributions

Each repository must state its own license. By submitting a contribution, you
represent that you have the right to submit it under that repository's stated
terms. If a repository has no explicit license, do not assume permission to
reuse or redistribute its contents; open a licensing issue before making a
substantial contribution.
