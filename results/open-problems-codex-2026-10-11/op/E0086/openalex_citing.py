from pathlib import Path
import urllib.request,json
u='https://api.openalex.org/works?filter=cites:https%3A%2F%2Fdoi.org%2F10.48550%2FarXiv.1606.03787&per-page=100'
try:
 b=urllib.request.urlopen(u,timeout=20).read();Path('search_openalex_citing_doi.txt').write_bytes(b);r=['openalex_citing_doi',u,'OK',len(b)]
except Exception as e:r=['openalex_citing_doi',u,'ERROR',str(e)]
Path('search_log4.json').write_text(json.dumps([r],indent=2));print(r)
