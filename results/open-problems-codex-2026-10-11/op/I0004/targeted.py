exec(open('research.py',encoding='utf8').read().split('queries=')[0])
exec('def fetch'+open('research.py',encoding='utf8').read().split('def fetch')[1].split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
 'arxiv_bremont':'https://export.arxiv.org/api/query?search_query=au:Bremont&max_results=60',
 'arxiv_gpln':'https://export.arxiv.org/api/query?search_query=ti:%22Transient%20random%20walks%22&max_results=30',
 'arxiv_recent':'https://export.arxiv.org/api/query?search_query=all:%22oriented%20lattices%22&sortBy=submittedDate&sortOrder=descending&max_results=40',
 'crossref_target':'https://api.crossref.org/works?query='+urllib.parse.quote('Bremont stratified quasi periodic recurrence random walks')+'&rows=20',
 'openalex_retry':'https://api.openalex.org/works?search='+urllib.parse.quote('2609.07621')+'&per_page=5',
 'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2609.07621',
 'semantic_source':'https://api.semanticscholar.org/graph/v1/paper/ARXIV:2609.07621?fields=title,year,citations.title,citations.year,citations.externalIds',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(lambda kv:fetch(*kv),queries.items()))
(ROOT/'targeted_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for r in results:print(json.dumps(r))
