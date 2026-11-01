from search import fetch,P
import json,urllib.parse,concurrent.futures
queries=[('levelp','https://arxiv.org/pdf/2302.02473'),('worstcase','https://arxiv.org/pdf/1309.7565'),
 ('arxiv_revealment','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:revealment AND (all:majority OR all:recursive)','max_results':40})),
 ('openalex_retry','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'iterated majority revealment','per_page':15})),
 ('openalex_arxiv','https://api.openalex.org/works/https://arxiv.org/abs/1102.5761'),
 ('semantic_retry','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1102.5761?fields=title,citations.title,citations.year,citations.externalIds')]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: results=list(ex.map(fetch,queries))
(P/'search_more_log.json').write_text(json.dumps(results,indent=2),encoding='utf8'); print(json.dumps(results,indent=2))
import fitz
for name in ['levelp','worstcase']:
 try:
  d=fitz.open(P/(name+'.json')); txt='\n'.join(p.get_text() for p in d); (P/(name+'.txt')).write_text(txt,encoding='utf8')
  for i,p in enumerate(d):
   t=p.get_text()
   if name=='levelp' and ('393' in t or 'two-level' in t or 'open' in t): print(name,'PDF page',i+1,t)
 except Exception as e: print(repr(e))
