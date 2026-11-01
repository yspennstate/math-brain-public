from pathlib import Path
import urllib.request,concurrent.futures,xml.etree.ElementTree as E,json
urls={'arxiv_recent_page2':'https://export.arxiv.org/api/query?search_query=all:%22percolation%22+AND+(all:%22two-point%22+OR+all:%22connection%22)+AND+submittedDate:[202601010000+TO+202610112359]&start=100&max_results=100&sortBy=submittedDate&sortOrder=descending','semantic_citing':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2601.00291/citations?fields=title,year,authors,externalIds&limit=100','crossref_exact':'https://api.crossref.org/works?query.title=The%20probability%20of%20connection%20between%20two%20vertices%20cannot%20be%20monotone%20with%20the%20distance&rows=5','openalex_title':'https://api.openalex.org/works?search=%22The%20probability%20of%20connection%20between%20two%20vertices%22&per-page=5'}
def get(k,u):
 try:
  b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'G0008 research'}),timeout=35).read();Path(k+'.response').write_bytes(b);res=f'OK {len(b)}'
 except Exception as e:res=str(e);Path(k+'.error').write_text(res)
 with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write(f'\n- 2026-10-11 {k}: `{u}` — {res}\n')
 return k,res
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:print(list(ex.map(lambda kv:get(*kv),urls.items())))
ns={'a':'http://www.w3.org/2005/Atom'}
if Path('arxiv_recent_page2.response').exists():
 r=E.fromstring(Path('arxiv_recent_page2.response').read_bytes())
 for en in r.findall('a:entry',ns):
  title=en.findtext('a:title',namespaces=ns);summary=en.findtext('a:summary',namespaces=ns)
  print(en.findtext('a:id',namespaces=ns),title)
  if any(w in summary.lower() for w in ['monotonicity','monotonically']):print(summary)
