import json,urllib.request,concurrent.futures,pathlib
x=json.loads(pathlib.Path('crossref.txt').read_text())
for it in x['message']['items']:
 if it.get('DOI')=='10.1214/aop/1176990844':print(json.dumps(it,indent=2))
qs={'site_locality_html':'https://arxiv.org/html/2609.07026v1','supercritical_html':'https://arxiv.org/html/2603.03257v1'}
def f(x):
 k,u=x
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathResearch/1.0'}),timeout=30) as r:d=r.read()
  pathlib.Path(k+'.txt').write_bytes(d);res={'service':k,'url':u,'bytes':len(d)}
 except Exception as e:res={'service':k,'url':u,'error':str(e)}
 with open('followup_log.jsonl','a',encoding='utf8') as out:out.write(json.dumps({'date':'2026-10-11',**res})+'\n')
 print(res,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(f,qs.items()))
