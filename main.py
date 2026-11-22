#!/usr/bin/env python3
"""The $49 Audit Plan — make.fun entry.

Writes a short, agent-executable plan to /output/entry.txt:
turn $100 into the most money in 30 days by selling cheap SEO-audit
PDFs to Shopify store owners. Stdlib only, no network.
"""
import os

PLAN = (
    "Sell $49 SEO-audit PDFs to Shopify stores: code finds 500 stores, "
    "generates audits, emails owners preview + pay link. "
    "$100 covers APIs, domain, email. "
    "Day 1: build auditor, list 200 stores. "
    "Edge: each audit costs $0.08, so $49 undercuts agencies 10x; "
    "2% of 500 = 10 sales = $490."
)


def main() -> None:
    text = PLAN.strip()
    assert text, "plan must not be empty"
    assert 1 <= len(text) <= 280, f"plan is {len(text)} code points, must be 1-280"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {path}: {len(text)} characters")


if __name__ == "__main__":
    main()
