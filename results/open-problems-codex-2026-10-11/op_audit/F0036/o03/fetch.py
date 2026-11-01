import requests, pathlib, concurrent.futures
import pymupdf
root=pathlib.Path(__file__).parent
urls={'special':'https://arxiv.org/pdf/0806.2326','original':'https://arxiv.org/pdf/math/0610625','survey':'https://arxiv.org/pdf/1506.00724'}
def fetch(item):
 name,url=item
 r=requests.get(url,timeout=60); r.raise_for_status()
 (root/(name+'.pdf')).write_bytes(r.content)
 d=pymupdf.open(stream=r.content,filetype='pdf')
 (root/(name+'.txt')).write_text('\n'.join('PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf-8')
 return name,len(d)
print(list(concurrent.futures.ThreadPoolExecutor(3).map(fetch,urls.items())))
