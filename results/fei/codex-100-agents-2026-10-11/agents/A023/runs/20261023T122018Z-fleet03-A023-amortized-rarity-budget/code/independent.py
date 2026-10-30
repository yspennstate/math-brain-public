"""Reconstruct every spectrum by characters and every influence by physical edges.
Independent representation, same author; no independent-person review claimed.
"""
import sys,time,json,importlib.util
from pathlib import Path
from fractions import Fraction as Q
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
hp=ROOT/'runs/20261014T022245Z-fleet05-A023-amortized-rarity-budget/code/check_block.py'
sp=importlib.util.spec_from_file_location('prime_logs',hp);h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
START=time.perf_counter();CHECKS=0
def ck(v):
 global CHECKS
 assert v
 CHECKS+=1
 assert time.perf_counter()-START<180
def load(n):return json.loads((RUN/'out'/n).read_text(encoding='utf-8'))
def vector(o):return {int(k):Q(v) for k,v in o.items() if Q(v)}
def direct(t):
 N=len(t);p={}
 for s in range(N):
  a=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t))
  if a:p[s]=Q(a*a,N*N)
 ck(sum(p.values())==1);return p
def entropy(P):
 z={}
 for p in P.values():h.lg(z,p,-p)
 return h.add((1,z))
def cross(P,q):
 z={}
 for s,p in P.items():h.lg(z,q[s],-p)
 return h.add((1,z))
rows=load('rows.json');front=load('frontiers.json');profiles=[]
for row in rows:
 m=row['m'];fix={int(i):v for i,v in row['fix'].items()};active=[i for i in range(m) if i not in fix];A=fix[m+1];B=fix[m+2];marked=A==1 and B==0
 seed=[];actual=[];rare=0
 for x in range(1<<len(active)):
  y=sum(v<<i for i,v in fix.items() if i<m)+sum(((x>>j)&1)<<i for j,i in enumerate(active))
  phase=(y.bit_count()+sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,m,2)))%2
  b=1-2*phase;edited=A==1 and y==(B if B else 0);seed.append(b);actual.append(b*(-1 if edited else 1));rare+=int(edited)
 N=len(actual);P=direct(actual);Ps=direct(seed);ck(len(Ps)==1) # complete pair prefix only
 qo={i:(Ps.get(i,Q(0))+Q(1,N))/2 for i in range(N)}
 qn={i:(P.get(i,Q(0))+Q(1,N))/2 for i in range(N)} if marked else qo
 H=entropy(P);Co=cross(P,qo);Cn=cross(P,qn);Ko=h.add((1,Co),(-1,H));Kn=h.add((1,Cn),(-1,H));D=h.add((1,Cn),(-1,Co))
 ii={i:Q(sum(v!=actual[x^(1<<j)] for x,v in enumerate(actual)),N) for j,i in enumerate(active)}
 ID=sum(ii.values(),Q(0));IS=sum((Q(sum(v!=seed[x^(1<<j)] for x,v in enumerate(seed)),N) for j in range(len(active))),Q(0));Z=4*IS;M=Q(rare,N)
 Bo=h.add((1,h.rational(4*ID-Q(m,8))),(-1,Co));Bn=h.add((1,h.rational(4*ID-Q(m,8))),(-1,Cn))
 for name,val in [('H',H),('Cold',Co),('Kold',Ko),('Bold',Bo),('Cnew',Cn),('Knew',Kn),('D',D),('Bnew',Bn)]:ck(vector(row[name])==val)
 ck(Q(row['ID'])==ID and Q(row['M'])==M and Q(row['Z'])==Z and Q(row['R'])==0);ck(row['marked']==marked)
 ck(h.sign(Ko)>=0 and h.sign(Kn)>=0)
 if marked:ck(h.sign(h.add((1,h.rational(1)),(-1,Kn)))>=0 and h.sign(h.add((1,h.rational(1)),(-1,D)))>=0)
 else:ck(not D)
 # z=1 multiplies the WHOLE truth table by -1, with identical spectrum.
 ck(direct([-v for v in actual])==P)
 profiles.append({'B':Bn,'D':D,'C':Cn,'Kold':Ko,'Knew':Kn,'Z':Z,'M':M,'ID':ID,'ii':ii,'active':active,'fix':fix,'m':m})
for node in front['queries']:
 z=profiles[node['parent']];a,b=[profiles[i] for i in node['children']];j=node['coordinate']
 ck(z['Z']-(a['Z']+b['Z'])/2==4 and z['M']==(a['M']+b['M'])/2)
 ck(z['ID']-(a['ID']+b['ID'])/2==z['ii'][j])
 dc=h.add((1,z['C']),(-Q(1,2),a['C']),(-Q(1,2),b['C']))
 ck(h.add((1,z['B']),(-Q(1,2),a['B']),(-Q(1,2),b['B']))==h.add((1,h.rational(4*z['ii'][j])),(-1,dc)))
 inc=h.add((Q(1,2),a['D']),(Q(1,2),b['D']),(-1,z['D']));ck(inc==vector(node['signed_conversion_increment']))
results=[]
for m in [6,8]:
 mass=depth=consumed=EZ=EM=negative=extra=Q(0);EB={};ED={};count=0
 for leaf in front['terminal']:
  z=profiles[leaf['row']]
  if z['m']!=m:continue
  f=z['fix'];nfixed=sum(i<m for i in f);q=Q(1,1<<(nfixed+2));ck(q==Q(leaf['reach']));A=f[m+1];B=f[m+2]
  # Every even endpoint was queried; odd live iff original first endpoint was0.
  initial_live=[i+1 for i in range(0,m,2) if f[i]==0]
  used=sum(i in f for i in initial_live);ck(used==leaf['consumed_live'])
  is_extra=A==1 and B==0 and used>0;ck(used==1 if is_extra else True)
  ck(bool(leaf['negative'])==(A==B==0));ck(leaf['extra']==int(is_extra))
  mass+=q;depth+=q*nfixed;consumed+=q*used;EZ+=q*z['Z'];EM+=q*z['M'];extra+=q*int(is_extra);EB=h.add((1,EB),(q,z['B']));ED=h.add((1,ED),(q,z['D']));count+=1
  if A==B==0:ck(z['B']==h.rational(-Q(m,8)));negative+=q
 ck(mass==1 and negative==Q(1,4));ck(count==(164 if m==6 else 564));ck(extra==Q(1,4)*(1-Q(1,1<<(m//2))))
 ck(consumed==Q(m,16)+extra and depth==Q(13*m,16)+extra);ck(EZ==m-4*consumed and EM==Q(1,1<<(m+1)))
 ck(h.sign(h.add((1,EB),(-1,h.rational(Q(153,256)))))>0);ck(h.sign(h.add((1,h.rational(Q(1,4))),(-1,ED)))>=0)
 results.append({'m':m,'terminal_states':count,'expected_core_depth':str(depth),'consumed_live':str(consumed),'negative_mass':str(negative),'original_M':str(EM)})
g=front['guards'];z=profiles[g['parent']];a=profiles[g['surviving_child']];b=profiles[g['unedited_child']]
ck(not z['Kold'] and h.sign(z['D'])>0);ck(h.sign(a['D'])<0 and not b['D']);ck(len(z['active'])==3 and len(a['active'])==2)
out={'status':'PASS','profiles':len(rows),'terminal_states':sum(z['terminal_states'] for z in results),'query_nodes':len(front['queries']),'checks':CHECKS,'elapsed_seconds':time.perf_counter()-START,'results':results,'independence':'direct characters/physical edges, no production tables or influence routines; same author, independent-person review pending'}
(RUN/'out/independent_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
