"""Independent primary-source retrieval; PDF responses stay in memory only."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import hashlib, io, json, time, urllib.request
from pathlib import Path
from datetime import datetime, timezone
from pypdf import PdfReader
BASE=Path(__file__).resolve().parents[1]
assert os.getpriority(os.PRIO_PROCESS,0)>=10
PAPERS=['2603.29571v1','1404.1677v1','2611.14475v1','1202.1234v2','1410.6457v1','2011.02907v2','1008.4535v3','1403.3427v1','2108.01794v3','2211.02713v2','2303.16475v1','2405.08608v2','2412.12958v2','2505.00160v3','2606.08913v1','2002.11677v2','1911.07428v1']
def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Independent mathematical referee source audit'}),timeout=70) as r:
        return r.read(),r.geturl(),r.headers.get('Content-Type','')
def save_pdf(name,url):
    raw,final,ct=fetch(url)
    if not raw.startswith(b'%PDF'): raise ValueError((url,ct,raw[:60]))
    reader=PdfReader(io.BytesIO(raw))
    pages=[page.extract_text(extraction_mode='layout').replace('\x00','') for page in reader.pages]
    text='\n\f\n'.join('=== PDF PAGE %d ===\n%s'%(i+1,t) for i,t in enumerate(pages))
    out=BASE/'sources'/f'{name}.txt';out.write_text(text)
    rec={'name':name,'url':url,'final_url':final,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'response_sha256':hashlib.sha256(raw).hexdigest(),'text_sha256':hashlib.sha256(text.encode()).hexdigest(),'pages':len(pages),'bytes':len(raw)}
    with (BASE/'data'/'source_manifest.jsonl').open('a') as f: f.write(json.dumps(rec)+'\n')
    print(name,len(pages),len(raw),flush=True)
if __name__=='__main__':
 import sys
 for ident in sys.argv[1:] or PAPERS:
    if (BASE/'sources'/f'{ident}.txt').exists(): continue
    try:
        save_pdf(ident,'https://arxiv.org/pdf/'+ident)
        body,final,ct=fetch('https://arxiv.org/abs/'+ident)
        (BASE/'sources'/f'{ident}_metadata.txt').write_text(body.decode())
    except Exception as e: print('FAILED',ident,repr(e),flush=True)
