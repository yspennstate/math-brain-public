import urllib.request, urllib.parse, json, concurrent.futures, pathlib, datetime
ROOT=pathlib.Path(__file__).parent
queries={
 'source':'https://arxiv.org/pdf/0810.2994',
 'arxiv':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"circular law" AND (all:rate OR all:moment)')+'&start=0&max_results=35',
 'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('circular law rate convergence moment')+'&per-page=30',
 'openalex_source':'https://api.openalex.org/works?search='+urllib.parse.quote('From the Littlewood Offord problem to the circular law')+'&per-page=5',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('circular law rate convergence moment')+'&rows=25',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?query='+urllib.parse.quote('circular law rate convergence')+'&limit=25&fields=title,authors,year,externalIds,url,abstract',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('circular law random matrix')+'&per_page=15',
}
def fetch(pair):
 name,url=pair
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'C0109-mathematical-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (ROOT/(name+('.pdf' if name=='source' else '.json' if name not in ['arxiv'] else '.xml'))).write_bytes(data)
  return {'service':name,'url':url,'date':str(datetime.date.today()),'bytes':len(data),'status':'ok'}
 except Exception as e:return {'service':name,'url':url,'date':str(datetime.date.today()),'status':str(e)}
if __name__=='__main__':
 results=list(concurrent.futures.ThreadPoolExecutor(max_workers=7).map(fetch,queries.items()))
 (ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
 print(json.dumps(results,indent=2))
 try:
  import pymupdf
  doc=pymupdf.open(ROOT/'source.pdf')
  (ROOT/'source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 except Exception as e: print('PDF extraction:',e)
