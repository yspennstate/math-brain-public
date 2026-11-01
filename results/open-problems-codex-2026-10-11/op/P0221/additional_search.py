from research import fetch,ROOT
import concurrent.futures,urllib.parse as U
qs={
'author_problem':'https://www.stat.berkeley.edu/~aldous/Research/OP/online_zeta3.html',
'arxiv_exact':'https://export.arxiv.org/api/query?search_query='+U.quote('all:"online random" AND all:"spanning"')+'&max_results=40',
'crossref_aldous':'https://api.crossref.org/works?query='+U.quote('Aldous Angel Berestycki online spanning')+'&rows=15',
'openalex_alt':'https://api.openalex.org/works?search='+U.quote('Online purchasing under uncertainty')+'&per-page=5',
'semantic_match':'https://api.semanticscholar.org/graph/v1/paper/URL:https://www.stat.berkeley.edu/~aldous/Research/OP/Beres2008.pdf?fields=title,authors,year,citations.title,citations.year,citations.externalIds',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: rs=list(ex.map(fetch,qs.items()))
with (ROOT/'LITERATURE.md').open('a',encoding='utf-8') as f:
 for a,b,c,d in rs:f.write(f'\n2026-10-11 | {a} | {b} | {c} ({d} bytes)\n')
for r in rs:print(r)
