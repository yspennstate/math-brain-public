import itertools, json, math, sys, time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
ROOT=Path(__file__).resolve().parents[1]; checks=0; CACHE={}; DYAD=2**70
def ck(x):
 global checks
 assert x; checks+=1
def lower(x): return F((x*DYAD).__floor__(),DYAD)
def upper(x): return F((x*DYAD).__ceil__(),DYAD)
def lnu(x):
 z=(x-1)/(x+1); p=z; s=F(0)
 for j in range(18): s+=p/(2*j+1); p*=z*z
 return 2*s,2*s+2*p/(37*(1-z*z))
L2,H2=lnu(F(2))
def logint(x):
 if x in CACHE: return CACHE[x]
 k=x.numerator.bit_length()-x.denominator.bit_length(); a=x/F(2)**k
 if a<1: a*=2; k-=1
 if a>=2: a/=2; k+=1
 lo,hi=lnu(a); out=(F(k)+lo/H2,F(k)+hi/L2); CACHE[x]=out; return out
def block(m,h,t):
 lam=F(1,2*m)
 if not h: return (lam/32)**t
 if not t: return F(1,64)
 return F(math.factorial(t),24*8**(t-1)*t*t*(t+1))*lam**t
def case(r,mask,ms):
 corelist=list(itertools.combinations(range(r),2)); core=[e for k,e in enumerate(corelist) if mask>>k&1]
 deg=[sum(i in e for e in core) for i in range(r)]; groups=[]; edges=core[:]; weights=[F(1,2*max(deg[u],deg[v])) for u,v in core]
 offset=r
 for i,m in enumerate(ms):
  groups.append(tuple(range(offset,offset+m)))
  for j in groups[-1]: edges.append((i,j)); weights.append(F(1,2*m))
  offset+=m
 n=offset; size=1<<n; x=np.arange(size,dtype=np.int64); truth=np.full(size,-1,dtype=np.int64)
 for u,v in edges: truth[((x>>u)&1).astype(bool)&((x>>v)&1).astype(bool)]=1
 w=truth.copy(); d=1
 while d<size:
  a=w.reshape(-1,2*d); l=a[:,:d].copy(); rr=a[:,d:].copy(); a[:,:d]=l+rr; a[:,d:]=l-rr; d*=2
 sq=w*w; ck(int(sq.sum())==size*size)
 inf=[F(int(np.count_nonzero(truth!=truth[x^(1<<j)])),size) for j in range(n)]; I=sum(inf)
 pop=np.array([int(b).bit_count() for b in range(size)],dtype=np.int64)
 ck(F(int((sq*pop).sum()),size*size)==I)
 q=F(int(np.count_nonzero(truth==-1)),size); v=1-F(int(w[0])**2,size*size); ck(v==4*q*(1-q))
 conditional=[]
 for i,m in enumerate(ms):
  a=F(int(np.count_nonzero((truth==-1)&((x>>i&1)==0))),size); b=q-a
  ck(b<=a/F(2)**m); ck(inf[i]==2*(a-b)); ck(inf[i]>=a); ck(inf[i]>=F(2,3)*q)
  for j in groups[i]: ck(inf[j]==2*b)
  conditional.append({'a':str(a),'b':str(b),'hub_influence':str(inf[i]),'one_leaf_influence':str(inf[groups[i][0]])})
 for j in range(n): ck(sum(weights[k] for k,e in enumerate(edges) if j in e)<=1)
 ck(sum(weights)<=F(3*r,4)); ck(r*v<=6*I)
 D=math.prod(1+z/4 for z in weights)-1
 totalnum=F(1)
 for m in ms: totalnum*=sum(math.comb(m,t)*(block(m,0,t)+block(m,1,t)) for t in range(m+1))
 ck((totalnum-1)/D<=1)
 sq[0]=0; terms={D:v}; block_marg=[]
 for i,m in enumerate(ms):
  t=np.zeros(size,dtype=np.int64)
  for j in groups[i]: t+=(x>>j)&1
  state=((x>>i)&1)*(m+1)+t; hist=np.zeros(2*(m+1),dtype=np.int64); np.add.at(hist,state,sq)
  ck(int(hist.sum())==int(sq.sum())); marg=[]
  for h in [0,1]:
   for k in range(m+1):
    mass=F(int(hist[h*(m+1)+k]),size*size); U=block(m,h,k)
    ck(U>=F(1,96**(h+k)*m**k))
    if U!=1: terms[U]=terms.get(U,F(0))-mass
    marg.append(str(mass))
  block_marg.append(marg)
 lo=F(0); hi=F(0)
 for arg,coef in terms.items():
  l,h=logint(arg)
  lo=lower(lo+coef*(l if coef>=0 else h)); hi=upper(hi+coef*(h if coef>=0 else l))
 ck(hi<11*I)
 return {'r':r,'core_mask':mask,'private_counts':list(ms),'n':n,'I':str(I),'v':str(v),'false_probability':str(q),'conditionals':conditional,'edges':edges,'weights':[str(z) for z in weights],'D':str(D),'full_reference_subprobability':str((totalnum-1)/D),'spectral_block_marginals':block_marg,'cost_interval':[str(lo),str(hi)],'margin_to_11I':str(11*I-hi),'ratio_upper_display':float(hi/I)}
def run(pilot):
 start=time.perf_counter(); rows=[]; inputs=0
 partial=ROOT/'out'/('PILOT_PARTIAL.jsonl' if pilot else 'PARTIAL.jsonl')
 with partial.open('w',encoding='utf-8') as receipt:
  for r in range(1,3 if pilot else 5):
   for mask in range(1<<(r*(r-1)//2)):
    for ms in itertools.product([1,2],repeat=r):
     row=case(r,mask,ms); rows.append(row); inputs+=1<<row['n']; receipt.write(json.dumps(row)+'\n'); receipt.flush()
 for m in range(1,65):
  ck(F(m*m,2**m)<=F(9,8))
  for h in [0,1]:
   for t in range(m+1): ck(block(m,h,t)>=F(1,96**(h+t)*m**t))
 ck(243<256); ck(F(843,80)<11); ck(L2>F(2,3))
 result={'helper_version':'A009-private-leaf-core-v1','functions':len(rows),'physical_truth_inputs':inputs,'checks':checks,'elapsed_seconds':time.perf_counter()-start,'all_passed':True,'maximum_ratio_upper_display':max(row['ratio_upper_display'] for row in rows),'cases':rows}
 (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
if __name__=='__main__':
 sys.set_int_max_str_digits(0); run('--pilot' in sys.argv)
