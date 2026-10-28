"""Literal queue/leaf replay, separate from recursive policy profiles."""
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1]
src=(R/'code/check_tree.py').read_text(encoding='utf-8').split('count=0;critical=0')[0]
exec(compile(src,str(R/'code/check_tree.py'),'exec'))
trees=0;resets=0;dependencies=0;negative_reserves=0
for n in range(4):
 for mask in range(1<<(1<<n)):
  f=canonical(tuple(1-2*((mask>>x)&1) for x in range(1<<n)))
  for K in (1,2,8):
   queue=[(f,F(1),0)];leaves=[];qtotal=F(0);Rc=F(0);W=G=occ=();V=F(0)
   while queue:
    h,reach,depth=queue.pop(0);b=(len(h)-1).bit_length()
    stop=(not b) or (depth>0 and (sum(x<0 for x in h)+depth)%3==0)
    if stop:leaves.append((h,reach,depth));continue
    i=(sum(x<0 for x in h)+depth)%b
    ch,rv,wv,gv,pv,uv=node(h,i,K)
    qtotal+=reach;Rc+=reach*rv;W=add(W,mul(wv,reach));G=add(G,mul(gv,reach));V+=reach*pv;occ=add(occ,mul(uv,reach))
    if rv:resets+=1
    if uv:dependencies+=1
    queue.extend((child,reach/2,depth+1) for child in ch)
   ok(sum((r for _,r,_ in leaves),F(0))==1)
   ok(sum((r*d for _,r,d in leaves),F(0))==qtotal)
   dt=add(*(mul(deficit(h,K),r) for h,r,_ in leaves));droot=deficit(f,K);kappa=logq(1+F(2)**(3-K))
   ok(add(droot,mul(dt,-1),rat(K*Rc),W,G)==mul(kappa,qtotal))
   if Rc:ok(add(droot,mul(dt,-1),W,G)!=mul(kappa,qtotal))
   if nonneg(dt) and dt:negative_reserves+=1
   trees+=1
# A singleton occupied event has no internal pattern entropy. Its entire
# conditional W1 is exterior dependence, so replacing the exterior reference
# by its conditional marginal would incorrectly set this positive term to zero.
f=canonical((-1,)+(1,)*7);ch,rv,wv,gv,pv,uv=node(f,0,8)
ok(pv==F(1,4));ok(nonneg(uv) and bool(uv));ok(bool(wv))
# Positive root deficit does not make the full proper-child reserve nonnegative.
ch,rv,wv,gv,pv,uv=node(f,0,1);dc=mul(add(*(deficit(h,1) for h in ch)),F(1,2))
ok(nonneg(deficit(f,1)) and bool(deficit(f,1)));ok(nonneg(dc) and bool(dc))
ok(resets>0);ok(dependencies>0);ok(negative_reserves>0)
out={'status':'PASS','literal_trees':trees,'assertions':checks,'nonzero_reset_nodes':resets,'positive_exterior_dependence_nodes':dependencies,'negative_reserve_trees':negative_reserves,'seconds':time.monotonic()-start,'scope':'separate queue traversal and literal full-terminal reaches; shared exact local entropy kernels','guards':['omitted reset term breaks equality','point-defect occupied exterior KL positive','K1 positive root has negative child reserve']}
(R/'out/REPLAY.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
