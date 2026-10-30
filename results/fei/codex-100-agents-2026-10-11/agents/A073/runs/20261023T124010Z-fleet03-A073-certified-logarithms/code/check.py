from pathlib import Path
from fractions import Fraction as F
from itertools import product
import importlib.util,json,time,hashlib,sys
R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
helper=R.parent/'20261023T031904Z-fleet03-A073-certified-logarithms/code/check.py'
sp=importlib.util.spec_from_file_location('own_boolean',helper);b=importlib.util.module_from_spec(sp);sp.loader.exec_module(b)
def save(n,d):(O/n).write_text(json.dumps(d,indent=2,default=str)+'\n',encoding='utf-8')
def spike(p,alpha):
 if len(p)==1:return dict(p)
 full=0
 for s in p:full|=s
 q={s:(v if s==0 else (1-alpha)*v) for s,v in p.items()}
 q[full]=q.get(full,F(0))+alpha*(1-p.get(0,F(0)))
 return {s:v for s,v in q.items() if v}
def restriction(t,labels,j,y):
 k=labels.index(j);ls=tuple(a for a in labels if a!=j)
 return tuple(t[(s&((1<<k)-1))|((s>>k)<<(k+1))|(y<<k)] for s in range(1<<len(ls))),ls
def lift(n,q):
 ref={s:v for s,v in n.p.items() if not s>>3}
 for s,v in q.items():
  if s:
   for x in (0,1):ref[s|x]=v/4
 return b.Node(n.t,n.labels,ref)
def difference(p,qnew,qold):
 if qnew==qold:return F(0),F(0)
 a,c=b.ce(p,qnew);d,e=b.ce(p,qold);return a-e,c-d
def make(mask):
 labels=(3,4,5);t=tuple(-1 if mask>>s&1 else 1 for s in range(8));p=b.spec(t,labels);q=spike(p,F(1,8))
 ft=tuple((-1)**(s>>1&1) if not s&1 else (t[s>>3] if s>>2&1 else 1) for s in range(64))
 fp=b.spec(ft,tuple(range(6)));fq={s:v for s,v in fp.items() if not s>>3}
 for s,v in q.items():
  if s:
   for z in (0,1,4,5):fq[s|z]=v/16
 return b.Node(ft,tuple(range(6)),fq),t,labels,p,q
