import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, scipy.special as ss, itertools, json, math, pathlib, time

def partitions(n,lo=1):
 if n==0: yield (); return
 for j in range(lo,n+1):
  for tail in partitions(n-j,j): yield (j,)+tail

def polymer(n,b):
 states=list(partitions(n)); idx={p:i for i,p in enumerate(states)}; row=[];col=[];data=[]
 for z,p in enumerate(states):
  out={}
  for x in range(len(p)):
   for y in range(x+1,len(p)):
    q=list(p); q.pop(y);q.pop(x);q.append(p[x]+p[y]);q=tuple(sorted(q)); out[q]=out.get(q,0)+2/n
  for x,j in enumerate(p):
   for i in range(1,j):
    q=list(p);q.pop(x);q.extend([i,j-i]);q=tuple(sorted(q));out[q]=out.get(q,0)+b
  rate=0
  for q,v in out.items(): row.append(z);col.append(idx[q]);data.append(v);rate+=v
  row.append(z);col.append(z);data.append(-rate)
 Q=sp.csr_matrix((data,(row,col)),shape=(len(states),len(states)))
 lw=np.array([len(p)*math.log(b*n)-sum(ss.gammaln(p.count(j)+1) for j in set(p)) for p in states]); pi=np.exp(lw-ss.logsumexp(lw));root=np.sqrt(pi)
 S=sp.diags(root)@(-Q)@sp.diags(1/root)
 asym=max(abs((S-S.T).data),default=0)
 eig=np.linalg.eigvalsh(S.toarray())[:2] if len(states)<250 else sla.eigsh(S,k=2,which='SA',tol=1e-9,maxiter=30000,return_eigenvectors=False)
 eig=np.sort(eig); k=np.array([len(p) for p in states]); var=np.dot(pi,(k-np.dot(pi,k))**2); E=b*(n-np.dot(pi,k))
 return {'n':n,'beta':b,'states':len(states),'gap':float(eig[1]),'gap_over_sqrt_beta':float(eig[1]/math.sqrt(b)),'count_rayleigh':float(E/var),'symmetry_error':float(asym)}

def cert(n,b):
 a=n*math.sqrt(b);k=np.arange(1,n,dtype=float);r=np.arange(n-1,dtype=float)
 R1=b*(n-k-1)/(k+a+1)-k*(k-1)/(n*(k+a-1))+b+2*k/n
 R2=b*(n-r-2)/(r+a+1)-r*r/(n*(r+a-1))+b+r/n
 return min(R1.min(),R2.min())/math.sqrt(b)

def coupling_check(n):
 # Exhaustive pairs, joint generator marginals checked without stochastic simulation.
 def gen(X):
  return {frozenset(X^{i}): (b if i not in X else (len(X)-1)/n) for i in range(n) if i not in X or len(X)>1}
 b=.137; worst=0.;pairs=0
 sets=[frozenset(i for i in range(n) if mask>>i&1) for mask in range(1,2**n)]
 for X in sets:
  for Y in sets:
   if X<Y and len(Y-X)==1:
    k=len(X);e=next(iter(Y-X)); joint=[]
    for i in range(n):
     if i not in Y: joint.append((X|{i},Y|{i},b))
     elif i in X:
      if k>1: joint.append((X-{i},Y-{i},(k-1)/n))
      joint.append((X,Y-{i},1/n))
    joint.extend([(Y,Y,b),(X,X,k/n)])
   elif len(X)==len(Y) and len(X-Y)==1:
    r=len(X)-1; joint=[]
    for i in range(n):
     if i not in X|Y:joint.append((X|{i},Y|{i},b))
     elif i in X&Y and r>0:joint.append((X-{i},Y-{i},r/n))
    joint.append((X|Y,X|Y,b))
    if r>0:joint.append((X&Y,X&Y,r/n))
   else:continue
   pairs+=1
   for original,side in [(X,0),(Y,1)]:
    got={}
    for event in joint:
     if event[side]!=original:got[event[side]]=got.get(event[side],0)+event[2]
    target=gen(original)
    for dest in set(got)|set(target):worst=max(worst,abs(got.get(dest,0)-target.get(dest,0)))
 return {'n':n,'pairs':pairs,'max_marginal_error':worst}

rows=[]
for n in [2,3,4,6,8,12,16,20,24,28]:
 for b in ([1/n] if n>8 else [1/n,1e-4,1.]):
  out=polymer(n,b);rows.append(out); print(json.dumps(out),flush=True)
checks=[coupling_check(n) for n in range(2,8)]
checks.append({'certificate_grid_min_ratio':min(cert(n,b) for n in [8,9,16,31,100,1000,10000] for b in np.geomspace(4/n**2,1/16,21)),'claimed_lower_ratio':.2})
pathlib.Path('numerics.json').write_text(json.dumps({'spectra':rows,'checks':checks},indent=2),encoding='utf8');print(json.dumps(checks),flush=True)
