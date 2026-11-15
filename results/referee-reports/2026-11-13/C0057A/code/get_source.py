"""Fetch PDF bytes into memory, extract text; never save PDF/image files."""
import io, json, sys, hashlib, datetime
from pathlib import Path
import requests
from pypdf import PdfReader
url, name = sys.argv[1:]
r = requests.get(url, timeout=90); r.raise_for_status()
reader=PdfReader(io.BytesIO(r.content))
pages=[p.extract_text() or '' for p in reader.pages]
p=Path('sources')/(name+'.txt')
p.write_text('\n\n'.join(f'===== PDF PAGE {i+1} =====\n{s}' for i,s in enumerate(pages)))
with Path('data/source_manifest.jsonl').open('a') as f:
 f.write(json.dumps(dict(name=name,url=url,retrieved=datetime.datetime.now().isoformat(),pdf_sha256=hashlib.sha256(r.content).hexdigest(),pages=len(pages),text=str(p)))+'\n')
print(name,len(pages),'pages',p.stat().st_size,'text bytes')
