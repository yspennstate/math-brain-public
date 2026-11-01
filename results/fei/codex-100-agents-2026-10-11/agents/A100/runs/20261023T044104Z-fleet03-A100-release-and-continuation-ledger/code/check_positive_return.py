from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,time,hashlib,math
R=Path(__file__).resolve().parents[1];O=R/'out';start=time.perf_counter();checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
 assert time.perf_counter()-start<55

def spec(g):
 N=len(g);a=[sum(g[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
 p=[F(v*v,N*N) for v in a];ck(sum(p)==1);return p

def canonical(g):
 N=len(g);p=spec(g);e=F(1,N);M=sum(x>0 for x in p);W=2*e-M*e*e
 q=[(1-W)*p[s] if s<N and p[s] else e*e for s in range(2*N)]
 f=g+g[:];f[N]*=-1;ck(sum(q)==1);ck(all(y>0 for x,y in zip(spec(f),q) if x));return f,q

def bitinsert(x,j,b):return (x%2**j)+2**(j+1)*(x//2**j)+b*2**j

def child(f,q,j):
 N=len(f)//2;ps=[];fs=[]
 for b in (0,1):
  z=[f[bitinsert(x,j,b)] for x in range(N)];fs.append(z);ps.append(spec(z))
 P=spec(f);pm=[P[bitinsert(s,j,0)]+P[bitinsert(s,j,1)] for s in range(N)]
 qm=[q[bitinsert(s,j,0)]+q[bitinsert(s,j,1)] for s in range(N)]
 ck(pm==[(ps[0][s]+ps[1][s])/2 for s in range(N)])
 raw=[[qm[s]*ps[b][s]/pm[s] if pm[s] else qm[s] for s in range(N)] for b in (0,1)]
 Z=[sum(z) for z in raw];ck(sum(Z)==2 and min(Z)>0)
 qs=[[v/Z[b] for v in raw[b]] for b in (0,1)]
 for b in (0,1):ck(sum(qs[b])==1);ck(all(y>0 for x,y in zip(ps[b],qs[b]) if x))
 return fs,ps,qs,Z

def core(w,k):return [(1 if (x&((1<<w)-1)) else -1)*(1 if (x>>w) else -1) for x in range(1<<(w+k))]
f,q=canonical(core(4,2));siblings=[];norm=[]
for j,k in [(4,1),(4,0)]:
 fs,ps,qs,Z=child(f,q,j);siblings.append({'P':[str(x) for x in ps[1]],'Q':[str(x) for x in qs[1]]});norm.append([str(x) for x in Z])
 freshf,freshq=canonical(core(4,k));ck(fs[0]==freshf);f,q=fs[0],freshq
fs,ps,qs,Z=child(f,q,0);freshf,freshq=canonical(core(3,0));ck(fs[0]==freshf)
ck(Z[0]==F(529,452));p,old=ps[0],qs[0];classes=Counter((p[s],old[s],freshq[s]) for s in range(16))
expected=Counter({(F(49,64),F(18375,33856),F(63,128)):1,(F(1,64),F(1695,33856),F(7,128)):7,(F(1,64),F(113,8464),F(1,64)):8});ck(classes==expected)
ratio=F(1)
for s in range(16):
 exponent=p[s]*64;ck(exponent.denominator==1);ratio*=(old[s]/freshq[s])**int(exponent)
N=12250**49*3390**7*452**8;D=11109**49*3703**7*529**8
ck(ratio==F(N,D));ck(N>16*D);ck(N*N<512*D*D)
# Exact conditional-nonempty term, separately from the vacuum penalty.
z=p[0];oldplus=[v/(1-old[0]) for v in old[1:]];freshplus=[v/(1-freshq[0]) for v in freshq[1:]]
profile_ratio=F(1)
for a,b in zip(oldplus,freshplus):profile_ratio*=a/b
ck(profile_ratio<1)
# Physical P has equal 1/64 mass on each nonvacuum atom, so reached profile bill=log2(profile_ratio)/512<0.
calfresh=[z]+[(1-z)*v for v in freshplus];ck(sum(calfresh)==1)
# Calibrating fresh cannot preserve a positive bill here: vacuum calibration is nonpositive relative to old,
# and the nonempty term is strictly negative.
ck(old[1]/old[8]==F(15,4));ck(freshq[1]/freshq[8]==F(7,2))
# One fixed original-source canonical reference r transports by marginalization:
# r_A(s)=sum_T r(s,T). Exhaust all 8 deletion masks of a deliberately nonflat 3-bit reference.
r=[F(x,36) for x in range(1,9)]
def marginal(q,keep,n):
 out=[F(0)]*(1<<len(keep))
 for mask,v in enumerate(q):out[sum(((mask>>j)&1)<<k for k,j in enumerate(keep))]+=v
 return out
for mask in range(8):
 keep=[j for j in range(3) if mask>>j&1];direct=marginal(r,keep,3)
 for j in range(3):
  if j not in keep:
   mid=[i for i in range(3) if i!=j];qmid=marginal(r,mid,3);ind=[mid.index(i) for i in keep];ck(marginal(qmid,ind,2)==direct)
result={'status':'PASS','helper':'A100-direct-character-third-reset-v1','exact_assertions':checks,'boolean_witnesses':1,'arithmetic':'Direct character integer sums and Fraction; strict integer comparisons only','third_normalizer':str(Z[0]),'profile_ratio_numerator':str(profile_ratio.numerator),'profile_ratio_denominator':str(profile_ratio.denominator),'reached_profile_term':'log2(profile_ratio)/512 < 0','vacuum_calibrated_fresh_signed_charge':'strictly negative: -D_Ber(z||old_vacuum) plus negative profile term','source_transport_guard':'A094 normalized physical-child posterior; A097 theorem uses direct spectral marginal transport','original_reach':'1/8','classes':[{'P':str(a),'oldQ':str(b),'freshQ':str(c),'count':v} for (a,b,c),v in classes.items()],'charge_formula':'log2(N/D)/512','N':str(N),'D':str(D),'strict_lower':'1/128','strict_upper':'9/1024','N_gt_16D':True,'N_squared_lt_512D_squared':True,'retained_complementary_terminals':siblings,'previous_normalizers':norm,'fixed_original_reference_marginal_composition':'PASS for every deletion subset and possible intermediate coordinate of supplied nonflat 3-bit r','scope_guard':'Positive residual-source canonical conversion; no contradiction of same ORIGINAL-source commuting return; no universal third-reset or FEI claim','runtime_seconds':round(time.perf_counter()-start,6)}
(O/'POSITIVE_RETURN_REVIEW.json').write_bytes((json.dumps(result,indent=2)+'\n').encode());print(json.dumps({k:v for k,v in result.items() if k not in ['N','D','retained_complementary_terminals','classes']},indent=2))
