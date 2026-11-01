import urllib.request, pathlib, concurrent.futures, json
root=pathlib.Path('.')
urls={
'source.pdf':'https://arxiv.org/pdf/1910.09213',
'arxiv.xml':'https://export.arxiv.org/api/query?search_query=all:%22frozen%20percolation%22&max_results=50',
'openalex.json':'https://api.openalex.org/works?search=frozen%20percolation&per-page=50',
'crossref.json':'https://api.crossref.org/works?query.title=frozen%20percolation&rows=30',
'semantic.json':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1910.09213?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
'github.json':'https://api.github.com/search/repositories?q=frozen+percolation'}
def get(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as f: data=f.read()
  (root/name).write_bytes(data)
  return name,url,len(data),'OK'
 except Exception as e: return name,url,0,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(get,urls.items()))
(root/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 doc=pymupdf.open('source.pdf')
 (root/'source.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
except Exception as e: print('PDF extraction',e)
