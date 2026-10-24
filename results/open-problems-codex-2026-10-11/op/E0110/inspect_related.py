import urllib.request, pathlib, concurrent.futures, json
urls={
'burgers_pdf':'https://arxiv.org/pdf/1908.06591',
'crossref_rbm2020':'https://api.crossref.org/works/10.1287/moor.2019.1006',
'crossref_rbm2018':'https://api.crossref.org/works/10.1007/s11134-018-9574-1'}
def get(kv):
 k,u=kv
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as r:b=r.read()
  pathlib.Path(k+('.pdf' if k.endswith('pdf') else '.json')).write_bytes(b);s=f'OK {len(b)} bytes'
 except Exception as e:s=str(e)
 return k,u,s
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p:
 for k,u,s in p.map(get,urls.items()):
  print(k,s,flush=True)
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write(f'\n- 2026-10-11 {k}: {u}\n  {s}\n')
try:
 import pymupdf
 d=pymupdf.open('burgers_pdf.pdf');s='\n'.join(p.get_text() for p in d);pathlib.Path('burgers.txt').write_text(s,encoding='utf8')
 for line in s.splitlines():
  if any(t in line.lower() for t in ['spectral gap','poincar','ergodic','tang']):print(line)
except Exception as e:print(e)
for k in ['crossref_rbm2020','crossref_rbm2018']:
 try:
  j=json.load(open(k+'.json'))['message'];print(j.get('title'),j.get('author'),j.get('container-title'),j.get('volume'),j.get('page'))
 except Exception:pass
