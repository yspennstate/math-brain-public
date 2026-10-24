exec(open('search.py',encoding='utf-8-sig').read().split('with concurrent')[0])
urls={
'fpv':'https://arxiv.org/pdf/math/0511186',
'gouere':'https://arxiv.org/pdf/0712.3638',
'openalex_retry':'https://api.openalex.org/works?search=stable%20marriage%20Poisson&per_page=50',
'openalex_source':'https://api.openalex.org/works/https://doi.org/10.1214/009117906000000098',
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:math/0511186?fields=title,year,citations.title,citations.year,citations.externalIds',
'arxiv_vacant':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"stable marriage" AND (all:unclaimed OR all:percolation)')+'&max_results=100'}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: results=list(ex.map(lambda kv:fetch(*kv),urls.items()))
with open('search_log.json',encoding='utf8') as f:old=json.load(f)
(P/'search_log.json').write_text(json.dumps(old+results,indent=2),encoding='utf8')
for r in results:print(r)
import pymupdf
for k in ['fpv','gouere']:
 try:
  doc=pymupdf.open(P/(k+'.json'));(P/(k+'.txt')).write_text('\n'.join('--- PDF PAGE '+str(i+1)+' ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf8')
 except Exception as e:print(e)
