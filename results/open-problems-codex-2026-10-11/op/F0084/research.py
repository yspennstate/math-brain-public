import requests, pathlib, json, concurrent.futures, datetime
ROOT=pathlib.Path(__file__).resolve().parent
queries={
 'source_pdf':'https://arxiv.org/pdf/math/0505668',
 'arxiv':'https://export.arxiv.org/api/query?search_query=all:%22stable%20marriage%22%20AND%20all:Poisson&max_results=50',
 'openalex':'https://api.openalex.org/works?search=stable%20marriage%20Poisson%20Lebesgue&per-page=50',
 'crossref':'https://api.crossref.org/works?query=stable%20marriage%20Poisson%20Lebesgue&rows=30',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0505668?fields=title,year,citationCount,citations.title,citations.year,citations.externalIds',
 'github':'https://api.github.com/search/repositories?q=stable+marriage+Poisson+Lebesgue',
}
def fetch(k,u):
 try:
  r=requests.get(u,timeout=55,headers={'User-Agent':'MathematicalResearch/1.0'})
  p=ROOT/(k+('.pdf' if k.endswith('pdf') else '.json' if k in ['openalex','crossref','semantic','github'] else '.xml'))
  p.write_bytes(r.content)
  return {'service':k,'url':u,'date':str(datetime.date.today()),'status':r.status_code,'bytes':len(r.content),'file':p.name}
 except Exception as e: return {'service':k,'url':u,'error':str(e)}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
  results=list(ex.map(lambda kv:fetch(*kv),queries.items()))
 (ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
 print(json.dumps(results,indent=2))
 try:
  import pymupdf
  doc=pymupdf.open(ROOT/'source_pdf.pdf')
  (ROOT/'source.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 except Exception as e: print('PDF extraction:',e)
