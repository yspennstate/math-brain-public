import requests,pathlib,concurrent.futures,pymupdf
ids=['1704.05297','1602.01328','2604.24180','2603.13642','2304.01167']
def get(i):
 try:
  r=requests.get('https://arxiv.org/pdf/'+i,timeout=40);r.raise_for_status();pathlib.Path(i+'.pdf').write_bytes(r.content);d=pymupdf.open(i+'.pdf');pathlib.Path(i+'.txt').write_text('\n\n'.join('PDF PAGE '+str(j+1)+'\n'+p.get_text() for j,p in enumerate(d)),encoding='utf8');return i,len(d)
 except Exception as e:return i,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for x in ex.map(get,ids):print(x,flush=True)
