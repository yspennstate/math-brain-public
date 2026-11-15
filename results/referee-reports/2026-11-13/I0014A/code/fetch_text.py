"""Download text, or convert a PDF in RAM to text; never persist PDF bytes."""
import argparse, hashlib, io, json, os, subprocess, tarfile, urllib.request
from datetime import datetime, timezone
from pathlib import Path
os.environ.update(OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1', MKL_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(); p.add_argument('url'); p.add_argument('name'); p.add_argument('--tex',action='store_true'); a=p.parse_args()
r=urllib.request.urlopen(a.url,timeout=45); b=r.read(30_000_000)
meta={'url':a.url,'retrieved_utc':datetime.now(timezone.utc).isoformat(),'content_type':r.headers.get('content-type'),'bytes':len(b),'sha256_download':hashlib.sha256(b).hexdigest()}
if a.tex:
 with tarfile.open(fileobj=io.BytesIO(b), mode='r:*') as t:
  parts=[]
  for m in t.getmembers():
   if m.isfile() and m.name.endswith(('.tex','.bbl','.bib')):
    parts.append('\n===== '+m.name+' =====\n'+t.extractfile(m).read().decode('utf-8',errors='replace'))
 out=''.join(parts)
elif b.startswith(b'%PDF'):
 run=subprocess.run(['/opt/homebrew/bin/pdftotext','-layout','-','-'],input=b,capture_output=True,check=True)
 out=run.stdout.decode('utf-8'); meta['pdf_pages']=out.count('\f'); meta['conversion']='pdftotext -layout; PDF held only in RAM'
else:
 from html.parser import HTMLParser
 class Plain(HTMLParser):
  def __init__(self): super().__init__(); self.out=[]; self.skip=0
  def handle_starttag(self,tag,attrs):
   if tag in ('script','style'): self.skip+=1
   if tag in ('p','div','section','h1','h2','h3','li','br'): self.out.append('\n')
  def handle_endtag(self,tag):
   if tag in ('script','style'): self.skip=max(0,self.skip-1)
  def handle_data(self,d):
   if not self.skip: self.out.append(d)
 parser=Plain();parser.feed(b.decode('utf-8',errors='replace'));out=''.join(parser.out)
f=ROOT/'sources'/a.name
f.write_text(out)
meta['text_sha256']=hashlib.sha256(out.encode()).hexdigest()
(ROOT/'data'/(a.name+'.json')).write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta))
