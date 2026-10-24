from pathlib import Path
import urllib.request,json,concurrent.futures
qs={'zerner_legacy_reader':'https://r.jina.ai/https://projecteuclid.org/euclid.ecp/1463434786','zerner_doi':'https://doi.org/10.1214/ecp.v7-1060','hewitt_pdf':'https://www.ams.org/tran/1955-080-02/S0002-9947-1955-0076206-8/S0002-9947-1955-0076206-8.pdf'}
def f(k,u):
 try:
  r=urllib.request.urlopen(u,timeout=35);b=r.read();Path(k+('.pdf' if k.endswith('pdf') else '.html')).write_bytes(b);return k,r.status,len(b),r.geturl()
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rs=list(ex.map(lambda x:f(*x),qs.items()))
Path('second_primary_log.json').write_text(json.dumps({'date':'2026-10-12','queries':qs,'results':rs},indent=2));print(rs)
if Path('zerner_legacy_reader.html').exists():print(Path('zerner_legacy_reader.html').read_text(encoding='utf8',errors='replace')[:22000])
