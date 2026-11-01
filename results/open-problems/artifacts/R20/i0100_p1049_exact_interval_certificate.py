#!/usr/bin/env python3
"""R20/I0100 exact p=1049 localized-Paley theta certificate.

This checker reuses the interval-arithmetic primitives of the already archived
p=1033 checker.  It independently recomputes the p=1049 Paley difference set,
real-cyclotomic embedding, primal basic solution, dual basic solution, all
strict positivity/slack inequalities, and matching primal/dual objective.
"""
import sympy as sp
import mpmath as mp
import i0100_p1033_exact_interval_certificate as B

P=1049
N=524
NONEDGE=[3,4,6,10,12,13,14,15,22,24,27,28,31,32,33,34,36,39,41,43,44,51,53,55,56,57,60,62,64,66,67,68,70,72,73,74,77,78,80,82,83,86,90,91,92,93,96,98,99,100,103,105,106,107,111,112,113,114,115,116,118,122,123,125,126,127,129,130,131,135,137,143,144,147,148,149,150,153,154,157,159,160,161,165,169,171,174,175,176,179,180,184,187,189,192,194,195,196,197,198,199,200,201,202,203,204,207,211,212,213,214,216,217,218,222,225,227,232,235,238,244,245,246,247,249,251,252,255,257,258,260]
SUPPORT=[0,1,2,3,4,7,9,11,12,14,15,20,22,23,24,25,26,28,30,31,33,34,35,41,43,44,48,52,54,55,56,57,58,60,61,62,66,67,68,71,72,74,76,77,78,82,83,87,89,90,91,93,95,97,100,103,104,105,106,107,110,112,115,118,119,122,124,125,126,127,130,135,136,138,139,143,144,148,151,152,153,155,160,161,162,166,173,178,180,181,182,184,186,190,192,193,195,197,199,200,201,206,207,209,211,212,215,220,221,222,223,224,225,227,228,229,232,233,234,237,239,242,243,246,249,250,251,252,253,258,259,262]

def main():
    assert sp.isprime(P) and P % 4 == 1
    n, nchk = B.reduced_nonedge_diffs(P)
    assert n == N and nchk == NONEDGE
    assert len(SUPPORT) == len(NONEDGE) + 1

    x=sp.Symbol('x')
    K=sp.QQ.algebraic_field(2*sp.cos(2*sp.pi/n))
    minpoly=sp.Poly.from_list(
        [sp.Rational(int(q.numerator),int(q.denominator)) for q in K.mod.to_list()],
        gens=x)

    mp.mp.dps=180
    approx=2*mp.cos(2*mp.pi/n)
    ten=10**145
    lo_num=int(mp.floor(approx*ten)); hi_num=lo_num+1
    alo=sp.Rational(lo_num,ten); ahi=sp.Rational(hi_num,ten)
    assert minpoly.count_roots(alo,ahi)==1
    assert minpoly.count_roots(ahi,sp.oo)==0
    alpha=B.IV(B.from_rat(alo).lo,B.from_rat(ahi).hi)

    C=[B.ZERO]*(n//2+1)
    C[0]=B.TWO; C[1]=alpha
    for mm in range(1,n//2):
        C[mm+1]=alpha*C[mm]-C[mm-1]
    COS=[B.half(C[mm]) for mm in range(n//2+1)]
    def cosiv(mm):
        mm%=n; mm=min(mm,n-mm); return COS[mm]

    # Primal basic solution: probability normalization plus all nonedge
    # Fourier vanishing constraints.  The source theta value is n*w_0.
    A=[[B.ONE for _ in SUPPORT]] + [
        [cosiv(mm*d) for mm in SUPPORT] for d in NONEDGE]
    rhs=[B.ONE]+[B.ZERO]*len(NONEDGE)
    w=B.solve_interval(A,rhs)
    assert all(v.lo>0 for v in w)

    # Matching dual basic solution and strict slacks on every nonsupport
    # half-frequency.
    AT=[[A[j][i] for j in range(len(A))] for i in range(len(A))]
    dual_rhs=[B.ONE if mm==0 else B.ZERO for mm in SUPPORT]
    y=B.solve_interval(AT,dual_rhs)
    a=y[0]; lam=y[1:]
    slacks=[]
    for mm in range(n//2+1):
        if mm in SUPPORT:
            continue
        q=a
        for coeff,d in zip(lam,NONEDGE):
            q=q+coeff*cosiv(mm*d)
        assert q.lo>0,('dual slack',mm,q.lo,q.hi,B.digits10_width(q))
        slacks.append(q)

    w0=w[SUPPORT.index(0)]
    assert not (w0.hi<a.lo or a.hi<w0.lo)
    theta=B.IV(n*w0.lo,n*w0.hi)
    target=sp.sqrt(sp.Rational(P,2))
    overshoot=2*theta.lo*theta.lo > P*B.SCALE*B.SCALE

    print('I0100 exact certificate')
    print('p',P,'n',n,'field_degree',minpoly.degree(),'bits',B.BITS)
    print('nonedge_half_constraints',len(NONEDGE))
    print('strict_positive_primal_half_weights',len(w))
    print('strict_positive_nonsupport_half_slacks',len(slacks))
    print('theta_interval_mid',B.dec(theta))
    print('sqrt_p_over_2',sp.N(target,45))
    print('ratio_mid',sp.N(sp.Rational(theta.mid(),B.SCALE)/target,40))
    print('w0_digits',B.digits10_width(w0),'a_digits',B.digits10_width(a))
    print('min_weight',B.dec(min(w,key=lambda z:z.lo),30))
    print('min_slack',B.dec(min(slacks,key=lambda z:z.lo),30))
    print('certified_theta_gt_sqrt_p_over_2',overshoot)
    print('covered_primes_before=[5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033]')
    print('covered_primes_after=[5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049]')
    print('largest_exact_prime=1049')
    print('PASS_p',P)
    print('ALL_EXACT_CHECKS_PASS')

if __name__=='__main__':
    main()
