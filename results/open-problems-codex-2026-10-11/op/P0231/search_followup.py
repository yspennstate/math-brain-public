import research_fetch as f, urllib.parse as u, concurrent.futures as c, json
Q={
'openalex_doi':'https://api.openalex.org/works/https://doi.org/10.30757/ALEA.v20-59',
'openalex_citing':'https://api.openalex.org/works?filter=cites:doi:10.30757/ALEA.v20-59&per-page=50',
'semantic_search':'https://api.semanticscholar.org/graph/v1/paper/search?query=Poissonian%20coloring&limit=20&fields=title,year,externalIds',
'arxiv_broad':'https://export.arxiv.org/api/query?search_query='+u.quote('(all:"Poisson" AND all:"coloring") OR (all:"Poissonian" AND all:"colouring")')+'&max_results=60&sortBy=submittedDate&sortOrder=descending',
'crossref_exact':'https://api.crossref.org/works?query.title='+u.quote('Poisson coloring frontier dimension zero one')+'&rows=15',
'github_broad':'https://api.github.com/search/repositories?q='+u.quote('Poisson coloring frontier'),
}
with c.ThreadPoolExecutor(max_workers=6) as p: results=list(p.map(lambda kv:f.fetch(*kv),Q.items()))
(f.ROOT/'search_followup_log.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print(json.dumps(results,indent=2))
