import json,pathlib,requests,concurrent.futures
qs={
'huang_abs':'https://arxiv.org/abs/1911.03330',
'huang_pdf':'https://arxiv.org/pdf/1911.03330',
'arxiv_stationary_energy':'https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20all:stationary%20AND%20all:percolation&max_results=20&sortBy=submittedDate&sortOrder=descending'
}
def g(k,u):
 try:
  r=requests.get(u,timeout=35);pathlib.Path(k+('.pdf' if r.content.startswith(b'%PDF') else '.txt')).write_bytes(r.content);return {'service':k,'url':u,'status':r.status_code,'bytes':len(r.content),'date':'2026-10-11'}
 except Exception as e:return {'service':k,'url':u,'error':str(e),'date':'2026-10-11'}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:a=list(ex.map(lambda kv:g(*kv),qs.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+a,indent=2));print(json.dumps(a,indent=2))
