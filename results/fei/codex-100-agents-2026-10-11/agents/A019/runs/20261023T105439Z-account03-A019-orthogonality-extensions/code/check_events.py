import json,sys,time,hashlib,math
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261014T055119Z-account05-A019-orthogonality-extensions/code/check_exposure.py'
src=OLD.read_text(encoding='utf-8');ns={'Q':Q,'lru_cache':lru_cache,'checks':0}
exec(src[src.index('def ck(x):'):src.index("transport={'positive'")],ns)
ck,add,lf,psi,iv=[ns[z] for z in ('ck','add','logform','psi','interval')]
def scale(q,f):return add((q,f))
def const(q):return {2:Q(q)} if q else {}
def nonneg(f):return not f or iv(f)[0]>=0
def positive(f):return bool(f) and iv(f)[0]>0
def pos(f):
 if positive(f):return f
 ck(nonneg(scale(-1,f)));return {}
def entropy(p):return ce(p,p)
def ce(p,q):
 out={}
 for (a,b),count in Counter(zip(p,q)).items():
  if a:ck(b>0);out=add((1,out),(-a*count,lf(b)))
 return out
def fw(tt):
 a=list(tt);s=1
 while s<len(a):
  for z in range(0,len(a),2*s):
   for j in range(z,z+s):a[j],a[j+s]=a[j]+a[j+s],a[j]-a[j+s]
  s*=2
 return tuple(Q(z,len(a)) for z in a)
