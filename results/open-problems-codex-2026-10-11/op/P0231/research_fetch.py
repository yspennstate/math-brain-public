import urllib.request, urllib.parse, concurrent.futures, pathlib, json, datetime
ROOT=pathlib.Path(__file__).resolve().parent
queries={
 'source':'https://alea.impa.br/articles/v20/20-59.pdf',
 'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Poissonian coloring"')+'&max_results=30',
 'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('Fractal properties of the frontier in Poissonian coloring')+'&per-page=15',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('Poissonian coloring frontier')+'&rows=15',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2302.07254?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('"Poissonian coloring"'),
}
def fetch(k,url):
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'P0231-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (ROOT/(k+('.pdf' if k=='source' else '.txt'))).write_bytes(data)
  return {'service':k,'url':url,'date':datetime.datetime.now().isoformat(),'status':'ok','bytes':len(data)}
 except Exception as e:return {'service':k,'url':url,'date':datetime.datetime.now().isoformat(),'status':str(e)}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  results=list(pool.map(lambda kv:fetch(*kv),queries.items()))
 (ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
 print(json.dumps(results,indent=2))
 try:
  import pymupdf
  doc=pymupdf.open(ROOT/'source.pdf')
  (ROOT/'source_text.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
  print(''.join(p.get_text() for p in list(doc)[:4]))
 except Exception as e: print('PDF extraction:',repr(e))
