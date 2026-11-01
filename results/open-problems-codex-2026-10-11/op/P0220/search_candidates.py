import urllib.request,urllib.parse,concurrent.futures
from pathlib import Path
items=[('variations_metadata','https://api.semanticscholar.org/graph/v1/paper/c84debdbf417d764a819cb4579a17bb1f99b23d7?fields=title,authors,year,abstract,externalIds,openAccessPdf'),('erickson_metadata','https://api.semanticscholar.org/graph/v1/paper/53dba18293ea5da10145d1932fe93b98ae29eb33?fields=title,authors,year,abstract,externalIds,openAccessPdf'),('corwin2018','https://www.ams.org/journals/bull/2018-55-03/S0273-0979-2018-01623-6/S0273-0979-2018-01623-6.pdf'),('arxiv_variations','https://export.arxiv.org/api/query?search_query='+urllib.parse.quote('ti:"Variations on Hammersley"')+'&max_results=5')]
def f(it):
 n,u=it
 try:
  data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'P0220-research/1.0'}),timeout=30).read();Path(n+('.pdf' if n=='corwin2018' else '.raw')).write_bytes(data);r='OK '+str(len(data))
 except Exception as e:r=str(e)
 with Path('LITERATURE.md').open('a',encoding='utf8') as out:out.write('\n- 2026-10-11 '+n+': '+u+'\n  Result: '+r+'\n')
 return n,r
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for a in ex.map(f,items):print(a)
