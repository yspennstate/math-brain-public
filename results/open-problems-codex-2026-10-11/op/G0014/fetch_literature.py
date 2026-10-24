import urllib.request, urllib.parse, json, pathlib, concurrent.futures, datetime
root=pathlib.Path(__file__).parent
queries={
 'source_pdf':'https://arxiv.org/pdf/2608.21125',
 'source_html':'https://arxiv.org/html/2608.21125',
 'arxiv_id':'https://export.arxiv.org/api/query?id_list=2608.21125',
 'arxiv_search':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"threshold cascades" AND all:"Bramson"')+'&max_results=20',
 'openalex_source':'https://api.openalex.org/works?search='+urllib.parse.quote('Two problems for threshold cascades of interacting diffusions on unimodular random trees')+'&per-page=5',
 'openalex_recent':'https://api.openalex.org/works?search='+urllib.parse.quote('threshold cascades Bramson')+'&filter=from_publication_date:2026-08-01&per-page=20',
 'crossref':'https://api.crossref.org/works?query='+urllib.parse.quote('threshold cascades unimodular Bramson')+'&rows=10',
 'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.21125?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
 'github':'https://api.github.com/search/repositories?q='+urllib.parse.quote('"threshold cascades"'),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0','Accept':'*/*'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read(); status=r.status
  path=root/(name+('.pdf' if name=='source_pdf' else '.txt'));path.write_bytes(data)
  return {'service':name,'url':url,'date':str(datetime.date.today()),'status':status,'bytes':len(data),'file':path.name}
 except Exception as e: return {'service':name,'url':url,'date':str(datetime.date.today()),'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,queries.items()))
(root/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for x in results:print(json.dumps(x))
try:
 import pymupdf
 doc=pymupdf.open(root/'source_pdf.pdf')
 (root/'source_extracted.txt').write_text('\n'.join(f'\n=== PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 print('PDF extracted',len(doc))
except Exception as e:print('PDF extraction:',e)
