from fractions import Fraction as F
from dataclasses import dataclass
import itertools
import sympy as sp

@dataclass(frozen=True)
class Iv:
    lo:F; hi:F
    def __post_init__(self):
        if self.lo>self.hi: raise ValueError((self.lo,self.hi))
    @staticmethod
    def pt(x): return Iv(x if isinstance(x,F) else F(x), x if isinstance(x,F) else F(x))
    def __add__(self,o):
        o=o if isinstance(o,Iv) else Iv.pt(o); return Iv(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return Iv(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-o)
    def __rsub__(self,o): return Iv.pt(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Iv) else Iv.pt(o)
        z=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return Iv(min(z),max(z))
    __rmul__=__mul__
    def pow(self,n):
        if n==0:return Iv.pt(1)
        if n%2==0 and self.lo<0<self.hi:return Iv(F(0),max(self.lo**n,self.hi**n))
        z=(self.lo**n,self.hi**n); return Iv(min(z),max(z))

def fr(q):
    q=sp.Rational(q); return F(int(q.p),int(q.q))

def p_iv(expr, vv, box):
    p=sp.Poly(sp.expand(expr),*vv)
    ans=Iv.pt(0)
    for mon,coef in p.terms():
        t=Iv.pt(fr(coef))
        for X,e in zip(box,mon):
            if e:t=t*X.pow(e)
        ans=ans+t
    return ans

def fmt(I): return (float(I.lo),float(I.hi))

U=sp.Matrix([
[-sp.Rational(656,21025),sp.Rational(2433,3625),sp.Rational(2688,4205),-sp.Rational(1356,3625)],
[-sp.Rational(5856,47125),-sp.Rational(192,325),sp.Rational(35733,47125),sp.Rational(16,65)],
[sp.Rational(35733,47125),sp.Rational(16,65),sp.Rational(5856,47125),sp.Rational(192,325)],
[sp.Rational(2688,4205),-sp.Rational(1356,3625),sp.Rational(656,21025),-sp.Rational(2433,3625)]])
assert U*U.T==sp.eye(4) and U.det()==-1
assert all(U[i,j]!=0 for i in range(4) for j in range(4))
assert all(U.extract(I,J).det()!=0 for I in itertools.combinations(range(4),2) for J in itertools.combinations(range(4),2))

b=(-4,-2,3,-1)
Db=sp.diag(*b); C=U*Db*U.T
x0,x1,x2,x3,y2,y3=sp.symbols('x0 x1 x2 x3 y2 y3', real=True)
vv=(x0,x1,x2,x3,y2,y3)
a=(x0+sp.I*sp.Rational(7,4), x1-sp.I*sp.Rational(11,10), x2+sp.I*y2, x3+sp.I*y3)
X=sp.diag(*a)+C
D=sp.expand(X.det()); Adj=X.adjugate()
pairs=list(itertools.combinations(range(4),2))

Fexpr=[]
for r,s in pairs:
    K=sp.zeros(4); K[r,s]=1; K[s,r]=-1
    dC=K*C-C*K
    Fexpr.append(sp.expand(sp.re(sp.trace(Adj*dC))))
J=sp.Matrix(Fexpr).jacobian(vv)
assert all(sp.Poly(f,*vv).total_degree()<=3 for f in Fexpr)

for r,s in pairs:
    S=sp.zeros(4); S[r,s]=1; S[s,r]=1
    dC=sp.I*(S*C-C*S)
    assert sp.expand(sp.trace(Adj*dC))==0
for r in range(4):
    S=sp.zeros(4); S[r,r]=1
    dC=sp.I*(S*C-C*S)
    assert sp.expand(sp.trace(Adj*dC))==0

center=(
F('-1.306978760847276'),F('-2.311269351538912'),F('-0.169908501435229'),
F('0.635994359385863'),F('-1.418141008695427'),F('0.390813072733030'))
r=F(1,10**8)
box=tuple(Iv(c-r,c+r) for c in center)
A=(
(F('-0.0644580074161721'),F('0.391786287587297'),F('0.1598800400240651'),F('-0.4174651096319694'),F('-0.0549529725584976'),F('0.0957863797104736')),
(F('-0.0451893504273266'),F('0.288154551945863'),F('0.181149805874911'),F('-0.2969673431302598'),F('-0.1659353901935619'),F('0.1549763366602587')),
(F('-0.012177148718299'),F('0.1248114632215282'),F('-0.1358997072404455'),F('-0.1004051660391908'),F('0.0530680227489032'),F('-0.0435828893686108')),
(F('0.0451790666043996'),F('-0.2448498010'),F('-0.3141575089075643'),F('0.2192590771727887'),F('0.2334440163951549'),F('-0.1123669767509702')),
(F('-0.0322069047891196'),F('0.1175510087879104'),F('-0.0632879935780405'),F('-0.0227931790804556'),F('0.0463514279209251'),F('0.0248017970215977')),
(F('-0.0079415332836357'),F('-0.0311198749490875'),F('0.0315398250081861'),F('0.0034078431314113'),F('-0.0728633638972479'),F('0.0102051283771939')))
subs={q:sp.Rational(center[i].numerator,center[i].denominator) for i,q in enumerate(vv)}
Fc=tuple(fr(sp.expand(f).subs(subs)) for f in Fexpr)
base=[]
for i in range(6): base.append(center[i]-sum(A[i][j]*Fc[j] for j in range(6)))
Jiv=[[p_iv(J[i,j],vv,box) for j in range(6)] for i in range(6)]
Kbox=[]; Bmat=[]
for i in range(6):
    out=Iv.pt(base[i]); brow=[]
    for j in range(6):
        Bij=Iv.pt(1 if i==j else 0)
        for k in range(6): Bij=Bij-A[i][k]*Jiv[k][j]
        brow.append(Bij); out=out+Bij*Iv(-r,r)
    Bmat.append(brow); Kbox.append(out)
assert all(Kbox[i].lo>center[i]-r and Kbox[i].hi<center[i]+r for i in range(6))
Am=sp.Matrix([[sp.Rational(q.numerator,q.denominator) for q in row] for row in A])
assert Am.det()!=0
q_contract=max(sum(max(abs(Bmat[i][j].lo),abs(Bmat[i][j].hi)) for j in range(6)) for i in range(6))
assert q_contract < 1

P=[[sp.expand(U[i,j]**2) for j in range(4)] for i in range(4)]
def Q(i,j): return sp.expand(U.extract([0,i],[0,j]).det()**2)
coef=((0,2,1),(1,0,2),(2,1,0))
lift=P[1][3]+P[2][1]+P[3][2]-P[1][2]-P[2][3]-P[3][1]
for ii,i in enumerate((1,2,3)):
    for jj,j in enumerate((1,2,3)): lift += coef[ii][jj]*Q(i,j)
lift=sp.factor(lift)
assert lift== -sp.Rational(10349074315776,1167289931640625) < 0

Dre=sp.expand(sp.re(D)); Dim=sp.expand(sp.im(D))
DreI=p_iv(Dre,vv,box); DimI=p_iv(Dim,vv,box)
assert DreI.hi<0 and DimI.hi<0
row_gaps=[]; col_gaps=[]; row_gap_expr=[]; col_gap_expr=[]
for r0,s0 in pairs:
    Psw=sp.eye(4); Psw.row_swap(r0,s0)
    Dr=sp.expand((sp.diag(*a)+Psw*C*Psw.T).det())
    Dc=sp.expand((sp.diag(*a)+U*Psw*Db*Psw.T*U.T).det())
    rge=sp.expand(sp.re(D-Dr)); cge=sp.expand(sp.re(D-Dc))
    rg=p_iv(rge,vv,box); cg=p_iv(cge,vv,box)
    assert rg.lo>0 and cg.lo>0
    row_gap_expr.append(rge); col_gap_expr.append(cge)
    row_gaps.append(rg); col_gaps.append(cg)
assert sp.expand(sum(row_gap_expr)-sum(col_gap_expr))==0

Kmix=sp.zeros(4); Kmix[0,1]=1; Kmix[1,0]=-1; Kmix[2,3]=-1; Kmix[3,2]=1
C1=Kmix*C-C*Kmix; C2=Kmix*C1-C1*Kmix
d2=0
for pp in itertools.permutations(range(4)):
    inv=sum(pp[i]>pp[j] for i in range(4) for j in range(i+1,4)); sg=-1 if inv%2 else 1
    for i in range(4):
        term=C2[i,pp[i]]
        for k in range(4):
            if k!=i: term*=X[k,pp[k]]
        d2 += sg*term
    for i in range(4):
        for j in range(i+1,4):
            term=2*C1[i,pp[i]]*C1[j,pp[j]]
            for k in range(4):
                if k!=i and k!=j: term*=X[k,pp[k]]
            d2 += sg*term
d2I=p_iv(sp.expand(sp.re(d2)),vv,box)
assert d2I.lo>0

Abox=(Iv(center[0]-r,center[0]+r),Iv(center[1]-r,center[1]+r),Iv(center[2]-r,center[2]+r),Iv(center[3]-r,center[3]+r))
Ybox=(Iv.pt(F(7,4)),Iv.pt(F(-11,10)),Iv(center[4]-r,center[4]+r),Iv(center[5]-r,center[5]+r))
assert all(not (Y.lo<=0<=Y.hi) for Y in Ybox)
for i,j in pairs:
    assert (Abox[i].hi<Abox[j].lo or Abox[j].hi<Abox[i].lo or Ybox[i].hi<Ybox[j].lo or Ybox[j].hi<Ybox[i].lo)
assert len(set(b))==4

perms=list(itertools.permutations(range(4)))
def zperm(p):
    z=sp.Integer(1)
    for i in range(4): z*=a[i]+b[p[i]]
    return sp.expand(z)
tri=((1,0,2,3),(1,2,3,0),(2,3,1,0))
z=[zperm(p) for p in tri]
def cross(z1,z2): return sp.expand(sp.re(z1)*sp.im(z2)-sp.im(z1)*sp.re(z2))
den=sp.expand(cross(z[1]-z[0],z[2]-z[0]))
nums=(sp.expand(cross(z[1]-D,z[2]-D)),sp.expand(cross(z[2]-D,z[0]-D)),sp.expand(cross(z[0]-D,z[1]-D)))
denI=p_iv(den,vv,box); numI=tuple(p_iv(q,vv,box) for q in nums)
assert denI.lo>0 and all(q.lo>0 for q in numI)

print('PASS MOC4-NONSINGULAR-STRICT-STATIONARY-LIFT-NOGO-v1')
print('krawczyk_box_radius', r)
print('contraction_inf_bound', float(q_contract))
print('krawczyk_offsets', [(float(q.lo-center[i]),float(q.hi-center[i])) for i,q in enumerate(Kbox)])
print('spectral_center', [float(c) for c in center])
print('det_re_interval', fmt(DreI))
print('det_im_interval', fmt(DimI))
print('min_row_swap_gap', min(float(q.lo) for q in row_gaps))
print('min_col_swap_gap', min(float(q.lo) for q in col_gaps))
print('mixed_K01_minus_K23_second_derivative_interval', fmt(d2I))
print('projected_lift_facet', lift)
print('hull_triangle', tri)
print('triangle_area2_interval', fmt(denI))
print('barycentric_weight_bounds', [(float(q.lo/denI.hi),float(q.hi/denI.lo)) for q in numI])
