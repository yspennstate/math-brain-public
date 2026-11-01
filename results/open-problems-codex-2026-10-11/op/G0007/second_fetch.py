import requests,pathlib,json,concurrent.futures
q={
'broman_arxiv':'https://export.arxiv.org/api/query?search_query=au:Broman%20AND%20au:Steif&max_results=30',
'broman_crossref':'https://api.crossref.org/works?query.author=Broman%20Steif&query=contact%20process%20movability&rows=8',
'noise_arxiv':'https://export.arxiv.org/api/query?search_query=all:%22contact%20process%22%20AND%20(all:movability%20OR%20all:thinning%20OR%20all:sharpness)&max_results=30&sortBy=submittedDate&sortOrder=descending'
}
def get(k,u):
 try:
  r=requests.get(u,timeout=40);pathlib.Path('second_'+k+'.txt').write_bytes(r.content);return {'service':k,'url':u,'date':'2026-10-11','status':r.status_code,'bytes':len(r.content)}
 except Exception as e:return {'service':k,'url':u,'date':'2026-10-11','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:a=list(ex.map(lambda kv:get(*kv),q.items()))
pathlib.Path('second_search_log.json').write_text(json.dumps(a,indent=2));print(json.dumps(a,indent=2))
