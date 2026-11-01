import concurrent.futures, urllib.request, urllib.parse, pathlib, json
from pypdf import PdfReader
ROOT=pathlib.Path(__file__).resolve().parent
jobs={
 'source':'https://arxiv.org/pdf/0810.4221',
 'graham':'https://arxiv.org/pdf/0909.1352',
 'surface':'https://arxiv.org/pdf/2103.09199',
 'arxiv_search':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'(all:"directed polymer" OR all:"last passage") AND (all:chaos OR all:superconcentration OR all:"noise sensitivity")','max_results':25,'sortBy':'relevance'}),
 'openalex_search':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'directed polymers disorder chaos','per-page':15}),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ProbabilityAudit/1.0'})
  with urllib.request.urlopen(req,timeout=50) as r: data=r.read()
  ext='.pdf' if name in ('source','graham','surface') else '.txt'
  dest=ROOT/(name+ext); dest.write_bytes(data)
  if ext=='.pdf':
   reader=PdfReader(dest)
   (ROOT/(name+'.txt')).write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+(p.extract_text() or '') for i,p in enumerate(reader.pages)),encoding='utf-8')
  return {'name':name,'url':url,'bytes':len(data),'status':'success'}
 except Exception as e:return {'name':name,'url':url,'status':'error','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(fetch,jobs.items()))
(ROOT/'fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
