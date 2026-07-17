import json
import re
import unittest
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_PROJECT_FILES = {
    "amazon-product-search.md",
    "chatgpt-deepseek-sentiment.md",
    "bilstm-stock-strategy.md",
}

FEATURED_PROJECTS = {
    "Amazon Product Search & Review Summarization": "/portfolio/amazon-product-search/",
    "ChatGPT vs. DeepSeek User Sentiment & Product Strategy": "/portfolio/chatgpt-deepseek-sentiment/",
    "BiLSTM Stock Forecasting & Dynamic Trading Strategy": "/portfolio/bilstm-stock-strategy/",
}

FORBIDDEN_PUBLIC_TEXT = (
    "18% higher returns",
    "33% RMSE reduction",
    "Short description of portfolio item",
    "This is an item in your portfolio",
    "This is a sample blog post",
    "Teaching experience 1",
    "University 1, Department",
    "MarshBerry",
    "RIA M&A",
)

REMOVED_SAMPLE_PATHS = (
    ".github/ISSUE_TEMPLATE",
    "CONTRIBUTING.md",
    "_data/authors.yml",
    "_data/comments",
    "_drafts/post-draft.md",
    "_posts/2012-08-14-blog-post-1.md",
    "_posts/2013-08-14-blog-post-2.md",
    "_posts/2014-08-14-blog-post-3.md",
    "_posts/2015-08-14-blog-post-4.md",
    "_posts/2199-01-01-future-post.md",
    "_talks",
    "_teaching",
    "_pages/archive-layout-with-content.md",
    "_pages/collection-archive.html",
    "_pages/markdown.md",
    "_pages/non-menu-page.md",
    "_pages/page-archive.html",
    "_pages/talkmap.html",
    "_pages/talks.html",
    "_pages/teaching.html",
    "_pages/terms.md",
    "_pages/year-archive.html",
    "files/paper1.pdf",
    "files/paper2.pdf",
    "files/paper3.pdf",
    "files/slides1.pdf",
    "files/slides2.pdf",
    "files/slides3.pdf",
    "markdown_generator",
    "talkmap",
    "talkmap.ipynb",
    "talkmap.py",
    "images/3953273590_704e3899d5_m.jpg",
    "images/500x300.png",
    "images/bio-photo-2.jpg",
    "images/bio-photo.jpg",
    "images/editing-talk.png",
    "images/foo-bar-identity-th.jpg",
    "images/foo-bar-identity.jpg",
    "images/image-alignment-1200x4002.jpg",
    "images/image-alignment-150x150.jpg",
    "images/image-alignment-300x200.jpg",
    "images/image-alignment-580x300.jpg",
    "images/paragraph-indent.png",
    "images/paragraph-no-indent.png",
    "images/IMG_1939 2.JPG",
    "images/profile.png",
    "images/site-logo.png",
    "images/manifest.json",
)


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


