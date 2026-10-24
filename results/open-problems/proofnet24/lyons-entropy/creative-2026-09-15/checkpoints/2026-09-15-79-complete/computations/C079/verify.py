"""Exact C079 proof constants, phase identities and rational complex samples.

Run from the campaign root: python computations/C079/verify.py
Only the explicitly labeled full-Hessian diagnostic uses floating point.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json
import sympy as sp

OUT = Path(__file__).resolve().parent
checks = 0

def check(x):
    global checks
    assert x
    checks += 1

def log_bounds(q, n=30):
    """Rational atanh-series enclosure, valid for every positive rational q."""
    q=F(q)
    if q < 1:
        lo,hi=log_bounds(1/q,n)
        return -hi,-lo
    z=(q-1)/(q+1)
    lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    tail=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return lo,lo+tail

def sb(q):
    return sp.Rational(q.numerator,q.denominator)

def fq(q):
    q=sp.Rational(q)
    return F(int(q.p),int(q.q))

def outward_sum(terms):
    lo=hi=F(0)
    for c,q in terms:
        a,b=log_bounds(q)
        if c<0: a,b=b,a
        lo+=c*a; hi+=c*b
    return lo,hi

def display(interval):
    return {"lower":str(interval[0]),"upper":str(interval[1]),
            "decimal_lower":float(interval[0]),"decimal_upper":float(interval[1])}

# Exact Laurent phase polynomials, with all three independent phases retained.
r,za,zb,zc=sp.symbols('r za zb zc',nonzero=True)
Q=sp.Matrix([[0,1,1,1],[1,0,za,-zb],
             [1,1/za,0,zc],[1,-1/zb,1/zc,0]])
L=sp.eye(4)+r*Q
C=lambda z:(z+1/z)/2
tri=list(combinations(range(4),3))
tc=[C(za),-C(zb),C(zc),-C(za*zc/zb)]
fc=[C(za*zc),-C(zb/zc),-C(zb/za)]
d4=1-6*r*r+2*r**3*sum(tc)+r**4*(3-2*sum(fc))
Z=16-24*r*r+4*r**3*sum(tc)+r**4*(3-2*sum(fc))
for mask in range(16):
    s=[i for i in range(4) if mask>>i&1]
    if len(s)<=1: expected=1
    elif len(s)==2: expected=1-r*r
    elif len(s)==3: expected=1-3*r*r+2*r**3*tc[tri.index(tuple(s))]
    else: expected=d4
    actual=L.extract(s,s).det() if s else sp.Integer(1)
    check(sp.expand(actual-expected)==0)
check(sp.expand((sp.eye(4)+L).det()-Z)==0)
a,b,c=sp.symbols('a b c',real=True)
xs=[a,b,c,a+c-b]; ys=[a+c,b-c,b-a]
check(sp.expand(sum(x*x for x in xs)-sum(y*y for y in ys))==0)

# Centered coefficients and exact core spectral certificates.
Q0=sp.Matrix([[0,1,1,1],[1,0,1,-1],[1,1,0,1],[1,-1,1,0]])
L0=sp.eye(4)+Q0/4
K0=sp.eye(4)-(sp.eye(4)+L0).inv()
R0=K0-sp.eye(4)/2
check(Q0.charpoly().as_expr()==Q0.charpoly().gen**4-6*Q0.charpoly().gen**2+5)
pa=F(15,16); dp=F(27,32); dm=F(25,32); df=F(165,256)
cr=dp**2*dm**2/(pa**6*df)
check(cr==F(4096,4125))
check((pa**3/dp)**2*cr==F(125,132))
check((pa**3/dm)**2*cr==F(243,220))
check((pa**2/dp)**4*cr==F(3125,2673))
check((pa**2/dm)**4*cr==F(2187,1375))

basebounds={
 "pair_min":(F(3125,2673),F(4),F(39,1000),None),
 "pair_max":(F(2187,1375),F(4),None,F(117,1000)),
 "eta_plus_abs":(F(132,125),F(2),F(1,50),F(7,250)),
 "eta_minus":(F(243,220),F(2),F(1,25),F(1,20)),
 "quad_abs":(F(4125,4096),F(1),F(7,1000),F(71,10000)),
}
base_log_cert={}
for name,(q,scale,lo,hi) in basebounds.items():
    ll,uu=log_bounds(q)
    ll/=scale;uu/=scale
    if lo is not None:check(ll>lo)
    if hi is not None:check(uu<hi)
    base_log_cert[name]=display((ll,uu))

spectral=[]
for name,E,rr in [('plus',-R0.extract([0,1,2],[0,1,2]),sp.Rational(1,8)),
                  ('minus',R0.extract([0,1,3],[0,1,3]),sp.Rational(1,5))]:
    minors=[]
    for sign in [-1,1]:
        M=rr*sp.eye(3)+sign*E
        row=[sp.factor(M[:k,:k].det()) for k in [1,2,3]]
        for q in row:check(q>0)
        minors.append([str(q) for q in row])
    s2=sp.trace(E*E);de=E.det()
    cubic=sp.factor(rr**3-rr*s2-2*de)
    check(cubic>0)
    spectral.append(dict(type=name,r=str(rr),trace_square=str(s2),determinant=str(de),
                         rI_pm_E_leading_minors=minors,compound_determinant=str(cubic)))

# Entire phase-cube proof constants, all rational.
delta=F(1,20)
epsilon=F(7,16)*delta+delta*delta/4
check(epsilon==F(9,400))
resolvent_delta=(F(16,23)**2*epsilon)/(1-F(16,23)*epsilon)
inverse_delta=(F(16,7)**2*epsilon)/(1-F(16,7)*epsilon)
check(resolvent_delta==F(72,6509));check(resolvent_delta<F(3,250))
check(inverse_delta==F(72,581));check(inverse_delta<F(1,8))
check(3*F(11,21)**2<1)
check(F(9,46)<F(1,5))
B=12*delta**2/50
check(B==F(3,5000))
d4_error=F(15,64)*delta**2
check(d4_error==F(3,5120))
zeta=d4_error/(F(165,256)-d4_error)
check(zeta==F(1,1099));check(zeta<F(1,1000))
dc=B+F(1,1000);check(dc==F(1,625))
deta=9*delta**2/50+dc/2;check(deta==F(1,800))
dap=B/2+dc/4;check(dap==F(7,10000))
check(F(39,1000)-dap>F(3,80))
check(F(117,1000)+dap<F(3,25))
check(F(7,250)+deta<F(3,100))
check(F(1,20)+deta<F(13,250))
check(F(1,50)>deta);check(F(1,25)>deta)
check(F(71,10000)+dc==F(87,10000))
rho_plus=F(3,100)*(F(1,8)+2*F(3,250))
rho_minus=F(13,250)*(F(1,5)+2*F(3,250))
check(rho_minus>rho_plus)
cubic_bound=2*rho_minus+rho_plus
quartic_bound=3*F(87,10000)*F(53,250)**2
gap=F(3,80)-cubic_bound-quartic_bound
budget=F(3,80)+F(3,2)*(F(3,25)-F(3,80))
check(cubic_bound==F(13883,500000))
check(quartic_bound==F(733149,625000000))
check(gap==F(5350601,625000000));check(gap>F(1,128))
check(budget==F(129,800));check(1-budget>F(4,5))
check(L0.inv()[0,1]*L0.inv()[1,3]*L0.inv()[3,0]==sp.Rational(448,6655))

# A small exact complex-rational matrix implementation avoids symbolic swell.
class Qc:
    __slots__=('re','im')
    def __init__(self,re=0,im=0):
        if isinstance(re,Qc):self.re,self.im=re.re,re.im
        else:self.re,self.im=F(re),F(im)
    def __add__(self,o):
        o=Qc(o);return Qc(self.re+o.re,self.im+o.im)
    __radd__=__add__
    def __neg__(self):return Qc(-self.re,-self.im)
    def __sub__(self,o):return self+-Qc(o)
    def __rsub__(self,o):return Qc(o)+-self
    def __mul__(self,o):
        o=Qc(o);return Qc(self.re*o.re-self.im*o.im,self.re*o.im+self.im*o.re)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Qc(o);d=o.re*o.re+o.im*o.im
        return Qc((self.re*o.re+self.im*o.im)/d,(self.im*o.re-self.re*o.im)/d)
    def conj(self):return Qc(self.re,-self.im)
    def __eq__(self,o):
        o=Qc(o);return self.re==o.re and self.im==o.im
    def __bool__(self):return bool(self.re or self.im)
    def __complex__(self):return complex(float(self.re),float(self.im))
    def pack(self):return [str(self.re),str(self.im)]

def eye(n):return [[Qc(i==j) for j in range(n)] for i in range(n)]
def inv(M):
    n=len(M);B=[[Qc(x) for x in M[i]]+eye(n)[i] for i in range(n)]
    for i in range(n):
        pivot=next(j for j in range(i,n) if B[j][i])
        B[i],B[pivot]=B[pivot],B[i]
        d=B[i][i];B[i]=[x/d for x in B[i]]
        for j in range(n):
            if j!=i:
                c=B[j][i];B[j]=[x-c*y for x,y in zip(B[j],B[i])]
    return [row[n:] for row in B]

def poly_mul(p,q):
    out=[Qc() for _ in range(len(p)+len(q)-1)]
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]=out[i+j]+x*y
    return out

def det_poly(M,A=None):
    n=len(M)
    out=[Qc() for _ in range(n+1)]
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        p=[Qc(sign)]
        for i,j in enumerate(perm):p=poly_mul(p,[M[i][j],A[i][j] if A else Qc()])
        for k,v in enumerate(p):out[k]=out[k]+v
    return out+[Qc() for _ in range(5-len(out))]

def sub(M,mask):
    ii=[i for i in range(4) if mask>>i&1]
    return [[M[i][j] for j in ii] for i in ii]

def real(q):
    check(q.im==0);return q.re

zvalues=[Qc(F(2499,2501),F(100,2501)),
         Qc(F(3599,3601),F(-120,3601)),
         Qc(F(6399,6401),F(160,6401))]
for z,t in zip(zvalues,[F(1,50),F(-1,60),F(1,80)]):
    check(z*z.conj()==1)
    check(2*abs(t)<delta) # |arg z|=2 atan |t| < 2 |t|.
Ls=eye(4)
edges={(0,1):Qc(1),(0,2):Qc(1),(0,3):Qc(1),
       (1,2):zvalues[0],(1,3):-zvalues[1],(2,3):zvalues[2]}
for (i,j),z in edges.items():Ls[i][j]=z/4;Ls[j][i]=z.conj()/4
Bs=[[Ls[i][j]+Qc(i==j) for j in range(4)] for i in range(4)]
Bi=inv(Bs);Ks=[[Qc(i==j)-Bi[i][j] for j in range(4)] for i in range(4)]
Li=inv(Ls)
for M in [Ls,Ks,[[Qc(i==j)-Ks[i][j] for j in range(4)] for i in range(4)]]:
    for k in range(1,5):check(real(det_poly(sub(M,(1<<k)-1))[0])>0)
check((Ls[0][1]*Ls[1][2]*Ls[2][0]).re>0)
check((Li[0][1]*Li[1][3]*Li[3][0]).re>0)
check((Ls[0][1]*Ls[1][2]*Ls[2][0]).im!=0)
check((Li[0][1]*Li[1][3]*Li[3][0]).im!=0)
Zs=real(det_poly(Bs)[0])
minors=[real(det_poly(sub(Ls,m))[0]) for m in range(16)]
atoms=[q/Zs for q in minors]
check(sum(atoms)==1)
SAMPLE=[]
for name,diag in [('positive',[1,2,3,4]),('indefinite',[1,-2,3,-4])]:
    A=[[Qc(diag[i] if i==j else 0) for j in range(4)] for i in range(4)]
    A[0][1]=Qc(0,F(1,5));A[1][0]=A[0][1].conj()
    A[2][3]=Qc(F(1,7));A[3][2]=A[2][3]
    check(Ks[0][2]!=0 and A[0][2]==0)
    commutator=[[sum((Ks[i][k]*A[k][j]-A[i][k]*Ks[k][j] for k in range(4)),Qc()) for j in range(4)] for i in range(4)]
    check(any(x!=0 for row in commutator for x in row))
    # Diagonal perturbation from its signed diagonal has norm <=1/5<1.
    inclusions=[det_poly(sub(Ks,m),sub(A,m)) for m in range(16)]
    polys=[]
    for m in range(16):
        q=[Qc() for _ in range(5)]
        for t in range(16):
            if t&m==m:
                sign=(-1)**((t^m).bit_count())
                q=[x+sign*y for x,y in zip(q,inclusions[t])]
        signed=[[Ks[i][j]-Qc(i==j and not(m>>i&1)) for j in range(4)] for i in range(4)]
        direct=[(-1)**(4-m.bit_count())*x for x in det_poly(signed,A)]
        check(q==direct)
        row=[real(x) for x in q]
        check(row[0]==atoms[m]);polys.append(row)
    for k in range(1,5):check(sum(p[k] for p in polys)==0)
    fi=sum((p[1]**2/p[0] for p in polys),F(0))
    # Frozen curvature = -sum p'' log p, and normalization removes log Z.
    terms=[(-2*polys[m][2],minors[m]) for m in range(16)]
    flo,fhi=outward_sum(terms)
    norm=sum((A[i][j]*A[i][j].conj()).re for i in range(4) for j in range(4))
    check(fi-fhi>=F(4,5)*fi+norm/128)
    if name=='positive':check(flo>0)
    # The frozen-log Möbius table and its centered expansion agree coefficientwise.
    # Coefficients of each independent log minor are checked, not approximated.
    R=[[Ks[i][j]-Qc(F(1,2) if i==j else 0) for j in range(4)] for i in range(4)]
    centered=[det_poly(sub(R,m),sub(A,m)) for m in range(16)]
    for source in range(16):
        weights={t: -(-1)**((t^source).bit_count()) for t in range(16) if t&source==source}
        coeff=F(0)
        for u in range(16):
            if u.bit_count()<2:continue
            alpha=sum((F(w)*F(1,2)**((t^u).bit_count()) for t,w in weights.items() if t&u==u),F(0))
            coeff+=alpha*2*real(centered[u][2])
        check(coeff==-2*polys[source][2])
    SAMPLE.append(dict(name=name,A=[[x.pack() for x in row] for row in A],
                       atom_polynomials=[[str(x) for x in row] for row in polys],
                       Fisher=str(fi),Fisher_decimal=float(fi),frozen_curvature=display((flo,fhi)),
                       entropy_curvature=display((-fi+flo,-fi+fhi)),
                       frobenius_square=str(norm)))

# Floating full-matrix Hessian diagnostic, explicitly not a proof input.
import numpy as np
Kn=np.array([[complex(x) for x in row] for row in Ks])
basis=[];metric=[]
for i in range(4):
    E=np.zeros((4,4),complex);E[i,i]=1;basis.append(E);metric.append(1)
for i,j in combinations(range(4),2):
    E=np.zeros((4,4),complex);E[i,j]=E[j,i]=1;basis.append(E);metric.append(2)
    E=np.zeros((4,4),complex);E[i,j]=1j;E[j,i]=-1j;basis.append(E);metric.append(2)
FI=np.zeros((16,16));frozen=np.zeros((16,16))
for m,p in enumerate(atoms):
    M=Kn.copy()
    for i in range(4):
        if not(m>>i&1):M[i,i]-=1
    Mi=np.linalg.inv(M);Bs=[Mi@E for E in basis];tr=np.array([np.trace(B).real for B in Bs])
    second=np.array([[(tr[i]*tr[j]-np.trace(Bs[i]@Bs[j]).real) for j in range(16)] for i in range(16)])
    FI+=float(p)*np.outer(tr,tr)
    frozen-=float(p)*np.log(float(p))*second
H=-FI+frozen
certificate=-H-F(4,5).__float__()*FI-np.diag(metric)/128
diagnostic=dict(label='floating point diagnostic only; theorem does not rely on it',
                Hessian_max_eigenvalue=float(np.linalg.eigvalsh(H)[-1]),
                displayed_bound_surplus_min_eigenvalue=float(np.linalg.eigvalsh(certificate)[0]))
result=dict(status='PASS',exact_assertions=checks,
            phase_cube='r=1/4; |a|, |b|, |c| <= 1/20; Q24=-exp(i b)',
            constants=dict(cubic=str(cubic_bound),quartic=str(quartic_bound),
                           Fisher_surplus=str(1-budget),norm_surplus=str(gap)),
            core_R=[[str(x) for x in R0.row(i)] for i in range(4)],
            core_spectral_certificates=spectral,base_log_intervals=base_log_cert,
            sample_L=[[x.pack() for x in row] for row in Ls],
            sample_K=[[x.pack() for x in row] for row in Ks],
            sample_atoms=[str(p) for p in atoms],samples=SAMPLE,diagnostic=diagnostic)
(OUT/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(f'PASS: {checks} exact assertions; complete independent-phase atom identities;')
print('uniform full-Fisher constants; direct and complemented phase-cone exclusions;')
print('two rational complex atom/derivative/curvature samples.')
for sample in SAMPLE:
    print(sample['name'], 'FI',sample['Fisher_decimal'],'frozen',sample['frozen_curvature']['decimal_lower'],
          'Hessian',sample['entropy_curvature']['decimal_lower'])
print(diagnostic)
