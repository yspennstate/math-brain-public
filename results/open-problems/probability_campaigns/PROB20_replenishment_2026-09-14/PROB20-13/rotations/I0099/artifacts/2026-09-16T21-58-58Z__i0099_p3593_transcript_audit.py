#!/usr/bin/env python3
from pathlib import Path
import re, sys
p=3593
omega=16
root=Path(sys.argv[1])
files=sorted(root.glob('chunk_*.out'), key=lambda f:int(f.stem.split('_')[1]))
assert len(files)==6, len(files)
header_re=re.compile(r'I0099_V4_WITNESS p=(\d+) omega=(\d+) Hn=(\d+) witness=([0-9,]+) witness_nodes=(\d+)')
cert_re=re.compile(r'CERTIFIED_V4_RANGE p=(\d+) omega=(\d+) s3=(\d+)\.\.(\d+) all_no_one_larger=1 obligations=(\d+) total_nodes=(\d+) proof64=([0-9a-f]+) seconds=([0-9.]+)')
ranges=[]; witnesses=[]; total_nodes=0; total_oblig=0
for f in files:
    txt=f.read_text()
    hm=header_re.search(txt); cm=cert_re.search(txt)
    assert hm and cm, f
    assert int(hm.group(1))==p and int(hm.group(2))==omega and int(hm.group(3))==(p-5)//4
    W=list(map(int,hm.group(4).split(',')))
    assert len(W)==omega and W[:2]==[0,1]
    witnesses.append(W)
    assert int(cm.group(1))==p and int(cm.group(2))==omega
    a,b=int(cm.group(3)),int(cm.group(4)); ranges.append((a,b))
    total_oblig += int(cm.group(5)); total_nodes += int(cm.group(6)); int(cm.group(7),16)
assert all(W==witnesses[0] for W in witnesses)
W=witnesses[0]
def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True
assert isprime(p) and p%4==1
qr={x*x%p for x in range(1,p)}
for i in range(len(W)):
    for j in range(i):
        assert (W[i]-W[j])%p in qr
H=[x for x in range(2,p) if x in qr and (x-1)%p in qr]
assert len(H)==(p-5)//4
Hset=set(H)
def inv(x): return pow(x,p-2,p)
seen=set(); reps=[]
for x in H:
    if x in seen: continue
    orbit=set(); stack=[x]
    while stack:
        y=stack.pop()
        if y in orbit: continue
        assert y in Hset
        orbit.add(y)
        stack.append((1-y)%p)
        stack.append(inv(y))
    seen |= orbit; reps.append(min(orbit))
assert len(reps)==150
ranges=sorted(ranges)
assert ranges==[(0,25),(25,50),(50,75),(75,100),(100,125),(125,150)], ranges
print(f'p={p} omega={omega} Hn={len(H)} s3reps={len(reps)}')
print('WITNESS=' + ','.join(map(str,W)))
print('WITNESS_PAIRWISE_QR=PASS')
print('S3_ORBIT_REBUILD=PASS')
print('RANGE_PARTITION_0_150=PASS')
print(f'TOTAL_V4_OBLIGATIONS={total_oblig}')
print(f'TOTAL_DECISION_NODES={total_nodes}')
print('ALL_CHUNK_CERT_LINES=PASS')
print('I0099_P3593_TRANSCRIPT_AUDIT_PASS')
