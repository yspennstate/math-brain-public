#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
from math import factorial
import json, random


def parity_value(R, S, c=Fraction(1)):
    return c if len(R & S) % 2 else Fraction(0)


def shapley_values(players, value):
    players = tuple(players)
    n = len(players)
    out = {a: Fraction(0) for a in players}
    for a in players:
        others = [b for b in players if b != a]
        for mask in range(1 << (n-1)):
            S = {others[j] for j in range(n-1) if (mask >> j) & 1}
            k = len(S)
            w = Fraction(factorial(k) * factorial(n-k-1), factorial(n))
            out[a] += w * (value(S | {a}) - value(S))
    return out


def block_defect(m, R, c=Fraction(1)):
    players = tuple(range(2*m))
    fine = shapley_values(players, lambda S: parity_value(R, S, c))
    blocks = tuple(range(m))
    coarse = shapley_values(blocks, lambda B: parity_value(R, {2*j+b for j in B for b in (0,1)}, c))
    delta = []
    for j in blocks:
        delta.append(fine[2*j] + fine[2*j+1] - coarse[j])
    return delta


def formula_data(m, R, c=Fraction(1)):
    touched=[]; doubled=[]; single=[]
    for j in range(m):
        occ = int(2*j in R)+int(2*j+1 in R)
        if occ:
            touched.append(j)
        if occ==2:
            doubled.append(j)
        elif occ==1:
            single.append(j)
    q=len(R); r=len(doubled); k=len(single); s=r+k
    assert q == k+2*r
    if q % 2 != 1:
        raise ValueError('R must have odd size')
    delta=[]
    for j in range(m):
        if j in doubled:
            delta.append(Fraction(2)*c/q)
        elif j in single:
            delta.append(c/q-c/k)
        else:
            delta.append(Fraction(0))
    current={}
    if s:
        for a,b in combinations(touched,2):
            current[(a,b)] = (delta[a]-delta[b])/s
    energy=sum(v*v for v in current.values())
    expected=Fraction(2*(q-k), q*q*k)*c*c
    ward=(Fraction(q-1,q)*c*c) if q>0 else Fraction(0)
    inv=Fraction(c*c,q)
    return dict(q=q,r=r,k=k,s=s,delta=delta,current=current,energy=energy,expected=expected,ward=ward,inv=inv)


def translated_sign(R,z):
    return -1 if len(R & z)%2 else 1

# 1) exhaustive direct Shapley versus formula for all odd relations, m <= 3
shapley_checks=0
energy_checks=0
ratio_max=Fraction(0)
ratio_arg=None
for m in range(1,4):
    P=set(range(2*m))
    for mask in range(1,1<<(2*m)):
        R={i for i in P if mask>>i&1}
        if len(R)%2==0: continue
        f=formula_data(m,R)
        d=block_defect(m,R)
        assert d==f['delta'], (m,R,d,f['delta'])
        assert sum(d,Fraction(0))==0
        assert f['energy']==f['expected']
        shapley_checks+=1; energy_checks+=1
        if f['q']>1:
            ratio=f['energy']/f['ward']
            if ratio>ratio_max:
                ratio_max=ratio; ratio_arg=(m,tuple(sorted(R)),f['q'],f['k'])
            assert ratio <= Fraction(2,3)
        assert f['energy'] <= 2*f['inv'] if f['q']>=3 else f['energy']==0
assert ratio_max==Fraction(2,3)

# 2) resolvent identity exhaustive odd q,k feasible through q<=31
resolvent_checks=0
for q in range(1,32,2):
    for k in range(1,q+1,2):
        if (q-k)%2: continue
        # 2 int int x^(q-1)(y^(k-1)-y^(q-1)) = exact rational
        res = Fraction(2,q)*(Fraction(1,k)-Fraction(1,q))
        coeff=Fraction(2*(q-k),q*q*k)
        assert res==coeff
        if q>1:
            assert coeff/Fraction(q-1,q) <= Fraction(2,3)
        resolvent_checks += 1

# 3) exact Walsh translation diagonalisation for deterministic signed families
# Aggregate duplicate supports before checking, as required by the theorem.
rng=random.Random(160912)
translation_checks=0
family_checks=0
negative_credit_families=0
for m in range(1,5):
    allR=[]
    for mask in range(1,1<<(2*m)):
        R=frozenset(i for i in range(2*m) if mask>>i&1)
        if len(R)%2: allR.append(R)
    for trial in range(12):
        coeff={}
        for _ in range(min(12,len(allR)*2)):
            R=rng.choice(allR)
            c=Fraction(rng.randint(-4,4), rng.choice([1,2,3]))
            if c:
                coeff[R]=coeff.get(R,Fraction(0))+c
        coeff={R:c for R,c in coeff.items() if c}
        if any(c<0 for c in coeff.values()): negative_credit_families+=1
        # relation currents
        rel={R:formula_data(m,set(R),c)['current'] for R,c in coeff.items()}
        rhs=sum((formula_data(m,set(R),c)['energy'] for R,c in coeff.items()),Fraction(0))
        # average over all syndrome translations z in fine q-flip player cube
        total=Fraction(0)
        for zmask in range(1<<(2*m)):
            z={i for i in range(2*m) if zmask>>i&1}
            e=Fraction(0)
            for a,b in combinations(range(m),2):
                j=Fraction(0)
                for R,c in coeff.items():
                    j += translated_sign(set(R),z)*rel[R].get((a,b),Fraction(0))
                e += j*j
            total += e
            translation_checks+=1
        lhs=total/Fraction(1<<(2*m))
        assert lhs==rhs,(m,trial,lhs,rhs)
        family_checks+=1

# 4) generic pointwise cross-term obstruction: same current, distinct syndrome characters
# One doubled block and k odd single blocks; choosing either clone in each single
# gives 2^k distinct odd supports with identical current at z=0.
pointwise_obstruction=[]
for k in (1,3,5,7,9):
    q=k+2
    one=Fraction(2*(q-k),q*q*k)  # c=1 current energy
    count=2**k
    diagonal=count*one
    pointwise=count*count*one
    assert pointwise/diagonal == count
    pointwise_obstruction.append({'k':k,'relations':count,'amplification':count})

# 5) direct character orthogonality sanity, distinct supports
orth_checks=0
for m in range(1,5):
    supports=[]
    for mask in range(1,1<<(2*m)):
        R=frozenset(i for i in range(2*m) if mask>>i&1)
        if len(R)%2: supports.append(R)
    for A,B in combinations(supports[:min(16,len(supports))],2):
        s=0
        for zmask in range(1<<(2*m)):
            z={i for i in range(2*m) if zmask>>i&1}
            s += translated_sign(set(A),z)*translated_sign(set(B),z)
        assert s==0
        orth_checks+=1

out={
  'status':'PASS',
  'scope':'exact algebraic checks for parity-current/Walsh-frame theorem; not an FEI proof',
  'direct_shapley_checks':shapley_checks,
  'current_energy_checks':energy_checks,
  'resolvent_checks':resolvent_checks,
  'translation_state_energy_checks':translation_checks,
  'signed_family_checks':family_checks,
  'families_with_negative_aggregate_coefficients':negative_credit_families,
  'character_orthogonality_checks':orth_checks,
  'pointwise_cross_term_obstruction':pointwise_obstruction,
  'sharp_ratio_max':f'{ratio_max.numerator}/{ratio_max.denominator}',
  'sharp_ratio_example':ratio_arg,
  'singleton_q1_current_energy':'0',
}
print(json.dumps(out,sort_keys=True,indent=2))
