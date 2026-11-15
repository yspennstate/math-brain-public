"""Re-aggregate saved observations and check the requested artifact constraints."""
from pathlib import Path
import csv,json,statistics
base=Path('.')
rows=list(csv.DictReader((base/'data/paths.csv').open()))
summary=json.loads((base/'data/simulation_summary.json').read_text())
results=[]
for s in summary['summary']:
 a=[r for r in rows if r['model']==s['model']]
 completed=[int(r['neighbourhood_time']) for r in a if r['neighbourhood_time']]
 assert len(a)==s['paths']==80
 assert len(completed)==s['neighbourhood_swallowed']
 assert sum(bool(r['root_corner_time']) for r in a)==s['root_swallowed']
 assert sum(r['censor']=='time_cap' for r in a)==s['time_censored']
 assert sum(r['censor']=='edge_cap' for r in a)==s['edge_censored']
 assert len(completed)+s['time_censored']+s['edge_censored']==len(a)
 assert statistics.median(completed)==s['median_completed_only']
 assert max(completed)==s['max_completed_time']
 for r in a:
  if r['neighbourhood_time']:
   assert r['root_corner_time'] and int(r['root_corner_time'])<=int(r['neighbourhood_time'])
  if r['root_corner_time']: assert int(r['root_corner_time'])<=int(r['steps'])
 results.append(dict(model=s['model'],rows=len(a),absorbed=len(completed)))
assert (base/'REPORT.md').read_text().splitlines()[0]=='PARTIAL'
for p in base.rglob('*'):
 if not p.is_file():continue
 assert p.suffix.lower() not in ('.pdf','.png','.jpg','.jpeg','.webp','.gif','.tif','.tiff','.bmp'),str(p)
 if p.parent.name=='sources':
  assert p.suffix=='.txt',str(p)
  text=p.read_text()
  assert '\x00' not in text,str(p)
  assert not p.read_bytes().startswith(b'%PDF-')
source_rows=[json.loads(s) for s in (base/'data/source_manifest.jsonl').read_text().splitlines()]
assert len({r['name'] for r in source_rows})==len(source_rows)
for r in source_rows:
 assert Path(r['text']).read_text().count('===== PDF PAGE')==r['pages']
out=dict(simulation_reaggregation=results,source_pdf_extractions=len(source_rows),
         no_pdf_or_image_files=True,source_texts_decode=True,report_status='PARTIAL')
(base/'data/artifact_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
