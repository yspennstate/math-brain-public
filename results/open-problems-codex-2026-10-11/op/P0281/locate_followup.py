from pathlib import Path
import urllib.request,concurrent.futures,json
urls={'followup.pdf':'https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ-followup.pdf','followup_alt.pdf':'https://lpetrov.cc/LaTeX/2025-03-19-AIM-KPZ/2025-03-19-AIM-KPZ-follow-up.pdf','aim_workshop.html':'https://aimath.org/workshops/upcoming/roadstokpz/'}
def f(it):
 k,u=it
 try:
  r=urllib.request.urlopen(u,timeout=25);b=r.read();Path(k).write_bytes(b);return[k,u,r.status,len(b)]
 except Exception as e:return[k,u,str(e)]
r=list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(f,urls.items()));Path('search_log_5.json').write_text(json.dumps(r,indent=2));print(r)
