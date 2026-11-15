"""Fetch primary sources, retaining plain text only; PDF bytes stay in memory/pipes."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
import hashlib, json, subprocess, sys, urllib.request
import requests
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
class Extract(HTMLParser):
 def __init__(self): super().__init__(); self.out=[]; self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'): self.skip+=1
  if tag in ('p','div','section','h1','h2','h3','h4','h5','h6','li','br'): self.out.append('\n')
 def handle_endtag(self,tag):
  if tag in ('script','style'): self.skip-=1
 def handle_data(self,d):
  if not self.skip:self.out.append(d)
def fetch(name,url,kind):
 r=requests.get(url,timeout=45,headers={'User-Agent':'Research-source-check/1.0'}); r.raise_for_status(); b=r.content
 if kind=='pdf':
  if not b.startswith(b'%PDF'):raise ValueError('not PDF')
  txt=subprocess.run(['pdftotext','-layout','-','-'],input=b,stdout=subprocess.PIPE,check=True).stdout.decode()
 else:
  p=Extract();p.feed(b.decode('utf-8',errors='replace'));txt=''.join(p.out)
 header=f'SOURCE URL: {url}\nRETRIEVED: 2026-11-13\nRaw response SHA256: {hashlib.sha256(b).hexdigest()}\nText extraction: '+('pdftotext -layout; form-feed separates PDF pages' if kind=='pdf' else 'HTMLParser text')+'\n\n'
 (ROOT/'sources'/f'{name}.txt').write_text(header+txt)
 print(name,len(b),len(txt),flush=True)
if __name__=='__main__':
 for row in json.loads(sys.argv[1]):
  try:fetch(*row)
  except Exception as e: print(row[0],type(e).__name__,str(e),flush=True)
