#!/usr/bin/env python3
# Exact checker for R17 PROB10-02.  The update uses one genuine fresh Y bit
# across the whole active X window; no independent Bernoulli match array occurs.
from fractions import Fraction
from itertools import product

UV=((0,0),(0,1),(1,0),(1,1))
L_SOURCE=Fraction(99083249,125000000)


def transition(m,x,g,u,v):
    w=m//2
    c=[]
    cp=0
    for i in range(m):
        ci=0 if g[i] else max(cp,int(x[i]==v))
        c.append(ci)
        cp=ci
    gp=[]
    for i in range(m-1):
        gp.append(g[i+1]+c[i+1]-c[i])
    gp.append((1-c[-1])*int(u==v))
    xp=x[1:]+(u,)
    reward=g[w]+c[w]
    assert reward in (0,1)
    assert all(z in (0,1) for z in gp)
    return xp,tuple(gp),reward


def run(m,x,g,word):
    R=0
    for u,v in word:
        x,g,r=transition(m,x,g,u,v)
        R+=r
    return R


def extremal_gradients(m):
    w=m//2
    return (1,)*w+(0,)*w, (0,)*w+(1,)*w


def exhaustive_sandwich(m,N):
    gminus,gplus=extremal_gradients(m)
    cases=0
    maxgap=0
    for x in product((0,1),repeat=m):
        for g in product((0,1),repeat=m):
            for inds in product(range(4),repeat=N):
                word=tuple(UV[a] for a in inds)
                r=run(m,x,g,word)
                lo=run(m,x,gminus,word)
                hi=run(m,x,gplus,word)
                assert lo<=r<=hi
                assert hi-lo<=m//2
                maxgap=max(maxgap,hi-lo)
                cases+=1
    return cases,maxgap


def H0(g,w):
    m=2*w
    return sum(g[w:m-1],0)+Fraction(2,3)*g[m-1]


def h0_min_residual(m):
    w=m//2
    best=None
    for x in product((0,1),repeat=m):
        for g in product((0,1),repeat=m):
            h=H0(g,w)
            z=Fraction(0)
            for u,v in UV:
                xp,gp,r=transition(m,x,g,u,v)
                z+=Fraction(r+H0(gp,w)-h,4)
            if best is None or z<best:
                best=z
    return best


def pseudo_stationary_marginal_check(m):
    # For m>=4, a=(m-3)/(3(m-1)), b=2/(3(m-1)).  Conditional on B,
    # use g=1^m with mass a and each singleton e_j with mass b; x=B^m.
    assert m>=4 and m%2==0
    a=Fraction(m-3,3*(m-1))
    b=Fraction(2,3*(m-1))
    old=[{(xv,gv):Fraction(0) for xv in (0,1) for gv in (0,1)} for _ in range(m)]
    new=[{(xv,gv):Fraction(0) for xv in (0,1) for gv in (0,1)} for _ in range(m)]
    er=Fraction(0)
    total=Fraction(0)
    for B in (0,1):
        x=(B,)*m
        cases=[((1,)*m,a)]
        cases += [(tuple(1 if i==j else 0 for i in range(m)),b) for j in range(m)]
        for g,pg in cases:
            ps=Fraction(1,2)*pg
            total+=ps
            for i in range(m):
                old[i][(x[i],g[i])]+=ps
            for u,v in UV:
                p=ps*Fraction(1,4)
                xp,gp,r=transition(m,x,g,u,v)
                er+=p*r
                for i in range(m):
                    new[i][(xp[i],gp[i])]+=p
    assert total==1
    target={(0,0):Fraction(1,3),(0,1):Fraction(1,6),
            (1,0):Fraction(1,3),(1,1):Fraction(1,6)}
    for i in range(m):
        assert old[i]==target
        assert new[i]==target
    assert er==Fraction(2,3)
    return a,b,er


print('R17 PROB10-02 extremal-gradient / one-site obstruction exact checker')
for m,N in ((2,3),(4,3),(6,2)):
    cases,gap=exhaustive_sandwich(m,N)
    print(f'SANDWICH_EXHAUSTIVE m={m} N={N} cases={cases} max_gap={gap} bound_w={m//2} PASS')

# General sharp family: x=0^m, no future matches, word (u,v)=(0,1)^w.
for m in range(2,14,2):
    w=m//2
    gminus,gplus=extremal_gradients(m)
    x=(0,)*m
    word=((0,1),)*w
    lo=run(m,x,gminus,word)
    hi=run(m,x,gplus,word)
    assert lo==0 and hi==w
    print(f'SANDWICH_SHARP_FAMILY m={m} horizon={w} lower={lo} upper={hi} gap={hi-lo} PASS')

# Exact lower Bellman witness from the prior carry factorization.
for m in (4,6,8):
    z=h0_min_residual(m)
    assert z==Fraction(2,3)
    print(f'H0_EXHAUSTIVE m={m} min_residual={z} PASS')

# Exact pseudo-stationary one-site marginal law proving the matching upper obstruction.
for m in (4,6,8,10,12,20):
    a,b,er=pseudo_stationary_marginal_check(m)
    print(f'PSEUDO_MARGINAL_INVARIANCE m={m} a={a} b={b} expected_reward={er} PASS')

# Reuse the previous exact w=5 Bellman upper fraction only as an arithmetic
# obstruction: widths <=5 were already certified individually in the earlier artifact.
w5_hi=Fraction(3745176481648434628276480,4835703278458516698824704)
assert w5_hi<L_SOURCE
print('PRIOR_W5_UPPER_LT_CURRENT_SOURCE_LOWER',w5_hi,'<',L_SOURCE,'PASS')
print('ONE_SITE_OPTIMUM_EXACT_VALUE 2/3 (lower witness H0 + upper pseudo-stationary marginal law)')
print('ALL_EXACT_CHECKS_PASS')
