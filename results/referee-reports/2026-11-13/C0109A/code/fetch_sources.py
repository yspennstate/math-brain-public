"""Fetch papers into plain text; PDF response bytes never go to the filesystem."""
import argparse, hashlib, io, json, subprocess, time
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[1]

def fetch(name, url):
    r = requests.get(url, timeout=100)
    r.raise_for_status()
    raw = r.content
    if raw.startswith(b'%PDF'):
        p = subprocess.run(['pdftotext', '-layout', '-', '-'], input=raw,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        txt = p.stdout.decode('utf-8')
    else:
        raise ValueError('Expected PDF response, got ' + r.headers.get('Content-Type', '?'))
    out = ROOT / 'sources' / (name + '.txt')
    out.write_text(txt)
    item = {'name': name, 'url':url, 'retrieved_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'text_sha256':hashlib.sha256(txt.encode()).hexdigest(), 'characters':len(txt),
            'pdf_pages':txt.count('\f'), 'conversion':'pdftotext -layout stdin/stdout; no PDF saved'}
    with (ROOT/'sources'/'manifest.jsonl').open('a') as f:
        f.write(json.dumps(item)+'\n')
    print(json.dumps(item), flush=True)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('name'); ap.add_argument('url')
    a=ap.parse_args(); fetch(a.name,a.url)
