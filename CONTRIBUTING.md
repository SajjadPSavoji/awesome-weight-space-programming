# Contributing

Thank you for helping keep this list accurate.

## How it works

To contribute, open a pull request and follow the style of the existing entries (fields below; look at a
few neighbours in your category for summary length and tone). Every pull request is reviewed, and it is
merged once its relevance is confirmed. We may adjust the wording or the category to keep the list
consistent; the commit stays yours.

**If you are an author of the work,** say so in the pull request and include the details:

- your affiliation, and the full author list;
- the status: preprint, under review, or accepted (and at which venue);
- links to the paper, code, data and models, as available;
- the headline result with its setting (model, task, baseline), as it appears in the work;
- in a line, what it adds beyond the entries already listed.

Self-submissions are welcome; the disclosure is what lets reviewers check them quickly.

## Adding an entry

1. Add one object to [`data/entries.json`](data/entries.json):

   ```json
   {
     "id": "short-lowercase-slug",
     "title": "Exact title of the paper, repository or post",
     "authors": "First Author, Second Author",
     "org": "Lab or institution (optional)",
     "date": "2026-11-04",
     "venue": "Preprint | NeurIPS 2026 | GitHub | Blog | X thread",
     "category": "robotics-vla",
     "kind": "paper | report | repo | post | model | dataset | benchmark",
     "evidence": "peer | preprint | code | post",
     "links": {"paper": "https://arxiv.org/abs/...", "code": "https://github.com/..."},
     "repo": "owner/name (optional, adds a stars badge)",
     "summary": "One or two sentences: what network was programmed, how, and the headline number as the source reports it.",
     "added": "2026-11-04"
   }
   ```

   `category` must be an id from [`data/categories.json`](data/categories.json). To propose a new
   category or subcategory, add it there in the same pull request and say why the existing ones do not
   fit.

2. Run `python3 scripts/build.py` (standard library only) and commit both the JSON and `README.md`.

## What belongs here

- **In scope:** work where a model reads, edits or writes another network's weights directly, and
  benchmarks, tools and critiques of that work. Groundwork such as model editing, activation steering,
  compiled weights and weight-space learning goes under *Foundations*.
- **Papers:** any on-topic paper or report, whatever its traction.
- **Repositories:** some traction (stars, forks) or an organization owner. Young repositories are
  watched and re-checked, and join the list once they gain traction.
- **Summaries:** neutral. Quote the source's numbers and conditions, with no adjectives.

## Corrections

Open an issue or pull request. Wrong numbers, dead links and better categories are all welcome.
