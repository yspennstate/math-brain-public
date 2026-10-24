from search import fetch,P
import json,fitz
r=fetch(('jacka','https://arxiv.org/pdf/0911.5413'))
(P/'search_jacka_pdf_log.json').write_text(json.dumps([r],indent=2),encoding='utf8');print(r)
try:
 d=fitz.open(P/'jacka.json');t='\n'.join(p.get_text() for p in d);(P/'jacka.txt').write_text(t,encoding='utf8')
 for i,p in enumerate(d):
  s=p.get_text()
  if any(w in s for w in ['2.28','majority','Schramm']):print('PDF page',i+1,s[:6500])
except Exception as e:print(repr(e))
