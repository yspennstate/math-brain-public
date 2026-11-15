"""Fetch the primary sources used by this attempt and record hashes."""
from pathlib import Path
import urllib.request,hashlib,json,subprocess
p=Path('sources');p.mkdir(exist_ok=True)
urls={'gu_dpp':'https://sevenkplus.com/data/dpp.pdf','lyons_2003':'https://www.numdam.org/item/10.1007/s10240-003-0016-0.pdf','lyons_errata':'https://rdlyons.pages.iu.edu/errata/bases.pdf','borcea_branden_liggett':'https://arxiv.org/pdf/0707.2340','lyons_2014':'https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf'}
rows={}
for name,url in urls.items():
 f=p/(name+'.pdf')
 try:
  with urllib.request.urlopen(url,timeout=35) as r:f.write_bytes(r.read())
  subprocess.run(['pdftotext','-layout',str(f),str(f.with_suffix('.txt'))],check=True)
  rows[name]=dict(url=url,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),status='downloaded')
 except Exception as e:rows[name]=dict(url=url,status='error',error=str(e))
 print(name,rows[name]['status'],flush=True)
(p/'manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
