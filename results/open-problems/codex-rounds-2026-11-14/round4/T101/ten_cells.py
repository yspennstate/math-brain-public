#!/usr/bin/env python3
"""Exhaust cell interiors; exact gap series and probability audits (stdlib)."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
import json
from math import prod
import os
from pathlib import Path
import resource
import time


def canon(corners):
    v = tuple(corners)
    return min(w[j:] + w[:j] for w in (v, v[::-1]) for j in range(len(v)))


def cell_shapes(side, corners_wanted):
    # Represent a unit edge by the sorted pair of its endpoints.
    all_edges = set()
    squares = []
    for y in range(side):
        for x in range(side):
            v = ((x,y), (x+1,y), (x+1,y+1), (x,y+1))
            e = {tuple(sorted((v[j],v[(j+1)%4]))) for j in range(4)}
            squares.append(e)
            all_edges.update(e)
    edge_list = sorted(all_edges)
    index = {e:i for i,e in enumerate(edge_list)}
    square_bits = [sum(1 << index[e] for e in sq) for sq in squares]
    boundary = 0
    old_gray = 0
    found = {}
    for number in range(1, 1 << (side*side)):
        gray = number ^ (number >> 1)
        changed = gray ^ old_gray
        boundary ^= square_bits[changed.bit_length()-1]
        old_gray = gray
        adjacent = defaultdict(list)
        bits = boundary
        while bits:
            low = bits & -bits
            v,w = edge_list[low.bit_length()-1]
            adjacent[v].append(w)
            adjacent[w].append(v)
            bits ^= low
        if any(len(a) != 2 for a in adjacent.values()):
            continue
        start = min(adjacent)
        cycle = [start]
        previous, current = start, adjacent[start][0]
        while current != start:
            cycle.append(current)
            a,b = adjacent[current]
            previous, current = current, (a if a != previous else b)
        if len(cycle) != len(adjacent):
            continue
        corners = []
        for i,v in enumerate(cycle):
            a,b = cycle[i-1],cycle[(i+1)%len(cycle)]
            if (v[0]-a[0],v[1]-a[1]) != (b[0]-v[0],b[1]-v[1]):
                corners.append(v)
        if len(corners) not in corners_wanted:
            continue
        ox = min(x for x,y in corners)
        oy = min(y for x,y in corners)
        corners = [(x-ox,y-oy) for x,y in corners]
        w,h = max(x for x,y in corners),max(y for x,y in corners)
        if {x for x,y in corners} != set(range(w+1)):
            continue
        if {y for x,y in corners} != set(range(h+1)):
            continue
        pairs = list(zip(corners,corners[1:]+corners[:1]))
        hg = tuple(sum(y==v and min(x,u)<=j<max(x,u)
                       for (x,y),(u,v) in pairs)//2 for j in range(w))
        vg = tuple(sum(x==u and min(y,v)<=j<max(y,v)
                       for (x,y),(u,v) in pairs)//2 for j in range(h))
        assert all(c in (1,2) for c in hg+vg)
        cells = {(i%side-ox,i//side-oy) for i in range(side*side)
                 if gray & (1<<i)}
        rows = [''.join('1' if (x,y) in cells else '0' for x in range(w))
                for y in range(h)]
        found[canon(corners)] = dict(k=len(corners),width=w,height=h,
                                   horizontal=hg,vertical=vg,rows=rows)
    return found


def mul(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def factor_power(sign,n):
    v = [1]
    for _ in range(n):
        v = mul(v,[1,sign])
    return v


def divide_factor(v, sign):
    """Divide by 1+sign*r if exact, else return None."""
    if len(v) <= 1:
        return None
    q = [v[0]]
    for i in range(1,len(v)-1):
        q.append(v[i]-sign*q[-1])
    return q if v[-1] == sign*q[-1] else None


def rational_series(groups, maxgaps):
    # t^a u^b = r^(a+2b)/[(1-r)^(a+b)(1+r)^b].
    pole_plus = max(g.count(2) for g in groups)
    numerator = [0]
    for g,count in groups.items():
        a,b = g.count(1),g.count(2)
        term = [0]*(a+2*b) + [count*x for x in mul(
            factor_power(-1,maxgaps-a-b),factor_power(1,pole_plus-b))]
        numerator += [0]*max(0,len(term)-len(numerator))
        for i,x in enumerate(term):
            numerator[i] += x
    while len(numerator)>1 and numerator[-1]==0:
        numerator.pop()
    powers = [maxgaps,pole_plus]
    for j,sign in enumerate((-1,1)):
        while powers[j]:
            q = divide_factor(numerator,sign)
            if q is None:
                break
            numerator = q
            powers[j] -= 1
    return numerator,powers


def ev(poly,r):
    out = Q(0)
    for c in reversed(poly):
        out = out*r+c
    return out


def audit(found,k,limit):
    shapes = {s:v for s,v in found.items() if v['k']==k}
    groups = Counter(tuple(sorted(v['horizontal']+v['vertical'])) for v in shapes.values())
    num,powers = rational_series(groups,k-2)
    def closed_g(r):
        a,b = powers
        f = ev(num,r)/(1-r)**a/(1+r)**b
        dn = [i*num[i] for i in range(1,len(num))]
        return r*(ev(dn,r)/(1-r)**a/(1+r)**b
                  + f*(Q(a)/(1-r)-Q(b)/(1+r)))
    unrooted = [0]*(limit+1)
    for g,count in groups.items():
        seq = [1]+[0]*limit
        for c in g:
            nxt = [0]*(limit+1)
            for m in range(c,limit+1):
                nxt[m] = seq[m-c] + nxt[m-c]
            seq = nxt
        for m,value in enumerate(seq):
            unrooted[m] += count*value
    checks=[]
    for p in (Q(1,10),Q(1,4),Q(1,2),Q(3,4)):
        q=1-p
        r=q*q
        direct = Q(0)
        for shape in shapes.values():
            h,v=shape['horizontal'],shape['vertical']
            term=prod(r**c/(1-r**c) for c in h+v)
            direct += term*sum(Q(2*c)/(1-r**c) for c in h)
        assert direct == closed_g(r)
        value = (p/2)**k*q**(-k)*direct
        if k==8:
            assert value == p*q*q*(10+23*q*q)/(64*(2-p)**7)
        checks.append(dict(p=str(p),probability=str(value)))
    leading=sum(Q(k-2,2**(2*k-1)*prod(g))*count
                for g,count in groups.items() if len(g)==k-2)
    if k==8:
        assert len(shapes)==38 and leading==Q(33,8192)
        assert num==[0,0,0,0,0,8,14] and powers==[6,0]
    return dict(k=k,count=len(shapes),groups=[dict(gaps=g,count=c) for g,c in sorted(groups.items())],
                F_numerator=num,F_denominator_powers=powers,
                root_counts={str(2*m):m*unrooted[m] for m in range(2,limit+1)},
                checks=checks,linear_coefficient=str(leading),
                shapes=[dict(v,corners=s) for s,v in sorted(shapes.items())])


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--stage',choices=('recheck','ten'),required=True)
    args=parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(180,180))
    assert os.environ.get('OMP_NUM_THREADS')=='1'
    assert os.getpriority(os.PRIO_PROCESS,0)>=15
    start=time.monotonic()
    side,k=(3,8) if args.stage=='recheck' else (4,10)
    found=cell_shapes(side,{k})
    data=audit(found,k,30)
    data.update(elapsed_seconds=time.monotonic()-start,
                peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                priority=os.getpriority(os.PRIO_PROCESS,0),cell_subsets=(1<<(side*side))-1)
    assert data['peak_rss_bytes'] < 1_000_000_000
    name='earlier_recheck.json' if k==8 else 'ten_data.json'
    Path(name).write_text(json.dumps(data,indent=2)+'\n')
    for key in ('count','groups','F_numerator','F_denominator_powers','checks','linear_coefficient',
                'elapsed_seconds','peak_rss_bytes','priority'):
        print(f'{key}={data[key]}')
    print('root_counts='+str({l:n for l,n in data['root_counts'].items() if int(l)<=20}))
    print('output='+name)


if __name__=='__main__':
    main()
