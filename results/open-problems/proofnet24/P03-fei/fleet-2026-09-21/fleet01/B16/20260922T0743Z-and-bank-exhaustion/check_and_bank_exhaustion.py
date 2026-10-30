#!/usr/bin/env python3
from fractions import Fraction as F

# Exact 35-inequality positive-multiplier certificate.
# It proves: if L_{p,q}(psi) >= -K M(p,q) on these pairs and psi(1/2)=0,
# then R_wit(psi) <= kappa K. No floating point is used.

def srep(x):
    return x if x <= F(1,2) else 1-x

CERT = [
 ((1080,1081),(3,8),4820718911,661801480960),
 ((4,1081),(1,4),14462156733,5294411847680),
 ((1072,1081),(1,4),10350575,43665252352),
 ((1072,1081),(3,8),1915,2117764739072),
 ((16,1081),(1,4),14462156733,21177647390720),
 ((18,1081),(1,2),30640,517032407),
 ((1026,1081),(1,2),1915,33090074048),
 ((1024,1081),(1081,2048),443569786466041,572325920734208),
 ((1024,1081),(1,2),309596144080163,2710738866012160),
 ((64,1081),(1,4),14462156733,84710589562880),
 ((1014,1081),(1,2),10350575,5458156544),
 ((1010,1081),(1,2),1915,2068129628),
 ((72,1081),(1,4),15320,517032407),
 ((110,1081),(1,2),1915,66180148096),
 ((128,1081),(1,2),14462156733,338842358251520),
 ((912,1081),(1,4),4820718911,41362592560),
 ((910,1081),(1,2),10350575,170567392),
 ((880,1081),(1,2),1915,529441184768),
 ((228,1081),(1,4),4820718911,10340648140),
 ((268,1081),(1,4),10350575,10916313088),
 ((1,4),(284,1081),1915,4136259256),
 ((1,4),(288,1081),3830,517032407),
 ((1,4),(684,1081),10350575,341134784),
 ((1,4),(440,1081),1915,132360296192),
 ((1,4),(512,1081),14462156733,677684716503040),
 ((794,1081),(1,2),10350575,1364539136),
 ((768,1081),(1081,2048),1225600,5330231),
 ((338,1081),(1,2),4820718911,165450370240),
 ((402,1081),(1,2),1915,1058882369536),
 ((676,1081),(1,2),4820718911,330900740480),
 ((626,1081),(1,2),10350575,85283696),
 ((576,1081),(1,2),1915,1034064814),
 ((574,1081),(1,2),10350575,2729078272),
 ((1081,2048),(512,1081),30958168192343,143081480183552),
 ((568,1081),(1,2),1915,16545037024)
]

coeff = {}
cost = F(0)
for (pn,pd),(qn,qd),ln,ld in CERT:
    p,q,lam = F(pn,pd),F(qn,qd),F(ln,ld)
    assert lam > 0
    # -L = -q psi(p)-p psi(q)+psi(pq) <= K M.
    for x,c in ((srep(p),-q),(srep(q),-p),(srep(p*q),F(1))):
        coeff[x]=coeff.get(x,F(0))+lam*c
    cost += lam*p*q*(1-p)*(1-q)

# Center coefficient is irrelevant because psi(1/2)=0.
coeff.pop(F(1,2),None)
coeff={x:c for x,c in coeff.items() if c}
target={F(3,8):F(57,256), F(967,2048):-F(1)}
assert coeff == target
kappa=cost
assert kappa == F(792001822391570453,11721234856636579840)
assert kappa < F(67570,10**6)

delta=F(176114,10**7)   # source witness deficit is strictly greater than this.
A=F(258204856,10**9)    # guaranteed extra AND bank above the certified 0.01 lift.
Kreq=delta/kappa
assert Kreq > F(26064,100000)
assert Kreq > A

print("PASS")
print("multiplier_count",len(CERT))
print("kappa_exact",f"{kappa.numerator}/{kappa.denominator}")
print("kappa_decimal",format(float(kappa),".15f"))
print("K_required_from_delta_gt_0.0176114",format(float(Kreq),".15f"))
print("guaranteed_AND_bank",format(float(A),".15f"))
print("required_over_bank",format(float(Kreq/A),".12f"))
