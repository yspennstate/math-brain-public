import concurrent.futures, json, urllib.request, urllib.parse, time
from pathlib import Path
ROOT=Path(__file__).parent
queries={
 'source': 'https://arxiv.org/pdf/1204.6447',
 'arxiv_api': 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"polynomial threshold" AND (all:"independence" OR all:"Gaussian")','max_results':40,'sortBy':'submittedDate','sortOrder':'descending'}),
 'openalex_search': 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Gaussian polynomial thresholds bounded independence','per-page':30}),
 'openalex_source': 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Open problems in analysis of Boolean functions','per-page':5}),
 'crossref': 'https://api.crossref.org/works?'+urllib.parse.urlencode({'query':'Gaussian polynomial threshold bounded independence','rows':25}),
 'semantic': 'https://api.semanticscholar.org/graph/v1/paper/search?'+urllib.parse.urlencode({'query':'Gaussian polynomial threshold bounded independence','limit':30,'fields':'title,authors,year,externalIds,url,abstract'}),
 'github': 'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'Gaussian polynomial threshold independence','per_page':20}),
 'kane_search': 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Kane k independent Gaussians fool polynomial threshold functions','per-page':20}),
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'P0170 mathematical literature audit'})
  with urllib.request.urlopen(req,timeout=65) as r: data=r.read(); status=r.status
  (ROOT/(name+('.pdf' if name=='source' else '.json' if name!='arxiv_api' else '.xml'))).write_bytes(data)
  result={'service':name,'url':url,'status':status,'bytes':len(data),'date':'2026-10-12'}
 except Exception as e: result={'service':name,'url':url,'error':str(e),'date':'2026-10-12'}
 with (ROOT/'search_log.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(result)+'\n')
 print(json.dumps(result),flush=True)
 return result
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: list(pool.map(fetch,queries.items()))
 try:
  import pymupdf
  doc=pymupdf.open(ROOT/'source.pdf')
  (ROOT/'source.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
 except Exception as e: print('PDF extraction',repr(e))
