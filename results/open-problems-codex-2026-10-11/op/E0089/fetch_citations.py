import pathlib,urllib.request,concurrent.futures,json,pymupdf
ids=['2501.18976','2011.04572','1806.11405']
def f(a):
 u='https://arxiv.org/pdf/'+a
 try:
  b=urllib.request.urlopen(u,timeout=45).read();pathlib.Path(a+'.pdf').write_bytes(b);d=pymupdf.open(stream=b,filetype='pdf');s='\n'.join(f'\n--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d));pathlib.Path(a+'.txt').write_text(s,encoding='utf8');print(a,s[:1400]);
  for phrase in ['Bartha','regular graph','noise sensit','bootstrap']:
   positions=[i for i in range(len(s)) if s.startswith(phrase,i)][:8]
   print(phrase,[s[max(0,i-100):i+250] for i in positions])
  return [a,u,'OK']
 except Exception as e:return [a,u,str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(f,ids))
pathlib.Path('citation_fetch_log.json').write_text(json.dumps(r,indent=2),encoding='utf8')
