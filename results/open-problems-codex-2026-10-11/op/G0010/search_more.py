import urllib.request, urllib.parse, concurrent.futures,json,pathlib,xml.etree.ElementTree as E
urls={
'openalex_retry':'https://api.openalex.org/works?search='+urllib.parse.quote('2608.19145')+'&per-page=5',
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2608.19145',
'openalex_citations':'https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2608.19145&per-page=25',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('The critical probability for percolation on finite graphs')+'&limit=10&fields=title,year,externalIds',
'arxiv_later':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:percolation AND submittedDate:[20260819 TO 20261013]')+'&max_results=100&sortBy=submittedDate&sortOrder=descending',
'github_exact':'https://api.github.com/search/repositories?q='+urllib.parse.quote('"2608.19145"')}
def f(it):
 n,u=it
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'ResearchVerification/1.0'}),timeout=30) as r: d=r.read();code=r.status
  pathlib.Path(n+('.xml' if n.startswith('arxiv') else '.json')).write_bytes(d)
  return dict(service=n,url=u,status=code,bytes=len(d),date='2026-10-12')
 except Exception as e:return dict(service=n,url=u,error=str(e),date='2026-10-12')
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(f,urls.items()))
p=pathlib.Path('search_log.json'); old=json.loads(p.read_text());p.write_text(json.dumps(old+r,indent=2));print(json.dumps(r,indent=2))
if pathlib.Path('arxiv_later.xml').exists():
 ns={'a':'http://www.w3.org/2005/Atom'}
 for e in E.parse('arxiv_later.xml').getroot().findall('a:entry',ns):print(e.find('a:published',ns).text,e.find('a:id',ns).text,' '.join(e.find('a:title',ns).text.split()))
