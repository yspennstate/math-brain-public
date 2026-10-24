#!/usr/bin/env python3
"""Independent numerical and small-source verification for REPORT.md.

Standard library only. The proofs in REPORT.md establish arbitrary depth.
"""
from decimal import Decimal as D, localcontext, getcontext
from fractions import Fraction
from math import ceil
import json

getcontext().prec = 160
LN2 = D(2).ln()
TOL = D("1e-85")


def close(x, y, name):
    error = abs(x-y)
    assert error <= TOL*(1+abs(x)+abs(y)), (name, str(error), str(x), str(y))


def log2(x):
    assert x > 0
    return x.ln()/LN2


def entropy_bernoulli(p):
    ans = D(0)
    if p:
        ans -= p*log2(p)
    if p != 1:
        ans -= (1-p)*log2(1-p)
    return ans


def negexp(x):
    # exp(-900) is below 1e-390. The discarded numerical tail is far below
    # the 1e-85 checking tolerance even after every finite factor used here.
    if x > 900:
        return D(0)
    return (-x).exp()


def log_active(x):
    """log2(1-exp(-x)); x is the exact reference empty-block exponent."""
    y = negexp(x)
    return (1-y).ln()/LN2 if y else D(0)


def root_c(N, r):
    # The tested generators satisfy I>=3/2, so the positive root is above1/2.
    lo, hi = D("0.5"), D(1)
    for _ in range(440):
        c = (lo+hi)/2
        empty = negexp(-D(N)*(1-c*r).ln())
        residual = 1-empty-c
        if residual > 0:
            lo = c
        else:
            hi = c
    return (lo+hi)/2


def fwht(values):
    out = list(values)
    step = 1
    while step < len(out):
        for base in range(0, len(out), 2*step):
            for j in range(step):
                x, y = out[base+j], out[base+j+step]
                out[base+j], out[base+j+step] = x+y, x-y
        step *= 2
    return out


def majority(bits):
    return 1 if sum(bits)>0 else -1


def generator(b):
    vals = [majority([1 if mask>>j&1 else -1 for j in range(b)])
            for mask in range(1<<b)]
    raw = fwht(vals)
    pi = {mask: Fraction(x*x, 1<<(2*b)) for mask, x in enumerate(raw) if x}
    assert 0 not in pi and sum(pi.values()) == 1
    marg = [sum(v for s,v in pi.items() if s>>j&1) for j in range(b)]
    assert len(set(marg)) == 1
    mu = sum(marg)
    h = -sum((D(q.numerator)/D(q.denominator))*log2(D(q.numerator)/D(q.denominator))
             for q in pi.values())
    return dict(b=b, pi=pi, mu=D(mu.numerator)/D(mu.denominator), h=h)


def formulas(g, m):
    b, mu, h = g["b"], g["mu"], g["h"]
    alpha = mu/D(b)
    N = b**m
    I = mu**m
    r = alpha**m
    c = root_c(N, r)
    t = c*r
    ell_nat = -(1-t).ln()
    ell = ell_nat/LN2
    ds = {}
    for j in range(1, m+1):
        lu = log_active(D(b**(j-1))*ell_nat)
        lv = log_active(D(b**j)*ell_nat)
        d = lv - mu*lu + (D(b)-mu)*D(b**(j-1))*ell - h
        assert d >= -TOL
        ds[j] = d
    Ksum = sum(mu**(m-j)*ds[j] for j in ds)
    Hmax = (D(N)*entropy_bernoulli(t)-entropy_bernoulli(c))/c
    H = h*(I-1)/(mu-1)
    close(Ksum, Hmax-H, ("fullKL", b, m))
    A = max(D(0), log2(D(b))-h)
    return dict(g=g,m=m,N=N,I=I,r=r,c=c,t=t,ell=ell,ds=ds,K=Ksum,
                Hmax=Hmax,H=H,A=A)


def loss(x, L, M):
    mu, m = x["g"]["mu"], x["m"]
    if L >= M:
        return D(0)
    return sum(mu**(m-j)*x["ds"][j] for j in range(L+1,M+1))


def bound(x, L, M):
    if L >= M:
        return D(0)
    b,mu=x["g"]["b"],x["g"]["mu"]
    z=D(b)/mu
    return ((x["I"]*mu**(-L)-mu**(x["m"]-M))
            *(log2(1/x["t"])+x["A"]/(mu-1))
            +x["I"]*x["ell"]*(z**M-z**L))


def ceil_log(x, base):
    return int((x.ln()/base.ln()).to_integral_value(rounding="ROUND_CEILING"))


