from pathlib import Path
import requests
import pymupdf
u='https://projecteuclid.org/journals/probability-surveys/volume-3/issue-none/Uniqueness-and-non-uniqueness-in-percolation-theory/10.1214/154957806000000096.pdf'
r=requests.get(u,timeout=40)
print(r.status_code,len(r.content),flush=True)
Path('source.pdf').write_bytes(r.content)
try:
 d=pymupdf.open('source.pdf')
 Path('source.txt').write_text('\n'.join(p.get_text() for p in d),encoding='utf-8')
 for i,p in enumerate(d):
  t=p.get_text()
  if 'monotonic' in t.lower() or i==11 or 'Schonmann' in t: print('PDF PAGE',i+1,'\n',t,flush=True)
except Exception as e: print(e,flush=True)
