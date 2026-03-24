# Crossref Research Tools 📚

> Search 130M+ research papers via the Crossref API. Find papers by DOI, author, or topic. Track citation counts. No API key needed.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![No API Key](https://img.shields.io/badge/API%20Key-Not%20Required-green.svg)](https://api.crossref.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## What Is Crossref?

[Crossref](https://www.crossref.org/) is a DOI registration agency that indexes 130M+ scholarly works from 17,000+ publishers. Their API is completely free and open.

## Quick Start

```bash
# Search papers on any topic
python3 search.py "machine learning" --limit 5

# Look up a DOI
python3 doi_lookup.py "10.1038/nature12373"

# Find author's publications
python3 author_search.py "Geoffrey Hinton" --limit 10

# Track a journal's recent publications
python3 journal_works.py "Nature" --limit 5
```

## Tools

| Script | What it does |
|--------|-------------|
| `search.py` | Full-text search across 130M+ papers |
| `doi_lookup.py` | Get metadata for any DOI |
| `author_search.py` | Find all works by an author |
| `journal_works.py` | Recent publications from a journal |
| `citation_count.py` | Check citation count for a DOI |

## API Features

- **130M+ works** indexed
- **No API key** required
- **No rate limit** (with polite pool: add `mailto` parameter)
- **DOI resolution** — look up any paper by DOI
- **Full-text search** across titles and abstracts
- **Filters** by date, type, publisher, ISSN
- Returns **JSON** with full metadata

## Example Output

```
$ python3 search.py "transformer attention" --limit 3

1. Attention Is All You Need (2017)
   Authors: Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin
   Citations: 98,432
   DOI: 10.48550/arXiv.1706.03762

2. BERT: Pre-training of Deep Bidirectional Transformers (2019)
   Citations: 72,156
   DOI: 10.18653/v1/N19-1423
```

## Related Projects

- [OpenAlex Research Tools](https://github.com/spinov001-art/openalex-research-tools) — 250M+ works, author networks, institutions
- [awesome-web-scraping-2026](https://github.com/spinov001-art/awesome-web-scraping-2026) — 77+ data collection tools
- [free-apis-list](https://github.com/spinov001-art/free-apis-list) — 200+ free APIs for developers

## License

MIT
