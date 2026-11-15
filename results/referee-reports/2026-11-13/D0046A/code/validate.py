#!/usr/bin/env python3
"""Validate deliverables and independently recompute CSV estimates with math.fsum."""
import csv,hashlib,json,math,pathlib
from collections import defaultdict
ROOT=pathlib.Path(__file__).resolve().parents[1]
meta=json.loads((ROOT/'data/edge_metadata.json').read_text())
assert meta['nice']>=10 and meta['peak_rss_mb']<4000
assert meta['threads_requested']<=4
expected={'hermitian_bm':{int(n):r for n,r in meta['dense_reps'].items()},
          'independent_tri_ou':{int(n):r for n,r in meta['tri_reps'].items()}}
groups=defaultdict(dict);count=0
with (ROOT/'data/edge_samples.csv').open() as f:
    for r in csv.DictReader(f):
        model=r['model'];n=int(r['n']);rank=int(r['eigenvalue_rank']);rep=int(r['rep']);s=float(r['s']);x=float(r['edge_value'])
        assert math.isfinite(x)
        key=(model,n,rank);point=(rep,s)
        assert point not in groups[key]
        groups[key][point]=x;count+=1
for key,d in groups.items():
    model,n,rank=key
    assert len(d)==4*expected[model][n]
    for rep in range(expected[model][n]):
        assert all((rep,s) in d for s in meta['lags_s'])
    other=groups[(model,n,3-rank)]
    assert all((x>=other[p] if rank==1 else x<=other[p]) for p,x in d.items())
assert len(groups)==24
max_corr_error=max_msd_error=0.
with (ROOT/'data/summary.csv').open() as f:
    summary=list(csv.DictReader(f))
for row in summary:
    key=(row['model'],int(row['n']),int(row['rank']));s=float(row['lag_s']);d=groups[key]
    m=int(row['reps']);x=[d[(r,0.)] for r in range(m)];y=[d[(r,s)] for r in range(m)]
    mx=math.fsum(x)/m;my=math.fsum(y)/m
    covariance=math.fsum((a-mx)*(b-my) for a,b in zip(x,y))
    varx=math.fsum((a-mx)**2 for a in x);vary=math.fsum((b-my)**2 for b in y)
    corr=covariance/math.sqrt(varx*vary)
    msd=math.fsum((a-b)**2 for a,b in zip(x,y))/m
    max_corr_error=max(max_corr_error,abs(corr-float(row['correlation'])))
    max_msd_error=max(max_msd_error,abs(msd-float(row['mean_squared_increment'])))
assert len(summary)==72
assert max_corr_error<1e-12 and max_msd_error<1e-12
source_count=0
for p in (ROOT/'sources').glob('*.metadata.txt'):
    d=json.loads(p.read_text());txt=p.with_name(p.name.replace('.metadata.txt','.txt')).read_bytes()
    assert hashlib.sha256(txt).hexdigest()==d['text_sha256']
    assert txt.count(b'\x0c')==d['pages']
    assert d['pdf_retained'] is False
    source_count+=1
assert source_count==28
for p in ROOT.rglob('*'):
    if not p.is_file():continue
    assert p.suffix.lower()!='.pdf',str(p)
    with p.open('rb') as f:assert not f.read(5).startswith(b'%PDF'),str(p)
report=(ROOT/'REPORT.md').read_text()
assert report.splitlines()[0]=='PARTIAL'
assert '> Are there operator limits of matrix-valued (say Hermitian) Brownian motion?' in report
assert not any(w in report for w in ['after execution','page locations verified','exact pages in source index'])
# Delimiter parity outside code blocks is a useful corruption check.
assert report.count('$')%2==0
assert report.count(chr(92)+'[')==report.count(chr(92)+']')
assert json.loads((ROOT/'data/math_audit.json').read_text())['all_passed']
import xml.etree.ElementTree as ET
ET.parse(ROOT/'data/edge_comparison.svg')
results=dict(all_passed=True,sample_rows=count,summary_rows=len(summary),source_texts=source_count,
             max_independent_correlation_error=max_corr_error,max_independent_msd_error=max_msd_error,
             peak_rss_mb=meta['peak_rss_mb'],nice=meta['nice'],threads_requested=meta['threads_requested'],
             no_pdf_files=True,source_hashes_verified=True,svg_xml_valid=True)
(ROOT/'data/validation.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
