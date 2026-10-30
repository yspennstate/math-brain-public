from pathlib import Path
from fractions import Fraction as Q
import exact as E
import itertools,json,time,sys
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv;start=time.perf_counter()
def budget():
 if time.perf_counter()-start>(55 if pilot else 180):raise RuntimeError('frozen cap')
def H(t):return E.entropy(E.walsh(t))
def profile(K,C,mu):
 kh=E.walsh(K);ch=E.walsh(C);c=Q(sum(C),len(C))
 return E.add(E.add(E.entropy(tuple(a+mu*b for a,b in zip(kh,ch))),E.cost(mu*mu),-c),E.entropy(ch),1-mu*mu)
def generic(K,C,g):
 c=Q(sum(C),len(C));ga=E.walsh(g)
 f=tuple(K[z]+C[z]*v for v in g for z in range(len(C)));fa=E.walsh(f)
 ex=E.add(E.entropy(fa),H(g),-c)
 E.ok(ex==profile(K,C,ga[0]),'scalar profile identity')
 for u,x in enumerate(ga):E.ok(sum(fa[u*len(C)+z]**2 for z in range(len(C)))==c*x*x+(1-c)*(u==0),'actual core marginal')
 E.le({},ex,'profile nonnegative')
 upper=E.add({2:len(C).bit_length()-1},E.add(E.cost(c),E.cost(1-c)))
 E.le(ex,upper,'profile m+h2(c) upper')
 return f
roots=0;direct=0
gs=[tuple(1-2*((mask>>x)&1) for x in range(4)) for mask in range(16)]
for cfg in itertools.product((-1,0,1),repeat=4):
 C=tuple(int(x==0) for x in cfg);K=cfg
 for g in gs:
  generic(K,C,g);roots+=1;budget()
  if pilot and roots>=81:break
 if pilot and roots>=81:break
if not pilot:
 C=(0,0,0,1);K=(1,1,-1,0)
 for g in gs:
  tagged=tuple(v*(-1)**j for v in g for j in range(2))
  f=generic(K,C,tagged)
  # Independent direct character sums, bitwise intersection rather than FWHT.
  aa=tuple(Q(sum(v*(-1)**((x&s).bit_count()) for x,v in enumerate(f)),len(f)) for s in range(len(f)))
  E.ok(aa==E.walsh(f),'direct five-bit amplitude reproduction');direct+=1

def state(b,g,nj,sgn,alive):
 c=Q(1,len(b)) if alive else Q(0);C=tuple(int(alive and z==len(b)-1) for z in range(len(b)));K=tuple(v-C[z] for z,v in enumerate(b))
 f=tuple(v*sgn*(-1)**j.bit_count() if C[z] else b[z] for v in g for j in range(1<<nj) for z in range(len(b)))
 mu=Q(0) if nj else sgn*Q(sum(g),len(g));hh=H(f);a=E.add({},H(g),c);ex=profile(K,C,mu)
 E.ok(hh==E.add(a,ex),'actual inherited core plus scalar exterior')
 E.le({},ex,'current escrow nonnegative')
 return dict(H=hh,A=a,Z=ex,t=c,full=f)
