from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re,xml.etree.ElementTree as ET,datetime
root=Path(__file__).resolve().parents[1]
report=(root/'REPORT.md').read_text();assert report.splitlines()[0]=='MINOR'
assert 'PLACEHOLDER' not in report and '\x0b' not in report
missing=[]
for target in re.findall(r'\]\(([^)]+)\)',report):
 if '://' not in target and not target.startswith('#') and not (root/target).exists():missing.append(target)
assert not missing,missing
assert all(p.suffix=='.txt' and p.read_text() for p in (root/'sources').iterdir())
for p in root.rglob('*'):
 if p.is_file():
  assert p.suffix.lower() not in ('.pdf','.png','.jpg','.jpeg','.tiff','.webp'),str(p)
  with p.open('rb') as f:assert f.read(5)!=b'%PDF-',str(p)
source_hashes=0
for line in (root/'data'/'source_manifest.jsonl').read_text().splitlines():
 d=json.loads(line);p=root/'sources'/(d['name']+'.txt')
 assert hashlib.sha256(p.read_bytes()).hexdigest()==d['text_sha256'];source_hashes+=1
short=[json.loads(x) for x in (root/'data'/'ring_results.jsonl').read_text().splitlines()]
long=[json.loads(x) for x in (root/'data'/'ring_long.jsonl').read_text().splitlines()]
assert len(short)==26 and len(long)==8
assert all(x['nice']==10 and x['n']==10000 and 0<=x['current']<=1 for x in short+long)
summary=json.loads((root/'data'/'summary.json').read_text());assert summary['max_simulator_rss_bytes']<4*1024**3
assert summary['analysis_peak_rss_bytes']<4*1024**3
assert F(2)-(F(1,10)*2+F(9,10))==F(9,10)
assert abs(summary['predictions']['2']['J']*float(F(9,10))-summary['predictions']['2']['halfwidth'])<1e-14
assert json.loads((root/'data'/'growth_checks.json').read_text())['endpoint_checks']==1291
for r in json.loads((root/'data'/'rational_validation.json').read_text()):assert r['exact_balance']
ET.parse(root/'data'/'current_density.svg')
# The supplied manifest permits checking the input code was not changed.
claim_hashes=0
for entry in json.loads((root/'claim_files'/'data'/'code_manifest.json').read_text()):
 p=root/'claim_files'/entry['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'];claim_hashes+=1
result=dict(time=datetime.datetime.now().astimezone().isoformat(),verdict='MINOR',source_hashes=source_hashes,claim_code_hashes_unchanged=claim_hashes,large_ring_records=len(short)+len(long),all_large_ring_nice=10,small_ring_rational_balances=4,growth_endpoints=1291,report_links_valid=True,svg_valid=True,no_pdfs_or_raster_images=True,source_directory_text_only=True,simulator_peak_bytes=summary['max_simulator_rss_bytes'],analysis_peak_bytes=summary['analysis_peak_rss_bytes'])
(root/'data'/'final_audit.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
