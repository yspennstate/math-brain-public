"""Download PDFs in memory, keep only pdftotext output and a text provenance ledger."""
import datetime, hashlib, pathlib, subprocess, sys, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
name, url = sys.argv[1:3]
req = urllib.request.Request(url, headers={'User-Agent': 'D0064 literature research'})
with urllib.request.urlopen(req, timeout=90) as response:
    blob = response.read(30_000_000)
if not blob.startswith(b'%PDF'):
    raise ValueError('Expected PDF; no file saved')
p = subprocess.run(['pdftotext', '-layout', '-', '-'], input=blob, capture_output=True, check=True)
txt = p.stdout.decode('utf-8')
path = ROOT / 'sources' / (name + '.txt')
path.write_text(txt)
with (ROOT / 'sources' / 'MANIFEST.txt').open('a') as f:
    f.write(f'{name}.txt\nURL: {url}\nUTC: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\nPDF SHA256 (not retained): {hashlib.sha256(blob).hexdigest()}\nText SHA256: {hashlib.sha256(p.stdout).hexdigest()}\nPages: {txt.count(chr(12))}\n\n')
print(f'{path.name}: {len(txt)} characters, {txt.count(chr(12))} pages')
