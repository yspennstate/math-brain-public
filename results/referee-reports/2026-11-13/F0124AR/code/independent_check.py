"""Independent exact audit. Standard library only; no submitted-code imports.

python3 code/independent_check.py
All fractions are exact. One process, bounded state count, inherited nice >=10.
"""
import csv
import itertools
import json
import math
import os
import resource
import time
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PEAK = 0


def likelihood(word, p):
    """Integrate a complete observed word over walk and scenery.

    State is (current index, tuple of spatial colours left-to-right).
    Each step adds denominator 2*b; revisits compensate with factor 2.
    Initial observation has probability 1/2.
    """
    global PEAK
    a, b = p.numerator, p.denominator
    states = {(0, (word[0],)): 1}
    for colour in word[1:]:
        nxt = defaultdict(int)
        for (pos, scenery), weight in states.items():
            for step, numerator in ((1, a), (-1, b-a)):
                if not numerator:
                    continue
                dest = pos + step
                if dest == -1:
                    key, scale = (0, (colour,) + scenery), numerator
                elif dest == len(scenery):
                    key, scale = (dest, scenery + (colour,)), numerator
                elif scenery[dest] == colour:
                    key, scale = (dest, scenery), 2 * numerator
                else:
                    continue
                nxt[key] += weight * scale
        states = nxt
        PEAK = max(PEAK, len(states))
        assert len(states) < 250_000, 'state cap exceeded'
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 2*1024**3, 'RSS cap exceeded'
    return F(sum(states.values()), 2 * (2*b)**(len(word)-1))


def conditional(exterior, p):
    m = (len(exterior)-1)//2
    values = []
    for colour in (0, 1):
        word = list(exterior)
        word[m] = colour
        values.append(likelihood(word, p))
    return values[1] / sum(values)


def positions(steps):
    s = [0]
    for x in steps:
        s.append(s[-1]+x)
    return s


def cuts(s):
    return tuple(k for k in range(len(s)-1)
                 if max(s[:k+1]) <= s[k] < min(s[k+1:]))


def brute(word, p):
    """Separate path enumeration with physical coordinates, allowing a hole."""
    total = F(0)
    for steps in itertools.product((-1, 1), repeat=len(word)-1):
        mapping = {}
        for site, colour in zip(positions(steps), word):
            if colour is None:
                continue
            if site in mapping and mapping[site] != colour:
                break
            mapping[site] = colour
        else:
            r = steps.count(1)
            total += p**r * (1-p)**(len(steps)-r) / 2**len(mapping)
    return total


def bilateral_origin(exterior, p):
    """Direct independent arms anchored at S_0=0, backward drift reversed."""
    m=(len(exterior)-1)//2
    numerator=denominator=F(0)
    for increments in itertools.product((-1,1), repeat=2*m):
        past, future=increments[:m],increments[m:]
        times={0:0}
        for k in range(1,m+1):
            times[-k]=-sum(past[:k])
            times[k]=sum(future[:k])
        mapping={}
        for t in range(-m,m+1):
            if t==0:
                continue
            site, colour=times[t], exterior[t+m]
            if site in mapping and mapping[site]!=colour:
                break
            mapping[site]=colour
        else:
            rights=increments.count(1)
            weight=p**rights*(1-p)**(2*m-rights)/2**len(mapping)
            denominator+=weight
            numerator+=weight*(mapping[0] if 0 in mapping else F(1,2))
    return numerator/denominator


def gas_likelihood(word, p):
    """Independent renewal sum of no-cut block activities, with endpoints."""
    N = len(word)
    activity = {}
    for u in range(N):
        for v in range(u, N):
            L = v-u
            val = F(0)
            for steps in itertools.product((-1, 1), repeat=L):
                s = positions(steps)
                if cuts(s) or (u > 0 and min(s) < 0) or (v < N-1 and max(s) > s[-1]):
                    continue
                mapping = {}
                for site, colour in zip(s, word[u:v+1]):
                    if colour is None:
                        continue
                    if site in mapping and mapping[site] != colour:
                        break
                    mapping[site] = colour
                else:
                    h = sum(x is not None for x in word[u:v+1])
                    val += ((1-p)/p)**steps.count(-1) * 2**(h-len(mapping))
            activity[u, v] = val
    z = [F(1)] + [F(0)]*N
    for end in range(1, N+1):
        z[end] = sum(z[start]*activity[start,end-1] for start in range(end))
    return z[N] * p**(N-1) / 2**sum(x is not None for x in word)


def geometry():
    count = blocks = 0
    for L in range(15):
        for steps in itertools.product((-1, 1), repeat=L):
            count += 1
            s = positions(steps)
            cs = cuts(s)
            crossings = defaultdict(list)
            for k, (x,y) in enumerate(zip(s,s[1:])):
                crossings[min(x,y)].append((k, y-x))
            assert set(cs) == {vs[0][0] for vs in crossings.values()
                               if len(vs)==1 and vs[0][1]==1}
            starts = (0,) + tuple(k+1 for k in cs)
            ends = cs + (L,)
            for u,v in zip(starts, ends):
                blocks += 1
                segment = s[u:v+1]
                ell = steps[u:v].count(-1)
                assert v-u <= 3*ell
                assert not cuts(segment)
                assert u==0 or segment[0]==min(segment)
                assert v==L or segment[-1]==max(segment)
                for hole in (None, *range(len(segment))):
                    observed = [x for i,x in enumerate(segment) if i!=hole]
                    assert len(observed)-len(set(observed)) <= 2*ell
    return dict(walks=count, blocks=blocks)


