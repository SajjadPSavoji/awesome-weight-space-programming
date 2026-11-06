"""Build README.md from data/categories.json and data/entries.json.

    python3 scripts/build.py                        # writes ./README.md
    python3 scripts/build.py --mirror ../awesome-wsp  # also writes the mirror's README
    python3 scripts/build.py --check                # exit 1 if README.md is stale

Standard library only. Never edit README.md by hand: edit the JSON and rebuild.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEWS_DAYS = 14
NEWS_MAX = 12

EVIDENCE = {
    "peer": "📄 peer-reviewed",
    "preprint": "📝 preprint",
    "code": "💻 code / results",
    "post": "💬 post only",
}
LINK_ORDER = [("paper", "Paper"), ("post", "Post"), ("thread", "Thread"), ("code", "Code"),
              ("project", "Project"), ("model", "Model"), ("data", "Data")]


def load():
    meta = json.loads((ROOT / "data/list.json").read_text())
    cats = json.loads((ROOT / "data/categories.json").read_text())
    entries = json.loads((ROOT / "data/entries.json").read_text())
    return meta, cats, entries


def slug(text: str) -> str:
    """GitHub's heading anchor: lowercase, drop punctuation except - and space, spaces to -."""
    s = re.sub(r"[^\w\- ]", "", text.lower(), flags=re.UNICODE)
    return s.replace(" ", "-")


def heading(cat: dict) -> str:
    return f"{cat.get('emoji', '')} {cat['title']}".strip()


def flat(cats: list[dict]) -> dict[str, dict]:
    out = {}
    for c in cats:
        out[c["id"]] = c
        for ch in c.get("children", []):
            out[ch["id"]] = ch | {"parent": c["id"]}
    return out


def primary(e: dict) -> str:
    for k, _ in LINK_ORDER:
        if e["links"].get(k):
            return e["links"][k]
    return ""


def render_entry(e: dict) -> str:
    links = " ".join(f"[[{label}]({e['links'][k]})]" for k, label in LINK_ORDER if e["links"].get(k))
    stars = (f" ![GitHub stars](https://img.shields.io/github/stars/{e['repo']}?style=social)"
             if e.get("repo") else "")
    who = e.get("org") or e.get("authors") or ""
    cites = f"{cite_count(e['citations'])} citations ({e['citations_source']})" if e.get("citations") else ""
    meta = " · ".join(x for x in [who, f"*{e['venue']}*", e["date"], f"`{EVIDENCE[e['evidence']]}`", cites] if x)
    return (f"- **[{e['title']}]({primary(e)})**  \n"
            f"  {meta}  \n"
            f"  {links}{stars}  \n"
            f"  {e['summary']}\n")


def sort_key(e: dict):
    return e["date"]


