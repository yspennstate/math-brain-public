#!/usr/bin/env python3
"""C045 exact certificate. Standard-library arithmetic proves all claims.
NumPy, when present, is used only for separately labeled diagnostics.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
import json, math
from pathlib import Path
PAIRS=list(combinations(range(3),2))

def det(a):
 n=len(a)
 if not n:return F(1)
 ans=F(0)
 for perm in permutations(range(n)):
  inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
  val=F((-1)**inv)
  for i in range(n):val*=a[i][perm[i]]
  ans+=val
 return ans

def inv(a):
 n=len(a); b=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
 for i in range(n):
  k=next(k for k in range(i,n) if b[k][i]); b[i],b[k]=b[k],b[i]
  d=b[i][i]; b[i]=[z/d for z in b[i]]
  for k in range(n):
   if k!=i:
    d=b[k][i];b[k]=[x-d*y for x,y in zip(b[k],b[i])]
 return [r[n:] for r in b]

def ldl_pivots(a):
 n=len(a); low=[[F(i==j) for j in range(n)] for i in range(n)]; ds=[]
 for i in range(n):
  d=a[i][i]-sum(low[i][k]**2*ds[k] for k in range(i)); assert d>0
  ds.append(d)
  for j in range(i+1,n):low[j][i]=(a[j][i]-sum(low[j][k]*low[i][k]*ds[k] for k in range(i)))/d
 return ds

def log_bounds(x,terms=40):
 """Exact odd-series enclosure after reducing x to [1,2)."""
 x=F(x); power=0
 while x>=2:x/=2;power+=1
 while x<1:x*=2;power-=1
 def small(y):
  z=(y-1)/(y+1)
  lo=2*sum(z**(2*k+1)/F(2*k+1) for k in range(terms))
  hi=lo+2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
  return lo,hi
 lo,hi=small(x);l2,h2=small(F(2))
 if power>=0:return lo+power*l2,hi+power*h2
 return lo+power*h2,hi+power*l2

def main():
 x=[F(40),F(42),F(41)]; r=[F(450),F(35),F(350)]
 L=[[2*r[i]*r[j]/(x[i]+x[j]) for j in range(3)] for i in range(3)]
 ell=[L[i][i] for i in range(3)]
 u=[((x[i]-x[j])/(x[i]+x[j]))**2 for i,j in PAIRS]
 assert u==[F(1,1681),F(1,6561),F(1,6889)]
 w=[]
 for s in range(8):
  ids=[i for i in range(3) if s>>i&1]
  v=F(1)
  for i in ids:v*=ell[i]
  for k,(i,j) in enumerate(PAIRS):
   if i in ids and j in ids:v*=u[k]
  assert v==det([[L[i][j] for j in ids] for i in ids]);w.append(v)
 Z=sum(w);p=[v/Z for v in w]
 J=inv([[L[i][j]+(i==j) for j in range(3)] for i in range(3)])
 K=[[F(i==j)-J[i][j] for j in range(3)] for i in range(3)]
 for s in range(8):
  Q=[[K[i][j]-(i==j and not(s>>i&1)) for j in range(3)] for i in range(3)]
  assert (-1)**(3-s.bit_count())*det(Q)==p[s]
 assert p[0]*p[3]*p[5]*p[6]==p[1]*p[2]*p[4]*p[7]
 N=[F(s.bit_count()) for s in range(8)];EN=sum(p[s]*N[s] for s in range(8))
 v=sum(p[s]*(N[s]-EN)**2 for s in range(8));assert v>F(1,6)
 labs=[];marg=[];T2=[]
 for i,j in PAIRS:
  lab=[(s>>i&1)+2*(s>>j&1) for s in range(8)]
  mass=[sum(p[s] for s in range(8) if lab[s]==a) for a in range(4)]
  labs.append(lab);marg.append(mass)
  T2.append((mass[1]+mass[2])**2/(4*mass[0]*mass[3]))
 lower_T=[F(141,20),F(76,5),F(21,2)]
 upper_T=[F(15,2),F(31,2),F(11)]
 for z,a,b in zip(T2,lower_T,upper_T):assert a*a<z<b*b
 clo=[F(7),F(17,2),F(17,2)];chi=[F(149,20),F(44,5),F(177,20)]
 for uu,a,b in zip(u,clo,chi):
  lo,hi=log_bounds(1/uu);assert a<lo and hi<b
 # Exact elementary upper bounds used in the written proof.
 z=F(9,73);assert 2*(z+z**3/(3*(1-z*z)))<F(1,4)
 assert 10*F(25,36)+F(1,2)<F(149,20)
 assert F(44,5)+F(4,81)<F(177,20)
 fup=[F(17,50),F(21,100),F(3,10)]
 for a,T,f in zip(chi,lower_T,fup):assert (a-2)/(2*(1+T))<f
 # Both endpoint scalar budgets >1; the whole affine interval fails.
 assert F(7,17)+F(17,66)+F(17,48)>1
 assert F(7)*F(1,6)>1
 beta=F(3,4);t=F(2)
 def RR(k,s,z):return 1/marg[k][labs[k][s]] if labs[k][s]==labs[k][z] else F(0)
 W=[[beta*((1/p[s] if s==z else 0)+1/p[0])-t*N[s]*N[z]-sum(fup[k]*(RR(k,s,z)-RR(k,s,0)-RR(k,0,z)+RR(k,0,0)) for k in range(3)) for z in range(1,8)] for s in range(1,8)]
 piv=ldl_pivots(W)
 simple_pivot_bounds=[F(7789),F(83),F(12),F(1,10),F(1,4),F(100),F(1351952)]
 assert all(d>b for d,b in zip(piv,simple_pivot_bounds))
 pivot_floors=[(1000000*d.numerator)//d.denominator for d in piv];assert all(a>0 for a in pivot_floors)
 # Uniform strong-coefficient family constant: e^4 exceeds this exact sum.
 exp4lower=sum(F(4)**k/F(math.factorial(k)) for k in range(7));assert exp4lower>48
 assert 3*F(8)/exp4lower<F(1,2)
 # Concrete close-Cauchy example outside the old fixed-minimum scalar test.
 xc=[F(100),F(101),F(102)]
 uc=[((xc[i]-xc[j])/(xc[i]+xc[j]))**2 for i,j in PAIRS]
 Zc=4+sum(uc)+math.prod(uc)
 assert Zc<F(9,2) and 3/Zc**2>F(1,8)
 assert 1/max(uc)>81**2 # e<3 -> exp(8)<3^8=81^2.
 # Exact obstruction: admissible symmetric zero-triple law, u=1/1024.
 us=F(1,1024);zs=2*(us+3);ps=[(us if s.bit_count() in (0,3) else F(1))/zs for s in range(8)]
 gs=ps[1]*ps[2]-ps[0]*ps[3]
 cyc=(ps[0]**2*ps[7]+2*ps[1]*ps[2]*ps[4]-ps[0]*(ps[1]*ps[6]+ps[2]*ps[5]+ps[4]*ps[3]))/2
 assert gs>0 and cyc*cyc<gs**3
 vlo=3*(3*us+1)/(4*(us+3))
 qvar=(3*us+1)/(2*(us+3)*(us+1))
 assert 3*(vlo-qvar)/vlo==(3*us+1)/(us+1)
 assert (3*us+1)/(2*(us+3))>F(1,6)
 assert 10*F(2,3)/6>1
 result={'status':'PASS','exact_arithmetic':True,'L':[[str(z) for z in row] for row in L],
  'atoms':[str(z) for z in p],'K':[[str(z) for z in row] for row in K],
  'pair_coefficient_bounds':[[str(a),str(b)] for a,b in zip(clo,chi)],
  'T_bounds':[[str(a),str(b)] for a,b in zip(lower_T,upper_T)],
  'variance':str(v),'f_upper':[str(z) for z in fup],
  'certificate_beta':str(beta),'certificate_t':str(t),'LDL_pivot_lower_bounds':[str(F(a,1000000)) for a in pivot_floors],
  'LDL_simple_lower_bounds':[str(d) for d in simple_pivot_bounds],
  'LDL_pivots':[str(d) for d in piv],
  'scalar0_lower':str(F(7,17)+F(17,66)+F(17,48)),
  'scalarmin_lower':str(F(7,6)),'exp4_lower':str(exp4lower)}
 try:
  import numpy as np
  pn=np.array([float(z) for z in p]);Kn=np.array([[float(z) for z in row] for row in K]);cn=-np.log([float(z) for z in u])
  sq=np.sqrt(pn); nn=sq*(np.array(N,dtype=float)-float(EN));Ps=[];den=[]
  for k in range(3):
   Ps.append(np.array([[sq[s]*sq[z]/float(marg[k][labs[k][s]]) if labs[k][s]==labs[k][z] else 0 for z in range(8)] for s in range(8)])-np.outer(sq,sq))
   den.append(2*(1+math.sqrt(float(T2[k]))))
  Ps=np.array(Ps);fn=(cn-2)/den
  B=np.einsum('i,ijk->jk',fn,Ps)+2*np.outer(nn,nn)
  Bup=np.einsum('i,ijk->jk',np.array(fup,dtype=float),Ps)+2*np.outer(nn,nn)
  bas=[]
  for i in range(3):
   a=np.zeros((3,3),complex);a[i,i]=1;bas.append(a)
  for i,j in PAIRS:
   a=np.zeros((3,3),complex);a[i,j]=a[j,i]=1/np.sqrt(2);bas.append(a)
   a=np.zeros((3,3),complex);a[i,j]=1j/np.sqrt(2);a[j,i]=-1j/np.sqrt(2);bas.append(a)
  FI=np.zeros((9,9));H=np.zeros((9,9))
  for s in range(8):
   Q=Kn-np.diag([not(s>>i&1) for i in range(3)]);Qi=np.linalg.inv(Q)
   R=np.array([Qi@a for a in bas]);tr=np.trace(R,axis1=1,axis2=2).real
   h=pn[s]*(np.outer(tr,tr)-np.einsum('aij,bji->ab',R,R).real)
   FI+=pn[s]*np.outer(tr,tr);H-=pn[s]*np.outer(tr,tr)+np.log(pn[s])*h
  gap=-H-.25*FI-2*np.eye(9)
  result['floating_diagnostics_only']={'scalar0':float(sum(cn/den)),
   'scalarmin':float(sum((cn-min(cn))/den)+min(cn)*float(v)),
   'matrix_rho_actual':float(np.linalg.eigvalsh(B)[-1]),'matrix_rho_rational_upper_weights':float(np.linalg.eigvalsh(Bup)[-1]),
   'K_eigenvalues':np.linalg.eigvalsh(Kn).tolist(),
   'strong_hessian_gap_min_eigenvalue':float(np.linalg.eigvalsh(gap)[0])}
 except ImportError:result['floating_diagnostics_only']='NumPy unavailable; not needed for proof.'
 out=Path(__file__).with_name('verification_results.json');out.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:z for k,z in result.items() if k not in ['LDL_pivots','atoms','K']},indent=2))
if __name__=='__main__':main()
