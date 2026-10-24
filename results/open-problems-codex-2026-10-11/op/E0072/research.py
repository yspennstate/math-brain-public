import urllib.request, json, pathlib, datetime, concurrent.futures
P=pathlib.Path(__file__).resolve().parent
queries={
 'source': 'https://arxiv.org/pdf/1406.0763',
 'arxiv': 'https://export.arxiv.org/api/query?search_query=all:%22conjugation-invariant%22+AND+all:%22random%20walk%22&max_results=20',
 'openalex_search': 'https://api.openalex.org/works?search=conjugation%20invariant%20random%20walk%20drift&per-page=20',
 'openalex_source': 'https://api.openalex.org/works?search=Five%20remarks%20about%20random%20walks%20on%20groups&per-page=5',
 'crossref': 'https://api.crossref.org/works?query=conjugation%20invariant%20random%20walk%20drift&rows=20',
 'semantic_scholar': 'https://api.semanticscholar.org/graph/v1/paper/search?query=conjugation%20invariant%20random%20walk%20drift&limit=20&fields=title,authors,year,url,abstract',
 'github': 'https://api.github.com/search/repositories?q=conjugation+invariant+random+walk',
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'E0072 mathematical research'})
  data=urllib.request.urlopen(req,timeout=35).read()
  (P/(name+('.pdf' if name=='source' else '.txt'))).write_bytes(data)
  return name,url,'OK',len(data)
 except Exception as e: return name,url,'ERROR',str(e)
results=list(concurrent.futures.ThreadPoolExecutor(max_workers=7).map(fetch,queries.items()))
(P/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results),flush=True)
try:
 import pymupdf
 doc=pymupdf.open(P/'source.pdf')
 (P/'source_text.txt').write_text('\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
 print(doc[24].get_text(),flush=True)
except Exception as e: print('PDF extraction:',repr(e),flush=True)
