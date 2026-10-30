from pathlib import Path
from fractions import Fraction as Q
import exact as E
import itertools,json,time,sys
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv
def save(name,x):
 (R/'out'/name).write_text(json.dumps(x,indent=2),encoding='utf-8')
def budget():
 if time.perf_counter()-start>(55 if pilot else 180):raise RuntimeError('frozen runtime cap')
def patterns(n):return itertools.product((-1,0,1),repeat=n)
def restrict(tab,pat):
 for i in reversed(range(len(pat))):
  if pat[i]>=0:tab=E.slice_table(tab,i,pat[i])
 return tab
def H(tab):return E.entropy(E.walsh(tab))
def state(b,g,ids,opened,alive,phase=1):
 ne=len(ids);t=Q(1,len(b)) if alive else Q(0)
 f=tuple(v if alive and z==0 else b[z] for v in g for z in range(len(b)))
 if phase==-1:full=tuple(y for v in g for z in range(len(b)) for y in (v,v if alive and z==0 else b[z]))
 elif phase==0:full=tuple(v for v in g for z in range(len(b)))
 else:full=f
 a=E.walsh(full);ga=E.walsh(g);V=1-ga[0]**2
 density=(1+t)/2 if phase==-1 else Q(1) if phase==0 else t
 U=E.add(H(g),E.cost(ga[0]**2),-1);U=E.add({},U,density)
 RR=E.add({},E.cost(density),V)
 q=5*density*E.influence(ga)
 s=6*E.influence(a,0) if phase==-1 else Q(0) if phase==0 else None
 # Exposed variance reserve is symbolic because non-dyadic cases are permitted.
 S={2:s} if s is not None else E.add({},E.cost(t),V)
 ee=Q(0)
 for block in sorted(set(i//3 for i in ids)):
  places=[j for j,i in enumerate(ids) if i//3==block]
  if phase==0:continue
  if phase==-1 or block not in opened:
   ee+=4*sum(E.influence(a,j+(phase==-1)) for j in places)
  else:ee+=2*len(places)
 P=E.add(E.add(E.add(U,RR),S),{2:q+ee})
 return dict(H=E.entropy(a),P=P,a=a,U=U,R=RR,S=S,Q=q,E=ee,t=t,V=V)

gates=[];admitted=[]
for mask in range(16):
 tab=[1]*8
 for j,x in enumerate((3,5,6,7)):tab[x]=1-2*((mask>>j)&1)
 tab=tuple(tab);I=E.influence(E.walsh(tab));gates.append(dict(mask=mask,I=str(I)))
 if I>=Q(3,2):admitted.append((mask,tab))
save('gate_admission.json',dict(gates=gates,admitted=[x[0] for x in admitted]))
states=edges=olddebits=0
gs=[tuple(1-2*((mask>>x)&1) for x in range(4)) for mask in range(16)]
# All two-bit signs already contain every restriction type, so main uses no
# redundant internal partial assignments. This narrowed domain is frozen separately.
for mask,b in (admitted[:1] if pilot else admitted):
 for g in (gs[:2] if pilot else gs):
  for pat in patterns(3):
   bb=restrict(b,pat);ids=tuple(i for i,v in enumerate(pat) if v==-1)
   opened=set() if len(ids)==3 else {0};alive=all(v!=1 for v in pat)
   s=state(bb,g,ids,opened,alive);states+=1
   for j,original in enumerate(ids):
    ch=[state(E.slice_table(bb,j,v),g,ids[:j]+ids[j+1:],{0},alive and v==0) for v in (0,1)]
    dh=E.add(s['H'],E.add(ch[0]['H'],ch[1]['H']),-Q(1,2))
    drop=s['E']-(ch[0]['E']+ch[1]['E'])/2
    E.ok(drop>=2,'same original block allocation >=2')
    E.le(dh,{2:drop},'full exterior entropy payment')
    E.ok(E.add(ch[0]['U'],ch[1]['U'])==E.add({},s['U'],2),'U harmonic')
    dr=E.add(s['R'],E.add(ch[0]['R'],ch[1]['R']),-Q(1,2))
    ds=E.add(s['S'],E.add(ch[0]['S'],ch[1]['S']),-Q(1,2))
    E.ok(dr=={2:s['t']*s['V']} if s['t']*s['V'] else dr=={},'exact current fine release')
    E.ok(ds==dr,'same diminished variance release')
    E.le(dh,E.add(s['P'],E.add(ch[0]['P'],ch[1]['P']),-Q(1,2)),'full terminal P')
    edges+=1
   budget()
  E.walsh.cache_clear();E.cost_cached.cache_clear();E.bounds_cached.cache_clear()

# Independent direct character sums on 16 prescribed five-bit exposed functions.
direct=0
if not pilot:
 b=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
 for g in gs:
  f=tuple(v if z==0 else b[z] for v in g for z in range(8))
  aa=tuple(sum(v*(-1)**((x&s).bit_count()) for x,v in enumerate(f))*Q(1,len(f)) for s in range(len(f)))
  E.ok(aa==E.walsh(f),'direct character amplitude reproduction');direct+=1

# One fixed complete mixed tree on two majority blocks, source, and AND2 data.
# This order includes positive internal debit before X and between exterior queries.
tree_nodes=frontiers=0
if not pilot:
 M=tuple(1 if x.bit_count()<=1 else -1 for x in range(8))
 b=tuple(M[x&7]*M[x>>3] for x in range(64));g=(1,1,1,-1)
 order=[('g',0),('X',0),('z',0),('g',1),('z',1),('z',2),('z',3),('z',4),('z',5)]
 root=state(b,g,tuple(range(6)),set(),True,-1)
 agg=[dict(H={},P={},w=Q(0)) for _ in range(10)]
 def visit(b,g,ids,gids,opened,alive,phase,d,w):
  global tree_nodes,olddebits
  tree_nodes+=1;s=state(b,g,ids,opened,alive,phase)
  for k in ('H','P'):agg[d][k]=E.add(agg[d][k],s[k],w)
  agg[d]['w']+=w
  if d==len(order):return
  typ,orig=order[d];children=[]
  for v in (0,1):
   bb=b;gg=g;ii=ids;gi=gids;op=set(opened);al=alive;ph=phase
   if typ=='g':
    j=gids.index(orig);gg=E.slice_table(g,j,v);gi=gids[:j]+gids[j+1:]
   elif typ=='X':ph=v
   else:
    j=ids.index(orig);bb=E.slice_table(b,j,v);ii=ids[:j]+ids[j+1:];op.add(orig//3);al=alive and v==0
   cs=state(bb,gg,ii,op,al,ph);children.append((bb,gg,ii,gi,op,al,ph,cs))
  dh=E.add(s['H'],E.add(children[0][-1]['H'],children[1][-1]['H']),-Q(1,2))
  dp=E.add(s['P'],E.add(children[0][-1]['P'],children[1][-1]['P']),-Q(1,2))
  E.le(dh,dp,'mixed tree same owner local edge')
  if typ=='g' and dh and E.bounds(dh)[0]>0:olddebits+=1
  for bb,gg,ii,gi,op,al,ph,_ in children:visit(bb,gg,ii,gi,op,al,ph,d+1,w/2)
  budget()
 visit(b,g,tuple(range(6)),(0,1),set(),True,-1,0,Q(1))
 for z in agg:
  E.ok(z['w']==1,'both full actual terminals')
  E.le(E.add(root['H'],z['H'],-1),E.add(root['P'],z['P'],-1),'original full stopped potential')
  frontiers+=1
 E.ok(olddebits>0,'positive previous internal debits actually exercised')

result=dict(status='PASS',pilot=pilot,admitted_gates=len(admitted),states=states,exterior_edges=edges,direct_roots=direct,tree_nodes=tree_nodes,frontiers=frontiers,positive_internal_debits=olddebits,assertions=E.checks,seconds=time.perf_counter()-start)
save('pilot.json' if pilot else 'validation.json',result);print(json.dumps(result))
