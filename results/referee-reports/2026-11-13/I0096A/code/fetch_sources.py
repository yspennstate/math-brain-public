"""Download papers as plain text. PDF bytes exist in memory only.

Run: OPENBLAS_NUM_THREADS=1 nice -n 10 python3 code/fetch_sources.py
"""
import io
import json
import os
import re
import time
from pathlib import Path
import urllib.request
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PAPERS = {
    'randomstrasse_2603.29571v1': 'https://arxiv.org/pdf/2603.29571v1',
    'balan_wang_1308.4718v1': 'https://arxiv.org/pdf/1308.4718v1',
    'balan_wang_published': 'https://www.cscamm.umd.edu/publications/ACHA2015paper_CS-16-05.pdf',
    'prior_2607.06249v1': 'https://arxiv.org/pdf/2607.06249v1',
    'haggblom_2609.28198v1': 'https://arxiv.org/pdf/2609.28198v1',
    'yang_wen_prior_2608.07410v1': 'https://arxiv.org/pdf/2608.07410v1',
}

def fetch(name, url):
    target = ROOT / 'sources' / (name + '.txt')
    if target.exists():
        return {'name': name, 'url': url, 'status': 'already saved'}
    req = urllib.request.Request(url, headers={'User-Agent': 'Research text retrieval; no PDF persistence'})
    with urllib.request.urlopen(req, timeout=75) as r:
        raw = r.read(30_000_000)
    reader = PdfReader(io.BytesIO(raw))
    text = '\n\n'.join(f'===== PDF PAGE {i+1} =====\n{p.extract_text()}' for i, p in enumerate(reader.pages))
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', ' ', text)
    target.write_text(f'SOURCE URL: {url}\nRetrieved UTC: {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())}\n\n' + text)
    return {'name': name, 'url': url, 'status': 'saved plain text', 'pages': len(reader.pages), 'characters': len(text)}

if __name__ == '__main__':
    (ROOT / 'sources').mkdir(exist_ok=True)
    (ROOT / 'data').mkdir(exist_ok=True)
    import sys
    papers = PAPERS if len(sys.argv) == 1 else {sys.argv[1]: sys.argv[2]}
    for name, url in papers.items():
        try:
            result = fetch(name, url)
        except Exception as e:
            result = {'name': name, 'url': url, 'error': str(e)}
        with (ROOT / 'data' / 'source_manifest.jsonl').open('a') as f:
            f.write(json.dumps(result) + '\n')
        print(json.dumps(result), flush=True)
