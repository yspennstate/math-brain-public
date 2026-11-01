from prior import *

COUNT=0;NODES=0;ZEROFIBERS=0;NULLCHILDREN=0
def ck(ok):
 global COUNT
 COUNT+=1
 assert ok

def clean(a):return {k:v for k,v in a.items() if v}
def lift(p):
 q={}
 for s,v in enumerate(p):
  if not v:continue
  ls=[j for j in range(s.bit_length()) if s>>j&1] if s else [-1]
  for l in ls:q[s,l]=v/len(ls)
 return q

def cem(p,q):
 out={}
 for j,v in p.items():
  if v:ck(q.get(j,0)>0);out=add(out,log(q[j]),-v)
 return out

def overhead(p):
 out={}
 for s,v in enumerate(p):
  if s and v:out=add(out,log(s.bit_count()),v)
 return out

def reduced(s,i):return (s&((1<<i)-1))|((s>>(i+1))<<i)

def query(f,r,i):
 global NODES,ZEROFIBERS,NULLCHILDREN
 NODES+=1;p=prob(f);fs=[restrict(f,i,b) for b in [0,1]];ps=[prob(g) for g in fs]
 jp,jr=lift(p),lift(r);ck(sum(jp.values())==sum(jr.values())==1)
 lp=overhead(p);c0=ce(p,r);cj=cem(jp,jr)
 ck(cj==add(c0,lp));ck(add(cj,cem(jp,jp),-1)==add(c0,entropy(f),-1))
 outp=[{},{}];outr=[{},{}];rawr=[[Q(0)]*len(ps[0]) for _ in range(2)]
 for t in range(len(ps[0])):
  s0=(t&((1<<i)-1))|((t>>i)<<(i+1));s1=s0|(1<<i);mass=p[s0]+p[s1]
  ck(ps[0][t]+ps[1][t]==2*mass)
  kap=[ps[b][t]/(2*mass) for b in range(2)] if mass else [Q(1,2)]*2
  ck(sum(kap)==1)
  if not mass and r[s0]+r[s1]:ZEROFIBERS+=1
  for b in range(2):rawr[b][t]=(r[s0]+r[s1])*kap[b]
  for s in [s0,s1]:
   ls=[j for j in range(s.bit_length()) if s>>j&1] if s else [-1]
   for l in ls:
    if not t:targets=[(-1,Q(1))]
    elif l==i:
     pts=[j for j in range(t.bit_length()) if t>>j&1];targets=[(j,Q(1,len(pts))) for j in pts]
    else:targets=[(l-(l>i),Q(1))]
    ck(sum(q for _,q in targets)==1)
    for b in range(2):
     for mark,q in targets:
      key=(t,mark);outp[b][key]=outp[b].get(key,Q(0))+jp.get((s,l),Q(0))*kap[b]*q
      outr[b][key]=outr[b].get(key,Q(0))+jr.get((s,l),Q(0))*kap[b]*q
 refs=[];zs=[];jointchild=[]
 for b in range(2):
  outp[b]=clean(outp[b]);outr[b]=clean(outr[b])
  ck(outp[b]=={j:q/2 for j,q in lift(ps[b]).items()});ck(outr[b]==lift(rawr[b]))
  z=sum(rawr[b]);ck(z>0);zs.append(z);rr=[q/z for q in rawr[b]]
  calibrated=[]
  for t,q in enumerate(rr):
   pm=ps[b][0] if not t else 1-ps[b][0];qm=rr[0] if not t else 1-rr[0]
   ck(not pm or qm>0);calibrated.append(q*pm/qm if pm else Q(0))
  refs.append(tuple(calibrated));ck(sum(calibrated)==1);ck(calibrated[0]==ps[b][0])
  # Independently calibrate the actual pushed JOINT reference by null mark.
  jq={}
  for key,q in outr[b].items():
   pm=ps[b][0] if key[0]==0 else 1-ps[b][0];qm=rr[0] if key[0]==0 else 1-rr[0]
   if pm:jq[key]=(q/z)*pm/qm
  ck(clean(jq)==lift(calibrated))
  if ps[b][0]==1:NULLCHILDREN+=1
  jointchild.append(cem(lift(ps[b]),lift(calibrated)))
 ck(sum(zs)==1)
 lc=scale(add(overhead(ps[0]),overhead(ps[1])),Q(1,2));lam=add(lp,lc,-1)
 formula={};rho={}
 for s,q in enumerate(p):
  d=s.bit_count()
  if (s>>i)&1 and d>=2:
   formula=add(formula,log(Q(d,d-1)),q);rho=add(rho,log(d-1),q/d)
 ck(lam==formula);inf=edge_inf(f,i)
 ck(nonnegative(lam));ck(nonnegative(rho));ck(nonnegative(add({2:inf},lam,-1)));ck(nonnegative(add({2:inf},rho,-1)))
 ck(nonnegative(add({2:influence(f)-(1-p[0])},lp,-1)))
 terminal=scale(add(ce(ps[0],refs[0]),ce(ps[1],refs[1])),Q(1,2));drop=add(c0,terminal,-1)
 jt=scale(add(jointchild[0],jointchild[1]),Q(1,2));jdrop=add(cj,jt,-1)
 ck(jdrop==add(drop,lam));ck(nonnegative(drop));ck(nonnegative(jdrop))
 hdrop=add(entropy(f),scale(add(entropy(fs[0]),entropy(fs[1])),Q(1,2)),-1);B=erasure(f,i)
 ck(nonnegative(B));ck(nonnegative(add(hdrop,B,-1)))
 parentD=add(c0,entropy(f),-1);childD=scale(add(add(ce(ps[0],refs[0]),entropy(fs[0]),-1),add(ce(ps[1],refs[1]),entropy(fs[1]),-1)),Q(1,2))
 ck(nonnegative(add(parentD,childD,-1)))
 ck(influence(f)==inf+sum((influence(g) for g in fs),Q(0))/2)
 return fs,refs,{'Z':[str(z) for z in zs],'lambda':lam,'rho':rho,'base_release':drop,'joint_release':jdrop,'base_terminal':terminal,'joint_terminal':jt,'I_spent':inf}

