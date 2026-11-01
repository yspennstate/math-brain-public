import concurrent.futures, json, pathlib, requests, datetime
ROOT=pathlib.Path(__file__).parent
queries={
 'arxiv':'http://export.arxiv.org/api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:monotonicity&max_results=20',
 'arxiv_https':'https://export.arxiv.org/api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:monotonicity&max_results=20',
 'openalex':'https://api.openalex.org/works?search=percolation%20uniqueness%20monotonicity&per-page=25',
 'openalex_source':'https://api.openalex.org/works/https://doi.org/10.1214/154957806000000096',
 'crossref':'https://api.crossref.org/works?query=percolation%20uniqueness%20monotonicity&rows=20',
 'semantic_scholar':'https://api.semanticscholar.org/graph/v1/paper/search?query=percolation%20uniqueness%20monotonicity&limit=20&fields=title,authors,year,url,externalIds',
 'github':'https://api.github.com/search/repositories?q=percolation+uniqueness+monotonicity',
 'arxiv_endpoint':'https://export.arxiv.org/api/query?search_query=all:percolation+AND+all:uniqueness+AND+all:threshold&sortBy=submittedDate&sortOrder=descending&max_results=25'
}
def get(item):
 name,url=item
 try:
  r=requests.get(url,timeout=45,headers={'User-Agent':'Mathematical-status-check/1.0'})
  (ROOT/(name+'.txt')).write_text(r.text,encoding='utf-8')
  row={'service':name,'url':url,'date':'2026-10-11','status':r.status_code,'bytes':len(r.content)}
  print(json.dumps(row),flush=True)
  return row
 except Exception as e:
  row={'service':name,'url':url,'date':'2026-10-11','error':str(e)}
  print(json.dumps(row),flush=True); return row
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 rows=list(ex.map(get,queries.items()))
source=ROOT/'openalex_source.txt'
try:
 wid=json.loads(source.read_text(encoding='utf-8'))['id'].split('/')[-1]
 rows.append(get(('openalex_citations',f'https://api.openalex.org/works?filter=cites:{wid}&per-page=100&sort=publication_date:desc')))
except Exception as e: print('citation lookup:',e,flush=True)
(ROOT/'search_log.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
