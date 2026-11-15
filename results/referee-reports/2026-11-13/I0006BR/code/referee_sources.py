"""Independent live retrieval. Persist UTF-8 text only; never write PDF bytes."""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


class PlainMath(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0
        self.in_math = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag == 'math':
            self.in_math += 1
            self.parts.append(' ' + dict(attrs).get('alttext', '') + ' ')
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'li', 'tr', 'br'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden -= 1
        if tag == 'math':
            self.in_math -= 1

    def handle_data(self, data):
        if not self.hidden and not self.in_math:
            self.parts.append(data)

    def result(self):
        return '\n'.join(' '.join(s.split()) for s in ''.join(self.parts).splitlines() if s.strip()) + '\n'


def main():
    manifest = []
    for ident in ('2609.02829', '2609.02820'):
        for kind, url in (
            ('listing', f'https://arxiv.org/abs/{ident}'),
            ('v1', f'https://arxiv.org/html/{ident}v1'),
        ):
            with urlopen(Request(url, headers={'User-Agent': 'Independent mathematical referee source verification'}), timeout=60) as res:
                payload = res.read()
                content_type = res.headers.get('Content-Type', '')
            assert 'html' in content_type, content_type
            parser = PlainMath()
            parser.feed(payload.decode('utf-8'))
            output = parser.result()
            target = ROOT / 'sources' / f'{ident}-{kind}-referee-live.txt'
            target.write_text(output)
            manifest.append(dict(url=url, retrieved_utc=datetime.now(timezone.utc).isoformat(),
                                 sha256_response=hashlib.sha256(payload).hexdigest(),
                                 sha256_text=hashlib.sha256(output.encode()).hexdigest(),
                                 output=str(target.relative_to(ROOT)), response_type=content_type))
            print(target.name, len(output))
    (ROOT / 'data' / 'referee_sources.json').write_text(json.dumps(manifest, indent=2) + '\n')


def literature():
    items = [
        ('rwrs-gantert-koenig-shi.txt', 'https://www.wias-berlin.de/people/koenig/www/RWRSDev.pdf'),
        ('swiss-cheese-listing.txt', 'https://arxiv.org/abs/math/0103238'),
        ('lifshits-transition-listing.txt', 'https://arxiv.org/abs/cond-mat/0310389'),
        ('lifshits-anisotropic-listing.txt', 'https://arxiv.org/abs/math-ph/0310033'),
        ('bou-rabee-publications.txt', 'https://nitromannitol.github.io/'),
        ('panagiotis-publications.txt', 'https://sites.google.com/view/christoforos-panagiotis/'),
        ('earlier-sandpile-2604.13968.txt', 'https://arxiv.org/html/2604.13968v1'),
    ]
    records = []
    for name, url in items:
        try:
            with urlopen(Request(url, headers={'User-Agent': 'Independent mathematical referee source verification'}),timeout=45) as response:
                payload = response.read()
                content_type = response.headers.get('Content-Type', '')
            if payload.startswith(b'%PDF'):
                # Pipes only: the PDF is never stored on the filesystem.
                output = subprocess.run(['pdftotext','-layout','-','-'],input=payload,
                                        stdout=subprocess.PIPE,check=True).stdout.decode('utf-8')
            else:
                parser = PlainMath()
                parser.feed(payload.decode('utf-8'))
                output = parser.result()
            (ROOT/'sources'/name).write_text(output)
            records.append(dict(url=url,output=name,content_type=content_type,
                retrieved_utc=datetime.now(timezone.utc).isoformat(),
                sha256_text=hashlib.sha256(output.encode()).hexdigest()))
            print(name,len(output))
        except Exception as exc:
            records.append(dict(url=url,error=str(exc)))
            print(name,type(exc).__name__,str(exc))
    (ROOT/'data'/'referee_literature_sources.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__ == '__main__':
    import sys
    literature() if '--literature' in sys.argv else main()