def small_direct_check(g):
    # A genuine depth-two majority truth table on nine original variables.
    vals=[]
    for mask in range(1<<9):
        children=[]
        for a in range(3):
            children.append(majority([1 if mask>>(3*a+j)&1 else -1 for j in range(3)]))
        vals.append(majority(children))
    raw=fwht(vals)
    P={s:D(v*v)/D(1<<18) for s,v in enumerate(raw) if v}
    assert 0 not in P
    assert sum(P.values()) == 1
    close(sum(D(s.bit_count())*p for s,p in P.items()),D(9)/4,"directI")
    close(-sum(p*log2(p) for p in P.values()),D(5),"directH")
    x=formulas(g,2)
    t,c=x["t"],x["c"]
    u=1-(1-t)**3
    qtilde_total=D(0)
    K=D(0)
    var=D(0)
    for S in range(1,1<<9):
        k=S.bit_count()
        q=t**k*(1-t)**(9-k)/c
        blocks=[(S>>(3*a))&7 for a in range(3)]
        nactive=sum(bool(v) for v in blocks)
        qt=u**nactive*(1-u)**(3-nactive)/c
        for block in blocks:
            if block:
                frac=g["pi"].get(block,Fraction(0))
                qt *= D(frac.numerator)/D(frac.denominator)
        qtilde_total+=qt
        if S in P:
            p=P[S]
            assert qt>0
            K+=p*log2(p/q)
            var+=p*log2(qt/q)
    close(qtilde_total,D(1),"hybridNormalization")
    close(K,x["K"],"directKL")
    close(var,g["mu"]*x["ds"][1],"directVariational")
    assert var<=K+TOL
    return {"direct_truth_table_entries":512,"hybrid_nonempty_sets_checked":511,
            "hybrid_total":str(qtilde_total),"K":str(K),"retained_bottom_one":str(var)}


def main():
    gs=[generator(3),generator(5)]
    close(gs[0]["mu"],D(3)/2,"RMmu")
    close(gs[0]["h"],D(2),"RMh")
    close(gs[1]["mu"],D(15)/8,"MAJ5mu")
    output={"status":"PASS","generators":[],"examples":[]}
    checks=0
    for g in gs:
        output["generators"].append({"arity":g["b"],"mu":str(g["mu"]),"entropy":str(g["h"])})
        for m in [1,2,3,4,6,8,11,16,24,32,64,128]:
            x=formulas(g,m)
            choices=sorted(set([0,1,m//3,m//2,max(0,m-2),m]))
            for L in choices:
                for M in choices:
                    if L<M:
                        actual=loss(x,L,M)
                        upper=bound(x,L,M)
                        assert actual<=upper+TOL*(1+abs(upper)),("remainder",g["b"],m,L,M)
                        checks+=1
            eps=D(1)/4
            alpha=g["mu"]/D(g["b"])
            if x["I"]<2 or x["r"]>D("0.5"):
                L,K=m,0
            else:
                a=D(m)*log2(1/alpha)+1+x["A"]/(g["mu"]-1)
                L=ceil_log(2*a/eps,g["mu"])
                K=ceil_log(4/(eps*LN2),1/alpha)
            omitted=loss(x,min(m,L),max(0,m-K))
            assert omitted<=eps*x["I"]+TOL
            retained=x["K"]-omitted
            C=g["h"]/(g["mu"]-1)+2*eps
            assert retained>=x["Hmax"]-C*(x["I"]-1)-TOL*(1+x["Hmax"])
            if g["b"]==3:
                L0=min(m,ceil_log(D(4*(m+1)),g["mu"]))
                omitted0=loss(x,L0,m)
                assert omitted0<=2*(x["I"]-1)+TOL
                assert x["K"]-omitted0>=x["Hmax"]-6*(x["I"]-1)-TOL*(1+x["Hmax"])
                if m>=16:
                    maxL=int(D(m)/(2*log2(D(3))))
                    for testL in [0,1,min(maxL,m//4),maxL]:
                        assert loss(x,testL,m)>=D(m)*x["I"]/(8*g["mu"]**(testL+1))-TOL
            else:
                L0,omitted0=None,None
            if m in [16,32,64,128]:
                output["examples"].append({
                    "arity":g["b"],"depth":m,"I":str(x["I"]),
                    "bottom_heights":min(m,L),"top_heights":min(m,K),
                    "epsilon":str(eps),"actual_loss_over_I":str(omitted/x["I"]),
                    "K_over_I":str(x["K"]/x["I"]),
                    "bottom_only_L_for_center6":L0,
                    "bottom_only_loss_over_I":str(omitted0/x["I"]) if omitted0 is not None else None
                })
    output["finite_remainder_checks"]=checks
    output["independent_walsh_hybrid_check"]=small_direct_check(gs[0])
    print(json.dumps(output,indent=2))

if __name__=="__main__":
    main()

