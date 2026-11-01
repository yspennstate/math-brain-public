import urllib.request,urllib.parse,concurrent.futures,pathlib,json,datetime
queries=[('arxiv','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"peeling" AND all:"Boltzmann"')+'&max_results=30&sortBy=submittedDate&sortOrder=descending'),('openalex','https://api.openalex.org/works?search='+urllib.parse.quote('filled peeling critical Boltzmann maps')+'&per-page=30'),('crossref','https://api.crossref.org/works?query='+urllib.parse.quote('Peeling random planar maps Curien')+'&rows=15'),('semantic','https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('peeling Boltzmann maps')+'&limit=30&fields=title,authors,year,externalIds,abstract'),('github','https://api.github.com/search/repositories?q='+urllib.parse.quote('peeling Boltzmann maps'))]
def run(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'})
  data=urllib.request.urlopen(req,timeout=45).read();pathlib.Path(name+'.txt').write_bytes(data)
  return name,url,'OK '+str(len(data))
 except Exception as e:return name,url,repr(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: r=list(ex.map(run,queries))
pathlib.Path('search_log.json').write_text(json.dumps(r,indent=2),encoding='utf8')
for x in r:print(x)
