import urllib.request, urllib.parse, concurrent.futures, pathlib, json, datetime
P=pathlib.Path(__file__).parent
queries={
'source':'https://arxiv.org/pdf/1506.00724',
'arxiv':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Brownian net"','max_results':100,'sortBy':'submittedDate','sortOrder':'descending'}),
'openalex':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Brownian net bubble','per-page':50}),
'openalex_source':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'The Brownian web the Brownian net and their universality','per-page':5}),
'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'Brownian net bubble hypothesis','rows':30}),
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'Brownian net bubble','limit':50,'fields':'title,authors,year,abstract,externalIds,url'}),
'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"Brownian net"','per_page':50}),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'probability-research/1.0'})
  with urllib.request.urlopen(req,timeout=50) as r: data=r.read(); status=r.status
  suffix='.pdf' if name=='source' else '.xml' if name=='arxiv' else '.json'
  (P/(name+suffix)).write_bytes(data)
  outcome=f'HTTP {status}, {len(data)} bytes; saved {name+suffix}'
 except Exception as e: outcome=str(e)
 return {'service':name,'url':url,'date':'2026-10-12','outcome':outcome}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 results=list(ex.map(fetch,queries.items()))
(P/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results: print(r)
try:
 import pymupdf
 doc=pymupdf.open(P/'source.pdf')
 (P/'source.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
except Exception as e: print('PDF extraction:',e)
