#!/usr/bin/env python3
"""Check artifact constraints and locate cited results in saved source texts."""
import os
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
import ast,hashlib,json,re
from pathlib import Path
assert Path('REPORT.md').read_text().splitlines()[0]=='PARTIAL'
for p in Path('code').glob('*.py'):ast.parse(p.read_text(),filename=str(p))
records=[json.loads(line) for line in Path('data/source_manifest.jsonl').read_text().splitlines()]
for r in records:
 p=Path('sources',r['name']+'.txt')
 assert hashlib.sha256(p.read_bytes()).hexdigest()==r['text_sha256']
 assert re.search(r'===== PDF PAGE \d+ =====',p.read_text())
for p in Path('sources').iterdir():
 assert p.suffix=='.txt' and p.is_file(),str(p)
 assert not any(ord(c)<32 and c not in '\n\t\r' for c in p.read_text()),str(p)
for p in Path('.').rglob('*'):
 if not p.is_file():continue
 assert p.suffix.lower() not in {'.pdf','.png','.jpg','.jpeg','.gif','.webp','.tif','.tiff','.djvu','.ps'},str(p)
 with p.open('rb') as f:head=f.read(8)
 assert not head.startswith((b'%PDF',b'\x89PNG',b'\xff\xd8\xff',b'GIF8')),str(p)
locators={
'bou_rabee_peres_2026':[r'Theorem 1\.1',r'Theorem 1\.2',r'Problem 3'],
'bosi_2019':[r'Theorem 9\.'],
'campanino_petritis_2003':[r'Theorem 1\.6',r'Theorem 1\.7',r'Theorem 1\.8'],
'campanino_petritis_2014':[r'Theorem 1\.5'],
'guillotin_leny_dynamic':[r'Theorem 1'],
'guillotin_leny_functional':[r'Theorem 2\.'],
'cgps_2011_published':[r'THEOREM 20\.'],
'pene_2009':[r'Theorem 1\.',r'Theorem 2\.'],
'devulder_pene':[r'Theorem 1\.'],
'bremont_2017_published':[r'Theorem 2\.4\.',r'Proposition 7\.1\.'],
'bremont_quasiperiodic':[r'Theorem 3\.2\.',r'Proposition 3\.3\.'],
'bremont_independent':[r'Theorem 1\.3'],
'gaudilliere_landim':[r'Theorem 2\.4\.',r'Lemma 5\.5\.'],
'ledger_toth_valko_2018':[r'Theorem 1\.1\.'],
'nguyen_2026':[r'Theorem 1\.1\.'],
'iterated_rwrs_2025':[r'Theorem 1\.1\.'],
'armstrong_bou_rabee_kuusi_2026':[r'Theorem A\('],
'gu_hao_2026':[r'Theorem 1\.1',r'Theorem 1\.2'],
'bosi_hu_peres_2022':[r'Theorem 4\.']}
index=[]
for name,patterns in locators.items():
 parts=re.split(r'===== PDF PAGE (\d+) =====',Path('sources',name+'.txt').read_text())
 for pattern in patterns:
  hits=[]
  for i in range(1,len(parts),2):
   for m in re.finditer(pattern,parts[i+1]):
    hits.append({'pdf_page':int(parts[i]),'context':parts[i+1][max(0,m.start()-20):m.end()+140].replace('\n',' ')})
  assert hits,(name,pattern)
  index.append({'source':name,'pattern':pattern,'hits':hits})
Path('data/literature_locators.json').write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n')
checks=json.loads(Path('data/check_summary.json').read_text())
quadrants=json.loads(Path('data/quadrant_checks.json').read_text())
mc=json.loads(Path('data/monte_carlo.json').read_text())
assert checks['status']=='all checks passed' and len(quadrants)==12
summary={'status':'passed','report_first_line':'PARTIAL','source_records_verified':len(records),
'cited_locator_patterns_found':len(index),'source_storage':'plain text only',
'pdf_or_image_artifacts':0,'numeric_checks':'passed','quadrant_exact_checks':len(quadrants),
'numerical_peak_rss_bytes':max(checks['peak_rss_bytes'],mc['peak_rss_bytes']),
'numerical_thread_count':1,'nice':os.getpriority(os.PRIO_PROCESS,0),
'report_sha256':hashlib.sha256(Path('REPORT.md').read_bytes()).hexdigest()}
Path('data/final_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
