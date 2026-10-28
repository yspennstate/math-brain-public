from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import sys,importlib.util,json,time,argparse
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
hp=R.parents[1]/'runs/20261022T231605Z-account03-A020-selector-boundary-tests/code/check.py'
sp=importlib.util.spec_from_file_location('exact',hp);h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
N=0
def ck(t):
 global N
 N+=1
 assert t
def plus(*args):
 z=h.con(0)
 for a in args:z=h.add(z,a)
 return z
def show(z):return [str(h.floorq(z[0])),str(h.ceilq(z[1]))]
def overlap(z,w):ck(z[0]<=w[1] and w[0]<=z[1])
def entropy(p):return plus(*(h.eta(a) for a in p))
def project(v,mask):
 for i in reversed(range(mask.bit_length())):
  if mask>>i&1:v=h.marginal(v,i)
 return v
def cut(v,mask,bits):
 for i in reversed(range(mask.bit_length())):
  if mask>>i&1:v=h.restrict(v,i,bits>>i&1)
 return v
E=[(-1 if (t&1)==0 and ((t>>1)&3)==0 else 1)*(-1 if (t&1)==0 and ((t>>3)&3)==0 else 1) for t in range(32)]
PE=h.law(E);INF=[Q(sum(E[t]!=E[t^(1<<i)] for t in range(32)),32) for i in range(5)]
ck(Q(sum(E),32)==Q(5,8));ck(INF==[Q(3,8)]+[Q(1,4)]*4)
@lru_cache(None)
def seed(mask):
 p=project(PE,mask);er=entropy(p);ir=sum(INF[i] for i in range(5) if not(mask>>i&1))
 ck(sum(p)==1);ck(er[1]<4*ir if ir else er==h.con(0))
 return p[0],er,ir,p
@lru_cache(None)
def debit(p):
 b=p/2;t=(1+b)**2/(2*(1+b*b))
 eraw=h.scale(h.sub(h.con(1),plus(h.eta(t),h.eta(1-t))),(1+b*b)/2)
 # Proven KL/chi-square bound, useful below fixed log precision, not a reset.
 eb=(max(Q(0),eraw[0]),min(p*p,eraw[1]));ck(eb[0]<=eb[1])
 L=plus(h.scale(h.log2((9+p*p)/8),Q(1,2)),h.scale(h.log2((9+p*p)/(1+p*p)),p*p/8))
 u=plus(L,eb);ck(u[0]>=0 and u[1]<Q(5,8))
 return u
def fullcost(H,P0):
 q0=(1+P0)/2
 return plus(h.scale(plus(h.con(5*(1-P0)),H,h.scale(h.eta(P0),-1)),Q(1,2)),
             h.scale(h.log2(16/q0),3*P0/8),h.scale(h.log2(1/(q0/16+Q(1,4))),(1+P0/4)/2))
@lru_cache(None)
def mixed(k,j,krem,masks):
 rho=Q(1,1<<k);rp=Q(1,1<<krem);mu=Q(5,8)**j;p=rho*(1-mu)/2
 r0=Q(1);HR=h.con(0);IG=Q(0)
 for mask in masks:
  s,eh,ii,_=seed(mask);r0*=s;HR=plus(HR,eh);IG+=ii
 ck(len(masks)==j)
 c=rho*rp/4;b0=r0+1-2*mu;P0=c*b0;principal=1-2*p+P0
 ck(b0>0);ck(2*p+1-2*p==1)
 HP=plus(h.scale(plus(HR,h.scale(h.eta(r0),-1),h.eta(b0)),rho/2),h.con(2*p*(k+krem+2)),h.scale(h.eta(P0),-1),h.eta(principal))
 C=fullcost(HP,P0);U=debit(p);W=[];I=[]
 for sign in [1,-1]:
  fi=6+2*(krem-1)*p+rho*IG-sign*p
  W.append(h.sub(h.sub(h.con(fi),C),U));I.append(fi)
  removed=2*(k-krem)*p+rho*(j*Q(11,8)-IG)
  ck(fi+removed==6+2*(k-1)*p+rho*j*Q(11,8)-sign*p)
  if k>=5 and j>=2:ck(W[-1][0]>Q(107,64))
 if k>=5 and j>=2:
  # Root CE uses the original q atom rather than the newly erased empty atom.
  _,eh,_,_=seed(0);hr=h.scale(eh,j);b=mu*mu+1-2*mu;c0=rho*rho/4
  hrp=plus(h.scale(plus(hr,h.scale(h.eta(mu*mu),-1),h.eta(b)),rho/2),h.con(2*p*(2*k+2)),h.scale(h.eta(c0*b),-1),h.eta(1-2*p+c0*b))
  cc=plus(hrp,h.con(1),h.scale(h.log2((1+p*p)/(p*p)),-p*p))
  root=plus(h.scale(cc,Q(1,2)),h.con(3))
  ck(h.sub(h.con(6+2*k*p+rho*j*Q(11,8)),root)[0]>Q(19,8))
 return {'k':k,'blocks':j,'remaining_padding':krem,'query_masks':list(masks),'mu':str(mu),'p':str(p),'projected_seed_entropy':show(HR),'remaining_seed_influence':str(IG),'P_core_empty':str(P0),'core_entropy':show(HP),'full_CE':show(C),'fourI_both_signs':[str(x) for x in I],'old_U':show(U),'W_both_signs':[show(x) for x in W]},(HP,P0,C,I)

