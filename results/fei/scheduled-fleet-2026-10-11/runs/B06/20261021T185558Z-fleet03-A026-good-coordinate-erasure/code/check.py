import json,time,sys,itertools
from fractions import Fraction as Q
from pathlib import Path
import core as c
R=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0
def eq(a,b):
 global checks
 assert a==b,(a,b);checks+=1
def add(a,b,k=1):
 z=dict(a);c.add(z,b,k);return z
def scale(a,k):return add({},a,k)
def sub(a,b):return add(a,b,-1)
def av(a,b):return add(scale(a,Q(1,2)),b,Q(1,2))
def nonneg(a):
 global checks
 c.positive(a);checks+=1
def info(g,h):
 Wg=c.b.walsh(g);Wh=c.b.walsh(h);N=len(g);P={}
 for u,v in zip(Wg,Wh):c.add(P,c.phi(Q(u*u,N*N),Q(v*v,N*N)))
 return sub(c.const(1),scale(P,Q(1,2)))
enc=tuple(1 if x.bit_count()>=2 else -1 for x in range(8))
eq(c.physical(enc)['H'],c.const(2));eq(c.physical(enc)['mu'],0)
def node(g,h,check_compose=True):
 shadow=tuple(x for pair in zip(h,g) for x in pair)
 s=c.shadow(shadow,False);T=av(c.physical(g)['H'],c.physical(h)['H']);J=info(g,h)
 predicted=add(add(T,J),s['B']);predicted=add(predicted,c.const(2*s['delta']))
 if check_compose:
  f=c.compose(shadow,enc);pf=c.physical(f);eq(pf['H'],predicted)
 else:pf={'H':predicted}
 return {'g':g,'h':h,'T':T,'J':J,'B':s['B'],'delta':s['delta'],'H':predicted,'Iprod':s['Ip'],'pf':pf}
def children(n,i):return [node(c.split(n['g'],i,b),c.split(n['h'],i,b)) for b in [0,1]]
pilot='--pilot' in sys.argv
identity_rows=0
for n in ([1] if pilot else [1,2]):
 for _,g in c.tables(n):
  for _,h in c.tables(n):
   x=node(g,h)
   for i in range(n):
    ch=children(x,i)
    eq(av(c.const(ch[0]['delta']),c.const(ch[1]['delta'])),c.const(x['delta']))
    debit=sub(add(sub(x['H'],av(ch[0]['H'],ch[1]['H'])),av(ch[0]['B'],ch[1]['B'])),x['B'])
    debit=sub(debit,sub(x['T'],av(ch[0]['T'],ch[1]['T'])))
    eq(debit,sub(x['J'],av(ch[0]['J'],ch[1]['J'])))
    identity_rows+=1
    assert time.perf_counter()-start<55
