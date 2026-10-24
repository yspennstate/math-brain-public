#!/usr/bin/env python3
import re,sys
from pathlib import Path
p=3617; omega=17
text=Path(sys.argv[1]).read_text().splitlines()
Q={x*x%p for x in range(1,p)}
assert len(Q)==(p-1)//2
headers=[]; rows=[]; sums=[]
rh=re.compile(r'^I0099_V4_CERT p=(\d+) omega=(\d+) Hn=(\d+) s3reps=(\d+) witness=([0-9,]+) witness_nodes=(\d+)$')
rr=re.compile(r'^si=(\d+) u=(\d+) K=(\d+) v4reps=(\d+) no_nodes=(\d+)$')
rs=re.compile(r'^CERTIFIED_V4_RANGE p=(\d+) omega=(\d+) s3=(\d+)\.\.(\d+) all_no_one_larger=1 obligations=(\d+) total_nodes=(\d+) seconds=([0-9.]+)$')
for line in text:
    if m:=rh.match(line):headers.append(m.groups())
    elif m:=rr.match(line):rows.append(tuple(map(int,m.groups())))
    elif m:=rs.match(line):sums.append(m.groups())
assert len(headers)==5 and len(sums)==5
for h in headers:
    hp,ho,hn,hs,w,wn=h
    assert (int(hp),int(ho),int(hn),int(hs))==(p,omega,(p-5)//4,151)
    W=list(map(int,w.split(',')))
    assert len(W)==omega and len(set(W))==omega
    for i in range(omega):
        for j in range(i): assert (W[i]-W[j])%p in Q
assert len({h[4] for h in headers})==1
witness=headers[0][4]
vals=[x for x in range(2,p) if x in Q and (x-1)%p in Q]
assert len(vals)==903
idx={x:i for i,x in enumerate(vals)}
def inv(x):return pow(x,p-2,p)
def S(x):return (1-x)%p
def T(x):return inv(x)
unseen=set(vals); reps=[]; orbits=[]
while unseen:
    seed=min(unseen); dq=[seed]; orb={seed}
    while dq:
        x=dq.pop()
        for y in (S(x),T(x)):
            assert y in idx
            if y not in orb:orb.add(y);dq.append(y)
    unseen-=orb; reps.append(min(orb));orbits.append(orb)
assert len(reps)==151 and reps==sorted(reps)
ranges=[]; agg_ob=agg_nodes=0
for s in sums:
    sp,so,a,b,ob,nodes,sec=s
    assert (int(sp),int(so))==(p,omega)
    ranges.append((int(a),int(b)));agg_ob+=int(ob);agg_nodes+=int(nodes)
assert ranges==[(0,30),(30,60),(60,90),(90,120),(120,151)]
assert agg_ob==17050 and agg_nodes==77800297
assert len(rows)==151 and [r[0] for r in rows]==list(range(151))
def isedge(x,y):return (x-y)%p in Q
calc_ob=0
for si,u,Kreported,v4reported,nodes in rows:
    assert u==reps[si]
    K=[x for x in vals if isedge(x,u)]
    assert len(K)==Kreported
    Kset=set(K)
    def A(x): return u*inv(x)%p
    def B(x): return (x-u)%p*inv((x-1)%p)%p
    unseen2=set(K); n_orb=0
    while unseen2:
        seed=min(unseen2); stack=[seed]; orb={seed}
        while stack:
            x=stack.pop()
            for y in (A(x),B(x)):
                assert y in Kset
                if y not in orb:orb.add(y);stack.append(y)
        unseen2-=orb;n_orb+=1
    assert n_orb==v4reported
    calc_ob+=n_orb
assert calc_ob==17050
assert (-1)%p in Q
for si,u,*_ in rows:
    assert u in Q and (u-1)%p in Q
def isprime(n):
    if n<2:return False
    d=2
    while d*d<=n:
        if n%d==0:return n==d
        d+=1
    return True
n=p+1
while not (n%4==1 and isprime(n)):n+=1
assert n==3637
print(f'P={p} HN={len(vals)} S3_ORBITS={len(reps)} V4_OBLIGATIONS={calc_ob}')
print(f'WITNESS={witness}')
print(f'RANGES={ranges}')
print(f'TOTAL_DECISION_NODES={agg_nodes}')
print('ALL_WITNESS_EDGES_QR=PASS')
print('S3_ORBIT_COVERAGE=PASS')
print('V4_ORBIT_COVERAGE_AND_SQUARE_MULTIPLIER_SYMMETRY=PASS')
print('ALL_RANGE_SUMMARIES_ONE_LARGER_EXCLUDED=PASS')
print('NEXT_ADMISSIBLE_PRIME=3637')
print('I0099_P3617_TRANSCRIPT_AUDIT_PASS')
