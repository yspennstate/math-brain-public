import urllib.request,urllib.parse,json,pathlib,concurrent.futures,datetime
queries=[('arxiv','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Brownian" AND all:"mode" AND all:"free"')+'&max_results=30'),('arxiv_source','https://export.arxiv.org/api/query?id_list=1710.08240'),('openalex','https://api.openalex.org/works?search='+urllib.parse.quote('Large time unimodality classical free Brownian')+'&per-page=30'),('crossref','https://api.crossref.org/works?query='+urllib.parse.quote('Brownian mode location Hasebe Ueda')+'&rows=30'),('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('Brownian unimodality mode')+'&limit=30&fields=title,year,authors,url,abstract'),('github','https://api.github.com/search/repositories?q='+urllib.parse.quote('Brownian mode unimodality'))]
pathlib.Path('LITERATURE.md').write_text('# Literature status\nSearch date: 2026-10-11. API failures are recorded, not interpreted as negative searches.\n',encoding='utf8')
def run(q):
 name,url=q
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'P0177-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  pathlib.Path(name+'.response').write_bytes(data)
  result='OK '+str(len(data))+' bytes'
 except Exception as e: result=repr(e)
 return name,url,result
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for name,url,result in ex.map(run,queries):
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- '+name+': '+url+'\n  '+result+'\n')
  print(name,result)
