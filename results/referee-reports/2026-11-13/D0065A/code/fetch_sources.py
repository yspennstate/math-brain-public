"""Fetch papers into memory; retain only UTF-8 text and provenance, never PDFs."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
import io, json, subprocess, sys, hashlib, datetime
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parents[1]
def fetch(name,url):
    r=requests.get(url,timeout=100); r.raise_for_status()
    raw=r.content
    if not raw.startswith(b'%PDF'): raise ValueError(f'Not PDF: {url}: {raw[:100]}')
    p=subprocess.run(['pdftotext','-layout','-','-'],input=raw,stdout=subprocess.PIPE,check=True)
    pages=p.stdout.decode('utf-8').split('\f')
    if not pages[-1].strip(): pages.pop()
    out=f'Source URL: {url}\nRetrieved UTC: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\nPDF SHA256 (bytes not retained): {hashlib.sha256(raw).hexdigest()}\nExtraction: pdftotext -layout via memory pipes; page numbers below are 1-based PDF pages.\n'
    out+=''.join(f'\n===== PDF PAGE {i} =====\n{t}' for i,t in enumerate(pages,1))
    (ROOT/'sources'/f'{name}.txt').write_text(out)
    print(name, len(pages),'pages',len(out),'text bytes',flush=True)
if __name__=='__main__':
    fetch(sys.argv[1],sys.argv[2])
