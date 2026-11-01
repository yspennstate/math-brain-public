import itertools as it
import numpy as np
import sympy as sp
from pathlib import Path
OUT=Path(__file__).resolve().parent
n=6
SS=[[i for i in range(n) if m>>i&1] for m in range(1<<n)]
pairs=list(it.combinations(range(n),2)); pi={a:i for i,a in enumerate(pairs)}
def mobius(f):
 c=list(f)
 for i in range(n):
  for m in range(1<<n):
   if m>>i&1:c[m]-=c[m^(1<<i)]
 return c

def operator(K,f):
 c=mobius(f);T=sp.zeros(15)
 for k in range(2,5):
  for S in it.combinations(range(n),k):
   cm=c[sum(1<<i for i in S)]
   if cm==0:continue
   ps=list(it.combinations(range(k),2))
   for a in ps:
    ia=pi[tuple(S[j] for j in a)];ra=[S[j] for j in range(k) if j not in a]
    for b in ps:
     ib=pi[tuple(S[j] for j in b)];rb=[S[j] for j in range(k) if j not in b]
     T[ia,ib]+=cm*(-1)**(sum(a)+sum(b))*K.extract(ra,rb).det()
 return T
edges=[(0,1),(2,3),(0,2),(1,3),(0,3),(1,2)]
B=sp.zeros(4,6)
for j,(a,b) in enumerate(edges): B[a,j]=1;B[b,j]=-1
fnull=[len(S)-B[:,S].rank() for S in SS]
K=sp.Matrix(6,6,lambda i,j:sp.Rational(1,2)*(int(i//2==j//2)-sp.Rational(1,3)))
T=operator(K,fnull)
print('K',K,'fnull nonzero',[(S,fnull[m]) for m,S in enumerate(SS) if fnull[m]],sep='\n')
print('T spectrum',T.eigenvals())
print('T',T)
for ev,mul,V in T.eigenvects():
 if ev<0: print('negative ev',ev,'basis',V)
for eps in [sp.Rational(1,100),sp.Rational(1,10),1]:
 L=eps*sp.eye(n)+B.T*B
 f=[0 if not S else -sp.log(L.extract(S,S).det()) for S in SS]
 TN=np.array(operator(K,f),dtype=float)
 print('eps',eps,'min',np.linalg.eigvalsh(TN))
