#!/usr/bin/env python3
import re, sys, math, base64, gzip, hashlib
from pathlib import Path

LO=3181
HI=3389
payload=Path(sys.argv[1]).read_text(encoding='utf-8')
if payload.startswith('I0099_EXECUTED_TRANSCRIPT_ENCODING=gzip+base64'):
    msha=re.search(r'^RAW_SHA256=([0-9a-f]{64})$',payload,re.M)
    m=re.search(r'BEGIN_GZIP_BASE64\n(.*?)\nEND_GZIP_BASE64',payload,re.S)
    assert msha and m
    raw=gzip.decompress(base64.b64decode(m.group(1)))
    assert hashlib.sha256(raw).hexdigest()==msha.group(1)
    text=raw.decode('utf-8')
else:
    text=payload

def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def inv(a,p): return pow(a,p-2,p)

def qrset(p): return {x*x%p for x in range(1,p)}

sections={}
for m in re.finditer(r'^### PRIME p=(\d+) omega=(\d+)\n(.*?)(?=^### PRIME|\Z)',text,re.M|re.S):
    p=int(m.group(1)); w=int(m.group(2)); sections[p]=(w,m.group(3))
expected=[p for p in range(LO+1,HI+1) if p%4==1 and isprime(p)]
assert sorted(sections)==expected,(sorted(sections),expected)

for p in expected:
    omega,body=sections[p]
    QR=qrset(p)
    wm=re.search(rf'^WITNESS p={p} omega={omega} vertices=([0-9,]+)$',body,re.M)
    assert wm
    W=list(map(int,wm.group(1).split(',')))
    assert len(W)==omega and W[:2]==[0,1] and len(set(W))==omega
    for i in range(omega):
        for j in range(i):
            assert (W[i]-W[j])%p in QR

    H=[x for x in range(2,p) if x in QR and (x-1)%p in QR]
    assert len(H)==(p-5)//4
    idx={x:i for i,x in enumerate(H)}
    oid=[-1]*len(H); reps=[]
    for i in range(len(H)):
        if oid[i]>=0: continue
        q=[i]; oid[i]=len(reps); mem=[]
        for v in q:
            mem.append(v)
            x=H[v]
            ys=((1-x)%p,inv(x,p))
            for y in ys:
                assert y in idx
                z=idx[y]
                if oid[z]<0:
                    oid[z]=oid[i]; q.append(z)
                else:
                    assert oid[z]==oid[i]
        reps.append(min(mem,key=lambda z:H[z]))

    headers=re.findall(rf'^I0099_V4_(?:CERT|NOWITNESS) p={p} omega={omega} Hn=(\d+) s3reps=(\d+)(?: .*)?$',body,re.M)
    assert headers
    assert all(int(hn)==len(H) and int(sr)==len(reps) for hn,sr in headers)

    recs={}
    for mm in re.finditer(r'^si=(\d+) u=(\d+) K=(\d+) v4reps=(\d+) no_nodes=(\d+)$',body,re.M):
        si,u,Ksz,v4,nodes=map(int,mm.groups())
        assert si not in recs
        recs[si]=(u,Ksz,v4,nodes)
    assert sorted(recs)==list(range(len(reps))), (p,len(recs),len(reps), sorted(set(range(len(reps)))-set(recs))[:10])

    # Independently rebuild every localized K_u and its V4 orbits.
    for si,ri in enumerate(reps):
        u=H[ri]
        K=[x for x in H if (x-u)%p in QR]
        u0,Ksz,v4reported,nodes=recs[si]
        assert u0==u and Ksz==len(K) and nodes>0
        Kset=set(K)
        seen=set(); norb=0
        for x in K:
            if x in seen: continue
            norb+=1
            stack=[x]; seen.add(x)
            while stack:
                z=stack.pop()
                a=u*inv(z,p)%p
                b=(z-u)%p*inv((z-1)%p,p)%p
                for y in (a,b):
                    assert y in Kset
                    if y not in seen:
                        seen.add(y); stack.append(y)
        assert norb==v4reported,(p,si,norb,v4reported)

    ranges=[]
    for mm in re.finditer(rf'^CERTIFIED_V4_RANGE p={p} omega={omega} s3=(\d+)\.\.(\d+) all_no_one_larger=1 obligations=(\d+) total_nodes=(\d+) seconds=([0-9.]+)$',body,re.M):
        a,b,obl,nodes=map(int,mm.group(1,2,3,4)); sec=float(mm.group(5))
        assert 0<=a<=b<=len(reps) and nodes>0 and sec>=0
        assert obl==sum(recs[i][2] for i in range(a,b))
        assert nodes==sum(recs[i][3] for i in range(a,b))
        ranges.append((a,b))
    ranges.sort()
    cursor=0
    for a,b in ranges:
        assert a==cursor,(p,cursor,a,b)
        cursor=b
    assert cursor==len(reps),(p,cursor,len(reps))
    print(f'p={p} omega={omega} Hn={len(H)} s3reps={len(reps)} ranges={len(ranges)} STRUCTURAL_PASS')

print(f'CONTIGUOUS_PRIME_COVERAGE_{LO+1}_{HI}=PASS count={len(expected)}')
print('ALL_WITNESSES_EXACT_QR_PASS')
print('ALL_S3_ORBIT_RECONSTRUCTIONS_PASS')
print('ALL_V4_LOCALIZATION_ORBIT_RECONSTRUCTIONS_PASS')
print('ALL_RANGE_PARTITIONS_AND_TOTALS_PASS')
print('I0099_EXTENSION_AUDIT_PASS')
