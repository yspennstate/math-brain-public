import urllib.request,urllib.parse,concurrent.futures,pathlib,json
qs={
'cerf_html':'https://arxiv.org/html/2608.23661v1',
'new_abs':'https://arxiv.org/abs/2610.08682',
'new_html':'https://arxiv.org/html/2610.08682v1',
'openalex_exact':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'doi:https://doi.org/10.48550/arXiv.2608.23661','per-page':5}),
'openalex_tail':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'site percolation finite cluster tail','filter':'from_publication_date:2026-08-24','per-page':30}),
'arxiv_exact':'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"2608.23661" OR (all:"site percolation" AND all:"critical")','max_results':20,'sortBy':'submittedDate','sortOrder':'descending'}),
'github_exact':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"2608.23661"','per_page':10}),
}
def f(x):
 k,u=x
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'MathResearch/1.0'}),timeout=30) as r:d=r.read()
  pathlib.Path(k+'.txt').write_bytes(d); res={'service':k,'url':u,'bytes':len(d)}
 except Exception as e:res={'service':k,'url':u,'error':str(e)}
 with open('LITERATURE.md','a',encoding='utf8') as out:out.write('\n2026-10-11 query: '+json.dumps(res)+'\n')
 print(res,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:list(ex.map(f,qs.items()))
