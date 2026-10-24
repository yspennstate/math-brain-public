import requests,pathlib,json,concurrent.futures
qs={
'arxiv_tolerance':'https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20(all:%22finite%20energy%22%20OR%20all:%22insertion%20tolerance%22)&max_results=20',
'crossref_tolerance':'https://api.crossref.org/works?query=%22contact%20process%22%20%22finite%20energy%22&rows=5',
'arxiv_critical_tree':'https://export.arxiv.org/api/query?search_query=all:%22invariant%20percolation%22%20AND%20all:tree%20AND%20all:critical&max_results=20'
}
def g(k,u):
 try:
  r=requests.get(u,timeout=35);pathlib.Path(k+'.txt').write_bytes(r.content);return {'service':k,'url':u,'status':r.status_code,'bytes':len(r.content),'date':'2026-10-11'}
 except Exception as e:return {'service':k,'url':u,'error':str(e),'date':'2026-10-11'}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:a=list(ex.map(lambda kv:g(*kv),qs.items()))
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+a,indent=2));print(json.dumps(a,indent=2))
