#!/usr/bin/env python3
"""Falsification checks for the EQ_d full-boundary-collar derivation.

This checks algebraic identities and finite numerical instances only.  It does not
prove FEI or replace the analytic boundary argument in REPORT.md.
"""
import math, random


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)


def phi_basis(bit,p):
    q=1-p
    return math.sqrt(q/p) if bit else -math.sqrt(p/q)


def spectrum_eq(p):
    d=len(p); P=math.prod(p); Q=math.prod(1-x for x in p); r=P+Q
    masses=[]
    for mask in range(1<<d):
        if mask==0:
            a=1-2*r
        else:
            a=0.0
            prod0=prod1=1.0
            for i in range(d):
                if mask>>i & 1:
                    prod0*=phi_basis(0,p[i]); prod1*=phi_basis(1,p[i])
            a=-2*(Q*prod0+P*prod1)
        masses.append(a*a)
    return masses


def spectrum_corner(p, corner_one):
    d=len(p)
    prob=math.prod(p) if corner_one else math.prod(1-x for x in p)
    masses=[]
    for mask in range(1<<d):
        if mask==0:
            a=1-2*prob
        else:
            prod=1.0
            for i in range(d):
                if mask>>i & 1:
                    prod*=phi_basis(1 if corner_one else 0,p[i])
            a=-2*prob*prod
        masses.append(a*a)
    return masses


def entropy(mu):
    return sum(-x*math.log2(x) for x in mu if x>0)


def generic_gamma(x):
    # Smooth symmetric positive test potential; only used to check decomposition.
    y=min(x,1-x)
    return 4.2*y*math.log2(1/y)+0.3*x*(1-x) if y>0 else 0.0


def defect_eq(p,gamma):
    P=math.prod(p); Q=math.prod(1-x for x in p)
    H=entropy(spectrum_eq(p))
    rhs=0.0
    for i,pi in enumerate(p):
        pm=math.prod(p[j] for j in range(len(p)) if j!=i)
        qm=math.prod((1-p[j]) for j in range(len(p)) if j!=i)
        rhs+=(pm+qm)*(gamma(pi)+h2(4*pi*(1-pi)))
    return rhs-gamma(P+Q)-H


def defect_corner(p,gamma,one):
    prob=math.prod(p) if one else math.prod(1-x for x in p)
    H=entropy(spectrum_corner(p,one))
    rhs=0.0
    for i,pi in enumerate(p):
        coef=math.prod((p[j] if one else 1-p[j]) for j in range(len(p)) if j!=i)
        rhs+=coef*(gamma(pi)+h2(4*pi*(1-pi)))
    return rhs-gamma(prob)-H


def fannes_bound(delta,n):
    if delta<=0: return 0.0
    # Standard finite-alphabet form, valid for delta<=1-1/n; our tests are tiny.
    return h2(delta)+delta*math.log2(n-1)


def main():
    rng=random.Random(240413)
    max_decomp=0.0
    max_entropy_excess=0.0
    cases=0
    for d in range(3,8):
        N=1<<d
        for _ in range(300):
            # Force P,Q simultaneously small but allow extreme unequal ratios.
            p=[10**rng.uniform(-3.7,-0.35) for _ in range(d)]
            if rng.random()<0.5:
                # mixed face: some coordinates near one
                for i in rng.sample(range(d), rng.randint(1,d-1)):
                    p[i]=1-10**rng.uniform(-3.7,-0.35)
            P=math.prod(p); Q=math.prod(1-x for x in p)
            if P+Q>=0.2: continue
            de=defect_eq(p,generic_gamma)
            da=defect_corner(p,generic_gamma,True)
            db=defect_corner(p,generic_gamma,False)
            HE=entropy(spectrum_eq(p)); HA=entropy(spectrum_corner(p,True)); HB=entropy(spectrum_corner(p,False))
            identity=da+db+generic_gamma(P)+generic_gamma(Q)-generic_gamma(P+Q)-(HE-HA-HB)
            max_decomp=max(max_decomp,abs(de-identity))

            muA=spectrum_corner(p,True); muB=spectrum_corner(p,False); muE=spectrum_eq(p)
            X=4*P*(1-P); Y=4*Q*(1-Q)
            if X+Y<1:
                nu=[0.0]*N
                nu[0]=1-X-Y
                for s in range(1,N): nu[s]=muA[s]+muB[s]
                l1=sum(abs(muE[s]-nu[s]) for s in range(N))
                delta=0.5*l1
                excess=HE-entropy(nu)-fannes_bound(delta,N)
                max_entropy_excess=max(max_entropy_excess,excess)
            cases+=1

    # Hierarchical two-corner scale: Fannes cost / potential mixing tends to zero.
    A=4.9096
    ratios=[]
    for k in (6,8,10,12,14):
        M=2.0**(-k); m=2.0**(-2*k)
        r=M+m
        mix=A*r*h2(m/r)
        delta=min(0.49,(2**7)*M*m)  # d=5: 2^(d+2) P Q
        omega=fannes_bound(delta,1<<5)
        ratios.append(omega/mix)

    # One-active-coordinate currency asymptotic W_N/nu -> t(1-t).
    t=0.37; vals=[]
    d=5
    for k in (6,8,10,12,14):
        nu=2.0**(-k)
        rest=[nu/(d-1)]*(d-1)
        p=[t]+rest
        Q=math.prod(1-x for x in p); s=sum(p)
        W=Q*(s-(1-Q))
        vals.append(W/nu)

    assert max_decomp < 2e-12
    assert max_entropy_excess < 2e-12
    assert all(ratios[i+1] < ratios[i] for i in range(len(ratios)-1))
    assert abs(vals[-1]-t*(1-t)) < 2e-4
    print("PASS")
    print(f"cases={cases}")
    print(f"max_decomposition_residual={max_decomp:.3e}")
    print(f"max_entropy_interaction_minus_Fannes={max_entropy_excess:.3e}")
    print("hierarchical_error_over_mixing=" + ",".join(f"{x:.6g}" for x in ratios))
    print("one_active_W_over_nu=" + ",".join(f"{x:.8f}" for x in vals))
    print(f"one_active_target={t*(1-t):.8f}")

if __name__=="__main__":
    main()
