#!/usr/bin/env python3
"""Exact sanity checks for B17's buried-atom cancellation-flow route.

The universal theorem in REPORT.md is analytic.  This program exhaustively
checks its rational spectral/variance consequences through n=4 and verifies
the exact Boolean packing-collision witnesses.  No floating-point comparison
decides a PASS.
"""
from fractions import Fraction
import json

def fwht_int(vals):
    a=list(map(int, vals)); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def superset_zeta(nums,n):
    q=list(nums)
    for i in range(n):
        bit=1<<i
        for S in range(1<<n):
            if not (S&bit):
                q[S]+=q[S|bit]
    return q

function_count=0
nonempty_coefficient_checks=0
integer_variance_checks=0
maximal_support_checks=0
for n in range(1,5):
    N=1<<n
    for mask in range(1<<N):
        vals=[-1 if (mask>>x)&1 else 1 for x in range(N)]
        W=fwht_int(vals)
        sq=[w*w for w in W]
        qnum=superset_zeta(sq,n)
        function_count+=1
        for S in range(1,N):
            if W[S]==0: continue
            nonempty_coefficient_checks+=1
            m=S.bit_count()
            # delta=2^(1-m), mu=|fhat(S)|/delta = |W[S]|*2^(m-1)/N.
            mu=Fraction(abs(W[S])*(1<<(m-1)),N)
            var_scaled=Fraction(qnum[S]-sq[S],N*N) * (1<<(2*m-2))
            if mu<=1:
                assert var_scaled >= mu*(1-mu)
                integer_variance_checks+=1
            # q=p iff no supported strict superset.
            if qnum[S]==sq[S]:
                assert mu>=1
                maximal_support_checks+=1

# Four-bit exact Boolean collision witness:
# f=-1 at antipodal 0111 and 1000, +1 elsewhere.
n=4; N=16
vals=[1]*N
vals[0b0111]=vals[0b1000]=-1
W=fwht_int(vals)
sq=[w*w for w in W]
weights=[Fraction(x,N*N) for x in sq]
support=[S for S,w in enumerate(W) if w]
assert support==[0,3,5,6,9,10,12,15]
assert weights[0]==Fraction(9,16)
for S in support[1:]:
    assert weights[S]==Fraction(1,16)
I=sum((S.bit_count()*weights[S] for S in range(N)),Fraction(0))
assert I==1
pairs=[S for S in support if S.bit_count()==2]
assert len(pairs)==6
top=15
# delta^2=1/4, p=1/16, so d=p*log2(4)=1/8 exactly.
pair_deficit=Fraction(1,8)
for S in pairs:
    strict=[T for T in support if T!=S and (T&S)==S]
    assert strict==[top]
    assert not [T for T in support if T.bit_count()==3 and (T&S)==S]
total_demand=len(pairs)*pair_deficit
top_capacity=top.bit_count()*weights[top]
assert total_demand==Fraction(3,4)
assert top_capacity==Fraction(1,4)
assert total_demand/top_capacity==3

# Perfect-autocorrelation cancellation for every nonzero xor shift.
a=[Fraction(w,N) for w in W]
for U in range(1,N):
    assert sum((a[A]*a[A^U] for A in range(N)),Fraction(0))==0
# For every pair S, the strict receiver top has xor shift U=top xor S,
# which is the complementary pair and is itself a supported source atom.
for S in pairs:
    U=top^S
    assert U in pairs

# Smallest checked Hasse-skip example: n=3, mask 6.
vals3=[-1 if (6>>x)&1 else 1 for x in range(8)]
W3=fwht_int(vals3)
supp3=[S for S,w in enumerate(W3) if w]
assert supp3==[0,3,4,7]
S=4
assert [T for T in supp3 if T!=S and (T&S)==S]==[7]
assert not [T for T in supp3 if T.bit_count()==2 and (T&S)==S]

# All-dimensional two-antipodal family formula checked at several even n.
family_checks=[]
for n in (4,6,8,10):
    N=1<<n
    vals=[1]*N
    vals[0]=vals[N-1]=-1
    Wn=fwht_int(vals)
    pn=Fraction(16,N*N)
    assert Wn[0]==N-4
    supportn=[S for S,w in enumerate(Wn) if w]
    assert supportn[0]==0
    assert all((S.bit_count()%2)==0 for S in supportn)
    assert len(supportn)==1<<(n-1)
    for S in supportn[1:]:
        assert Fraction(Wn[S]*Wn[S],N*N)==pn
    near=[S for S in supportn if S.bit_count()==n-2]
    assert len(near)==n*(n-1)//2
    # For near-top S: delta^2/p = 4, so d_S=2p.
    demand=2*pn*len(near)
    topcap=n*pn
    assert demand/topcap==n-1
    # Every near-top S has top as its only supported strict superset.
    for S in near:
        strict=[T for T in supportn if T!=S and (T&S)==S]
        assert strict==[(1<<n)-1]
    family_checks.append({"n":n,"near_top_count":len(near),
                          "receiver_congestion_lower_bound":str(n-1)})

out={
 "status":"PASS",
 "scope":"exhaustive Boolean n=1..4 exact rational spectral variance consequences; exact n=4 congestion witness; exact n=3 Hasse-skip witness",
 "functions_checked":function_count,
 "nonempty_fourier_coefficients_checked":nonempty_coefficient_checks,
 "integer_variance_checks_mu_le_1":integer_variance_checks,
 "maximal_support_granularity_checks":maximal_support_checks,
 "two_antipodal_family_checks":family_checks,
 "collision_witness":{
   "n":4,
   "negative_inputs_binary":["0111","1000"],
   "support_masks":support,
   "spectrum":"p_empty=9/16; p_S=1/16 on six level-2 sets and the full set",
   "influence":"1",
   "pair_deficit_each":"1/8",
   "pair_deficit_total":"3/4",
   "only_common_strict_receiver":"1111",
   "receiver_capacity":"1/4",
   "strict_superset_congestion_kappa":"3",
   "immediate_supported_supersets_per_pair":0
 },
 "hasse_skip_witness":{"n":3,"mask":6,"support_masks":supp3,"buried_singleton":4,"only_strict_receiver":7},
 "full_FEI_status":"OPEN / NOT PROVED"
}
print(json.dumps(out,indent=2,sort_keys=True))
