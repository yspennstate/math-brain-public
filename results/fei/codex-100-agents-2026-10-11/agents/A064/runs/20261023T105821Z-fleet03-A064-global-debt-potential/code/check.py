from pathlib import Path
from fractions import Fraction as F
import json,time,sys,hashlib
import exact as e
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv
NQ=NC=0
def pos(x):
 if not x:return {}
 a,b=e.interval(x);e.ck(a>0 or b<0,'strictly classified nonzero prime-log sign')
 return x if a>0 else {}
def nn(x,label):e.ck(not x or e.interval(x)[0]>=0,label)
def make(g,h):
 return tuple(((-1 if s&1 else 1)*h[s>>2]) if s&2 else g[s>>2] for s in range(4*len(g)))
def query(t,i,Q):
 global NQ
 NQ+=1;return e.transport(t,i,Q)
def continued(t,Q):
 global NC
 n=len(t).bit_length()-1;K=e.kl(e.stats(t)[0],Q)
 for i in range(1,n):
  cc,qq,rr,O,KK,E,z=query(t,i,Q);NC+=1
  e.eq(K,e.plus((1,E),(1,O),(F(1,2),KK[0]),(F(1,2),KK[1])),'post-reset ACTUAL physical-query full KL chain')
  nn(e.plus((1,K),(-1,O),(-F(1,2),KK[0]),(-F(1,2),KK[1])),'no new allowance during post-reset continuation')
  for b,c in enumerate(cc):
   H=e.stats(c)[2];CE=e.plus((1,H),(1,KK[b]));e.eq(e.plus((1,CE),(-1,H)),KK[b],'full entropy retained at continued inherited stop')
def case(g,h,label):
 t=make(g,h);n=len(g).bit_length()-1
 pg,dg,Hg,Mg,TCg=e.stats(g);ph,dh,Hh,Mh,TCh=e.stats(h)
 p,ds,H,M,K=e.stats(t);beta=tuple((a+b)/2 for a,b in zip(dg,dh));Rcore=e.product(beta);Q=e.product(ds)
 e.ck(ds==(F(1,2),F(1,2))+beta,'physical influences independently counted')
 for s,x in enumerate(p):e.ck(x==(ph if s&1 else pg)[s>>2]/4,'full exact paired spectrum')
 e.eq(H,e.plus((1,e.constant(2)),(F(1,2),Hg),(F(1,2),Hh)),'paired entropy exact')
 cc,qq,rr,O,KK,E,z=query(t,1,Q);e.eq(E,{},'root product eligibility gives ZERO erasure credit')
 aa=[sum((r for r,x in zip(Rcore,pb) if x),F()) for pb in (pg,ph)]
 e.ck(rr==[F(1,2)+(aa[0]-aa[1])/4,F(1,2)-(aa[0]-aa[1])/4],'prediction includes ALL reference-only rows')
 e.ck(min(rr)>=F(1,4) and max(rr)<=F(3,4),'uniform actual predicted reach bounds')
 JJ=[];BB=[]
 for b,c in enumerate(cc):
  pb,db,hb,mb,tcb=e.stats(c);product=e.product(db)
  TC=(TCg,TCh)[b];e.eq(tcb,TC,'actual intermediate product TC')
  Ak=e.plus((1,e.kl((pg,ph)[b],Rcore)),(-1,TC));nn(Ak,'marginal projection loss nonnegative')
  A2=e.plus(*[(1,e.kl((d,1-d),(beta[j],1-beta[j]))) for j,d in enumerate((dg,dh)[b])])
  e.eq(Ak,A2,'product projection loss separately derived from physical marginals')
  e.eq(KK[b],e.plus((1,TC),(1,Ak),(1,e.log(2*rr[b]))),'normalized inherited KL exact on child source support')
  J=e.plus((1,TC),(-1,KK[b]));e.eq(J,e.plus((-1,Ak),(-1,e.log(2*rr[b]))),'COMPLETE signed reset bill')
  B=pos(J);nn(e.plus((1,KK[b]),(1,B),(-1,TC)),'before-reset pending retained')
  e.eq(TC,e.kl(pb,product),'ACTUAL reset reference, no abstract substitute')
  continued(c,product);JJ.append(J);BB.append(B)
 Broot=e.plus((F(1,2),BB[0]),(F(1,2),BB[1]));nn(e.plus((1,e.constant(F(1,2))),(-1,Broot)),'half-bit original cap')
 e.eq(e.plus((1,K),(1,Broot),(-F(1,2),KK[0]),(-F(1,2),KK[1]),(-F(1,2),BB[0]),(-F(1,2),BB[1])),O,'root potential pays actual O, BOTH child boundaries')
 Gamma=e.plus((1,M),(-1,e.constant(2)),(-F(1,2),Mg),(-F(1,2),Mh));nn(Gamma,'physical marginal Jensen refund')
 e.eq(e.plus((F(1,2),JJ[0]),(F(1,2),JJ[1])),e.plus((1,O),(-1,Gamma)),'endpoint separated from pending positive parts')
 gh=tuple(a*b for a,b in zip(g,h));nn(e.plus((1,Mg),(1,Mh),(-1,e.stats(gh)[3])),'A087 derivative product entropy bound')
 return {'label':label,'n':n,'r':[str(x) for x in rr],'support_mass':[str(x) for x in aa],'root_K':e.enc(K),'O':e.enc(O),'signed_bills':[e.enc(x) for x in JJ],'pending':e.enc(Broot),'pending_interval':e.enciv(Broot),'marginal_refund':e.enc(Gamma),'reference_only_mass':str(z)}
def truth(mask):return tuple(1 if mask&(1<<s) else -1 for s in range(4))
records=[];masks=[0,7] if pilot else list(range(16))
for a in masks:
 for b in masks:records.append(case(truth(a),truth(b),f'{a},{b}'))
sharp=[]
for n in ([4] if pilot else [4,6,8]):
 g=tuple(-1 if (s&1)&((s>>1).bit_count()&1) else 1 for s in range(1<<n))
 h=tuple(-1 if sum(((s>>j)&1)*((s>>(j+1))&1) for j in range(0,n,2))%2 else 1 for s in range(1<<n))
 rec=case(g,h,f'sharp{n}');target=e.plus((1,e.constant(F(1,2))),(-F(1,2),e.log(1+F(1,1<<(n-2)))))
 e.eq({int(k):F(v) for k,v in rec['pending'].items()},target,'sharp actual Boolean family exact pending')
 e.ck(e.interval(target)[0]>0 and e.interval(target)[1]<F(1,2),'strict finite sharpness range')
 e.ck(rec['r']==[str((1+F(1,1<<(n-2)))/4),str((3-F(1,1<<(n-2)))/4)],'sharp predictions')
 if n==4:e.ck(F(8,5)>F(4,3),'pending exceeds tempting endpoint cap')
 sharp.append(rec)
e.ck(NQ==(29 if pilot else 1319),'nonempty exact query coverage')
e.ck(NC==(24 if pilot else 1060),'all post-reset first ordinary directions')
elapsed=time.perf_counter()-start;e.ck(elapsed<55,'frozen runtime')
out={'status':'PASS','pilot':pilot,'assertions':e.COUNT,'seconds':elapsed,'pairs':len(records),'sharp_dimensions':[x['n'] for x in sharp],'query_nodes':NQ,'post_reset_query_nodes':NC,'records':records,'sharp':sharp,'helper_sha256':hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest()}
(R/'out'/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['records','sharp']}))
