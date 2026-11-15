"""Fetch source PDFs only into RAM; save page-numbered plain text, no PDF files."""
import argparse, datetime, hashlib, io, json, os
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import requests
from pypdf import PdfReader
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('name'); p.add_argument('url')
a = p.parse_args()
r = requests.get(a.url, timeout=90)
r.raise_for_status()
if not r.content.startswith(b'%PDF'):
    raise ValueError('Expected PDF response')
reader = PdfReader(io.BytesIO(r.content))
parts = [f'SOURCE URL: {a.url}\nFETCHED UTC: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\nPDF SHA256 (bytes held in RAM only): {hashlib.sha256(r.content).hexdigest()}\nPAGES: {len(reader.pages)}\n']
for n, page in enumerate(reader.pages, 1):
    parts.append(f'\n\n===== PDF PAGE {n} =====\n\n{page.extract_text(extraction_mode="layout")}\n')
path = ROOT / 'sources' / f'{a.name}.txt'
path.write_text(''.join(parts).replace(chr(0), '[NULL]'))
print(json.dumps({'path':str(path.relative_to(ROOT)), 'pages':len(reader.pages), 'chars':path.stat().st_size}))
