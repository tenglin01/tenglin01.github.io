---
title: "Amazon Product Search & Review Summarization"
excerpt: "An evaluated NLP search system spanning 104,259 products and 300,000 customer reviews."
collection: portfolio
---

I co-developed an end-to-end search and review-summarization system for Amazon Office Products. The project connected data preparation, information retrieval, evaluation, and a lightweight Flask interface in one reproducible workflow.

## At a glance

| | |
|---|---|
| **Question** | Can product metadata and customer reviews support fast, relevant search and concise review summaries? |
| **Data** | 300,000 customer reviews; 104,259 indexed products |
| **Methods** | TF-IDF, cosine similarity, extractive summarization, offline retrieval evaluation |
| **Tools** | Python, pandas, scikit-learn, SciPy, Flask |
| **Role** | Team project — co-developed the analysis and application workflow |

## Approach

1. **Prepared the corpus.** Product metadata and a controlled review sample were parsed, cleaned, and joined into a searchable product table.
2. **Built the retrieval layer.** Product titles and descriptions were represented with TF-IDF. The final sparse search matrix covered 104,259 products across a 50,000-term vocabulary, with cosine similarity used for ranking.
3. **Added review summaries.** The application selected informative review sentences and included safeguards for products with limited review coverage.
4. **Created a search interface.** A Flask dashboard returned ranked products, metadata, and review summaries for a user query.
5. **Evaluated relevance.** Product-title self-retrieval was tested on 200 queries using Hit@10, MRR@10, and nDCG@10 rather than relying only on anecdotal examples.

## Results

| Metric | Result |
|---|---:|
| Hit@10 | **98.0%** |
| MRR@10 | **92.45%** |
| nDCG@10 | **93.85%** |
| Queries ranked first | **177 of 200** |

The strongest result was coverage: 196 of 200 title queries retrieved the expected product within the top ten. MRR@10 and nDCG@10 also show that the relevant item usually appeared near the top rather than merely somewhere in the result set.

## Practical implications and limitations

This project demonstrates how a simple, interpretable retrieval baseline can perform strongly when paired with careful corpus construction and explicit evaluation. The title-based evaluation is intentionally narrow, however; a production system would also require human relevance judgments for natural-language queries, latency testing, and monitoring for catalog drift.

## Review the work

- [Open the sanitized notebook](/files/projects/amazon-office-search/Office_Products_Search_System.ipynb)
- [Read the reproducibility notes](/files/projects/amazon-office-search/README.md)

**Attribution:** Team project. Results and methods are described as shared project work; no claim of sole ownership is made.
