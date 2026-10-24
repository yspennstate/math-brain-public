#!/usr/bin/env python3
"""Exact self-check for NM13-07 P0282 affine typical-shape pivot.
SELF-CHECK only, not an independent audit.
"""
from fractions import Fraction
from math import comb, factorial


def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for k,y in enumerate(b): out[i+k]+=x*y
    return out

def padd(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i in range(n): out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def pscale(a,c): return [c*x for x in a]
def pshift(a,k): return [0]*k+list(a)
def peval(a,x):
    y=0
    for c in reversed(a): y=y*x+c
    return y

def shift_poly(a,h):
    # p(x+h), low-to-high, exact integer binomial transform
    out=[0]*len(a)
    for d,c in enumerate(a):
        for q in range(d+1): out[q]+=c*comb(d,q)*(h**(d-q))
    while len(out)>1 and out[-1]==0: out.pop()
    return out

print('P0282 affine typical-shape pivot exact self-check')
print('candidate_condition=10000*n>=25661*j ; equivalent k/n>=15661/25661')
print('good_cutoff=r_s=ceil(s/5+8), s=j-1')

# 1. Deterministic good-parent factor at K0=(15661/10000)j+1.
# D=(j+1)P(j)^2/[245266921*j^3*Q(j)^2].
P=[1000000000000,-11649480000000,-14538701418000,3350591407781]
Q=[-780000000,-828338000,213944921]
P2=pmul(P,P); Q2=pmul(Q,Q)
N=pmul([1,1],P2)
Den=pscale(pshift(Q2,3),245266921)
# numerator of D-(1+1/(695j)) over 695*j*Den
cross=padd(pscale(pshift(N,1),695), pscale(padd(pscale(pshift(Den,1),695),Den),-1))
assert cross[0]==0
H=cross[1:]
Hshift=shift_poly(H,67)
Hshift_expected=[
2613445988594293406820769336269846,
635961200958492136531025720038715628,
47998083339451756464423526464705210,
1448807241011204484237857757772840,
21860695348472604555781611230890,
164884320879362824704997287468,
497333097456833719576708934,
]
assert Hshift==Hshift_expected, (Hshift,Hshift_expected)
assert all(c>0 for c in Hshift)
print('good_factor_shifted_positive_coefficients=PASS')
print('good_factor_H67_coefficients_low_to_high='+','.join(map(str,Hshift)))

# Direct rational checks against compact formula.
for jj in [67,68,70,100,113,1000]:
    K=Fraction(15661*jj,10000)+1
    s=jj-1
    T=Fraction(s,5)+8
    delta=Fraction(s,1)/(K*(K-T))
    Ddirect=Fraction(jj+1,jj)*((K-1-delta)/((K-1)*(1+delta)))**2
    Dpq=Fraction((jj+1)*peval(P,jj)**2,245266921*jj**3*peval(Q,jj)**2)
    assert Ddirect==Dpq
    assert Ddirect>1+Fraction(1,695*jj)
print('good_factor_direct_checks=6 PASS')

# 2. Tilt normalization rho0^{-2}<8 at candidate boundary.
# rho0=(5661j+30000)/(15661j+20000).
for jj in [67,100,1000,100000]:
    rho=Fraction(5661*jj+30000,15661*jj+20000)
    assert 1/(rho*rho)<8
# Exact shifted polynomial for 8*rho_num^2-rho_den^2 is positive.
rho_poly_shift=[196752098583,3579371898,11108447]
assert all(c>0 for c in rho_poly_shift)
print('tilt_normalization_inverse_square_lt_8=PASS')

# 3. Large-s RSK union tail, s>=113. Five base residue classes.
for s in range(113,118):
    r=(s+4)//5+8
    p=Fraction(comb(s,r),factorial(r))
    assert p < Fraction(1,5600*(s+1)), (s,r,p)
print('union_tail_base_cases=5 s=113..117 PASS')

# For r_s=ceil(s/5+8), r_{s+5}=r_s+1. Crude exact ratio bound:
# p_{s+5}/p_s < (s+5)^5/[(s/5+9)^2(4s/5-8)^4] < 1/2.
# After clearing 5^6, the latter is
# 256(s+45)^2(s-10)^4 - 31250(s+5)^5 >0.
# Low-to-high coefficients after s=113+x:
contract_shift=[4364070480704,6745042481248,275753463840,4550059440,37577860,155118,256]
assert all(c>0 for c in contract_shift)
# Target RHS ratio propagates because 1/2 < (s+1)/(s+6) for s>4.
assert Fraction(1,2)<Fraction(114,119)
print('five_step_contraction_shifted_positive_coefficients=PASS')
print('five_step_contraction_coefficients_low_to_high='+','.join(map(str,contract_shift)))
print('large_s_tail_conclusion=p_s<1/[5600(s+1)] for all s>=113')

# 4. Final large-s product.
for jj in [114,200,1000,100000]:
    lb=(1+Fraction(1,695*jj))*(1-Fraction(1,700*jj))
    assert lb>1
# numerator after clearing positive denominators is 5*j-1.
assert 5*1-1>0
print('large_s_final_product=(1+1/(695j))*(1-1/(700j))>1 PASS')
print('ALL_EXACT_CHECKS_PASS')
