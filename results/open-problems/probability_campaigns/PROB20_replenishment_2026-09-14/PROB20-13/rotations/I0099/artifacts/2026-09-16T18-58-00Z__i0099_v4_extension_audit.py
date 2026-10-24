#!/usr/bin/env python3
from pathlib import Path
import re, sys, zlib, lzma, base64, hashlib

T = Path(sys.argv[1]) if len(sys.argv)>1 else Path('/mnt/data/2026-09-16T18-58-00Z__i0099_v4_extension_3061_3181.out')
LO, HI = 3061, 3181

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n%d==0:return False
        d+=2
    return True

def inv(x,p): return pow(x,p-2,p)

def qrset(p): return {x*x%p for x in range(1,p)}

hdr_re=re.compile(r'^I0099_V4_CERT p=(\d+) omega=(\d+) Hn=(\d+) s3reps=(\d+) witness=([0-9,]+) witness_nodes=(\d+)$')
si_re=re.compile(r'^si=(\d+) u=(\d+) K=(\d+) v4reps=(\d+) no_nodes=(\d+)$')
cert_re=re.compile(r'^CERTIFIED_V4_RANGE p=(\d+) omega=(\d+) s3=(\d+)\.\.(\d+) all_no_one_larger=1 obligations=(\d+) total_nodes=(\d+) seconds=([0-9.]+)$')

blob=T.read_text().splitlines()
if blob and blob[0] in ('I0099_V4_EXTENSION_ZLIB_BASE64_V1','I0099_V4_EXTENSION_XZ_BASE64_V1'):
    meta=dict(item.split('=',1) for item in blob[1].split() if '=' in item)
    enc=base64.b64decode(''.join(blob[2:]))
    raw=zlib.decompress(enc) if blob[0].endswith('ZLIB_BASE64_V1') else lzma.decompress(enc)
    assert hashlib.sha256(raw).hexdigest()==meta['raw_sha256']
    assert len(raw)==int(meta['raw_bytes'])
    lines=raw.decode().splitlines()
else:
    lines=blob
headers={}
records={}
ranges={}
curp=None
for line in lines:
    m=hdr_re.match(line)
    if m:
        p,omega,hn,reps=map(int,m.group(1,2,3,4)); W=tuple(map(int,m.group(5).split(',')))
        item=(omega,hn,reps,W)
        if p in headers: assert headers[p]==item
        else: headers[p]=item
        curp=p
        continue
    m=si_re.match(line)
    if m:
        assert curp is not None
        si,u,K,v4,nodes=map(int,m.groups())
        old=records.setdefault(curp,{}).get(si)
        item=(u,K,v4,nodes)
        assert old is None or old==item
        records[curp][si]=item
        continue
    m=cert_re.match(line)
    if m:
        p,omega,a,b,obl,nodes=m.group(1,2,3,4,5,6)
        p,omega,a,b,obl,nodes=map(int,(p,omega,a,b,obl,nodes))
        assert p==curp
        ranges.setdefault(p,[]).append((a,b,obl,nodes))

expected=[p for p in range(LO+1,HI+1) if p%4==1 and isprime(p)]
assert sorted(headers)==expected, (sorted(headers),expected)
print('EXPECTED_PRIMES=',expected)

for p in expected:
    omega,hn,nreps,W=headers[p]
    Q=qrset(p)
    H=[x for x in range(2,p) if x in Q and (x-1)%p in Q]
    assert len(H)==hn==(p-5)//4
    assert len(W)==omega and len(set(W))==omega and W[0:2]==(0,1)
    for i in range(omega):
        for j in range(i):
            assert (W[i]-W[j])%p in Q
    idx={x:i for i,x in enumerate(H)}
    def s(x): return (1-x)%p
    def t(x): return inv(x,p)
    # S3 vertex invariance. Adjacency preservation is proved symbolically in the report
    # by exact square-multiplier identities; the executed C++ search uses these maps only for orbit partitioning.
    for x in H:
        assert s(x) in idx and t(x) in idx
    seen=set(); sreps=[]
    for x in H:
        if x in seen: continue
        orb={x}; frontier=[x]
        while frontier:
            z=frontier.pop()
            for w in (s(z),t(z)):
                assert w in idx
                if w not in orb: orb.add(w);frontier.append(w)
        seen |= orb; sreps.append(min(orb))
    sreps.sort()
    # C++ discovers orbits in H order and stores minimum representative; H order is increasing, so reps sorted.
    assert len(sreps)==nreps
    assert set(records[p])==set(range(nreps)), (p,len(records[p]),nreps)
    total_v4=0
    for si,u in enumerate(sreps):
        ru,rK,rv4,nodes=records[p][si]
        assert ru==u and nodes>0
        K=[x for x in H if (x-u)%p in Q]
        assert len(K)==rK
        Kset=set(K)
        def a(x): return u*inv(x,p)%p
        def b(x): return (x-u)%p*inv((x-1)%p,p)%p
        def c(x): return u*((x-1)%p)*inv((x-u)%p,p)%p
        for x in K:
            for f in (a,b,c): assert f(x) in Kset
        # V4 relations are checked exactly on every localized vertex. Adjacency preservation
        # is proved by exact determinant/square-multiplier identities in the report, and the C++
        # executable also checks it before accepting each S3 anchor.
        for x in K:
            assert a(a(x))==x and b(b(x))==x and c(c(x))==x
            assert a(b(x))==c(x) and b(a(x))==c(x)
        vseen=set(); cnt=0
        for x in K:
            if x in vseen: continue
            orb={x,a(x),b(x),c(x)}
            assert orb <= Kset
            vseen |= orb; cnt+=1
        assert cnt==rv4, (p,si,u,cnt,rv4)
        total_v4 += cnt
    # Certified ranges must form a disjoint partition 0..nreps, and obligation count is sum v4reps in each range.
    rr=sorted({(a,b,obl,nodes) for a,b,obl,nodes in ranges[p] if a<b})
    pos=0
    for a0,b0,obl,nodes in rr:
        assert a0==pos and b0<=nreps and nodes>0
        calc=sum(records[p][si][2] for si in range(a0,b0))
        assert calc==obl,(p,a0,b0,calc,obl)
        pos=b0
    assert pos==nreps
    print(f'p={p} omega={omega} Hn={hn} s3reps={nreps} v4_obligations={total_v4} witness=PASS S3=PASS V4=PASS ranges=PASS')

print(f'COVERAGE_ALL_ADMISSIBLE_PRIMES_{LO+1}_{HI}=PASS')
print('ALL_WITNESSES_EXACT_QR=PASS')
print('ALL_S3_VERTEX_ORBITS_EXACT=PASS')
print('ALL_V4_VERTEX_MAPS_RELATIONS_AND_ORBITS_EXACT=PASS')
print('ALL_ORBIT_COUNTS_AND_RANGE_PARTITIONS=PASS')
print('NOTE=This structural audit does not independently re-enumerate every branch-and-bound proof tree; upper-bound evidence is the archived deterministic exhaustive C++ search plus its completed per-obligation transcript.')
print('I0099_V4_EXTENSION_AUDIT_PASS')
