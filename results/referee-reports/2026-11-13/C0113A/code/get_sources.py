"""Fetch public papers; keep only extracted text, never a PDF file."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import json, hashlib, datetime, sys, subprocess
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parents[1]
def fetch(name,url):
    target=ROOT/'sources'/f'{name}.txt'
    r=requests.get(url,timeout=90); r.raise_for_status()
    raw=r.content
    if raw.startswith(b'%PDF'):
        converted=subprocess.run(['pdftotext','-layout','-','-'],input=raw,stdout=subprocess.PIPE,check=True).stdout.decode('utf-8')
        pages=[f'\n\n=== PDF PAGE {i+1} (printed page may differ) ===\n\n'+page for i,page in enumerate(converted.split('\f')) if page.strip()]
        body=''.join(pages)
    else:
        body=r.text
    body=''.join(c for c in body if ord(c)>=32 or c in '\n\t')
    target.write_text(f'SOURCE URL: {url}\nRETRIEVED: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\nRESPONSE SHA256: {hashlib.sha256(raw).hexdigest()}\n\n'+body)
    print(json.dumps({'name':name,'url':url,'bytes':len(raw),'text_chars':len(body)}),flush=True)
if __name__=='__main__':
    for i in range(1,len(sys.argv),2):
        try: fetch(sys.argv[i],sys.argv[i+1])
        except Exception as e: print(json.dumps({'name':sys.argv[i],'error':str(e)}),flush=True)
