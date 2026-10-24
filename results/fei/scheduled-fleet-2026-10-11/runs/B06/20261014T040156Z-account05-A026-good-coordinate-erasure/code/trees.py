import sys,time,json
from fractions import Fraction as F
import core as c
start=time.perf_counter();pilot=sys.argv[1]=='pilot'
def avg(a,b):
 if isinstance(a,dict):
  z={};c.add(z,a,F(1,2));c.add(z,b,F(1,2));return z
 return (a+b)/2
def visit(f,h,policy,limit,depth=0):
 s=c.shadow(f);ph=c.physical(h);actual=c.physical(c.compose(f,h));q=(1+ph['mu'])/2;v=4*q*(1-q)
 W=v*s['Ip'];X=q*sum(s['ap'])+(1-q)*sum(s['am']);nh=len(h).bit_length()-1
 enc=[i for i in range(nh) if actual['d'][i]]
 dat=[j for j in range(len(f).bit_length()-2) if actual['d'][nh+j]]
 if not enc and not dat or limit is not None and depth==limit:
  return dict(Q={},G={},L=F(0),W=W,X=X,ex=F(0),Se=F(0),Sd=F(0),Ei={},Ed={},H=actual['H'],I=actual['I'],nodes=0)
 if policy=='max':
  ix=max(enc+[nh+j for j in dat],key=lambda i:(actual['d'][i],-i));typ='e' if ix<nh else 'd';ix=ix if typ=='e' else ix-nh
 else:
  prefer=policy=='encoder' or policy=='alternate' and depth%2==0
  typ='e' if enc and (prefer or not dat) else 'd';ix=(enc if typ=='e' else dat)[0]
 children=[visit(f,c.split(h,ix,b),policy,limit,depth+1) if typ=='e' else visit(c.split(f,ix+1,b),h,policy,limit,depth+1) for b in [0,1]]
 z={k:avg(children[0][k],children[1][k]) for k in children[0]};z['nodes']=1+children[0]['nodes']+children[1]['nodes']
 if typ=='e':
  gamma=F(ph['W'][1<<ix],len(h));charge={};c.add(charge,s['B'],gamma*gamma)
  gap=c.const(gamma*gamma*s['Ip']);c.add(gap,charge,-1);c.positive(gap)
  assert actual['d'][ix]==s['delta']*ph['d'][ix]
  c.add(z['Q'],charge);c.add(z['G'],gap);c.add(z['Ei'],ph['B'][ix],s['delta']);z['Se']+=actual['d'][ix]
 else:
  loss=v*(s['ap'][ix]+s['am'][ix]);e=q*s['ap'][ix]+(1-q)*s['am'][ix]
  assert e<=actual['d'][nh+ix]
  z['L']+=loss;z['ex']+=e;z['Sd']+=actual['d'][nh+ix];c.add(z['Ed'],actual['B'][nh+ix])
 total=dict(z['Q']);c.add(total,z['G']);c.add(total,c.const(z['L']+z['W']-W));assert not total
 assert z['ex']+z['X']==X and z['Se']+z['Sd']+z['I']==actual['I']
 margin=dict(z['H']);c.add(margin,z['Ei']);c.add(margin,z['Ed']);c.add(margin,z['Q']);c.add(margin,c.const(F(9,2)*z['Se']+3*z['Sd']));c.add(margin,actual['H'],-1);c.positive(margin)
 return z
roots=[]
for n in [1,2]:
 for _,f in c.tables(n):
  for m in [0,1,2]:
   for _,h in c.tables(m):roots.append((f,h))
special=[tuple(1 if x.bit_count()>=2 else -1 for x in range(8)),tuple(1 if x==7 else -1 for x in range(8)),tuple(-1 if x==0 else 1 for x in range(8))]
for _,f in c.tables(3):
 for h in special:roots.append((f,h))
assert len(roots)==1208
count=nodes=0
for f,h in roots:
 if pilot and not c.physical(c.compose(f,h))['I']:continue
 for policy in ['encoder','data','alternate','max']:
  for limit in [None,2]:
   z=visit(f,h,policy,limit);count+=1;nodes+=z['nodes']
   if pilot and count==16:break
  if pilot and count==16:break
 if pilot and count==16:break
 if time.perf_counter()-start>(60 if pilot else 120):raise RuntimeError('frozen watchdog')
result={'status':'PASS','trees':count,'node_visits':nodes,'elapsed_seconds':time.perf_counter()-start,'controls_not_executed':'Five bent unlock controls remain analytic PROOF section5; not included in executed tree count.'}
c.dump('pilot_trees.json' if pilot else 'main_trees.json',result);print(json.dumps(result))
