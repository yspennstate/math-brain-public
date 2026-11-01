import concurrent.futures, urllib.request, urllib.parse, json, pathlib, datetime
out=pathlib.Path('.')
queries={
'source_pdf':'https://arxiv.org/pdf/2608.19145',
'arxiv':'http://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"percolation" AND (all:"spectral radius" OR au:Christoph)')+'&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending',
'openalex':'https://api.openalex.org/works?search='+urllib.parse.quote('The critical probability for percolation on finite graphs')+'&per-page=15',
'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('The critical probability for percolation on finite graphs')+'&rows=15',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.19145?fields=title,authors,year,citationCount,citations.title,citations.year,citations.externalIds',
'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('"percolation" "spectral"'),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ResearchVerification/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read(); status=r.status
  ext='pdf' if name=='source_pdf' else 'json' if name!='arxiv' else 'xml'
  (out/(name+'.'+ext)).write_bytes(data)
  return dict(service=name,url=url,status=status,bytes=len(data),date=str(datetime.date.today()))
 except Exception as e: return dict(service=name,url=url,error=str(e),date=str(datetime.date.today()))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 results=list(pool.map(fetch,queries.items()))
pathlib.Path('search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 doc=pymupdf.open('source_pdf.pdf')
 pathlib.Path('source.txt').write_text('\n'.join(f'\n--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
 print('PDF extracted',len(doc))
except Exception as e: print('extraction',repr(e))
