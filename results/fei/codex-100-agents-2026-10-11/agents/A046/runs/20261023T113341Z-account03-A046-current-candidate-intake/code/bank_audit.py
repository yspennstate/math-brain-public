import check as c
from fractions import Fraction as F
import json,time
R=c.R;start=time.perf_counter()
spec={'helper_version':'original-bank-v1','family':'F_g for frozen g=chi_z*d6*d(k+1), k=1,2; whole-core root spike1/8; actual first activation reset1/7, then query i and full samealpha reset','cases':2,'terminals_per_case':5,'symmetry':'none; both signs/outcomes retained','arithmetic':'Fraction FWHT, actual normalized kernels,32-term certified logarithms; shared primitives with main checker, no external independence claimed','memory_MB':100,'max_seconds':55}
(R/'out/BANK_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
def H(p):
 out=(F(0),F(0))
 for v in p:
  if v:out=c.sub(out,c.scale(c.log2(v),v))
 return out
def I(p):return sum(F(t.bit_count())*v for t,v in enumerate(p))
def surplus(p):return c.sub((4*I(p),4*I(p)),H(p))
def query(vals,Q,i):
 P=c.spectrum(vals);old=c.kl(P,Q);E=c.erase(P,i);D=c.erase(Q,i)
 children=[];Zs=[];mean=(F(0),F(0))
 for b in (0,1):
  v=c.restrict(vals,i,b);p=c.spectrum(v)
  raw=[d*(pc/(2*e) if e else F(1,2)) for e,d,pc in zip(E,D,p)]
  Z=sum(raw);q=[x/Z for x in raw];Zs.append(Z)
  mean=c.add(mean,c.scale(c.kl(p,q),F(1,2)));children.append((v,q))
 release=c.sub(old,mean)
 erased_loss=c.sub(old,c.kl(E,D));outcome=c.kl([F(1,2),F(1,2)],Zs)
 c.overlap(release,c.add(erased_loss,outcome))
 return children,release
records=[]
for k in (1,2):
 r=6;n=r+k+2;i=r+1
 g=[]
 for x in range(1<<n):
  g.append((-1 if x&1 else 1)*(-1 if ((x>>1)&63)==63 else 1)*(-1 if ((x>>i)&((1<<(k+1))-1))==(1<<(k+1))-1 else 1))
 vals=[]
 for u in range(1<<(n+3)):
  x=u&1;a=(u>>1)&1;b=(u>>2)&1
  vals.append((-1 if a else 1) if not x else g[u>>3] if b else 1)
 P=c.spectrum(vals);qcore=c.fresh_core(g,F(1,8));Q=list(P)
 for t in range(1,len(qcore)):
  for control in (0,1,4,5):Q[8*t+control]=qcore[t]/16
 c.eq(sum(Q),1)
 A0=c.kl(P,Q);M0=c.sub(c.sub((4*I(P),4*I(P)),H(P)),A0)
 bs,relb=query(vals,Q,2);releases=relb
 terminal=[(F(1,2),bs[0][0],bs[0][1])]
 ass,rela=query(bs[1][0],bs[1][1],1);releases=c.add(releases,c.scale(rela,F(1,2)))
 sig1=sig2=(F(0),F(0))
 for a,(va,qa) in enumerate(ass):
  s=1 if a==0 else -1
  pa,fresh=c.lifted(g,s,F(1,7));c.eq(c.spectrum(va),pa)
  sig1=c.add(sig1,c.scale(c.sub(c.kl(pa,fresh),c.kl(pa,qa)),F(1,4)))
  iss,reli=query(va,fresh,i+1);releases=c.add(releases,c.scale(reli,F(1,4)))
  for b,(vb,qb) in enumerate(iss):
   core=c.restrict(g,i,b);pb,new=c.lifted(core,s,F(1,7));c.eq(pb,c.spectrum(vb))
   sig2=c.add(sig2,c.scale(c.sub(c.kl(pb,new),c.kl(pb,qb)),F(1,8)))
   terminal.append((F(1,8),vb,new))
 c.overlap(sig2,c.scale(c.grouped(6,k,F(1,7)),F(1,2)))
 assert sig2[0]>F(1,4096)
 S=K=(F(0),F(0));terminal_records=[]
 for reach,v,q in terminal:
  p=c.spectrum(v);s=surplus(p);kl=c.kl(p,q)
  S=c.add(S,c.scale(s,reach));K=c.add(K,c.scale(kl,reach))
  terminal_records.append({'reach':str(reach),'surplus_interval':[str(x) for x in s],'terminal_KL':[str(x) for x in kl]})
 sigma=c.add(sig1,sig2);c.overlap(c.add(A0,sigma),c.add(releases,K))
 remaining=min(S[0],M0[0]-sigma[1])-F(1,4);assert remaining>=F(3,4)
 records.append({'k':k,'terminals':terminal_records,'first_sigma':[str(x) for x in sig1],'second_sigma':[str(x) for x in sig2],'root_margin':[str(x) for x in M0],'same_bank_remaining_lower':str(remaining)})
 assert time.perf_counter()-start<55
out={'status':'PASS','cases':2,'terminals':10,'seconds':time.perf_counter()-start,'assertions':c.CHECKS,'same_original_account':True,'old_quarter_retained':True,'records':records}
(R/'out/BANK_AUDIT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