def fulltree(f,r):
 base={};joint={};lam={};rho={};spent=Q(0);term={};termL={};remain=Q(0);leaves=0;nodes=0
 def visit(g,rr,reach):
  nonlocal base,joint,lam,rho,spent,term,termL,remain,leaves,nodes
  if influence(g)==0:
   term=add(term,cem(lift(prob(g)),lift(rr)),reach);termL=add(termL,overhead(prob(g)),reach);remain+=reach*influence(g);leaves+=1;return
  gs,rs,c=query(g,rr,0);nodes+=1
  base=add(base,c['base_release'],reach);joint=add(joint,c['joint_release'],reach);lam=add(lam,c['lambda'],reach);rho=add(rho,c['rho'],reach);spent+=reach*c['I_spent']
  for b in range(2):visit(gs[b],rs[b],reach/2)
 visit(f,r,Q(1));p=prob(f);ii=influence(f);v=1-p[0];lp=overhead(p);initial=ce(p,r)
 ck(add(joint,term)==add(initial,lp));ck(lam==add(lp,termL,-1));ck(ii==spent+remain)
 ck(nonnegative(add({2:spent},rho,-1)));bill=add(add(joint,term),rho)
 ck(nonnegative(add(add(initial,{2:2*ii-v-remain}),bill,-1)))
 return {'nodes':nodes,'leaves':leaves,'initial_I':str(ii),'old_base_debit':ser(base),'full_joint_debit':ser(joint),'full_terminal_CE':ser(term),'lambda_total':ser(lam),'reselection_entropy_total':ser(rho),'combined_bill':ser(bill)}

def parity_cases(ds):
 out=[]
 for d in ds:
  lam=log(Q(d,d-1));rho=scale(log(d-1),Q(1,d));ck(nonnegative(add({2:Q(1)},rho,-1)))
  complete={}
  for j in range(2,d+1):complete=add(complete,log(j-1),Q(1,j))
  ck(nonnegative(add({2:Q(d)},complete,-1)))
  if d==8:ck(nonnegative(add(rho,lam,-1)));ck(7**9>8**8)
  out.append({'degree':d,'lambda':ser(lam),'rho':ser(rho),'full_character_tree_rho':ser(complete)})
 return out

def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;lane=int(sys.argv[sys.argv.index('--lane')+1]) if '--lane' in sys.argv else None
 codes=[23] if pilot else [c for c in range(256) if c%4==lane];records=[];trees=[];single=0
 for c in codes:
  ck(time.perf_counter()-start<55);f=table(3,c)
  for uniform in [False,True]:
   rr=phase_ref(f,False) if uniform else prob(f)
   for i in ([0] if pilot else range(3)):
    gs,rs,rec=query(f,rr,i);single+=1
    if len(records)<8:records.append({'code':c,'uniform':uniform,'i':i,**{k:ser(v) if isinstance(v,dict) else str(v) if isinstance(v,Q) else v for k,v in rec.items()}})
   tr=fulltree(f,rr);tr.update(code=c,uniform=uniform);trees.append(tr)
 ps=parity_cases(range(2,9) if pilot else range(2,65)) if pilot or lane==0 else []
 out={'status':'PASS','helper':'A056-per-set-witness-physical-kernel-v1','pilot':pilot,'lane':lane,'assertions_executed':COUNT,'single_queries':single,'full_trees':len(trees),'physical_nodes_checked':NODES,'reference_only_pair_fibers':ZEROFIBERS,'constant_child_laws':NULLCHILDREN,'runtime_seconds':time.perf_counter()-start,'examples':records,'trees':trees,'parity_cases':ps,'full_FEI':'OPEN'}
 (R/'out'/('pilot.json' if pilot else f'lane{lane}.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ['examples','trees','parity_cases']}|{'parity_cases':len(ps)},indent=2))

if __name__=='__main__':main()
