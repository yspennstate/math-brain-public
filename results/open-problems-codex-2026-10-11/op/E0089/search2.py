import urllib.request,urllib.parse,json,pathlib,concurrent.futures
urls={
'oa_retry':'https://api.openalex.org/works?search=Noise%20sensitivity%20in%20bootstrap%20percolation&per_page=10',
'oa_source':'https://api.openalex.org/works/https://arxiv.org/abs/1509.08454',
'crossref_regular':'https://api.crossref.org/works?query='+urllib.parse.quote('bootstrap percolation random regular graph noise')+'&rows=30',
's2_search':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('Noise sensitivity in bootstrap percolation')+'&limit=10&fields=title,year,externalIds',
'arxiv_regular':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"bootstrap percolation" AND all:"regular"')+'&max_results=50',
'oa_citations_search':'https://api.openalex.org/works?filter=cites:W2330601998&per-page=100'
}
def f(k,u):
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'research E0089'}),timeout=40).read();pathlib.Path(k+'.data').write_bytes(b); print(k,'OK',b.decode()[:200]);return [k,u,'OK']
 except Exception as e:print(k,str(e));return [k,u,str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(lambda kv:f(*kv),urls.items()))
pathlib.Path('search_log2.json').write_text(json.dumps({'date':'2026-10-12','results':r},indent=2),encoding='utf8')
