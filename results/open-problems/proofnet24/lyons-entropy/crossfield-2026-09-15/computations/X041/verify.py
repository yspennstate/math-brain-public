"""X041: exact six-site tensor-lift certificate; high-precision entropy checks."""
from pathlib import Path
from itertools import product
import json
import sympy as s
import mpmath as mp
out = Path(__file__).resolve().parent
Q=s.Rational; I=s.I; t=s.symbols('t', real=True)
K0=s.Matrix([[Q(2,5),Q(1,20),Q(1,25)],
             [Q(1,20),Q(1,2),Q(1,30)],
             [Q(1,25),Q(1,30),Q(3,5)]])
k=K0[1:,0]; w=s.Matrix([I/30,Q(1,40)])
d=-Q(1,10); lam=s.Integer(1); F=k*k.H
A=s.zeros(3); A[0,0]=d; A[1:,0]=w; A[0,1:]=w.H; A[1:,1:]=F
Kt=K0+t*A
checks=0
def check(v):
    global checks
    assert bool(v), v
    checks+=1
def zer(v): check(s.simplify(v)==0)
def margins(M):
    lo=[]; hi=[]
    for i in range(M.rows):
        rad=sum(abs(s.re(M[i,j]))+abs(s.im(M[i,j]))
                for j in range(M.cols) if j!=i)
        lo.append(s.simplify(M[i,i]-rad))
        hi.append(s.simplify(1-M[i,i]-rad))
    check(all(x>0 for x in lo+hi))
    return {'lower':list(map(str,lo)),'upper':list(map(str,hi))}
marg={'K0':margins(K0),'K1':margins(K0+A),
      'R_plus_3F':margins(K0[1:,1:]+3*F)}
check(lam*d<0); check(A.det()<0)
J=s.ones(2); V=s.Matrix([[1,-1],[-1,1]])/6
physical=s.diag(V,V,V)+s.kronecker_product(Kt,J)/2
physical_A=s.kronecker_product(A,J)/2
check(physical_A.rank()==3)
for j in range(6):
    inds=[i for i in range(6) if i!=j]
    check(physical_A.extract(inds,inds).rank()==3)
bits=list(product((0,1),repeat=3))
def atoms(M):
    n=M.rows
    return {b:s.factor((-1)**(n-sum(b))*
                     (M-s.diag(*[1-x for x in b])).det(method='domain-ge'))
            for b in product((0,1),repeat=n)}
p=atoms(Kt)
zer(sum(p.values())-1)
check(max(s.degree(v,t) for v in p.values())==3)
# Block channel order: empty, first, second, both.
C=[[Q(2,3),Q(1,6),Q(1,6),0],
   [0,Q(1,3),Q(1,3),Q(1,3)]]
for x in (0,1): zer(sum(C[x])-1)
ys=list(product(range(4),repeat=3))
q={y:s.factor(sum(p[b]*s.prod(C[b[i]][y[i]] for i in range(3))
                         for b in bits)) for y in ys}
zer(sum(q.values())-1)
# Four exact values prove the degree<=3 atom identity throughout the line.
for tv in (Q(0),Q(1,3),Q(2,3),Q(1)):
    mat=physical.subs(t,tv)
    for y in ys:
        b=tuple(z for local in y for z in ((local&1),((local>>1)&1)))
        val=(-1)**(6-sum(b))*(mat-s.diag(*[1-x for x in b])).det(method='domain-ge')
        zer(val-q[y].subs(t,tv))
# Aggregate the two identical singleton groups: E selects slope 1/2.
groups=[]
for e in bits:
    sigma=[Q(1,2) if z else Q(1) for z in e]
    rho=[Q(1,2) if z else Q(0) for z in e]
    wt=s.prod(Q(2,3) if z else Q(1,3) for z in e)
    gp={}
    for b in bits:
        shifted=Kt+s.diag(*[(rho[i]-(1-b[i]))/sigma[i] for i in range(3)])
        gp[b]=s.factor((-1)**(3-sum(b))*s.prod(sigma)*shifted.det())
    zer(sum(gp.values())-1)
    groups.append((wt,gp))
zer(sum(wt for wt,_ in groups)-1)
# The split law for the empty output gives an affine nonnegative correction.
tau=Q(2,3); eta=Q(1,2)
zer(Q(1,3)*Q(1,2)**2*2+Q(1,3)-eta)
mp.mp.dps=70
def num(x): return mp.mpf(str(s.N(s.re(x),80)))
def data(polys,tv):
    H=mp.mpf(0); FI=mp.mpf(0); accel=mp.mpf(0)
    for poly in polys.values():
        a=num(poly.subs(t,tv)); b=num(s.diff(poly,t).subs(t,tv))
        c=num(s.diff(poly,t,2).subs(t,tv))
        check(a>0)
        H-=a*mp.log(a); FI+=b*b/a; accel+=c*mp.log(a)
    return H,FI,FI+accel,accel
numeric=[]
for tv in (Q(0),Q(1,2),Q(1)):
    ho,io,co,ao=data(q,tv)
    gh=gi=gc=ga=mp.mpf(0)
    for wt,polys in groups:
        h,fi,curv,accel=data(polys,tv); ww=num(wt)
        gh+=ww*h; gi+=ww*fi; gc+=ww*curv; ga+=ww*accel
        check(curv>=fi-mp.mpf('1e-60'))
    corr=num(3-s.trace(Kt.subs(t,tv)))*mp.log(2)
    predicted=3*mp.log(3)+gh-corr
    errors=[abs(ho-predicted),abs(io-gi),abs(co-gc),abs(ao-ga)]
    check(max(errors)<mp.mpf('1e-60'))
    check(co>=num(4*eta*d*d))
    numeric.append({'t':str(tv),'entropy':mp.nstr(ho,25),
                    'minus_H_second':mp.nstr(co,25),
                    'Fisher':mp.nstr(io,25),
                    'max_identity_error':mp.nstr(max(errors),5)})
certificate={'status':'exact identities and finite-example checks only',
 'exact_and_numeric_assertions':checks,'seed_direction_determinant':str(A.det()),
 'seed_contraction_margins':marg,
 'physical_sites':6,'physical_direction_rank':3,
 'every_single_site_complement_direction_rank':3,
 'channel_total_variation':str(tau),'refinement_second_slope_moment':str(eta),
 'proved_chord_improvement_coefficient':str(2*eta*d*d),
 'numeric_illustrations':numeric}
(out/'certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(certificate,indent=2))
