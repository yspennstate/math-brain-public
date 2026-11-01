from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time,sys,itertools,hashlib
R=Path(__file__).resolve().parents[1]
H=R.parents[1]/'runs/20261011T223903Z-fleet05-A039-projection-under-restrictions/code/baseline_check.py'
assert hashlib.sha256(H.read_bytes()).hexdigest()=='d6bc7dd1abce58f20c9488cd692818b12a6861d82b0f3c512b391005ab4d2599'
s=importlib.util.spec_from_file_location('logs',H);L=importlib.util.module_from_spec(s);s.loader.exec_module(L)
mul,div,sub,plus=L.mul,L.div,L.minus,L.plus
zero=(F(0),F(0));one=(F(1),F(1));checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
def sumiv(vals):
 o=zero
 for v in vals:o=plus(o,v)
 return o
def scale(c,v):return mul((F(c),F(c)),v)
def kl(p,q):return sumiv(scale(x,L.log_iv(div((x,x),y))) for x,y in zip(p,q) if x)
def enc(v):return [str(x) for x in v]
def info(t):
 p=L.law(t);n=len(t).bit_length()-1;d=L.marg(p,n)
 ck(sum(p)==1)
 for j in range(n):ck(d[j]==F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t)))
 h=L.evalformal(L.ent(p));tc=L.evalformal(L.add(*[(1,L.h(x)) for x in d],(-1,L.ent(p))))
 surplus=sub((4*sum(d),4*sum(d)),h)
 if L.add((4*sum(d),L.L(F(2))),(-1,L.ent(p)))=={}:surplus=zero
 return p,d,h,tc,surplus
def rootref(p,d):
 v=1-p[0];r=[x/v for x in d]
 def g(c):
  w=F(1)
  for x in r:w*=1-c*x
  return 1-c-w
 lo,hi=F(0),F(1);ck(g(hi)<0);ck(sum(r)>1)
 for _ in range(48):
  m=(lo+hi)/2
  if g(m)>0:lo=m
  else:hi=m
 ck(lo>0 and g(lo)>0 and g(hi)<0)
 c=(lo,hi);theta=[scale(x,c) for x in r];q=[]
 for t in range(len(p)):
  if t==0:q.append((p[0],p[0]));continue
  a=(v,v)
  for j in range(len(d)):a=mul(a,theta[j] if t>>j&1 else sub(one,theta[j]))
  q.append(div(a,c))
 ck(sumiv(q)[0]<=1<=sumiv(q)[1])
 for j,x in enumerate(d):
  a=sumiv(q[t] for t in range(len(q)) if t>>j&1);ck(a[0]<=x<=a[1])
 return q,c
def erase(v,i):
 return [plus(v[t],v[t|(1<<i)]) for t in range(len(v)) if not t>>i&1]
def step(tab,q,i):
 p=L.law(tab);children=[L.restrict(tab,i,y) for y in [0,1]];ps=[L.law(t) for t in children]
 fused=[p[t]+p[t|(1<<i)] for t in range(len(p)) if not t>>i&1]
 ck(fused==[(x+y)/2 for x,y in zip(*ps)])
 qr=erase(q,i);k=[[ps[y][t]/(2*fused[t]) if fused[t] else F(1,2) for t in range(len(fused))] for y in [0,1]]
 out=[sumiv(scale(k[y][t],qr[t]) for t in range(len(qr))) for y in [0,1]]
 qc=[[div(scale(k[y][t],qr[t]),out[y]) for t in range(len(qr))] for y in [0,1]]
 E=sub(kl(p,q),kl(fused,qr));E=(max(F(0),E[0]),E[1]) # exact conditional KL is nonnegative
 O=kl([F(1,2),F(1,2)],out)
 ledger=plus(E,plus(O,scale(F(1,2),sumiv(kl(ps[y],qc[y]) for y in [0,1]))))
 A=kl(p,q);ck(ledger[0]<=A[1] and A[0]<=ledger[1])
 rows=sum(x==0 for x in fused)
 return children,qc,E,O,rows
def quotient(v):
 # On four-variable leaves ordered x,b,data,data, forget the data block.
 return [sum((v[t] for t in range(len(v)) if t&3==u),F(0)) for u in range(4)]
