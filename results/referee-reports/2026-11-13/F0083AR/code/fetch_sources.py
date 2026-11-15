"""Fetch scholarly PDF bytes into memory; retain only extracted plain text."""
import os
for variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[variable] = '1'
import argparse
import datetime
import hashlib
import pathlib
import subprocess
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('url')
args = parser.parse_args()
assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
root = pathlib.Path(__file__).resolve().parents[1]
request = urllib.request.Request(args.url, headers={'User-Agent': 'Independent mathematical referee source verification'})
with urllib.request.urlopen(request, timeout=90) as response:
    raw = response.read(35_000_001)
    final_url = response.url
assert len(raw) <= 35_000_000
assert raw.startswith(b'%PDF'), (final_url, raw[:80])
result = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
destination = root / 'sources' / (args.name + '.txt')
destination.parent.mkdir(exist_ok=True)
destination.write_bytes(result.stdout)
with (root / 'sources' / 'manifest.txt').open('a') as stream:
    stream.write(f'{datetime.datetime.now().astimezone().isoformat()}\n{args.name}\n{args.url}\nresolved: {final_url}\nPDF sha256 (bytes not saved): {hashlib.sha256(raw).hexdigest()}\ntext sha256: {hashlib.sha256(result.stdout).hexdigest()}\n\n')
print(destination.relative_to(root), 'bytes', len(result.stdout), 'pages', result.stdout.count(b'\f'))
