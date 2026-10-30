#!/usr/bin/env python3
from fractions import Fraction
from math import log2, comb
import json

def fwht(a):
    a=list(map(int,a)); n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def spectral(vals):
    N=len(vals); W=fwht(vals); den=N*N
    return [Fraction(w*w,den) for w in W]

def exact_banks(ps):
    n=(len(ps)).bit_length()-1
    I=sum((p*s.bit_count() for s,p in enumerate(ps)), Fraction(0))
    tau=sum(ps[1:], Fraction(0))
    r=[Fraction(0) for _ in range(n)]
    e=[[Fraction(0) for _ in range(n)] for __ in range(n)]
    ordinary_depth=Fraction(0)
    for s,p in enumerate(ps):
        k=s.bit_count()
        if not p or k==0: continue
        ordinary_depth += p*k*(k-1)
        for i in range(n):
            if (s>>i)&1:
                r[i]+=p/Fraction(k)
        if k>=2:
            for i in range(n):
                if not ((s>>i)&1): continue
                for j in range(n):
                    if i!=j and ((s>>j)&1):
                        e[i][j]+=p/Fraction(k)
    return I,tau,r,e,ordinary_depth

def H_float(probs):
    return sum(float(p)*log2(1/float(p)) for p in probs if p)

def layer_incidence_residual(ps):
    """R_inc = sum_k mass_k [H(S|K=k)-H(M|K=k)], base 2."""
    n=(len(ps)).bit_length()-1
    ans=0.0
    for k in range(1,n+1):
        layer=[s for s,p in enumerate(ps) if p and s.bit_count()==k]
        mass=sum((ps[s] for s in layer),Fraction(0))
        if not mass: continue
        q=[ps[s]/mass for s in layer]
        hs=H_float(q)
        mark=[Fraction(0) for _ in range(n)]
        for s,qq in zip(layer,q):
            for i in range(n):
                if (s>>i)&1:
                    mark[i]+=qq/Fraction(k)
        hm=H_float(mark)
        ans += float(mass)*(hs-hm)
    return ans

exhaustive = {}
total_functions=0
max_rinc_ratio={"value":None,"n":None,"mask":None}
for n in range(1,5):
    N=1<<n; checked=0
    for mask in range(1<<N):
        vals=[-1 if ((mask>>x)&1) else 1 for x in range(N)]
        ps=spectral(vals)
        I,tau,r,e,D=exact_banks(ps)
        assert sum(r,Fraction(0)) == tau
        assert sum((e[i][j] for i in range(n) for j in range(n) if i!=j), Fraction(0)) == I-tau
        for i in range(n):
            for j in range(n):
                if i!=j:
                    assert e[i][j] == e[j][i]
        assert D == sum((p*s.bit_count()*(s.bit_count()-1) for s,p in enumerate(ps)), Fraction(0))
        den=I-tau
        if den>0:
            rinc=layer_incidence_residual(ps)
            ratio=rinc/float(den)
            if max_rinc_ratio["value"] is None or ratio>max_rinc_ratio["value"]:
                max_rinc_ratio={"value":ratio,"n":n,"mask":mask}
        checked += 1
    exhaustive[str(n)] = checked
    total_functions += checked

# Exact central-binomial lower bound 4m a_m^2 >= 1 used in analytic majority no-go.
for m in range(1,1001):
    a=Fraction(comb(2*m,m), 4**m)
    assert 4*m*a*a >= 1

def majority_vals(n):
    m=(n-1)//2
    return [1 if x.bit_count()<=m else -1 for x in range(1<<n)]

maj=[]
for n in [3,5,7,9,11,13]:
    m=(n-1)//2
    ps=spectral(majority_vals(n))
    I,tau,r,e,D=exact_banks(ps)
    infl=[sum((p for s,p in enumerate(ps) if (s>>i)&1),Fraction(0)) for i in range(n)]
    assert len(set(infl))==1
    j=infl[0]
    assert j == Fraction(comb(2*m,m), 4**m)
    assert I == n*j
    assert tau == 1
    # Exact majority derivative geometry gives d_i/j_i=m, hence sum d_i=mJ.
    assert D == m*I
    Hdepth=I-tau
    weighted_defect=float(D) - 0.5*float(I)*log2(1/float(j))
    rinc=layer_incidence_residual(ps)
    maj.append({
        "n":n,
        "j":f"{j.numerator}/{j.denominator}",
        "I":f"{I.numerator}/{I.denominator}",
        "ordinary_depth_sum":f"{D.numerator}/{D.denominator}",
        "harmonic_mixed_curvature_sum":f"{Hdepth.numerator}/{Hdepth.denominator}",
        "ordinary_depth_over_J":float(D/I),
        "weighted_depth_defect_over_J":weighted_defect/float(I),
        "harmonic_bank_over_J":float(Hdepth/I),
        "R_inc_over_harmonic_bank":rinc/float(Hdepth),
    })

one_point=[]
for n in [4,5,6,8,10,12,16,20]:
    # f=1-2*1_{0}; nonzero Fourier masses are all q=(2/2^n)^2.
    N=2**n
    p0=Fraction((N-2)**2,N*N)
    q=Fraction(4,N*N)
    tau=1-p0
    I=q*sum(Fraction(comb(n,k)*k) for k in range(1,n+1))
    rinc=0.0
    for k in range(1,n+1):
        mass=comb(n,k)*float(q)
        rinc += mass*(log2(comb(n,k))-log2(n))
    den=float(I-tau)
    one_point.append({
        "n":n,
        "I":float(I),
        "tau":float(tau),
        "R_inc_over_harmonic_bank":rinc/den if den>0 else None,
    })

out={
    "status":"PASS",
    "scope":{
        "exhaustive_boolean_functions_n_le_4":exhaustive,
        "total_exhaustive_functions":total_functions,
        "central_binomial_lower_bound_m_le_1000":"PASS",
        "majority_dimensions":[3,5,7,9,11,13],
        "one_point_dimensions":[4,5,6,8,10,12,16,20],
    },
    "exact_identities_checked":[
        "sum_i r_i = tau",
        "e_ik = e_ki",
        "sum_{i!=k} e_ik = I - tau",
        "ordinary mixed-depth sum = E[K(K-1)]",
        "for odd majority: ordinary mixed-depth sum = ((n-1)/2) J",
    ],
    "finite_diagnostic_not_a_theorem":{
        "max_R_inc_over_I_minus_tau_n_le_4":max_rinc_ratio,
        "majority":maj,
        "one_point_defect":one_point,
    },
    "full_FEI_status":"OPEN; finite diagnostics do not establish the proposed harmonic-Riesz bridge"
}
print(json.dumps(out,indent=2))
