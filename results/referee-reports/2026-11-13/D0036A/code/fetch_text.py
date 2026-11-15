"""Fetch sources, keeping only text; PDF bytes are parsed exclusively in memory."""
import argparse
import io
import json
import os
from pathlib import Path
import resource
import subprocess
import time
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('name')
p.add_argument('url')
p.add_argument('--html', action='store_true')
a = p.parse_args()
start = time.time()
r = requests.get(a.url, timeout=75, headers={'User-Agent':'D0036 scholarly source text extraction'})
r.raise_for_status()
if r.content.startswith(b'%PDF') or not a.html:
    assert r.content.startswith(b'%PDF'), (r.status_code,r.headers.get('content-type'))
    # pdftotext via pipes produces better formula extraction and no PDF file.
    out = subprocess.run(['pdftotext','-layout','-','-'], input=r.content, capture_output=True, check=True).stdout.decode('utf-8')
    if not out.strip(): out = '[Image-only PDF: text extraction returned no readable text. No PDF or images retained.]'
    pages = out.split('\f')
    text = '\n'.join(f'\n===== PDF PAGE {i+1} =====\n{t}' for i,t in enumerate(pages) if t.strip())
else:
    from html.parser import HTMLParser
    class Plain(HTMLParser):
        def __init__(self):
            super().__init__(); self.parts = []; self.skip = 0
        def handle_starttag(self, tag, attrs):
            if tag in ('script','style'): self.skip += 1
        def handle_endtag(self, tag):
            if tag in ('script','style'): self.skip = max(0,self.skip-1)
        def handle_data(self, data):
            if not self.skip and data.strip(): self.parts.append(data.strip())
    parser = Plain(); parser.feed(r.text); text = '\n'.join(parser.parts)
head = f'SOURCE URL: {a.url}\nFETCHED UTC: {time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())}\nOnly extracted text retained. PDF page markers are 1-based.\n\n'
(ROOT/'sources'/f'{a.name}.txt').write_text(head+text)
print(json.dumps({'name':a.name,'url':a.url,'bytes_received':len(r.content),'text_chars':len(text),'seconds':round(time.time()-start,2)}))
