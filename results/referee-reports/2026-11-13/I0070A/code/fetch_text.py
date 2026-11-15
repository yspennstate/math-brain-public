"""Fetch scholarly PDFs into memory and save only page-separated plain text."""
import os
os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1')
import sys, io, json, hashlib, datetime, subprocess
from pathlib import Path
import requests
root = Path(__file__).resolve().parents[1]
name, url = sys.argv[1:3]
r = requests.get(url, timeout=90)
r.raise_for_status()
raw = r.content
if not raw.startswith(b'%PDF'):
    raise RuntimeError(f'Not a PDF: {r.status_code}, {r.headers.get("Content-Type")}, {raw[:80]!r}')
p = subprocess.run(['pdftotext','-layout','-','-'], input=raw, capture_output=True, check=True)
body = p.stdout.decode('utf-8')
pages = body.split('\f')
if not pages[-1].strip(): pages.pop()
header = f'SOURCE URL: {url}\nRETRIEVED: {datetime.datetime.now().astimezone().isoformat()}\nPDF SHA256 (bytes never saved): {hashlib.sha256(raw).hexdigest()}\nEXTRACTION: pdftotext -layout; PDF page numbers below are 1-based.\n\n'
text = header + ''.join(f'\n===== PDF PAGE {i} =====\n\n{x}' for i,x in enumerate(pages,1))
(root/'sources'/f'{name}.txt').write_text(text)
entry = {'name':name,'url':url,'final_url':r.url,'pages':len(pages),'sha256_pdf':hashlib.sha256(raw).hexdigest(),'retrieved':datetime.datetime.now().astimezone().isoformat()}
with (root/'data'/'source_manifest.jsonl').open('a') as out: out.write(json.dumps(entry)+'\n')
print(json.dumps(entry))
