---
title: "ChatGPT vs. DeepSeek User Sentiment & Product Strategy"
excerpt: "A multi-source analysis of approximately 843,000 public social-media and app-review records."
collection: portfolio
---

This five-person team project compared how users discussed and reviewed ChatGPT and DeepSeek, then translated the quantitative findings into product priorities. The analysis combined sentiment measurement, statistical testing, segmentation, and time-based exploration across approximately 843,000 public records.

## At a glance

| | |
|---|---|
| **Question** | How do user sentiment, engagement, and recurring concerns differ between ChatGPT and DeepSeek? |
| **Data** | Approximately 843,000 tweets and app reviews from three public datasets |
| **Methods** | Four sentiment lexicons, Pearson correlation, K-means, PCA, time-series analysis |
| **Tools** | R, tidyverse, text mining, clustering, data visualization |
| **Role** | Collaborative analysis and final presentation in a five-person team |

## Data and method

The combined analysis covered 500,002 ChatGPT tweets, 327,575 ChatGPT app reviews, and 15,124 DeepSeek reviews. AFINN, NRC, Syuzhet, and Bing sentiment methods were used to reduce dependence on a single lexicon. Pearson correlations tested relationships among sentiment, ratings, likes, and thumbs-up counts, while K-means and PCA were used to explore review segments. Time-series views and term-frequency analysis added context for how discussion themes changed.

## Key findings

| Review outcome | ChatGPT | DeepSeek |
|---|---:|---:|
| Positive | **77.16%** | **73.60%** |
| Negative | **6.7%** | **12.9%** |

- DeepSeek's negative-review share was nearly twice ChatGPT's in the reviewed datasets, pointing to a larger concentration of user friction.
- Sentiment had almost no linear relationship with likes or thumbs-up counts in the aggregate data, so engagement volume was not a reliable proxy for satisfaction.
- Clustering separated reviews primarily by behavior and length, with silhouette scores of 0.773 for ChatGPT and 0.757 for DeepSeek in the selected specification.

## Product implications

The evidence supports prioritizing reliability and privacy communication before treating raw engagement as a success metric. Product teams should pair sentiment with issue-level themes, ratings, and retention measures; high interaction counts can coexist with negative experiences. The comparative view also shows why platform-specific feedback loops are more useful than one global social-engagement KPI.

## Limitations

Lexicon methods can miss sarcasm, context, and rapidly changing AI terminology. The source datasets also differ in platform, time coverage, and user behavior, so the comparison is directional rather than a controlled causal estimate.

**Attribution:** This was a five-person team project. The page presents shared analysis and recommendations and does not claim sole authorship.
