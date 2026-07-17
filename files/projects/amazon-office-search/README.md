# Amazon Office Products Search System

This folder contains the sanitized notebook for a team project that combines product search, offline retrieval evaluation, and extractive review summarization.

## Data source

The project uses the public [Amazon Reviews 2023 dataset](https://amazon-reviews-2023.github.io/) maintained by the McAuley Lab at UC San Diego. Download the Office Products review and metadata files from the official source and place their decompressed JSONL versions beside the notebook with these names:

- `Office_Products.jsonl`
- `meta_Office_Products.jsonl`

The raw data is not redistributed in this repository. Review the source site's terms and citation guidance before downloading or reusing it.

## Environment

The notebook uses:

- Python 3.10+
- pandas
- NumPy
- SciPy
- scikit-learn
- joblib
- Matplotlib
- Flask

Create an isolated environment and install the packages above before running the notebook.

## Workflow

Run the notebook from top to bottom to:

1. parse and clean product metadata and reviews;
2. build product text representations;
3. fit a 50,000-term TF-IDF vocabulary;
4. index 104,259 products in a sparse matrix;
5. rank products with cosine similarity;
6. generate extractive review summaries;
7. evaluate 200 title queries; and
8. launch the optional Flask search interface.

## Evaluation definitions

- **Hit@10:** share of evaluation queries whose expected product appears in the top ten results.
- **MRR@10:** mean reciprocal rank of the expected product, truncated after rank ten.
- **nDCG@10:** normalized discounted cumulative gain through rank ten.

The reviewed run achieved 98.0% Hit@10, 92.45% MRR@10, and 93.85% nDCG@10. Those figures come from the saved project evaluation and are not recomputed automatically when the cleared notebook is opened.

## Intentionally excluded

To keep the portfolio safe and lightweight, this repository does not include:

- raw Amazon datasets;
- generated product or review tables;
- TF-IDF matrices and fitted vectorizers;
- pickle, joblib, or NumPy index artifacts;
- virtual environments, IDE settings, or caches; or
- executed notebook outputs containing raw review text.

## Attribution

Team project. The notebook and results are published as shared project work and do not claim sole ownership by any one contributor.
