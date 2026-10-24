from research import get,ROOT
import json,urllib.parse,concurrent.futures
urls={
 'openalex_exact':'https://api.openalex.org/works?filter=title.search:'+urllib.parse.quote('Largest common substructures in probabilistic combinatorics')+'&per_page=5',
 'semantic_source_citations':'https://api.semanticscholar.org/graph/v1/paper/URL:'+urllib.parse.quote('https://www.stat.berkeley.edu/~aldous/Research/OP/common_subs.pdf',safe='')+'/citations?fields=title,year,authors&limit=100',
 'arxiv_aldous':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"Aldous" AND (all:"coincidence" OR all:"common partial" OR all:"common substructures")')+'&max_results=30',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: results=list(pool.map(get,urls.items()))
(ROOT/'citations_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for x in results:print(json.dumps(x))
# OpenAlex source work identity is required before citing-work traversal.
p=ROOT/'openalex_exact.raw'
if p.exists():
 data=json.loads(p.read_bytes());print('source candidates',[(x['id'],x.get('title')) for x in data.get('results',[])])
 for x in data.get('results',[]):
  if 'largest common substructures in probabilistic combinatorics'==x.get('title','').lower():
   wid=x['id'];res=get(('openalex_citing','https://api.openalex.org/works?filter=cites:'+wid+'&per_page=100'));print(json.dumps(res))
