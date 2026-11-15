"""Download papers into RAM; retain only extracted plain text and metadata."""
import argparse
import datetime
import hashlib
import json
import pathlib
import subprocess
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]

def fetch(name, url):
    target = ROOT / 'sources' / (name + '.txt')
    if target.exists():
        print('exists', name, flush=True)
        return
    req = urllib.request.Request(url, headers={'User-Agent': 'E0098 research source verification'})
    with urllib.request.urlopen(req, timeout=90) as response:
        content = response.read()
        final_url = response.url
    if not content.startswith(b'%PDF'):
        raise ValueError(f'{url}: not a PDF stream')
    result = subprocess.run(['pdftotext', '-layout', '-', '-'], input=content,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    extracted = result.stdout.decode('utf-8')
    pages = extracted.count('\f')
    metadata = {'url': url, 'final_url': final_url, 'fetched_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'pdf_sha256_in_memory': hashlib.sha256(content).hexdigest(), 'pdf_pages': pages,
                'method': 'pdftotext -layout stdin stdout; PDF only in RAM'}
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(metadata, ensure_ascii=False) + '\n\n' + extracted)
    print(name, pages, 'pages', len(extracted), 'text characters', flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('url')
    args = parser.parse_args()
    fetch(args.name, args.url)
