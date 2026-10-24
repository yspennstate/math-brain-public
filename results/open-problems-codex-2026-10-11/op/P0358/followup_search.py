import urllib.parse
from search_literature import fetch
fetch(('openalex_citation_attempt','https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:https://doi.org/10.1007/s10114-026-4459-4','per-page':100})))
fetch(('semantic_sharp','https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.32480?fields=title,authors,year,abstract'))
url='http://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"discounted" AND all:"branching"','sortBy':'submittedDate','sortOrder':'descending','max_results':30})
k,d,s=fetch(('arxiv_discounted',url))
if s!='ERROR': print(d[:1500])
if s=='ERROR': fetch(('arxiv_discounted_https',url.replace('http:','https:',1)))
