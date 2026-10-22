#!/usr/bin/env python3
"""Validate a RONGE design-critic JSON and compute the gate.

Usage:
  python3 validate_review.py review.json
  cat review.json | python3 validate_review.py
"""
from __future__ import annotations
import json
import sys
from pathlib import Path


def load() -> dict:
    raw = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) > 1 else sys.stdin.read()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise SystemExit("review must be a JSON object")
    return data


def main() -> int:
    data = load()
    scores = data.get("scores")
    if not isinstance(scores, dict) or not scores:
        raise SystemExit("missing scores object")
    nums = []
    for key, value in scores.items():
        if not isinstance(value, (int, float)) or not 0 <= value <= 10:
            raise SystemExit(f"score {key} must be 0..10")
        nums.append(float(value))
    avg = round(sum(nums) / len(nums), 2)
    recommended = data.get("recommended")
    if recommended not in {"A", "B", "C", "none"}:
        raise SystemExit("recommended must be A/B/C/none")
    print(json.dumps({
        "average": avg,
        "recommended": recommended,
        "gate": "pass" if avg >= 9 else "iterate" if avg >= 7 else "rebuild",
        "scores": scores,
        "top_gaps": data.get("top_gaps", []),
    }, ensure_ascii=False, indent=2))
    return 0 if avg >= 9 else 1


if __name__ == "__main__":
    raise SystemExit(main())
