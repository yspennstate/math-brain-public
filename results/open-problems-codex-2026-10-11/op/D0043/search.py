import urllib.request, urllib.parse, json, pathlib, concurrent.futures, datetime
ROOT=pathlib.Path(__file__).resolve().parent
queries={
'source':'https://arxiv.org/pdf/1804.06953',
'arxiv':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"multicritical" AND (all:"beta" OR all:"operator")','max_results':30}),
'openalex':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'exotic edge operators','per-page':20}),
'openalex_source':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Operator limits of random matrices','per-page':5}),
'crossref':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'multicritical random matrix stochastic operator','rows':20}),
'semantic':'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'multicritical edge random matrices','limit':20,'fields':'title,authors,year,externalIds,url,abstract'}),
'github':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'multicritical random matrix'}),
'arxiv_exotic':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"exotic edge"','max_results':30}),
'openalex_multi':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'multicritical beta ensembles','per-page':30}),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'D0043-research/1.0'})
  with urllib.request.urlopen(req,timeout=35) as r: data=r.read(12000000)
  (ROOT/(name+('.pdf' if name=='source' else '.json' if name not in ('arxiv','arxiv_exotic') else '.xml'))).write_bytes(data)
  result=f'{name}: {len(data)} bytes'
 except Exception as e: result=f'{name}: ERROR {e}'
 return {'date':str(datetime.datetime.now()),'service':name,'url':url,'result':result}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 results=list(pool.map(fetch,queries.items()))
(ROOT/'search_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results: print(r['result'])
try:
 import pymupdf
 doc=pymupdf.open(ROOT/'source.pdf')
 (ROOT/'source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 print('PDF extracted',len(doc))
except Exception as e: print('PDF extraction:',e)