def run(pilot):
 start=time.monotonic();masks=[0,1,22,23,105,255] if pilot else list(range(256));tag='PILOT' if pilot else 'MAIN';count=len(masks)*6
 save(tag+'_FROZEN.json',{'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependency_helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),'family':'ALL three-bit Boolean cores, original whole-essential-block1/8 correlated lift; b then a BOTH signs, full first1/7 resets; one chosen sign queries any core coordinate; retain and reset BOTH data children at same1/7','truth_masks':masks,'case_count':count,'symmetry':'none; all256 truth tables in main','arithmetic':'Fraction truth tables, Walsh and physical influences, coherent references with fair source-zero fallback; fixed16-term certified logs','memory_MB':120,'max_runtime_seconds':55 if pilot else 240,'precision_stop':'no refinement after sign; exact equality recognized atomwise'})
 checks=cases=pos=neg=zero=0;fixture=None;minreserve=F(100);minsupplier=F(100)
 for mask in masks:
  assert time.monotonic()-start<(55 if pilot else 240)
  root,t,labels,p,q=make(mask);Ic=b.influence(t,labels);hc=b.ent(p);cc=b.ce(p,q);mu=F(sum(t),8)
  if Ic:
   assert 4*Ic-cc[1]>0;minsupplier=min(minsupplier,4*Ic-cc[1]);checks+=1
   assert 4*Ic-hc[1]>=1-abs(mu);checks+=1
  else:assert hc==cc==(F(0),F(0));checks+=1
  b0=root.child(2,0);b1=root.child(2,1)
  original=[b1.child(1,y) for y in (0,1)];fresh=[lift(n,spike(p,F(1,7))) for n in original]
  dfirst=[difference(n.p,r.q,n.q) for n,r in zip(original,fresh)];sig1lo=sum(z[0] for z in dfirst)/4;sig1hi=sum(z[1] for z in dfirst)/4
  h0=b.ent(root.p);c0=b.ce(root.p,root.q);Ahi=c0[1]-h0[0]
  for sign in (0,1):
   for j in labels:
    incoming=[fresh[sign].child(j,y) for y in (0,1)]
    cps=[];targets=[]
    for y,n in enumerate(incoming):
     ct,cl=restriction(t,labels,j,y);cp=b.spec(ct,cl);cps.append(cp);targets.append(lift(n,spike(cp,F(1,7))))
     if b.influence(ct,cl):assert b.ent(cp)[1]<=4*b.influence(ct,cl)
     else:assert b.ent(cp)==(F(0),F(0))
     checks+=1
    ds=[difference(n.p,z.q,n.q) for n,z in zip(incoming,targets)];local_lo=sum(z[0] for z in ds)/2;local_hi=sum(z[1] for z in ds)/2
    if local_lo>0:pos+=1
    elif local_hi<0:neg+=1
    elif all(n.q==z.q for n,z in zip(incoming,targets)):zero+=1
    else:
     save('UNRESOLVED_SIGN.json',{'mask':mask,'sign':sign,'coordinate':j,'interval':[local_lo,local_hi]});raise AssertionError('fixed precision unresolved, no sign claimed')
    checks+=1
    leaves=[(F(1,2),b0),(F(1,4),fresh[1-sign])]+[(F(1,8),n) for n in targets]
    Hlo=Hhi=If=KLlo=F(0)
    for w,n in leaves:
     a,c=b.ent(n.p);Hlo+=w*a;Hhi+=w*c;If+=w*n.I;d,e=b.ce(n.p,n.q);KLlo+=w*(d-c)
    sigma2_hi=local_hi/4;ehi=h0[1]-Hlo-4*(root.I-If)
    reserve=4*If-Hhi-max(F(0),Ahi+ehi+sig1hi+sigma2_hi)-F(1,4)
    assert reserve>=F(3,4);checks+=1;minreserve=min(minreserve,reserve)
    assert KLlo<=Ahi+sig1hi+sigma2_hi;checks+=1
    if mask==22 and sign==0 and j==3:
     assert local_lo>F(1,4096)
     K=F(1)
     for n,z in zip(incoming,targets):
      for s,v in n.p.items():assert (16*v).denominator==1;K*=(n.q[s]/z.q[s])**int(16*v)
     assert K>1 and K.numerator**128>2*K.denominator**128
     fixture={'truth_mask':mask,'core_truth':t,'sign':sign,'data_coordinate':j,'local_average_price_bits':'log2(N/D)/32','N':K.numerator,'D':K.denominator,'certified_positive_margin':'local average reset >1/4096 bits','comparison':'N^128>2D^128','first_weighted_price_interval':[sig1lo,sig1hi],'second_weighted_price_interval':[local_lo/4,local_hi/4],'remaining_original_reserve_lower':reserve,'old_booking':F(1,4),'incoming_children':[n.q for n in incoming],'fresh_children':[n.q for n in targets],'child_spectra':[n.p for n in incoming]}
    cases+=1
  save(tag+'_CHECKPOINT.json',{'last_truth_mask':mask,'cases':cases,'checks':checks,'status':'PASS_so_far'})
 assert cases==count and fixture
 save(tag+'_CHECK.json',{'status':'PASS','truth_tables':len(masks),'cases':cases,'checks':checks,'local_prices':{'positive':pos,'negative':neg,'zero':zero},'minimum_original_reserve_lower':minreserve,'minimum_nonconstant_initial_supplier_margin':minsupplier,'runtime_seconds':time.monotonic()-start,'all_dimensional_scope':'finite checker validates n<=3 supplied interface; eight-generation conditional theorem is analytic in PROOF.md'})
 save(tag+'_A049_FIXTURE.json',fixture)
 save('EIGHT_RESET_INTEGER_SIGN.json',{'logarithm':'log2(7/6)<1/4','lhs':7**4,'rhs':2*6**4,'strict_integer_margin':2*6**4-7**4,'generations':8,'original_margin':'M0>=1+2t','total_reset_gross_bound':'8*Var(g)*log2(7/6)/4 <2t(1-t)','remaining_original_margin':'>=1+2t^2; old quarter retained'})
 print(json.dumps({'mode':tag,'status':'PASS','cases':cases,'checks':checks,'positive':pos,'negative':neg,'zero':zero,'runtime_seconds':time.monotonic()-start}))
if __name__=='__main__':run('--pilot' in sys.argv)
