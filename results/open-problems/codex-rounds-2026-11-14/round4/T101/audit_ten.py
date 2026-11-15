#!/usr/bin/env python3
"""Independent segment-intersection classification and rooted walk audit."""
import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
from math import comb, prod
import os
from pathlib import Path
import resource
import time


def canonical_edges(corners):
    return tuple(sorted(tuple(sorted((v,w))) for v,w in
                        zip(corners,corners[1:]+corners[:1])))


def segments_meet(a,b,c,d):
    if a[1]==b[1] and c[1]==d[1]:
        return a[1]==c[1] and max(min(a[0],b[0]),min(c[0],d[0])) <= min(max(a[0],b[0]),max(c[0],d[0]))
    if a[0]==b[0] and c[0]==d[0]:
        return a[0]==c[0] and max(min(a[1],b[1]),min(c[1],d[1])) <= min(max(a[1],b[1]),max(c[1],d[1]))
    if a[0]==b[0]:
        a,b,c,d=c,d,a,b
    return min(a[0],b[0])<=c[0]<=max(a[0],b[0]) and min(c[1],d[1])<=a[1]<=max(c[1],d[1])


def coordinates(k):
    n=k//2
    sequences=[]
    sequence_counts={}
    for a in range(2,n+1):
        seq=[s for s in product(range(a),repeat=n) if set(s)==set(range(a))
             and all(s[i]!=s[(i+1)%n] for i in range(n))]
        sequences.extend(seq)
        sequence_counts[a]=len(seq)
    found=set()
    reps=0
    for xs,ys in product(sequences,repeat=2):
        v=tuple(z for i in range(n) for z in ((xs[i],ys[i]),(xs[(i+1)%n],ys[i])))
        pairs=list(zip(v,v[1:]+v[:1]))
        if any(segments_meet(*pairs[i],*pairs[j]) for i in range(k)
               for j in range(i+1,k) if j!=i+1 and (i,j)!=(0,k-1)):
            continue
        reps+=1
        found.add(canonical_edges(v))
    assert reps==k*len(found)
    return found,dict(sequence_counts=sequence_counts,candidates=len(sequences)**2,
                      representations=reps,count=len(found))


def walks(limit):
    path=[(0,0),(1,0)]
    seen=set(path)
    counts=Counter()
    nodes=0
    def visit(dx,dy,turns):
        nonlocal nodes
        nodes+=1
        x,y=path[-1]
        for ux,uy in ((dx,dy),(-dy,dx),(dy,-dx)):
            t=turns+((dx,dy)!=(ux,uy))
            if t>10:
                continue
            w=(x+ux,y+uy)
            if w==(0,0):
                total=t+((ux,uy)!=(1,0))
                if len(path)>=4 and total<=10:
                    counts[len(path),total]+=1
            elif w not in seen and len(path)+abs(w[0])+abs(w[1])<=limit:
                seen.add(w)
                path.append(w)
                visit(ux,uy,t)
                path.pop()
                seen.remove(w)
    visit(1,0,0)
    return counts,nodes


def coefficient(m):
    # G10=8*r^6*H(r)/[(1-r)^9(1+r)^3]. This signed finite
    # convolution is independent of the positive gap dynamic program.
    h=(12,110,312,405,247,58)
    return 8*sum(c*sum((-1)**j*comb(j+2,2)*comb(m-6-i-j+8,8)
                       for j in range(m-6-i+1))
                 for i,c in enumerate(h) if m>=6+i)


def closed(p):
    q=1-p
    r=q*q
    h=12+110*r+312*r*r+405*r**3+247*r**4+58*r**5
    return p*q*q*h/(128*(2-p)**9*(1+r)**3)


def audit_probabilities(data):
    checks=[]
    cutoff=500
    for p in (Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(1)):
        q=1-p
        r=q*q
        value=closed(p)
        if q:
            # Total-semiperimeter derivative, rather than horizontal roots.
            gap_value=Q(0)
            for row in data['groups']:
                g=row['gaps']
                gap_value+=row['count']*prod(r**c/(1-r**c) for c in g)*sum(Q(c)/(1-r**c) for c in g)
            assert (p/2)**10*q**(-10)*gap_value==value
        partial=sum(coefficient(m)*(p/2)**10*q**(2*m-10) for m in range(6,cutoff+1))
        # With at most eight gaps, positive gap assignments of semiperimeter m
        # are bounded by C(m-1,7), for m>=16. Sending widths to c*width
        # injects them into positive j-part compositions. For j<=8 and
        # m>=16, C(m-1,j-1)<=C(m-1,7). Root multiplier is m.
        first=528*(cutoff+1)*comb(cutoff,7)*(p/2)**10*q**(2*(cutoff+1)-10)
        rho=r*Q(cutoff+2,cutoff-6)
        assert rho<1
        tail=first/(1-rho)
        assert 0<=value-partial<=tail<Q(1,10**30)
        baseline=p/(8*(2-p)**3)+p*q*q/(4*(2-p)**5)+p*q*q*(10+23*q*q)/(64*(2-p)**7)
        checks.append(dict(p=str(p),R10=str(value),B10=str(baseline+value),tail_bound_exact=str(tail)))
    leading=sum(Q(8*row['count'],2**19*prod(row['gaps'])) for row in data['groups'] if len(row['gaps'])==8)
    assert leading==Q(143,65536)==Q(12+110+312+405+247+58,128*2**9*8)
    assert Q(225,8192)+leading==Q(1943,65536)
    assert checks[2]['B10']=='497923/19683000'
    return checks


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-length',type=int,choices=(16,18,20),default=20)
    args=parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(180,180))
    assert os.environ.get('OMP_NUM_THREADS')=='1' and os.getpriority(os.PRIO_PROCESS,0)>=15
    start=time.monotonic()
    data=json.loads(Path('ten_data.json').read_text())
    found,stats=coordinates(10)
    expected={canonical_edges(tuple(map(tuple,s['corners']))) for s in data['shapes']}
    assert found==expected and len(found)==528
    print('PASS independent segment classification:',stats,flush=True)
    counts,nodes=walks(args.max_length)
    for length in range(4,args.max_length+1,2):
        m=length//2
        assert counts[length,4]==m*(m-1)
        assert counts[length,6]==(16*comb(m,4) if m>=4 else 0)
        expected8=(40*comb(m+1,6) if m>=5 else 0)+(92*comb(m,6) if m>=6 else 0)
        assert counts[length,8]==expected8
        assert counts[length,10]==data['root_counts'][str(length)]==coefficient(m)
    print(f'PASS independent rooted walks through {args.max_length}; nodes={nodes}',flush=True)
    for m in range(2,31):
        assert coefficient(m)==data['root_counts'][str(2*m)]
    checks=audit_probabilities(data)
    print('PASS exact probability and tail audits at five densities; tails <1e-30',flush=True)
    for c in checks:
        print({k:v for k,v in c.items() if k!='tail_bound_exact'},flush=True)
    result=dict(coordinate_audit=stats,walk_nodes=nodes,
                walk_counts=[dict(length=l,k=k,count=n) for (l,k),n in sorted(counts.items())],
                checks=checks,coefficient_check_through_perimeter=60,
                R10_linear_coefficient='143/65536',B10_linear_coefficient='1943/65536',
                elapsed_seconds=time.monotonic()-start,
                peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                priority=os.getpriority(os.PRIO_PROCESS,0))
    assert result['peak_rss_bytes']<1_000_000_000
    Path('ten_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print({k:result[k] for k in ('elapsed_seconds','peak_rss_bytes','priority')})


if __name__=='__main__':
    main()
