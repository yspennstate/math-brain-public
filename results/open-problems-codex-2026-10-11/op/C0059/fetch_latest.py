import requests,pathlib,concurrent.futures,pymupdf,re
ids=['2411.05541','2311.08571','2412.02666']
def get(i):
 try:
  r=requests.get('https://arxiv.org/pdf/'+i,timeout=40);r.raise_for_status();pathlib.Path(i+'.pdf').write_bytes(r.content);d=pymupdf.open(i+'.pdf');t='\n\n'.join('PDF PAGE '+str(j+1)+'\n'+p.get_text() for j,p in enumerate(d));pathlib.Path(i+'.txt').write_text(t,encoding='utf8')
  with open('LITERATURE.md','a',encoding='utf8') as f:f.write('\n- 2026-10-12 paper fetch '+r.url+' HTTP '+str(r.status_code)+'; '+str(len(d))+' pages, local '+i+'.pdf/.txt\n')
  return i,t[:1700],[(t[max(0,m.start()-130):m.end()+220]).replace('\n',' ') for m in list(re.finditer('transien|recurr',t,re.I))[:12]]
 except Exception as e:return i,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for x in ex.map(get,ids):print(x,flush=True)
