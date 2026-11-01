"""Exact rational construction for the C072 fixed-support-three theorem."""
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
from math import prod
import json

N=6
U=[[F(x) for x in row] for row in [[1,0,1],[0,1,1],[1,1,0],[1,-1,1],[2,1,-1],[1,2,1]]]
PAIRS=list(combinations(range(3),2))
V=[row+[row[i]+row[j] for i,j in PAIRS] for row in U]
S0=2**32; S1=2**33
KDIAG=[F(1,i+1) for i in range(1,7)]
VBASE=[F(i,i+1) for i in range(1,7)]
HB=sum(VBASE)
Z=[[F(i==j) for j in range(6)] for i in range(6)]
for col,(i,j) in enumerate(PAIRS,3): Z[i][col]=Z[j][col]=F(-1)

def zeros(n,m=None): return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]
def transpose(A): return list(map(list,zip(*A)))
def matmul(A,B): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B): return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def sub(A,B): return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(c,A): return [[c*x for x in row] for row in A]
def outer(a,b): return [[x*y for y in b] for x in a]
def quad(A,x): return sum(xi*y*xj for xi,row in zip(x,A) for y,xj in zip(row,x))
def transform(A): return matmul(transpose(Z),matmul(A,Z))
def transform_row(q): return [sum(q[i]*Z[i][j] for i in range(6)) for j in range(6)]
def det3(T,i,j):
 a,b,c=T[0][0],T[0][i],T[0][j]
 d,e,f=T[i][i],T[i][j],T[j][j]
 return a*d*f+2*b*c*e-a*e*e-d*c*c-f*b*b

def determinant(A):
 A=[r[:] for r in A]; n=len(A); val=F(1)
 for i in range(n):
  j=next((j for j in range(i,n) if A[j][i]),None)
  if j is None:return F(0)
  if j!=i:A[i],A[j]=A[j],A[i];val=-val
  pivot=A[i][i];val*=pivot
  for j in range(i+1,n):
   ratio=A[j][i]/pivot
   for k in range(i+1,n):A[j][k]-=ratio*A[i][k]
 return val

def inverse(A):
 n=len(A);B=[A[i][:]+[F(i==j) for j in range(n)] for i in range(n)]
 for i in range(n):
  j=next(j for j in range(i,n) if B[j][i]);B[i],B[j]=B[j],B[i]
  z=B[i][i];B[i]=[v/z for v in B[i]]
  for j in range(n):
   if j!=i:
    z=B[j][i];B[j]=[v-z*w for v,w in zip(B[j],B[i])]
 return [r[n:] for r in B]

@lru_cache(None)
def atoms(s):
 rho=F(s,1)/(1+s*HB); out=[]
 for mask in range(64):
  bits=[(mask>>i)&1 for i in range(6)];eps=[2*b-1 for b in bits]
  base=[k if b else 1-k for k,b in zip(KDIAG,bits)];p0=prod(base)
  rows=[[VBASE[i]]+V[i] for i in range(6)]
  T=[[sum(eps[k]*rows[k][i]*rows[k][j]/base[k] for k in range(6)) for j in range(7)] for i in range(7)]
  p=p0*(1+rho*T[0][0])
  q=[p0*(T[i][i]+rho*(T[0][0]*T[i][i]-T[0][i]**2)) for i in range(1,7)]
  R=zeros(6)
  for i,j in combinations(range(1,7),2):
   R[i-1][j-1]=R[j-1][i-1]=p0*(T[i][i]*T[j][j]-T[i][j]**2+rho*det3(T,i,j))
  out.append({'p':p,'q':transform_row(q),'r':transform(R),'bits':bits})
 assert sum(a['p'] for a in out)==1
 for i in range(6):
  assert sum(a['q'][i] for a in out)==0
  for j in range(6):assert sum(a['r'][i][j] for a in out)==0
 return out

def rawlog(y,terms=24):
 assert 1<=y<=2
 u=(y-1)/(y+1);uu=u*u;power=u;ans=F(0)
 for j in range(terms):ans+=2*power/F(2*j+1);power*=uu
 return ans,ans+2*power/(F(2*terms+1)*(1-uu))
LOG2=rawlog(F(2))
LOGSCALE=10**12
@lru_cache(None)
def log_bounds(x):
 assert x>0
 k=x.numerator.bit_length()-x.denominator.bit_length()
 y=x/(2**k) if k>=0 else x*(2**(-k))
 while y<1:y*=2;k-=1
 while y>=2:y/=2;k+=1
 lo,hi=rawlog(y)
 if k>=0:lo+=k*LOG2[0];hi+=k*LOG2[1]
 else:lo+=k*LOG2[1];hi+=k*LOG2[0]
 return F((lo*LOGSCALE).__floor__(),LOGSCALE), F((hi*LOGSCALE).__ceil__(),LOGSCALE)

