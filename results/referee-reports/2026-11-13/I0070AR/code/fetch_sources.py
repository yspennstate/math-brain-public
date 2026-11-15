"""Independent source fetch: keep plain text only, never create a PDF file."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import sys, subprocess, hashlib, json, datetime
from pathlib import Path
import requests
root = Path(__file__).resolve().parents[1]
name, url = sys.argv[1:3]
r = requests.get(url, timeout=55)
r.raise_for_status()
raw = r.content
if not raw.startswith(b'%PDF'):
    raise ValueError(f'Expected PDF bytes; got {r.headers.get("Content-Type")}')
body = subprocess.run(['pdftotext','-layout','-','-'], input=raw, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.decode()
pages = body.split('\f')
if not pages[-1].strip(): pages.pop()
record = dict(name=name,url=url,final_url=r.url,retrieved=datetime.datetime.now().astimezone().isoformat(),pdf_sha256=hashlib.sha256(raw).hexdigest(),pages=len(pages))
output = json.dumps(record,ensure_ascii=False)+'\n\n'+''.join(f'\n===== PDF PAGE {i} =====\n\n{p}' for i,p in enumerate(pages,1))
(root/'sources'/f'{name}.txt').write_text(output)
record['text_sha256']=hashlib.sha256(output.encode()).hexdigest()
with (root/'data'/'sources.jsonl').open('a') as f: f.write(json.dumps(record)+'\n')
print(json.dumps(record))
