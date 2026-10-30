#!/usr/bin/env python3
"""Preserved exploratory algorithms, not certified universal inequalities.
The original run used the same algorithms in separate scripts. Only output
locations and the command-line wrapper were changed for portable preservation.
The tree run has a 35-second cap and may finish fewer than 20,000 iterations.
"""
import numpy as np

def fwht(x):
 a=np.asarray(x,dtype=np.int64).copy(); N=a.shape[-1]; h=1
 while h<N:
  v=a.reshape(*a.shape[:-1],-1,2,h);l=v[...,0,:].copy();r=v[...,1,:].copy()
  v[...,0,:]=l+r;v[...,1,:]=l-r;h*=2
 return a

def vals(W):
 N=W.shape[-1]; n=N.bit_length()-1;d=np.array([i.bit_count() for i in range(N)])
 I=W**2@d;K=np.zeros(len(W),dtype=np.int64); B=np.zeros(len(W))
 for i in range(n):
  inds=np.array([s for s in range(N) if not s>>i&1]); a=W[:,inds];b=W[:,inds|(1<<i)]
  K+=np.sum(np.abs(a*b),axis=1)
  aa=a*a;bb=b*b;tot=aa+bb
  p=aa/np.maximum(tot,1);q=1-p
  B+=np.sum(tot*(-p*np.log2(np.maximum(p,1e-300))-q*np.log2(np.maximum(q,1e-300))),axis=1)
 return I,K,B


import numpy as np,math,collections,json

def monotones(n):
 out=[0,1]; N=1
 for k in range(n):
  out=[a|(b<<N) for a in out for b in out if (a&~b)==0]; N*=2
 return out

def pe2(a,b):
 t=a+b
 return np.where(a>0,a*np.log2(np.maximum(t,1e-300)/np.maximum(a,1e-300)),0)+np.where(b>0,b*np.log2(np.maximum(t,1e-300)/np.maximum(b,1e-300)),0)

def features(mask,n):
 N=1<<n;v=np.array([1-2*(mask>>x&1) for x in range(N)]);W=fwht(v)
 I=sum(s.bit_count()*int(a*a) for s,a in enumerate(W))/(N*N)
 cs=tuple(sorted(abs(int(W[1<<i])) for i in range(n)))
 pairs=collections.Counter((abs(int(W[s])),abs(int(W[s|1<<i]))) for i in range(n) for s in range(N) if not s>>i&1 and W[s] and W[s|1<<i])
 return (I,cs,tuple(sorted((x,y,m) for (x,y),m in pairs.items())))

def limitval(feat,n,depth=30):
 I,cs,pairs=feat;N=1<<n
 if not pairs:return 0,0
 a=np.array([x*x/(N*N) for x,y,m in pairs]);b=np.array([y*y/(N*N) for x,y,m in pairs]);mult=np.array([m for x,y,m in pairs])
 ccount=collections.Counter(c/N for c in cs if c)
 dist={0.:1.};R=0;terms=[]
 # distribution under equal path count divided by I^j; log t bins avoid underflow
 for j in range(depth):
  ls=np.array(list(dist));t2=np.exp(2*ls);w=np.array(list(dist.values()))
  eq=pe2(a[:,None],b[:,None]*t2[None,:]); E=mult@eq
  term=float(E@w/I);R+=term;terms.append(term)
  dd=collections.defaultdict(float)
  for x,m in dist.items():
   for c,ct in ccount.items():dd[round(x+math.log(c),10)]+=m*ct/I
  dist=dd
  if len(dist)>40000:break
 return R,len(terms)
def run_recursive_search():
 n=5;N=1<<n; ms=[x for x in monotones(n) if x.bit_count()==N//2]
 print('balanced',len(ms),flush=True)
 classes={}
 for x in ms:classes.setdefault(features(x,n),x)
 print('classes',len(classes),flush=True)
 out=[]
 for i,(ft,x) in enumerate(classes.items()):
  val,d=limitval(ft,n,30);out.append({'lower_float':val,'depth':d,'mask':x,'feature':ft})
  if val>4:print('ABOVE4',out[-1],flush=True)
 out.sort(key=lambda r:r['lower_float'],reverse=True)
 print(json.dumps(out[:10],indent=2));open('recur_search5.json','w').write(json.dumps(out,indent=2))

import numpy as np,math,json,random,time

def pe(a,b):
 a=np.asarray(a,dtype=float)**2; b=np.asarray(b,dtype=float)**2; t=a+b
 return np.where(a>0,a*np.log1p(b/np.maximum(a,1e-300)),0)+np.where(b>0,b*np.log1p(a/np.maximum(b,1e-300)),0)

def combine(A,B,op):
 # node: p, E_indicator_nats, first_coefficients, number_leaves, expression
 pa,ea,ca,na,ta=A;pb,eb,cb,nb,tb=B
 if op==0:
  p=pa*pb;c=np.r_[ca*pb,cb*pa];e=pb*ea+pa*eb
 else:
  qa,qb=1-pa,1-pb;p=1-qa*qb;c=np.r_[ca*qb,cb*qa]
  eca=ea+np.sum(pe(qa,ca)-pe(pa,ca));ecb=eb+np.sum(pe(qb,cb)-pe(pb,cb))
  e=qb*eca+qa*ecb+np.sum(pe(p,c)-pe(1-p,c))
 return (p,e,c,na+nb,(op,ta,tb))

def score(A):
 p,e,c,n,t=A;I=2*sum(c);B=4*(e+sum(pe(.5-p,c)-pe(p,c)))/math.log(2)
 return B/I if I>1e-14 else 0

def run_tree_search():
 rng=random.Random(20260921);leaf=(.5,math.log(2)/2,np.array([.5]),1,'x')
 # indicator x on +/- cube coeff a0=a1=.5; PE(.5,.5)=.5ln2
 pool=[leaf];best=(0,None);start=time.monotonic();records=[]
 for it in range(20000):
  if time.monotonic()-start>35:break
  A=rng.choice(pool);B=rng.choice(pool)
  if A[3]+B[3]>512:continue
  C=combine(A,B,rng.randrange(2)); sc=score(C)
  if sc>best[0]:
   best=(sc,C);records.append({'iteration':it,'ratio_float':sc,'n':C[3],'p_float':C[0]});print(records[-1],flush=True)
  # diversifies biases and budgets rather than only keep maxima
  if 1e-10<C[0]<1-1e-10 and len(pool)<1500:pool.append(C)
  elif 1e-10<C[0]<1-1e-10:
   j=rng.randrange(1,len(pool))
   if sc>score(pool[j]) or rng.random()<.01:pool[j]=C
 out={'seed':20260921,'iterations':it+1,'status':'EXPLORATORY_FLOAT_NOT_CERTIFIED','records':records,'best_expression':best[1][4]}
 open('tree_search.json','w').write(json.dumps(out,indent=2))
 print('BEST',best[0],best[1][3])

if __name__ == '__main__':
 import argparse
 parser=argparse.ArgumentParser()
 parser.add_argument('part',choices=['recursive','trees'])
 args=parser.parse_args()
 (run_recursive_search if args.part=='recursive' else run_tree_search)()
