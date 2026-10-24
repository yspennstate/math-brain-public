import urllib.request, pathlib
u='https://alea.math.cnrs.fr/articles/v15/15-15.pdf'
p=pathlib.Path('source.pdf'); p.write_bytes(urllib.request.urlopen(u,timeout=60).read())
import pymupdf
d=pymupdf.open(p); pathlib.Path('source.txt').write_text('\n'.join(page.get_text() for page in d),encoding='utf8')
print('downloaded',len(d),'pages')
