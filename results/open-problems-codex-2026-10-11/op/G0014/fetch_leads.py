import urllib.request,pathlib,json
import pymupdf
root=pathlib.Path(__file__).parent
items={'recent_decoupling':'https://arxiv.org/pdf/2609.27972','chen':'https://arxiv.org/pdf/1402.5864'}
log=[]
for name,url in items.items():
 r={'date':'2026-10-11','service':'arxiv_pdf','url':url}
 try:
  with urllib.request.urlopen(url,timeout=40) as res:data=res.read();r['status']=res.status
  p=root/(name+'.pdf');p.write_bytes(data);doc=pymupdf.open(p)
  (root/(name+'_extracted.txt')).write_text('\n'.join(f'=== PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8');r['pages']=len(doc)
 except Exception as e:r['error']=str(e)
 log.append(r);print(r)
(root/'search_log_round3.json').write_text(json.dumps(log,indent=2),encoding='utf8')
