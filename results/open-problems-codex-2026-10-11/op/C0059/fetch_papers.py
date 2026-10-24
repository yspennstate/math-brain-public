import requests,pathlib,concurrent.futures,pymupdf
ids=['1910.09623','1506.01590','1912.08790']
def get(i):
 try:
  r=requests.get('https://arxiv.org/pdf/'+i,timeout=45);r.raise_for_status();pathlib.Path(i+'.pdf').write_bytes(r.content);d=pymupdf.open(i+'.pdf');pathlib.Path(i+'.txt').write_text('\n\n'.join('PDF PAGE '+str(j+1)+'\n'+p.get_text() for j,p in enumerate(d)),encoding='utf8');return i,len(d)
 except Exception as e:return i,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:print(list(ex.map(get,ids)))
