#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction


def dirs(d):
    out=[]
    for i in range(d):
        for s in (1,-1):
            v=[0]*d; v[i]=s; out.append(tuple(v))
    return out

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)

def states_F2(d):
    D=dirs(d); S=[]
    # state = (size, nonzero_tail_or_None, delta, Delta, type)
    # type 0=singleton, type 1=two-vertex cluster.
    for de in D:
        S.append((1,None,de,de,0))
    for f in D:
        for de in D:
            if de != f:  # tail 0; live iff head != f
                S.append((2,None,de,de,1))
        for de in D:
            if de != neg(f):  # tail f; live iff head != 0
                S.append((2,f,de,add(f,de),1))
    return S,D

def noncut(A,B):
    # Exact |cluster|<=2 specialization established in the prior R09 F2 certificate:
    # cut iff B has nonzero tail equal to -delta(A).
    return not (B[0]==2 and B[1] is not None and B[1]==neg(A[2]))

def matching_mass_int(weights, coord=0):
    # Maximum fractional matching on unit edges x--x+e_coord.
    # The graph is a disjoint union of paths. By bipartite LP duality this equals
    # the minimum vertex-cover weight, computed exactly by path dynamic programming.
    groups=defaultdict(dict)
    for x,w in weights.items():
        if not w: continue
        key=x[:coord]+x[coord+1:]
        groups[key][x[coord]]=w
    total=0
    for line in groups.values():
        ks=sorted(line)
        j=0
        while j < len(ks):
            k=j
            while k+1 < len(ks) and ks[k+1]==ks[k]+1:
                k+=1
            comp=ks[j:k+1]
            if len(comp)>=2:
                dp_not=0
                dp_yes=line[comp[0]]
                for pos in comp[1:]:
                    dp_not,dp_yes=dp_yes,min(dp_not,dp_yes)+line[pos]
                total += min(dp_not,dp_yes)
            j=k+1
    return total

def build_F2_components(d,p):
    S,D=states_F2(d); m=2*d
    # u=(1-p)^m, v=p(1-p)^(2m-2); scale all two-middle weights by u^2.
    r=p*(1-p)**(m-2)  # v/u
    nr,dr=r.numerator,r.denominator
    pair_w=[dr*dr,nr*dr,nr*nr]  # common denominator dr^2
    total=defaultdict(int)
    row={t:defaultdict(int) for t in D}       # C nonzero tail t
    col={b:defaultdict(int) for b in D}       # D delta b
    inter={(t,b):defaultdict(int) for t in D for b in D}
    for C in S:
        t=C[1]
        for E in S:
            if not noncut(C,E):
                continue
            b=E[2]
            w=pair_w[C[4]+E[4]]
            x=add(C[3],E[3])
            total[x]+=w
            col[b][x]+=w
            if t is not None:
                row[t][x]+=w
                inter[(t,b)][x]+=w
    return S,D,r,total,row,col,inter

def endpoint_measure(comp,a,e=None):
    # A endpoint enters only via a=delta(A); B endpoint enters only via its nonzero tail e.
    S,D,r,total,row,col,inter=comp
    ta=neg(a)
    z=dict(total)
    for x,w in row[ta].items(): z[x]=z.get(x,0)-w
    if e is not None:
        be=neg(e)
        for x,w in col[be].items(): z[x]=z.get(x,0)-w
        for x,w in inter[(ta,be)].items(): z[x]=z.get(x,0)+w
    return {x:w for x,w in z.items() if w}

def conv(a,b):
    out=defaultdict(Fraction)
    for x,wx in a.items():
        for y,wy in b.items():
            out[add(x,y)] += wx*wy
    return dict(out)

def matching_mass_frac(weights,coord=0):
    groups=defaultdict(dict)
    for x,w in weights.items():
        if not w: continue
        key=x[:coord]+x[coord+1:]
        groups[key][x[coord]]=w
    total=Fraction(0)
    for line in groups.values():
        ks=sorted(line); j=0
        while j<len(ks):
            k=j
            while k+1<len(ks) and ks[k+1]==ks[k]+1: k+=1
            comp=ks[j:k+1]
            if len(comp)>=2:
                dp_not=Fraction(0); dp_yes=line[comp[0]]
                for pos in comp[1:]:
                    dp_not,dp_yes=dp_yes,min(dp_not,dp_yes)+line[pos]
                total += min(dp_not,dp_yes)
            j=k+1
    return total

def random_parity_mixture(d):
    D=dirs(d); q={x:Fraction(1,2*d) for x in D}
    q2=conv(q,q); q3=conv(q2,q)
    mu=defaultdict(Fraction)
    for x,w in q2.items(): mu[x]+=w/2
    for x,w in q3.items(): mu[x]+=w/2
    M=matching_mass_frac(dict(mu),0)
    formula=Fraction(18*d*d-27*d+13,8*d**3)
    assert M==formula
    return M

def main():
    print('R09 exact F2 shift-matching and parity-randomization certificate')
    for d in (7,8,9,10):
        p=Fraction(1,4*d)
        comp=build_F2_components(d,p); D=comp[1]
        minima=None; args=[]; checked=0
        for ai,a in enumerate(D):
            for ei,e in [(-1,None)]+list(enumerate(D)):
                z=endpoint_measure(comp,a,None if e is None else e)
                s=sum(z.values())
                M=matching_mass_int(z,0)
                ratio=Fraction(M,s)
                checked += 1
                if minima is None or ratio < minima:
                    minima=ratio; args=[(ai,ei)]
                elif ratio==minima:
                    args.append((ai,ei))
        # Exact exhaustive extremizers: A direction and B nonzero tail align with +/-e1.
        assert args==[(0,0),(1,1)]
        mixed=random_parity_mixture(d)
        print(f'd={d} p={p} endpoint_classes={checked}')
        print(f'  min_F2_matching_fraction={minima}')
        print(f'  min_F2_matching_decimal={float(minima):.15f}')
        print(f'  extremizers={args}')
        print(f'  randomized_2_or_3_step_p0_matching={mixed}')
        print(f'  randomized_2_or_3_step_p0_decimal={float(mixed):.15f}')
    # Fixed two-step p=0 obstruction: sum of two nearest-neighbor steps has even checkerboard parity,
    # so every unit-shift edge joins support to zero mass and the matching is exactly zero.
    for d in (7,8,9,10):
        D=dirs(d); q={x:Fraction(1,2*d) for x in D}; q2=conv(q,q)
        assert matching_mass_frac(q2,0)==0
    print('fixed_two_step_p0_matching=0 in d=7,8,9,10')
    print('ALL_EXACT_CHECKS_PASS')

if __name__=='__main__':
    main()
