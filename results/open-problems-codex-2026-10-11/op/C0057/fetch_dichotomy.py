import urllib.request,pathlib,pymupdf,json
u='https://arxiv.org/pdf/2603.13642'
try:
 b=urllib.request.urlopen(u,timeout=45).read();pathlib.Path('dichotomy.pdf').write_bytes(b);d=pymupdf.open('dichotomy.pdf');pathlib.Path('dichotomy.txt').write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+x.get_text() for i,x in enumerate(d)),encoding='utf8');r='OK '+str(len(b))
except Exception as e:r=str(e)
p=pathlib.Path('search_log.json');p.write_text(json.dumps(json.loads(p.read_text())+[['dichotomy',u,r]],indent=2),encoding='utf8');print(r)
