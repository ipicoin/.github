---
ipi: draft
title: Short descriptive title
description: One-line purpose
author: Name or GitHub handle
discussions-to: URL
status: Draft
type: Standards Track / Core
created: YYYY-MM-DD
requires: none
---

# IPI-draft: Short descriptive title

## Abstract

State the proposed change and its result in a short paragraph.

## Motivation

Describe the concrete problem, affected users or operators, current evidence,
and why existing behavior is insufficient.

## Scope and non-goals

Define what this proposal changes and what it deliberately leaves unchanged.

## Specification

Define observable behavior precisely. Use normative MUST, MUST NOT, SHOULD,
SHOULD NOT, and MAY only where an implementation can be tested against them.
Specify state transitions, formats, validation, errors, versioning, and failure
behavior as applicable.

## Rationale and alternatives

Explain the major design choices, alternatives considered, and why they were
not selected. Include the option of making no change.

## Compatibility and migration

Describe backward and forward compatibility, activation, data migration,
rollback, client behavior, and impact on existing integrations.

## Security considerations

Identify assets, actors, trust boundaries, privileged roles, attack paths,
failure modes, and mitigations. State assumptions explicitly.

## Privacy considerations

Identify public, private, linkable, retained, and erasable data. Explain
metadata leakage and any effect on consent or data minimization.

## Operational considerations

Describe configuration, monitoring, resource requirements, dependencies,
deployment order, recovery, shutdown, and incident handling.

## Independence impact

Evaluate the proposal against [IPI-0001](IPI-0001.md). State whether it adds a
coordinator, key holder, service provider, oracle, bridge, sequencer, or another
required dependency and how an operator can verify or replace it.

## Test and verification plan

List deterministic conformance tests, test vectors, adversarial cases,
reproduction commands, and evidence required before each lifecycle transition.

## Reference implementation

Link implementations or state that none exists. A reference implementation does
not replace the specification.

## Open questions

List unresolved decisions and the evidence needed to close them.
