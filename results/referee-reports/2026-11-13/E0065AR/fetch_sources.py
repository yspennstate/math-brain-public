"""Save text only. PDF responses, when needed, pass through memory/stdin."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS', '1')
from pathlib import Path
import hashlib
import json
import subprocess
import requests
from html.parser import HTMLParser

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'li', 'tr', 'br'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'li', 'tr'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)

ROOT = Path(__file__).resolve().parent

def fetch(name, url):
    r = requests.get(url, timeout=90)
    r.raise_for_status()
    if r.content.startswith(b'%PDF'):
        p = subprocess.run(['pdftotext', '-layout', '-', '-'], input=r.content,
                           capture_output=True, check=True)
        body = p.stdout.decode('utf-8')
        method = 'PDF received in memory; pdftotext stdin/stdout; no PDF saved'
    else:
        parser = TextParser()
        parser.feed(r.text)
        body = '\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip())
        method = 'HTML parsed to plain text; no HTML saved'
    p = ROOT / 'sources' / (name + '.txt')
    p.parent.mkdir(exist_ok=True)
    p.write_text('Source: ' + url + '\nExtraction: ' + method + '\n\n' + body)
    return {'file': str(p.relative_to(ROOT)), 'url': url, 'status': r.status_code,
            'method': method, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
            'characters': len(body)}

if __name__ == '__main__':
    import sys
    print(json.dumps(fetch(sys.argv[1], sys.argv[2]), indent=2))
