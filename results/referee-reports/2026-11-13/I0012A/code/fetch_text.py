"""Fetch a PDF in memory and save only pdftotext output; no PDF file is created."""
import hashlib, json, pathlib, subprocess, sys, urllib.request
url, target = sys.argv[1:]
raw = urllib.request.urlopen(url, timeout=60).read()
if not raw.startswith(b'%PDF'):
    raise ValueError('Not a PDF response')
p = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw, capture_output=True, check=True)
pathlib.Path(target).write_bytes(p.stdout)
print(json.dumps({'url':url, 'target':target, 'pdf_bytes_in_memory':len(raw), 'sha256_pdf':hashlib.sha256(raw).hexdigest(), 'text_bytes':len(p.stdout), 'pages':p.stdout.count(b'\f')}))
