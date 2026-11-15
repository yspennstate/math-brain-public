#!/usr/bin/env python3
"""Download papers in memory; at most three workers, plain text output only."""
import io,json,hashlib,urllib.request,subprocess
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
items=[
('kammerer_geodesics','https://arxiv.org/pdf/2412.02666'),
('kammerer_large_cauchy','https://arxiv.org/pdf/2304.01167'),
('kammerer_cle4','https://arxiv.org/pdf/2311.08571'),
('kammerer_o2','https://arxiv.org/pdf/2411.05541'),
('large_faces_2025','https://arxiv.org/pdf/2501.18566'),
('curien_marzouk_subdiffusive','https://msp.org/pmp/2021/2-1/pmp-v2-n1-p01-s.pdf'),
('budd_peeling','https://arxiv.org/pdf/1506.01590'),
('budd_may2017_notes','https://hef.ru.nl/~tbudd/docs/mappeeling.pdf'),
]

def fetch(item):
 name,url=item
 try:
  r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45)
  b=r.read(45_000_000)
  assert b.startswith(b'%PDF'), 'Response is not PDF'
  p=subprocess.run(['pdftotext','-layout','-','-'],input=b,capture_output=True,check=True)
  pages=p.stdout.decode('utf-8').split('\f')
  out='SOURCE: '+url+'\nEXTRACTED UTC: '+datetime.now(timezone.utc).isoformat()+'\nPDF SHA256 (not retained): '+hashlib.sha256(b).hexdigest()+'\n'
  for i,s in enumerate(pages,1):
   if s.strip():out+='\n========== PDF PAGE '+str(i)+' ==========\n\n'+s
  path=Path('sources')/(name+'.txt');path.write_text(out)
  return {'name':name,'url':url,'sha256_pdf':hashlib.sha256(b).hexdigest(),'pages':len(pages)-1,'characters':len(out),'ok':True}
 except Exception as e:return {'name':name,'url':url,'ok':False,'error':str(e)}
with ThreadPoolExecutor(max_workers=3) as pool:
 results=list(pool.map(fetch,items))
Path('data/fetch_manifest_recent.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results:print(json.dumps(r),flush=True)
