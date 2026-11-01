from pathlib import Path
import urllib.request,concurrent.futures,json,urllib.parse,datetime
queries=[('source1993','https://www.stat.berkeley.edu/~aldous/Research/OP/patience.pdf'),('source1999','https://www.stat.berkeley.edu/~aldous/Papers/me86.pdf'),('source1995','https://www.stat.berkeley.edu/~aldous/Papers/me71.pdf'),('arxiv','http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:Hammersley AND (all:stationary OR all:drift)')+'&max_results=30'),('openalex','https://api.openalex.org/works?search='+urllib.parse.quote('Hammersley drift jump stationary')+'&per-page=20'),('crossref','https://api.crossref.org/works?query='+urllib.parse.quote('Hammersley drift jump stationary')+'&rows=20'),('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('Hammersley drift jump')+'&limit=20&fields=title,authors,year,url,externalIds'),('github','https://api.github.com/search/repositories?q='+urllib.parse.quote('Hammersley stationary'))]
Path('LITERATURE.md').write_text('# Literature and status search\n\nDate: 2026-10-11. No exact solution has yet been verified.\n\nSource page fetched successfully: https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html (saved source.html).\n',encoding='utf8')
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'P0220-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  Path(name+('.pdf' if name.startswith('source') else '.json' if name!='arxiv' else '.xml')).write_bytes(data)
  return name,url,'OK '+str(len(data))
 except Exception as e:return name,url,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
 for name,url,result in pool.map(fetch,queries):
  with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n- '+name+': '+url+'\n  Result: '+result+'\n')
  print(name,result)
