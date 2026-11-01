import pathlib, urllib.request, urllib.parse, json, concurrent.futures, datetime
ROOT=pathlib.Path(__file__).parent
jobs={
 'survey.pdf':'https://arxiv.org/pdf/1109.3343',
 'arxiv.xml':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"heavy tailed" AND all:"circular law"','max_results':40}),
 'openalex.json':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'heavy tailed circular law','per-page':40}),
 'crossref.json':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'heavy tailed circular law','rows':30}),
 'semantic.json':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'heavy tailed circular law','limit':30,'fields':'title,authors,year,externalIds,abstract,url'}),
 'github.json':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'heavy tailed circular law'}),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mathematics-research/1.0'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read()
  (ROOT/name).write_bytes(data)
  status=f'OK {len(data)} bytes'
 except Exception as e: status=f'FAILED {e}'
 return {'file':name,'url':url,'date':str(datetime.date.today()),'status':status}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 results=list(ex.map(fetch,jobs.items()))
(ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results: print(r)
try:
 import pymupdf
 doc=pymupdf.open(ROOT/'survey.pdf')
 (ROOT/'survey.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
except Exception as e: print('PDF extraction:',e)
