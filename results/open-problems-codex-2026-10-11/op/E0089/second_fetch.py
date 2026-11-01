import urllib.request,pathlib,concurrent.futures,json,pymupdf
ids=['math/0609802','1505.05484','1302.7014']
def f(a):
 u='https://arxiv.org/pdf/'+a;k=a.replace('/','_')
 try:
  b=urllib.request.urlopen(u,timeout=45).read();pathlib.Path('second_'+k+'.pdf').write_bytes(b);d=pymupdf.open(stream=b,filetype='pdf');s='\n'.join(f'\n--- PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(d));pathlib.Path('second_'+k+'.txt').write_text(s,encoding='utf8');print(a,s[:1800]);return[a,u,'OK']
 except Exception as e:return[a,u,str(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(f,ids))
pathlib.Path('second_fetch_log.json').write_text(json.dumps(r,indent=2),encoding='utf8')
