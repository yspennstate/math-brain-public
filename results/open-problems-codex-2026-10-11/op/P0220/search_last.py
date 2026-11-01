from pathlib import Path
import urllib.request,urllib.parse,concurrent.futures
items=[('openalex_source_lookup','https://api.openalex.org/works/https://doi.org/10.1090/S0273-0979-99-00796-X'),('variations2021','https://arxiv.org/pdf/2106.11186'),('arxiv_erickson','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"Explicit marginal distributions" AND all:"Robinson"')+'&max_results=5')]
def f(it):
 n,u=it
 try:
  data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'P0220-research/1.0'}),timeout=25).read();Path(n+('.pdf' if n=='variations2021' else '.raw')).write_bytes(data);r='OK '+str(len(data))
 except Exception as e:r=str(e)
 with Path('LITERATURE.md').open('a',encoding='utf8') as out:out.write('\n- 2026-10-11 '+n+': '+u+'\n  Result: '+r+'\n')
 return n,r
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for a in ex.map(f,items):print(a)
