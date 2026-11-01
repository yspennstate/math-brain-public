from pathlib import Path
import urllib.request,concurrent.futures,xml.etree.ElementTree as E
queries=[('borodin_rains_api','https://export.arxiv.org/api/query?search_query=ti:%22Eynard%22+AND+au:%22Rains%22&max_results=5'),('new_source_check','https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html')]
def fetch(it):
 n,u=it
 try:
  data=urllib.request.urlopen(u,timeout=30).read();Path(n+'.raw').write_bytes(data);s='OK '+str(len(data))
 except Exception as e:s=str(e)
 return n,u,s
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for n,u,s in ex.map(fetch,queries):
  with Path('LITERATURE.md').open('a',encoding='utf8') as f:f.write('\n- Continuation 2026-10-11 '+n+': '+u+'\n  Result: '+s+'\n')
  print(n,s)
