# Crossref Research Tools

> Python toolkit for Crossref API — search 150M+ academic papers, build citation networks, analyze funding. No API key needed.

[![Dev.to Tutorial](https://img.shields.io/badge/Tutorial-Dev.to-0A0A0A?logo=devdotto)](https://dev.to/0012303/crossref-api-search-150m-academic-papers-for-free-no-api-key-needed-319n)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Features

- **Paper Search** — find papers by keyword, author, DOI
- **Citation Networks** — build citation graphs for any research area
- **Funding Analysis** — discover who funds specific research topics
- **Publication Monitoring** — track new papers in real-time
- **Batch DOI Resolution** — resolve thousands of DOIs efficiently

## Quick Start

```bash
pip install requests
```

```python
import requests

results = requests.get("https://api.crossref.org/works", params={
    "query": "machine learning drug discovery",
    "rows": 5,
    "sort": "relevance"
}).json()

for item in results["message"]["items"]:
    title = item["title"][0] if item.get("title") else "No title"
    cited = item.get("is-referenced-by-count", 0)
    print(f"[{cited} citations] {title}")
```

## Build Citation Network

```python
def get_top_cited(query, sample_size=100):
    results = requests.get("https://api.crossref.org/works", params={
        "query": query,
        "rows": sample_size,
        "select": "DOI,title,is-referenced-by-count,author",
        "sort": "is-referenced-by-count",
        "order": "desc"
    }).json()

    papers = []
    for item in results["message"]["items"]:
        authors = item.get("author", [{}])
        first_author = authors[0].get("family", "Unknown") if authors else "Unknown"
        papers.append({
            "doi": item["DOI"],
            "title": item["title"][0][:80] if item.get("title") else "Untitled",
            "citations": item.get("is-referenced-by-count", 0),
            "author": first_author
        })
    return sorted(papers, key=lambda x: x["citations"], reverse=True)[:10]
```

## Funding Analysis

```python
from collections import Counter

def analyze_funding(query, sample=50):
    results = requests.get("https://api.crossref.org/works", params={
        "query": query, "rows": sample,
        "filter": "has-funder:true"
    }).json()

    funders = Counter()
    for item in results["message"]["items"]:
        for funder in item.get("funder", []):
            funders[funder.get("name", "Unknown")] += 1

    for name, count in funders.most_common(10):
        print(f"  {count:3d} papers — {name}")
```

## Rate Limits

| Pool | Rate | How to get |
|------|------|------------|
| Public | 50 req/sec | Default |
| Polite | 50+ req/sec | Add `mailto` param |
| Plus | Unlimited | Paid subscription |

## Related Projects

- [OpenAlex Research Tools](https://github.com/spinov001-art/openalex-research-tools) — search 250M+ papers via OpenAlex API
- [npm Package Health Check](https://github.com/spinov001-art/npm-package-health-check) — security audit npm packages
- [AI Market Research](https://github.com/spinov001-art/ai-market-research) — AI-powered market research tools

## License

MIT

