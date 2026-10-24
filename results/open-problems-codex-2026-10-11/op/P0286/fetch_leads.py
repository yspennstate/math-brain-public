from pathlib import Path
import urllib.request, concurrent.futures, json, pymupdf
urls={
 'decoupling':'https://arxiv.org/pdf/2504.00765',
 'martin':'https://arxiv.org/pdf/1810.10650',
 'ferrari_martin':'https://arxiv.org/pdf/math/060805 multi',
}
urls.pop('ferrari_martin')
def fetch(k,u):
 try:
  data=urllib.request.urlopen(u,timeout=45).read(); Path(k+'.pdf').write_bytes(data)
  doc=pymupdf.open(k+'.pdf'); text='\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc)); Path(k+'.txt').write_text(text,encoding='utf-8')
  return k,len(data),len(doc)
 except Exception as e:return k,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:print(list(ex.map(lambda x:fetch(*x),urls.items())))
