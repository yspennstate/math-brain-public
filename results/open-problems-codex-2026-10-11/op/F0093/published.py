import json,urllib.request
from pathlib import Path
x=json.loads(Path('crossref.response').read_text())['message']['items'][0]
print('Crossref links',x.get('link'),x.get('URL'))
url='https://alea.impa.br/articles/v20/20-42.pdf'
try:
 data=urllib.request.urlopen(url,timeout=35).read();Path('alea_20_42.pdf').write_bytes(data)
 import pymupdf
 d=pymupdf.open('alea_20_42.pdf');text='\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d));Path('alea_20_42.txt').write_text(text,encoding='utf8')
 print(text[:450]);i=text.find('Question 1.5');print(text[i:i+1500]);status='OK'
except Exception as e:status=str(e)
with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n- Published ALEA PDF fetch, 2026-10-12: '+url+'; '+status+'\n')
print(status)
