#!/usr/bin/env python3
"""Look up any paper by DOI using Crossref API.

Usage: python3 doi_lookup.py "10.1038/nature12373"
"""

import urllib.request
import json
import sys
import ssl


def lookup_doi(doi: str):
    """Get metadata for a DOI from Crossref."""
    ctx = ssl.create_default_context()
    url = f"https://api.crossref.org/works/{doi}?mailto=example@example.com"
    req = urllib.request.Request(url, headers={"User-Agent": "CrossrefTools/1.0"})
    resp = urllib.request.urlopen(req, context=ctx, timeout=30)
    data = json.loads(resp.read())
    return data["message"]


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 doi_lookup.py "10.1038/nature12373"')
        sys.exit(1)

    doi = sys.argv[1]
    paper = lookup_doi(doi)

    title = paper.get("title", ["N/A"])[0]
    authors = ", ".join(
        f"{a.get('given', '')} {a.get('family', '')}".strip()
        for a in paper.get("author", [])
    )
    year = paper.get("published-print", paper.get("created", {}))
    year = year.get("date-parts", [[None]])[0][0] if year else "?"
    journal = paper.get("container-title", ["N/A"])[0] if paper.get("container-title") else "N/A"
    citations = paper.get("is-referenced-by-count", 0)
    refs = paper.get("references-count", 0)
    ptype = paper.get("type", "?")

    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")
    print(f"  Authors:    {authors}")
    print(f"  Year:       {year}")
    print(f"  Journal:    {journal}")
    print(f"  Type:       {ptype}")
    print(f"  Citations:  {citations:,}")
    print(f"  References: {refs}")
    print(f"  DOI:        {doi}")
    if paper.get("URL"):
        print(f"  URL:        {paper['URL']}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