def spectrum(tt):return tuple(z*z for z in fw(tt))
def cut(i,j):return (i&((1<<j)-1))|((i>>(j+1))<<j)
def fold(a,j):
 out=[Q(0)]*(len(a)//2)
 for i,v in enumerate(a):out[cut(i,j)]+=v
 ck(sum(out)==1);return tuple(out)
def restrict(tt,j,b):return tuple(tt[(i&((1<<j)-1))|((i>>j)<<(j+1))|(b<<j)] for i in range(len(tt)//2))
def contam(p):return tuple((z+int(i==0))/2 for i,z in enumerate(p))
def afun(p,z):
 out=scale((1+p)/2,lf((1+z)/(1+p)))
 return add((1,out),(p/2,lf(p/z))) if p else out
def actcost(tt,ref):
 p=spectrum(tt);mean=Q(sum(tt),len(tt))
 return add((1,const(1)),(Q(1,2),ce(p,ref)),(1,psi(mean/2)),(-1,afun(mean*mean/4,ref[0]/4)))
def actual_act(tt,ref,literal=False):
 coeff=fw(tt);pp=[];qq=[]
 for mask in range(4):
  sm=Q(1 if mask==0 else -1,2)
  for j,a in enumerate(coeff):
   i=mask*len(tt)+j;v=a*sm;aa=(int(i==0)+v)/2;bb=(int(i==0)-v)/2
   m=aa*aa+bb*bb;r=(ref[j]/4+int(i==0))/2
   frac=aa*aa/m if m else Q(1)
   pp.extend((aa*aa,bb*bb));qq.extend((r*frac,r*(1-frac)))
 ck(sum(pp)==sum(qq)==1);ck(ce(pp,qq)==actcost(tt,ref))
 if literal:
  vals=tuple(v for s in (-1,1,1,1) for h in tt for v in (1,h*s))
  slow=tuple(Q(sum(v*(-1 if (a&i).bit_count()%2 else 1) for i,v in enumerate(vals)),len(vals))**2 for a in range(len(vals)))
  ck(tuple(pp)==slow)
 return tuple(pp),tuple(qq)
def lift(t0,t1,r0,r1):
 tt=tuple(v for pair in zip(t0,t1) for v in pair);p=spectrum(tt);ref=[]
 for i in range(len(t0)):
  mass=p[2*i]+p[2*i+1];r=(r0[i]+r1[i])/2
  ref.extend((r*p[2*i]/mass,r*p[2*i+1]/mass) if mass else (r,Q(0)))
 ck(sum(ref)==1);return tt,tuple(ref)
def core(A):return tuple(1 if a else 1-2*u for a in A for u in (0,1))
def pack(f):return {str(p):str(v) for p,v in f.items()}
def summary(f):
 if not f:return ['0','0']
 lo,hi=iv(f);d=1<<100
 return [str(Q((lo*d).numerator//(lo*d).denominator,d)),str(Q(-((-hi*d).numerator//(-hi*d).denominator),d))]
def tree(A,ref,order,depth=0,validate=False):
 # Each returned spent cost is conditional at this node; global q1 reach comes later.
 tt=core(A);cost=actcost(tt,ref)
 if len(set(A))==1:return {},cost,0,1
 j=order[0];remain=[i-int(i>j) for i in order[1:]]
 childA=[restrict(A,j,b) for b in (0,1)];r=fold(ref,j+1)
 children=[core(a) for a in childA];cc=[actcost(t,r) for t in children]
 D=add((1,cost),(-Q(1,2),cc[0]),(-Q(1,2),cc[1]));ck(nonneg(D))
 if validate:
  pp,qq=actual_act(tt,ref,literal=depth==0);ra=fold(qq,j+2)
  pcs=[actual_act(t,r) for t in children]
  ck(tuple((a+b)/2 for a,b in zip(pcs[0][0],pcs[1][0]))==fold(pp,j+2))
  gains=[add((1,ce(p,ra)),(-1,c)) for (p,q),c in zip(pcs,cc)]
  ck(all(nonneg(g) for g in gains))
  raw=add((1,cost),(-Q(1,2),ce(pcs[0][0],ra)),(-Q(1,2),ce(pcs[1][0],ra)))
  ck(nonneg(raw));ck(D==add((1,raw),(Q(1,2),gains[0]),(Q(1,2),gains[1])))
 subs=[tree(a,r,remain,depth+1,validate) for a in childA]
 spent=add((1,D),(Q(1,2),subs[0][0]),(Q(1,2),subs[1][0]))
 leaves=add((Q(1,2),subs[0][1]),(Q(1,2),subs[1][1]))
 ck(spent==add((1,cost),(-1,leaves)))
 return spent,leaves,1+sum(x[2] for x in subs),sum(x[3] for x in subs)
def fixture(A,orders,theorem=False,review=False,validate=False):
 p=Q(sum(A),len(A));tt=core(A);ps=spectrum(tt);rr=contam(ps)
 t0=tuple(1-2*(i%2) for i in range(len(tt)));p0=spectrum(t0);r0=contam(p0)
 par,qr=lift(t0,tt,r0,rr);h1,hp=entropy(ps),entropy(spectrum(par))
 I=sum(v*i.bit_count() for i,v in enumerate(ps));c=ce(ps,rr)
 bank=add((1,const(1+I)),(-Q(1,4),add((1,const(1)),(1,c))))
 ca,c0,cp=actcost(tt,rr),actcost(t0,r0),actcost(par,qr)
 tq=add((1,cp),(-Q(1,2),ca),(-Q(1,2),c0),(-1,const(p)))
 ck(nonneg(add((1,const(Q(1,2))),(-1,add((1,cp),(-1,add((1,const(1)),(Q(1,2),hp),(1,psi(p/4)))))))))
 # Above subtracts exact H(F_parent)=1+Hp/2+Psi(p/4).
 rows=[]
 for order in orders:
  spent,leaves,nodes,nleaves=tree(A,rr,order,validate=validate)
  bill=scale(Q(1,2),spent)
  ck(positive(add((1,leaves),(-1,const(3-p)))))
  remaining=add((1,bank),(-1,const(Q(1,8))),(-1,pos(tq)),(-1,bill))
  criterion=add((1,const(Q(9,16)-3*p/2)),(1,const(I-(1-p))),(-Q(1,4),h1),(-Q(1,2),hp))
  ck(positive(add((1,remaining),(-1,criterion))))
  if theorem:ck(positive(add((1,remaining),(-1,const(Q(33,128))))))
  if review:ck(positive(add((1,remaining),(-1,const(Q(1,8))))))
  rows.append({'order':order,'nodes':nodes,'leaves':nleaves,'remaining':pack(remaining),'remaining_interval':summary(remaining),'criterion':pack(criterion),'first_query_full_excess':pack(tq)})
 return rows
def run():
 start=time.perf_counter();pilot='--pilot' in sys.argv;review='--review' in sys.argv;diagnostic='--diagnostic' in sys.argv
 endpoint=add((1,const(Q(1,16))),(-1,psi(Q(1,8))),(1,const(1)),(Q(1,2),psi(Q(1,4))))
 ck(positive(endpoint));ck(63**63>2**376);ck(positive(add((1,const(1)),(1,psi(Q(1,2))),(-1,const(2)))))
 cases=[]
 if review:
  inputs=[('point'+str(k),tuple(int(i==0) for i in range(1<<k)),[list(range(k))]) for k in range(2,8)]
 elif diagnostic:
  inputs=[('diag'+str(n),tuple(int(i in (0,1,3)) for i in range(1<<n)),[list(range(n))]) for n in (2,3,4)]
 else:
  inputs=[]
  for k,overlap in ([(8,7)] if pilot else [(k,j) for k in (8,9,10) for j in (k-1,k-2)]):
   n=2*k-overlap;s0=(1<<k)-1;s1=((1<<overlap)-1)|(((1<<(k-overlap))-1)<<k)
   A=tuple(int((i&s0)==0 or (i&s1)==0) for i in range(1<<n))
   orders=[list(range(n)),list(range(overlap,n))+list(range(overlap)),list(reversed(range(n)))]
   inputs.append((f'union{k}overlap{overlap}',A,orders[:1] if pilot else orders))
  if not pilot:
   for supp in ((0,3,5),(0,3,5,170)):
    inputs.append(('arbitrary'+str(len(supp)),tuple(int(i in supp) for i in range(512)),[list(range(9)),list(reversed(range(9))),[i for i in range(9) if i%2]+[i for i in range(9) if not i%2]]))
 for name,A,orders in inputs:
  cases.append({'name':name,'p':str(Q(sum(A),len(A))),'event_bits':len(A).bit_length()-1,'trees':fixture(A,orders,theorem=not(review or diagnostic),review=review,validate=diagnostic)})
  (R/'out/CHECKPOINT.json').write_text(json.dumps({'completed':name,'assertions':ns['checks']}),encoding='utf-8')
  assert time.perf_counter()-start<60,'Frozen 60-second cap'
 if review:
  gap=add((1,cases[0]['trees'][0]['remaining'] and {int(p):Q(v) for p,v in cases[0]['trees'][0]['remaining'].items()}),(-1,const(Q(1,8))))
  den=math.lcm(*(v.denominator for v in gap.values()));ex={p:int(v*den) for p,v in gap.items()}
  lhs=math.prod(p**v for p,v in ex.items() if v>0);rhs=math.prod(p**(-v) for p,v in ex.items() if v<0);ck(lhs>rhs)
  portable={'exponents':ex,'clearing_denominator':den,'left_bits':lhs.bit_length(),'right_bits':rhs.bit_length(),'left_gt_right':lhs>rhs}
 else:portable=None
 out={'status':'PASS','cases':len(cases),'assertions':ns['checks'],'seconds':time.perf_counter()-start,'helper_normalized_sha256':hashlib.sha256(src.encode()).hexdigest(),'profile_endpoint_gap':pack(endpoint),'binary_entropy_integer_certificate':{'base':63,'exponent':63,'power_of_two':376,'left_gt_right':63**63>2**376},'review_k2_integer_certificate':portable,'details':cases,'full_fei':'OPEN'}
 name='REVIEW_CHECKS.json' if review else 'DIAGNOSTIC_CHECKS.json' if diagnostic else 'PILOT.json' if pilot else 'CHECKS.json'
 (R/'out'/name).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ('details','profile_endpoint_gap','binary_entropy_integer_certificate')}))
if __name__=='__main__':run()
