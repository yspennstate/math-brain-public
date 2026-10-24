#!/usr/bin/env python3
import json, math
from fractions import Fraction

def fwht_int(v):
    a=list(v); h=1
    while h<len(a):
        for base in range(0,len(a),2*h):
            for k in range(h):
                x=a[base+k]; y=a[base+k+h]
                a[base+k]=x+y; a[base+k+h]=x-y
        h*=2
    return a

def spectrum(vals):
    N=len(vals); w=fwht_int(vals); m=[x*x for x in w]
    assert sum(m)==N*N
    return w,m

def entropy(vals):
    N=len(vals); _,m=spectrum(vals); den=N*N
    ans=0.0
    for a in m:
        if a:
            p=a/den; ans-=p*math.log2(p)
    return ans

def influences_truth(vals,m):
    M=1<<m
    return [Fraction(sum(vals[x]!=vals[x^(1<<k)] for x in range(M)),M)
            for k in range(m)]

def character_center(vals,n):
    p=influences_truth(vals,n)
    A=[i for i,x in enumerate(p) if x>Fraction(1,2)]
    out=[]
    for x,v in enumerate(vals):
        parity=sum((x>>i)&1 for i in A)&1
        out.append(-v if parity else v)
    pc=influences_truth(out,n)
    assert all(x<=Fraction(1,2) for x in pc)
    return out,pc,A

def physical_child(vals,n,i,b):
    out=[]
    for y in range(1<<(n-1)):
        x=0; r=0
        for k in range(n):
            if k==i: bit=b
            else: bit=(y>>r)&1; r+=1
            x |= bit<<k
        out.append(vals[x])
    return out

def pair_child(vals,n,i,j,s,eliminate):
    other=j if eliminate==i else i
    rem=[k for k in range(n) if k!=eliminate]
    out=[]
    for y in range(1<<(n-1)):
        bits={k:(y>>r)&1 for r,k in enumerate(rem)}
        bits[eliminate]=s ^ bits[other]
        x=sum(bits[k]<<k for k in range(n))
        out.append(vals[x])
    return out

def J_from_influences(p):
    return sum(((x if x<=Fraction(1,2) else 1-x) for x in p), Fraction(0,1))

def psi(x):
    x=float(x if x<=Fraction(1,2) else 1-x)
    if x<=0.0: return 0.0
    if x>=0.5: h=1.0
    else: h=-(x*math.log2(x)+(1-x)*math.log2(1-x))
    z=0.5+math.sqrt(x*(1-x))
    if z>=1.0: hz=0.0
    else: hz=-(z*math.log2(z)+(1-z)*math.log2(1-z))
    return h+1.0-hz

def run():
    functions=0; pair_checks=0; centered_checks=0; cap_checks=0
    max_cap_violation=-1e99
    ratios={}
    for n in range(1,5):
        N=1<<n; num=1<<N
        worst_phys=(-1.0,None,None); worst_hyb=(-1.0,None,None)
        nonconstant=0
        for mask in range(num):
            vals=[-1 if ((mask>>x)&1) else 1 for x in range(N)]
            functions+=1
            centered,p,A=character_center(vals,n)
            J=sum(p,Fraction(0,1))  # centered => J=I
            H=entropy(centered)
            if J: nonconstant+=1
            _,m=spectrum(centered); den=N*N
            phys=[]
            for i in range(n):
                if p[i]:
                    hc=sum(entropy(physical_child(centered,n,i,b)) for b in (0,1))/2.0
                    phys.append((H-hc)/float(p[i]))
            pairs=[]
            for i in range(n):
                for j in range(i+1,n):
                    pair_checks+=1
                    pij=Fraction(sum(m[S] for S in range(N)
                                     if ((S>>i)&1) and ((S>>j)&1)),den)
                    children=[pair_child(centered,n,i,j,s,i) for s in (0,1)]
                    child_p=[influences_truth(c,n-1) for c in children]
                    avgI=sum((sum(q,Fraction(0,1)) for q in child_p),Fraction(0,1))/2
                    assert J-avgI == 2*pij
                    avgJ=sum((J_from_influences(q) for q in child_p),Fraction(0,1))/2
                    D=J-avgJ
                    refund=sum((sum((2*x-1 for x in q if x>Fraction(1,2)),Fraction(0,1))
                                for q in child_p),Fraction(0,1))/2
                    assert D == 2*pij + refund
                    centered_checks+=1
                    for s in (0,1):
                        a=sorted(spectrum(pair_child(centered,n,i,j,s,i))[1])
                        b=sorted(spectrum(pair_child(centered,n,i,j,s,j))[1])
                        assert a==b
                    hc=sum(entropy(c) for c in children)/2.0
                    delta=H-hc
                    cap=min(psi(p[i]),psi(p[j]))
                    max_cap_violation=max(max_cap_violation,delta-cap)
                    assert delta <= cap+5e-12
                    cap_checks+=1
                    if D:
                        pairs.append(delta/float(D))
            if J:
                rp=min(phys) if phys else 0.0
                rh=min(phys+pairs) if pairs else rp
                HJ=H/float(J)
                if rp>worst_phys[0]+1e-12: worst_phys=(rp,mask,HJ)
                if rh>worst_hyb[0]+1e-12: worst_hyb=(rh,mask,HJ)
        ratios[str(n)]={
            "nonconstant":nonconstant,
            "worst_best_centered_physical_ratio":worst_phys[0],
            "worst_best_centered_hybrid_ratio":worst_hyb[0],
            "hybrid_extremizer_truth_mask":worst_hyb[1],
            "hybrid_extremizer_H_over_J":worst_hyb[2]
        }
    return {
        "status":"PASS",
        "scope":"all Boolean truth tables n<=4",
        "functions_checked":functions,
        "pair_affine_checks":pair_checks,
        "centered_J_drop_exact_checks":centered_checks,
        "psi_cap_checks":cap_checks,
        "max_numeric_psi_cap_violation":max_cap_violation,
        "exact_identities":[
            "after median-character centering, J-parent - average raw-child-I = 2 Pr_mu(i,j subset X)",
            "centered pair budget D_ij = 2 Pr_mu(i,j subset X) + average child recentering refund",
            "two quotient parameterizations give identical child spectral-mass multisets"
        ],
        "diagnostic_only":"entropy ratios and Psi cap use floating arithmetic and are not theorem certificates",
        "by_dimension":ratios
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
