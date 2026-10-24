from pathlib import Path
import urllib.request, concurrent.futures
import pymupdf
ids=['2609.32480','2601.07129','2603.16316','2603.16408','2602.18919']
def run(a):
 try:
  data=urllib.request.urlopen('https://arxiv.org/pdf/'+a,timeout=50).read()
  Path(a+'.pdf').write_bytes(data)
  doc=pymupdf.open(stream=data,filetype='pdf')
  txt=''.join('\nPAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc))
  Path(a+'.txt').write_text(txt,encoding='utf-8')
  print(a,txt[:1200],flush=True)
 except Exception as e: print(a,repr(e),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: list(ex.map(run,ids))
