import urllib.request,concurrent.futures,json
from pathlib import Path
qs={'paper_counterexample':'https://arxiv.org/pdf/1909.03159','paper_mob':'https://arxiv.org/pdf/1307.6052','paper_zeroone':'https://projecteuclid.org/journals/annales-de-linstitut-henri-poincare-probabilites-et-statistiques/volume-52/issue-1/Zeroone-law-for-directional-transience-of-one-dimensional-excited-random/10.1214/14-AIHP615.pdf'}
def f(k,u):
 try:
  r=urllib.request.urlopen(u,timeout=40);b=r.read();Path(k+'.pdf').write_bytes(b);return k,r.status,len(b)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(lambda x:f(*x),qs.items()))
Path('search_log_3.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':r},indent=2));print(r)
