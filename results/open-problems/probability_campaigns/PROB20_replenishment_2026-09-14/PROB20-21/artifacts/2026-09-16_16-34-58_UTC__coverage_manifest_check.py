#!/usr/bin/env python3
from pathlib import Path
import re, hashlib

ROOT=Path('/mnt/data')
batchf=ROOT/'2026-09-16_16-34-58_UTC__n6_middle_batches_output.txt'
gridf=ROOT/'2026-09-16_16-34-58_UTC__n6_counterexample_grid_output.txt'
enumf=ROOT/'2026-09-16_16-34-58_UTC__s6_independent_enumerator_output.txt'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

lines=batchf.read_text().splitlines()
blocks=[]; cur=None
for line in lines:
    m=re.match(r'^=== BATCH (\d+) (\d+) ===$',line)
    if m:
        if cur: blocks.append(cur)
        cur={'a':int(m.group(1)),'b':int(m.group(2)),'lines':[]}
    elif cur:
        cur['lines'].append(line)
if cur: blocks.append(cur)

records={}
pat=re.compile(r'^middle=\[1/524288,69/140\] failed_candidates=(\d+) nodes=(\d+) leaves=(\d+) maxdepth=(\d+) min_interval_lower_nat=([^ ]+) mask=(\d+) a=([^ ]+) b=([^ ]+)$')
for bl in blocks:
    mm=[pat.match(x) for x in bl['lines']]
    mm=[x for x in mm if x]
    good=('RESULT=BATCH_PASS' in bl['lines'] and 'exit_status=0' in bl['lines'] and len(mm)==1)
    if not good: continue
    m=mm[0]
    records[(bl['a'],bl['b'])]={
        'failed':int(m.group(1)), 'nodes':int(m.group(2)), 'leaves':int(m.group(3)),
        'maxdepth':int(m.group(4)), 'minlower':float(m.group(5)), 'minlower_text':m.group(5),
        'mask':m.group(6), 'ia':m.group(7), 'ib':m.group(8)
    }

expected=[(a,a+50) for a in range(0,1000,50)] + [(a,a+20) for a in range(1000,1160,20)] + [(1160,1170)]
missing=[x for x in expected if x not in records]
assert not missing, missing
assert sum(b-a for a,b in expected)==1170
assert all(records[x]['failed']==0 for x in expected)
nodes=sum(records[x]['nodes'] for x in expected)
leaves=sum(records[x]['leaves'] for x in expected)
maxdepth=max(records[x]['maxdepth'] for x in expected)
worst=min(expected,key=lambda x:records[x]['minlower'])
w=records[worst]

G=gridf.read_text()
m=re.search(r'counterexample_grid=j/128,j=1\.\.63 points=(\d+) certified_negative=(\d+) inconclusive=(\d+) min_lower_gap_nat=([^ ]+) mask=(\d+) alpha=(\d+)/128',G)
assert m
points,neg,inc=int(m.group(1)),int(m.group(2)),int(m.group(3))
assert points==1170*63 and neg==0 and inc==0
E=enumf.read_text()
assert 'S6_INDEPENDENT_ENUMERATION=PASS' in E
assert 'candidate_count= 1173' in E
hm=re.search(r'sorted_mask_sha256=([0-9a-f]{64})',E); assert hm

print('PROB20-21 N=6 COVERAGE MANIFEST CHECK: PASS')
print('compressed_candidates=1173 nontrivial_candidates=1170')
print('frozen_sorted_mask_sha256='+hm.group(1))
print(f'counterexample_grid_points={points} certified_negative={neg} inconclusive={inc}')
print(f'middle_candidates=1170 missing_batches=0 failed_candidates=0 nodes={nodes} leaves={leaves} maxdepth={maxdepth}')
print(f'middle_min_outward_lower_D_nat={w["minlower_text"]} mask={w["mask"]} a={w["ia"]} b={w["ib"]} batch={worst[0]}:{worst[1]}')
print('batch_output_sha256='+sha(batchf))
print('grid_output_sha256='+sha(gridf))
print('independent_enum_output_sha256='+sha(enumf))
