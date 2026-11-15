"""Download PDFs into RAM only and persist extracted plain text, with page labels."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import argparse
import datetime
import hashlib
import io
import json
from pathlib import Path
import requests
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]

def fetch(identifier):
    url = f'https://arxiv.org/pdf/{identifier}'
    response = requests.get(url, timeout=90)
    response.raise_for_status()
    payload = response.content
    if not payload.startswith(b'%PDF'):
        raise ValueError(f'Not a PDF: {url}')
    reader = PdfReader(io.BytesIO(payload))
    pages = [page.extract_text(extraction_mode='layout').replace('\x00', '') for page in reader.pages]
    out = ROOT / 'sources' / f'{identifier}.txt'
    out.parent.mkdir(exist_ok=True)
    out.write_text(f'SOURCE: {url}\nRetrieved: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\nPDF SHA256 (PDF not retained): {hashlib.sha256(payload).hexdigest()}\n' +
                   ''.join(f'\n\n===== PDF PAGE {i+1} =====\n\n{p}' for i, p in enumerate(pages)))
    print(json.dumps({'id': identifier, 'pages': len(pages), 'text': str(out), 'bytes': out.stat().st_size}), flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ids', nargs='+')
    args = parser.parse_args()
    for identifier in args.ids:
        try:
            fetch(identifier)
        except Exception as exc:
            print(json.dumps({'id': identifier, 'error': str(exc)}), flush=True)
