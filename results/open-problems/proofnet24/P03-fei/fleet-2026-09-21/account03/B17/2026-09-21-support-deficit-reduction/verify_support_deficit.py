#!/usr/bin/env python3
"""Deterministic checks for the B17 FEI support-deficit route.

No claim in this file is a proof of full FEI. Universal statements in REPORT.md
are proved algebraically there; these checks stress-test the proposed stronger
set inequality and exact counterexamples.
"""
import itertools, json, math

C_HOD = 6.4547837

def fwht(a):
    a = [float(x) for x in a]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def entropy(p):
    return -sum(x*math.log2(x) for x in p if x > 0.0)

def partial_metrics(vals):
    N = len(vals)
    delta = sum(float(v*v) for v in vals)/N
    if delta == 0:
        return None
    coeff = [x/N for x in fwht(vals)]
    mu = [x*x/delta for x in coeff]
    H = entropy(mu)
    I = sum(s.bit_count()*mu[s] for s in range(N))
    L = math.log2(1.0/delta)
    U = H-L
    E = I-L/2.0
    R = None if E <= 1e-12 else U/E
    return dict(delta=delta,H=H,I=I,L=L,U=U,E=E,R=R,
                defect_at_hod=U-C_HOD*E)

def indicator_from_mask(mask, n):
    return [1.0 if (mask >> x) & 1 else 0.0 for x in range(1 << n)]

def support(mask, n):
    return [x for x in range(1 << n) if (mask >> x) & 1]

def compress_mask(mask, n, i):
    out = mask
    for x in range(1 << n):
        if (x >> i) & 1:
            continue
        y = x | (1 << i)
        ax, ay = (mask >> x) & 1, (mask >> y) & 1
        if ax + ay == 1:
            out |= 1 << x
            out &= ~(1 << y)
    return out

def spectral_mu_boolean(vals):
    N = len(vals)
    c = [x/N for x in fwht(vals)]
    return [x*x for x in c]

def projection_entropy(mu, mask):
    probs = {}
    for s,w in enumerate(mu):
        key = s & mask
        probs[key] = probs.get(key,0.0) + w
    return entropy(probs.values())

def shapley_entropy(mu, n):
    Hproj = [projection_entropy(mu,A) for A in range(1<<n)]
    nf = math.factorial(n)
    phi=[]
    for i in range(n):
        bit=1<<i
        x=0.0
        for A in range(1<<n):
            if A & bit:
                continue
            k=A.bit_count()
            wt=math.factorial(k)*math.factorial(n-k-1)/nf
            x += wt*(Hproj[A|bit]-Hproj[A])
        phi.append(x)
    return phi,Hproj[-1]

def boolean_metrics(vals):
    mu=spectral_mu_boolean(vals)
    H=entropy(mu)
    I=sum(s.bit_count()*mu[s] for s in range(len(vals)))
    inf=[sum(mu[s] for s in range(len(vals)) if (s>>i)&1)
         for i in range((len(vals).bit_length()-1))]
    return H,I,inf,mu

def main():
    out = {"constant_tested": C_HOD}

    indicator = {}
    for n in range(1,5):
        N=1<<n
        best_all=(-1.0,None,None)
        best_half=(-1.0,None,None)
        max_defect=-1e300
        for mask in range(1,1<<N):
            m=partial_metrics(indicator_from_mask(mask,n))
            max_defect=max(max_defect,m["defect_at_hod"])
            if m["R"] is not None and m["R"] > best_all[0]:
                best_all=(m["R"],mask,m)
            if mask.bit_count() <= N//2 and m["R"] is not None and m["R"] > best_half[0]:
                best_half=(m["R"],mask,m)
        indicator[str(n)] = {
            "nonempty_sets": (1<<N)-1,
            "max_defect_at_hod": max_defect,
            "best_ratio_all": None if best_all[1] is None else {
                "ratio":best_all[0],"mask":best_all[1],"support":support(best_all[1],n),"metrics":best_all[2]},
            "best_ratio_density_at_most_half": None if best_half[1] is None else {
                "ratio":best_half[0],"mask":best_half[1],"support":support(best_half[1],n),"metrics":best_half[2]},
        }
    out["indicator_exhaustive"] = indicator

    ternary={}
    for n in range(1,4):
        N=1<<n
        count=0
        best=(-1.0,None,None)
        max_defect=-1e300
        for vals in itertools.product((-1,0,1), repeat=N):
            if all(v==0 for v in vals):
                continue
            count += 1
            m=partial_metrics(vals)
            max_defect=max(max_defect,m["defect_at_hod"])
            if m["R"] is not None and m["R"]>best[0]:
                best=(m["R"],vals,m)
        ternary[str(n)] = {
            "nonzero_functions":count,
            "max_defect_at_hod":max_defect,
            "best_ratio":None if best[1] is None else {"ratio":best[0],"values":list(best[1]),"metrics":best[2]},
        }
    out["ternary_partial_exhaustive"]=ternary

    lex=[]
    for n in range(3,13):
        N=1<<n
        choices=sorted(set((max(1,N//3), min(N-1,N//3+1))))
        candidates=[]
        for k in choices:
            vals=[1.0 if x<k else 0.0 for x in range(N)]
            m=partial_metrics(vals)
            candidates.append(((-1 if m["R"] is None else m["R"]),k,m))
        _,k,m=max(candidates,key=lambda z:z[0])
        lex.append({"n":n,"support_size":k,"density":m["delta"],"ratio":m["R"],"U":m["U"],"E":m["E"]})
    out["lex_near_one_third"]=lex
    out["one_third_staircase_limit"]={
        "H":4/3+math.log2(3), "I":1.0, "L":math.log2(3), "U":4/3,
        "E":1-math.log2(3)/2, "ratio":8/(3*(2-math.log2(3)))}

    compression=[]
    for mask,i in ((408,3),(1641,0)):
        cm=compress_mask(mask,4,i)
        compression.append({"mask":mask,"support":support(mask,4),"coordinate":i,
            "before":partial_metrics(indicator_from_mask(mask,4)),
            "compressed_mask":cm,"compressed_support":support(cm,4),
            "after":partial_metrics(indicator_from_mask(cm,4))})
    out["compression_counterexamples"]=compression

    neg = [2,3,6,7,8,11,12,15,16,17,19,20,21,23,32,36,40,41,44,45,
           48,49,50,51,52,53,55,57,58,61,62,64,66,67,68,70,71,82,86,
           91,95,96,98,100,102,105,106,107,109,110,111,113,117,121,
           123,125,127]
    negset=set(neg)
    vals=[-1.0 if x in negset else 1.0 for x in range(128)]
    H,I,inf,mu=boolean_metrics(vals)
    phi,H2=shapley_entropy(mu,7)
    ratios=[phi[i]/inf[i] if inf[i]>0 else None for i in range(7)]
    out["shapley_counterexample"]={
        "negative_vertices":neg,"H":H,"I":I,"global_H_over_I":H/I,
        "influences":inf,"shapley_entropy_contributions":phi,
        "sum_phi":sum(phi),"max_coordinate":max(range(7),key=lambda i:ratios[i]),
        "ratios":ratios,"max_ratio":max(x for x in ratios if x is not None),
        "entropy_chain_identity_error":abs(H-H2)}

    print(json.dumps(out,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
