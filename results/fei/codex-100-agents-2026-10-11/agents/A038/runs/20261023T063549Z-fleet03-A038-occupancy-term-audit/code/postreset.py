import json,sys,time
from pathlib import Path
from fractions import Fraction as F
import baseline as b
import interval_primitives as m
R=Path(__file__).resolve().parents[1];V=m.V;start=time.monotonic();count=0
def check(x,label):
 global count
 count+=1
 assert x,label
 if time.monotonic()-start>55:raise RuntimeError('55 second watchdog')
def overlap(a,c,label):check(a.a<=c.b and c.a<=a.b,label+' (diagnostic)')
def source(t):return b.source(t)
def norm(q):
 mass=sum(q,V(0));check(mass.a>0,'actual inherited reference normalizer positive')
 return [x/mass for x in q]
def root(k):
 if k==3:return b.make_root()
 t=[];dim=k+4
 for v in range(1<<dim):
  x,a,bb=[v>>j&1 for j in range(3)]
  core=(-1 if v>>(k+3)&1 else 1)*(-1 if (v>>3)&((1<<k)-1)==0 else 1)
  t.append((-1 if a else 1) if not x else (core if bb else 1))
 N=source(t);var=1-N['p'][0];r=[d/var for d in N['d']]
 def f(c):
  p=F(1)
  for d in r:p*=1-c*d
  return 1-c-p
 lo,hi=F(3,4),F(1);check(f(lo)>0>f(hi),'canonical bracket')
 der=F(0)
 for j,d in enumerate(r):
  v=d
  for ii,e in enumerate(r):
   if ii!=j:v*=1-lo*e
  der+=v
 check(der<1,'canonical root uniqueness on bracket')
 for _ in range(42):
  mid=(lo+hi)/2
  if f(mid)>0:lo=mid
  else:hi=mid
 c=V(lo,hi);q=[]
 for s in range(1<<dim):
  if s==0:q.append(V(1-var));continue
  v=V(var)/c
  for j,d in enumerate(r):v*=c*d if s>>j&1 else 1-c*d
  q.append(v)
 check(sum(q,V(0)).a<=1<=sum(q,V(0)).b,'canonical normalization')
 return N,q,m.kl(N['p'],q),c
def canonical(N):
 if N['p'][0]==0 and F(1) in N['d']:q=b.product_q(N['d'])
 else:q=N['p'][:]
 check(sum(q)==1 and q[0]==N['p'][0],'actual prescribed reset canonical boundaries')
 return [V(x) for x in q]
