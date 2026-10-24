from pathlib import Path
import urllib.request, urllib.parse, json, concurrent.futures
root=Path.cwd()
urls={
'survey':'https://arxiv.org/pdf/1204.1895',
'zerner':'https://r.jina.ai/https://projecteuclid.org/journalArticle/Download?urlid=10.1214%2FECP.v7-1060',
'arxiv_search':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"excited random walks" AND (all:"velocity" OR all:"non-transient" OR all:"non-ballistic")')+'&max_results=15',
'openalex_search':'https://api.openalex.org/works?search='+urllib.parse.quote('excited random walks zero velocity non transient')+'&per-page=15',
'openalex_problem':'https://api.openalex.org/works?search='+urllib.parse.quote('excited random walks Problem 4.7')+'&per-page=10',
'one_dimensional':'https://arxiv.org/pdf/1304.7287'
}
def fetch(pair):
 k,u=pair
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'ProbabilityAudit/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read(); status=r.status
  suffix='.pdf' if data.startswith(b'%PDF') else '.txt'
  (root/(k+suffix)).write_bytes(data)
  return {'name':k,'url':u,'status':status,'bytes':len(data),'file':k+suffix}
 except Exception as e: return {'name':k,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,urls.items()))
(root/'retrieval_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
for name in ['survey','one_dimensional']:
 p=root/(name+'.pdf')
 if p.exists():
  try:
   import pymupdf
   doc=pymupdf.open(p); text='\n'.join('PAGE '+str(i+1)+'\n'+page.get_text() for i,page in enumerate(doc)); (root/(name+'_extracted.txt')).write_text(text,encoding='utf-8'); print(name,'pages',len(doc))
  except Exception as e: print('extract',str(e))
