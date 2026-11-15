#!/usr/bin/env python3
"""Rank polygons by disjoint half-open unit-vertex sets; exact gap algebra."""
import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
from math import comb, prod
import os
from pathlib import Path
import resource
import signal
import time

PREVIOUS = Path('~/codex_op_1114r4/briefs/T101')
FACTORS = ([1, -1], [1, 1], [1, 1, 1])


def guard():
    resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
    signal.alarm(900)
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15


def canon(v):
    i = v.index(min(v))
    a = v[i:] + v[:i]
    b = a[:1] + a[:0:-1]
    return min(a, b)


def classify(k):
    n = k // 2
    words = []
    stats = {}
    for a in range(2, n + 1):
        ss = [s for s in product(range(a), repeat=n)
              if len(set(s)) == a and all(s[i] != s[i-1] for i in range(n))]
        onto=sum((-1)**(a-j)*comb(a,j)*((j-1)**n+(-1)**n*(j-1))
                 for j in range(a+1))
        assert len(ss)==onto
        stats[a] = len(ss)
        words.extend(ss)
    horizontal, vertical = {}, {}
    for a, b, c in product(range(n), repeat=3):
        if a == b:
            continue
        ds = 1 if b > a else -1
        horizontal[a, b, c] = sum(1 << (x + n*c) for x in range(a, b, ds))
        vertical[a, b, c] = sum(1 << (c + n*y) for y in range(a, b, ds))
    # Precompute each word's successive coordinates and strip weights.
    records = []
    for s in words:
        pairs = tuple(zip(s, s[1:] + s[:1]))
        crossings = [sum(min(a,b) <= j < max(a,b) for a,b in pairs)
                     for j in range(max(s))]
        assert all(c > 0 and c % 2 == 0 for c in crossings)
        records.append((s, pairs, tuple(c//2 for c in crossings)))
    found = {}
    reps = 0
    for xs, xp, h in records:
        for ys, yp, v in records:
            seen = 0
            for i in range(n):
                a, b = xp[i]
                c, d = yp[i]
                mask = horizontal[a,b,c]
                if seen & mask:
                    break
                seen |= mask
                mask = vertical[c,d,b]
                if seen & mask:
                    break
                seen |= mask
            else:
                reps += 1
                corners = tuple(z for i in range(n) for z in
                                ((xs[i],ys[i]),(xs[(i+1)%n],ys[i])))
                key = canon(corners)
                if key in found:
                    assert found[key] == (h,v)
                found[key] = h,v
    assert reps == k*len(found)
    return found, dict(word_counts=stats,candidates=len(words)**2,
                      representations=reps,count=len(found))


def trim(p):
    while len(p)>1 and not p[-1]:
        p.pop()
    return p


def add(a,b):
    out = [0]*max(len(a),len(b))
    for i,x in enumerate(a): out[i] += x
    for i,x in enumerate(b): out[i] += x
    return trim(out)


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    return trim(out)


def power(a,n):
    out=[1]
    for _ in range(n): out=mul(out,a)
    return out


def divexact(a,b):
    if len(a)<len(b): return None
    # All factors have constant term 1. Low-degree long division.
    rem=a[:]
    out=[0]*(len(a)-len(b)+1)
    for i in range(len(out)):
        out[i]=rem[i]
        for j,x in enumerate(b): rem[i+j] -= out[i]*x
    return trim(out) if not any(rem) else None


def reduce_fraction(num,poles):
    for i,f in enumerate(FACTORS):
        while poles[i]:
            q=divexact(num,f)
            if q is None: break
            num=q
            poles[i]-=1
    return num,poles


def fraction_from_groups(groups):
    poles=[max(sum(g) for g in groups),max(g[1] for g in groups),max(g[2] for g in groups)]
    num=[0]
    for (a,b,c),count in groups.items():
        t=[count]
        for f,e in zip(FACTORS,(poles[0]-a-b-c,poles[1]-b,poles[2]-c)):
            t=mul(t,power(f,e))
        num=add(num,[0]*(a+2*b+3*c)+t)
    return reduce_fraction(num,poles)


def derivative_fraction(num,poles):
    active=[int(e>0) for e in poles]
    extra=[1]
    for f,e in zip(FACTORS,active): extra=mul(extra,power(f,e))
    dn=[i*num[i] for i in range(1,len(num))] or [0]
    g=mul(dn,extra)
    for i,e in enumerate(poles):
        if not e: continue
        fi=FACTORS[i]
        di=[j*fi[j] for j in range(1,len(fi))]
        q=divexact(extra,fi)
        assert q is not None
        g=add(g,[-e*x for x in mul(mul(num,di),q)])
    return reduce_fraction([0]+g,[e+a for e,a in zip(poles,active)])


def ev(a,r):
    val=Q(0)
    for x in reversed(a): val=val*r+x
    return val


def value(num,poles,r):
    return ev(num,r)/prod(ev(f,r)**e for f,e in zip(FACTORS,poles))


def coefficients(groups,limit):
    out=[0]*(limit+1)
    for g,count in groups.items():
        seq=[1]+[0]*limit
        for weight,multiplicity in enumerate(g,1):
            for _ in range(multiplicity):
                nxt=[0]*(limit+1)
                for m in range(weight,limit+1):
                    nxt[m]=seq[m-weight]+nxt[m-weight]
                seq=nxt
        out=[a+count*b for a,b in zip(out,seq)]
    return out


def data_for(k,found,stats):
    groups=Counter(tuple((h+v).count(c) for c in (1,2,3)) for h,v in found.values())
    num,poles=fraction_from_groups(groups)
    gnum,gpoles=derivative_fraction(num,poles)
    coeff=coefficients(groups,40)
    checks=[]
    for p in (Q(1,10),Q(1,4),Q(1,2),Q(3,4)):
        q=1-p
        r=q*q
        total=Q(0)
        for h,v in found.values():
            total+=prod(r**c/(1-r**c) for c in h+v)*sum(Q(2*c)/(1-r**c) for c in h)
        assert total==value(gnum,gpoles,r)
        checks.append(dict(p=str(p),probability=str((p/2)**k*q**(-k)*total)))
    leading=sum(Q(count*(k-2),2**(2*k-1)*2**b*3**c)
                for (a,b,c),count in groups.items() if a+b+c==k-2)
    assert poles[0]==k-2 and gpoles[0]==k-1
    independent=Q(ev(gnum,Q(1)),2**k*2**(k-1)*2**gpoles[1]*3**gpoles[2])
    assert leading==independent
    return dict(k=k,stats=stats,groups=[dict(ones=a,twos=b,threes=c,count=count)
                    for (a,b,c),count in sorted(groups.items(),key=lambda t:(sum(t[0]),t[0][2],t[0][1]))],
                F_numerator=num,F_poles=poles,G_numerator=gnum,G_poles=gpoles,
                root_counts={str(2*m):m*v for m,v in enumerate(coeff)},
                checks=checks,linear_coefficient=str(leading),
                shapes=[dict(corners=s,horizontal=h,vertical=v) for s,(h,v) in sorted(found.items())])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--stage',choices=('recheck','twelve'),required=True)
    args=ap.parse_args()
    guard()
    start=time.monotonic()
    k=10 if args.stage=='recheck' else 12
    found,stats=classify(k)
    data=data_for(k,found,stats)
    if k==10:
        old=json.loads((PREVIOUS/'ten_data.json').read_text())
        oldshapes={canon(tuple(map(tuple,s['corners']))):(tuple(s['horizontal']),tuple(s['vertical'])) for s in old['shapes']}
        assert found==oldshapes
        assert data['F_numerator']==old['F_numerator']
        assert data['F_poles']==old['F_denominator_powers']+[0]
        assert data['checks']==old['checks']
        assert data['linear_coefficient']==old['linear_coefficient']=='143/65536'
        assert all(data['root_counts'][l]==v for l,v in old['root_counts'].items())
        print('PASS ten-corner result: every boundary, F10, probabilities, counts, linear coefficient',flush=True)
    data.update(elapsed_seconds=time.monotonic()-start,
                peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                priority=os.getpriority(os.PRIO_PROCESS,0))
    assert data['peak_rss_bytes']<1_000_000_000
    name='ten_recheck.json' if k==10 else 'twelve_data.json'
    Path(name).write_text(json.dumps(data,indent=2)+'\n')
    for key in ('stats','groups','F_numerator','F_poles','G_numerator','G_poles','checks',
                'linear_coefficient','elapsed_seconds','peak_rss_bytes','priority'):
        print(f'{key}={data[key]}',flush=True)
    print('root_counts='+str({l:n for l,n in data['root_counts'].items() if 12<=int(l)<=22}),flush=True)
    print('output='+name,flush=True)


if __name__=='__main__': main()
