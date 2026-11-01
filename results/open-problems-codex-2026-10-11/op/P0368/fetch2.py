import urllib.request,concurrent.futures,pathlib,json
urls={
'arxiv_retry.xml':'http://export.arxiv.org/api/query?search_query=ti:frozen+AND+all:percolation&max_results=30',
'openalex_source.json':'https://api.openalex.org/works/https://doi.org/10.1214/21-AOP1507',
'openalex_citing.json':'https://api.openalex.org/works?filter=cites:doi:10.1214/21-AOP1507&per_page=100',
'crossref_later.json':'https://api.crossref.org/works?query=frozen%20percolation%20endogeny&filter=from-pub-date:2019-10-01&rows=50',
'semantic_retry.json':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/21-AOP1507/citations?fields=title,year,externalIds&limit=100',
'arxiv_html.html':'https://arxiv.org/html/1910.09213',
'author.html':'https://staff.utia.cas.cz/swart/research.html'}
def f(it):
 n,u=it
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as r:d=r.read()
  pathlib.Path(n).write_bytes(d);return [n,u,len(d),'OK']
 except Exception as e:return[n,u,0,str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:out=list(ex.map(f,urls.items()))
pathlib.Path('search_log2.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
