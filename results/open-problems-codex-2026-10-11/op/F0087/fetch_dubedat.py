import urllib.request,pathlib
P=pathlib.Path(__file__).parent
u='https://arxiv.org/pdf/1110.2808'
b=urllib.request.urlopen(u,timeout=45).read();(P/'dubedat.pdf').write_bytes(b)
import pymupdf
D=pymupdf.open(P/'dubedat.pdf');(P/'dubedat.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(D)),encoding='utf8');print(len(D))
