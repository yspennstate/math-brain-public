import urllib.request, json, pathlib, concurrent.futures, datetime
root=pathlib.Path.cwd()
queries={
 'source_pdf':'https://arxiv.org/pdf/2609.09972',
 'source_abs':'https://arxiv.org/abs/2609.09972',
 'arxiv':'https://export.arxiv.org/api/query?search_query=all:contact%20AND%20all:percolation&sortBy=submittedDate&sortOrder=descending&max_results=40',
 'openalex':'https://api.openalex.org/works?search=Percolation%20of%20the%20contact%20process%20on%20the%20regular%20tree&per-page=20',
 'crossref':'https://api.crossref.org/works?query=contact%20process%20upper%20invariant%20measure%20percolation&rows=20',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.09972?fields=title,authors,year,abstract,citations.title,citations.year,citations.externalIds',
 'github':'https://api.github.com/search/repositories?q=contact+process+percolation',
}
def fetch(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'G0006-mathematics-literature-check/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read(); code=r.status
  name=k+('.pdf' if k=='source_pdf' else '.txt')
  (root/name).write_bytes(data)
  result={'service':k,'url':u,'status':code,'bytes':len(data),'file':name}
 except Exception as e: result={'service':k,'url':u,'error':str(e)}
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: results=list(ex.map(lambda kv:fetch(*kv),queries.items()))
(root/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results: print(json.dumps(r))
try:
 import pymupdf
 doc=pymupdf.open(root/'source_pdf.pdf')
 (root/'source_text.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 print('PDF text extracted',len(doc))
except Exception as e: print('Extraction:',e)
