import urllib.request,urllib.parse,pymupdf
from pathlib import Path
items={
 'askey_api':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"Askey-scheme"','max_results':5}),
 'askey':'https://arxiv.org/pdf/math/9602214',
}
for name,url in items.items():
 try:
  data=urllib.request.urlopen(url,timeout=40).read()
  if name=='askey':
   Path(name+'.pdf').write_bytes(data);d=pymupdf.open(name+'.pdf')
   text='\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d));Path(name+'.txt').write_text(text,encoding='utf-8');print(name,len(d),text[:1100])
  else:Path(name+'.txt').write_bytes(data);print(name,'downloaded')
 except Exception as e:print(name,str(e))
