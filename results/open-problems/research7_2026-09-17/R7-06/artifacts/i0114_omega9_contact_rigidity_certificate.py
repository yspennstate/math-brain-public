#!/usr/bin/env python3
"""Exact finite certificate for the 3x3 triangular-torus contact framework.

For the 9-point configuration (1/3)A2/A2, Fourier characters are indexed by
(k,l) in (Z/3Z)^2.  The three nearest-neighbor step classes are
(1,0), (0,1), (-1,1), with unit directions n1,n2,n3 at 60 degree angles.
This script verifies exactly that every nontranslation Fourier mode activates
at least two nonparallel constraints, hence the contact framework is
infinitesimally rigid modulo translations.  It also computes the sharp modewise
coercivity ratio min eig(sum s_j n_j n_j^T)/sum s_j = 1/4, where each active
third-root phase contributes |omega^m-1|^2=3.
"""
import sympy as sp

sqrt3 = sp.sqrt(3)
ns = [sp.Matrix([1,0]), sp.Matrix([sp.Rational(1,2), sqrt3/2]), sp.Matrix([-sp.Rational(1,2), sqrt3/2])]
rows=[]
ratios=[]
for k in range(3):
    for l in range(3):
        if k==0 and l==0:
            continue
        phases=[k%3,l%3,(l-k)%3]
        active=[j for j,m in enumerate(phases) if m!=0]
        assert len(active)>=2
        nonparallel=False
        for i in range(len(active)):
            for j in range(i+1,len(active)):
                a,b=ns[active[i]],ns[active[j]]
                det=sp.simplify(a[0]*b[1]-a[1]*b[0])
                if det!=0:
                    nonparallel=True
        assert nonparallel
        M=sp.zeros(2)
        for j in active:
            M += 3*(ns[j]*ns[j].T)
        tr=sp.simplify(sp.trace(M)); det=sp.simplify(M.det())
        lam=sorted([sp.simplify(v) for v in M.eigenvals().keys()], key=lambda z: float(z))
        lmin=lam[0]
        total=3*len(active)
        ratio=sp.simplify(lmin/total)
        ratios.append(ratio)
        rows.append(((k,l), tuple(active), M, lmin, ratio, tr, det))

assert min(ratios, key=lambda z: float(z)) == sp.Rational(1,4)
print('EXACT_CHECK_PASS')
for mode,active,M,lmin,ratio,tr,det in rows:
    print('mode=',mode,'active=',active,'M=',M.tolist(),'lambda_min=',lmin,'ratio=',ratio,'tr=',tr,'det=',det)
print('GLOBAL_COERCIVITY_RATIO=1/4')
print('INF_RIGID_MOD_TRANSLATIONS=TRUE')
