from pathlib import Path
from fractions import Fraction as Q
import itertools,json,time
import exact as E
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v,msg):
 global checks
 checks+=1
 if not v:raise AssertionError(msg)
def direct(g):return tuple(Q(sum(v*(-1)**((s&x).bit_count()) for x,v in enumerate(g)),len(g)) for s in range(len(g)))
def restricted(g,states):return tuple(v for x,v in enumerate(g) if all(a==2 or ((x>>i)&1)==a for i,a in enumerate(states)))
root=tuple(((-1)**(((x&3)==3))) if (x&3)!=3 else (-1)**(int(((x>>2)&3)==3)+int(((x>>4)&3)==3)+((x>>6)&1)) for x in range(128))
ck(direct(root)==E.walsh(root),'independent root characters')
states=edges=dead=tagcollapsed=biased=0
for ss in itertools.product(range(3),repeat=7):
 states+=1;tab=restricted(root,ss);coeff=E.walsh(tab)
 alive=all(a!=0 for a in ss[:2]);ne=ss[:2].count(2);t=Q(1,1<<ne) if alive else Q(0)
 untouched=sum(ss[j]==ss[j+1]==2 for j in (2,4));X=t*untouched
 dead+=int(not alive);tagcollapsed+=int(ss[6]!=2)
 core=tuple((-1)**(int((x&3)==3)+int(((x>>2)&3)==3)+((x>>4)&1)) for x in range(32));cg=restricted(core,ss[2:]);cc=E.walsh(cg);biased+=int(sum(cg)!=0)
 ck(E.entropy(cc)=={2:Q(2*untouched)} if untouched else E.entropy(cc)=={},'actual biased core full entropy')
 marginal=[sum(coeff[(s<<ne)+u]**2 for u in range(1<<ne)) for s in range(len(cc))]
 ck(all(marginal[s]==t*cc[s]**2+((1-t) if s==0 else 0) for s in range(len(cc))),'exact full core-frequency marginal')
 E.le({2:2*X} if X else {},E.entropy(coeff),'FULL entropy lower bound under coherent interference');checks+=1
 for i,a in enumerate(ss):
  if a!=2:continue
  edges+=1;ch=[]
  for value in (0,1):
   st=list(ss);st[i]=value;al=all(z!=0 for z in st[:2]);tt=Q(1,1<<st[:2].count(2)) if al else Q(0);uu=sum(st[j]==st[j+1]==2 for j in (2,4));ch.append(tt*uu)
  first=(2<=i<6 and ss[2+2*((i-2)//2)]==ss[3+2*((i-2)//2)]==2)
  ck(X-sum(ch)/2==(t if first else 0),'all edge first-touch/density drift')
 if time.perf_counter()-start>55:raise RuntimeError('frozen cap')
# Separate direct 9-bit seed lane verifies the actual rate6 excess witness.
m=8;c=Q(1,256);b=tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(4)) for x in range(256));plus=b;minus=tuple(v-2*int(x==255) for x,v in enumerate(b));seed=plus+minus
sd=direct(seed);ck(sd==E.walsh(seed),'direct9bit seed reproduction')
dd=E.add(E.entropy(sd),E.add(E.entropy(direct(plus)),E.entropy(direct(minus))),-Q(1,2));ex=E.add(dd,{2:-6*c});E.le({2:c},ex,'positive original rate6 local excess');checks+=1
ck(E.influence(sd,m)==c,'independent rare influence')
out={'status':'PASS','assertions':checks,'states':states,'edges':edges,'dead_mask_states':dead,'collapsed_tag_states':tagcollapsed,'biased_core_states':biased,'seed_excess_nats':[str(z) for z in E.bounds(ex)],'seconds':time.perf_counter()-start}
(R/'out/audit.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='seed_excess_nats'}))
