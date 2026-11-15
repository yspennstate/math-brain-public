"""Fetch papers into plain text; PDF bytes exist only in memory and pipes."""
import argparse, datetime, hashlib, json, pathlib, subprocess, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
def fetch(name, url):
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (mathematical literature study)'})
    raw = urllib.request.urlopen(req, timeout=90).read()
    if raw.startswith(b'%PDF'):
        run = subprocess.run(['pdftotext','-layout','-','-'],input=raw,capture_output=True,check=True)
        text = run.stdout.decode('utf-8')
    else:
        text = raw.decode('utf-8')
    out=ROOT/'sources'/name
    out.write_text(text)
    meta={'name':name,'url':url,'fetched_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'download_sha256':hashlib.sha256(raw).hexdigest(),'text_sha256':hashlib.sha256(text.encode()).hexdigest(),
          'text_pages':text.count('\f'),'bytes':len(text.encode())}
    with (ROOT/'sources'/'manifest.jsonl').open('a') as f: f.write(json.dumps(meta)+'\n')
    print(meta)
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('name'); p.add_argument('url'); a=p.parse_args(); fetch(a.name,a.url)
