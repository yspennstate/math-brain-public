import urllib.request, pathlib
p=pathlib.Path('.')
u='https://arxiv.org/pdf/1906.05037'
try:
 data=urllib.request.urlopen(u,timeout=50).read(); (p/'rolla.pdf').write_bytes(data)
 import pymupdf
 d=pymupdf.open('rolla.pdf'); (p/'rolla.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8')
 print('Downloaded',len(data),'bytes',len(d),'pages')
except Exception as e: print(type(e).__name__,str(e))
