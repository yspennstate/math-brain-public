from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt, lcm
import numpy as np
import argparse, json, time, hashlib

RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'; OUT.mkdir(exist_ok=True)
SCALE=1<<40; started=time.perf_counter(); assertions=0
def check(v):
 global assertions
 assert v
 assertions+=1
def save(name,obj):
 (OUT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def floor(x): return x.numerator//x.denominator
def ceil(x): return -((-x.numerator)//x.denominator)
def ln_unit(y):
 z=(y-1)/(y+1); z2=z*z; term=z; ans=F(0)
 for j in range(32): ans+=term/F(2*j+1); term*=z2
 ans*=2
 return ans,ans+2*term/(65*(1-z2))
LN2=ln_unit(F(2))
@lru_cache(None)
def log2_bounds(x):
 check(x>0)
 k=x.numerator.bit_length()-x.denominator.bit_length()
 y=x/(F(2)**k)
 if y<1: k-=1; y*=2
 if y>=2: k+=1; y/=2
 check(1<=y<2)
 a,b=ln_unit(y)
 return k+a/LN2[1],k+b/LN2[0]
@lru_cache(None)
def eta_bounds(x):
 if not x: return F(0),F(0)
 check(0<x<=1)
 a,b=log2_bounds(x)
 return -x*b,-x*a
def hb(x):
 a,b=eta_bounds(x); c,d=eta_bounds(1-x)
 return a+c,b+d
def entropy_bounds(masses):
 lo=hi=F(0)
 for x in masses:
  a,b=eta_bounds(x); lo+=a; hi+=b
 return lo,hi
@lru_cache(None)
def lattice(n,D):
 lo,hi=eta_bounds(F(n,D))
 return floor(SCALE*lo),ceil(SCALE*hi)

def tau_witness(p,x):
 if p==F(1,2): return {'p':str(p),'x':'0','lower':0,'upper':0,'meaning':'certified lower bound on tau* only'}
 rad=p*(1-p)*x*(1-x); scale=1<<100
 k=isqrt((rad.numerator*scale*scale)//rad.denominator)
 sl=F(k,scale); su=F(k+1,scale)
 check(sl*sl<=rad<=su*su)
 yl=p+(1-2*p)*x-2*su; yu=p+(1-2*p)*x-2*sl
 check(0<=yl<=yu<=F(1,2))
 hp=hb(p); hx=hb(x)
 hylo=hb(yl)[0]; hyhi=hb(yu)[1]
 lo=hp[0]-hx[1]-hyhi; hi=hp[1]-hx[0]-hylo
 check(lo>0)
 return {'p':str(p),'x':str(x),'y_bounds':[str(yl),str(yu)],
  'lower':floor(lo*SCALE),'upper':ceil(hi*SCALE),
  'meaning':'enclosure of explicit real-witness debt; lower is <= tau*'}

def child_tables(m):
 N=1<<m; points=4*N; cases=1<<(points-1)
 masks=1+2*np.arange(cases,dtype=np.int64)
 bits=((masks[:,None]>>np.arange(points,dtype=np.int64))&1)
 values=(2*bits-1).reshape(cases,N,4).transpose(0,2,1)
 chars=np.array([[(-1 if (s&x).bit_count()%2 else 1) for s in range(N)] for x in range(N)],dtype=np.int64)
 W=values@chars
 check(bool(np.all(np.sum(W*W,axis=2)==N*N)))
 return masks,W

def parent_nums(W,a,b):
 L=(8-a)*(8-b)*W[:,0,:]+a*(8-b)*W[:,1,:]+(8-a)*b*W[:,2,:]+a*b*W[:,3,:]
 D1=(8-b)*(W[:,1,:]-W[:,0,:])+b*(W[:,3,:]-W[:,2,:])
 D2=(8-a)*(W[:,2,:]-W[:,0,:])+a*(W[:,3,:]-W[:,1,:])
 D12=W[:,3,:]-W[:,2,:]-W[:,1,:]+W[:,0,:]
 return np.stack([L*L,a*(8-a)*D1*D1,b*(8-b)*D2*D2,a*(8-a)*b*(8-b)*D12*D12],axis=2)

def sum_eta(array,D):
 unique,inverse=np.unique(array,return_inverse=True)
 bounds=np.array([lattice(int(n),D) for n in unique],dtype=np.int64)
 vals=bounds[inverse].reshape(*array.shape,2)
 return vals.sum(axis=tuple(range(1,array.ndim)))

def prime_vector(terms):
 result={}
 for weight,masses in terms:
  check(sum(masses)==1)
  for x in masses:
   if not x: continue
   for val,sgn in [(x.numerator,1),(x.denominator,-1)]:
    d=2
    while d*d<=val:
     power=0
     while val%d==0: power+=1; val//=d
     if power: result[d]=result.get(d,F(0))-weight*x*sgn*power
     d+=1
    if val>1: result[val]=result.get(val,F(0))-weight*x*sgn
 return {prime:coef for prime,coef in result.items() if coef}
def exact_sign(vec):
 if not vec: return 0
 den=lcm(*(v.denominator for v in vec.values())); left=right=1
 for prime,v in vec.items():
  exponent=int(v*den)
  if exponent>0: left*=prime**exponent
  else: right*=prime**(-exponent)
 return (left>right)-(left<right)

def details(m,mask,a,b):
 N=1<<m; vals=[1 if (mask>>x)&1 else -1 for x in range(4*N)]
 W=[[sum(vals[z+4*x]*(-1 if (t&x).bit_count()%2 else 1) for x in range(N)) for t in range(N)] for z in range(4)]
 nums=parent_nums(np.array([W],dtype=np.int64),a,b)[0]
 D=4096*N*N; P=[F(int(v),D) for v in nums.reshape(-1)]
 Q=[sum(P[4*t:4*t+4]) for t in range(N)]
 weights=[F((8-a)*(8-b),64),F(a*(8-b),64),F((8-a)*b,64),F(a*b,64)]
 children=[[F(v*v,N*N) for v in row] for row in W]
 terms=[(F(2),Q),(-F(1),P)]+[(-w,c) for w,c in zip(weights,children)]
 vec=prime_vector(terms)
 el=eh=F(0)
 for w,mass in terms:
  lo,hi=entropy_bounds(mass)
  if w>=0: el+=w*lo; eh+=w*hi
  else: el+=w*hi; eh+=w*lo
 return {'residual_bits':m,'truth_mask':int(mask),'truth_table':vals,
  'truth_index':'z1+2*z2+4*residual_index','biases':[str(F(a,8)),str(F(b,8))],
  'integer_child_Walsh':W,'squared_parent_spectrum':[str(v) for v in P],
  'parent_order':'residual frequency major, block frequency minor (0,1,2,3)',
  'residual_marginal':[str(v) for v in Q],'physical_child_weights':[str(v) for v in weights],
  'child_spectra':[[str(v) for v in row] for row in children],
  'debt_prime_log_vector':{str(k):str(v) for k,v in sorted(vec.items())},
  'debt_bounds_lattice':[floor(el*SCALE),ceil(eh*SCALE)]},vec

def main(maxm):
 taus={a:tau_witness(F(a,8),x) for a,x in [(1,F(1,32)),(2,F(1,16)),(3,F(1,256)),(4,F(0))]}
 save('TAU_LOWER_WITNESSES.json',{'lattice_scale':SCALE,'witnesses':taus})
 rows=[]; total=0; zero_checks=0; inconclusive=[]
 for m in range(maxm+1):
  masks,W=child_tables(m); N=1<<m; D=4096*N*N
  child_eta=[]
  for z in range(4): child_eta.append(sum_eta(W[:,z,:]**2,N*N))
  for a in range(1,5):
   for b in range(1,5):
    nums=parent_nums(W,a,b); q=nums.sum(axis=2)
    check(bool(np.all(nums>=0))); check(bool(np.all(q.sum(axis=1)==D)))
    ep=sum_eta(nums,D); eq=sum_eta(q,D)
    weights=[(8-a)*(8-b),a*(8-b),(8-a)*b,a*b]
    child_low=sum(w*e[:,0] for w,e in zip(weights,child_eta))//64
    child_high=(sum(w*e[:,1] for w,e in zip(weights,child_eta))+63)//64
    lows=2*eq[:,0]-ep[:,1]-child_high
    highs=2*eq[:,1]-ep[:,0]-child_low
    tau_low=taus[a]['lower']+taus[b]['lower']
    bad=np.flatnonzero(highs>tau_low)
    if a==b==4:
     for i in bad:
      rec,vec=details(m,int(masks[i]),a,b)
      sig=exact_sign(vec); zero_checks+=1
      check(sig<=0)
      if sig==0: lows[i]=highs[i]=0
      else: inconclusive.append(rec)
    elif len(bad):
     for i in bad[:8]: inconclusive.append(details(m,int(masks[i]),a,b)[0])
    idx=int(np.argmax(lows)); maxlo=int(lows[idx]); maxhi=int(highs.max())
    candidates=np.flatnonzero(highs>=maxlo)
    witness,vec=details(m,int(masks[idx]),a,b)
    tied=[]; other=[]
    for i in candidates:
     if i==idx: tied.append(int(masks[i])); continue
     rec,v=details(m,int(masks[i]),a,b)
     if v==vec: tied.append(int(masks[i]))
     else: other.append(rec)
    check(not other)
    delta=F(a,16)*log2_bounds(F(8-a,a))[0]+F(b,16)*log2_bounds(F(8-b,b))[0]
    deltahi=F(a,16)*log2_bounds(F(8-a,a))[1]+F(b,16)*log2_bounds(F(8-b,b))[1]
    ratio=None
    if delta>0:
     ratio=[str(F(maxlo,SCALE)/deltahi),str(F(maxhi,SCALE)/delta)]
    row={'m':m,'a':a,'b':b,'representatives':len(masks),'full_cases':2*len(masks),
     'maximum_debt_lattice':[maxlo,maxhi],'exact_maximizers_representatives':len(tied),
     'maximizer_masks':tied,'witness':witness,'tax_lower_lattice':tau_low,
     'rigorous_gap_to_tau_lower_lattice':tau_low-maxhi,'half_delta_bounds':[str(delta),str(deltahi)],
     'maximum_ratio_bounds':ratio}
    rows.append(row); total+=len(masks)
    save('PILOT.json' if maxm==1 else 'CENSUS.json',{'status':'RUNNING','scale':SCALE,'rows':rows})
   print(json.dumps({'m':m,'completed_bias_row':a,'elapsed_seconds':time.perf_counter()-started}),flush=True)
 check(not inconclusive)
 result={'status':'PASS','scale':SCALE,'full_cases':2*total,'representatives':total,
  'rows':rows,'assertions':assertions,'exact_zero_checks':zero_checks,
  'runtime_seconds':time.perf_counter()-started,'tau_claim_assumed':False,
  'global_conclusion':'All evaluated actual debts <= explicit lower bounds on sum tau*; uniformly biased pair has exact nonpositive sign.'}
 save('PILOT.json' if maxm==1 else 'CENSUS.json',result)
 print(json.dumps({k:v for k,v in result.items() if k!='rows'}))

if __name__=='__main__':
 parser=argparse.ArgumentParser(); parser.add_argument('--max-m',type=int,choices=[1,2],required=True)
 args=parser.parse_args(); main(args.max_m)
