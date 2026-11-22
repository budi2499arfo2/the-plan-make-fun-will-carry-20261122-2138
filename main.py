#!/usr/bin/env python3
"""The $49 Audit Plan — a make.fun entry for
the-plan-make-fun-will-carry-20261122-2138.

Writes a single short plan (1-280 Unicode code points) to
/output/entry.txt: how an AI agent turns $100 into the most money
in 30 days by selling SEO-audit PDFs to Shopify stores.

The grader runs this in a sandbox with no network, the repository
read-only, an empty writable /output, and a 60-second wall budget,
so the program uses only the Python standard library and creates
its output directory when it does not exist yet.
"""

import os
import sys

# The entry must be 1-280 Unicode code points, and not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 280

# Environment variable the harness may set to point at the output dir.
OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"

# Where the entry goes when the harness sets no output directory.
DEFAULT_OUTPUT_DIR = "/output"

OUTPUT_FILENAME = "entry.txt"


def build_plan() -> str:
    """Return the plan text, written out in full by this function."""
    return (
        "Sell $49 SEO audits to Shopify stores. Code scans stores, "
        "writes audits as PDFs, emails owners a preview + pay link. "
        "$100 covers APIs, domain, email. Day 1: build the auditor, "
        "list 200 stores. Edge: each audit costs $0.08, so $49 beats "
        "agencies 10x; 2% of 500 = 10 sales = $490."
    )


def validate_plan(text: str) -> None:
    """Check the plan against the competition's entry gate.

    Raises ValueError with a plain explanation when a rule fails:
    the text must be 1-280 Unicode code points, must encode as
    UTF-8, and must contain something besides whitespace.
    """
    if not isinstance(text, str):
        raise ValueError("plan must be a string")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(
            f"plan is {len(text)} code points, must be "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("plan must not be only whitespace")
    # Encoding round-trip: proves the text is valid UTF-8.
    text.encode("utf-8")


def resolve_output_dir() -> str:
    """Pick the output directory: env var first, /output as fallback."""
    chosen = os.environ.get(OUTPUT_DIR_ENV, "").strip()
    return chosen if chosen else DEFAULT_OUTPUT_DIR


def write_entry(text: str, output_dir: str) -> str:
    """Write the plan to entry.txt inside output_dir; return its path.

    Reads the file back after writing and raises if what landed on
    disk does not match the plan exactly.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        if handle.read() != text:
            raise ValueError("written entry does not match the plan")
    return path


def main() -> int:
    """Build the plan, validate it, write it, and report what happened."""
    plan = build_plan()
    validate_plan(plan)
    path = write_entry(plan, resolve_output_dir())
    print(f"wrote {path}: {len(plan)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
