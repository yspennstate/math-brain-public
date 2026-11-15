"""Fetch PDFs into memory; retain only page-delimited text and provenance."""
import io, json, hashlib, datetime, sys, time
from pathlib import Path
import requests
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
def fetch(name,url):
    out=ROOT/'sources'/f'{name}.txt'
    if out.exists(): return
    r=requests.get(url,timeout=20); r.raise_for_status()
    if not r.content.startswith(b'%PDF'): raise ValueError((url,r.headers.get('Content-Type'),r.text[:120]))
    pages=PdfReader(io.BytesIO(r.content)).pages
    txt='SOURCE URL: '+url+'\nFETCHED: '+datetime.datetime.now().astimezone().isoformat()+'\nPDF SHA256 (bytes not retained): '+hashlib.sha256(r.content).hexdigest()+'\n'
    for i,p in enumerate(pages,1): txt+=f'\n\n===== PDF PAGE {i} =====\n'+(p.extract_text() or '')
    out.write_text(''.join(c if ord(c)>=32 or c in '\n\t' else ' ' for c in txt))
    print(name,len(pages),len(txt),flush=True)
if __name__=='__main__':
    for name,url in zip(sys.argv[1::2],sys.argv[2::2]):
        try: fetch(name,url)
        except Exception as e: print(name,type(e).__name__,str(e),flush=True)
