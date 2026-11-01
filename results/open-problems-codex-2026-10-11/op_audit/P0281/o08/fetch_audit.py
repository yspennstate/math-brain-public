import urllib.request, urllib.parse, json, concurrent.futures
from pathlib import Path
import pymupdf
jobs={
 'bf':'https://arxiv.org/pdf/0804.3035',
 'hks':'https://arxiv.org/pdf/1911.04392v4',
 'source':'https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ.pdf',
 'arxiv':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:TASEP AND (all:concavity OR all:"log-concave")','max_results':30}),
 'openalex':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'TASEP log concavity','per-page':15}),
 'bkm':'https://arxiv.org/pdf/2412.15116',
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityAudit/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read(); status=r.status
  if data.startswith(b'%PDF'):
   Path(name+'.pdf').write_bytes(data)
   doc=pymupdf.open(stream=data,filetype='pdf')
   Path(name+'.txt').write_text('\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
  else: Path(name+'.response').write_bytes(data)
  return {'name':name,'url':url,'status':status,'bytes':len(data)}
 except Exception as e:return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,jobs.items()))
Path('fetch_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
