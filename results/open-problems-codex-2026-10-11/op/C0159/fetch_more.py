exec(open('fetch_literature.py',encoding='utf-8-sig').read().split('with concurrent.futures')[0])
jobs={
'arxiv_source':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"Uniqueness and non-uniqueness in percolation theory"','max_results':5}),
'arxiv_nonunimodular':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:nonunimodular AND (all:repulsion OR all:clusters)','max_results':40,'sortBy':'submittedDate','sortOrder':'descending'}),
'timar_pdf':'https://arxiv.org/pdf/math/0702873',
'openalex_retry':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Neighboring clusters Bernoulli','per-page':10}),
'openalex_citing':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:doi:10.1214/154957806000000096','per-page':100}),
'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/154957806000000096?fields=title,year,citations.title,citations.year,citations.externalIds',
'crossref_source':'https://api.crossref.org/works/10.1214/154957806000000096'}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for out in ex.map(lambda kv:fetch(*kv),jobs.items()):print(json.dumps(out))
