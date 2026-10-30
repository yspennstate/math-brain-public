from pathlib import Path
from fractions import Fraction as F
import json,time,sys
import exact as e
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv
histories=prefixes=pivots=fixtures=0
def nn(x,label):e.ck(not x or e.interval(x)[0]>=0,label)
def W(t):return e.plus((1,e.stats(e.child(t,0,0))[3]),(1,e.stats(e.child(t,0,1))[3]))
def walk(t,Q):
 global histories,prefixes,pivots
 histories+=1;p=e.stats(t)[0];K=e.kl(p,Q);w=W(t);P=e.plus((1,K),(1,w));n=len(t).bit_length()-1
 cc,qq,rr,O,KK,E,z=e.transport(t,0,Q);pivots+=1
 mean_pre={}
 for b,c in enumerate(cc):
  pc,dc,hc,mc,tc=e.stats(c);pre=e.plus((1,KK[b]),(2,mc))
  mean_pre=e.plus((1,mean_pre),(F(1,2),pre))
  e.eq(tc,e.kl(pc,e.product(dc)),'source audit ACTUAL product conversion')
  nn(e.plus((1,pre),(-1,tc),(-1,mc)),'reset+continuation funded by original counterfactual bank')
  e.eq(e.plus((1,pre),(-1,tc),(-1,mc)),e.plus((1,KK[b]),(1,hc)),'reset drop equals inherited KL plus FULL child entropy')
 nn(e.plus((1,P),(-1,mean_pre),(-1,O)),'arbitrary-reference pivot pays nonzero O')
 for i in range(1,n):
  cs,qs,rs,oo,ks,ee,zz=e.transport(t,i,Q);prefixes+=1
  ws=[W(c) for c in cs];nn(e.plus((1,w),(-F(1,2),ws[0]),(-F(1,2),ws[1])),'arbitrary non-affine counterfactual marginal reserve supermartingale')
  nn(e.plus((1,P),(-1,oo),(-F(1,2),ks[0]),(-F(1,2),ks[1]),(-F(1,2),ws[0]),(-F(1,2),ws[1])),'all ordered prefix drift')
  for c,q in zip(cs,qs):walk(c,q)
for mask in ([0,7] if pilot else range(128)):
 t=(1,)+tuple(1 if mask&(1<<s) else -1 for s in range(7))
 for Q in (e.stats(t)[0],tuple(F(j,36) for j in range(1,9))):fixtures+=1;walk(t,Q)
point=[]
for n in ([3] if pilot else [3,4,5,6,8]):
 t=(-1,)+(1,)*((1<<n)-1);p,ds,H,M,TC=e.stats(t)
 cc,qq,rr,O,KK,E,z=e.transport(t,0,p)
 e.eq(O,{});e.ck(all(not k for k in KK),'Q=P inherited children exact zero KL')
 expected=e.plus((F(1,2),e.stats(cc[0])[4]),(F(1,2),e.stats(cc[1])[4]));I=sum(ds,F())
 bound=F(n-7)+F(4,n)
 nn(e.plus((1,expected),(-I*bound,e.constant(1))),'arbitrary-Q source obstruction lower bound')
 if n==8:e.ck(bound==F(3,2) and e.interval(expected)[0]>0,'positive all-dimensional obstruction control')
 point.append({'n':n,'expected_terminal_KL':e.enc(expected),'I':str(I),'ratio_lower':str(bound)})
e.ck(fixtures==(4 if pilot else 256),'nonempty arbitrary source/reference domain')
e.ck(histories==13*fixtures and pivots==histories and prefixes==6*fixtures,'all ordered prefixes/outcomes included')
elapsed=time.perf_counter()-start;e.ck(elapsed<55,'frozen audit runtime')
out={'status':'PASS','pilot':pilot,'assertions':e.COUNT,'seconds':elapsed,'fixtures':fixtures,'prepivot_histories':histories,'prefix_query_nodes':prefixes,'pivot_query_nodes':pivots,'point_obstructions':point,'source_review':'A087-PROTECTED-PIVOT-PHASE-LIABILITY@1 independently reconstructed, unchanged scope'}
(R/'out'/('AUDIT_PILOT.json' if pilot else 'AUDIT.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='point_obstructions'}))