def cite_count(n: int) -> str:
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def render(meta, cats, entries, mirror: bool = False) -> str:
    by_cat: dict[str, list] = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)
    # anchor on the newest addition, not the clock, so the build is reproducible (CI --check)
    today = max((date.fromisoformat(e["added"]) for e in entries if len(e.get("added", "")) == 10), default=date.today())
    lines: list[str] = []
    repo = f"{meta['owner']}/{meta['canon']}"
    lines += [
        '<div align="center">',
        "",
        f"# {meta['title']} [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        f"**{meta['tagline']}**",
        "",
        f"[![Last commit](https://img.shields.io/github/last-commit/{repo}?color=green)](https://github.com/{repo}/commits/main)",
        f"![Entries](https://img.shields.io/badge/entries-{len(entries)}-blue)",
        f"![Updated](https://img.shields.io/badge/updated-{meta.get('updated', 'daily')}-orange)",
        "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)",
        "[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)",
        "",
        "</div>",
        "",
    ]
    if mirror:
        lines += [f"> **This is a mirror of [{meta['canon']}](https://github.com/{repo}).** Same content, rebuilt "
                  f"from the same data. Please star and open pull requests there.", ""]
    lines += [meta["intro"], ""]
    if meta.get("survey"):
        sv = meta["survey"]
        lines += [f"> 📄 **Companion survey:** [{sv['title']}]({sv['url']})"
                  + (f" ({sv['version']})" if sv.get("version") else ""), ""]
    # News
    history = {c["id"] for c in cats if c.get("order") == "oldest"}
    history |= {ch["id"] for c in cats if c["id"] in history for ch in c.get("children", [])}
    recent = [e for e in entries if e.get("added") and e["category"] not in history
              and date.fromisoformat(e["added"]) >= today - timedelta(days=NEWS_DAYS)]
    recent.sort(key=lambda e: (e["added"], e["date"]), reverse=True)
    if recent:
        lines += ["## 🔥 Recently Added", ""]
        for e in recent[:NEWS_MAX]:
            lines.append(f"- **{e['added']}** · [{e['title']}]({primary(e)}) "
                         f"({flat(cats)[e['category']]['title']})")
        lines.append("")
    # Milestones
    ms = sorted([e for e in entries if e.get("milestone")], key=sort_key)
    if ms:
        lines += ["## 🧭 Milestones", "", "| Date | Milestone | Who | Work |", "|:--|:--|:--|:--|"]
        for e in ms:
            lines.append(f"| {e['date']} | {e['milestone']} | {e.get('org') or e.get('authors', '')} | "
                         f"[{e['title']}]({primary(e)}) |")
        lines.append("")
    # Contents
    lines += ["## Contents", ""]
    for c in cats:
        n = len(by_cat.get(c["id"], [])) + sum(len(by_cat.get(ch["id"], [])) for ch in c.get("children", []))
        if not n:
            continue
        lines.append(f"- [{heading(c)}](#{slug(heading(c))}) ({n})")
        for ch in c.get("children", []):
            if by_cat.get(ch["id"]):
                lines.append(f"  - [{ch['title']}](#{slug(ch['title'])}) ({len(by_cat[ch['id']])})")
    lines += ["- [Legend](#legend)", "- [How This List Is Maintained](#how-this-list-is-maintained)",
              "- [Related Lists](#related-lists)", "- [Contributing](#contributing)", "- [Citation](#citation)", ""]
    # Sections
    for c in cats:
        newest = c.get("order") != "oldest"  # history sections read oldest first
        own = sorted(by_cat.get(c["id"], []), key=sort_key, reverse=newest)
        kids = [ch for ch in c.get("children", []) if by_cat.get(ch["id"])]
        if not own and not kids:
            continue
        lines += [f"## {heading(c)}", ""]
        if c.get("blurb"):
            lines += [f"*{c['blurb']}*", ""]
        for e in own:
            lines.append(render_entry(e))
        for ch in kids:
            lines += [f"### {ch['title']}", ""]
            for e in sorted(by_cat[ch["id"]], key=sort_key, reverse=newest):
                lines.append(render_entry(e))
    # Footer
    lines += [
        "## Legend", "",
        " · ".join(f"`{v}`" for v in EVIDENCE.values()), "",
        "Entries are newest first within each section, except historical sections, which read oldest first. "
        "Summaries report the source's own numbers and settings. Evidence labels say what kind of source backs an "
        "entry, not whether its claims hold. Citation counts, where shown, are from Semantic Scholar (S2) or "
        "OpenAlex (OA) at the time the entry was added; the two sources are not comparable, so read them as "
        "orders of magnitude.", "",
        "## How This List Is Maintained", "",
        f"An automated sweep ({meta.get('updated', 'daily')}) checks arXiv, GitHub and the Hugging Face Hub for new "
        f"work. {meta['scope']} On-topic papers are listed whatever their traction; repositories are listed "
        "once they show traction or come from an organization, and young ones are kept on a watch list and "
        "re-checked. Categories grow as the field does: a new section opens when work no longer fits the "
        "existing ones. Corrections are welcome as issues or pull requests.", "",
        "## Related Lists", "",
        *[f"- [{n}]({u})" + (f": {d}" if d else "") for n, u, d in meta.get("related", [])],
        "",
        "## Contributing", "",
        "Contributions are welcome. To add a work, open a pull request that adds one object to "
        "[`data/entries.json`](data/entries.json) in the same style as the existing entries, then run "
        "`python3 scripts/build.py`. Each pull request is reviewed, and it is merged once its relevance "
        "is confirmed. **If you are an author of the work, say so** in the pull request and include the "
        "details: affiliation, status (preprint, under review or accepted, and where), links to code and "
        "data, and the headline result with its setting. See [CONTRIBUTING.md](CONTRIBUTING.md) for the "
        "fields and inclusion rules.", "",
        "## Citation", "",
        "```bibtex",
        f"@misc{{{meta['canon']},",
        f"  author       = {{{meta['author']}}},",
        f"  title        = {{{meta['title']}}},",
        f"  year         = {{{meta['year']}}},",
        f"  howpublished = {{\\url{{https://github.com/{repo}}}}}",
        "}",
        "```", "",
        "## Star History", "",
        f"[![Star History Chart](https://api.star-history.com/svg?repos={repo}&type=Date)](https://star-history.com/#{repo}&Date)",
        "",
    ]
    text = "\n".join(lines)
    if mirror:  # the mirror has no data/ or CONTRIBUTING.md: point at the canonical repo
        base = f"https://github.com/{repo}/blob/main/"
        text = re.sub(r"\]\((data/[^)]+|CONTRIBUTING\.md)\)", lambda m: f"]({base}{m.group(1)})", text)
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mirror", help="path to the mirror repo clone")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    sys.path.insert(0, str(ROOT / "scripts"))
    from validate import validate  # noqa: E402
    meta, cats, entries = load()
    errors = validate(cats, entries)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    text = render(meta, cats, entries)
    if args.check:
        stale = (ROOT / "README.md").read_text() != text
        print("README.md is stale: run scripts/build.py" if stale else "README.md is up to date")
        return int(stale)
    (ROOT / "README.md").write_text(text)
    if args.mirror:
        m = Path(args.mirror).expanduser()
        (m / "README.md").write_text(render(meta, cats, entries, mirror=True))
    print(f"built README: {len(entries)} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
