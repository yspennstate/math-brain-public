from pathlib import Path
from fractions import Fraction as F
import json,time,sys
import mathcore as m
ROOT=Path(__file__).resolve().parents[1]
pilot='--pilot' in sys.argv;m.limit=55 if pilot else 175
cases=paid=overlapping=connected=giant_cases=0

def sumv(vs):
 d={}
 for v in vs:d=m.add((d,1),(v,1))
 return d

def check(g,A,name=None):
 global cases,paid,overlapping,connected,giant_cases
 cases+=1;n=len(g).bit_length()-1;r=A.bit_count();p=m.mass(g)
 comps=m.components(g);E=m.energy(g,A);I=4*E
 m.ck(E==m.edges(g,A));m.ck(E==sum((m.edges(c,A) for c in comps),F(0)))
 m.ck(m.energy(tuple(1-2*v for v in g),A)==I)
 # Independently construct retained-Y queried fibers, not physical X children.
 groups={y:[] for y in range(len(g)) if y&A==0}
 for x in range(len(g)):groups[x&~A].append(x)
 Q={};W={};Omega={}
 for ys in groups.values():
  my=F(sum(g[x] for x in ys),len(ys));mks=[F(sum(c[x] for x in ys),len(ys)) for c in comps]
  m.ck(sum(mks,F(0))==my)
  Q=m.add((Q,1),(m.entropy([my]),F(1,len(groups))))
  W=m.add((W,1),(m.entropy(mks),F(1,len(groups))))
  if my:Omega=m.add((Omega,1),(m.entropy([mk/my for mk in mks]),my/len(groups)))
 m.ck(W==m.add((Q,1),(Omega,1)));m.nonneg(Omega)
 m.nonneg(m.add(({2:2*E},1),(W,-1)))
 projcost=sumv([m.add((m.logv(F(len(m.projection(c,A)),1<<r)),-m.mass(c))) for c in comps])
 m.nonneg(m.add((W,1),(projcost,-1)))
 full_cond=sumv([m.add((m.logv(F(sum(c))),m.mass(c)/p)) for c in comps]) if p else {}
 within=m.add(({2:r},1),(W,-1/p)) if p else {}
 if p:m.nonneg(m.add((full_cond,1),(within,-1)))
 sets=[m.projection(c,A) for c in comps]
 overlap=any(sets[i]&sets[j] for i in range(len(sets)) for j in range(i))
 overlapping+=overlap;connected+=len(comps)==1
 # Original labels survive in every actual queried-X child.
 gc=m.children(g,A);cc=[m.children(c,A) for c in comps]
 Z={}
 for ix,h in enumerate(gc):
  delta=m.add((m.raw(h),1),(sumv([m.raw(cs[ix]) for cs in cc]),-1))
  Z=m.add((Z,1),(delta,F(1,len(gc))))
 D=m.add((m.raw(g),1),(sumv([m.raw(c) for c in comps]),-1))
 Lg,B,J=m.ledger(g,A)
 sumL=sumv([m.ledger(c,A)[0] for c in comps]);cross=m.add((Lg,1),(sumL,-1))
 m.ck(D==m.add((cross,1),(Z,1)))
 if not overlap:m.ck(not Z)
 # In natural units, kappa*E*ln2=2E. No floating comparison.
 bound=m.add(({2:r*p},1),(sumL,-1),(cross,-1))
 m.ck(m.interval(bound)[0]+2*E>=0)
 f=tuple(1-2*v for v in g);Lf=m.ledger(f,A)[0]
 # Verify raw upper plus the analytic rational relaxation a<21/4.
 m.nonneg(m.add(({2:4*r*p+F(21,4)*I},1),(Lf,-1)))
 ispaid=m.ge(m.add((W,1),({2:F(r,2)*p},-1))) if p else False
 if ispaid:
  paid+=1;m.ck(I>=r*p)
  m.nonneg(m.add(({2:F(37,4)*I},1),(Lf,-1)))
 if p and all(sum(c)**2<=1<<(n-1) for c in comps):
  giant_cases+=1
  if r==n-1:m.ck(ispaid)
 return dict(name=name,dimension=n,block=A,p=p,component_sizes=[sum(c) for c in comps],
   projection_sizes=[len(s) for s in sets],projection_overlap=overlap,paid=ispaid,
   Q=m.vec(Q),Omega=m.vec(Omega),W=m.vec(W),projection_information=m.vec(projcost),
   signed_terminal_cross=m.vec(Z),root_component_excess=m.vec(D),sign_drop=m.vec(Lf),I_A=I)

tables=0
for n in range(3 if pilot else 4):
 for mask in range(1<<(1<<n)):
  g=tuple(mask>>x&1 for x in range(1<<n));tables+=1
  for A in range(1,(1<<n)-1):check(g,A)
fixtures=[]
def fixture(n,U,A,name):
 fixtures.append(check(tuple(int(x in U) for x in range(1<<n)),A,name))
fixture(8,{x+(y<<4) for x in [0,1,2] for y in range(16) if y.bit_count()<=1 or y==15},15,'identical_component_projections_with_retained_star')
fixture(4,{0,1,5,7,14,15},3,'connected_full_projection_sparse_fibers')
fixture(5,{0,4,12,13,15,3,19,27,26,24},3,'overlap_label_credit_is_decisive')
if not pilot:
 fixture(7,{x for x in range(128) if (x&15).bit_count()<=1 or x==15},15,'Brain45_original_separator')
 fixture(9,{x for x in range(512) if (x&31).bit_count()<=1 or x==31},31,'Brain44_original_separator')
 fixture(4,{x+(y<<2) for x in range(4) for y in [0,3]},3,'full_overlapping_projections_zero_queried_influence')
m.ck(fixtures[0]['projection_overlap'] and fixtures[0]['paid'])
m.ck(fixtures[1]['paid'] and not fixtures[1]['projection_information'])
m.ck(fixtures[1]['component_sizes']==[6])
m.ck(fixtures[2]['projection_overlap'] and fixtures[2]['paid'])
m.ck(m.ge({int(k):F(v) for k,v in fixtures[2]['Omega'].items()}))
q={int(k):F(v) for k,v in fixtures[2]['Q'].items()}
m.ck(not m.ge(m.add((q,1),({2:F(fixtures[2]['p'])},-1))))
# Do not assert positivity of the terminal cross term; retain its exact sign.
m.save('PILOT_FIXTURES.json' if pilot else 'FIXTURES.json',fixtures)
result=dict(status='PASS',pilot=pilot,tables=tables,block_cases=cases,paid_cases=paid,
  overlapping_cases=overlapping,connected_cases=connected,small_component_cases=giant_cases,
  fixtures=len(fixtures),assertions=m.checks,seconds=time.perf_counter()-m.start,
  peak_memory='unmeasured',full_fei='OPEN')
m.save('PILOT.json' if pilot else 'EXACT_CHECK.json',result)
print(json.dumps(result,indent=2))
