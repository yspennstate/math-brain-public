#!/usr/bin/env python3
import math, itertools, json, hashlib

def xorv(*vecs):
    if not vecs:
        return ()
    n=len(vecs[0]); out=[0]*n
    for v in vecs:
        for i,b in enumerate(v):
            out[i]^=b
    return tuple(out)

def zero(N): return (0,)*N

def span(gens,N):
    out=[]
    for mask in range(1<<len(gens)):
        v=[0]*N
        for j,g in enumerate(gens):
            if (mask>>j)&1:
                for i,b in enumerate(g): v[i]^=b
        out.append(tuple(v))
    return list(dict.fromkeys(out))

def rm1(n):
    N=1<<n
    gens=[tuple(1 for _ in range(N))]
    for i in range(n):
        gens.append(tuple((x>>i)&1 for x in range(N)))
    return span(gens,N)

def monomial(n,inds):
    N=1<<n
    return tuple(int(all((x>>i)&1 for i in inds)) for x in range(N))

def corr(phase):
    N=len(phase)
    return sum(1 if b==0 else -1 for b in phase)/N

def influences(phase,n):
    N=1<<n
    sig=[1 if b==0 else -1 for b in phase]
    ans=[]
    for i in range(n):
        c=sum(sig[x]!=sig[x^(1<<i)] for x in range(N))
        ans.append(c/N)
    return ans

def folded_J(phase,n):
    return sum(min(t,1-t) for t in influences(phase,n))

def gauge_min(phase,n):
    N=1<<n
    infl=influences(phase,n)
    linear=[]
    for i,t in enumerate(infl):
        if t>0.5:
            linear.append(monomial(n,[i]))
    return xorv(phase,*linear) if linear else phase

def phi_discrete(x,kernel):
    r=math.sqrt(max(0.0,x))
    return sum(w*(1-math.cos(s*r)) for s,w in kernel)

def q_from_S(S,active):
    q=zero(len(active[0]))
    for j,g in enumerate(active):
        if (S>>j)&1: q=xorv(q,g)
    return q

def avg_phi(q,P,phi):
    return sum(phi(corr(xorv(q,p))**2) for p in P)/len(P)

def F_terminal(S,active,P0,P1,phi):
    q=q_from_S(S,active)
    return avg_phi(q,P0,phi)-avg_phi(q,P1,phi)

def gate_delta(q,bf,g,P,phi):
    # Boolean-phase gate difference minus comparator gate difference.
    return (
        avg_phi(xorv(q,bf),P,phi)-avg_phi(xorv(q,bf,g),P,phi)
        -avg_phi(q,P,phi)+avg_phi(xorv(q,g),P,phi)
    )

def walsh_coeff(vals,R):
    m=(len(vals).bit_length()-1)
    return sum(vals[S]*((-1)**((S&R).bit_count())) for S in range(1<<m))/(1<<m)