def interval_mul(a,b):
 z=[x*y for x in a for y in b];return min(z),max(z)

def frozen_bounds(data0,data1):
 lo=zeros(6);hi=zeros(6)
 for a,b in zip(data0,data1):
  pmin,pmax=sorted([a['p'],b['p']]);logs=(log_bounds(pmin)[0],log_bounds(pmax)[1])
  for i in range(6):
   for j in range(6):
    rr=sorted([a['r'][i][j],b['r'][i][j]])
    l,u=interval_mul(rr,logs);lo[i][j]-=u;hi[i][j]-=l
 mid=scale(F(1,2),add(lo,hi));width=scale(F(1,2),sub(hi,lo))
 upper=[row[:] for row in mid]
 for i in range(6):upper[i][i]+=sum(width[i])
 return lo,hi,mid,width,upper

def gram_coefficients(data0,data1):
 out=[zeros(6) for _ in range(3)]
 for a,b in zip(data0,data1):
  den=max(a['p'],b['p']);qa,qb=a['q'],b['q']
  pieces=[outer(qa,qa),scale(F(1,2),add(outer(qa,qb),outer(qb,qa))),outer(qb,qb)]
  for k in range(3):out[k]=add(out[k],scale(1/den,pieces[k]))
 return out

def basis_real():
 out=[]
 for i in range(3):out.append([[row[i]*col[i] for col in U] for row in U])
 for i,j in PAIRS:out.append([[row[i]*col[j]+row[j]*col[i] for col in U] for row in U])
 return out
BASES=basis_real()
FROB=[[sum(x*y for a,b in zip(A,B) for x,y in zip(a,b)) for B in BASES] for A in BASES]

def floor_matrix_lower(A,precision=10**6):
 B=[[F((x*precision).__floor__(),precision) for x in row] for row in A]
 for i in range(len(A)):B[i][i]-=F(len(A),precision)
 return B

def ldl(A):
 n=len(A);L=zeros(n);D=[]
 for i in range(n):
  L[i][i]=F(1)
  z=A[i][i]-sum(L[i][k]**2*D[k] for k in range(i));D.append(z)
  assert z>0,('nonpositive pivot',i,float(z))
  for j in range(i+1,n):L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/z
 assert matmul(L,matmul([[D[i] if i==j else F(0) for j in range(n)] for i in range(n)],transpose(L)))==A
 return L,D

def kernel(s):
 rho=F(s)/(1+s*HB)
 return [[(KDIAG[i] if i==j else F(0))+rho*VBASE[i]*VBASE[j] for j in range(6)] for i in range(6)]

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,list):return [encode(y) for y in x]
 if isinstance(x,tuple):return [encode(y) for y in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x

def decode(x):
 if isinstance(x,str):return F(x)
 if isinstance(x,list):return [decode(y) for y in x]
 if isinstance(x,dict):return {k:decode(v) for k,v in x.items()}
 return x

def dump(path,obj):
 with open(path,'w') as f:json.dump(encode(obj),f,indent=2)

if __name__=='__main__':
 print('Constructing exact 128 atom endpoint tables...',flush=True)
 a,b=atoms(S0),atoms(S1)
 print('Bounding all frozen logarithms on the interval...',flush=True)
 lo,hi,mid,width,upper=frozen_bounds(a,b)
 print('Forming full cross-score Bernstein matrices...',flush=True)
 G=gram_coefficients(a,b);cert=[]
 for i,g in enumerate(G):
  exact=sub(sub(g,upper),FROB);B=floor_matrix_lower(exact);L,D=ldl(B)
  print('Bernstein',i,'positive pivot floors',[v.__floor__() for v in D],flush=True)
  cert.append({'matrix':B,'ldl_L':L,'ldl_D':D,'pivot_floors':[v.__floor__() for v in D]})
 dump('computations/C072/bernstein_certificate.json',{'s_interval':[S0,S1],'U':U,'h':HB,'frob':FROB,'frozen_lower':lo,'frozen_upper':hi,'curvature_upper_matrix':upper,'bernstein':cert})
 dump('computations/C072/endpoint_atoms.json',{'s0':a,'s1':b})
 print('Saved exact whole-interval real-support certificate.',flush=True)
