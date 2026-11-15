"""Fetch source PDFs in memory, persist only pdftotext output and metadata."""
import argparse, datetime, hashlib, json, pathlib, subprocess, urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('name');p.add_argument('url');a=p.parse_args()
b=urllib.request.urlopen(a.url,timeout=90).read()
if not b.startswith(b'%PDF'): raise ValueError('Response is not PDF')
r=subprocess.run(['pdftotext','-layout','-','-'],input=b,capture_output=True,check=True)
out=ROOT/'sources'/(a.name+'.txt');out.write_bytes(r.stdout)
manifest=ROOT/'data/source_manifest.json';records=json.loads(manifest.read_text()) if manifest.exists() else []
record={'name':a.name,'url':a.url,'retrieved':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pdf_sha256':hashlib.sha256(b).hexdigest(),'text_sha256':hashlib.sha256(r.stdout).hexdigest(),'pdf_persisted':False,'pages':r.stdout.count(b'\f')}
records.append(record);manifest.write_text(json.dumps(records,indent=2)+'\n');print(record)
