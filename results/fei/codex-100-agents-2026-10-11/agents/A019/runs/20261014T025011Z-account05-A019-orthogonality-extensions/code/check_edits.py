import json,time,sys,itertools
from fractions import Fraction as Q
from pathlib import Path
R=Path(__file__).resolve().parents[1]
pilot='--pilot' in sys.argv
spec={'helper_version':'A019-internal-edge-v1','family':'all Boolean core/edit-set pairs on uniform cubes; two shared-bit products with origin edits and arbitrary cores','domain':'pilot n=1,2 core/edit pairs; full n=1,2,3 core/edit pairs plus 256 ordered two-bit core pairs at AND/OR masks and 256 ordered shared-mask pairs at cores AND and XOR','case_count':272 if pilot else 66320,'symmetry':'none','arithmetic':'integer truth tables, integer Walsh, exact Fraction energy and allocation','memory_estimate_MB':40,'maximum_runtime_seconds':60}
(R/'out'/('PILOT_SPEC.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2))
start=time.monotonic();checks=cases=independent=0
def ck(x):
 global checks
 checks+=1
 assert x
def fw(a):
 a=list(a);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def edge(a):
 n=(len(a)).bit_length()-1
 return sum((a[x]-a[x^(1<<i)])**2 for x in range(len(a)) for i in range(n))
def energy(a):
 c=fw(a);return Q(sum(i.bit_count()*v*v for i,v in enumerate(c)),len(a)**2)
for n in ([1,2] if pilot else [1,2,3]):
 N=1<<n;gs=[[1-2*((k>>x)&1) for x in range(N)] for k in range(1<<N)]
 for k,g in enumerate(gs):
  for e in range(1<<N):
   cases+=1
   if time.monotonic()-start>60:raise TimeoutError('frozen deadline')
   b=gs[k^e];D=[g[x]*((e>>x)&1) for x in range(N)]
   si=so=0;adj=False
   for x in range(N):
    for i in range(n):
     y=x^(1<<i);ex=(e>>x)&1;ey=(e>>y)&1
     if ex and ey:si+=(g[x]-g[y])**2;adj=True
     if not ex and not ey:so+=(g[x]-g[y])**2
   J=Q(edge(g)+edge(b),8*N);kap=Q(edge(D),4*N);inside=Q(si,4*N);outside=Q(so,4*N)
   ck(2*kap-J==inside-outside)
   ck(kap==energy(D));ck(J==(energy(g)+energy(b))/2)
   ck((kap<=J/2)==(inside<=outside))
   if not adj:
    independent+=1;ck(kap<=J/2)
   if e.bit_count()==1:ck(kap==Q(n,2*N));ck(J>=Q(n,N))
def product_test(cores,masks):
 global cases
 cases+=1
 N=4;a=2;M=16
 def child(b):return [cores[0][x]*(-1 if ((masks[0]>>b)&1) and x==0 else 1)*cores[1][y]*(-1 if ((masks[1]>>b)&1) and y==0 else 1) for y in range(N) for x in range(N)]
 leaves=[child(b) for b in range(4)]
 full=[leaves[b][v] for v in range(M) for b in range(4)]
 c=fw(full);den=len(full)**2
 J=sum(energy(l) for l in leaves)/4
 d=Q(sum((s&3).bit_count()*v*v for s,v in enumerate(c)),den)
 mixed=Q(sum(v*v for s,v in enumerate(c) if s&3==3),den)
 Tpriv=Q(2*sum((s>>2).bit_count()*(s&3).bit_count()*v*v for s,v in enumerate(c)),den)
 owned=Q(0)
 for direction in (0,1):
  other=1-direction
  for v in (0,1):
   b0=v<<other;b1=b0|(1<<direction)
   js=[];ks=[];qs=[]
   for j in range(2):
    ends=[[cores[j][x]*(-1 if ((masks[j]>>b)&1) and x==0 else 1) for x in range(N)] for b in (b0,b1)]
    jj=(energy(ends[0])+energy(ends[1]))/2
    kk=energy([Q(x-y,2) for x,y in zip(*ends)])
    q=Q(sum(x*y for x,y in zip(*ends)),N)
    ck(q>=0);ck(kk<=jj/2);js.append(jj);ks.append(kk);qs.append(q)
   for j in range(2):owned+=((1-qs[1-j])*js[j]/2+qs[1-j]*ks[j])/2
 ck(Tpriv==2*owned);ck(Tpriv<=2*J);ck(2*mixed<=d)
 rootD=[Q(leaves[b][v]-leaves[b|1][v],2) for v in range(M) for b in (0,2)]
 T=2*energy(rootD)+energy([Q(x-y,2) for x,y in zip(leaves[0],leaves[2])])+energy([Q(x-y,2) for x,y in zip(leaves[1],leaves[3])])
 ck(T==Tpriv+2*mixed);ck(T<=2*J+d)
if not pilot:
 gs=[[1-2*((k>>x)&1) for x in range(4)] for k in range(16)]
 for g,h in itertools.product(gs,repeat=2):product_test([g,h],[8,14])
 for masks in itertools.product(range(16),repeat=2):product_test([gs[8],gs[6]],masks)
# Arbitrary edit regions fail half-private even after disagreement folding.
g=[1,1,-1,1];E=[1,0,1,0];b=[x*(1-2*e) for x,e in zip(g,E)]
J=(energy(g)+energy(b))/2;kap=energy([x*e for x,e in zip(g,E)])
ck(J==1);ck(kap==Q(3,4));ck(sum(E)==2)
out={'status':'PASS','cases':cases,'checks':checks,'independent_set_pairs':independent,'seconds':time.monotonic()-start,'counterexample':{'core':g,'edit_set':E,'J':str(J),'kappa':str(kap),'q':'0'},'full_fei':'OPEN'}
(R/'out'/('PILOT_CHECK.json' if pilot else 'EDIT_CHECK.json')).write_text(json.dumps(out,indent=2));print(json.dumps(out))
