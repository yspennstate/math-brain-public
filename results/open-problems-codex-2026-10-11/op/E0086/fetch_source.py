from pathlib import Path
import urllib.request
p=Path('.')
p.joinpath('STATUS.md').write_text('STATE: WORKING\nNEXT: Verify source Open problem 2 and search subsequent literature.\nVERDICT: NO_PROGRESS\n\n2026-10-11: Started source verification and read-only brain recall.\n',encoding='utf-8')
url='https://arxiv.org/pdf/1606.03787'
b=urllib.request.urlopen(url,timeout=60).read(); p.joinpath('source.pdf').write_bytes(b)
try:
 import pymupdf
 d=pymupdf.open('source.pdf'); p.joinpath('source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+page.get_text() for i,page in enumerate(d)),encoding='utf-8')
 print('pages',len(d))
except ImportError:
 import pypdf
 d=pypdf.PdfReader('source.pdf'); p.joinpath('source.txt').write_text('\n'.join(f'\nPDF PAGE {i+1}\n'+page.extract_text() for i,page in enumerate(d.pages)),encoding='utf-8')
