import urllib.request, pathlib
u='https://www.imo.universite-paris-saclay.fr/~nicolas.curien/cours/peccot.pdf'
p=pathlib.Path('source.pdf'); p.write_bytes(urllib.request.urlopen(u,timeout=60).read())
import pymupdf
D=pymupdf.open(p)
pathlib.Path('source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+x.get_text() for i,x in enumerate(D)),encoding='utf8')
print(len(D))
