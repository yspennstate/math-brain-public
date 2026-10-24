import requests, concurrent.futures, json
from pathlib import Path
import pymupdf
root=Path(__file__).parent
def fetch(item):
 name,ident=item
 url='https://arxiv.org/pdf/'+ident
 try:
  r=requests.get(url,timeout=30); r.raise_for_status()
  (root/(name+'.pdf')).write_bytes(r.content)
  doc=pymupdf.open(stream=r.content,filetype='pdf'); pages=[p.get_text() for p in doc]
  text='\n'.join(pages); (root/(name+'.txt')).write_text(text,encoding='utf-8')
  hits=[(i+1,line) for i,p in enumerate(pages) for line in p.splitlines() if any(term in line.lower() for term in ['ancestor','conjecture 8.3','pmrca','meeting point'])]
  print(name,'pages',len(doc),'hits',hits[:30]); print('\n'.join(pages[:2])[:6000])
  return {'url':url,'status':r.status_code,'pages':len(doc),'hits':hits}
 except Exception as e: return {'url':url,'error':str(e)}
res=list(concurrent.futures.ThreadPoolExecutor(2).map(fetch,[('kou','2512.10761'),('universality','2401.09370')]))
(root/'followup_search.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
