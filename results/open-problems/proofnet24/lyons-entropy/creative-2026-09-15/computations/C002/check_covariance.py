"""Exact rational checks of C002's complementary-pair formulas.
Standard library only. These checks supplement the symbolic proof in the report.
"""
from fractions import Fraction as F

def inverse(A):
 n=len(A);B=[list(map(F,row))+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
 for i in range(n):
  k=next(k for k in range(i,n) if B[k][i]);B[i],B[k]=B[k],B[i]
  t=B[i][i];B[i]=[x/t for x in B[i]]
  for j in range(n):
   if j!=i:
    t=B[j][i];B[j]=[x-t*y for x,y in zip(B[j],B[i])]
 return [row[n:] for row in B]
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def bil(x,A,y):return sum(x[i]*A[i][j]*y[j] for i in range(len(x)) for j in range(len(y)))
def quad_grad(v,A):return sum(v[i]*A[i][j]*v[j] for i in range(3) for j in range(3))
basis=[]
for i in range(3):
 A=[[F(0) for _ in range(3)] for _ in range(3)];A[i][i]=F(1);basis.append(A)
for i,j in [(1,2),(2,0),(0,1)]:
 A=[[F(0) for _ in range(3)] for _ in range(3)];A[i][j]=A[j][i]=F(1);basis.append(A)
h=[[1,1,1,1],[1,-1,-1,1],[-1,1,-1,1],[-1,-1,1,1]]
for v in [(F(1,10),F(1,5),F(3,10)),(F(0),F(1,10),F(2,5)),(F(2,7),)*3]:
 r=[x*x for x in v];T=sum(r);q0=(1-4*T)/8;q=[q0]+[q0+T-x for x in r]
 assert q0>0
 V=[[sum(2*q[a]*h[a][i]*h[a][j] for a in range(4)) for j in range(4)] for i in range(4)]
 Vformula=[[1,-4*r[2],-4*r[1],-4*r[0]],[-4*r[2],1,-4*r[0],-4*r[1]],[-4*r[1],-4*r[0],1,-4*r[2]],[-4*r[0],-4*r[1],-4*r[2],1]]
 assert V==Vformula
 for a in range(4):assert [dot(row,h[a]) for row in V]==[8*q[a]*x for x in h[a]]
 Vi=inverse(V);mom=[];atom=[]
 for A in basis:
  a=[A[i][i] for i in range(3)];s=sum(a);z=quad_grad(v,A)
  g=[s/4-z]+[x/2-s/4-z for x in a]
  j=[2*x for x in a]+[-8*z]
  assert j==[sum(2*g[b]*h[b][i] for b in range(4)) for i in range(4)]
  mom.append(j);atom.append(g)
 for i in range(6):
  for j in range(6):assert bil(mom[i],Vi,mom[j])==sum(2*atom[i][a]*atom[j][a]/q[a] for a in range(4))
 # Gram identities may be verified at arbitrary positive rational m;
 # their derivation does not use the matched logarithmic values.
 m=[F(2),F(3),F(5)];Rm=dot(m,r)
 G=[]
 for k in range(3):G.append([[F(2*(i==j==k)) for j in range(3)] for i in range(3)])
 G.append([[-8*v[i]*v[j] for j in range(3)] for i in range(3)])
 u=[sum(m[i]*A[i][i] for i in range(3)) for A in G]
 assert u==[2*x for x in m]+[-8*Rm]
 D=[[sum(m[i]*A[i][j]*m[j]*B[j][i] for i in range(3) for j in range(3)) for B in G] for A in G]
 for i in range(3):
  for j in range(3):assert D[i][j]==4*m[i]*m[i]*(i==j)
  assert D[i][3]==D[3][i]==-16*m[i]*m[i]*r[i]
 assert D[3][3]==64*Rm*Rm
 print('PASS exact covariance, Fisher, and Gram identities at v=',tuple(str(x) for x in v))
