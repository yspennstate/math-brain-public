import pathlib,json,urllib.request,concurrent.futures,xml.etree.ElementTree as ET
p=pathlib.Path('.')
q={
'arxiv_exact':'https://export.arxiv.org/api/query?search_query=all:%222608.23661%22+OR+(all:%22pivotal%22+AND+au:%22Raphael_Cerf%22)&max_results=30',
'openalex_retry':'https://api.openalex.org/works?search=theta%20Cerf&per-page=5',
'openalex_citations':'https://api.openalex.org/works?filter=cites:doi:10.48550/arXiv.2608.23661&per-page=20',
'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?query=second%20order%20pivotal%20Cerf&limit=10&fields=title,year,externalIds',
'crossref_exact':'https://api.crossref.org/works?query=2608.23661&rows=5',
'github_exact':'https://api.github.com/search/repositories?q=%222608.23661%22'}
def f(t):
 name,url=t
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research/1.0'}),timeout=35) as r:data=r.read();s=r.status
  (p/(name+'.txt')).write_bytes(data)
  return dict(service=name,url=url,date='2026-10-11',status=s,bytes=len(data))
 except Exception as e:return dict(service=name,url=url,date='2026-10-11',error=str(e))
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(f,q.items()))
a=json.loads((p/'search_log.json').read_text());a.extend(r);(p/'search_log.json').write_text(json.dumps(a,indent=2))
for z in r:print(z)
ns={'a':'http://www.w3.org/2005/Atom'}
for file in p.glob('arxiv*.txt'):
 try:
  x=ET.fromstring(file.read_text());print(file)
  for e in x.findall('a:entry',ns):print(e.findtext('a:id',namespaces=ns),e.findtext('a:title',namespaces=ns),e.findtext('a:summary',namespaces=ns)[:500])
 except Exception as e:print(e)
for file in ['crossref.txt','crossref_exact.txt']:
 x=json.loads((p/file).read_text());print(file)
 for e in x['message']['items']:print(e.get('title'),e.get('DOI'))
