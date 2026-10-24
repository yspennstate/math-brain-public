import urllib.request,pathlib,json
url='https://arxiv.org/pdf/1411.0040'
try:
 data=urllib.request.urlopen(url,timeout=40).read();pathlib.Path('pitman_tang.pdf').write_bytes(data)
 import pymupdf
 d=pymupdf.open('pitman_tang.pdf');pathlib.Path('pitman_tang.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.get_text() for i,p in enumerate(d)),encoding='utf8');print('pages',len(d))
except Exception as e:print(type(e).__name__,e)
p=pathlib.Path('search_log.json');a=json.loads(p.read_text());a.append(dict(service='citing_paper_pdf',url=url,date='2026-10-12',file='pitman_tang.pdf'));p.write_text(json.dumps(a,indent=2),encoding='utf8')