def run(k,policy):
 N,q,A,c=root(k);names=['x','a','b']+['y'+str(j) for j in range(k)]+['z']
 old=[];new=[];pre_releases=V(0);post_releases=V(0);B=V(0);positiveO=0;referenceonly=0;rows=[]
 def split(n,qq,nn,w,label):
  nonlocal referenceonly,positiveO
  i=nn.index(label);rest=nn[:i]+nn[i+1:];out=m.push(n,qq,i)
  pp=m.push(n,[V(p) for p in n['p']],i);kids=[source(m.restrict(n['t'],i,s)) for s in range(2)]
  for s in range(2):
   for got,p in zip(pp[s],kids[s]['p']):check(got.a==got.b==p/2,'exact physical coherent kernel')
  qn=norm(qq);barp=[];barq=[]
  for s in range(len(qq)):
   if s>>i&1:continue
   barp.append(n['p'][s]+n['p'][s|1<<i]);barq.append(qn[s]+qn[s|1<<i])
   if barp[-1]==0 and barq[-1].a>0:referenceonly+=1
  Kin=m.kl(n['p'],qn);E=Kin-m.kl(barp,barq)
  mass=sum(qq,V(0));O=m.kl([F(1,2)]*2,[sum(row,V(0))/mass for row in out])
  if O.a>0:positiveO+=1
  Kchild=sum((m.kl(kids[s]['p'],norm(out[s]))/2 for s in range(2)),V(0))
  overlap(Kin,E+O+Kchild,'current-reference complete KL chain')
  return kids,out,rest,(E+O)*w,O
 def post(n,qq,nn,w,path):
  nonlocal post_releases
  if not path:
   new.append((n,qq,nn,w));return
  kids,out,rest,release,O=split(n,qq,nn,w,path[0]);post_releases+=release
  for s in range(2):post(kids[s],out[s],rest,w/2,path[1:])
 def pre(n,qq,nn,w,path,values):
  nonlocal pre_releases,B
  if not path:
   old.append((n,qq,nn,w))
   if 'x' in nn:
    new.append((n,qq,nn,w));return
   qnew=canonical(n);K=m.kl(n['p'],qnew);B+=K*w
   check(K.b<=F(7,8),'initial canonical reset KL price')
   oldK=m.kl(n['p'],norm(qq))
   rows.append({'physical_weight':str(w),'old_inherited_KL':oldK.out(),'booked_reset_KL':K.out(),'prefix_values':values})
   paths=[['y1'],['y0'],['y0','y1'],['z'] if values.get('y0')==0 else ['y1']]
   post(n,qnew,nn,w,paths[policy]);return
  lab=path[0];kids,out,rest,release,O=split(n,qq,nn,w,lab);pre_releases+=release
  for s in range(2):
   tail=[] if lab=='b' and s==0 else path[1:]
   pre(kids[s],out[s],rest,w/2,tail,{**values,lab:s})
 paths=[['b','y0','x'],['b','z','x'],['b','x'],['b','y0','x']]
 pre(N,q,names,F(1),paths[policy],{})
 def stats(front):
  H=sum((n['H']*w for n,qq,nn,w in front),V(0));If=sum((n['I']*w for n,qq,nn,w in front),F(0))
  return H,If,4*If-H
 H0,I0,S0=stats(old);H1,I1,S1=stats(new)
 L0=A+m.positive(N['H']-H0-4*(N['I']-I0));U=m.positive(H0-H1-4*(I0-I1))
 oldK=sum((m.kl(n['p'],norm(qq))*w for n,qq,nn,w in old),V(0))
 overlap(A,pre_releases+oldK,'complete original M bill retained')
 # b0's inherited bill stays inside L0, not B. Only descendants of RESET leaves split B.
 terminalK=sum((m.kl(n['p'],norm(qq))*w for n,qq,nn,w in new if 'x' not in nn),V(0))
 overlap(B,post_releases+terminalK,'whole first reset B retained under transport')
 check(S0.a>=2 and S1.a>=2,'old and new complete terminal surplus floors')
 check(L0.b<F(39,32),'strong bound on actual old whole booking, not just A')
 check(B.b<=F(7,32),'first reset debit retained')
 residue=S1-L0-B-F(11,32)-U
 check(residue.a>F(7,32),'old L0 plus old B plus old omega plus NEW U paid')
 overlap(residue,V(min(S0.a,S1.a),min(S0.b,S1.b))-L0-B-F(11,32),'separate-account min identity')
 for n,qq,nn,w in new:check(n['H'].b<=4*n['I'],'all new terminal hereditary certificates')
 check(sum(w for n,qq,nn,w in old)==sum(w for n,qq,nn,w in new)==1,'all complementary terminal weights retained')
 if k==3 and policy==2:check(B.a>0 and positiveO>0,'genuine positive reset and nonfair current outcome exercised')
 if k==4:check(B.a>0,'positive reset AFTER a proper active pre-data query')
 return {'m':k,'policy':policy,'A':A.out(),'S0':S0.out(),'S1':S1.out(),'L0':L0.out(),'B0':B.out(),'new_U':U.out(),'omega':'11/32','remaining':residue.out(),'post_releases':post_releases.out(),'post_terminal_KL':terminalK.out(),'positive_outcome_nodes':positiveO,'reference_only_rows':referenceonly,'reset_frontier':rows,'old_terminal_count':len(old),'new_terminal_count':len(new)}
def scalar():
 out=[]
 check(F(25,36)<F(3,4),'natural log2 upper bound')
 check(F(21,64)>F(1,4),'empty-entropy repair gap')
 for k in range(1,17):
  eps=F(1,2**k);p0=(1-2*eps)**2
  H=-(p0*m.lg(p0) if p0 else V(0))-(2**k-1)*4*eps**2*m.lg(4*eps**2)
  I=2*k*eps;check(H.a>=8*(k-1)*eps,'new exact lower entropy bound')
  check((4*I-H).b<=8*eps,'point-defect stopping surplus potential')
  if k>=3:
   check(F(2,3)*(1-eps)*(1-2*eps)**2>=F(21,64),'empty-entropy uniform lower factor')
   check((k-1)*eps<=F(1,4),'decreasing k epsilon')
  out.append({'k':k,'H':H.out(),'I':str(I),'V':str(8*eps)})
 for k in range(3,17):
  eps=F(1,2**k);G=2*m.h(F(1,4))+k*m.h(eps/2)
  bound=G-1-2*(k-1)*eps
  check(bound.b<F(39,32),'full old booking envelope')
 # Exact potential extremizers: stop point tree at k=2, keeping z.
 extremizers=[]
 for k in [3,4]:
  mean=4+F(1,2**(k-2))*2
  check(mean==4+F(8,2**k),'exact stopping potential attainment')
  extremizers.append({'m':k,'mean_core_surplus':str(mean),'stop_active_k':2})
 return out,extremizers
if __name__=='__main__':
 scalar_rows,extremizers=scalar();domain=[(3,0)] if '--pilot' in sys.argv else [(3,j) for j in range(4)]+[(4,0)]
 histories=[run(k,p) for k,p in domain]
 out={'status':'PASS','assertions':count,'baseline_assertions':b.COUNT,'primitive_assertions':m.COUNT,'runtime_seconds':time.monotonic()-start,'histories':histories,'scalar_rows':scalar_rows,'potential_extremizers':extremizers,'identity_rung':'analytic chain rule; interval overlaps diagnostics only'}
 name='PILOT.json' if '--pilot' in sys.argv else 'CHECK.json'
 (R/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
 print(json.dumps({k:out[k] for k in ['status','assertions','baseline_assertions','primitive_assertions','runtime_seconds']}))
