"""Retrieve source PDFs in memory, retain only pdftotext output. No PDF files."""
import urllib.request, subprocess, pathlib, hashlib, json, datetime
ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCES = {
 'seppalainen_1999': 'https://arxiv.org/pdf/math/9906194',
 'sly_2016': 'https://arxiv.org/pdf/1609.06589',
 'seppalainen_notes': 'https://people.math.wisc.edu/~tseppalainen/excl-book/ajo.pdf',
 'bahadoran_bodineau_2018': 'https://arxiv.org/pdf/1602.06718',
 'bahadoran_guiol_ravishankar_saada_2014': 'https://arxiv.org/pdf/1201.2160',
 'bahadoran_mountford_ravishankar_saada_2020': 'https://arxiv.org/pdf/1801.01654',
 'basu_sidoravicius_sly_2014': 'https://arxiv.org/pdf/1408.3464',
}
for name, url in SOURCES.items():
 try:
  req = urllib.request.Request(url,headers={'User-Agent':'Independent mathematical referee, source verification'})
  raw = urllib.request.urlopen(req,timeout=90).read()
  if not raw.startswith(b'%PDF'): raise ValueError('Not PDF')
  txt = subprocess.run(['pdftotext','-layout','-','-'],input=raw,check=True,stdout=subprocess.PIPE).stdout
  (ROOT/'sources'/f'{name}.txt').write_bytes(txt)
  record=dict(name=name,url=url,time=datetime.datetime.now(datetime.timezone.utc).isoformat(),pdf_bytes=len(raw),text_sha256=hashlib.sha256(txt).hexdigest())
  with (ROOT/'data'/'source_manifest.jsonl').open('a') as f: f.write(json.dumps(record)+'\n')
  print(name,len(txt),flush=True)
 except Exception as e: print(name,type(e).__name__,str(e),flush=True)
