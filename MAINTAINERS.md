# IPI Maintainer Policy

Maintainers are stewards of defined components, not owners of community work.
Their responsibility is to keep contributions reviewable, releases verifiable,
and authority narrow enough that the project can survive individual departures.

## Becoming a maintainer

A candidate should demonstrate:

- sustained, high-quality contributions in the relevant area;
- reliable review and respectful communication;
- sound security, compatibility, and licensing judgment;
- willingness to document decisions and help other contributors grow; and
- availability consistent with the component's maintenance needs.

Nomination should happen publicly. Granting write or admin access requires
approval from at least two existing maintainers or, while the project has fewer
than two independent maintainers, an organization owner plus a documented plan
to remove that bootstrap exception.

## Access rules

- Use an individual GitHub account, a unique credential, and two-factor
  authentication.
- Do not share passwords, access tokens, signing keys, or recovery codes.
- Grant the least privilege needed for the role.
- Use pull requests for normal changes; do not bypass branch rules for
  convenience.
- Keep release and infrastructure credentials outside source repositories.
- Review access after role changes and at least every six months.

Organization-owner access should be separate from routine development wherever
practical. Bots and service accounts must have a documented owner, purpose,
scope, and removal procedure.

## Review and releases

Maintainers must not be the sole approver of their own material changes. Changes
to consensus, cryptography, releases, signing, permissions, or security require
independent review appropriate to the risk.

A release should identify its source revision, build procedure, dependency
versions, artifacts and checksums, compatibility, known limitations, and
upgrade or rollback path. A public endpoint is not evidence of release quality.

## Inactivity and removal

Maintainers may step down at any time. Access may be reduced after sustained
inactivity, a role change, a security concern, repeated policy violations, or a
request from the maintainer. Removal should preserve attribution and should be
documented without exposing private information.

Compromised or abandoned access may be suspended immediately and reviewed after
containment.

## Current maintainer record

Until repository-specific maintainer teams are published, GitHub repository and
team permissions are the authoritative record. Each active repository should
add a public maintainer section or CODEOWNERS file once at least two responsible
reviewers have accepted the role.

General coordination: [GitHub Discussions](https://github.com/ipicoin/.github/discussions)

Private security or access concern: [hello@ipi.io](mailto:hello@ipi.io)
