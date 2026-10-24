import urllib.request,concurrent.futures
from pathlib import Path
ids=['2307.05097','2502.04113','2402.02562','2608.29501','2105.04082']
def fetch(a):
 try:
  b=urllib.request.urlopen('https://arxiv.org/pdf/'+a,timeout=45).read();Path('paper_'+a+'.pdf').write_bytes(b)
  import pymupdf
  d=pymupdf.open(stream=b,filetype='pdf');s='\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d));Path('paper_'+a+'.txt').write_text(s,encoding='utf-8')
  return a,len(d),s[:7000]
 except Exception as e:return a,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for x in ex.map(fetch,ids):print(x)
