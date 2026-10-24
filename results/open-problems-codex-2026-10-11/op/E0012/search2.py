import urllib.request,concurrent.futures,pathlib,json,xml.etree.ElementTree as ET
qs={
'arxiv_allelopathy':'https://export.arxiv.org/api/query?search_query=all:allelopathy&max_results=50',
'crossref_allelopathy':'https://api.crossref.org/works?query=allelopathy%20contact%20process&rows=25',
'openalex_retry':'https://api.openalex.org/works?search=allelopathy%20contact%20process&per_page=25',
'openalex_source_correct':'https://api.openalex.org/works/https://doi.org/10.1214/08-AAP590',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:0906.2293/citations?limit=100&fields=title,year,authors,externalIds',
'github_allelopathy':'https://api.github.com/search/repositories?q=allelopathy+contact+process&per_page=20'}
def f(k,u):
 try:
  data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'ResearchAudit/1.0'}),timeout=35).read();pathlib.Path(k+'.json').write_bytes(data)
  return [k,u,'OK',len(data)]
 except Exception as e:return [k,u,'ERROR',str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:r=list(ex.map(lambda kv:f(*kv),qs.items()))
with open('LITERATURE.md','a',encoding='utf8') as out:
 for x in r:out.write('\n2026-10-12 '+repr(x)+'\n')
print(r)
for k,u,st,*_ in r:
 if st!='OK':continue
 if k.startswith('arxiv'):
  ns={'a':'http://www.w3.org/2005/Atom'}
  for e in ET.parse(k+'.json').findall('a:entry',ns):print(e.findtext('a:title',namespaces=ns),e.findtext('a:id',namespaces=ns),e.findtext('a:summary',namespaces=ns))
 elif k.startswith('crossref'):
  for w in json.load(open(k+'.json',encoding='utf8'))['message']['items']:print(w.get('title'),w.get('DOI'),w.get('author'),w.get('published'))
