from pathlib import Path
import json,urllib.request,concurrent.futures
qs={'zerner_author':'https://www.math.uni-tuebingen.de/user/zerner/','zerner_jina':'https://r.jina.ai/https://projecteuclid.org/journals/electronic-communications-in-probability/volume-7/issue-none/A-Non-Ballistic-Law-of-Large-Numbers-for-Random-Walks/ecp.v7-1060.full'}
def f(k,u):
 try:
  r=urllib.request.urlopen(u,timeout=35);b=r.read();Path(k+'.html').write_bytes(b);return k,r.status,len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:rs=list(ex.map(lambda x:f(*x),qs.items()))
Path('second_author_log.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':rs},indent=2));print(rs)
for f in ['zerner_emis_html.html','zerner_jina.html','zerner_author.html']:
 if Path(f).exists():print('\nFILE',f,Path(f).read_text(encoding='utf8',errors='replace')[:11000])
