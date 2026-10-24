import hashlib,json,sys,time
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261014T055119Z-account05-A019-orthogonality-extensions/code/check_exposure.py'
src=OLD.read_text(encoding='utf-8');ns={'Q':Q,'lru_cache':lru_cache,'checks':0}
exec(src[src.index('def ck(x):'):src.index("transport={'positive'")],ns)
direct='--direct' in sys.argv;pilot='--pilot' in sys.argv
if direct:
 def slow(tt):return tuple(Q(sum(z*(-1 if (i&j).bit_count()%2 else 1) for j,z in enumerate(tt)),len(tt)) for i in range(len(tt)))
 ns['fw']=slow
ck,sp,ce,add,psi,nn,lf=[ns[x] for x in ('ck','spectrum','ce','add','psi','nonnegative','logform')]
def cst(x):return {2:Q(x)} if x else {}
def kl(p,q):return add((1,ce(p,q)),(-1,ce(p,p)))
def contam(p):return tuple((x+int(i==0))/2 for i,x in enumerate(p))
def fold(a,j):
 n=len(a)//2;out=[]
 for i in range(n):
  z=(i&((1<<j)-1))|((i>>j)<<(j+1));out.append(a[z]+a[z|(1<<j)])
 return tuple(out)
def restrict(h,j,b):
 return tuple(h[(i&((1<<j)-1))|((i>>j)<<(j+1))|(b<<j)] for i in range(len(h)//2))
def corelift(a,b,qa,qb):
 h=tuple(v for pair in zip(a,b) for v in pair);p=sp(h);q=[]
 for i in range(len(a)):
  mass=p[2*i]+p[2*i+1];qr=(qa[i]+qb[i])/2
  q.extend((qr*p[2*i]/mass,qr*p[2*i+1]/mass) if mass else (qr,Q(0)))
 ck(sum(q)==1);return h,tuple(q)
def activate(h,q):
 tt=tuple(1 if x==0 else h[y]*(-1 if z==0 else 1) for z in range(4) for y in range(len(h)) for x in range(2))
 p=sp(tt);ref=[]
 for j in range(4*len(h)):
  qr=(q[j%len(h)]/4+int(j==0))/2;mass=p[2*j]+p[2*j+1]
  ref.extend((qr*p[2*j]/mass,qr*p[2*j+1]/mass) if mass else (qr,Q(0)))
 ck(sum(ref)==1);ck(sum(p)==1)
 return tt,p,tuple(ref),ce(p,ref)
def pos(form):return form if nn(form) else {}
def strict_gt(f):return bool(f) and ns['interval'](f)[0]>0
start=time.monotonic();rows=[]
curv=add((1,psi(Q(1,8))),(-1,cst(1)),(-Q(1,2),psi(Q(1,4))))
ck(strict_gt(add((1,cst(Q(1,16))),(-1,curv))))
# Also independently bounds the source's first profile term.
firstcurv=add((1,psi(Q(1,16))),(-1,cst(1)),(-Q(1,2),psi(Q(1,8))))
ck(strict_gt(add((1,cst(Q(1,32))),(-1,firstcurv))))
for k in ([2] if pilot else [2,3] if direct else range(1,9)):
 e=Q(1,1<<k)
 a=tuple(1-2*u for v in range(1<<k) for u in range(2))
 b=tuple(1 if v==0 else 1-2*u for v in range(1<<k) for u in range(2))
 pa,pb=sp(a),sp(b);qa,qb=contam(pa),contam(pb)
 h,qh=corelift(a,b,qa,qb);rt=activate(h,qh);ch0=activate(a,qa);ch1=activate(b,qb)
 I0=sum(p*i.bit_count() for i,p in enumerate(pa));I1=sum(p*i.bit_count() for i,p in enumerate(pb))
 B=add((I0+I1,cst(1)),(-Q(1,4),ce(pa,qa)),(-Q(1,4),ce(pb,qb)))
 # B=(4I0-c0+4I1-c1)/4.
 tq=add((1,rt[3]),(-Q(1,2),ch0[3]),(-Q(1,2),ch1[3]),(-e,cst(1)))
 before=add((1,B),(-Q(1,8),cst(1)),(-1,pos(tq)))
 rc=fold(qb,1);ra=fold(ch1[2],2)
 corechildren=[restrict(b,1,v) for v in (0,1)]
 children=[activate(z,rc) for z in corechildren]
 for z in corechildren:
  pz=sp(z);ck(all(q>=p/4 for p,q in zip(pz,rc)))
 # Literal child spectra of the parent activation agree with independently built activations.
 for v,child in enumerate(children):
  literal=restrict(ch1[0],2,v);ck(literal==child[0])
  ck(sp(literal)==child[1])
  ck(fold(ra,0)==fold(child[2],0))
 raw=add((1,ch1[3]),(-Q(1,2),ce(children[0][1],ra)),(-Q(1,2),ce(children[1][1],ra)))
 gains=[add((1,ce(c[1],ra)),(-1,c[3])) for c in children]
 ck(all(nn(x) for x in gains))
 tv=add((1,ch1[3]),(-Q(1,2),children[0][3]),(-Q(1,2),children[1][3]))
 ck(tv==add((1,raw),(Q(1,2),gains[0]),(Q(1,2),gains[1])))
 dh=add((1,ce(ch1[1],ch1[1])),(-Q(1,2),ce(children[0][1],children[0][1])),(-Q(1,2),ce(children[1][1],children[1][1])))
 kp=kl(ch1[1],ch1[2]);kcs=[kl(c[1],c[2]) for c in children]
 ck(tv==add((1,dh),(1,kp),(-Q(1,2),kcs[0]),(-Q(1,2),kcs[1])))
 ck(nn(add((1,cst(Q(1,2))),(-1,kp))))
 ck(Q(sum(ch1[0][i]!=ch1[0][i^4] for i in range(len(ch1[0]))),len(ch1[0]))==e/2)
 after=add((1,before),(-Q(1,2),pos(tv)))
 if k>=2:
  ck(strict_gt(add((1,B),(-1,cst(1)))))
  ck(strict_gt(add((1,cst(Q(1,4))),(-1,tq))))
  ck(strict_gt(add((1,before),(-1,cst(Q(5,8))))))
  ck(strict_gt(add((1,cst(Q(45,64))),(-1,dh))))
  ck(strict_gt(add((1,cst(Q(77,64))),(-1,tv))))
  ck(strict_gt(add((1,after),(-1,cst(Q(3,128))))))
 # q0 dummy data query is exact in true and inherited references.
 ck(all(not p for i,p in enumerate(ch0[1]) if i&4));ck(all(not q for i,q in enumerate(ch0[2]) if i&4))
 row={'k':k,'B':{str(p):str(v) for p,v in B.items()},'Tq':{str(p):str(v) for p,v in tq.items()},'Tv':{str(p):str(v) for p,v in tv.items()},'conversion_gains':[{str(p):str(v) for p,v in x.items()} for x in gains],'remaining_after_old_U_and_full_both_queries':{str(p):str(v) for p,v in after.items()},'boundary_outside_uniform_theorem':k==1}
 rows.append(row)
 (R/'out/PARTIAL.json').write_text(json.dumps({'completed_k':k,'checks':ns['checks']},indent=2),encoding='utf-8')
 assert time.monotonic()-start<60
out={'status':'PASS','cases':len(rows),'checks':ns['checks'],'seconds':time.monotonic()-start,'mode':'direct character summation' if direct else 'integer Walsh/Fraction','source_arithmetic_normalized_sha256':hashlib.sha256(src.encode()).hexdigest(),'curvature_endpoint_prime_log':{str(p):str(v) for p,v in curv.items()},'curvature_upper_gap_interval':[str(x) for x in ns['interval'](add((1,cst(Q(1,16))),(-1,curv)))],'rows':rows,'full_fei':'OPEN'}
name='PILOT.json' if pilot else 'DIRECT_CERTIFICATE.json' if direct else 'CERTIFICATE.json'
(R/'out'/name).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('rows','curvature_upper_gap_interval','curvature_endpoint_prime_log')}))
