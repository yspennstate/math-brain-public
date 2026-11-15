"""Download primary papers to text; PDF bytes never touch the filesystem."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parent
PAPERS = [
    ('2510.20461', 'https://arxiv.org/pdf/2510.20461'),
    ('1205.4584', 'https://arxiv.org/pdf/1205.4584'),
    ('1609.01364', 'https://arxiv.org/pdf/1609.01364'),
    ('0810.4237', 'https://arxiv.org/pdf/0810.4237'),
]

def fetch(name, url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Independent mathematical referee/1.0'})
    with urllib.request.urlopen(req, timeout=75) as response:
        body = response.read()
        final_url = response.url
    if not body.startswith(b'%PDF'):
        raise ValueError(f'{url}: not PDF')
    result = subprocess.run(['pdftotext', '-layout', '-', '-'], input=body,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    content = result.stdout
    content.decode('utf-8')
    (ROOT / 'sources' / (name + '.txt')).write_bytes(content)
    meta = dict(name=name, requested_url=url, final_url=final_url,
                fetched_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                pdf_bytes=len(body), pdf_sha256=hashlib.sha256(body).hexdigest(),
                text_sha256=hashlib.sha256(content).hexdigest(),
                pages=content.count(b'\x0c'))
    with (ROOT / 'sources' / 'manifest.txt').open('a') as stream:
        stream.write(json.dumps(meta) + '\n')
    print(json.dumps(meta), flush=True)

if __name__ == '__main__':
    os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
    (ROOT / 'sources').mkdir(exist_ok=True)
    for name, url in PAPERS:
        try:
            fetch(name, url)
        except Exception as exc:
            print(name, type(exc).__name__, str(exc), flush=True)
