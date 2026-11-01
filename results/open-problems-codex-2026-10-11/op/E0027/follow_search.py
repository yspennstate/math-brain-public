exec(open('fetch.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
 'oa_exact':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':"Hunt's hypothesis",'per-page':100}),
 'oa_levy':'https://api.openalex.org/works?'+urllib.parse.urlencode({'search':'Hunt hypothesis Levy','per-page':50}),
 'oa_citing':'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'cites:W2968964261','per-page':100}),
 'cr_exact':'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':"Hunt's hypothesis",'rows':50}),
 'arxiv_https':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'all:"Hunt" AND all:"hypothesis" AND cat:math.PR','max_results':50,'sortBy':'submittedDate','sortOrder':'descending'}),
 's2_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:1908.06825?fields=title,year,citations.title,citations.year,citations.externalIds',
 'github_levy':'https://api.github.com/search/repositories?'+urllib.parse.urlencode({'q':'Hunt Levy hypothesis','per_page':30})}
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for r in ex.map(fetch,queries.items()): print(json.dumps(r),flush=True)
