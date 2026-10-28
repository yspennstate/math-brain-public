from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,importlib.util,time
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1]
HELPER=RUN.parents[2]/'A039/runs/20261014T055326Z-account05-A039-projection-under-restrictions/code/mixed.py'
s=importlib.util.spec_from_file_location('mixed',HELPER); M=importlib.util.module_from_spec(s);s.loader.exec_module(M)
L=M.L; Z=(F(0),F(0)); checks=0
def ck(b):
 global checks
 checks+=1
 assert b,checks
def overlap(a,b):ck(a[0]<=b[1] and b[0]<=a[1])
def h(p):return L.evalformal(L.ent(p))
def binary(d):return L.evalformal(L.h(d))
def avg(z):return M.scale(F(1,2),M.sumiv(z))
def positive(z):return(max(F(0),z[0]),max(F(0),z[1]))
def product(d):return [(q,q) for q in L.product(d)]
def fixture(w):
 core=[(1-2*int((z&((1<<w)-1))==0))*(1-2*int((z>>w)==0)) for z in range(1<<(2*w))]
 return [-1 if not(t&1) and t&2 else core[t>>3] if t&1 and t&4 else 1 for t in range(1<<(2*w+3))]
def run(w,order,pilot):
 tab=fixture(w); p,d,_,_,_=M.info(tab); Q,c=M.rootref(p,d); A=M.kl(p,Q)
 tabs,qs,Ea,Oa,rr=M.step(tab,Q,1)
 facts=[M.info(t) for t in tabs]; TC=avg([f[3] for f in facts]); K=avg([M.kl(f[0],q) for f,q in zip(facts,qs)])
 D=M.sub(M.plus(Oa,TC),A); overlap(D,M.sub(M.sub(TC,K),Ea))
 ck(all(f[1][0]+(facts[1-y][1][0])==1 for y,f in enumerate(facts)))
 labels=['x','b']+list(range(2*w)); frontier=[(t,labels[:],F(1,2),y) for y,t in enumerate(tabs)]
 O=Oa; E=Z; signed=Z; charged=positive(D); records=[]; node_count=1
 maxdepth=1 if pilot else 2*w
 for depth in range(maxdepth):
  nxt=[]; leveltc=Z
  for t,labels,reach,lineage in frontier:
   pp,dd,hh,tc,ss=M.info(t); q=product(dd)
   wanted=next(j for j in order if j in labels); i=labels.index(wanted)
   ts,qq,e,o,rows=M.step(t,q,i); ff=[M.info(t1) for t1 in ts]
   kt=avg([M.kl(f[0],q1) for f,q1 in zip(ff,qq)])
   newtc=avg([f[3] for f in ff]); sigma=M.sub(newtc,kt)
   fused=[pp[z]+pp[z|(1<<i)] for z in range(len(pp)) if not(z>>i&1)]
   B=M.sub(h(pp),h(fused)); J=M.sub(h(fused),avg([f[2] for f in ff]))
   Gamma=M.sumiv(M.sub(binary(dd[j]),avg([binary(f[1][j if j<i else j-1]) for f in ff])) for j in range(len(dd)) if j!=i)
   overlap(e,M.sub(binary(dd[i]),B))
   overlap(sigma,M.sub(M.plus(o,J),Gamma))
   ck(sigma[1]<=newtc[1])
   O=M.plus(O,M.scale(reach,o)); E=M.plus(E,M.scale(reach,e));signed=M.plus(signed,M.scale(reach,sigma));charged=M.plus(charged,M.scale(reach,positive(sigma)))
   leveltc=M.plus(leveltc,M.scale(reach,newtc));node_count+=1
   labs=labels[:i]+labels[i+1:]
   for y,t1 in enumerate(ts):nxt.append((t1,labs,reach/2,lineage))
  frontier=nxt
  full=[(M.info(t),reach,lineage) for t,_,reach,lineage in frontier]
  termtc=M.sumiv(M.scale(reach,f[3]) for f,reach,_ in full)
  termh=M.sumiv(M.scale(reach,f[2]) for f,reach,_ in full)
  overlap(M.plus(A,M.plus(D,signed)),M.plus(O,M.plus(termtc,E)))
  records.append({'depth':depth+1,'terminal_H':M.enc(termh),'terminal_KL':M.enc(termtc),'outcome_KL':M.enc(O),'released_erasure_KL':M.enc(E),'actual_signed_resets':M.enc(signed),'positive_withdrawal_including_first':M.enc(charged)})
  ck(time.perf_counter()-START<(60 if pilot else 600))
 delta=F(1,2**w); tg=2*delta*(1-delta)
 for y,f in enumerate(facts):
  expected=[tg/2,tg/2]+[delta/2]*(2*w)
  if y:expected[0]=1-expected[0]
  ck(f[1]==expected)
 return {'w':w,'order':order,'nodes':node_count,'c':M.enc(c),'A':M.enc(A),'first_D':M.enc(D),'frontiers':records,'final_balance_if_bank1':M.enc(M.sub((F(3,4),F(3,4)),charged))}
START=time.perf_counter();pilot='--pilot' in sys.argv
spec={'helper_sha256':hashlib.sha256(HELPER.read_bytes()).hexdigest(),'family':'F priority activation of two width-w point defects','domain':'pilot w2 one-private-depth; main w2 three orders, w3 interleaved, every outcome, actual reset after each query; analytic allw>=14','case_count':'pilot 3 query nodes; main 220 query nodes','symmetry':'none','arithmetic':'Fraction/FWHT and rational log intervals','memory_estimate_MB':180,'max_runtime_seconds':60 if pilot else 600}
(RUN/'out'/('PILOT_SPEC.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2),encoding='utf-8',newline='\n')
N=lambda w:(2*w+1)*(2*w*w+9*w+6)
ck(F(N(14),2**15)==F(3799,8192));ck(F(3,4)-F(3799,8192)==F(2345,8192));ck(F(2345,8192)>F(9,32))
# Exact translated-polynomial certificates: every coefficient is positive.
# 2N(w)-N(w+1), w=k+14 => 4k^3+176k^2+2545k+12071.
ck([4,176,2545,12071]==[4,12*14+8,12*14**2+16*14-31,4*14**3+8*14**2-31*14-39])
for w in range(14,101):ck(2*N(w)-N(w+1)==4*w**3+8*w*w-31*w-39)
cases=[(2,list(range(4)))] if pilot else [(2,[0,1,2,3]),(2,[3,2,1,0]),(2,[0,2,1,3]),(3,[0,3,1,4,2,5])]
out=[]
for w,order in cases:
 out.append(run(w,order,pilot))
 (RUN/'out'/('PILOT.json' if pilot else 'CHECK_RESULTS.json')).write_text(json.dumps({'status':'PARTIAL','cases':out},indent=2),encoding='utf-8',newline='\n')
result={'status':'PASS','checks':checks,'helper_checks':M.checks,'cases':out,'seconds':time.perf_counter()-START,'scope':'finite identity checks plus scalar induction certificate; all-history proof in PROOF.md; independent review pending'}
(RUN/'out'/('PILOT.json' if pilot else 'CHECK_RESULTS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
