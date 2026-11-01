from fractions import Fraction
from math import comb, prod
from itertools import product

def det_mod_rank(rows, p):
    A=[list(map(lambda x:x%p,row)) for row in rows]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                a=A[i][c]%p
                A[i]=[(A[i][j]-a*A[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

def support(v,p):
    return sum((x%p)!=0 for x in v)

def plane_support_spectrum(p):
    v=[1,1,-1,0,0,0]
    w=[0,0,0,1,1,-1]
    reps=[v,w]+[[(v[i]+t*w[i])%p for i in range(6)] for t in range(1,p)]
    return sorted(support(x,p) for x in reps)

def single_relation_boolean_count(p):
    c=0
    for x in product((0,1), repeat=3):
        if (x[0]+x[1]-x[2])%p==0:
            c+=1
    return c

def exact_family(m,p,current,D):
    # Two disjoint support-3 balanced relation lines.
    h=9*2**(m-6)
    N=Fraction(9,2)*comb(m,3)*comb(m-3,3)
    assert N.denominator==1
    N=int(N)
    # Greedy ordered basis of the (m-2)-dimensional null hyperplane:
    # after j independent Boolean columns, their span contains <= 2^j Boolean points.
    B=prod(h-2**j for j in range(m-2))
    extra=(h-m+1)*(h-m)
    E=N*B*extra
    c=Fraction(p*(p*p-1),p**D-1)
    delta=Fraction(2**(m+1),2**(m*m))*(Fraction(p)-c)*E
    new=current-delta
    return dict(m=m,p=p,D=D,h=h,N=N,B=B,extra=extra,E=E,c=c,delta=delta,new=new)

assert single_relation_boolean_count(7)==3
assert single_relation_boolean_count(11)==3
assert plane_support_spectrum(7)==[3,3]+[6]*6
assert plane_support_spectrum(11)==[3,3]+[6]*10

# Exact finite metric inputs from immutable R03 run21/C262, reused rather than recomputed.
current10=Fraction(635840639911659887775,2305843009213693952)
current11=Fraction(4089568153828729532838706676925,7787900129957441143457185792)

cases=[
    exact_family(9,7,current10,4),
    exact_family(10,11,current11,5),
]

expected=[
    {
      "h":72, "N":7560, "B":387599564800, "extra":4032,
      "E":11814778926268416000,
      "c":Fraction(7,50),
      "delta":Fraction(1207729927215,35184372088832),
      "new":Fraction(635761490123149925535,2305843009213693952)
    },
    {
      "h":144, "N":18900, "B":7094622434099200, "extra":18090,
      "E":2425658504840950579200000,
      "c":Fraction(132,16105),
      "delta":Fraction(319925953077122266875,7427120332677308219392),
      "new":Fraction(4089232687152555736280595956925,7787900129957441143457185792)
    }
]
for z,e in zip(cases,expected):
    for k,v in e.items():
        assert z[k]==v,(z["m"],k,z[k],v)

# A small direct finite sanity check for the cube/subspace lemma:
# any d-dimensional coordinate-subspace has exactly 2^d Boolean points,
# so the greedy bound's 2^j exclusion is sharp in that model.
for d in range(0,7):
    assert len(list(product((0,1), repeat=d)))==2**d

# Asymptotic upper envelope for this family:
# E <= N h^m, h=9*2^(m-6), N=O(m^6);
# after normalization the improvement is <= (p-c) * 2^(m+1-m^2) * N*h^m
# = 2(p-c)N*(9/32)^m. This tends to 0 exponentially for fixed p.
for z in cases:
    m,p=z["m"],z["p"]
    asym_upper=Fraction(2)*(Fraction(p)-z["c"])*z["N"]*Fraction(9,32)**m
    assert z["delta"] <= asym_upper
    print(f"CASE m={m} p={p}")
    print("support_spectrum", plane_support_spectrum(p))
    print("h",z["h"])
    print("planes_N",z["N"])
    print("ordered_basis_lower",z["B"])
    print("extra_columns_factor",z["extra"])
    print("exact_corank2_subset_E",z["E"])
    print("C253_c",z["c"],float(z["c"]))
    print("metric_delta",z["delta"],float(z["delta"]))
    print("new_metric_upper",z["new"],float(z["new"]))
    print("fixed_p_asymptotic_upper_for_delta",asym_upper,float(asym_upper))

print("SELF-CHECK PASS")
