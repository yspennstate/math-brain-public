"""Whole entropy-row cancellation, using only A075 logarithm arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,time,hashlib,sys
import review_log as ar
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[3]
SOURCE=BASE/'agents/A072/runs/20261023T120900Z-account03-A072-exact-walsh-engine'
checks=0;start=time.perf_counter()
def save(n,o):(ROOT/'out'/n).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def ck(x):
 global checks
 assert x
 checks+=1
def add(a,b,c=F(1)):return ar.add(a,b,c)
def scale(a,c):return ar.scale(a,c)
def pack(x):return {str(k):str(v) for k,v in sorted(x.items()) if v}
@lru_cache(None)
def factor(n):
 ck(n>0);o={};p=2
 while p*p<=n:
  while n%p==0:o[p]=o.get(p,F(0))+1;n//=p
  p=3 if p==2 else p+2
 if n>1:o[n]=o.get(n,F(0))+1
 return o
def lq(q):return add(factor(q.numerator),factor(q.denominator),F(-1))
def eta(q):return scale(lq(q),-q) if q else {}
def row(x,y):return add(add(eta(x*x),eta(y*y)),scale(add(eta((x+y)**2),eta((x-y)**2)),F(1,2)),F(-1))
def cmp(a,b):
 z=add(a,b,F(-1))
 if not z:return 0
 lo,hi=ar.enclose(z);ck(lo>0 or hi<0)
 return 1 if lo>0 else -1
@lru_cache(None)
def stats(t):
 N=len(t);n=(N-1).bit_length();W=ar.fwht(t);H={}
 ck(sum(w*w for w in W)==N*N)
 for A,w in enumerate(W):
  ck(w==sum(v*(-1)**((A&x).bit_count()) for x,v in enumerate(t)))
  H=add(H,eta(F(w*w,N*N)))
 for x in range(N):ck(sum(w*(-1)**((A&x).bit_count()) for A,w in enumerate(W))==N*t[x])
 ds=tuple(F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(n))
 ck(sum(ds)==sum((F(w*w,N*N)*A.bit_count() for A,w in enumerate(W)),F(0)))
 return H,tuple(W),ds
def child(t,i,b):return tuple(t[x] for x in range(len(t)) if x>>i&1==b)
@lru_cache(None)
def circuit(h,cores):
 ns=tuple((len(g)-1).bit_length() for g in cores);offs=[];off=0
 for n in ns:offs.append(off);off+=n
 def outputs(x):return tuple(g[(x>>o)&(len(g)-1)] for g,o in zip(cores,offs))
 def gate(z):return h[sum((v==-1)<<j for j,v in enumerate(z))]
 truth=tuple(gate(outputs(x)) for x in range(1<<off));H,W,ds=stats(truth);qs=[]
 for j in range(len(cores)):
  q=F(0)
  # Full physical average: pivotal event is independent of queried core's output.
  for x in range(1<<off):
   z=list(outputs(x));z[j]=1;a=gate(z);z[j]=-1;b=gate(z);q+=F(a!=b,1<<off)
  qs.append(q)
  cg=stats(cores[j]);H=add(H,cg[0],-q)
  for i,d in enumerate(cg[2]):ck(ds[offs[j]+i]==q*d)
 return H,truth,tuple(qs),tuple(offs)
def check_circuit(h,cores,label):
 C,t,qs,offs=circuit(h,cores);N=len(t);W=stats(t)[1];rows=[]
 for j,g in enumerate(cores):
  Hg,Wg,dg=stats(g);mu=F(Wg[0],len(g));offset=offs[j]
  for i,d in enumerate(dg):
   cc=[];qkids=[]
   for b in range(2):
    cs=list(cores);cs[j]=child(g,i,b);c,tt,q,oo=circuit(h,tuple(cs));cc.append(c);qkids.append(q)
    ck(tt==child(t,offset+i,b))
   for k in range(len(cores)):ck(F(qkids[0][k]+qkids[1][k],2)==qs[k])
   drift=add(scale(add(*cc),F(1,2)),C,F(-1));tau=F(Wg[1<<i],len(g));special={}
   for A in range(N):
    if A & ((len(g)-1)<<offset)==0:
     special=add(special,row(F(W[A],N),F(W[A|(1<<(offset+i))],N)))
   vac=row(mu,tau);expected=add(scale(vac,qs[j]),special,F(-1))
   ck(drift==expected);ck(cmp(special,{})>=0);ck(abs(mu)+abs(tau)<=1);ck(abs(tau)<=d)
   # Entire nonempty Fourier entropy decrement cancels, rather than only its erasure part.
   ck(cmp(drift,{2:3*qs[j]*d})<=0)
   # Independently test the improved vacuum-row estimate in natural entropy units.
   if vac:
    vlo,vhi=ar.enclose(vac);ck(vlo>=0)
    # ln2 has its own proved outward enclosure. Compare exact rational endpoint products.
    ck(vhi*ar.LN2[1] <= 2*abs(tau))
   else:ck(not vac)
   rows.append({'core':j,'coordinate':i,'C_drift':pack(drift),'exceptional_inner_row':pack(vac),'full_special_rows':pack(special),'physical_influence':str(qs[j]*d)})
 return {'label':label,'physical_bits':(N-1).bit_length(),'C':pack(C),'queries':rows}
def freeze():
 save('FROZEN_SPEC.json',{'helper_version':'A075-whole-entropy-row-v1','helper_sha256':hashlib.sha256((ROOT/'code/review_log.py').read_bytes()).hexdigest(),
 'family':'all16 outer2-input Boolean gates; first inner every2-bit truth table, second inner every1-bit truth table; constants and dummies retained; separate AND-of-OR(3,2,2) witness',
 'domain':{'pilot':'outer tables0..3, both cores all4 one-bit truth tables:64 circuits/128 physical rows','main':'outer0..15, first core0..15 on2bits, second0..3 on1bit:1024 circuits/3072 physical rows','witness':'one7-bit circuit,all7 physical queries'},
 'case_count':{'pilot':64,'main':1024,'witness':1},'symmetry':'none; complements and all physical rows retained','arithmetic':'integer direct characters and inverse/FWHT, independent physical edges, Fraction prime-log exact identities,192bit80term directed atanh signs',
 'memory_estimate_mb':180,'pilot_max_seconds':55,'maximum_runtime_seconds_per_command':180,'source_executable_imported':False})
 pins=[]
 for n in ['REPORT.md','PROOF.md','CLAIMS.json']:
  p=SOURCE/n;pins.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
 save('SOURCE_PINS.json',pins)
def run(pilot=False):
 done=0;queries=0;record=[]
 for hnum in range(4 if pilot else 16):
  h=tuple(-1 if hnum>>x&1 else 1 for x in range(4))
  for gnum in range(4 if pilot else 16):
   g=tuple(-1 if gnum>>x&1 else 1 for x in range(2 if pilot else 4))
   for knum in range(4):
    k=tuple(-1 if knum>>x&1 else 1 for x in range(2));c=check_circuit(h,(g,k),[hnum,gnum,knum]);done+=1;queries+=len(c['queries'])
    record.append(c)
    ck(time.perf_counter()-start<(55 if pilot else 180))
  if not pilot:
   save('CIRCUITS_'+str(hnum).zfill(2)+'.json',record);record=[]
 result={'status':'PASS','circuits':done,'physical_query_rows':queries,'checks':checks,'seconds':time.perf_counter()-start,'independent_whole_truth_spectra':stats.cache_info().currsize,'full_fei':'OPEN'}
 save('PILOT.json' if pilot else 'VALIDATION.json',result);print(json.dumps(result))
def witness():
 h=tuple(1 if z==0 else -1 for z in range(8));cores=tuple(tuple(-1 if x==0 else 1 for x in range(1<<m)) for m in (3,2,2));c=check_circuit(h,cores,'AND-of-OR(3,2,2)')
 ck(cmp({int(k):F(v) for k,v in c['queries'][0]['C_drift'].items()},{})>0)
 c.update(status='PASS',checks=checks,seconds=time.perf_counter()-start);save('WITNESS.json',c);print(json.dumps({k:c[k] for k in ['status','checks','seconds']}))
if __name__=='__main__':
 mode=sys.argv[1]
 try:
  if mode=='freeze':freeze()
  elif mode=='pilot':run(True)
  elif mode=='main':run()
  elif mode=='witness':witness()
  else:raise ValueError(mode)
 except Exception as e:
  save('FAILURE_'+mode+'.json',{'type':type(e).__name__,'error':str(e),'checks':checks,'seconds':time.perf_counter()-start});raise
