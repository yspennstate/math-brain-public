import concurrent.futures, urllib.request, urllib.parse, pathlib, json
from pypdf import PdfReader
root=pathlib.Path.cwd()
jobs={
'source':'https://arxiv.org/pdf/0810.4221',
'graham':'https://arxiv.org/pdf/0909.1352',
'surface':'https://arxiv.org/pdf/2103.09199',
'arxiv_search':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"directed polymer" AND (all:chaos OR all:superconcentration)','max_results':30,'sortBy':'relevance'}),
'openalex_search':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'directed polymers disorder chaos','per_page':15})}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'IndependentMathematicalAudit/1.0'})
  data=urllib.request.urlopen(req,timeout=50).read()
  ext='.pdf' if name in ['source','graham','surface'] else '.txt'
  path=root/(name+ext);path.write_bytes(data)
  if ext=='.pdf':
   reader=PdfReader(path);text='\n'.join('PDF PAGE '+str(i+1)+'\n'+p.extract_text() for i,p in enumerate(reader.pages));(root/(name+'.txt')).write_text(text,encoding='utf-8')
  return {'name':name,'url':url,'bytes':len(data),'status':'ok'}
 except Exception as e:return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(fetch,jobs.items()))
(root/'fetch_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
