"""Audit source-page locations, links, sample consistency, and final artifacts."""
import csv
import hashlib
import json
import math
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
report=(ROOT/'REPORT.md').read_text()
assert report.splitlines()[0]=='PARTIAL'
assert 'being completed' not in report and 'Work in progress' not in report
links=re.findall(r'\]\(([^)]+)\)',report)
missing=[x for x in links if not x.startswith('https:') and not (ROOT/x).exists()]
assert not missing,missing
sources=list((ROOT/'sources').iterdir())
assert all(p.is_file() and p.suffix=='.txt' for p in sources)
assert not list(ROOT.rglob('*.pdf'))
counts={}
for tag,wanted in [('main',14490),('validation',9000)]:
    rows=list(csv.DictReader((ROOT/'data'/f'{tag}_samples.csv').open()))
    assert len(rows)==wanted
    keys=[(r['ensemble'],r['n'],r['replicate'],r['region']) for r in rows]
    assert len(set(keys))==len(keys)
    for row in rows:
        n=int(row['n'])
        assert int(row['index'])=={'lower_edge':1,'bulk':n//2+1,'upper_edge':n}[row['region']]
        assert math.isclose(float(row['scaled_min']),n**1.5*float(row['minimum_coordinate']),rel_tol=1e-13)
        assert 0<=float(row['minimum_coordinate'])<=float(row['second_minimum_coordinate'])
        assert float(row['residual_l2'])<1e-9
    counts[tag]={'eigenvectors':len(rows),'matrices':len(rows)//3,
        'max_residual':max(float(row['residual_l2']) for row in rows)}
records=json.loads((ROOT/'code/theorem_pages.json').read_text())
checks=[]
for name,items in records.items():
    pages=(ROOT/'sources'/f'{name}.txt').read_text().split('\f')
    for page,needle in items:
        okay=needle in pages[page-1]
        checks.append({'source':name,'pdf_page':page,'statement':needle,'found':okay})
        assert okay,(name,page,needle)
paths=[ROOT/'REPORT.md',ROOT/'LOG.md']+sorted((ROOT/'code').glob('*.py'))+sorted((ROOT/'data').glob('*.csv'))
audit={'status':'passed','missing_report_links':missing,'source_files':len(sources),
    'paper_texts':len(records),'pdf_files':0,'sample_counts':counts,'literature_page_checks':checks,
    'notes':['Theorem 1.6 in 2606.06419v2 has its heading disrupted by PDF text extraction; checked the numeral, text, and physical PDF page.'],
    'sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(ROOT/'data/artifact_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
print('PASS',len(checks),'theorem/page checks;',counts,';',len(links),'links')
