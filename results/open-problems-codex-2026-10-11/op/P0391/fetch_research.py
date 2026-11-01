import concurrent.futures, urllib.request, json, pathlib, datetime
root=pathlib.Path(__file__).resolve().parent
queries={
'source_pdf':'https://arxiv.org/pdf/2202.02366',
'arxiv':'http://export.arxiv.org/api/query?search_query=all:%22symmetric%20queues%22&start=0&max_results=30',
'openalex_search':'https://api.openalex.org/works?search=Conjectures%20on%20Symmetric%20Queues%20in%20Heavy%20Traffic&per-page=10',
'openalex_related':'https://api.openalex.org/works?search=symmetric%20queues%20heavy%20traffic&per-page=30',
'crossref':'https://api.crossref.org/works?query=symmetric%20queues%20heavy%20traffic&rows=30',
'semantic':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2202.02366?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
'github':'https://api.github.com/search/repositories?q=%22symmetric+queues%22'}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'})
  with urllib.request.urlopen(req,timeout=45) as response: data=response.read()
  path=root/(name+('.pdf' if name=='source_pdf' else '.txt'))
  path.write_bytes(data)
  return {'service':name,'query':url,'date':str(datetime.date.today()),'result':'saved','bytes':len(data)}
 except Exception as e: return {'service':name,'query':url,'date':str(datetime.date.today()),'result':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: results=list(ex.map(fetch,queries.items()))
(root/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
try:
 import pymupdf
 doc=pymupdf.open(root/'source_pdf.pdf')
 (root/'source.txt').write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8')
 print((root/'source.txt').read_text(encoding='utf-8'))
except Exception as e: print('PDF extraction:',e)
