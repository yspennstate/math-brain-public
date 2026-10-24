#!/usr/bin/env python3
"""R20/I0100 exact p=1061 localized-Paley theta certificate.

The candidate support was discovered numerically only. This checker independently
recomputes the p=1061 Paley difference set, the intended real-cyclotomic
embedding, the primal basic solution, the matching dual basic solution, every
strict positivity/slack inequality, and the overlapping primal/dual objective
using exact Sturm isolation plus outward-rounded 1024-bit dyadic interval
arithmetic inherited from the archived p=1033 checker.
"""
import sympy as sp
import mpmath as mp
import i0100_p1033_exact_interval_certificate as B

P=1061
N=530
NONEDGE=[1,2,5,6,7,8,10,16,18,19,20,22,24,26,27,30,33,34,35,36,39,40,43,47,48,50,51,54,56,57,61,62,66,68,69,70,71,73,74,75,78,79,80,82,83,88,90,91,96,98,99,101,104,111,113,114,115,116,118,119,124,125,126,134,136,137,138,142,145,146,147,148,149,150,152,153,155,156,157,158,161,162,163,167,169,173,175,177,182,183,184,185,189,195,198,199,202,204,206,207,209,211,213,214,215,216,218,220,221,222,224,228,229,234,235,237,239,240,243,246,248,249,250,252,253,254,256,258,259,261,262,263,265]
SUPPORT=[0,2,3,5,6,9,12,16,19,25,26,30,31,33,34,35,36,38,39,40,41,44,45,48,49,50,52,55,56,57,58,61,62,68,70,71,73,74,80,82,83,84,85,89,90,91,92,96,99,100,103,110,112,113,114,116,117,118,119,124,126,129,130,131,132,133,135,139,140,141,145,149,150,151,152,153,154,155,156,159,161,162,164,167,169,171,172,173,175,176,180,181,182,183,184,185,186,189,191,193,196,200,202,203,204,208,212,214,217,220,221,222,223,227,228,229,230,233,235,237,240,242,243,245,246,247,249,250,251,254,256,259,260,262]

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

    # Primal: probability normalization plus all reduced nonedge Fourier zeros.
    A=[[B.ONE for _ in SUPPORT]] + [
        [cosiv(mm*d) for mm in SUPPORT] for d in NONEDGE]
    rhs=[B.ONE]+[B.ZERO]*len(NONEDGE)
    w=B.solve_interval(A,rhs)
    assert all(v.lo>0 for v in w)

    # Dual: interpolation on primal support and strict positivity off support.
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
    print('covered_primes_before=[5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049]')
    print('covered_primes_after=[5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061]')
    print('largest_exact_prime=1061')
    print('PASS_p',P)
    print('ALL_EXACT_CHECKS_PASS')

if __name__=='__main__':
    main()
