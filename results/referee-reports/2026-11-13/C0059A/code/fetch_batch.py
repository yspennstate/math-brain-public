#!/usr/bin/env python3
"""Download papers in memory; at most three workers, plain text output only."""
import io,json,hashlib,urllib.request,subprocess
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
items=[
('budd_curien_geometry','https://arxiv.org/pdf/1602.01328'),
('budd_curien_marzouk_cauchy','https://jep.centre-mersenne.org/item/10.5802/jep.82.pdf'),
('curien_marzouk_subdiffusive','https://cmarzouk.perso.math.cnrs.fr/Articles/Sous_diff.pdf'),
('curien_marzouk_roundish','https://cmarzouk.perso.math.cnrs.fr/Articles/Roundish.pdf'),
('gurel_gurevich_nachmias','https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p10-p.pdf'),
('bjornberg_stefansson','https://sigurdur.hi.is/files/robpm.pdf'),
('curien_saintflour','https://www.dropbox.com/scl/fi/gn449ms8xsekqmctyav4o/StFlour.pdf?rlkey=7vie1up33jwjnena818gsy4y6&dl=1'),
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
Path('data/fetch_manifest.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results:print(json.dumps(r),flush=True)
