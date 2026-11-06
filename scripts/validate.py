"""Schema checks for data/categories.json and data/entries.json (standard library only)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["id", "title", "date", "venue", "category", "kind", "evidence", "links", "summary", "added"]
KINDS = {"paper", "report", "repo", "post", "model", "dataset", "benchmark"}
EVIDENCE = {"peer", "preprint", "code", "post"}
LINK_KEYS = {"paper", "post", "thread", "code", "project", "model", "data"}
DATE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
ID = re.compile(r"^[a-z0-9][a-z0-9\-]*$")
REPO = re.compile(r"^[\w.\-]+/[\w.\-]+$")
MAX_SUMMARY_WORDS = 90


def category_ids(cats: list[dict]) -> list[str]:
    out = []
    for c in cats:
        out.append(c["id"])
        out += [ch["id"] for ch in c.get("children", [])]
    return out


def validate(cats: list[dict], entries: list[dict]) -> list[str]:
    errs = []
    cids = category_ids(cats)
    if len(cids) != len(set(cids)):
        errs.append("duplicate category ids")
    for c in cats:
        if c.get("children") and any(e["category"] == c["id"] for e in entries if "category" in e):
            pass  # entries may sit directly under a parent too
    seen, urls = set(), {}
    for i, e in enumerate(entries):
        tag = e.get("id", f"#{i}")
        for k in REQUIRED:
            if k not in e or e[k] in (None, "") and k != "venue":
                errs.append(f"{tag}: missing {k}")
        if errs and errs[-1].startswith(tag):
            continue
        if not ID.match(e["id"]):
            errs.append(f"{tag}: id must be lowercase slug")
        if e["id"] in seen:
            errs.append(f"{tag}: duplicate id")
        seen.add(e["id"])
        if not DATE.match(e["date"]) or not DATE.match(e["added"]):
            errs.append(f"{tag}: dates must be YYYY, YYYY-MM or YYYY-MM-DD")
        if e["category"] not in cids:
            errs.append(f"{tag}: unknown category {e['category']}")
        if e["kind"] not in KINDS:
            errs.append(f"{tag}: kind must be one of {sorted(KINDS)}")
        if e["evidence"] not in EVIDENCE:
            errs.append(f"{tag}: evidence must be one of {sorted(EVIDENCE)}")
        if not e["links"] or set(e["links"]) - LINK_KEYS:
            errs.append(f"{tag}: links must be a non-empty subset of {sorted(LINK_KEYS)}")
        for k, u in e["links"].items():
            if not str(u).startswith("https://"):
                errs.append(f"{tag}: {k} link must be https")
            if u in urls and k in ("paper", "code"):
                errs.append(f"{tag}: {k} link duplicates entry {urls[u]}")
            urls.setdefault(u, tag)
        if e.get("repo") and not REPO.match(e["repo"]):
            errs.append(f"{tag}: repo must be owner/name")
        if len(e["summary"].split()) > MAX_SUMMARY_WORDS:
            errs.append(f"{tag}: summary over {MAX_SUMMARY_WORDS} words")
        if "citations" in e and (not isinstance(e["citations"], int) or e["citations"] < 0
                                 or e.get("citations_source") not in ("S2", "OA")):
            errs.append(f"{tag}: citations must be a count with citations_source S2 or OA")
        if "|" in e["title"]:
            errs.append(f"{tag}: title may not contain |")
    return errs


if __name__ == "__main__":
    cats = json.loads((ROOT / "data/categories.json").read_text())
    entries = json.loads((ROOT / "data/entries.json").read_text())
    problems = validate(cats, entries)
    print("\n".join(problems) or f"ok: {len(entries)} entries")
    sys.exit(1 if problems else 0)
