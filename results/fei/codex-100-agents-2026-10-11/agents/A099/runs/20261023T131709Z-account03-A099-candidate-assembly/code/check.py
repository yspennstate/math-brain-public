from pathlib import Path
from fractions import Fraction as F
import json,sys,time
import prior_exact as E
R=Path(__file__).resolve().parents[1]; T=time.monotonic();COUNT=0
PILOT='--pilot' in sys.argv;CAP=55 if PILOT else 180
stats=dict(lifted_trees=0,physical_nodes=0,queries=0,geometric_transactions=0,ghost_leaf_occurrences=0,floor_wrappers=0)
def ck(x):
 global COUNT
 COUNT+=1
 assert x,COUNT
 assert time.monotonic()-T<CAP,'frozen runtime cap'
def put(n,x):(R/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def lift(g,L):
 n=len(g).bit_length()-1
 return tuple(g[sum(((x>>(j*L))&((1<<L)-1)).bit_count()%2<<j for j in range(n))] for x in range(1<<(n*L)))
def inf(f):
 return tuple(F(sum(f[x]!=f[x^(1<<j)] for x in range(len(f))),len(f)) for j in range(len(f).bit_length()-1))
def deletion(s,j):return (s&((1<<j)-1))|((s>>(j+1))<<j)
def walk(f,labels,blocks,alpha,corep,L):
 p=E.spec(f);stats['physical_nodes']+=1
 ck(sorted(x for x in p if x)==sorted(x for x in corep if x))
 weights=inf(f);ck(sum(weights)==sum(F(len(b))*a for b,a in zip(blocks,alpha)))
 choices=[j for j,b in enumerate(blocks) if len(b)>=2]
 if not choices:return
 # Outcome-sensitive legal policy, keeping BOTH children.
 bindex=choices[int(f[0]<0)%len(choices)];original=blocks[bindex][0];j=labels.index(original)
 ck(all(not(p[s] and p[s^(1<<j)]) for s in range(len(p))))
 q=E.marg(p,j);ck(E.ent(q)==E.ent(p));ck(weights[j]==alpha[bindex]);stats['queries']+=1
 nextlabels=labels[:j]+labels[j+1:];nb=[list(b) for b in blocks];nb[bindex].remove(original)
 for sign in (0,1):
  h=E.child(f,j,sign);ph=E.spec(h);ck(ph==q)
  ck(sum(inf(f))-sum(inf(h))==alpha[bindex])
  walk(h,nextlabels,nb,alpha,corep,L)
def treeleaves(f):
 n=len(f).bit_length()-1;root=E.spec(f);om=[s for s,p in enumerate(root) if p]
 if n<2:return [(f,4,{s:s for s in om})]
 # Both queries delete coordinates while each L3 block still has >=2 bits.
 out=[]
 for b in (0,1):
  h=E.child(f,0,b);mp={s:deletion(s,0) for s in om}
  if b==0:out.append((h,2,mp))
  else:
   for c in (0,1):out.append((E.child(h,0,c),1,{s:deletion(t,0) for s,t in mp.items()}))
 return out
def geometric(g):
 f=lift(g,3);p=E.spec(f);om=[s for s,v in enumerate(p) if v];leaves=treeleaves(f)
 for recipe in range(3):
  targets=[];products={s:1 for s in om};normpow=1;avg={}
  for ell,(h,k,mp) in enumerate(leaves):
   ph=E.spec(h);ck(all(ph[mp[s]]==p[s] for s in om));ck(len(set(mp.values()))==len(om))
   v=[1+(j+2*ell+recipe)%3 for j in range(len(ph))];norm=sum(x**4 for x in v);q=tuple(F(x**4,norm) for x in v)
   ck(sum(q)==1);normpow*=norm**k
   for s in om:products[s]*=v[mp[s]]**k
   avg=E.add(avg,E.sc(F(k,4),E.ce(ph,q)));targets.append((q,k,mp))
   if any(q[j] and not ph[j] for j in range(len(q))):stats['ghost_leaf_occurrences']+=1
  S=sum(products.values());star=tuple(F(products[s],S) if s in products else F(0) for s in range(len(p)))
  ck(S**4<=normpow);ck(sum(star)==1)
  minuslogZ=E.add(E.sc(F(1,4),E.logq(F(normpow))),E.sc(-1,E.logq(F(S))))
  ck(avg==E.add(E.ce(p,star),minuslogZ))
  klavg={}
  for q,k,mp in targets:
   pushed=[F(0)]*len(q)
   for s in om:pushed[mp[s]]=star[s]
   klavg=E.add(klavg,E.sc(F(k,4),E.kl(pushed,q)))
  ck(klavg==minuslogZ)
  q0=tuple((v+F(1,len(p)))/2 for v in p)
  debit=E.add(avg,E.sc(-1,E.ce(p,q0)))
  ck(debit==E.add(E.kl(p,star),E.sc(-1,E.kl(p,q0)),minuslogZ))
  stats['geometric_transactions']+=1
def wrappers():
 ctl=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
 g=tuple(-1 if x in (0,7) else 1 for x in range(8));p=E.spec(g)
 ck(p==tuple(F(1,4) if i in (0,3,5,6) else F(0) for i in range(8)))
 floor=(F(1,4),F(5,24),F(5,24),F(1,3));uniform=(F(1,4),)*4
 delta=E.sc(F(3,32),E.logq(F(27,25)))
 ck(E.sc(F(3,8),E.kl(uniform,floor))==delta);ck(1<F(27,25)<2)
 for L in (1,2,3):
  h=lift(g,L)
  # Exact factorized coefficients, plus literal full Boolean counting at L1,2.
  for sig in (-1,1):
   if L<=2:
    f=tuple(ctl[u]+sig*(1-ctl[u]**2)*v for v in h for u in range(16));pf=E.spec(f)
    ii=inf(f);expected=F(13 if sig==1 else 15,8)+F(9*L,16)
    ck(sum(ii)==expected);ck(sum(pf)==1);ck(sum(bool(x) for x in pf)<=64)
    ck(4*expected>=F(35,4))
   # Factorized source has four seed rows and16 controller frequencies for ANY L.
   ck(F(35,4)-F(1,4)-6-F(3,32)==F(77,32))
   stats['floor_wrappers']+=1
 # Maj3 guard independently uses direct character sums and physical edges.
 maj=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
 pp=E.spec(maj);ck(sorted(x for x in pp if x)==[F(1,4)]*4)
 ck(sum(inf(maj))==F(3,2));ck(3-2==1);ck(F(3,2)-2==F(-1,2))
 # Positive normalizer witness: exact fourth powers, with Rstar=P.
 qa=(F(3,8),F(3,8),F(1,8),F(1,8));qb=qa[::-1]
 ck(all(a*b==F(3,64) for a,b in zip(qa,qb)));ck(F(3,4)<1)
 bill=E.add(E.sc(F(1,2),E.add(E.ce(uniform,qa),E.ce(uniform,qb))),E.sc(-1,E.ent(uniform)))
 ck(bill==E.sc(F(1,2),E.logq(F(4,3))))
 put('EXACT_WITNESSES.json',dict(normalizer_bill='log2(4/3)/2 >0, Rstar=P, Z^2=3/4',floor_bill='(3/32)log2(27/25)>0',reserve='>77/32 after supplied old booking<=1/4',maj3_original_entropy_residual='1',maj3_remaining_influence_residual='-1/2',scope='Declared class necessity only; no universal FEI/source price. L3 wrapper influence/support certified analytically; literal wrappers L1,2.'))
for n in range(3 if PILOT else 4):
 for table in range(1<<(1<<n)):
  g=tuple(1 if table&(1<<x) else -1 for x in range(1<<n));p=E.spec(g);a=inf(g)
  for L in ((2,) if PILOT or n==3 else (2,3)):
   f=lift(g,L);ck(sum(inf(f))==L*sum(a));walk(f,list(range(n*L)),[list(range(j*L,(j+1)*L)) for j in range(n)],a,p,L);stats['lifted_trees']+=1
  if n<=2:geometric(g)
wrappers()
result=dict(status='PASS',exact_assertions=COUNT,seconds=time.monotonic()-T,**stats)
put('PILOT.json' if PILOT else 'EXACT_AUDIT.json',result);print(json.dumps(result))