def literal(pilot):
 k=1;rho=Q(1,2);mu=Q(5,8);p=rho*(1-mu)/2
 act=[int((t&1)==0 and E[t>>1]==-1) for t in range(64)]
 core=[(-1 if t&1 else 1) if act[t>>2] else (-1 if t>>1&1 else 1) for t in range(256)]
 F=h.full(core);pc=h.law(core);qh=[(v+int(i==1))/2 for i,v in enumerate(pc)];qf=h.fullref(qh)
 children=[h.restrict(F,1,b) for b in [0,1]];qc=h.marginal(qf,1);ck(sum(qf)==1)
 branches=0;frontiers=0
 for mask in ([0,1] if pilot else range(32)):
  for krem in ([1] if pilot else [0,1]):
   eventmask=(mask<<(k+2)) | (0 if krem else (1<<2))
   ref=project(qc,eventmask);ck(sum(ref)==1)
   dat,vals=mixed(1,1,krem,(mask,));HP,P0,C,I=vals
   # Conditional full laws are averaged over ALL physical outcomes explicitly.
   coords=[i for i in range(eventmask.bit_length()) if eventmask>>i&1]
   for qb in [0,1]:
    pp=[];phys=Q(0);ce=h.con(0)
    for valsbits in product([0,1],repeat=len(coords)):
     bits=sum(b<<i for i,b in zip(coords,valsbits));f=cut(children[qb],eventmask,bits);pf=h.law(f)
     pp.append(pf);phys+=h.influence(f)/Q(1<<len(coords));ce=plus(ce,h.scale(h.ce(pf,ref),Q(1,1<<len(coords))))
     branches+=1
    avg=[sum(row,Q(0))/len(pp) for row in zip(*pp)]
    ck(avg==project(h.law(children[qb]),eventmask));ck(4*phys==I[qb]);overlap(ce,C)
    # Recover full averaged data law and verify original Q matches its lift.
    data=[avg[2*t]+avg[2*t+1] for t in range(len(avg)//2)]
    nc=len(data)//4;Pbar=[2*sum(data[t+nc*z] for z in range(4))-int(t==0) for t in range(nc)]
    ck(sum(Pbar)==1);ck(Pbar[0]==P0);overlap(entropy(Pbar),HP)
    qcore=[(v+int(t==0))/2 for t,v in enumerate(Pbar)]
    ck(ref==h.fullref(qcore));frontiers+=1
 return {'original_dimension':11,'signed_frontiers':frontiers,'actual_signed_physical_branches':branches,'every_physical_outcome_retained':True,'reference_normalization':'PASS','projected_law_vs_literal_restriction':'PASS','interference':'gate means averaged as original p, never sqrt(P0)','scope':'small mu5/8 outside theorem; formula/ledger validation only'}

def a016(k):
 rho=Q(1,1<<k);mu=Q(81,256);p=rho*(1-mu)/2
 base=[(-1 if u else 1) if t else 1 for t in range(8) for u in [0,1]]
 ph=h.law([-1 if t==0 else 1 for t in range(8)])
 qc=[rho*(ph[t]+(1-2*mu if t==0 else 0))/8+(Q(1,2) if t==0 and u==0 else 0)+((1-2*p)/2 if t==0 and u==1 else 0) for t in range(8) for u in [0,1]]
 ck(sum(qc)==1);qf=h.fullref(qc);rows=[]
 for sign in [1,-1]:
  core=[sign if t==0 else (-1 if u else 1) for t in range(8) for u in [0,1]]
  f=h.full(core);pf=h.law(f);C=h.ce(pf,qf);I=h.influence(f)
  ck(4*I==Q(13,2)-Q(sign,8));ck(all(any(f[t]!=f[t^(1<<i)] for t in range(128)) for i in range(7)))
  select=[t for t in range(128) if ((t>>1)%16)>>1]
  ck(sum(pf[t] for t in select)==Q(7,64));ck(all(qf[t]==rho/2048 for t in select))
  sel=Q(7*(k+11),64);ck(C[0]>=sel)
  W=h.sub(h.sub(h.con(4*I),C),debit(p))
  if k==64:ck(W[1]<Q(-101,64))
  rows.append({'sign':sign,'fourI':str(4*I),'all7_relevant':True,'full_CE':show(C),'selected_cost':str(sel),'W':show(W)})
 # Original padding influence is retired once; no new bank credit is asserted.
 ck(Q(k,16)*rho==sum(Q(1,1<<depth)*(Q(1<<depth)*rho/16) for depth in range(k)))
 ck(Q(5,4)-Q(5,128)==Q(155,128))
 return {'k':k,'profiles':rows,'review':'essential-terminal obstruction and physical influence accounting HOLDS; expected tree proof analytic'}

def main(pilot):
 start=time.perf_counter();out={'status':'RUNNING','mixed':[],'literal':[],'A016':[]}
 ck(31**31>2**152);ck(Q(5,2)-Q(5,64)-Q(1,8)-Q(5,8)==Q(107,64))
 for mask in (range(8) if pilot else range(32)):seed(mask)
 for k in ([5] if pilot else [5,8]):
  for j in ([2] if pilot else [2,3,8]):
   for kr in ([5] if pilot else [0,1,k]):
    patterns=[(mask,)*j for mask in ([0,1,7] if pilot else range(32))]
    if not pilot:patterns.append(tuple(1 if z%2==0 else 30 for z in range(j)))
    for masks in patterns:
     out['mixed'].append(mixed(k,j,kr,masks)[0]);ck(time.perf_counter()-start<60)
   (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 out['literal'].append(literal(pilot));ck(time.perf_counter()-start<60)
 for k in ([64] if pilot else [5,8,16,32,64,128]):out['A016'].append(a016(k));ck(time.perf_counter()-start<60)
 out.update(status='PASS',assertions=N,runtime_seconds=time.perf_counter()-start)
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({'status':'PASS','assertions':N,'mixed_profiles':len(out['mixed']),'literal_frontiers':out['literal'][0]['signed_frontiers'],'A016_widths':len(out['A016']),'runtime_seconds':out['runtime_seconds']}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
