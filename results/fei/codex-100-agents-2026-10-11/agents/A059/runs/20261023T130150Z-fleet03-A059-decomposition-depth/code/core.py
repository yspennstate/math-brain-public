from pathlib import Path
from fractions import Fraction as Q
import exact as E
import json,time,sys
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv;start=time.perf_counter()
def H(g):return E.entropy(E.walsh(g))
def state(b,g,nj,sgn,alive):
 t=Q(1,len(b)) if alive else Q(0);C=tuple(int(alive and z==len(b)-1) for z in range(len(b)));K=tuple(v-C[z] for z,v in enumerate(b))
 f=tuple(v*sgn*(-1)**j.bit_count() if C[z] else b[z] for v in g for j in range(1<<nj) for z in range(len(b)))
 hh=H(f);a=E.add({},H(g),t);z=E.add(hh,a,-1)
 # This lane checks the escrow through full physical spectra, not the scalar formula.
 E.le({},z,'actual exterior excess nonnegative')
 return dict(H=hh,A=a,Z=z,t=t,full=f)
nodes=trees=fronts=positive=posttag=innovations=0
for gn,nj0 in ([(3,2)] if pilot else [(2,1),(3,2)]):
 for pol in ([1] if pilot else [0,1,2]):
  trees+=1;b=tuple((-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16))
  g=tuple(-1 if x==(1<<gn)-1 else 1 for x in range(1<<gn));root=state(b,g,nj0,1,True)
  aa=E.walsh(root['full']);E.ok(4*sum(E.influence(aa,j) for j in range(4))==7,'ACTUAL original owner')
  cg=[E.slice_table(g,0,v) for v in (0,1)];ss=[state(b,h,nj0,1,True) for h in cg]
  old=E.add(root['H'],E.add(ss[0]['H'],ss[1]['H']),-Q(1,2));E.ok(E.bounds(old)[0]>0,'old positive actual full debit')
  E.ok(ss[0]['Z']==ss[1]['Z']==root['Z'],'same original escrow after old debit')
  L0=E.add(E.add({2:Q(7)},old,-1),root['Z'],-1);E.le({2:Q(81,32)},L0,'tight original unused reserve')
  depthmax=6+nj0;agg=[dict(H={},B={},w=Q(0)) for _ in range(depthmax+1)]
  agg[0]=dict(H=root['H'],B={2:Q(7)},w=Q(1));nodes+=1
  def visit(b,g,nj,sgn,alive,ids,used,depth,w,L):
   global nodes,positive,posttag,innovations
   nodes+=1;s=state(b,g,nj,sgn,alive);B=E.add(L,s['Z']);E.le({2:Q(1,2)},L,'CURRENT unused reserve>=m/8')
   terminal=not ids and nj==0 and used
   for d in (range(depth,depthmax+1) if terminal else [depth]):
    agg[d]['H']=E.add(agg[d]['H'],s['H'],w);agg[d]['B']=E.add(agg[d]['B'],B,w);agg[d]['w']+=w
   if terminal:return
   choosecore=not used and (pol==1 or (pol==0 and not ids and not nj) or (pol==2 and (len(ids)<=2 or (nj<=1 and sum(g)>0))))
   kind='G' if choosecore else ('J' if nj and (pol==1 or (pol==2 and len(ids)%2==1)) else 'X' if ids else 'J' if nj else 'G')
   children=[]
   for v in (0,1):
    bb=b;gg=g;jj=nj;sg=sgn;al=alive;ii=ids;uu=used
    if kind=='G':gg=E.slice_table(g,0,v);uu=True
    elif kind=='X':bb=E.slice_table(b,0,v);ii=ids[1:];al=alive and v==1
    else:jj=nj-1;sg=sgn*(-1)**v
    children.append((bb,gg,jj,sg,al,ii,uu,state(bb,gg,jj,sg,al)))
   fee={}
   if kind=='G':
    dg=E.add(H(g),E.add(H(children[0][1]),H(children[1][1])),-Q(1,2));E.le({},dg,'core entropy debit sign');E.le(dg,{2:Q(2)},'universal core debit<=2')
    fee=E.add({},dg,s['t'])
    if fee and E.bounds(fee)[0]>0:positive+=1;posttag+=int(nj==0)
   Ln=E.add(L,fee,-1)
   dh=E.add(s['H'],E.add(children[0][-1]['H'],children[1][-1]['H']),-Q(1,2))
   drops=E.add(s['Z'],E.add(children[0][-1]['Z'],children[1][-1]['Z']),-Q(1,2))
   E.ok(dh==E.add(fee,drops),'FULL actual debit=paid core fee+current profile drop')
   bc=[E.add(Ln,ch[-1]['Z']) for ch in children]
   E.ok(dh==E.add(B,E.add(bc[0],bc[1]),-Q(1,2)),'SAME original current total budget')
   if bc[0]!=bc[1]:innovations+=1
   for bb,gg,jj,sg,al,ii,uu,_ in children:visit(bb,gg,jj,sg,al,ii,uu,depth+1,w/2,Ln)
   if time.perf_counter()-start>(55 if pilot else 90):raise RuntimeError('frozen core cap')
  for h in cg:visit(b,h,nj0,1,True,tuple(range(4)),False,1,Q(1,2),L0)
  for z in agg:
   fronts+=1;E.ok(z['w']==1,'both full terminals')
   E.ok(E.add(root['H'],{2:Q(7)},-1)==E.add(z['H'],z['B'],-1),'same original stopped equality after additional core')
  E.walsh.cache_clear();E.cost_cached.cache_clear();E.bounds_cached.cache_clear()
E.ok(positive>0,'actually positive additional core payment')
if not pilot:E.ok(posttag>0,'positive extra core query AFTER final tag actually tested')
out=dict(status='PASS',pilot=pilot,trees=trees,nodes=nodes,frontiers=fronts,positive_additional_core_nodes=positive,positive_posttag_core_nodes=posttag,nonzero_child_innovations=innovations,assertions=E.checks,seconds=time.perf_counter()-start)
(R/'out'/('core_pilot.json' if pilot else 'core_validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