def quotient_iv(v):return [sumiv(v[t] for t in range(len(v)) if t&3==u) for u in range(4)]
def run_core(code):
 v=[1 if code>>j&1 else -1 for j in range(8)]
 tab=[-1 if not (t&1) and t&2 else (v[t>>3] if t&1 and t&4 else 1) for t in range(64)]
 p,d,_,_,_=info(tab);Q,c=rootref(p,d);A=kl(p,Q)
 tabs,qs,E0,O0,rows0=step(tab,Q,1);edges={}
 for y,j in itertools.product(range(2),range(3)):
  edges[y,j]=step(tabs[y],qs[y],2+j)
  for t in edges[y,j][0]:info(t)
 policies=[]
 for j0,j1 in itertools.product(range(3),repeat=2):
  leaves=[];refs=[];E=E0;O=O0;rows=rows0
  for y,j in enumerate([j0,j1]):
   ts,qq,e,o,rr=edges[y,j];leaves+=ts;refs+=qq;E=plus(E,scale(F(1,2),e));O=plus(O,scale(F(1,2),o));rows+=rr
  facts=[info(t) for t in leaves]
  h=scale(F(1,4),sumiv(f[2] for f in facts));tc=scale(F(1,4),sumiv(f[3] for f in facts));S=scale(F(1,4),sumiv(f[4] for f in facts))
  ck(all(f[4][0]>=0 for f in facts))
  inh=scale(F(1,4),sumiv(kl(f[0],q) for f,q in zip(facts,refs)))
  sigma=sub(tc,inh);D=sub(plus(O,tc),A);direct=sub(sigma,E)
  ck(D[0]<=direct[1] and direct[0]<=D[1])
  conditional=[];quotient_sigma=[]
  for f,q in zip(facts,refs):
   pp,dd=f[:2];rp=L.product(dd);pq=quotient(pp);qq=quotient_iv(q);rq=quotient(rp)
   inherited_cond=sub(kl(pp,q),kl(pq,qq));fresh_cond=sub(kl(pp,[(x,x) for x in rp]),kl(pq,[(x,x) for x in rq]))
   conditional.append(sub(fresh_cond,inherited_cond));quotient_sigma.append(sub(kl(pq,[(x,x) for x in rq]),kl(pq,qq)))
  cs=scale(F(1,4),sumiv(conditional));qsig=scale(F(1,4),sumiv(quotient_sigma));decomp=plus(cs,qsig)
  ck(decomp[0]<=sigma[1] and sigma[0]<=decomp[1])
  margins={str(a):sub(scale(a,S),(max(F(0),D[0]),max(F(0),D[1]))) for a in [F(1,8),F(1,4),F(1,2),F(1)]}
  policies.append({'policy':[j0,j1],'D':enc(D),'surplus':enc(S),'terminal_H':enc(h),'margins':{k:enc(z) for k,z in margins.items()},'conditional_sigma':enc(cs),'quotient_sigma':enc(qsig),'reference_only_rows':rows})
 return {'core_code':code,'core_table':v,'c':enc(c),'root_A':enc(A),'policies':policies}
def main(pilot=False):
 start=time.perf_counter();limit=60 if pilot else 1200;out=[];accepted=[]
 for code in ([254] if pilot else range(256)):
  v=[1 if code>>j&1 else -1 for j in range(8)];vp=L.law(v);d=L.marg(vp,3)
  if not all(d) or len(set(x for x in vp if x))<=1:continue
  accepted.append(code);res=run_core(code);out.append(res)
  (R/'out'/('PILOT.json' if pilot else 'MIXED_CHECK.json')).write_text(json.dumps({'completed':len(out),'results':out},indent=2),encoding='utf-8')
  L.log2.cache_clear();ck(time.perf_counter()-start<limit)
 policies=[p for r in out for p in r['policies']];worst={}
 for a in ['1/8','1/4','1/2','1']:
  p=min(policies,key=lambda p:F(p['margins'][a][0]));worst[a]={'minimum_margin':p['margins'][a],'policy':p['policy'],'certified_policies':sum(F(p['margins'][a][0])>=0 for p in policies)}
 summary={'status':'COMPLETE','accepted_cores':len(accepted),'policies':len(policies),'checks':checks,'runtime_seconds':time.perf_counter()-start,'payment_tests':worst,'max_reference_only_rows':max(p['reference_only_rows'] for p in policies)}
 (R/'out'/('PILOT_SUMMARY.json' if pilot else 'SUMMARY.json')).write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary))
if __name__=='__main__':main('--pilot' in sys.argv)