def check_case(n,active,extra,kernel):
    N=1<<n
    P0=rm1(n)
    P1=P0 if extra is None else list(dict.fromkeys(P0+[xorv(p,extra) for p in P0]))
    bf=zero(N)
    for g in active: bf=xorv(bf,g)
    bf_g=gauge_min(bf,n)
    J=folded_J(bf_g,n)
    phi=lambda x: phi_discrete(x,kernel)
    m=len(active); allmask=(1<<m)-1
    vals=[F_terminal(S,active,P0,P1,phi) for S in range(1<<m)]
    Fminus=[0.5*(vals[S]-vals[S^allmask]) for S in range(1<<m)]

    # Exact terminal/local gate identity and its derived pointwise envelope.
    max_local_identity_err=0.0
    max_local_ratio=0.0
    L=sum(s*w for s,w in kernel)
    local_bound=2*L*L*J/N
    for S in range(1<<m):
        q=q_from_S(S,active)
        for j,g in enumerate(active):
            partial=0.5*(Fminus[S]-Fminus[S^(1<<j)])
            d0=gate_delta(q,bf,g,P0,phi)
            d1=gate_delta(q,bf,g,P1,phi)
            pred=-0.25*(d0-d1)
            max_local_identity_err=max(max_local_identity_err,abs(partial-pred))
            if local_bound>0:
                max_local_ratio=max(max_local_ratio,partial*partial/local_bound)

    # Parseval and L^{-1/2} parent aggregation.
    coeff={R:walsh_coeff(vals,R) for R in range(1<<m)}
    D=[vals[S^allmask]-vals[S] for S in range(1<<m)]
    source=sum(x*x for x in D)/(1<<m)
    parseval=4*sum(c*c for R,c in coeff.items() if R.bit_count()%2==1)
    sqrt_source=0.0
    raw_parent=0.0
    for j in range(m):
        for R,c in coeff.items():
            q=R.bit_count()
            if q%2==1 and ((R>>j)&1):
                sqrt_source += 4*c*c/q
                raw_parent += c*c
    global_bound=8*L*L*J
    global_ratio=source/global_bound if global_bound>0 else 0.0
    return {
        "n":n,"N":N,"active_count":m,"terminal_code_sizes":[len(P0),len(P1)],
        "J":J,"L":L,"source":source,"parseval":parseval,"sqrt_source":sqrt_source,
        "global_bound":global_bound,"global_ratio":global_ratio,
        "max_local_identity_err":max_local_identity_err,
        "max_local_ratio":max_local_ratio
    }

def main():
    kernels=[
        [(0.25,0.40),(0.80,0.35),(1.70,0.20)],
        [(0.10,0.25),(0.55,0.50),(2.40,0.10),(4.00,0.03)],
        [(0.35,0.60),(1.20,0.15),(3.10,0.04)],
    ]
    cases=[]
    # n=3: complete non-affine monomial quotient basis.
    n=3
    basis=[monomial(n,c) for d in range(2,n+1) for c in itertools.combinations(range(n),d)]
    for r in (2,3):
        for inds in itertools.combinations(range(len(basis)),r):
            active=[basis[i] for i in inds]
            extras=[basis[k] for k in range(len(basis)) if k not in inds]
            extra=extras[0] if extras else None
            for kernel in kernels:
                cases.append(check_case(n,active,extra,kernel))
    # n=4: deterministic spread of 4-active-coordinate cases.
    n=4
    basis=[monomial(n,c) for d in range(2,n+1) for c in itertools.combinations(range(n),d)]
    index_sets=[
        (0,1,2,3),(0,2,5,8),(1,4,7,10),(2,6,8,9),(3,5,9,10),
        (0,4,8,10),(1,3,6,9),(2,4,7,8)
    ]
    for inds in index_sets:
        active=[basis[i] for i in inds]
        extra=next(basis[k] for k in range(len(basis)) if k not in inds)
        for kernel in kernels:
            cases.append(check_case(n,active,extra,kernel))

    tol=2e-12
    assert all(c["max_local_identity_err"]<tol for c in cases)
    assert all(abs(c["source"]-c["parseval"])<tol for c in cases)
    assert all(abs(c["source"]-c["sqrt_source"])<tol for c in cases)
    assert all(c["max_local_ratio"]<=1+1e-10 for c in cases)
    assert all(c["global_ratio"]<=1+1e-10 for c in cases)

    out={
      "status":"PASS",
      "cases":len(cases),
      "max_local_identity_error":max(c["max_local_identity_err"] for c in cases),
      "max_local_bound_ratio":max(c["max_local_ratio"] for c in cases),
      "max_global_bound_ratio":max(c["global_ratio"] for c in cases),
      "max_parseval_error":max(abs(c["source"]-c["parseval"]) for c in cases),
      "max_sqrt_factorization_error":max(abs(c["source"]-c["sqrt_source"]) for c in cases),
      "notes":[
        "Finite discrete Borel kernels test the algebraic live-window theorem without quadrature.",
        "The all-dimensional proof is symbolic; these checks are falsification/self-check evidence only."
      ]
    }
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=="__main__":
    main()
