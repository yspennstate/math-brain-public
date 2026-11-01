from research import fetch,ROOT
import concurrent.futures,urllib.parse as U
qs={
'corrigendum_xml':'https://onlinelibrary.wiley.com/doi/full-xml/10.1002/rsa.21012',
'frieze_home':'https://www.math.cmu.edu/~af1p/',
'semantic_purchasing':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1002/rsa.20764?fields=title,year,citations.title,citations.year,citations.externalIds,references.title,references.paperId',
'openalex_source_id':'https://api.openalex.org/works?filter=title.search:'+U.quote('Online Random Weight Minimal Spanning Trees and a Stochastic Coalescent')+'&select=id,title,cited_by_count,cited_by_api_url',
'arxiv_limit':'https://export.arxiv.org/api/query?search_query='+U.quote('all:"spanning tree" AND (all:"purchasing" OR all:"online cost" OR all:"Berestycki")')+'&max_results=40',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: rs=list(ex.map(fetch,qs.items()))
with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:
 for a,b,c,d in rs:f.write(f'\n2026-10-11 | {a} | {b} | {c} ({d} bytes)\n')
 f.write('\n2026-10-11 | Crossref DOI lookup | https://api.crossref.org/works/10.1002/rsa.21012 | OK; saved corrigendum_metadata.json.\n')
for r in rs:print(r)
