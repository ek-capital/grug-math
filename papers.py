#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.11"
# dependencies = ["arxiv==4.0.0"]
# ///
"""Find recently submitted or updated arXiv papers."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone

import arxiv


def paper_data(result: arxiv.Result) -> dict[str, object]:
    return {
        "id": result.get_short_id(),
        "title": " ".join(result.title.split()),
        "authors": [author.name for author in result.authors],
        "published": result.published.date().isoformat(),
        "updated": result.updated.date().isoformat(),
        "categories": result.categories,
        "url": result.entry_id,
        "pdf": result.pdf_url,
        "doi": result.doi,
        "journal_ref": result.journal_ref,
        "summary": " ".join(result.summary.split()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search arXiv and keep only recently published or updated papers."
    )
    parser.add_argument(
        "query",
        help='arXiv query, for example: all:"cycle double cover" AND cat:math.CO',
    )
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    if args.days < 1 or args.limit < 1:
        parser.error("--days and --limit must be positive")

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    search = arxiv.Search(
        query=args.query,
        max_results=max(args.limit * 5, 50),
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    client = arxiv.Client(page_size=100, delay_seconds=3, num_retries=3)

    papers: list[dict[str, object]] = []
    for result in client.results(search):
        if max(result.published, result.updated) < cutoff:
            continue
        papers.append(paper_data(result))
        if len(papers) == args.limit:
            break

    if args.as_json:
        print(json.dumps(papers, indent=2, ensure_ascii=False))
        return 0

    print(f"# Recent arXiv papers\n\nQuery: `{args.query}`  ")
    print(f"Window: last {args.days} days  \nResults: {len(papers)}")
    for paper in papers:
        authors = ", ".join(paper["authors"])
        print(f"\n## {paper['title']}")
        print(f"\n- arXiv: [{paper['id']}]({paper['url']})")
        print(f"- Published: {paper['published']}; updated: {paper['updated']}")
        print(f"- Categories: {', '.join(paper['categories'])}")
        print(f"- Authors: {authors}")
        if paper["doi"]:
            print(f"- DOI: {paper['doi']}")
        print(f"\n{paper['summary']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
