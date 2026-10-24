import urllib.request,json,concurrent.futures
from pathlib import Path
qs={
'zerner_emis_html':'https://www.emis.de/journals/EJP-ECP/article/view/1060.html',
'zerner_emis_pdf':'https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/1060/1060-1-PB.pdf',
'zerner_euclid_modern':'https://projecteuclid.org/journals/electronic-communications-in-probability/volume-7/issue-none/A-Non-Ballistic-Law-of-Large-Numbers-for-Random-Walks/ecp.v7-1060.pdf'}
def f(k,u):
 try:
  r=urllib.request.urlopen(u,timeout=35);b=r.read();Path(k+('.html' if 'html' in k else '.pdf')).write_bytes(b);return k,r.status,len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(lambda x:f(*x),qs.items()))
Path('second_mirror_log.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':rs},indent=2));print(rs)
