"""Exact identity checks; analytic inequalities are proved in X074.md."""
import itertools,json
from pathlib import Path
import sympy as S
root=Path(__file__).resolve().parent
r,s=S.symbols('r s', nonnegative=True)
x,y=S.symbols('x y', nonnegative=True)
a,b,c=1-r*r,1-s*s,1-r*r*s*s
R,T,D,k=S.symbols('R S D k',real=True)
J=S.ones(2); swap=S.Matrix([[0,1],[1,0]])
U=S.Matrix([[2*(2*c-b)/(a*c),2/c-2*k],[2/c-2*k,2*(2*c-a)/(b*c)]])
F=U+2*k*swap
Fsimple=2*S.diag(1/a,1/b)+2/c*S.Matrix([[s*s,1],[1,r*r]])
assert S.simplify(F-Fsimple)==S.zeros(2)
C=S.Rational(625,544)**2+S.Rational(5,8)**2
assert C<S.Rational(7,4)
assert S.Rational(25,48)<S.Rational(625,544)
hmax=S.Rational(18,25)
assert 4-S.Rational(31,12)*hmax-S.Rational(35,8)*hmax**3==S.Rational(3169,6250)
assert 3-S.Rational(35,8)*hmax**2==S.Rational(183,250)
assert S.Rational(3169,6250)>=S.Rational(7,10)*hmax
assert S.Rational(183,250)>=S.Rational(7,10)
# Exact rank-four positive homogeneous coefficient.
a4=(4*r**4-3*r*r*s*s+s**4)/3
b4=-S.Rational(2,3)*(r**4-3*r*r*s*s+s**4)
d4=a4.xreplace({r:s,s:r})
assert S.factor(a4*d4-b4*b4)==r*r*s*s*(r-s)**2*(r+s)**2
assert S.expand((1-r*s)**2-a*b-(r-s)**2)==0
# Every first/second atom jet is calculated in the singular measured basis.
# The retained statistic is (N_A,X_3,X_4), not total N_B.
count=0
for cc,dd in [(S.Rational(3,10),S.Rational(1,5)),(S.Rational(1,4),S.Rational(1,6))]:
 rv,sv=4*cc**2,4*dd**2
 K=S.eye(4)/2
 K[0,2]=K[2,0]=cc
 K[1,3]=K[3,1]=dd
 basis=[]
 for i in range(4):
  A=S.zeros(4);A[i,i]=1;basis.append(A)
 for i,j in [(0,1),(2,3)]:
  for v in [S.Integer(1),S.I]:
   A=S.zeros(4);A[i,j]=v;A[j,i]=S.conjugate(v);basis.append(A)
 atoms=[]
 for bits in itertools.product([0,1],repeat=4):
  M=S.zeros(4)
  for j in range(4):M[:,j]=(K if bits[j] else S.eye(4)-K)[:,j]
  p=M.det(); inv=M.inv(); eps=[2*b-1 for b in bits]
  lq=-k*eps[0]*eps[1]/2-R*(eps[0]+eps[1])*eps[2]/2-T*(eps[0]+eps[1])*eps[3]/2-D*eps[2]*eps[3]/2+D*S.prod(eps)/2
  atoms.append((bits,p,inv,lq))
 for i in range(8):
  for j in range(i,8):
   A=basis[i] if i==j else basis[i]+basis[j]
   fs={}; acceleration=0
   for bits,p,inv,lq in atoms:
    Ap=A*S.diag(*[2*b-1 for b in bits]); M=inv*Ap
    p1=p*S.trace(M);p2=p*(S.trace(M)**2-S.trace(M*M))
    group=(bits[0]+bits[1],bits[2],bits[3])
    f,f1=fs.get(group,(0,0));fs[group]=(f+p,f1+p1)
    acceleration+=p2*lq
   fi=S.factor(sum(f1*f1/f for f,f1 in fs.values()))
   av,bv,ev,fv=[A[i,i] for i in range(4)]
   zv,wv=A[0,1],A[2,3]
   af=( -4*k*(av*bv-zv*S.conjugate(zv))-4*D*(ev*fv-wv*S.conjugate(wv))
    -4*R*(av+bv)*ev-4*T*(av+bv)*fv-4*D*(sv*av*ev+rv*bv*fv)
    -8*D*S.sqrt(rv*sv)*S.re(zv*S.conjugate(wv)))
   assert S.expand(acceleration-af)==0
   iform=4*(av*av+ev*ev+2*rv*av*ev)/(1-rv*rv)+4*(bv*bv+fv*fv+2*sv*bv*fv)/(1-sv*sv)-2*((1-sv*sv)*(av+rv*ev)-(1-rv*rv)*(bv+sv*fv))**2/((1-rv*rv)*(1-sv*sv)*(1-rv*rv*sv*sv))
   assert S.factor(fi-iform)==0
   count+=2
out={'status':'PASS','exact_atom_and_count_quadratic_assertions':count,'rational_and_symbolic_assertions':9,'scope':'Identities only; no finite grid supplies a universal sign proof.'}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
