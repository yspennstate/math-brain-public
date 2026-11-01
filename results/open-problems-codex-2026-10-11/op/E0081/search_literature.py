import concurrent.futures, json, urllib.request, urllib.parse, pathlib, datetime
ROOT=pathlib.Path(__file__).resolve().parent
queries=[
 ('arxiv', 'http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"patterns in random walks"','max_results':30})),
 ('arxiv_https', 'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"waiting time" AND all:"patterns"','max_results':40,'sortBy':'submittedDate','sortOrder':'descending'})),
 ('openalex_source', 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Patterns in random walks and Brownian motion','per-page':10})),
 ('openalex_patterns', 'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Pitman Tang patterns waiting time','per-page':30})),
 ('crossref', 'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':'Patterns in random walks and Brownian motion','rows':20})),
 ('semantic_scholar', 'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1411.0041?fields=title,authors,year,externalIds,citations.title,citations.year,citations.externalIds'),
 ('github', 'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'"Pitman" "Tang" patterns','per_page':20})),
]
def fetch(item):
 name,url=item
 try:
  request=urllib.request.Request(url,headers={'User-Agent':'ProbabilityResearch/1.0'})
  with urllib.request.urlopen(request,timeout=45) as response: body=response.read(); code=response.status
  ROOT.joinpath(name+'.response').write_bytes(body)
  result={'service':name,'query_url':url,'date':'2026-10-12','status':code,'bytes':len(body)}
 except Exception as e: result={'service':name,'query_url':url,'date':'2026-10-12','error':str(e)}
 with ROOT.joinpath('search_log.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(result)+'\n')
 print(json.dumps(result),flush=True)
 return result
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: list(pool.map(fetch,queries))
