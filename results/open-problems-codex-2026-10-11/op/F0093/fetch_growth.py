import urllib.request
from pathlib import Path
url='https://arxiv.org/pdf/math/0012108'
try:
 data=urllib.request.urlopen(url,timeout=30).read();Path('bartholdi_growth.pdf').write_bytes(data)
 import pymupdf
 doc=pymupdf.open('bartholdi_growth.pdf');s='\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc));Path('bartholdi_growth.txt').write_text(s,encoding='utf8');print(s[:11000]);status='OK'
except Exception as e:status=str(e)
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n- 2026-10-12 fetch Laurent Bartholdi growth paper: '+url+'; '+status+'\n')
