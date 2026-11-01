import sympy as s
import numpy as np
from itertools import combinations

def build(b=s.Rational(15,52)):
    K=s.eye(3)/2+s.I*s.Matrix([[0,b,-b],[-b,0,b],[b,-b,0]])
    basis=[]
    for i in range(3):
        a=s.zeros(3);a[i,i]=1;basis.append(a)
    for i,j in combinations(range(3),2):
        a=s.zeros(3);a[i,j]=a[j,i]=1;basis.append(a)
    for i,j in combinations(range(3),2):
        a=s.zeros(3);a[i,j]=s.I;a[j,i]=-s.I;basis.append(a)
    ps=[];vs=[]
    for mask in range(8):
        M=s.Matrix.hstack(*[(K if mask>>i&1 else s.eye(3)-K)[:,i] for i in range(3)])
        p=s.simplify(M.det());ps.append(p)
        vs.append(s.Matrix([s.simplify(p*s.trace(M.inv()*s.Matrix.hstack(*[(a if mask>>i&1 else -a)[:,i] for i in range(3)]))) for a in basis]))
    c=s.Symbol('c',real=True)
    pol=[s.zeros(9) for _ in range(3)]
    for i in range(8):
      for j in range(i+1,8):
        v=vs[i]/ps[i]-vs[j]/ps[j]
        pol[(i&1)+(j&1)]+=ps[i]*ps[j]*v*v.T
    d=s.Symbol('d',real=True)
    D=s.diag(d,1,1); E=D-s.eye(3)
    F=d*(s.eye(3)+K*E)*s.diag(c/d,c,c)*(s.eye(3)+E*K)
    def z(a):return s.simplify(2*s.trace(F*a.adjugate()))
    for i,a in enumerate(basis):
      for j,aa in enumerate(basis):
        p=s.expand((z(a+aa)-z(a)-z(aa))/2)
        for k in range(3):pol[k][i,j]-=p.coeff(d,k)
    return K,basis,ps,vs,[x.applyfunc(s.factor) for x in pol],c

if __name__=='__main__':
 K,basis,ps,vs,pol,c=build()
 print('atoms',ps,'log coefficient',ps[1]/ps[0])
 delta=pol[1]-pol[0]-pol[2]
 for sect in [list(range(6)),list(range(6,9))]:
  a=delta.extract(sect,sect)
  print('DELTA',sect,a)
  print(np.linalg.eigvalsh(np.array(a.subs(c,s.log(ps[1]/ps[0]))).astype(float)))
 print('parity cross Q1',pol[1][:6,6:])
 print('parity even equality',pol[0][:6,:6]==pol[2][:6,:6],pol[0][6:,6:]==pol[2][6:,6:])
