"""Fetch arXiv HTML into memory and save plain text only. No PDFs/images."""
import hashlib
import json
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


class Plain(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0
        self.math = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'math':
            attrs = dict(attrs)
            if self.math == 0:
                self.parts.append(' $' + attrs.get('alttext', '') + '$ ')
            self.math += 1
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'li', 'tr'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
        if tag == 'math':
            self.math -= 1
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'li', 'tr'):
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.skip and not self.math:
            self.parts.append(data)


records = []
for identifier in ('2609.02820', '2609.02829'):
    url = f'https://arxiv.org/html/{identifier}v1'
    req = Request(url, headers={'User-Agent': 'I0006B source verification'})
    with urlopen(req, timeout=45) as response:
        raw = response.read()
    parser = Plain()
    parser.feed(raw.decode('utf-8'))
    lines = [' '.join(line.split()) for line in ''.join(parser.parts).splitlines()]
    plain = '\n'.join(line for line in lines if line) + '\n'
    path = ROOT / 'sources' / f'{identifier}v1-html.txt'
    path.write_text(f'URL: {url}\nRetrieved UTC: {datetime.now(timezone.utc).isoformat()}\n\n' + plain)
    records.append({'url': url, 'html_bytes_in_memory': len(raw),
                    'saved_text': str(path.relative_to(ROOT)),
                    'sha256_saved': hashlib.sha256(path.read_bytes()).hexdigest()})
for path in sorted((ROOT / 'sources').glob('*')):
    if path.name.endswith('.txt') and not path.name.endswith('-html.txt'):
        records.append({'pre_staged_text': str(path.relative_to(ROOT)),
                        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                        'form_feed_pages': path.read_text().count('\f') + 1})
(ROOT / 'data' / 'source_manifest.json').write_text(json.dumps(records, indent=2) + '\n')
print(json.dumps(records, indent=2))
