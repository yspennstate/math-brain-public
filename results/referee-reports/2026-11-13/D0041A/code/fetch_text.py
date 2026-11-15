"""Download papers into RAM and retain only page-marked plain text."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
import io, sys, hashlib, json, datetime, re
from pathlib import Path
import requests
from pypdf import PdfReader
root=Path(__file__).resolve().parents[1]
name,url=sys.argv[1:3]
r=requests.get(url, timeout=90);r.raise_for_status()
raw=r.content
reader=PdfReader(io.BytesIO(raw))
text='SOURCE: '+url+'\nFETCHED: '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'\nPDF SHA256 (bytes not retained): '+hashlib.sha256(raw).hexdigest()+'\n'
text+='\n'.join(f'\n===== PDF PAGE {i+1} =====\n'+(p.extract_text(extraction_mode='layout') or '') for i,p in enumerate(reader.pages))
text=re.sub(r'[\x00-\x08\x0b-\x1f]','',text)
(root/'sources'/f'{name}.txt').write_text(text)
print(name,len(reader.pages),len(text))
