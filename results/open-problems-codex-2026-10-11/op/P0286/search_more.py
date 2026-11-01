from search import fetch
from pathlib import Path
import urllib.parse,json,concurrent.futures
queries={
'arxiv_spatial':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'(all:"multi-species" OR all:"two-species") AND (all:correlations OR all:covariance)','max_results':50}),
'arxiv_horizon':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"stationary horizon"','max_results':30}),
'crossref_focused':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':'Decoupling and decay of two-point functions in a two-species ASEP','rows':5}),
'openalex_retry':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'ASEP covariance','per-page':10}),
'semantic_retry':'https://api.semanticscholar.org/graph/v1/paper/arXiv:2504.00765?fields=title,authors,year,citations.title,citations.externalIds',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:results=list(ex.map(lambda x:fetch(*x),queries.items()))
Path('search_more_log.json').write_text(json.dumps(results,indent=2),encoding='utf-8'); print(json.dumps(results,indent=2))
