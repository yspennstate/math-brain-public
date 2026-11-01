import urllib.request, pathlib
u='https://arxiv.org/pdf/1509.08454'
b=urllib.request.urlopen(u,timeout=60).read()
pathlib.Path('source.pdf').write_bytes(b)
import pymupdf
D=pymupdf.open('source.pdf')
pathlib.Path('source.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(D)),encoding='utf8')
print(pathlib.Path('source.txt').read_text(encoding='utf8')[:24000])
