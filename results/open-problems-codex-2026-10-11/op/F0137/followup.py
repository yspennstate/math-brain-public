from research import fetch
import urllib.parse,concurrent.futures
jobs=[('perrel.pdf','https://arxiv.org/pdf/2404.06502'),('2d.pdf','https://arxiv.org/pdf/2501.06767'),
 ('openalex_source.json','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Random walks in Dirichlet environment an overview','per-page':5})),
 ('openalex_retry.json','https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Dirichlet environment','per-page':30,'filter':'from_publication_date:2016-01-01'})),
 ('semantic_citations.json','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1601.08219/citations?'+urllib.parse.urlencode({'limit':100,'fields':'title,year,authors,externalIds'})),
 ('arxiv_T.xml','https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:Dirichlet AND (all:ballisticity OR all:Sznitman OR all:regeneration)','max_results':60,'sortBy':'submittedDate','sortOrder':'descending'}))]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: list(ex.map(lambda j:fetch(*j),jobs))
