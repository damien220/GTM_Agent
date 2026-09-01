#!/usr/bin/env python3
"""Validate every GTM_Agent platform registry file against the schema documented
in refs/platform-scoring-methodology.md ("Platform YAML schema").

The schema was documented from Phase 2 onward but unenforced — a missing
`reach_rating`, a malformed `category_fit` list, or a typo'd `time_to_value`
silently breaks `distribution-specialist`'s scoring on the next run instead of
failing loudly. This is that guard (design-review-2026-08.md §2.2).

Uses the shared Dev_Agents/.venv (PyYAML); stdlib + yaml only, no other deps.

Usage:
    python lib/validate_platforms.py                  # validates ../platforms/*.yaml
    python lib/validate_platforms.py path/to/platforms
    python lib/validate_platforms.py path/to/one-platform.yaml

Exit codes: 0 all files valid · 1 at least one file invalid · 2 usage/IO error.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

# Exact category strings from refs/project-classification.md Dimension 1 —
# kept identical so a classification block matches category_fit with no
# translation step (platform-scoring-methodology.md, "Platform YAML schema").
CATEGORIES = {
    "dev tool / library",
    "SaaS / web app",
    "CLI",
    "game",
    "mobile app",
    "API",
    "content / creative tool",
    "AI agent",
}

TIME_TO_VALUE = {"fast", "medium", "slow"}

REQUIRED_FIELDS = {
    "id",
    "display_name",
    "url",
    "category_fit",
    "audience",
    "reach_rating",
    "effort_rating",
    "time_to_value",
    "prerequisites",
    "submission_workflow",
}
OPTIONAL_FIELDS = {"stack_fit_notes", "notes"}
KNOWN_FIELDS = REQUIRED_FIELDS | OPTIONAL_FIELDS

KEBAB_CASE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def _err(problems: list[str], msg: str) -> None:
    problems.append(msg)


def _check_str(problems: list[str], data: dict, key: str) -> None:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        _err(problems, f"`{key}` must be a non-empty string (got {value!r})")


def _check_rating(problems: list[str], data: dict, key: str) -> None:
    value = data.get(key)
    # bool is an int subclass in Python — reject it explicitly.
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 5:
        _err(problems, f"`{key}` must be an integer 1-5 (got {value!r})")


def _check_str_list(
    problems: list[str], data: dict, key: str, *, allow_empty: bool
) -> None:
    value = data.get(key)
    if not isinstance(value, list):
        _err(problems, f"`{key}` must be a list (got {type(value).__name__})")
        return
    if not value and not allow_empty:
        _err(problems, f"`{key}` must be a non-empty list")
    for i, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            _err(problems, f"`{key}[{i}]` must be a non-empty string (got {item!r})")


def validate_platform(data: object, stem: str) -> list[str]:
    """Return a list of schema problems. Empty list means the entry is valid.

    `stem` is the filename without its extension — `id` must match it.
    """
    problems: list[str] = []

    if not isinstance(data, dict):
        return ["top-level YAML must be a mapping of platform fields"]

    missing = REQUIRED_FIELDS - data.keys()
    if missing:
        _err(problems, f"missing required key(s): {sorted(missing)}")

    unknown = data.keys() - KNOWN_FIELDS
    if unknown:
        _err(problems, f"unknown top-level key(s): {sorted(unknown)}")

    platform_id = data.get("id")
    if not isinstance(platform_id, str) or not KEBAB_CASE.match(platform_id):
        _err(problems, f"`id` must be kebab-case (got {platform_id!r})")
    elif platform_id != stem:
        _err(
            problems,
            f"`id` must match the filename stem (id={platform_id!r}, file={stem!r})",
        )

    for key in ("display_name", "url", "audience"):
        _check_str(problems, data, key)

    for key in ("stack_fit_notes", "notes"):
        if key in data:
            _check_str(problems, data, key)

    category_fit = data.get("category_fit")
    if not isinstance(category_fit, list) or not category_fit:
        _err(
            problems,
            f"`category_fit` must be a non-empty list (got {category_fit!r})",
        )
    else:
        for i, item in enumerate(category_fit):
            if item not in CATEGORIES:
                _err(
                    problems,
                    f"`category_fit[{i}]` = {item!r} is not one of the "
                    f"project-classification.md categories: {sorted(CATEGORIES)}",
                )

    _check_rating(problems, data, "reach_rating")
    _check_rating(problems, data, "effort_rating")

    time_to_value = data.get("time_to_value")
    if time_to_value not in TIME_TO_VALUE:
        _err(
            problems,
            f"`time_to_value` must be one of {sorted(TIME_TO_VALUE)} "
            f"(got {time_to_value!r})",
        )

    _check_str_list(problems, data, "prerequisites", allow_empty=True)
    _check_str_list(problems, data, "submission_workflow", allow_empty=False)

    return problems


def validate_file(path: Path) -> list[str]:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except OSError as e:
        return [f"could not read file: {e}"]
    except yaml.YAMLError as e:
        return [f"not valid YAML: {e}"]
    return validate_platform(data, path.stem)


def _resolve_targets(argv: list[str]) -> list[Path]:
    if len(argv) > 2:
        raise ValueError(f"usage: {argv[0]} [platforms-dir-or-file]")

    if len(argv) == 2:
        target = Path(argv[1])
    else:
        target = Path(__file__).resolve().parent.parent / "platforms"

    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(target.glob("*.yaml"))
    raise ValueError(f"no such file or directory: {target}")


def main(argv: list[str]) -> int:
    try:
        targets = _resolve_targets(argv)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2

    if not targets:
        print("no *.yaml files found to validate", file=sys.stderr)
        return 2

    failed = 0
    for path in targets:
        problems = validate_file(path)
        if problems:
            failed += 1
            print(f"FAIL  {path.name}")
            for p in problems:
                print(f"        - {p}")
        else:
            print(f"PASS  {path.name}")

    total = len(targets)
    if failed:
        print(f"\n{failed} of {total} platform file(s) failed schema validation.")
        return 1

    print(
        f"\nAll {total} platform file(s) conform to the schema in "
        "refs/platform-scoring-methodology.md."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
