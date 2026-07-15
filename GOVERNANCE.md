# IPI Governance

This document defines how the IPI open-source project makes technical and
community decisions. It governs project repositories and processes; it does not
claim to be on-chain governance and does not give a token, company, or informal
title authority over the project.

## Principles

IPI governance should be:

- **evidence-led** — important claims and decisions must be reproducible;
- **open by default** — normal decisions happen in public issues, Discussions,
  pull requests, and IPI proposals;
- **least-authority** — access and emergency powers should be narrow, visible,
  and reviewable;
- **reversible where possible** — experiments should have exit and rollback
  paths;
- **attributable** — upstream work and contributor decisions remain traceable;
  and
- **independence-oriented** — changes should reduce hidden coordinators and make
  independent operation easier to verify.

## Roles

### Contributors

Anyone who participates constructively. Contributors can open issues,
Discussions, pull requests, reviews, and IPI proposals.

### Reviewers

Contributors with demonstrated knowledge of an area who provide substantive
review. Reviewers do not gain merge or administrative access automatically.

### Maintainers

People trusted with merge access for a defined repository or component.
Maintainers triage work, protect compatibility and security, review changes,
and steward releases. They must follow [MAINTAINERS.md](MAINTAINERS.md).

### Security responders

A small group with access to private vulnerability reports. They coordinate
validation, remediation, and disclosure and must avoid conflicts of interest.

### Organization owners

Custodians of GitHub organization settings, recovery, permissions, and legal or
security escalation. Ownership is an infrastructure responsibility, not
automatic technical authority.

The current GitHub permission configuration is the authoritative access record.
Titles in documents never grant access by themselves.

## Decision paths

### Routine repository changes

Bug fixes, tests, documentation, and bounded implementation changes use normal
pull-request review. The repository's branch rules and CODEOWNERS, when present,
define the minimum approval requirements.

### Substantial changes

Protocol behavior, public interfaces, consensus rules, compatibility,
cryptography, trust assumptions, governance, or coordinated changes across
repositories require an [IPI Improvement Proposal](ipi/README.md).

Implementation can begin experimentally before a proposal is accepted, but
acceptance must not be implied and production compatibility must not depend on
an unaccepted proposal.

### Security changes

Security fixes may be developed privately and merged with limited advance
detail. The reasoning, affected versions, and credit should be published after
coordinated disclosure when doing so is safe.

### Urgent operational action

An organization owner may temporarily restrict access, disable a compromised
workflow, protect a branch, rotate credentials, or take another bounded action
to prevent immediate harm. The action must be documented after containment,
with sensitive details withheld only as long as necessary.

## Reaching a decision

The preferred outcome is reasoned consensus: objections are answered with
evidence or the proposal changes. Consensus does not require unanimity.

If material disagreement remains, maintainers record the alternatives, risks,
and rationale. An accepted IPI requires approval from the maintainers
responsible for every affected component and no unresolved blocking security or
licensing issue. A maintainer must not approve their own change as the only
reviewer.

When the project lacks enough independent maintainers for this rule, a proposal
remains Draft or Review rather than creating the appearance of independent
approval.

## Conflicts of interest

Decision-makers must disclose financial, employment, personal, or security
interests that a reasonable contributor could view as affecting judgment. A
conflicted person may provide facts but should not be the deciding reviewer.

## Changes to governance

Material changes to this document use the IPI process. Administrative fixes,
broken links, and clarifications that do not change authority may use an ordinary
pull request.
