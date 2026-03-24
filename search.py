#!/usr/bin/env python3
"""Search 130M+ papers on Crossref API.

Usage: python3 search.py "topic" [--limit N]
"""

import urllib.request
import json
import sys
import ssl


def search_papers(query: str, limit: int = 10):
    """Search Crossref for papers matching query."""
    ctx = ssl.create_default_context()
    encoded = urllib.parse.quote(query)
    url = (
        f"https://api.crossref.org/works?"
        f"query={encoded}&rows={limit}&sort=relevance"
        f"&mailto=example@example.com"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "CrossrefTools/1.0"})
    resp = urllib.request.urlopen(req, context=ctx, timeout=30)
    data = json.loads(resp.read())
    return data["message"]["items"]


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 search.py "topic" [--limit N]')
        sys.exit(1)

    query = sys.argv[1]
    limit = 10
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        limit = int(sys.argv[idx + 1])

    print(f"\nSearching Crossref for: \"{query}\" (top {limit})\n")

    papers = search_papers(query, limit)
    for i, paper in enumerate(papers, 1):
        title = paper.get("title", ["N/A"])[0][:70]
        authors = ", ".join(
            a.get("family", "?") for a in paper.get("author", [])[:3]
        )
        if len(paper.get("author", [])) > 3:
            authors += " et al."
        year = paper.get("published-print", paper.get("created", {}))
        year = year.get("date-parts", [[None]])[0][0] if year else "?"
        citations = paper.get("is-referenced-by-count", 0)
        doi = paper.get("DOI", "N/A")

        print(f"{i:>3}. {title}")
        print(f"     Authors: {authors}")
        print(f"     Year: {year} | Citations: {citations:,}")
        print(f"     DOI: {doi}\n")

    print(f"Source: Crossref API (api.crossref.org) — free, no API key")


if __name__ == "__main__":
    import urllib.parse
    main()
