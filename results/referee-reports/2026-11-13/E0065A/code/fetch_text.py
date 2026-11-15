"""Fetch a PDF into RAM and save only its extracted plain text, with page markers."""
import io, sys, hashlib, urllib.request
from pathlib import Path
from pypdf import PdfReader
url, out = sys.argv[1:3]
req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (mathematical literature verification)'})
raw = urllib.request.urlopen(req, timeout=60).read()
r = PdfReader(io.BytesIO(raw))
text = f'Source URL: {url}\nPDF SHA256 (bytes never saved): {hashlib.sha256(raw).hexdigest()}\nPages: {len(r.pages)}\n\n'
for i,p in enumerate(r.pages, 1):
 text += f'\n===== PDF PAGE {i} =====\n' + p.extract_text() + '\n'
Path(out).write_text(text)
print(out, len(r.pages), len(text))
