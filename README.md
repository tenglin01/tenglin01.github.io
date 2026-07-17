# Teng Lin Analytics Portfolio

Source code and public project materials for [tenglin01.github.io](https://tenglin01.github.io/), a recruiter-facing portfolio covering data analytics, machine learning, business intelligence, and applied research.

## Featured work

- **Amazon Product Search & Review Summarization** — TF-IDF search across 104,259 products, evaluated at 98.0% Hit@10 on 200 title queries.
- **ChatGPT vs. DeepSeek User Sentiment & Product Strategy** — a team analysis of approximately 843,000 public social-media and app-review records.
- **BiLSTM Stock Forecasting & Dynamic Trading Strategy** — IEEE-published research across 11 stocks, 8 sectors, and four rebalancing windows.

Each project page separates verified outcomes, methods, practical implications, limitations, and team attribution.

## Repository structure

- `_pages/` — homepage, portfolio index, CV, publications, and utility pages
- `_portfolio/` — public project case studies
- `_publications/` — peer-reviewed publication records
- `files/projects/` — sanitized, lightweight project artifacts
- `tests/` — automated checks for claims, attribution, privacy boundaries, and template cleanup

Large raw datasets, generated model/search artifacts, virtual environments, caches, and executed notebook outputs are not stored here.

## Validate locally

Run the content tests:

```bash
python3 -m unittest discover -s tests -v
```

Build in an isolated Ruby 3.3 container:

```bash
docker run --rm \
  -v "$PWD":/srv/jekyll \
  -v portfolio_bundle_cache:/usr/local/bundle \
  -w /srv/jekyll \
  ruby:3.3 \
  bash -lc 'bundle install && bundle exec jekyll build'
```

The generated site is written to `_site/`.

## Public-content boundary

Confidential client work, restricted project materials, credentials, local paths, and private source data are intentionally excluded from this public repository. Only evidence-backed claims from reviewed public artifacts are published.

## Theme

The site is built with the open-source [Academic Pages](https://academicpages.github.io/) Jekyll theme and retains its MIT license.
