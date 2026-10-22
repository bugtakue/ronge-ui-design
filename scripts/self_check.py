#!/usr/bin/env python3
"""Lightweight self-check for the RONGE skill package."""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "CONTRIBUTING.md",
    "VERSION",
    "CHANGELOG.md",
    "presets/example-product.md",
    "references/method.md",
    "references/design-critic.md",
    "references/iphone-preview.md",
    "references/audit.md",
    "references/handoff.md",
    "references/accessibility.md",
    "references/motion.md",
    "references/validation.md",
    "references/page-recipes.md",
    "templates/design-brief.md",
    "templates/review-report.md",
    "scripts/seed.sh",
    "scripts/validate_review.py",
    "examples/synthetic-brief.md",
    "examples/synthetic-review.json",
    "examples/synthetic-walkthrough.md",
]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing: {rel}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---"):
        errors.append("SKILL.md needs YAML frontmatter")
    if "name: ronge-ui-design" not in skill:
        errors.append("frontmatter name must be ronge-ui-design")
    if "description:" not in skill:
        errors.append("frontmatter description missing")

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"`((?:references|presets|templates|scripts|examples)/[^`]+?\.(?:md|py|sh|json))`", text):
            if "<" in match.group(1) or ">" in match.group(1):
                continue
            if not (ROOT / match.group(1)).exists():
                errors.append(f"{path.relative_to(ROOT)} -> missing {match.group(1)}")

    for script in ("scripts/seed.sh", "scripts/validate_review.py"):
        p = ROOT / script
        if p.exists() and not (p.stat().st_mode & 0o111):
            errors.append(f"not executable: {script}")

    review = ROOT / "examples/synthetic-review.json"
    if review.exists():
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/validate_review.py"), str(review)],
            capture_output=True, text=True,
        )
        if proc.returncode not in (0, 1):
            errors.append("validate_review.py failed on synthetic-review.json")
    if errors:
        print("RONGE self-check: FAIL")
        for err in errors:
            print("-", err)
        return 1
    print("RONGE self-check: OK")
    print(f"files: {len(list(ROOT.rglob('*')))}")
    print(f"version: {(ROOT / 'VERSION').read_text().strip()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
