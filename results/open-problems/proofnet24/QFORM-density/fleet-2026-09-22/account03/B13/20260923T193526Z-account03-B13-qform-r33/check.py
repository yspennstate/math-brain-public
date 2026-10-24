import itertools, math
import numpy as np

rng=np.random.default_rng(20260923)

C3=3*2**(4/3)*math.e**(1/3)
c0=6*math.sqrt(math.pi)
Ksym=8*math.sqrt(3)*C3**1.5
Kunif=math.sqrt(2)*Ksym
Kpivot=8*math.sqrt(2)*C3**3
print("C3",repr(C3))
print("c0",repr(c0))
print("Ksym",repr(Ksym))
print("Kunif",repr(Kunif))
print("Kpivot",repr(Kpivot))

max_ratio=0.0
viol=0
samples=0
for r in (1,2,3):
  n=10
  for _ in range(1000):
    M=rng.normal(size=(n,n)); A=(M+M.T)/2
    for trial in range(200):
      S=sorted(rng.choice(n,r,replace=False).tolist())
      rem=[i for i in range(n) if i not in S]
      T=sorted(rng.choice(rem,r,replace=False).tolist())
      B=A[np.ix_(S,T)]
      if abs(np.linalg.det(B))>1e-7:
        break
    K=[i for i in range(n) if i not in set(S)|set(T)]
    P=A[np.ix_(K,T)]@np.linalg.inv(B)@A[np.ix_(S,K)]
    Ak=A[np.ix_(K,K)]
    U=Ak-P
    np.fill_diagonal(U,0.0)
    L=(P+P.T)/2
    vals,vecs=np.linalg.eigh(L)
    keep=np.argsort(np.abs(vals))[::-1][:r]
    R=(vecs[:,keep]*vals[keep])@vecs[:,keep].T
    E0=Ak-L
    np.fill_diagonal(E0,0.0)
    F=L-R
    np.fill_diagonal(F,0.0)
    E=E0+F
    lhs=np.linalg.norm(E,'fro')
    rhs=math.sqrt(2)*np.linalg.norm(U,'fro')
    ratio=lhs/rhs if rhs else 0.0
    max_ratio=max(max_ratio,ratio); samples+=1
    if lhs>rhs+1e-9:
      viol+=1
print("pivot_samples",samples)
print("pivot_violations",viol)
print("pivot_max_lhs_over_rhs",repr(max_ratio))

def V(A,r):
  n=A.shape[0]
  sets=list(itertools.combinations(range(n),r))
  total=0.0
  for S in sets:
    for T in sets:
      if set(S).isdisjoint(T):
        d=np.linalg.det(A[np.ix_(S,T)])
        total+=d*d
  return total

def avg_U2(A,r):
  n=A.shape[0]; vr=V(A,r)
  sets=list(itertools.combinations(range(n),r))
  num=0.0
  for S in sets:
    for T in sets:
      if not set(S).isdisjoint(T): continue
      B=A[np.ix_(S,T)]; db=np.linalg.det(B)
      if abs(db)<1e-10: continue
      K=[i for i in range(n) if i not in set(S)|set(T)]
      P=A[np.ix_(K,T)]@np.linalg.inv(B)@A[np.ix_(S,K)]
      U=A[np.ix_(K,K)]-P
      np.fill_diagonal(U,0.0)
      num+=db*db*np.linalg.norm(U,'fro')**2
  return num/vr

max_avg_ratio=0.0
for r in (1,2):
  for _ in range(20):
    M=rng.normal(size=(7,7)); A=(M+M.T)/2
    ratio=avg_U2(A,r)/((r+1)**2*V(A,r+1)/V(A,r))
    max_avg_ratio=max(max_avg_ratio,ratio)
print("average_identity_tests",40)
print("average_max_ratio",repr(max_avg_ratio))
print("QFORM_B13_R33_SYMRANK_CHECK_PASS")
