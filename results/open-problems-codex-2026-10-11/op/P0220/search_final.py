from pathlib import Path
import urllib.request,urllib.parse,concurrent.futures,json,xml.etree.ElementTree as E
q=[('crossref_1999','https://api.crossref.org/works?query.title='+urllib.parse.quote('Longest increasing subsequences from patience sorting to the Baik Deift Johansson theorem')+'&rows=3'),('arxiv_exact','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('all:"drift-jump" OR all:"leftmost Hammersley" OR (all:"patience sorting" AND all:"stationary")')+'&max_results=30'),('openalex_citations','https://api.openalex.org/works?filter=cites:doi:10.1090/S0273-0979-99-00796-X&per-page=20'),('semantic_citations','https://api.semanticscholar.org/graph/v1/paper/DOI:10.1090/S0273-0979-99-00796-X/citations?limit=100&fields=title,year,authors,url'),('later2020','https://arxiv.org/pdf/2005.13824'),('later2025','https://arxiv.org/pdf/2506.19008')]
def f(pair):
 n,u=pair
 try:
  data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'P0220-research/1.0'}),timeout=35).read();Path(n+('.pdf' if n.startswith('later') else '.raw')).write_bytes(data);s='OK '+str(len(data))
 except Exception as e:s=str(e)
 with Path('LITERATURE.md').open('a',encoding='utf8') as out:out.write('\n- 2026-10-11 '+n+': '+u+'\n  Result: '+s+'\n')
 return n,s
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for r in ex.map(f,q):print(r)
