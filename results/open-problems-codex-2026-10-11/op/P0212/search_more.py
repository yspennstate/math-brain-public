exec(open('search.py',encoding='utf8').read().split('with concurrent.futures.ThreadPoolExecutor')[0])
queries={
 'arxiv_low':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"coalescing" AND all:"low density"')+'&max_results=60',
 'arxiv_ising':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('(all:"constrained Ising" OR all:"FA-1f") AND (all:limit OR all:branching)')+'&max_results=60',
 'openalex_pillai':'https://api.openalex.org/works/https://doi.org/10.1214/15-AOP1080',
 'semantic_pillai_citations':'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1214/15-AOP1080/citations?fields=title,year,authors,abstract&limit=100',
 'crossref_genealogy':'https://api.crossref.org/works?query='+urllib.parse.quote('constrained Ising genealogy scaling limit')+'&rows=25',
 'arxiv_athreya':'https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"Branching-coalescing particle systems"')+'&max_results=10',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(fetch,queries.items()))
with (root/'LITERATURE.md').open('a',encoding='utf8') as f:
 for name,url,state in results:
  f.write(f'- {name}, 2026-10-11: {url}\n  Result: {state}\n');print(name,state)
for name in ['arxiv_low','arxiv_ising','arxiv_athreya']:
 p=root/(name+'.txt')
 if p.exists():
  import xml.etree.ElementTree as E
  ns={'a':'http://www.w3.org/2005/Atom'}
  for x in E.parse(p).getroot().findall('a:entry',ns): print(x.findtext('a:id',namespaces=ns),x.findtext('a:title',namespaces=ns),x.findtext('a:summary',namespaces=ns))
