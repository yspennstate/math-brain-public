from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,importlib.util,itertools,time
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
HELPER=R.parents[2]/'A039/runs/20261014T055326Z-account05-A039-projection-under-restrictions/code/mixed.py'
s=importlib.util.spec_from_file_location('mixed',HELPER);M=importlib.util.module_from_spec(s);s.loader.exec_module(M);L=M.L
Z=(F(0),F(0));checks=0;START=time.perf_counter()
def ck(b):
 global checks
 checks+=1
 assert b,checks
def meet(a,b):ck(a[0]<=b[1] and b[0]<=a[1])
def avg(z):return M.scale(F(1,2),M.sumiv(z))
def positive(z):return max(F(0),z[0]),max(F(0),z[1])
def marginalH(d):return M.sumiv(L.evalformal(L.h(x)) for x in d)
def prod(d):return [(x,x) for x in L.product(d)]
def fixture(w):
 h=[(1-2*int((z&((1<<w)-1))==0))*(1-2*int((z>>w)==0)) for z in range(1<<(2*w))]
 return [-1 if not(t&1) and t&2 else h[t>>3] if t&1 and t&4 else 1 for t in range(1<<(2*w+3))]
def original(p,d,kind):
 if kind=='occupancy':return M.rootref(p,d)[0]
 if kind=='actual':return [(x,x) for x in p]
 if kind=='uniform':return [(F(1,len(p)),F(1,len(p)))]*len(p)
 raise ValueError(kind)
def run(w,order,kind,pilot):
 tab=fixture(w);p,d,_,_,_=M.info(tab);q=original(p,d,kind);A=M.kl(p,q)
 ts,qs,Ea,Oa,_=M.step(tab,q,1);facts=[M.info(t) for t in ts]
 D=M.sub(M.plus(Oa,avg([f[3] for f in facts])),A)
 old=avg([M.kl(f[0],q1) for f,q1 in zip(facts,qs)])
 meet(D,M.sub(M.sub(avg([f[3] for f in facts]),old),Ea))
 initM=marginalH(facts[1][1]);R0=M.scale(F(1,2),facts[1][4]);ck(R0[0]>1)
 labels=['x','b']+list(range(2*w));front=[(t,labels[:],F(1,2),y) for y,t in enumerate(ts)]
 O=Oa;E=Z;signed=Z;charged=positive(D);ownerQ=Z;records=[];nodes=1;refonly=0
 for depth,wanted in enumerate(order):
  nxt=[]
  for tab,labels,reach,lineage in front:
   p,d,H,TC,S=M.info(tab);i=labels.index(wanted)
   ts,qs,e,o,rows=M.step(tab,prod(d),i);ff=[M.info(t) for t in ts]
   newtc=avg([f[3] for f in ff]);inherited=avg([M.kl(f[0],q1) for f,q1 in zip(ff,qs)])
   sigma=M.sub(newtc,inherited);ck(sigma[0]<=newtc[1]);refonly+=rows
   O=M.plus(O,M.scale(reach,o));E=M.plus(E,M.scale(reach,e));signed=M.plus(signed,M.scale(reach,sigma));charged=M.plus(charged,M.scale(reach,positive(sigma)))
   if lineage==1:
    dropH=M.sub(H,avg([f[2] for f in ff]));querycredit=M.sub((4*d[i],4*d[i]),dropH)
    ownerQ=M.plus(ownerQ,M.scale(reach,querycredit))
   newlabels=labels[:i]+labels[i+1:]
   nxt.extend((t,newlabels,reach/2,lineage) for t in ts);nodes+=1
  front=nxt;ff=[(M.info(t),reach,lineage) for t,_,reach,lineage in front]
  terminalH=M.sumiv(M.scale(reach,f[2]) for f,reach,_ in ff)
  terminalK=M.sumiv(M.scale(reach,f[3]) for f,reach,_ in ff)
  terminalS=M.sumiv(M.scale(reach,f[4]) for f,reach,_ in ff)
  ownerS=M.sumiv(M.scale(reach,f[4]) for f,reach,lineage in ff if lineage==1)
  curM=M.sumiv(M.scale(reach,marginalH(f[1])) for f,reach,_ in ff)
  ck(curM[0]<=initM[1]);meet(M.plus(ownerS,ownerQ),R0)
  meet(M.plus(A,M.plus(D,signed)),M.plus(O,M.plus(terminalK,E)))
  margin=M.sub((F(3,4),F(3,4)),charged)
  records.append({'depth':depth+1,'query':wanted,'full_terminal_H':M.enc(terminalH),'full_terminal_KL':M.enc(terminalK),'full_terminal_S4':M.enc(terminalS),'owner_terminal_S4':M.enc(ownerS),'same_original_owner_query_account':M.enc(ownerQ),'original_owner_total':M.enc(M.plus(ownerS,ownerQ)),'positive_reset_debits_including_old_first':M.enc(charged),'remaining_allocated_bit_after_old_quarter':M.enc(margin),'outcome_KL':M.enc(O),'unused_later_erasure_KL':M.enc(E)})
  ck(time.perf_counter()-START<(60 if pilot else 600))
 ck(all(f[4]==Z for f,_,_ in ff));meet(ownerQ,R0)
 if order[-2:]==['x','b']:
  delta=F(1,2**w);t=2*delta*(1-delta)
  meet(tuple(F(x) for x in records[-2]['full_terminal_S4']),(2*t,2*t))
 return {'w':w,'query_order':order,'original_reference':kind,'query_nodes':nodes,'source_A':M.enc(A),'first_uncovered_D':M.enc(D),'original_owner_R':M.enc(R0),'source_zero_rows':refonly,'frontiers':records}
