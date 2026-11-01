import ast,json,itertools,sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from time import perf_counter
run=Path(__file__).resolve().parents[1];start=perf_counter();checks=0
pilot='--pilot' in sys.argv
# Reuse only declared arithmetic functions, never execute another validation job.
tree=ast.parse((run/'code/check_delete.py').read_text())
names={'ck','fw','edges','phase','primitive','log2','entropy','reference'}
nodes=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names]
exec(compile(ast.Module(body=nodes,type_ignores=[]),'local_arithmetic_helpers','exec'))
l2,u2=primitive(2);ph=[phase(i) for i in range(16)]
tuples=[(f,f^8,f^6) for f in range(16)]+[(0,0,0)]
cases=0;minIU=None;maxGammaOverI=F(0);exposure=[];transcript=[]
gcases=[('MAJ3',[1 if u.bit_count()<2 else -1 for u in range(8)]),('AND3',[1 if u==0 else -1 for u in range(8)])]
witnesses=[]
for name,g in gcases:
 a=fw(g);Q,gl,gu=reference(a)
 Ig=F(sum(s.bit_count()*b*b for s,b in enumerate(a)),64);ck(gu<=8*Ig)
 achoices=range(2) if pilot else range(16)
 bchoices=range(8,10) if pilot else range(8,16)
 ws=tuples[:2] if pilot else tuples
 for af,bf,weak in itertools.product(achoices,bchoices,ws):
  truth=[]
  branch=[]
  for z in range(4):
   leaf=[]
   for d in range(16):
    x=(-1)**(d&1)*ph[af][z]
    y=sum((((d>>(i+1))&1)^(ph[weak[i]][z]==-1))<<i for i in range(3))
    v=g[y]
    leaf.append(1 if x+x*ph[bf][z]+v>0 else -1)
   branch.append(leaf);truth+=leaf
  b=fw(truth);ed=edges(truth)
  IU=F(sum(ed[4:]),32);IX=F(sum(ed[:4]),32)
  ck(IU>=F(1,2))
  pi=F(sum(ph[bf][z]==1 for z in range(4)),4)
  ck(pi in (F(1,4),F(3,4)))
  ck(IX==pi+(1-pi)*Ig)
  # Root data spectrum marginal and whole normalized reference.
  qbar=[F(0)]*16
  for z in range(4):
   qleaf=[F(0)]*16
   if ph[bf][z]==1:qleaf[1]=F(1)
   else:
    for s,p in enumerate(Q):qleaf[s<<1]=p
   ck(sum(qleaf)==1)
   for s in range(16):qbar[s]+=qleaf[s]/4
   raw=fw(branch[z])
   for s in range(16):
    if raw[s]:ck(qleaf[s]>0)
  ck(sum(qbar)==1)
  gamlo=gamhi=F(0)
  for s in range(16):
   mass=F(sum(b[s|(t<<4)]**2 for t in range(4)),4096)
   expected=pi*(s==1)
   if not s&1:expected+=(1-pi)*F(a[s>>1]**2,64)
   ck(mass==expected)
   if mass:
    ck(qbar[s]>0)
    lo,hi=log2(4/qbar[s]);gamlo+=mass*lo;gamhi+=mass*hi
  lp,up=log2(1/pi);lm,um=log2(1/(1-pi))
  hpl=pi*lp+(1-pi)*lm;hpu=pi*up+(1-pi)*um
  # Exact formula Gamma=2+h2(pi)+(1-pi)*Gamma_g verified by interval overlap.
  ck(gamlo<=2+hpu+(1-pi)*gu)
  ck(gamhi>=2+hpl+(1-pi)*gl)
  ck(gamhi<=4+(1-pi)*gu)
  ck(gamhi<=8*(IX+IU))
  ck(sum(v*v for v in b)==4096)
  # Every relative-phase crossing edge contributes exactly half disagreement.
  for j in (0,1):
   crossing=0
   for z in range(4):
    if z>>j&1 or ph[bf][z]==ph[bf][z^(1<<j)]:continue
    count=sum(branch[z][d]!=branch[z^(1<<j)][d] for d in range(16))
    ck(count==8);crossing+=count
   ck(F(ed[4+j],32)>=F(crossing,32))
  minIU=IU if minIU is None else min(minIU,IU)
  maxGammaOverI=max(maxGammaOverI,gamhi/(IX+IU))
  if af==0 and bf==8 and weak==(0,0,0):
   for signbit in (0,1):
    exposed=[truth[(z<<4)|(y<<1)|signbit] for z in range(4) for y in range(8)]
    ee=edges(exposed)
    exposure.append(dict(core=name,x_value=(-1)**signbit,I_U=str(F(sum(ee[3:]),16)),I_total=str(F(sum(ee),16))))
   witnesses.append(dict(core=name,common_phase=af,relative_phase=bf,weak_phases=weak,I_U=str(IU),I_data=str(IX),Gamma_interval=[str(gamlo),str(gamhi)],truth_table=truth,raw_spectrum=b,complete_data_mixture_masses=list(map(str,qbar))))
  transcript.append([name,af,bf,weak,str(IU),str(IX)])
  cases+=1
out=dict(status='PASS',pilot=pilot,helper_version=2,cases=cases,exact_assertions=checks,runtime_seconds=perf_counter()-start,minimum_I_U=str(minIU),maximum_complete_cost_over_I_upper=str(maxGammaOverI),core_exposure_fixtures=exposure,witnesses=witnesses)
p=run/'out'/('rank2_pilot.json' if pilot else 'rank2_validation.json')
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}))
