#!/usr/bin/env python3
"""Validate the IPI organization profile and community standards."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "ARCHITECTURE.md",
    "README.md",
    "profile/README.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "GOVERNANCE.md",
    "MAINTAINERS.md",
    "ROADMAP.md",
    "LICENSING.md",
    "LICENSE",
    "NOTICE",
    "TRADEMARKS.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    "ipi/README.md",
    "ipi/LICENSE",
    "ipi/IPI-0000.md",
    "ipi/IPI-0001.md",
    "ipi/IPI-template.md",
    "statements/README.md",
]

CLAIM_SURFACE = [
    "ARCHITECTURE.md",
    "README.md",
    "profile/README.md",
    "ROADMAP.md",
    "ipi/README.md",
    "ipi/IPI-0001.md",
]

BANNED_UNSUPPORTED_CLAIMS = [
    "fast" + "est",
    "safe" + "st",
    "simple" + "st",
    "unlimited " + "tps",
]

PROPOSAL_FIELDS = [
    "ipi",
    "title",
    "description",
    "author",
    "discussions-to",
    "status",
    "type",
    "created",
    "requires",
]

PROPOSAL_SECTIONS = [
    "## Abstract",
    "## Motivation",
    "## Scope and non-goals",
    "## Specification",
    "## Rationale and alternatives",
    "## Compatibility and migration",
    "## Security considerations",
    "## Privacy considerations",
    "## Operational considerations",
    "## Independence impact",
    "## Test and verification plan",
    "## Reference implementation",
    "## Open questions",
]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def local_markdown_targets(content: str) -> list[str]:
    targets: list[str] = []
    for remainder in content.split("](")[1:]:
        target = remainder.split(")", 1)[0].strip()
        if target:
            targets.append(target.split()[0].strip("<>"))
    return targets


def main() -> int:
    failures: list[str] = []

    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"missing required file: {relative_path}")
            continue
        if not path.read_text(encoding="utf-8").strip():
            failures.append(f"required file is empty: {relative_path}")

    for relative_path in CLAIM_SURFACE:
        lowered = read_text(relative_path).lower()
        for phrase in BANNED_UNSUPPORTED_CLAIMS:
            if phrase in lowered:
                failures.append(
                    f"unsupported claim '{phrase}' found in {relative_path}"
                )

    for relative_path in ["ipi/IPI-0000.md", "ipi/IPI-0001.md"]:
        content = read_text(relative_path)
        lines = content.splitlines()
        if not lines or lines[0] != "---":
            failures.append(f"missing metadata header: {relative_path}")
        for field in PROPOSAL_FIELDS:
            prefix = f"{field}:"
            if not any(line.startswith(prefix) for line in lines):
                failures.append(f"missing proposal field '{field}': {relative_path}")
        for heading in PROPOSAL_SECTIONS:
            if heading not in content:
                failures.append(f"missing proposal section '{heading}': {relative_path}")

    for relative_path in REQUIRED_FILES:
        if not relative_path.endswith(".md"):
            continue
        source = ROOT / relative_path
        if not source.is_file():
            continue
        for target in local_markdown_targets(read_text(relative_path)):
            if target.startswith(("http://", "https://", "mailto:", "#", "/")):
                continue
            local_part = target.split("#", 1)[0]
            if local_part and not (source.parent / local_part).exists():
                failures.append(
                    f"broken local link '{target}' in {relative_path}"
                )

    private_name_fragments = [
        "mlasz" + "czewski",
        "lasz" + "czewski",
    ]
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            lowered = path.read_text(encoding="utf-8").lower()
        except UnicodeDecodeError:
            continue
        for fragment in private_name_fragments:
            if fragment in lowered:
                failures.append(
                    f"prohibited personal reference found in {path.relative_to(ROOT)}"
                )

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    print("Community standards validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
