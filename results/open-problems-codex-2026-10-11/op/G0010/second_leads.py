from pathlib import Path
import json,urllib.request,concurrent.futures
queries={'hutchcroft_l2_pdf':'https://arxiv.org/pdf/1904.05804','hutchcroft_universal_pdf':'https://arxiv.org/pdf/2008.11197'}
def f(item):
 key,url=item
 try:
  with urllib.request.urlopen(url,timeout=40) as r:d=r.read();status=r.status
  Path(key+'.pdf').write_bytes(d)
  import pymupdf
  doc=pymupdf.open(key+'.pdf');s='\n'.join(f'--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc));Path(key+'.txt').write_text(s,encoding='utf-8')
  return {'service':key,'url':url,'date':'2026-10-12','status':status,'bytes':len(d)}
 except Exception as e:return {'service':key,'url':url,'date':'2026-10-12','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(f,queries.items()))
p=Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+r,indent=2));print(json.dumps(r,indent=2))
for key in queries:
 f=Path(key+'.txt')
 if not f.exists():continue
 s=f.read_text(encoding='utf-8')
 for term in ['finite graph','largest cluster','q→q','tree-graph']:
  at=s.find(term);print(key,term,at,s[max(0,at-300):at+1300] if at>=0 else '')
