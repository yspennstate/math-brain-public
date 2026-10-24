import requests,json,xml.etree.ElementTree as E,concurrent.futures
from pathlib import Path
jobs={'arxiv_exclusion.xml':'https://export.arxiv.org/api/query?search_query=all:%22competitive%20exclusion%22%20AND%20all:%22contact%22&max_results=100','semantic_stover.json':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06628/citations?limit=100&fields=title,year,authors,abstract','openalex_citing_final.json':'https://api.openalex.org/works?filter=cites:W2057281188&per_page=25&select=id,title,publication_year,doi'}
def f(k,u):
 try:
  r=requests.get(u,timeout=35);Path(k).write_bytes(r.content);a={'date':'2026-10-12','url':u,'file':k,'status':r.status_code}
 except Exception as e:a={'date':'2026-10-12','url':u,'error':str(e)}
 with open('search_log.jsonl','a',encoding='utf8') as g:g.write(json.dumps(a)+'\n')
 print(a,flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(lambda kv:f(*kv),jobs.items()))
ns={'a':'http://www.w3.org/2005/Atom'}
try:
 for e in E.parse('arxiv_exclusion.xml').findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns))
except Exception as e:print(e)
for fn in ['semantic_stover.json','openalex_citing_final.json']:
 o=json.loads(Path(fn).read_text());print(fn,o.get('message',o.get('meta')))
 for e in o.get('data',o.get('results',[])):
  a=e.get('citingPaper',e);print(a.get('title'),a.get('year',a.get('publication_year')),a.get('abstract'))
