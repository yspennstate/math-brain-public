"""Fetch a paper and retain only page-marked plain text; PDF stays in RAM."""
import io
import os
import sys
import hashlib
import json
import subprocess
from pathlib import Path
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault('OMP_NUM_THREADS', '1')

def main():
    url, name = sys.argv[1:3]
    response = requests.get(url, timeout=90)
    response.raise_for_status()
    raw = response.content
    if not raw.startswith(b'%PDF'):
        raise RuntimeError(f'Expected PDF, got {response.headers.get("content-type")}')
    reader = PdfReader(io.BytesIO(raw))
    extracted = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw,
                               capture_output=True, check=True).stdout.decode()
    chunks = [f'\n===== PDF PAGE {n} =====\n\n' + page
              for n, page in enumerate(extracted.split('\f'), 1) if page.strip()]
    target = ROOT / 'sources' / (name + '.txt')
    target.write_text(''.join(chunks))
    record = {'url': url, 'file': str(target.relative_to(ROOT)), 'pages': len(reader.pages),
              'pdf_sha256': hashlib.sha256(raw).hexdigest(),
              'text_sha256': hashlib.sha256(target.read_bytes()).hexdigest()}
    with (ROOT / 'data' / 'retrievals.jsonl').open('a') as out:
        out.write(json.dumps(record) + '\n')
    print(json.dumps(record))

if __name__ == '__main__':
    main()
