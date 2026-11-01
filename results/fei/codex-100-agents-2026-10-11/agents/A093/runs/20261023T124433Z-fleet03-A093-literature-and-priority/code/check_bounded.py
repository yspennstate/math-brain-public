from pathlib import Path
from fractions import Fraction as F
from itertools import product
import ast,json,time
R=Path(__file__).resolve().parents[1]
def save(n,x):(R/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
save('FAILED_MAIN.json',dict(status='FAILED_ENFORCED_WALL_CAP',helper='code/check.py',domain='all256 three-bit cores; all remaining size/sign states',first_failure='ck(spec(restrict(t,pos,b))==pp): AssertionError wall cap',max_runtime_seconds=55,elapsed_seconds='at least55; exact elapsed not persisted',coverage='no completed main PASS; partial traversal not counted',response='narrow domain, preserve prior outputs, do not raise runtime or dimension'))
save('FROZEN_BOUNDED.json',dict(helper='check_bounded.py v1',family='all256 labelled three-bit cores with six-bit parity-expanded root; BOTH five-bit children for EACH of six physical root queries; all8 sign translates of fully unwrapped three-bit core',domain='root ell=(2,2,2),theta0; endpoint ell=(1,1,1),theta0..7; root query positions0..5; nonuniform stopped/full sibling frontier per nonconstant core; fixed Maj3 control',case_count=dict(cores=256,states=2304,root_query_edges=1536),symmetry='none: no root coordinate omitted; family itself is explicitly narrowed',arithmetic='integer Walsh-Hadamard; Fraction physical-edge influences and exact spectral mass multisets',memory_estimate_MB=80,max_runtime_seconds=55,automatic_dimension_escalation=False))
names={'spec','influences','table','marginal','restrict'}
tree=ast.parse((R/'code/check.py').read_text(encoding='utf-8'));ns={'F':F}
exec(compile(ast.Module(body=[z for z in tree.body if isinstance(z,ast.FunctionDef) and z.name in names],type_ignores=[]),'<own-pure-definitions>','exec'),ns)
spec,influences,table,marginal,restrict=[ns[k] for k in ['spec','influences','table','marginal','restrict']]
t0=time.monotonic();count=states=edges=frontiers=0
def ck(x):
 global count
 count+=1;assert x,count
 assert time.monotonic()-t0<55,'wall cap'
for core in product([-1,1],repeat=8):
 P=spec(core);alpha=influences(core);J=sum(alpha);masses=sorted(x for x in P if x)
 root=table(core,[2,2,2],0);p=spec(root);inf=influences(root);states+=1
 ck(sorted(x for x in p if x)==masses);ck(sum(inf)==2*J)
 ck(sum(inf)==sum(i.bit_count()*v for i,v in enumerate(p)))
 for j in range(6):
  ck(inf[j]==alpha[j//2]);ck(all(not(p[s] and p[s^(1<<j)]) for s in range(64)))
  pp=marginal(p,j)
  for b in [0,1]:
   child=restrict(root,j,b);ck(spec(child)==pp);ck(sum(influences(child))==2*J-alpha[j//2])
  edges+=1
 for theta in range(8):
  endpoint=table(core,[1,1,1],theta);q=spec(endpoint);states+=1
  ck(sorted(x for x in q if x)==masses);ck(influences(endpoint)==alpha)
 if J:
  j=next(k for k,v in enumerate(alpha) if v)
  # Actual stopped plus sibling and fully unwrapped minus sibling.
  stopped=restrict(root,2*j,0);JS=sum(influences(stopped));ck(JS==2*J-alpha[j])
  endpoint=table(core,[1,1,1],1<<j);JE=sum(influences(endpoint));ck(JE==J)
  JF=(JS+JE)/2;tariff=alpha[j]+(J-alpha[j])/2
  for K in [F(1),F(2),F(4)]:ck(K*2*J-K*tariff==K*JF)
  frontiers+=1
maj=[1 if x.bit_count()<=1 else -1 for x in range(8)];p=spec(maj);J=sum(influences(maj))
ck(sorted(x for x in p if x)==[F(1,4)]*4);ck(J==F(3,2));ck(2*J-2==1);ck(J-2==F(-1,2))
out=dict(status='PASS',exact_assertions=count,core_count=256,physical_states=states,legal_query_edges=edges,nonuniform_frontiers=frontiers,seconds=time.monotonic()-t0,domain='bounded root+every physical root query+all full endpoint sign translates',majority_control=dict(H='2',I='3/2',original_entropy_residual='1',different_current_influence_residual='-1/2'),scope='Completed bounded three-bit domain only; failed larger domain not counted; universal quantifiers analytic')
save('VALIDATION.json',out);print(json.dumps(out))
