from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from html.parser import HTMLParser
import requests
class Meta(HTMLParser):
 def __init__(self):super().__init__();self.out=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta' and a.get('name','').startswith('citation_'):
   self.out.append((a['name'],a.get('content','')))
ids=['0810.2994','0708.2895','0709.3995','1807.00489','1912.09300','2111.03595','1206.1449','1612.07776','1206.1893','1912.04100','1607.05484','2012.05602','1708.06950','2408.13490','2508.03631']
def get(i):
 try:
  r=requests.get('https://arxiv.org/abs/'+i,timeout=30);r.raise_for_status();m=Meta();m.feed(r.text)
  return '\n'+i+'\n'+'\n'.join(k+': '+v for k,v in m.out)+'\n'
 except Exception as e:return i+' '+repr(e)+'\n'
with ThreadPoolExecutor(max_workers=3) as pool:
 texts=list(pool.map(get,ids))
Path('sources/arxiv_metadata.txt').write_text(''.join(texts))
print(''.join(texts))
