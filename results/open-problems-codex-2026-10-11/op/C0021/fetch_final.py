from search import fetch,P
import json,urllib.parse,concurrent.futures
queries=[
 ('openalex_citing','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:doi:10.1017/CBO9781139020299','per-page':100})),
 ('openalex_doi','https://api.openalex.org/works/https://doi.org/10.1017/CBO9781139020299'),
 ('arxiv_narrow','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"majority" AND (all:"query" OR all:"revealment")','max_results':100,'sortBy':'submittedDate','sortOrder':'descending'})),
 ('stochastic','https://arxiv.org/pdf/2606.24672'),
 ('github_visualizer','https://api.github.com/repos/tulasimohan/rec-maj-visualizer/readme'),
 ('github_recursive','https://api.github.com/repos/zpotthoff/Recursive-Majority/readme'),
 ('crossref_levelp','https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':'Level-p-complexity of Boolean Functions using Thinning Memoization and Polynomials','rows':3}))]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: results=list(ex.map(fetch,queries))
(P/'search_final_log.json').write_text(json.dumps(results,indent=2),encoding='utf8'); print(json.dumps(results,indent=2))
import fitz,base64
try:
 d=fitz.open(P/'stochastic.json'); (P/'stochastic.txt').write_text('\n'.join(p.get_text() for p in d),encoding='utf8');print(d[0].get_text())
except Exception as e:print(repr(e))
for name in ['github_visualizer','github_recursive']:
 try:
  x=json.loads((P/(name+'.json')).read_text()); txt=base64.b64decode(x['content']).decode();(P/(name+'.txt')).write_text(txt,encoding='utf8');print(name,txt[:5000])
 except Exception as e:print(repr(e))
