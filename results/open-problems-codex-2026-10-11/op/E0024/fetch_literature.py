import urllib.request, urllib.parse, concurrent.futures, pathlib, json, datetime
root=pathlib.Path('.')
queries={
'source_pdf':'https://arxiv.org/pdf/1908.06825',
'arxiv_http':'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Hunt hypothesis"','max_results':50}),
'arxiv_https':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Hunt" AND all:"Levy"','max_results':50,'sortBy':'submittedDate','sortOrder':'descending'}),
'openalex_search':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':"Hunt hypothesis Levy",'per-page':50}),
'openalex_source':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':"Hunt's hypothesis (H) for Markov processes: survey and beyond",'per-page':5}),
'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':"Hunt hypothesis Levy product",'rows':30}),
'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':"Hunt hypothesis",'limit':50,'fields':'title,year,authors,externalIds,url,abstract'}),
'semantic_citations':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06825/citations?'+urllib.parse.urlencode({'limit':100,'fields':'title,year,authors,externalIds,url,abstract'}),
'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'Hunt hypothesis Levy','per_page':30})}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Research-status-check/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  path=root/(name+('.pdf' if name=='source_pdf' else '.raw'))
  path.write_bytes(data)
  return {'service_query':name,'url':url,'date':str(datetime.date.today()),'bytes':len(data),'file':str(path),'status':'ok'}
 except Exception as e:return {'service_query':name,'url':url,'date':str(datetime.date.today()),'status':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=9) as ex:
 results=list(ex.map(fetch,queries.items()))
(root/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results:print(json.dumps(r))
try:
 import pymupdf
 d=pymupdf.open('source_pdf.pdf')
 (root/'source.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8')
 print('PDF extracted',len(d),'pages')
except Exception as e: print('PDF extraction:',e)
