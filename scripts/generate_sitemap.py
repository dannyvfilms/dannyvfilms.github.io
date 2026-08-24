#!/usr/bin/env python3
"""Generate the sitemap for the static GitHub Pages site."""

from pathlib import Path
from xml.sax.saxutils import escape


SITE_ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://dannyvfilms.github.io"
SITEMAP_PATH = SITE_ROOT / "sitemap.xml"


def page_url(page: Path) -> str:
    relative = page.relative_to(SITE_ROOT)
    if relative.parent == Path("."):
        return f"{SITE_URL}/"
    return f"{SITE_URL}/{relative.parent.as_posix().strip('/')}/"


def build_sitemap() -> str:
    urls = sorted(page_url(page) for page in SITE_ROOT.rglob("index.html"))
    entries = "\n".join(
        f"  <url>\n    <loc>{escape(url)}</loc>\n  </url>" for url in urls
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n"
        "</urlset>\n"
    )


if __name__ == "__main__":
    SITEMAP_PATH.write_text(build_sitemap(), encoding="utf-8")
    print(f"Wrote {SITEMAP_PATH}")
