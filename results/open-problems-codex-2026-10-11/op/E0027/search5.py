exec(open('fetch.py',encoding='utf-8-sig').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
 'oa_published_source':'https://api.openalex.org/works/https://doi.org/10.1007/s10114-021-9343-7',
 'oa_published_sum':'https://api.openalex.org/works/https://doi.org/10.1007/s40304-018-0136-y',
 'cr_source_doi':'https://api.crossref.org/works/10.1007/s10114-021-9343-7',
 's2_citations':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s10114-021-9343-7/citations?fields=title,year,externalIds,abstract&limit=100',
 's2_exact_bulk':'https://api.semanticscholar.org/graph/v1/paper/search/bulk?'+urllib.parse.urlencode({'query':'"Hunt’s hypothesis"','fields':'title,year,authors,externalIds,abstract','sort':'publicationDate:desc'})}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for r in ex.map(fetch,queries.items()): print(json.dumps(r),flush=True)