def bent(m):return tuple((-1)**sum(((x>>(2*k))&1)*((x>>(2*k+1))&1) for k in range(m//2)) for x in range(1<<m))
def family(m):
 H=bent(m);G=tuple(-1 if x==0 else 1 for x in range(1<<(m+1)))
 # j is the least significant data coordinate.
 H=tuple(H[x>>1] for x in range(len(G)))
 return G,H
def formula(m):
 t=Q(1,1<<m);a=(1-t)**2;b=(1-2*t)**2
 D=scale(c.phi(1,t),Q(1,4));c.add(D,c.phi(b,t),Q(1,4));c.add(D,c.phi(a,t),Q(-1,2))
 v=scale(c.phi(4*t*t,t),Q(1,4));c.add(v,c.phi(t*t,t),Q(-1,2));c.add(D,v,(1<<m)-1)
 return D
fixtures=[]
for m in ([2] if pilot else [2,4,6]):
 g,h=family(m);N=len(g);x=node(g,h);ch=children(x,0);D=sub(x['J'],av(ch[0]['J'],ch[1]['J']))
 eq(D,formula(m));t=Q(1,1<<m)
 pg=c.physical(g);ph=c.physical(h)
 eq(ph['H'],c.const(m));eq(ph['I'],Q(m,2));eq(pg['I'],(m+1)*t)
 eq(x['pf']['d'][3],t/2)
 release=(x['Iprod']-(ch[0]['Iprod']+ch[1]['Iprod'])/2)/2
 eq(release,t/2)
 for z in ch:eq(len(set(c.compose(tuple(v for pair in zip(z['h'],z['g']) for v in pair),enc))),2)
 nonneg(sub(c.const(4*pg['I']),pg['H']));nonneg(sub(c.const(4*ph['I']),ph['H']))
 S=sub(c.const(2*(pg['I']+ph['I'])),x['T'])
 original_booked=sub(sub(S,x['B']),c.const(x['delta']))
 remaining=sub(original_booked,D)
 extra=add(av(ch[0]['J'],ch[1]['J']),c.const(x['delta']))
 full=sub(remaining,extra)
 eq(full,sub(c.const(2*(pg['I']+ph['I'])),x['H']))
 if m>=4:nonneg(sub(D,c.const(t*(Q(m,2)-3))))
 fixtures.append({'m':m,'physical_data_I_j':str(t/2),'release_R':str(release),'disagreement_delta':str(x['delta']),'signed_JS_debit':c.b.serial(D),'debit_interval':list(map(str,c.interval(D))),'debit_over_I_interval':[str(v/(t/2)) for v in c.interval(D)],'original_booked_margin_interval':list(map(str,c.interval(original_booked))),'post_query_margin_interval':list(map(str,c.interval(remaining))),'full_margin_interval':list(map(str,c.interval(full)))})
 (R/'out/ACTUAL_FIXTURES.json').write_text(json.dumps(fixtures,indent=2)+'\n',encoding='utf-8')
 assert time.perf_counter()-start<55
symbolic=[]
if not pilot:
 for m in [4,6,8,10,12]:
  t=Q(1,1<<m);D=formula(m);nonneg(sub(D,c.const(t*(Q(m,2)-3))))
  symbolic.append({'m':m,'lower_bound_debit_over_I':m-6,'actual_debit_over_I_interval':[str(v/(t/2)) for v in c.interval(D)]})
 # Three adaptive data policies. Keep BOTH full actual terminal signs at every leaf.
 policies=['increasing','decreasing','adaptive'];tree_rows=[]
 for policy in policies:
  g,h=family(4);root=node(g,h);Jsum={};dropH={};dropT={};leaves=[];data_spend=Q(0);visits=0
  def walk(g,h,labels,reach,depth):
   global visits,data_spend
   z=node(g,h);visits+=1
   # Stop at two different proper depths depending on the realized history.
   stop=(not labels) or (depth>=3 and ((sum(g)+sum(h))%5==0))
   if stop:
    leaves.append((reach,z));return
   i=0 if policy=='increasing' else len(labels)-1 if policy=='decreasing' else (depth+int(sum(g)>sum(h)))%len(labels)
   ch=children(z,i);c.add(Jsum,sub(z['J'],av(ch[0]['J'],ch[1]['J'])),reach)
   c.add(dropH,sub(z['H'],av(ch[0]['H'],ch[1]['H'])),reach)
   c.add(dropT,sub(z['T'],av(ch[0]['T'],ch[1]['T'])),reach)
   local=(c.physical(g)['d'][i]+c.physical(h)['d'][i])/2
   data_spend+=reach*local
   for b,v in enumerate(ch):walk(v['g'],v['h'],labels[:i]+labels[i+1:],reach/2,depth+1)
  walk(g,h,list(range(5)),Q(1),0)
  JL={};BL={};HL={};TL={};deltaL=Q(0);Iremain=Q(0)
  for w,z in leaves:
   for dst,key in [(JL,'J'),(BL,'B'),(HL,'H'),(TL,'T')]:c.add(dst,z[key],w)
   deltaL+=w*z['delta'];Iremain+=w*(c.physical(z['g'])['I']+c.physical(z['h'])['I'])/2
  eq(Jsum,sub(root['J'],JL));eq(add(dropH,HL),root['H']);eq(add(dropT,TL),root['T']);eq(deltaL,root['delta'])
  eq(data_spend+Iremain,(c.physical(g)['I']+c.physical(h)['I'])/2)
  eq(sub(add(sub(dropH,dropT),BL),root['B']),Jsum)
  nonneg(sub(c.const(1),Jsum))
  tree_rows.append({'policy':policy,'node_visits':visits,'leaves':len(leaves),'queried_data_influence':str(data_spend),'remaining_data_influence':str(Iremain),'cumulative_signed_debit_interval':list(map(str,c.interval(Jsum)))})
  assert time.perf_counter()-start<55
 (R/'out/HISTORIES.json').write_text(json.dumps(tree_rows,indent=2)+'\n',encoding='utf-8')
out={'status':'PASS','mode':'pilot' if pilot else 'main','ordered_branch_pairs':16 if pilot else 272,'physical_coordinate_rows':identity_rows,'actual_fixtures':fixtures,'symbolic_fixtures':symbolic,'assertions':checks,'elapsed_seconds':time.perf_counter()-start,'sign_arithmetic':'outward rational log intervals, no floating-point decisions'}
(R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k not in ['actual_fixtures','symbolic_fixtures']}))
