import search_literature as s
jobs=[
 ('arxiv_star','https://export.arxiv.org/api/query',{'search_query':'all:"scale invariant" AND (all:"chaos" OR all:"random measures")','max_results':60}),
 ('arxiv_uniqueness','https://export.arxiv.org/api/query',{'search_query':'all:"multiplicative chaos" AND (all:"uniqueness" OR all:"classification")','max_results':60}),
 ('arxiv_freezing','https://export.arxiv.org/api/query',{'search_query':'all:"multiplicative chaos" AND (all:"glassy" OR all:"supercritical")','max_results':40}),
 ('crossref_source','https://api.crossref.org/works',{'query.title':'Gaussian multiplicative chaos and applications a review','rows':3}),
 ('openalex_doi','https://api.openalex.org/works/https://doi.org/10.1214/13-PS218',{}),
 ('semantic_source','https://api.semanticscholar.org/graph/v1/paper/ARXIV:1305.6221/citations',{'limit':100,'fields':'title,year,externalIds'}),
 ('github_followup','https://api.github.com/search/repositories',{'q':'"multiplicative chaos"','per_page':20}),
]
with s.concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 rows=list(ex.map(s.fetch,jobs))
(s.ROOT/'followup_search_log.json').write_text(s.json.dumps(rows,indent=2),encoding='utf8')
try:
 data=s.json.loads((s.ROOT/'openalex_doi.txt').read_text(encoding='utf8'))
 ident=data['id'].rsplit('/',1)[-1]
 rows.append(s.fetch(('openalex_citing','https://api.openalex.org/works',{'filter':'cites:'+ident,'per-page':200,'sort':'publication_date:desc'})))
except Exception as e:
 rows.append(s.fetch(('openalex_citing_doi','https://api.openalex.org/works',{'filter':'cites:doi:10.1214/13-PS218','per-page':200})))
(s.ROOT/'followup_search_log.json').write_text(s.json.dumps(rows,indent=2),encoding='utf8')
