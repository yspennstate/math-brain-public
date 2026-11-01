import urllib.request, pathlib
u='https://arxiv.org/pdf/math/0510518'
try:
 data=urllib.request.urlopen(u,timeout=60).read(); pathlib.Path('source.pdf').write_bytes(data); print(len(data))
except Exception as e: print(type(e).__name__,str(e))
try: import pymupdf; print('pymupdf available')
except ImportError:
 try: import pypdf; print('pypdf available')
 except ImportError: print('no pdf module')
