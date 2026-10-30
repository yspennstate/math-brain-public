from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
exec(compile((ROOT/'code/check.py').read_text(encoding='utf-8').split('cases=')[0],str(ROOT/'code/check.py'),'exec'))
seeds=[('constant+',tuple([1]*2)),('constant-',tuple([-1]*2)),('dictator3',tuple(1-2*(x&1) for x in range(8))),('majority3',tuple(1 if x.bit_count()<=1 else -1 for x in range(8))),('point3',tuple(-1 if x==7 else 1 for x in range(8))),('point2tensor',tuple(core(x,2,2) for x in range(16)))]
rows=[];GHOST=0
for name,h in seeds:
 p,ih=spec(h);u=p.get(0,F(0));v=1-u;mu=F(sum(h),len(h));n=len(h).bit_length()-1;N=1<<n
 for which in [0,1]:
  q={s:F(1,N) if not which else F(1,2) if not s else F(1,2*(N-1)) for s in range(N)}
  qs={0:F(1)} if not v else {0:u,**{s:v*q[s]/(1-q[0]) for s in range(1,N)}}
  B=kl({0:u,1:v},{0:q[0],1:1-q[0]})
  oldCE=add(ent(p),kl(p,q));newCE=add(ent(p),kl(p,qs))
  ck(not add(newCE,scale(oldCE,-1),B));nonnegative(add({2:4*ih},scale(newCE,-1)))
  tt=tuple(1-2*((z>>1)&1) if not z&1 else h[z>>3] if z&4 else 1 for z in range(1<<(n+3)))
  pp,I0=spec(tt);Q={2:F(1,4),3:F(1,4),0:(1+mu)**2/16,1:(1+mu)**2/16,4:(1-mu)**2/16,5:(1-mu)**2/16}
  for s,w in qs.items():
   if s:
    for c in [0,1,4,5]:Q[(s<<3)|c]=w/16
  Q={s:w for s,w in Q.items() if w};ck(sum(Q.values())==1)
  AF=kl(pp,Q);ck(not add(AF,scale(kl(p,qs),-F(1,4))))
  gamma=add(ent(pp),scale(ent(p),-F(1,4)));nonnegative(add({2:F(3)},scale(gamma,-1)))
  GHOST+=sum(s not in pp and w>0 for s,w in Q.items())
  cc=tuple(range(n+3));kids=query(node(tt,cc,Q,F(1)),2);mixed=query(kids[1],1);leaves=[kids[0],*mixed]
  Hf,If,K=totals(leaves);S=add({2:4*If},scale(Hf,-1));nonnegative(add(S,{2:F(-1)}))
  rows.append({'seed':name,'prior':which,'source_empty':str(u),'old_empty':str(q[0]),'calibration_credit_interval':list(map(str,bounds(B))),'root_source_KL_interval':list(map(str,bounds(AF))),'paired_a_S_interval':list(map(str,bounds(S)))})
ck(256**16>2*245**16)
result={'status':'PASS','cases':len(rows),'assertions':COUNT,'physical_nodes':NODES,'root_reference_only_positive_atoms':GHOST,'runtime_seconds':time.perf_counter()-START,'rows':rows,'scope':'A050 initial calibration/lift and one paired-a boundary; A036 constants independently reconstructed in PROOF; source helpers not run'}
save('REVIEW.json',result);print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
