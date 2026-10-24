import urllib.request, pathlib
u='https://math.washington.edu/sites/math/files/documents/research/1302.6958.pdf'
p=pathlib.Path('source.pdf')
p.write_bytes(urllib.request.urlopen(u,timeout=60).read())
try:
 import pymupdf
 d=pymupdf.open(p)
 pathlib.Path('source.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+page.get_text() for i,page in enumerate(d)),encoding='utf8')
 print('pages',len(d))
except ImportError:
 import pypdf
 d=pypdf.PdfReader(p)
 pathlib.Path('source.txt').write_text('\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+page.extract_text() for i,page in enumerate(d.pages)),encoding='utf8')
 print('pages',len(d.pages))
