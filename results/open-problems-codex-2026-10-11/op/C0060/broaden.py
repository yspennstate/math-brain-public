import urllib.request,urllib.parse,pathlib,concurrent.futures,json,xml.etree.ElementTree as ET
root=pathlib.Path(__file__).resolve().parent
jobs=[]
for name,q in [('arxiv_general','all:interlacements AND (all:graphs OR all:fractal)'),('arxiv_gasket','all:"vacant set" AND all:gasket'),('arxiv_positive','all:interlacements AND all:positivity'),('arxiv_prevost','au:Prevost AND all:percolation')]:
 jobs.append((name,'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote(q)+'&max_results=100&sortBy=submittedDate&sortOrder=descending'))
for name,q in [('crossref_general','vacant set random interlacements transient graphs'),('crossref_book','An introduction to random interlacements Drewitz Rath Sapozhnikov')]: jobs.append((name,'https://api.crossref.org/works?query.bibliographic='+urllib.parse.quote(q)+'&rows=30'))
jobs.extend([('openalex_retry','https://api.openalex.org/works?search=interlacements&per_page=50'),('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/search?query=vacant%20interlacements&limit=30&fields=title,authors,year,url,externalIds')])
def fetch(job):
 name,url=job
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'research-check/1.0'}),timeout=45) as r: b=r.read()
  (root/(name+('.xml' if name.startswith('arxiv') else '.json'))).write_bytes(b)
  result=f'{name}: OK {len(b)}'
  if name.startswith('arxiv'):
   d=ET.fromstring(b); ns={'a':'http://www.w3.org/2005/Atom'}
   for e in d.findall('a:entry',ns): result+='\n'+e.findtext('a:id',namespaces=ns)+' '+e.findtext('a:title',namespaces=ns).replace('\n',' ')
  elif name.startswith('crossref'):
   for e in json.loads(b)['message']['items']: result+='\n'+str(e.get('title'))+' '+e.get('DOI','')
 except Exception as e: result=f'{name}: ERROR {e}'
 with (root/'LITERATURE.md').open('a',encoding='utf8') as f: f.write(f'\n- 2026-10-11 | {name} | `{url}` | {result.splitlines()[0]}\n')
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 for x in ex.map(fetch,jobs): print(x)
