# Working in the IPI GitHub organization

These instructions apply to automated coding agents and human contributors
working in this repository.

## Mission

Help IPI become protocol infrastructure that unrelated people can operate,
verify, reproduce, and extend. Prefer working evidence over slogans. Keep the
current distinction between implemented, experimental, planned, and unknown
behavior visible.

Read before changing the repository:

1. [README.md](README.md)
2. [CONTRIBUTING.md](CONTRIBUTING.md)
3. [GOVERNANCE.md](GOVERNANCE.md)
4. [SECURITY.md](SECURITY.md)
5. [LICENSING.md](LICENSING.md)
6. [IPI-0000](ipi/IPI-0000.md) and, for independence claims,
   [IPI-0001](ipi/IPI-0001.md)

More specific AGENTS.md files override this file within their directories.

## Non-negotiable safeguards

- Never publish a secret, seed phrase, private key, access token, recovery code,
  private endpoint, customer record, or unrelated personal data.
- Never push directly to a protected default branch. Use a focused feature
  branch and a pull request.
- Do not delete repositories, branches, tags, releases, or history unless the
  user explicitly authorizes that exact destructive action.
- Do not rewrite public history to hide a leaked secret; rotate the secret first
  and follow the private security process.
- Do not relicense or remove third-party attribution without documented rights.
- Do not describe a component as production-ready, independent, audited,
  decentralized, or performance-leading without reproducible evidence.
- Preserve unrelated user changes in a dirty working tree.

## Bringing code into an IPI repository

Before publishing code:

1. Identify the correct destination repository and read its local instructions.
2. Inspect Git status, branches, remotes, commit history, and existing user
   changes.
3. Inventory licenses, upstream origins, generated files, large binaries, and
   contributor notices.
4. Scan the complete candidate tree and history for credentials and private
   information without printing discovered secret values.
5. Confirm that the destination license is explicit and compatible. If it is
   missing or uncertain, stop before publishing and open a licensing decision.
6. Run the repository's tests, linters, builds, and security checks.
7. Create a narrowly named branch from the current default branch.
8. Make small attributable commits with clear subjects.
9. Push only the feature branch and open a pull request using the template.
10. Link the relevant issue, Discussion, or IPI proposal and include exact test
    results, compatibility effects, known limitations, and rollback notes.

If the source is an existing Git repository, preserve its useful history and
upstream relationship instead of copying an unattributed snapshot. Never merge
unrelated histories merely to make a push succeed.

## Change classification

Use an ordinary pull request for local fixes, tests, documentation, and
implementation of an already accepted design. Start or update an IPI
Improvement Proposal for consensus, cryptography, accounts, public interfaces,
compatibility, governance, trust assumptions, or coordinated changes across
repositories.

Security-sensitive work follows [SECURITY.md](SECURITY.md) and may require a
private fork or security advisory instead of a public branch.

## Required validation

For this repository, run:

~~~shell
python3 scripts/check_community.py
git diff --check
~~~

For another repository, run every check documented there. Do not claim a check
passed if it was skipped, unavailable, flaky, or run against a different
revision.

## Pull request handoff

The final handoff must state:

- the branch and commit;
- the files and behavior changed;
- the exact validation performed and its result;
- security, privacy, license, migration, and operational effects;
- anything not verified; and
- the next safe action required from a maintainer.

Do not merge your own material change as its only reviewer unless an
organization owner has explicitly authorized a documented bootstrap change and
the branch rules allow it. If the project does not yet have an independent
reviewer, keep technical proposals in Draft, state the limitation plainly, and
record the bootstrap authorization in the pull request.
