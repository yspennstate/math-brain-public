import sys,time,json
from fractions import Fraction as F
from helper import c
start=time.perf_counter();pilot=sys.argv[1]=='pilot';nodes=0
def scaled(e,a):
 z={};c.add(z,e,a);return z
def half(a,b):
 z=scaled(a,F(1,2));c.add(z,b,F(1,2));return z
def sub(a,b):
 z=dict(a);c.add(z,b,-1);return z
def visit(f,h,policy,limit,depth=0):
 global nodes
 s=c.shadow(f);ph=c.physical(h);actual=c.physical(c.compose(f,h));q=(1+ph['mu'])/2;v=4*q*(1-q);nh=len(h).bit_length()-1
 V=scaled(s['h2'],v);W=v*s['Ip'];enc=[i for i in range(nh) if actual['d'][i]];dat=[j for j in range(len(f).bit_length()-2) if actual['d'][nh+j]]
 if not enc and not dat or limit is not None and depth==limit:return dict(Q={},G={},L={},V=V,GI={},LI=F(0),W=W)
 if policy=='max':
  ix=max(enc+[nh+j for j in dat],key=lambda i:(actual['d'][i],-i));typ='e' if ix<nh else 'd';ix=ix if typ=='e' else ix-nh
 else:
  prefer=policy=='encoder' or policy=='alternate' and depth%2==0;typ='e' if enc and (prefer or not dat) else 'd';ix=(enc if typ=='e' else dat)[0]
 children=[visit(f,c.split(h,ix,b),policy,limit,depth+1) if typ=='e' else visit(c.split(f,ix+1,b),h,policy,limit,depth+1) for b in [0,1]]
 z={k:half(children[0][k],children[1][k]) if isinstance(children[0][k],dict) else (children[0][k]+children[1][k])/2 for k in children[0]}
 if typ=='e':
  gamma=F(ph['W'][1<<ix],len(h));charge=scaled(s['B'],gamma*gamma);gap=scaled(sub(s['h2'],s['B']),gamma*gamma);c.positive(gap)
  c.add(z['Q'],charge);c.add(z['G'],gap);c.add(z['GI'],sub(c.const(gamma*gamma*s['Ip']),charge))
 else:
  childH=half(c.shadow(c.split(f,ix+1,0))['h2'],c.shadow(c.split(f,ix+1,1))['h2'])
  loss=scaled(sub(s['h2'],childH),v);c.positive(loss);LI=v*(s['ap'][ix]+s['am'][ix]);c.positive(sub(c.const(LI),loss))
  c.add(z['L'],loss);z['LI']+=LI
 account=dict(z['Q']);c.add(account,z['G']);c.add(account,z['L']);c.add(account,z['V']);c.add(account,V,-1);assert not account
 nested=sub(z['GI'],z['G']);c.add(nested,c.const(z['LI']));c.add(nested,z['L'],-1);c.add(nested,c.const(z['W']));c.add(nested,z['V'],-1);c.add(nested,c.const(-W));c.add(nested,V);assert not nested
 c.positive(sub(z['GI'],z['G']));c.positive(sub(c.const(z['LI']),z['L']));nodes+=1
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
count=0
for f,h in roots:
 if pilot and not c.physical(c.compose(f,h))['I']:continue
 for policy in ['encoder','data','alternate','max']:
  for limit in [None,2]:
   visit(f,h,policy,limit);count+=1
   if pilot and count==16:break
  if pilot and count==16:break
 if pilot and count==16:break
 if time.perf_counter()-start>(60 if pilot else 120):raise RuntimeError('frozen watchdog')
result=dict(status='PASS',trees=count,node_visits=nodes,elapsed_seconds=time.perf_counter()-start,accounts=['information reserve','nested boundary-minus-information reserve','nonnegative data and encoder slack differences'])
c.dump('pilot_trees.json' if pilot else 'main_trees.json',result);print(json.dumps(result))