pilot='--pilot' in sys.argv
orders=[]
for positions in itertools.combinations(range(6),2):
 for controls in [('x','b'),('b','x')]:
  data=iter(range(4));orders.append([controls[positions.index(j)] if j in positions else next(data) for j in range(6)])
cases=[(2,[0,'x',1,2,3,'b'],'occupancy')] if pilot else [(2,o,'occupancy') for o in orders]+[(3,[0,3,'x',1,4,'b',2,5],'occupancy')]+[(2,o,k) for k in ['actual','uniform'] for o in [orders[0],list(range(4))+['x','b'],list(range(4))+['b','x']]]
spec={'helper_version':'A039 mixed.py; SHA256 '+hashlib.sha256(HELPER.read_bytes()).hexdigest(),'actual_Boolean_family':'priority F, two disjoint equal-width point defects','parameter_domain':'pilot w2 one full control-interleaved order; main w2 all30 controller placements plus w3 interleaving and6 original-reference boundary trees','case_count':len(cases),'query_transactions':127 if pilot else 5083,'symmetry':'no Boolean symmetry reduction; every physical outcome explicitly retained; all30 controller placements at fixed private order','arithmetic':'integer Walsh, Fraction laws/kernels, rational log enclosures; exact polynomial tail','memory_estimate_MB':190,'maximum_runtime_seconds':60 if pilot else 600,'automatic_dimension_escalation':False}
(R/'out'/('PILOT_SPEC.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2),encoding='utf-8',newline='\n')
N=lambda w:(2*w+3)*(2*w*w+9*w+6)
ck(F(N(14),2**15)==F(4061,8192));ck(F(3,4)-F(4061,8192)==F(2083,8192));ck(F(2083,8192)>F(1,4))
ck([4,180,2667,12985]==[4,12*14+12,12*14**2+24*14-21,4*14**3+12*14**2-21*14-49])
delta=F(1,2**14);ck(4*delta*(1-delta)<F(1,4))
out=[]
for w,o,k in cases:
 out.append(run(w,o,k,pilot));L.log2.cache_clear()
 (R/'out'/('PILOT.json' if pilot else 'CHECK_RESULTS.json')).write_text(json.dumps({'status':'PARTIAL','cases':out},indent=2),encoding='utf-8',newline='\n')
result={'status':'PASS','direct_assertions':checks,'helper_assertions':M.checks,'query_transactions':sum(c['query_nodes'] for c in out),'cases':out,'seconds':time.perf_counter()-START,'scope':'finite full-controller ledger tests; infinite dimension/adaptive policy proof in PROOF.md; no independent agent acceptance'}
(R/'out'/('PILOT.json' if pilot else 'CHECK_RESULTS.json')).write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
