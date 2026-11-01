import json,xml.etree.ElementTree as E,urllib.request,concurrent.futures
from pathlib import Path
ns={'a':'http://www.w3.org/2005/Atom'}
r=E.fromstring(Path('arxiv.response').read_bytes())
for en in r.findall('a:entry',ns):
 print(en.findtext('a:id',namespaces=ns),en.findtext('a:published',namespaces=ns),en.findtext('a:title',namespaces=ns))
x=json.loads(Path('crossref.response').read_bytes())
for it in x['message']['items'][:15]: print(it.get('title'),it.get('DOI'),it.get('published'))
urls={
'arxiv_2015':'https://export.arxiv.org/api/query?search_query=ti:%22remark%20on%20monotonicity%22&max_results=10',
'arxiv_recent':'https://export.arxiv.org/api/query?search_query=all:%22percolation%22+AND+(all:%22two-point%22+OR+all:%22connection%22)+AND+submittedDate:[202601010000+TO+202610112359]&max_results=100&sortBy=submittedDate&sortOrder=descending',
'openalex_source':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2601.00291',
'openalex_retry':'https://api.openalex.org/works?search=monotonicity%20Bernoulli%20bond%20percolation&per_page=10',
'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?query=monotonicity%20Bernoulli%20percolation&limit=10&fields=title,authors,year,externalIds',
'crossref_since':'https://api.crossref.org/works?query=percolation%20two%20point%20monotonicity&filter=from-pub-date:2026-01-01&rows=25',
'github_title':'https://api.github.com/search/repositories?q=%22percolation%22+%22connection%22'}
def get(k,u):
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (mathematics research)'}),timeout=40).read(); Path(k+'.response').write_bytes(b); res=f'OK {len(b)} bytes'
 except Exception as e: res=str(e); Path(k+'.error').write_text(res)
 with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write(f'\n- 2026-10-11 {k}: `{u}` — {res}\n')
 return k,res
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:print(list(ex.map(lambda x:get(*x),urls.items())))