class PortfolioContentTests(unittest.TestCase):
    def test_homepage_features_the_approved_projects(self):
        homepage = unescape(read_text("_pages/about.md"))
        for title, url in FEATURED_PROJECTS.items():
            with self.subTest(title=title):
                self.assertIn(title, homepage)
                self.assertIn(f'href="{url}"', homepage)
        self.assertIn('<div class="stat-number">98%</div>', homepage)
        self.assertIn("Search Hit@10", homepage)

    def test_navigation_exposes_portfolio_before_publications(self):
        navigation = read_text("_data/navigation.yml")
        self.assertIn('title: "Portfolio"', navigation)
        self.assertIn('title: "Publications"', navigation)
        portfolio_position = navigation.index('title: "Portfolio"')
        publications_position = navigation.index('title: "Publications"')
        self.assertLess(portfolio_position, publications_position)
        self.assertIn("url: /portfolio/", navigation)

    def test_resume_link_targets_the_retained_resume_file(self):
        config = read_text("_config.yml")
        self.assertIn('resume           : "/files/Resume_TENG_LIN.pdf"', config)
        self.assertIn('repository               : "tenglin01/tenglin01.github.io"', config)
        self.assertTrue((ROOT / "files/Resume_TENG_LIN.pdf").is_file())

    def test_head_references_only_existing_favicon_assets(self):
        head = read_text("_includes/head/custom.html")
        self.assertIn("/images/favicon.ico", head)
        self.assertNotIn("manifest.json", head)
        for missing_name in (
            "apple-touch-icon",
            "android-chrome",
            "favicon-16x16",
            "favicon-32x32",
            "favicon-96x96",
        ):
            self.assertNotIn(missing_name, head)

    def test_portfolio_collection_contains_only_real_projects(self):
        actual = {path.name for path in (ROOT / "_portfolio").iterdir() if path.is_file()}
        self.assertEqual(EXPECTED_PROJECT_FILES, actual)

    def test_amazon_page_has_verified_evidence_and_attribution(self):
        self.assertTrue((ROOT / "_portfolio/amazon-product-search.md").is_file())
        page = read_text("_portfolio/amazon-product-search.md")
        for expected in (
            "300,000",
            "104,259",
            "200",
            "98.0%",
            "92.45%",
            "93.85%",
            "Team project",
        ):
            self.assertIn(expected, page)

    def test_sentiment_page_has_verified_evidence_and_attribution(self):
        self.assertTrue((ROOT / "_portfolio/chatgpt-deepseek-sentiment.md").is_file())
        page = read_text("_portfolio/chatgpt-deepseek-sentiment.md")
        for expected in (
            "843,000",
            "12.9%",
            "6.7%",
            "K-means",
            "PCA",
            "five-person team",
        ):
            self.assertIn(expected, page)

    def test_bilstm_page_has_verified_evidence_and_full_citation(self):
        self.assertTrue((ROOT / "_portfolio/bilstm-stock-strategy.md").is_file())
        page = read_text("_portfolio/bilstm-stock-strategy.md")
        for expected in (
            "11 stocks",
            "8 sectors",
            "3-day",
            "5-day",
            "7-day",
            "14-day",
            "Jiayi Liu",
            "Yufeng Yang",
            "Teng Lin",
            "Chuanhui Peng",
            "Yancong Deng",
            "10.1109/MLHMI63000.2024.00013",
        ):
            self.assertIn(expected, page)

    def test_amazon_notebook_is_sanitized_and_small(self):
        project_dir = ROOT / "files/projects/amazon-office-search"
        notebook_path = project_dir / "Office_Products_Search_System.ipynb"
        self.assertTrue(notebook_path.is_file())
        notebook = json.loads(notebook_path.read_text(encoding="utf-8"))

        code_cells = [cell for cell in notebook["cells"] if cell.get("cell_type") == "code"]
        self.assertGreater(len(code_cells), 0)
        for index, cell in enumerate(code_cells):
            with self.subTest(cell=index):
                self.assertEqual([], cell.get("outputs", []))
                self.assertIsNone(cell.get("execution_count"))

        serialized = json.dumps(notebook)
        self.assertNotIn("/Users/", serialized)
        self.assertNotIn("C:\\\\", serialized)

        readme = read_text("files/projects/amazon-office-search/README.md")
        self.assertIn("Team project", readme)
        self.assertIn("Amazon Reviews 2023", readme)

        forbidden_suffixes = {".csv", ".gz", ".pkl", ".joblib", ".npz"}
        for path in project_dir.rglob("*"):
            if not path.is_file():
                continue
            with self.subTest(path=path.name):
                self.assertLess(path.stat().st_size, 5 * 1024 * 1024)
                self.assertNotIn(path.suffix.lower(), forbidden_suffixes)

    def test_template_samples_are_removed(self):
        for relative_path in REMOVED_SAMPLE_PATHS:
            with self.subTest(path=relative_path):
                path = ROOT / relative_path
                if path.is_dir():
                    self.assertFalse(any(candidate.is_file() for candidate in path.rglob("*")))
                else:
                    self.assertFalse(path.exists())

    def test_readme_describes_the_personal_portfolio(self):
        readme = read_text("README.md")
        self.assertTrue(readme.startswith("# Teng Lin Analytics Portfolio"))
        self.assertIn("tenglin01.github.io", readme)
        self.assertIn("Confidential", readme)

    def test_test_suite_is_excluded_from_the_generated_site(self):
        config = read_text("_config.yml")
        self.assertIsNotNone(re.search(r"(?m)^\s+- tests\s*$", config))

    def test_public_content_has_no_placeholder_confidential_or_bad_claims(self):
        content_roots = [
            ROOT / "README.md",
            ROOT / "_pages",
            ROOT / "_portfolio",
            ROOT / "_publications",
            ROOT / "_posts",
            ROOT / "_talks",
            ROOT / "_teaching",
            ROOT / "files/projects",
        ]
        searchable_suffixes = {".md", ".html", ".yml", ".yaml", ".json", ".ipynb", ".txt"}
        texts = []
        for root in content_roots:
            if root.is_file():
                texts.append(root.read_text(encoding="utf-8", errors="ignore"))
            elif root.exists():
                for path in root.rglob("*"):
                    if path.is_file() and path.suffix.lower() in searchable_suffixes:
                        texts.append(path.read_text(encoding="utf-8", errors="ignore"))
        public_text = "\n".join(texts)
        for forbidden in FORBIDDEN_PUBLIC_TEXT:
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, public_text)


if __name__ == "__main__":
    unittest.main()