def swap_audit():
    """Check the pair involution including central-colour marks exactly."""
    m, n = 3, 2
    exteriors = ([1,1,1,None,1,1,1], [0,1,1,None,1,1,0])
    systems = []
    for exterior in exteriors:
        records = {}
        for colour in (0,1):
            word = list(exterior)
            word[m] = colour
            for steps in itertools.product((-1,1),repeat=2*m):
                s, mapping = positions(steps), {}
                for site,c in zip(s,word):
                    if site in mapping and mapping[site]!=c:
                        break
                    mapping[site]=c
                else:
                    records[(steps,colour)] = (steps.count(-1),len(mapping),cuts(s))
        systems.append(records)
    checked = 0
    for (x,U),(lx,rx,cx) in systems[0].items():
        for (y,V),(ly,ry,cy) in systems[1].items():
            common = set(cx)&set(cy)
            left = [k for k in common if m-n<=k<m]
            right = [k for k in common if m<=k<m+n]
            if not left or not right:
                continue
            a,b=max(left)+1,min(right)+1
            xx=x[:a]+y[a:b-1]+x[b-1:]
            yy=y[:a]+x[a:b-1]+y[b-1:]
            lxx,rxx,cxx=systems[0][xx,V]
            lyy,ryy,cyy=systems[1][yy,U]
            assert lx+ly==lxx+lyy and rx+ry==rxx+ryy
            assert set(cxx)&set(cyy)==common
            assert xx[:a]+yy[a:b-1]+xx[b-1:]==x
            checked += 1
    return checked


def exterior(m, n, pattern):
    def colour(t):
        if t==0:
            return None
        if abs(t)<=n or pattern=='black':
            return 1
        k=abs(t)-n-1
        if pattern=='white':
            return 0
        if pattern=='WWBB':
            return (0,0,1,1)[k%4]
        if pattern=='asymmetric':
            return int(t<0)
        raise ValueError(pattern)
    return [colour(t) for t in range(-m,m+1)]


def main():
    begin=time.monotonic()
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    # This sandbox rejects setrlimit; enforce state and RSS caps each step.
    summary={'geometry':geometry(), 'swap_pairs':swap_audit()}
    checks=0
    for p in (F(97,100),F(9,10),F(1,2)):
        for word in itertools.product((0,1), repeat=7):
            assert likelihood(word,p)==brute(word,p)
            checks+=1
        for small in itertools.product((0,1), repeat=6):
            word=list(small[:3]) + [None] + list(small[3:])
            assert gas_likelihood(word,p)==brute(word,p)
            checks+=1
    summary['exact_cross_checks']=checks
    arm_checks=0
    for p in (F(97,100),F(9,10)):
        for colours in itertools.product((0,1),repeat=6):
            eta=list(colours[:3])+[None]+list(colours[3:])
            assert conditional(eta,p)==bilateral_origin(eta,p)
            assert conditional(eta,p)+conditional([None if c is None else 1-c for c in eta],p)==1
            assert conditional(eta,p)==conditional(eta,1-p)
            arm_checks+=1
    summary['bilateral_arm_checks']=arm_checks
    for L in range(1,101):
        for t in (F(12,97),F(4,27)):
            tail=sum(F(math.comb(L,k))*t**k for k in range((L+2)//3,L+1))
            assert tail**3 <= (27*t/4)**L
    summary['exact_chernoff_checks']=200
    rows=[]
    for p in (F(97,100),F(9,10)):
        for n in (2,4,6):
            for m in (n,n+4,n+12,n+24):
                base=conditional(exterior(m,n,'black'),p)
                for pattern in ('black','white','WWBB','asymmetric'):
                    g=base if pattern=='black' else conditional(exterior(m,n,pattern),p)
                    rows.append(dict(p=str(p),n=n,m=m,pattern=pattern,
                                     g=str(g),decimal=f'{float(g):.12f}',
                                     gap=str(abs(g-base)),gap_decimal=f'{float(abs(g-base)):.12f}'))
                print('computed',p,n,m,flush=True)
    with (ROOT/'data/finite_windows.csv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    bound=[]
    for p in (F(97,100),F(9,10)):
        rho=(27*float((1-p)/p))**(1/3)
        bound.append(dict(p=str(p),rho=rho,
                          log10_c=(-2*rho/(1-rho)**2)/math.log(10) if rho<1 else None))
    summary.update(rows=len(rows),peak_states=PEAK,elapsed_seconds=time.monotonic()-begin,
                   maxrss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                   nice=os.getpriority(os.PRIO_PROCESS,0),bounds=bound)
    (ROOT/'data/check_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
