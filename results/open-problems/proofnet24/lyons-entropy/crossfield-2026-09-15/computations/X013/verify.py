"""Exact rational checks for the X013 majorant square certificate.
Run from any directory. Writes certificate.json beside this file.
No optimized numerical matrix is used in the certificate.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math
import sympy as sp

R=sp.Rational
I=sp.I
K=sp.Matrix([[R(1,10),R(27,200),R(1,250),R(1,250)],
             [R(27,200),R(2,5),R(1,125),-R(1,250)],
             [R(1,250),R(1,125),R(1,2),3*I/1000],
             [R(1,250),-R(1,250),-3*I/1000,R(13,20)]])
A=sp.diag(1,-1,R(1,20),-R(1,20))
D=sp.Matrix([[R(197,195),R(28,195),0,0],
             [R(28,195),R(197,195),0,0],
             [0,0,R(1,20),0],[0,0,0,R(1,20)]])
absA=sp.diag(1,1,R(1,20),R(1,20))
n=4

def real(x):
 x=sp.simplify(x)
 assert sp.im(x)==0
 return sp.re(x)

def frac(x):
 x=real(x)
 return F(int(sp.numer(x)),int(sp.denom(x)))

def log_interval(x, terms=42):
 """Rational enclosure by range reduction and the positive atanh series."""
 x=F(x); assert x>0
 shift=0
 while x>=2: x/=2; shift+=1
 while x<1: x*=2; shift-=1
 def atanh_log(y):
  z=(y-1)/(y+1)
  lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
  tail=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
  return lo,lo+tail
 a,b=atanh_log(x); c,d=atanh_log(F(2))
 if shift>=0:return a+shift*c,b+shift*d
 return a+shift*d,b+shift*c

def add(x,y): return x[0]+y[0],x[1]+y[1]
def scale(c,x):
 c=F(c)
 return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def point(x):return F(x),F(x)
def interval_data(x):
 unit=10**22
 lo=F((x[0]*unit).numerator//(x[0]*unit).denominator,unit)
 hi=-F((-x[1]*unit).numerator//(-x[1]*unit).denominator,unit)
 return {'lower':str(lo),'upper':str(hi),'display':[float(lo),float(hi)]}

# Independent top-coefficient Grassmann implementation.
def sign_mul(a,b):
 if a&b:return 0
 parity=0
 for k in range(8):
  if (a>>k)&1:parity+=(b&((1<<k)-1)).bit_count()
 return -1 if parity%2 else 1

def mul(u,v):
 out={}
 for a,x in u.items():
  for b,y in v.items():
   s=sign_mul(a,b)
   if s:out[a|b]=out.get(a|b,0)+s*x*y
 return {m:sp.expand(x) for m,x in out.items() if x!=0}

def bilinear(M):
 out={}
 for i in range(n):
  for j in range(n):
   if M[i,j]!=0:
    a=1<<(2*i);b=1<<(2*j+1)
    out[a|b]=sign_mul(a,b)*M[i,j]
 return out

def exp_grass(Q):
 q=bilinear(Q);out={0:sp.Integer(1)};power={0:sp.Integer(1)}
 for k in range(1,n+1):
  power=mul(power,q)
  for m,x in power.items():out[m]=out.get(m,0)+x/sp.factorial(k)
 return {m:sp.expand(x) for m,x in out.items()}

leading={}
for name,M in [('K',K),('I-K',sp.eye(n)-K)]:
 vals=[real(M[:j,:j].det()) for j in range(1,n+1)]
 assert all(v>0 for v in vals)
 leading[name]=[str(v) for v in vals]
for M in [D+A,D-A]:
 assert real(M[:2,:2].det())==0
 assert M[0,0]>0 and M[1,1]>0 and M[2,2]>=0 and M[3,3]>=0
assert real(D[:2,:2].det())==1
L=K*(sp.eye(n)-K).inv()
ratio=real(sp.prod(L[i,i] for i in range(n))/L.det())
Delta=log_interval(frac(ratio))
rows=[]
JA=F(0);JD=F(0);Jabs=F(0)
VA=bilinear(A);VA2=mul(VA,VA)
for mask in range(1<<n):
 Q=K-sp.diag(*[int(not(mask>>i&1)) for i in range(n)])
 det=real(Q.det());p=frac((-1)**(n-mask.bit_count())*det)
 assert p>0
 Y=Q.inv()
 s=frac(sp.trace(Y*A));q=frac(sp.trace(Y*A*Y*A));sD=frac(sp.trace(Y*D));sabs=frac(sp.trace(Y*absA))
 tD=frac(sp.trace(Y*D*Y*D))
 JA+=p*s*s;JD+=p*sD*sD;Jabs+=p*sabs*sabs
 coeff=s*s-q
 N=tD-q;V=tD-s*s/4
 assert N>=0 and V>=0
 expQ=exp_grass(Q)
 assert sp.simplify(expQ.get(255,0)-det)==0
 assert sp.simplify(mul(expQ,VA).get(255,0)-det*sp.Rational(s.numerator,s.denominator))==0
 assert sp.simplify(mul(expQ,VA2).get(255,0)-det*sp.Rational(coeff.numerator,coeff.denominator))==0
 sub=[j for j in range(n) if mask>>j&1]
 f_ratio=real(sp.prod(L[j,j] for j in sub)/L.extract(sub,sub).det()) if sub else sp.Integer(1)
 assert 1<=f_ratio<=ratio
 rows.append({'mask':mask,'p':p,'s':s,'q':q,'N':N,'V':V,'f_ratio':frac(f_ratio),'coeff':coeff})
assert sum(x['p'] for x in rows)==1
assert sum(x['p']*x['s'] for x in rows)==0
assert sum(x['p']*x['coeff'] for x in rows)==0
assert sum(x['p']*x['N'] for x in rows)==JD-JA
for i in range(n):assert sum(x['p']*x['coeff'] for x in rows if x['mask']>>i&1)==0
old=add(point(JA),scale(JA/4-Jabs,Delta))
new=add(point(JA),scale(JA/4-JD,Delta))
assert old[1]<-F(1,5)
assert new[0]>F(1,5)
actual=point(JA);r1=point(0);r2=point(0)
for x in rows:
 actual=add(actual,scale(x['p']*x['coeff'],log_interval(x['p'])))
 f=log_interval(x['f_ratio'])
 r1=add(r1,scale(x['p']*x['V'],f))
 delta_f=add(Delta,scale(-1,f))
 r2=add(r2,scale(x['p']*(3*x['s']*x['s']/4+x['N']),delta_f))
represented=add(new,add(r1,r2))
assert max(actual[0],represented[0])<=min(actual[1],represented[1])
cycles={}
for name,M in [('L',L),('Linv',L.inv())]:
 cycles[name]={}
 for triple in [(0,1,2),(0,1,3)]:
  i,j,k=triple;v=sp.simplify(M[i,j]*M[j,k]*M[k,i])
  cycles[name][''.join(str(a+1) for a in triple)]={'real':str(sp.re(v)),'imag':str(sp.im(v))}
 vals=[F(cycles[name][key]['real']) for key in cycles[name]]
 assert vals[0]*vals[1]<0
assert K*A-A*K!=sp.zeros(n)
result={
 'status':'PASS; all sign decisions exact rational interval decisions',
 'K':[[str(v) for v in row] for row in K.tolist()],
 'A':[[str(v) for v in row] for row in A.tolist()],
 'D':[[str(v) for v in row] for row in D.tolist()],
 'leading_principal_minors':leading,
 'FI_A':str(JA),'FI_D':str(JD),'FI_abs_A':str(Jabs),
 'FI_display':{'A':float(JA),'D':float(JD),'abs_A':float(Jabs)},
 'Delta':interval_data(Delta),
 'spectral_certificate':interval_data(old),
 'majorant_certificate':interval_data(new),
 'full_curvature_minus_H_second':interval_data(actual),
 'remainder_fV':interval_data(r1),'remainder_delta_minus_f':interval_data(r2),
 'mixed_triangle_products':cycles,
 'exact_checks':{'positive_atoms':16,'grassmann_identity_checks':48,'normalization_and_modular_second_derivative_checks':8,'majorant_feasibility':True,'old_certificate_below_minus_one_fifth':True,'new_certificate_above_one_fifth':True},
}
Path(__file__).with_name('certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: 16 atoms; 48 exact Grassmann identities; feasible nonspectral majorant.')
print('Fisher values:',result['FI_display'])
for name in ['Delta','spectral_certificate','majorant_certificate','full_curvature_minus_H_second','remainder_fV','remainder_delta_minus_f']:
 print(name,result[name]['display'])
print('PASS: spectral certificate < -1/5; nonspectral certificate > 1/5.')
print('PASS: both L and inverse L have mixed triangle signs.')
