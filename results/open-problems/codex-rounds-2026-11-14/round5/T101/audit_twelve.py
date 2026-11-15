#!/usr/bin/env python3
"""Independent cell-row classification, unit walks, signed series, and tails."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
import json
from math import comb, prod
import os
from pathlib import Path
import resource
import signal
import time

H=(3,129,1928,10326,28484,45522,43964,25510,8121,1093)
A=(1,36,454,1964,4246,5068,3378,1196,165)


def segment_key(corners):
    return tuple(sorted(tuple(sorted((a,b))) for a,b in
                        zip(corners,corners[1:]+corners[:1])))


def cycle_of_rows(rows,width):
    edges=set()
    for y,row in enumerate(rows):
        for x in range(width):
            if not row & (1<<x): continue
            v=((x,y),(x+1,y),(x+1,y+1),(x,y+1))
            for i in range(4):
                e=tuple(sorted((v[i],v[(i+1)%4])))
                if e in edges: edges.remove(e)
                else: edges.add(e)
    adj=defaultdict(list)
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    assert all(len(v)==2 for v in adj.values())
    start=min(adj)
    path=[start]
    prev,cur=start,adj[start][0]
    while cur!=start:
        path.append(cur)
        following=adj[cur][0] if adj[cur][0]!=prev else adj[cur][1]
        prev,cur=cur,following
    if len(path)!=len(adj): return None
    corners=tuple(v for i,v in enumerate(path)
                  if path[i-1][0]!=path[(i+1)%len(path)][0]
                  and path[i-1][1]!=path[(i+1)%len(path)][1])
    return corners


def cells(k):
    side=k//2-1
    found={}
    nodes=0
    candidates=0
    rejected=0
    for width in range(1,side+1):
        trans={}
        for a,b in product(range(1<<width),repeat=2):
            xs=0
            bad=False
            for x in range(width+1):
                # SW, SE, NW, NE: bits 0,1,2,3.
                t=((a>>(x-1))&1 if x else 0) | (((a>>x)&1)<<1)
                t|=(((b>>(x-1))&1 if x else 0)<<2) | (((b>>x)&1)<<3)
                if t in (6,9): bad=True
                if t.bit_count() in (1,3): xs|=1<<x
            if not bad and xs: trans[a,b]=xs.bit_count(),xs
        nexts={a:[(b,*trans[a,b]) for b in range(1,1<<width)
                  if (a,b) in trans] for a in range(1<<width)}

        def visit(rows,total,xmask):
            nonlocal nodes,candidates,rejected
            nodes+=1
            last=rows[-1]
            top,tx=trans[last,0]
            if total+top==k and xmask|tx==(1<<(width+1))-1:
                candidates+=1
                corners=cycle_of_rows(rows,width)
                if corners is None:
                    rejected+=1
                else:
                    assert len(corners)==k
                    assert {x for x,y in corners}==set(range(width+1))
                    assert {y for x,y in corners}==set(range(len(rows)+1))
                    # Crossing weights directly from cell occupancy differences.
                    rowpairs=zip((0,)+rows,rows+(0,))
                    diffs=tuple(a^b for a,b in rowpairs)
                    h=tuple(sum((d>>x)&1 for d in diffs)//2 for x in range(width))
                    v=tuple((row^(row<<1)).bit_count()//2 for row in rows)
                    key=segment_key(corners)
                    assert key not in found
                    found[key]=(h,v,rows)
            if len(rows)==side: return
            for b,turns,xs in nexts[last]:
                if total+turns<=k-2:
                    visit(rows+(b,),total+turns,xmask|xs)

        for b,turns,xs in nexts[0]:
            if turns<=k-2: visit((b,),turns,xs)
    return found,dict(prefixes=nodes,local_candidates=candidates,
                      disconnected_boundaries=rejected,count=len(found))


def walks(limit):
    visited={(0,0),(1,0)}
    counts=Counter()
    nodes=0
    def visit(x,y,dx,dy,length,turns):
        nonlocal nodes
        nodes+=1
        for u,v in ((dx,dy),(-dy,dx),(dy,-dx)):
            t=turns+((dx,dy)!=(u,v))
            if t>12: continue
            w=x+u,y+v
            if w==(0,0):
                k=t+((u,v)!=(1,0))
                if length+1>=4 and k<=12: counts[length+1,k]+=1
            elif w not in visited and length+1+abs(w[0])+abs(w[1])<=limit:
                visited.add(w)
                visit(*w,u,v,length+1,t)
                visited.remove(w)
    visit(1,0,1,0,1,0)
    return counts,nodes


def coefficient(m):
    return 2*sum(h*sum((-1)**j*comb(j+4,4)*comb(m-6-i-j+10,10)
                       for j in range(m-6-i+1))
                 for i,h in enumerate(H) if m>=6+i)


def polynomial(a,r):
    return sum(c*r**i for i,c in enumerate(a))


def audit_polynomial_identity(found):
    # Independent coefficient expansion of the common-denominator identity.
    def multiply(a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j]+=x*y
        return c
    def factor(a,n):
        c=[1]
        for _ in range(n): c=multiply(c,a)
        return c
    groups=Counter(tuple((h+v).count(c) for c in (1,2,3)) for h,v,rows in found.values())
    num=[0]*18
    for (a,b,c),count in groups.items():
        term=multiply(multiply(factor([1,-1],10-a-b-c),factor([1,1],5-b)),factor([1,1,1],1-c))
        for i,x in enumerate(term): num[a+2*b+3*c+i]+=count*x
    expected=[0]*6+multiply(multiply([1,1],[1,1,1]),list(A))
    assert num==expected
    # Derivative numerator, in a separate direct polynomial expansion.
    sixAplus=[(6+i)*a for i,a in enumerate(A)]
    first=multiply(sixAplus,[1,0,-1])
    second=[0]+multiply(list(A),[6,14])
    dg=[x+y for x,y in zip(first,second)]
    assert dg==[2*h for h in H]+[0]
    print('PASS exact common-denominator and derivative polynomial identities',flush=True)
    return num


def closed(p):
    q=1-p
    return p*polynomial(H,q*q)/(2048*(2-p)**11*(1+q*q)**5)


def baseline(p):
    q=1-p
    d=2-p
    return (p/(8*d**3)+p*q*q/(4*d**5)+p*q*q*(10+23*q*q)/(64*d**7)
            +p*q*q*polynomial((12,110,312,405,247,58),q*q)/(128*d**9*(1+q*q)**3))


def audit_probabilities(found):
    groups=Counter(tuple(sorted(h+v)) for h,v,rows in found.values())
    cutoff=500
    ns=[coefficient(m) for m in range(6,cutoff+1)]
    checks=[]
    for p in (Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(1)):
        q=1-p
        r=q*q
        exact=closed(p)
        if q:
            f=Q(0)
            total=Q(0)
            for g,count in groups.items():
                term=count*prod(r**c/(1-r**c) for c in g)
                f+=term
                total+=term*sum(Q(c)/(1-r**c) for c in g)
            assert f==r**6*polynomial(A,r)/((1-r)**10*(1+r)**4)
            assert total*(p/2)**12*q**(-12)==exact
        partial=sum(n*(p/2)**12*q**(2*m-12) for m,n in enumerate(ns,6))
        # j<=10 gaps inject into positive j-part compositions.
        # For m>=20 all these are bounded by C(m-1,9).
        first=len(found)*(cutoff+1)*comb(cutoff,9)*(p/2)**12*q**(2*(cutoff+1)-12)
        rho=r*Q(cutoff+2,cutoff-8)
        assert rho<1
        tail=first/(1-rho)
        assert 0<=exact-partial<=tail<Q(1,10**30)
        checks.append(dict(p=str(p),R12=str(exact),B12=str(baseline(p)+exact),
                           tail_bound_exact=str(tail)))
    leading_F=sum(Q(count,prod(g)) for g,count in groups.items() if len(g)==10)
    leading=leading_F*Q(10,2**23)
    assert leading_F==Q(sum(A),16)==Q(4127,4)
    assert leading==Q(sum(H),2048*2**11*2**5)==Q(20635,16777216)
    assert Q(1943,65536)+leading==Q(518043,16777216)
    assert closed(Q(1))==Q(6,2**12)==Q(3,2048)
    assert baseline(Q(1))+closed(Q(1))==Q(259,2048)
    return checks,leading,leading_F


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(180,180))
    signal.alarm(900)
    assert os.environ.get('OMP_NUM_THREADS')=='1' and os.getpriority(os.PRIO_PROCESS,0)>=15
    start=time.monotonic()
    data=json.loads(Path('twelve_data.json').read_text())
    found,stats=cells(12)
    expected={segment_key(tuple(map(tuple,s['corners']))):(tuple(s['horizontal']),tuple(s['vertical']))
              for s in data['shapes']}
    assert {s:v[:2] for s,v in found.items()}==expected
    assert len(found)==9901
    print('PASS independent cell-row enumeration; every boundary and strip weight:',stats,flush=True)
    common_num=audit_polynomial_identity(found)
    counts,nodes=walks(20)
    old=json.loads(Path('ten_recheck.json').read_text())
    for length in range(4,21,2):
        m=length//2
        assert counts[length,4]==m*(m-1)
        assert counts[length,6]==(16*comb(m,4) if m>=4 else 0)
        assert counts[length,8]==((40*comb(m+1,6) if m>=5 else 0)+(92*comb(m,6) if m>=6 else 0))
        assert counts[length,10]==old['root_counts'][str(length)]
        assert counts[length,12]==data['root_counts'][str(length)]==coefficient(m)
    for m in range(41): assert coefficient(m)==data['root_counts'][str(2*m)]
    print('PASS independent unit walks through perimeter 20; nodes='+str(nodes),flush=True)
    print('PASS signed-binomial and positive gap counts through perimeter 80',flush=True)
    checks,leading,leading_F=audit_probabilities(found)
    print('PASS exact probabilities, endpoint, two small-p derivations, and tails <1e-30',flush=True)
    for c in checks: print({k:v for k,v in c.items() if k!='tail_bound_exact'},flush=True)
    result=dict(cell_stats=stats,walk_nodes=nodes,
                walk_counts=[dict(length=l,k=k,count=n) for (l,k),n in sorted(counts.items())],
                checks=checks,F_leading_coefficient=str(leading_F),
                R12_linear_coefficient=str(leading),B12_linear_coefficient='518043/16777216',
                endpoint_R12='3/2048',endpoint_B12='259/2048',
                coefficient_check_through_perimeter=80,
                F_common_denominator_numerator=common_num,
                rows=[dict(segments=s,horizontal=h,vertical=v,rows=rows)
                      for s,(h,v,rows) in sorted(found.items())],
                elapsed_seconds=time.monotonic()-start,
                peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                priority=os.getpriority(os.PRIO_PROCESS,0))
    assert result['peak_rss_bytes']<1_000_000_000
    Path('twelve_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print({k:result[k] for k in ('elapsed_seconds','peak_rss_bytes','priority')},flush=True)


if __name__=='__main__': main()
