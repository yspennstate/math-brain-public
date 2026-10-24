import json,pathlib
for fn in ['crossref_resolution.response','semantic_source.response','resolution_publisher.response']:
 print('\nFILE',fn)
 d=pathlib.Path(fn).read_text(encoding='utf8');
 if fn=='crossref_resolution.response':
  m=json.loads(d)['message'];print(json.dumps({k:m.get(k) for k in ['title','author','published','volume','article-number','DOI','link','reference','URL']},ensure_ascii=False,indent=2))
 else:print(d[:3200])
import pymupdf
D=pymupdf.open('resolution_pdf.pdf')
for i in [7,8,9,10,20,21]:
 if i<len(D): print('PAGE',i+1,D[i].get_text())
