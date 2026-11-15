"""Retrieve a research source as text, keeping PDF bytes only in memory."""
import argparse
import datetime
import hashlib
import io
import json
import os
from pathlib import Path
from html.parser import HTMLParser

for variable in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[variable] = "1"

import requests
from pypdf import PdfReader


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1
        if tag in ("p", "div", "br", "h1", "h2", "h3", "li"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("name", help="plain-text basename under sources/")
    args = parser.parse_args()
    if Path(args.name).name != args.name or not args.name.endswith(".txt"):
        parser.error("name must be a .txt basename")
    if os.getpriority(os.PRIO_PROCESS, 0) < 10:
        os.setpriority(os.PRIO_PROCESS, 0, 10)
    response = requests.get(args.url, timeout=60)
    response.raise_for_status()
    raw = response.content
    metadata = {"url": args.url, "final_url": response.url,
                "retrieved_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "sha256_received_bytes": hashlib.sha256(raw).hexdigest(),
                "received_bytes": len(raw), "content_type": response.headers.get("Content-Type")}
    if raw.startswith(b"%PDF"):
        reader = PdfReader(io.BytesIO(raw))
        metadata["pdf_page_count"] = len(reader.pages)
        body = "\n\n".join(f"===== PDF PAGE {i + 1} =====\n{page.extract_text()}"
                            for i, page in enumerate(reader.pages))
    else:
        html = TextParser()
        html.feed(response.text)
        body = "".join(html.parts)
    text = json.dumps(metadata, ensure_ascii=False, indent=2) + "\n\n" + body
    Path("sources", args.name).write_text(text, encoding="utf-8")
    print(json.dumps({"saved": args.name, **metadata}, ensure_ascii=False))


if __name__ == "__main__":
    main()
