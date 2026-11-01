import urllib.request, urllib.parse, json, concurrent.futures, datetime
from pathlib import Path
queries = {
 'arxiv_recent': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:ASEP AND (all:correlation OR all:stationary) AND submittedDate:[20250319 TO 20261012]','max_results':50}),
 'arxiv_queue': 'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:ASEP AND all:queue','max_results':30}),
 'openalex': 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'two species ASEP stationary correlations','per-page':25}),
 'openalex_source': 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'All roads to KPZ Universality Open Problems','per-page':5}),
 'crossref': 'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'two species ASEP stationary correlations','rows':25}),
 'semantic': 'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'two species ASEP stationary correlations','limit':20,'fields':'title,authors,year,externalIds,url,abstract'}),
 'github': 'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'ASEP stationary correlations','per_page':20}),
}
def fetch(k,u):
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'ProbabilityResearch/1.0'})
  with urllib.request.urlopen(req,timeout=35) as r: body=r.read().decode(); status=r.status
  Path(k+'.txt').write_text(body,encoding='utf-8')
  return {'service':k,'url':u,'date':'2026-10-12','status':status,'file':k+'.txt'}
 except Exception as e: return {'service':k,'url':u,'date':'2026-10-12','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex: results=list(ex.map(lambda x:fetch(*x),queries.items()))
Path('search_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
