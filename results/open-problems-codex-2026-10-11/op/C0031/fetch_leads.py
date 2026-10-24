import pathlib,urllib.request,concurrent.futures,pymupdf,json
R=pathlib.Path(__file__).parent
ids=['2408.14389','1811.07038','2010.01261']
def go(a):
 url='https://arxiv.org/pdf/'+a
 try:
  with urllib.request.urlopen(url,timeout=45) as f:b=f.read()
  p=R/(a+'.pdf');p.write_bytes(b);doc=pymupdf.open(p)
  t='\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc))
  (R/(a+'.txt')).write_text(t,encoding='utf8')
  print('PAPER',a,'\n'+t[:23000],flush=True);status='OK'
 except Exception as e:status=str(e)
 return {'url':url,'date':'2026-10-11','status':status}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:log=list(ex.map(go,ids))
(R/'leads_log.json').write_text(json.dumps(log,indent=2),encoding='utf8')
