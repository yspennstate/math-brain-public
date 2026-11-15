"""Retrieve primary sources as plain text; never write PDF or HTML files."""
import hashlib
import io
import json
import os
from pathlib import Path
import re
from html.parser import HTMLParser
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0
        self.in_math = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'math':
            self.in_math += 1
            self.parts.append(attrs.get('alttext', '[math]'))
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr', 'br'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
        if tag == 'math':
            self.in_math -= 1
        if tag in ('p', 'div', 'section', 'li', 'tr'):
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.skip and not self.in_math:
            self.parts.append(data)


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    folder = ROOT / 'sources'
    folder.mkdir(exist_ok=True)
    records = []
    urls = [
        ('dozier_2608.26321v1', 'https://arxiv.org/html/2608.26321v1', 'html'),
        ('dozier_2608.26321v1_pages', 'https://arxiv.org/pdf/2608.26321v1', 'pdf'),
        ('bencs_2608.09729v1', 'https://arxiv.org/html/2608.09729v1', 'html'),
        ('bencs_2608.09729v1_pages', 'https://arxiv.org/pdf/2608.09729v1', 'pdf'),
        ('kempton_1603.05553v1', 'https://arxiv.org/pdf/1603.05553v1', 'pdf'),
        ('alon_birthday', 'https://www.cs.tau.ac.il/~nogaa/PDFS/birthday.pdf', 'pdf'),
    ]
    for name, url, kind in urls:
        record = {'name': name, 'url': url}
        try:
            r = requests.get(url, timeout=45)
            record.update(status=r.status_code, final_url=r.url)
            r.raise_for_status()
            if kind == 'pdf':
                reader = PdfReader(io.BytesIO(r.content))
                body = '\n\n'.join(f'=== PDF PAGE {i+1} ===\n{p.extract_text()}' for i,p in enumerate(reader.pages))
                record['pages'] = len(reader.pages)
            else:
                parser = Text()
                parser.feed(r.text)
                body = re.sub(r'\n[ \t]*\n(?:[ \t]*\n)+', '\n\n', ''.join(parser.parts))
            text = f'Source: {url}\nRetrieved: 2026-11-13\nMethod: {kind}, mathematical alttext retained for HTML; PDF bytes only in RAM.\n\n' + body
            target = folder / (name + '.txt')
            target.write_text(text)
            record.update(file=str(target.relative_to(ROOT)), sha256=hashlib.sha256(target.read_bytes()).hexdigest())
        except Exception as e:
            record['error'] = str(e)
        records.append(record)
        print(json.dumps(record), flush=True)
    (folder / 'retrieval_manifest.txt').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