nodes=trees=fronts=positive=innovations=negative_literal_cash=0
literal_witness=None
for gn,jwidth in ([(2,1)] if pilot else [(2,1),(3,2)]):
 for policy in ([0] if pilot else [0,1,2]):
  trees+=1;g=tuple(-1 if x==(1<<gn)-1 else 1 for x in range(1<<gn))
  b=tuple((-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16))
  root=state(b,g,jwidth,1,True);B0=Q(7);mdepth=1+4+jwidth
  old=[E.slice_table(g,0,v) for v in (0,1)];st=[state(b,h,jwidth,1,True) for h in old]
  oldcost=E.add(root['H'],E.add(st[0]['H'],st[1]['H']),-Q(1,2))
  E.ok(oldcost==E.add({},E.add(H(g),E.add(H(old[0]),H(old[1])),-Q(1,2)),Q(1,16)),'exact old core cost')
  E.ok(E.bounds(oldcost)[0]>0,'actual positive old debit');positive+=1
  E.ok(st[0]['Z']==st[1]['Z']==root['Z'],'same start escrow in both old children')
  L=E.add(E.add({2:B0},oldcost,-1),root['Z'],-1);E.le({2:Q(1)},L,'unused original >=m/4')
  agg=[dict(H={},B={},w=Q(0)) for _ in range(mdepth+1)]
  agg[0]=dict(H=root['H'],B={2:B0},w=Q(1));nodes+=1
  def visit(b,g,nj,sgn,alive,ids,depth,w,spent,path):
   global nodes,innovations,negative_literal_cash,literal_witness
   nodes+=1;s=state(b,g,nj,sgn,alive);cash=E.add(L,s['Z'])
   E.le(L,cash,'same-owner nonnegative residual profile')
   literal=E.add({2:B0},spent,-1)
   if literal and E.bounds(literal)[1]<0:
    negative_literal_cash+=1
    if literal_witness is None:literal_witness=dict(path=path,cash_nats_prime_logs={str(p):str(q) for p,q in literal.items()})
   terminal=not ids and nj==0
   for d in (range(depth,mdepth+1) if terminal else [depth]):
    agg[d]['H']=E.add(agg[d]['H'],s['H'],w);agg[d]['B']=E.add(agg[d]['B'],cash,w);agg[d]['w']+=w
   if terminal:return
   if policy==0:kind='X' if ids else 'J'
   elif policy==1:kind='J' if nj else 'X'
   else:kind='J' if nj and (len(ids)%2==1 or s['t']==0) else 'X' if ids else 'J'
   index=0 if kind=='J' else (len(ids)-1 if policy==2 else 0)
   children=[]
   for v in (0,1):
    if kind=='X':bb=E.slice_table(b,index,v);jj=nj;ss=sgn;al=alive and v==1;ii=ids[:index]+ids[index+1:]
    else:bb=b;jj=nj-1;ss=sgn*(-1)**v;al=alive;ii=ids
    z=state(bb,g,jj,ss,al);children.append((bb,jj,ss,al,ii,z))
   dh=E.add(s['H'],E.add(children[0][-1]['H'],children[1][-1]['H']),-Q(1,2))
   ez=E.add({},E.add(children[0][-1]['Z'],children[1][-1]['Z']),Q(1,2))
   E.ok(dh==E.add(s['Z'],ez,-1),'exact current cash drop and full debit')
   E.ok(s['A']==E.add({},E.add(children[0][-1]['A'],children[1][-1]['A']),Q(1,2)),'inherited core remains harmonic')
   if kind=='J' and nj==1:
    C=tuple(int(alive and z==len(b)-1) for z in range(len(b)));K=tuple(v-C[z] for z,v in enumerate(b))
    kh=E.walsh(K);ch=E.walsh(C);alpha=sgn*Q(sum(g),len(g));q=alpha*alpha;dd={};packet={}
    for aa,cc in zip(kh,ch):
     dd=E.add(dd,E.paird(aa,alpha*cc));packet=E.add(packet,E.phi(aa*aa,q*cc*cc))
    E.ok(dh==dd,'exact current last-tag packet')
    remainder=E.add(dh,packet,-1);E.le({},remainder,'physical JS nonnegative');E.leconst(remainder,2*s['t']*q,'JS<=2tq nats')
    cap=E.add({2:s['t']*q*(len(ids)+Q(9,2))},E.cost(q),s['t'])
    E.le(dh,cap,'retained current q-log ticket')
   if children[0][-1]['Z']!=children[1][-1]['Z']:innovations+=1
   for v,(bb,jj,ss,al,ii,_) in enumerate(children):visit(bb,g,jj,ss,al,ii,depth+1,w/2,E.add(spent,dh),path+[(kind,ids[index] if kind=='X' else nj,v)])
   budget()
  for v,h in enumerate(old):visit(b,h,jwidth,1,True,tuple(range(4)),1,Q(1,2),oldcost,[('old',0,v)])
  for z in agg:
   E.ok(z['w']==1,'both full actual terminals')
   E.ok(E.add(root['H'],{2:B0},-1)==E.add(z['H'],z['B'],-1),'same original full stopped equality');fronts+=1
  E.walsh.cache_clear();E.cost_cached.cache_clear();E.bounds_cached.cache_clear()

# Exterior-only profile roots use no giant inherited-core truth table.
large_roots=[]
if not pilot:
 for m in (4,8,12,16):
  n=1<<m;c=Q(1,n)
  # For paired quadratic, bhat(s)=2^-m/2 b(s); all-one point chat=c*(-1)^|s|.
  kh=tuple(Q((-1)**sum(((s>>(2*j))&1)*((s>>(2*j+1))&1) for j in range(m//2)),1<<(m//2))-c*(-1)**s.bit_count() for s in range(n))
  z=E.add(E.entropy(kh),{2:2*c*m});B0=2*m-4*m*c
  E.le(z,{2:m+1},'dimension bound actual exterior root')
  E.le({2:Q(m,4)},E.add({2:B0-2*c},z,-1),'all omitted small-m roots have original escrow margin')
  large_roots.append(dict(m=m,B0=str(B0)));budget();E.cost_cached.cache_clear();E.bounds_cached.cache_clear()
cert=[]
for m in range(4,65,4):
 c=Q(1,1<<m);N=m*(1<<m)-2*m+1;B0=2*m-4*m*c
 E.ok(2*c*N-B0==2*c,'implicit actual Boolean product obstruction')
 E.ok(2*c*(N-1)>B0-2*c,'same diminished owner after positive old debit')
 cert.append(dict(m=m,N=N,core_variables=2*N,old_debit=str(2*c),B0=str(B0),total_debit=str(2*c*N),deficit=str(2*c)))
E.ok(H((1,1,1,-1))=={2:Q(2)},'exact AND2 factor entropy')
for v in (0,1):E.ok(H(E.slice_table((1,1,1,-1),0,v))=={},'both old AND2 restrictions have zero entropy')
out=dict(status='PASS',pilot=pilot,generic_roots=roots,direct_roots=direct,mixed_trees=trees,nodes=nodes,frontiers=fronts,positive_old_debits=positive,nonzero_child_innovations=innovations,negative_literal_cash_nodes=negative_literal_cash,literal_cash_witness=literal_witness,exterior_roots=large_roots,obstruction_certificates=cert,assertions=E.checks,seconds=time.perf_counter()-start)
(R/'out').mkdir(exist_ok=True)
(R/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k not in ('obstruction_certificates','literal_cash_witness')}))
