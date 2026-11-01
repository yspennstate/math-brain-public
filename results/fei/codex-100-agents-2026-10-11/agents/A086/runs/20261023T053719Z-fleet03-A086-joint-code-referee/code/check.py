"""Independent exact source inheritance, prescribed floors and full frontier audit."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
from time import perf_counter
import importlib.util, hashlib, json, sys
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[1]/'runs/20261021T203248Z-fleet03-A086-joint-code-referee/code/check.py'
assert hashlib.sha256(OLD.read_bytes()).hexdigest()=='48cd9de1ec443e89be969dd3eac40569c413ddbfafaa9df70e9db1ef238907bc'
spec=importlib.util.spec_from_file_location('own_log_library',OLD); lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)
START=perf_counter(); assertions=histories=0
def ck(b,label):
 global assertions
 assertions+=1
 if not b: raise AssertionError(label)
 if perf_counter()-START>58: raise TimeoutError('frozen 60sec limit')
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def sub(x,y):return add(x,mul(-1,y))
def specp(tab):return tuple(x*x for x in lib.spectrum(tab))
def H(P):return lib.ce(P,P)
def D(P,Q):return sub(lib.ce(P,Q),H(P))
def inherit(tab,Q,j):
 s=sum(Q);children=[lib.child(tab,j,b) for b in (0,1)];P=[specp(t) for t in children]
 m=tuple((x+y)/2 for x,y in zip(*P));r=tuple(Q[lib.bitmask_insert(k,j,0)]+Q[lib.bitmask_insert(k,j,1)] for k in range(len(m)))
 raw=[tuple(r[k]*P[b][k]/m[k] if m[k] else r[k] for k in range(len(m))) for b in (0,1)]
 Z=[sum(v) for v in raw];ck(sum(Z)==2*s and min(Z)>0,'normalizers and zero fibers')
 QQ=[tuple(s*x/Z[b] for x in raw[b]) for b in (0,1)]
 for b in (0,1):ck(sum(QQ[b])==s and all(not pp or qq>0 for pp,qq in zip(P[b],QQ[b])),'mass and coverage')
 # Verify disintegration by atomwise likelihood identity before taking logarithms.
 for b in (0,1):
  for k,pp in enumerate(P[b]):
   if pp:ck(pp/QQ[b][k]==m[k]/r[k]*Z[b]/s,'complete likelihood identity')
 return children,QQ
def point_edit(tab,R,pad=0):
 # One fresh fair controller, zero edit point. Source includes any padding.
 base=tuple(tab[x%len(tab)] for x in range(len(tab)*2**pad));n=(len(base)-1).bit_length();rho=F(1,2**(n+1))
 table=tuple(v-2*base[0]*int(x==0) for x,v in enumerate(base+base));P=specp(table)
 RP=tuple(R[k] if k<len(R) else F(0) for k in range(len(base)))
 beta=6*rho;rd=tuple((v+beta/F(len(base)))/(1+beta) for v in RP)
 marginal=tuple(P[k]+P[k+len(base)] for k in range(len(base)))
 Q=tuple(rd[k%len(base)]*P[k]/marginal[k%len(base)] for k in range(len(P)))
 ck(sum(P)==1 and sum(Q)==(sum(R)+beta)/(1+beta),'floor full mass')
 ck(all(not pp or qq>0 for pp,qq in zip(P,Q)),'floor true support')
 return table,P,Q
def case(tab,s,eta,order):
 global histories
 a=(len(tab)-1).bit_length();Pg=specp(tab);R=tuple(s*((1-eta)*pp+eta/F(len(Pg))) for pp in Pg)
 Ig=lib.influence(tab);c=lib.ce(Pg,R);DD=D(Pg,R);HH=H(Pg)
 root,Pr,Qr=point_edit(tab,R,1);Hr=H(Pr);I=lib.influence(root)
 d=sum(tab[0]!=tab[1<<j] for j in range(a));rho=F(1,2**(a+2));C=2*rho*(a+1-d);J=2*rho;E=2*rho*d
 ck(I==Ig+C-E+J,'literal edge change')
 ck(E<=Ig/4,'original erased edge bound')
 ck(lib.ce(Pr,Qr)[1]<=2*c[0]+30*rho*(a+2)+F(1,2**70),'root envelope')
 ck(Hr[1]<=2*HH[0]+30*rho*(a+2)+F(1,2**70),'aux scalar entropy')
 # First padding query: off branch keeps R, active branch gets fresh floor.
 current=tab;model=R;labels=list(range(a));offD=mul(F(1,2),DD);sourceD=(F(0),F(0));weight=F(1,2)
 active,Pact,Qact=point_edit(current,model)
 L=add(Hr,add(offD,mul(weight,D(Pact,Qact))))
 ck(L[1]<F(3,2)*c[0]+F(41,4)*Ig,'padding full ledger')
 for k,physical in enumerate(order,1):
  idx=labels.index(physical);children,models=inherit(current,model,idx)
  sourceD=add(sourceD,mul(weight/2,D(specp(children[1]),models[1])))
  current,model=children[0],models[0];weight/=2;labels.pop(idx)
  active,Pact,Qact=point_edit(current,model)
  finalD=add(offD,add(sourceD,mul(weight,D(Pact,Qact))));L=add(Hr,finalD)
  ck(sum(model)==s,'original source mass still retained')
  if k<a:
   bound=add(mul(2*(1+F(1,2)),c),(30*rho*(2*a+1+2-k),)*2)
   ck(L[1]<bound[0]+F(1,2**65),'source prefix quantitative bill')
   ck(L[1]<3*c[0]+F(45,4)*Ig,'source prefix influence price')
  else:
   ck(L[1]<=2*c[0]+30*rho*(a+2)+F(1,2**65),'zero-source final bill')
  # C0 is the supplied exact certified upper bound; never refreshed at descendants.
  C0=c[1]/Ig;K=4*C0+15;U=min((C0+1)*Ig,K*(C+J))
  ck(K*I-L[1]>=K*(C+J),'same original rate and margin')
  ck(K*I-L[1]-U>=0,'entire old sufficient allowance')
 histories+=1
def main():
 pilot='--pilot' in sys.argv;batch=int(sys.argv[sys.argv.index('--batch')+1]) if '--batch' in sys.argv else None
 dims=(1,2) if pilot else ((3,) if batch is not None else (1,2,3))
 for a in dims:
  for bits in range(1,2**(2**a)-1):
   if batch is not None and (bits-1)//64!=batch:continue
   tab=tuple(1 if (bits>>x)&1 else -1 for x in range(2**a))
   for s in (F(1),F(1,2)):
    for eta in (F(0),F(1,4)):
     for order in permutations(range(a)):case(tab,s,eta,order)
 result={'status':'PASS','histories':histories,'assertions':assertions,'seconds':perf_counter()-START,'dimensions':dims,'arithmetic':'Fraction and outward96-bit rational logarithm intervals','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 name='PILOT.json' if pilot else (f'BATCH_{batch}.json' if batch is not None else 'EXACT_RESULTS.json')
 (ROOT/'out').mkdir(exist_ok=True);(ROOT/'out'/name).write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':
 try:main()
 except Exception as e:
  (ROOT/'out').mkdir(exist_ok=True);(ROOT/'out'/'FAILURE.json').write_text(json.dumps({'status':'FAIL_OR_INCOMPLETE','error':repr(e),'assertions':assertions,'histories':histories,'seconds':perf_counter()-START}),encoding='utf-8');raise
