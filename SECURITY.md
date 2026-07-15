# Security Policy

Security reports are welcome. Please give maintainers a reasonable opportunity
to investigate and coordinate a fix before public disclosure.

## Report a vulnerability privately

Do not open a public issue, Discussion, or pull request for a suspected
vulnerability.

1. Use the affected repository's **Report a vulnerability** form under its
   Security tab when available.
2. If private vulnerability reporting is unavailable, email
   [hello@ipi.io](mailto:hello@ipi.io) with the subject
   “SECURITY: repository and short summary”.

Include:

- the affected repository, revision, component, and environment;
- a clear description of the behavior and realistic impact;
- minimal reproduction steps or a proof of concept;
- whether the issue has been disclosed elsewhere;
- any suggested mitigation; and
- a safe way to contact you.

Encrypt sensitive material before sending it by ordinary email and ask for a
secure transfer method if needed. Never send private keys, seed phrases,
production credentials, or unrelated personal data.

## What to expect

The project aims to acknowledge a complete report within five business days.
Validation, remediation, release, and disclosure timing depend on severity and
affected dependencies. The reporter will receive updates when there is
meaningful progress. No bug bounty or payment is promised unless a written
program explicitly says otherwise.

## Supported versions

IPI is pre-release software. Unless a repository states otherwise, only its
current default branch and most recent explicitly supported release receive
security fixes. Historical branches, experiments, demonstrations, and testnets
may be changed or retired without backports.

No public endpoint, testnet, wallet, terminal, bridge, or contract should be
assumed production-safe merely because it is reachable.

## Good-faith research

Use only accounts and assets you control. Avoid privacy violations, data
destruction, service degradation, denial of service, social engineering,
physical attacks, and access beyond what is necessary to demonstrate the issue.
Stop and report if testing exposes private data or creates risk for others.

The project will treat good-faith research that follows this policy as an effort
to improve IPI. This policy does not authorize testing of third-party services
or infrastructure.

## Operational secrets

If a secret appears in a repository, treat it as compromised even after the
file is removed. Notify the project privately so the credential can be revoked,
rotated, and investigated. Rewriting Git history is not a substitute for
rotation.
