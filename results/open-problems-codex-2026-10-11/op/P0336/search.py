import urllib.request, json, concurrent.futures, pathlib, datetime
root=pathlib.Path(__file__).parent
queries={
 'source_pdf':'https://arxiv.org/pdf/2505.19104',
 'source_abs':'https://arxiv.org/abs/2505.19104',
 'arxiv':'http://export.arxiv.org/api/query?search_query=all:%22empirical%20optimal%20transport%22%20AND%20all:%22Euclidean%22&start=0&max_results=20',
 'openalex':'https://api.openalex.org/works?search=Distributional%20Limit%20Theory%20for%20Optimal%20Transport&per-page=10',
 'crossref':'https://api.crossref.org/works?query=empirical%20Euclidean%20transport%20plan%20rectangles&rows=10',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2505.19104?fields=title,authors,year,citations.title,citations.externalIds,citations.year',
 'github':'https://api.github.com/search/repositories?q=empirical+optimal+transport+euclidean'
}
def get(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'P0336-mathematics-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: b=r.read()
  (root/(k+('.pdf' if k=='source_pdf' else '.txt'))).write_bytes(b)
  return {'service':k,'url':u,'date':'2026-10-12','status':'ok','bytes':len(b)}
 except Exception as e: return {'service':k,'url':u,'date':'2026-10-12','status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 results=list(ex.map(lambda kv:get(*kv),queries.items()))
(root/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 d=pymupdf.open(root/'source_pdf.pdf'); (root/'source_text.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
 print('PDF extracted',len(d))
except Exception as e: print('PDF extraction',e)
