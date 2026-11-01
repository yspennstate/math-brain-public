#!/usr/bin/env python3
"""Exact finite checks for lattice-valued flat spectral packets.
Python >=3.10, NumPy. No floating-point comparison certifies an inequality.
The analytical theorems are in REPORT.md; this script is a finite self-check.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib,json
import numpy as np
SEED=2026092051

def fwht(a):
 a=np.asarray(a,dtype=np.int64).copy()
 one=a.ndim==1
 if one:a=a[None,:]
 N=a.shape[1];assert N>0 and N&(N-1)==0
 for j in range(N.bit_length()-1):
  r=a.reshape(len(a),-1,2<<j);u=r[:,:,:1<<j].copy();v=r[:,:,1<<j:].copy()
  r[:,:,:1<<j]=u+v;r[:,:,1<<j:]=u-v
 return a[0] if one else a

def anf_degree(a):
 a=np.asarray(a,dtype=np.int64).copy()
 one=a.ndim==1
 if one:a=a[None,:]
 N=a.shape[1]
 for j in range(N.bit_length()-1):
  z=a.reshape(len(a),-1,2<<j);z[:,:,1<<j:]^=z[:,:,:1<<j]
 wt=np.array([s.bit_count() for s in range(N)])
 ans=np.max(np.where(a!=0,wt[None,:],-1),axis=1)
 return int(ans[0]) if one else ans

def v2(k):
 k=abs(int(k));assert k
 return (k&-k).bit_length()-1

def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(c,a):return (c*a[0],c*a[1]) if c>=0 else(a[1]*c,a[0]*c)
@lru_cache(None)
def log2(q):
 q=F(q);assert q>0
 k=q.numerator.bit_length()-q.denominator.bit_length();t=q/F(2)**k
 if t<1:k-=1;t*=2
 if t>=2:k+=1;t/=2
 def ln(t):
  z=(t-1)/(t+1);zz=z*z;power=z;out=F(0);M=48
  for j in range(M):out+=2*power/(2*j+1);power*=zz
  return out,out+2*power/((2*M+1)*(1-zz))
 a,b=ln(t);c,d=ln(F(2))
 return F(k)+a/d,F(k)+b/c
@lru_cache(None)
def entropy(N,hist):
 out=(F(0),F(0))
 for m,count in hist:
  if m:out=add(out,scale(F(count*m*m,N*N),log2(F(N*N,m*m))))
 return out
@lru_cache(None)
def certify_ratio(N,hist,s,Jnum):
 lo,hi=entropy(N,hist);bound=F((4+2*s)*Jnum,N*N)
 assert hi<=bound,(N,hist,s,Jnum,hi-bound)
 return True

def all_boolean():
 out={'functions':0,'nonzero_band_cases':0,'integral_band_functions':0,
      'half_integer_band_functions':0,'nonplateaued_integral_functions':0,
      'by_dimension':{}}
 for n in range(1,5):
  N=1<<n;x=np.arange(N);bits=(np.arange(1<<N,dtype=np.int64)[:,None]>>x[None,:])&1
  f=1-2*bits;W=fwht(f);absw=abs(W);L=len(f);sq=W*W
  assert np.all(sq.sum(axis=1)==N*N)
  smax=np.zeros(L,dtype=np.int64);Arank=np.zeros(L,dtype=np.int64)
  badhalf=np.zeros(L,dtype=np.int64);allqone=np.ones(L,dtype=bool)
  reconstruction=np.zeros_like(W);squarepieces=np.zeros_like(W)
  bandcount=np.zeros(L,dtype=np.int64)
  for m in range(1,N+1):
   selected=absw==m;count=selected.sum(axis=1);ids=np.flatnonzero(count)
   if not len(ids):continue
   masks=np.sign(W[ids])*selected[ids];V=fwht(masks)
   vals=np.abs(V);lookup=np.array([n+1]+[v2(k) for k in range(1,N+1)])
   r=lookup[vals].min(axis=1)
   assert np.all(m*(np.int64(1)<<r)<=N)  # Boolean projection lattice gap.
   deg=anf_degree(selected[ids]);assert np.all(deg<=n-r)
   bandfold=np.zeros(len(ids),dtype=np.int64)
   for j in range(n):
    inc=selected[ids][:,(x&(1<<j))!=0].sum(axis=1)
    bandfold+=np.minimum(inc,count[ids]-inc)
   assert np.all(2*bandfold>=r*count[ids])  # all-center centroid lower bound
   meshden=np.maximum(0,n-v2(m)-r)
   smax[ids]=np.maximum(smax[ids],meshden)
   massnum=count[ids]*m*m;Arank[ids]+=massnum*r
   badhalf[ids]+=massnum*(m*(np.int64(1)<<r)*2==N)
   allqone[ids]&=(m&(m-1))==0
   reconstruction[ids]+=m*V;squarepieces[ids]+=(m*V)**2
   bandcount[ids]+=1;out['nonzero_band_cases']+=len(ids)
  assert np.array_equal(reconstruction,N*f)
  integral=smax==0;half=smax<=1
  assert np.all(squarepieces[integral]==N*N)
  assert np.all(allqone[half])
  Jnum=np.zeros(L,dtype=np.int64)
  for j in range(n):
   inc=sq[:,(x&(1<<j))!=0].sum(axis=1)
   Jnum+=np.minimum(inc,N*N-inc)
  assert np.all(2*Jnum>=Arank)
  for row,ss,jn in zip(absw,smax,Jnum):
   hist=tuple(sorted(Counter(map(int,row)).items()));certify_ratio(N,hist,int(ss),int(jn))
  nc=half & (bandcount>0) & (absw.max(axis=1)<N)
  assert np.all(Jnum[nc]>=N*N)  # half-grid noncharacters have I>=1 in every gauge
  # In the half-grid case the exact identity has only powers-of-two logarithms.
  Hnum=np.zeros(L,dtype=np.int64)
  for m in (1<<j for j in range(n+1)):
   Hnum+=np.sum(sq*(absw==m),axis=1)*2*(n-v2(m))
  assert np.all(Hnum[half]==2*(Arank[half]+badhalf[half]))
  counts={str(int(k)):int(v) for k,v in zip(*np.unique(smax,return_counts=True))}
  out['by_dimension'][str(n)]={'functions':L,'grid_exponent_counts':counts,
    'integral_functions':int(integral.sum()),'nonplateaued_integral':int((integral&(bandcount>1)).sum())}
  out['functions']+=L;out['integral_band_functions']+=int(integral.sum())
  out['half_integer_band_functions']+=int(half.sum())
  out['nonplateaued_integral_functions']+=int((integral&(bandcount>1)).sum())
 out['distinct_entropy_bound_certificates']=certify_ratio.cache_info().currsize
 out['scope']='Every Boolean truth table in dimensions 1--4. The grid exponent is measured, not bounded universally.'
 return out

def ternary_flat():
 total=flat=0;by={}
 for n in range(1,4):
  N=1<<n;x=np.arange(N);g=((np.arange(3**N,dtype=np.int64)[:,None]//(3**x)[None,:])%3)-1
  W=fwht(g);m=np.max(abs(W),axis=1);good=(m>0)&np.all((W==0)|(abs(W)==m[:,None]),axis=1)
  counts=0
  for row,mm in zip(W[good],m[good]):
   assert mm&(mm-1)==0;k=n-v2(mm);assert k>=0
   mask=np.sign(row);V=fwht(mask);r=min(v2(z) for z in V if z)
   assert r==k and anf_degree(row!=0)<=n-k
   massnum=int(np.sum(row*row));Jnum=0
   for j in range(n):
    inc=int(np.sum((row*row)[(x&(1<<j))!=0]));Jnum+=min(inc,massnum-inc)
   assert 2*Jnum>=k*massnum
   counts+=1
  total+=len(g);flat+=counts;by[str(n)]={'ternary_functions':len(g),'nonzero_flat_functions':counts}
 return {'ternary_truth_tables':total,'flat_ternary_functions':flat,'by_dimension':by}

def describe(f):
 N=len(f);n=N.bit_length()-1;W=fwht(f);sq=W*W;bands=[];s=0
 for m in sorted(set(map(int,abs(W)))-{0}):
  mask=np.where(abs(W)==m,np.sign(W),0);V=fwht(mask);r=min(v2(z) for z in V if z)
  b=F(m*(1<<r),N);assert 0<b<=1
  den=max(0,n-v2(m)-r);s=max(s,den)
  bands.append({'amplitude':str(F(m,N)),'count':int(np.count_nonzero(mask)),
    'divisibility_order':r,'mesh':str(b),'grid_exponent':den,
    'physical_values':sorted(set(str(F(m*int(z),N)) for z in V))})
 I=F(sum(int(z)*a.bit_count() for a,z in enumerate(sq)),N*N)
 hist=tuple(sorted(Counter(map(int,abs(W))).items()));H=entropy(N,hist)
 return W,bands,s,I,H

def witness():
 x=np.arange(32);b=[(x>>i)&1 for i in range(5)]
 f=1-2*((b[3]==b[0]*b[1])&(b[4]==b[0]*b[2])).astype(np.int64)
 W,bands,s,I,H=describe(f)
 assert s==1 and I==F(15,8) and H==(F(7,2),F(7,2))
 assert len(bands)==2 and bands[0]['physical_values']==['-3/2','1/2']
 return f,{'dimension':5,'definition':'1-2*1{y1=x1*x2, y2=x1*x3}',
  'walsh_integers':W.tolist(),'bands':bands,'grid_exponent':s,'entropy':str(H[0]),'influence':str(I),
  'refutes':'Power-of-two Fourier amplitudes automatically have integral magnitude-band projections.',
  'does_not_refute':'FEI, or a constant-four FEI bound for all power-of-two spectra.'}

def tensor_tests(base):
 rows=[]
 for t in (1,2,3):
  n=5*t;x=np.arange(1<<n);f=np.ones(len(x),dtype=np.int64)
  for j in range(t):f*=base[(x>>(5*j))&31]
  W,band,s,I,H=describe(f)
  assert s==t and I==F(15*t,8) and H==(F(7*t,2),F(7*t,2))
  assert band[0]['mesh']==str(F(1,1<<t))
  rows.append({'factors':t,'dimension':n,'grid_exponent':s,'entropy':str(H[0]),'influence':str(I),
     'lowest_band_mesh':band[0]['mesh']})
 return {'actual_truth_tables':len(rows),'rows':rows,
    'interpretation':'Grid denominators can grow under tensor powers even while H/I stays exactly 28/15. The all-t statement is proved separately.'}

def affine_rank(rows):
 piv={}
 for r in rows:
  r=int(r)
  while r:
   j=r.bit_length()-1
   if j in piv:r^=piv[j]
   else:piv[j]=r;break
 return len(piv)

def affine_minimum(f):
 N=len(f);n=N.bit_length()-1;W=fwht(f);corr=fwht(W*W)
 # N^2 times autocorrelation. Greedy minimum-weight binary basis.
 costs=[(N*N-abs(int(corr[v])),v) for v in range(1,N)]
 basis=[];answer=0
 for c,v in sorted(costs):
  if affine_rank(basis+[v])>len(basis):basis.append(v);answer+=c
  if len(basis)==n:break
 return F(answer,2*N*N)

def nonaffine_cells():
 n=9;x=np.arange(1<<n);bits=[(x>>i)&1 for i in range(n)]
 q1=bits[0]*bits[1]+bits[2]*bits[3];q2=bits[0]*bits[2]+bits[1]*bits[3]
 h1=1-2*(q1%2);h2=1-2*(q2%2);T=1-2*bits[4];S=1-2*bits[5]
 h=(h1+T*h2)//2;hp=(h1-T*h2)//2
 g1=h*(1+S)//2;g2=h*(1-S)//2;g3=hp
 assert np.all(g1*g1+g2*g2+g3*g3==1)
 f=(1-2*bits[6])*g1+(1-2*bits[7])*g2+(1-2*bits[8])*g3
 assert np.all(abs(f)==1)
 W,bands,s,I,H=describe(f);assert s==0 and H==(F(7),F(7)) and len(bands)==2
 # Physical data cells on the first six coordinates really are nonaffine.
 for g in (g1[:64],g2[:64],g3[:64]):
  A=[int(z) for z in np.flatnonzero(g)];v=A[0];span=affine_rank([a^v for a in A])
  assert len(A)<(1<<span)
 return f,{'dimension':n,'entropy':str(H[0]),'influence':str(I),'affine_minimum':str(affine_minimum(f)),
   'band_summary':[{k:v for k,v in z.items() if k!='physical_values'} for z in bands],
   'grid_exponent':s,'all_three_physical_cells_nonaffine':True}

def affine_tests(base,nonaffine):
 rng=np.random.default_rng(SEED);count=0
 for root in (base,nonaffine):
  N=len(root);n=N.bit_length()-1;x=np.arange(N);_,bs,ss,_,HH=describe(root)
  profiles=[(b['amplitude'],b['count'],b['divisibility_order'],b['mesh']) for b in bs]
  initial_min=affine_minimum(root)
  for repeat in range(8):
   rows=[]
   while len(rows)<n:
    r=int(rng.integers(1,N))
    if affine_rank(rows+[r])>len(rows):rows.append(r)
   transformed=np.zeros(N,dtype=np.int64)
   for i,r in enumerate(rows):transformed|=np.array([(int(z)&r).bit_count()%2 for z in x])<<i
   transformed^=int(rng.integers(0,N));char=int(rng.integers(0,N))
   f=root[transformed]*(1-2*np.array([(int(z)&char).bit_count()%2 for z in x]))
   _,bb,s,I,H=describe(f)
   assert [(b['amplitude'],b['count'],b['divisibility_order'],b['mesh']) for b in bb]==profiles
   assert s==ss and H==HH and affine_minimum(f)==initial_min
   assert H[1]<=(4+2*s)*I;count+=1
 return {'affine_and_character_images':count,'minimum_basis_cost_checked':True}

def scalar_test():
 # h(p)+2(1-p) <= 2*2delta*log2(1/delta) for 0<=delta<=1/4.
 count=0
 for j in range(257):
  d=F(j,1024)
  if d in (0,F(1,4)):count+=1;continue
  p=(1-2*d)**2
  left=add(scale(p,log2(1/p)),(2*(1-p),2*(1-p)))
  right=scale(4*d,log2(1/d));assert left[1]<right[0]
  count+=1
 return {'biased_head_scalar_grid':count,'endpoints_certified_exactly':True}


def shared_branch_tests():
 rng=np.random.default_rng(SEED+1);x=np.arange(8)
 e0=(1-2*((x>>1)&1))*(1-(x&1))
 e1=(1-2*((x>>2)&1))*(x&1)
 E0,E1=fwht(e0),fwht(e1)
 assert np.all(E0*E1==0) and np.all(e0*e0+e1*e1==1)
 count=0
 for _ in range(24):
  h0=1-2*rng.integers(0,2,size=8,dtype=np.int64)
  h1=1-2*rng.integers(0,2,size=8,dtype=np.int64)
  Ftable=(np.outer(h0,e0)+np.outer(h1,e1)).ravel()
  assert np.all(abs(Ftable)==1)
  W0,W1=fwht(h0),fwht(h1)
  expected=(np.outer(W0,E0)+np.outer(W1,E1)).ravel()
  actual=fwht(Ftable);assert np.array_equal(actual,expected)
  # Each selector has two coefficients of magnitude 1/2. This exact
  # multiset identity proves the entropy formula, without comparing floats.
  actual_nonzero=sorted(abs(int(z)) for z in actual if z)
  expected_nonzero=sorted([4*abs(int(z)) for row in (W0,W1) for z in row if z for _ in range(2)])
  assert actual_nonzero==expected_nonzero
  def energy(W):return F(sum(int(z)**2*j.bit_count() for j,z in enumerate(W)),len(W)**2)
  assert energy(actual)==F(3,2)+(energy(W0)+energy(W1))/2
  count+=1
 return {'shared_branch_pairs':count,'dimension':6,'spectral_mixture_and_energy_identities_exact':True,
         'scope':'The two Boolean branches use the SAME three auxiliary variables; branch independence is not assumed.'}

def main():
 output={'status':'PASS','date':'2026-09-20','seed':SEED,'full_FEI_proved':False,
  'independent_review':False,'proof_assistant_used':False,'all_boolean':all_boolean(),
  'flat_ternary':ternary_flat()}
 base,w=witness();nonaffine,na=nonaffine_cells()
 output.update({'five_variable_obstruction':w,'nonaffine_cell_example':na,
  'tensor_powers':tensor_tests(base),'affine_checks':affine_tests(base,nonaffine),
  'scalar_checks':scalar_test(),'shared_branch_composition':shared_branch_tests()})
 output['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 text=json.dumps(output,indent=2)+'\n';Path(__file__).with_name('verification.json').write_text(text)
 print(text,end='')
if __name__=='__main__':main()
