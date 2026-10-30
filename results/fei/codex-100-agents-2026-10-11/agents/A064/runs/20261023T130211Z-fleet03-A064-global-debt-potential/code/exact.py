from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,sys,time,hashlib
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0
def ck(x,label=''):
 global COUNT
 COUNT+=1
 if not x:raise AssertionError(label)
def plus(*es):
 z={}
 for c,e in es:
  for p,x in e.items():z[p]=z.get(p,F())+c*x
 return {p:x for p,x in z.items() if x}
@lru_cache(None)
def factors(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def log(q):
 ck(q>0,'log domain')
 return plus((1,{p:F(x) for p,x in factors(q.numerator).items()}),(-1,{p:F(x) for p,x in factors(q.denominator).items()}))
def constant(c):return {2:F(c)} if c else {}
def ent(p):return plus(*[(-x,log(x)) for x in p if x])
def kl(p,q):
 ck(sum(p)==sum(q)==1,'normalized KL laws')
 for x,y in zip(p,q):ck(not x or y>0,'source support retained')
 return plus(*[(x,log(x/y)) for x,y in zip(p,q) if x])
def eq(a,b,label=''):ck(not plus((1,a),(-1,b)),label)
GRID=1<<96
def rnd(a,b):return F((a*GRID).__floor__(),GRID),F((b*GRID).__ceil__(),GRID)
def ln(q):
 z=(q-1)/(q+1);ck(0<=z<=F(1,3));s=F();p=z
 for j in range(32):s+=p/F(2*j+1);p*=z*z
 return rnd(2*s,2*s+2*p/(65*(1-z*z)))
L2=ln(F(2))
@lru_cache(None)
def lprime(p):
 e=p.bit_length()-1;a,b=ln(F(p,1<<e))
 return rnd(e+a/L2[1],e+b/L2[0])
def interval(e):
 lo=hi=F()
 for p,c in e.items():
  a,b=lprime(p);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
 return lo,hi
def enc(e):return {str(p):str(c) for p,c in sorted(e.items())}
def enciv(e):return [str(x) for x in interval(e)]
def insert(s,i,b):return (s&((1<<i)-1))|((s>>i)<<(i+1))|(b<<i)
def child(t,i,b):return tuple(t[insert(s,i,b)] for s in range(len(t)//2))
@lru_cache(None)
def stats(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):u,v=a[k],a[k+h];a[k],a[k+h]=u+v,u-v
  h*=2
 p=tuple(F(x*x,len(t)**2) for x in a);n=len(t).bit_length()-1
 ck(sum(p)==1,'Parseval')
 ds=tuple(sum((x for s,x in enumerate(p) if s&(1<<i)),F()) for i in range(n))
 for i,d in enumerate(ds):ck(d==F(sum(t[s]!=t[s^(1<<i)] for s in range(len(t))),len(t)),'physical edges independently')
 H=ent(p);M=plus(*[(1,ent((d,1-d))) for d in ds]);TC=plus((1,M),(-1,H))
 return p,ds,H,M,TC
def product(ds):
 out=[]
 for s in range(1<<len(ds)):
  q=F(1)
  for i,d in enumerate(ds):q*=d if s&(1<<i) else 1-d
  out.append(q)
 return out
def transport(t,i,Q):
 p=stats(t)[0];cs=[child(t,i,b) for b in (0,1)];pc=[stats(c)[0] for c in cs]
 qs=[[F() for _ in range(len(p)//2)] for b in (0,1)];ref=F();reach=[F(),F()]
 pe=[];qe=[]
 for s in range(len(p)//2):
  pp=p[insert(s,i,0)]+p[insert(s,i,1)];qq=Q[insert(s,i,0)]+Q[insert(s,i,1)];pe.append(pp);qe.append(qq)
  if not pp:ref+=qq
  kk=[pc[b][s]/(2*pp) if pp else F(1,2) for b in (0,1)]
  ck(sum(kk)==1,'kernel including every zero-source row')
  for b in (0,1):qs[b][s]=qq*kk[b];reach[b]+=qs[b][s]
 ck(sum(reach)==1 and min(reach)>0,'positive predicted normalization')
 qs=[[x/reach[b] for x in qs[b]] for b in (0,1)]
 O=kl((F(1,2),F(1,2)),reach);K=kl(p,Q);Ks=[kl(pc[b],qs[b]) for b in (0,1)];E=plus((1,K),(-1,kl(pe,qe)))
 eq(K,plus((1,E),(1,O),(F(1,2),Ks[0]),(F(1,2),Ks[1])),'exact prime-log normalized chain')
 return cs,qs,reach,O,Ks,E,ref
def mul(a,b,l):
 poly={2:0b111,3:0b1011}[l];z=0
 while b:
  if b&1:z^=a
  b>>=1;a<<=1
  if a&(1<<l):a^=poly
 return z
def core(l):
 q=1<<l
 return tuple((-1 if (s&(q-1))&1 else 1)*(-1 if (s>>(2*l))==mul(s&(q-1),(s>>l)&(q-1),l) else 1) for s in range(q**3))
def carrier(g):
 return tuple((-1 if ((z&1)^((z>>1)&1)^((z>>2).bit_count()&1))&((z>>1)&1) else 1)*g[z>>2] for z in range(4*len(g)))
def fieldcase(l):
 h=core(l);m=3*l;G=carrier((1,)*len(h));H=carrier(h)
 t=tuple((G if not s&1 else H)[s>>1] for s in range(2*len(G)))
 ph,dh,Hh,Mh,_=stats(h);pp,dd,HH,MM,Kroot=stats(t)
 q=1<<l;ck(ph[0]==0,'balanced field core')
 masses={}
 for x in ph:
  if x:masses[x]=masses.get(x,0)+1
 ck(masses=={F((q-2)**2,q*q):1,F(4,q**4):(q-1)*q*q},'full all-atom core Walsh spectrum')
 pc=F(2,q)-F(2,q*q);dx=F(2,q)
 for i,d in enumerate(dh):
  if i<l:ck(d==(1-pc if i==0 else pc),'a physical direction with chosen psi')
  elif i<2*l:ck(d==pc,'b marginal')
  else:ck(d==dx,'x marginal')
 eq(Mh,plus((2*l,ent((pc,1-pc))),(l,ent((dx,1-dx)))),'all-l marginal-entropy formula')
 ck(all(d==F(1,2) for d in dd),'all root influences half')
 eq(Kroot,plus((1,constant(m-1)),(-F(1,2),Hh)))
 Q=[F(1,len(t))]*len(t)
 cs,qs,reach,O,Ks,E,ref=transport(t,0,Q)
 ck(reach==[F(1,2*q),1-F(1,2*q)],'fair-extension corrected root prediction')
 eq(E,{},'zero root erasure credit')
 eq(Ks[0],constant(2*l-1),'inherited G KL')
 eq(Ks[1],plus((1,constant(m)),(-1,Hh),(1,log(reach[1]))),'inherited H KL')
 for c in cs:ck(all(d==F(1,2) for d in stats(c)[1]),'all child influences half')
 leaves=[];terminalTC=[];terminalH=[];terminalCE=[];signed=[];refonly=[];secondO=[]
 for b,c in enumerate(cs):
  # Remaining labels after selector: u=0,v=1, core bits>=2.
  ccs,cqs,rr,oo,kks,ee,z=transport(c,1,qs[b]);ck(rr==[F(1,2),F(1,2)],'INHERITED Bayes carrier query fair')
  eq(oo,{},'no carrier outcome cost');secondO.append(oo);refonly.append(str(z))
  this=[]
  for cc in ccs:
   p,ds,hh,mm,tc=stats(cc);R=product(ds);eq(tc,kl(p,R),'actual full terminal product KL')
   eq(hh,Hh if b else {},'full terminal entropy, not erased')
   eq(tc,plus((1,Mh),(-1,Hh)) if b else {},'full terminal TC')
   terminalH.append(hh);terminalTC.append(tc);terminalCE.append(mm);leaves.append(cc);this.append(tc)
  signed.append(plus((F(1,2),this[0]),(F(1,2),this[1]),(-1,Ks[b])))
 eq(signed[0],constant(-(2*l-1)),'G deferred reset credit')
 delta=plus((1,Mh),(-1,constant(m)),(-1,log(reach[1])))
 eq(signed[1],delta,'H intermediate-stop booking')
 if l==2:
  eq(Hh,constant(5));ck(interval(delta)[0]>0,'exception is actually positive');ck(interval(delta)[1]<F(1,64),'exception rigorous upper')
  W=plus((F(1,2),delta))
 else:ck(interval(delta)[1]<0,'all-l proof sign checked at3');W={}
 S=plus((1,constant(2*m+2)),(-F(1,2),Hh))
 ck(interval(plus((F(1,1472),S),(-1,W)))[0]>0,'new booking below1/1472 ORIGINAL owner')
 residual=plus((F(3,4),S),(-1,W));ck(interval(plus((1,residual),(-F(1103,1472),S)))[0]>0,'retain old quarter booking in same owner')
 net=plus((1,O),(F(1,4),terminalTC[0]),(F(1,4),terminalTC[1]),(F(1,4),terminalTC[2]),(F(1,4),terminalTC[3]),(-1,Kroot))
 ck(interval(plus((1,constant(1-l)),(-1,net)))[0]>0,'strict negative ENDPOINT kept separate from intermediate booking')
 # Root potential and each child-to-terminal inequality, in exact expressions.
 bks=[{},delta if l==2 else {}];P0=plus((1,Kroot),(1,W));P1=[plus((1,Ks[b]),(1,bks[b])) for b in (0,1)]
 eq(plus((1,P0),(-F(1,2),P1[0]),(-F(1,2),P1[1])),O,'root potential drift')
 for b in (0,1):
  gap=plus((1,P1[b]),(-F(1,2),terminalTC[2*b]),(-F(1,2),terminalTC[2*b+1]));ck(not gap or interval(gap)[0]>=0,'intermediate current KL plus booked future reset retained')
 return {'l':l,'m':m,'parent_dimension':m+3,'root_reach':[str(x) for x in reach],'root_reference_only_mass':str(ref),'second_reference_only_masses':refonly,'root_TC':enc(Kroot),'inherited_child_KL':[enc(k) for k in Ks],'carrier_outcome_KL':[enc(k) for k in secondO],'pending_H_booking_signed':enc(delta),'new_expected_booking':enc(W),'new_booking_interval':enciv(W),'original_owner':enc(S),'remaining_after_OLD_QUARTER':enc(residual),'final_mean_H':enc(plus(*[(F(1,4),x) for x in terminalH])),'final_mean_TC':enc(plus(*[(F(1,4),x) for x in terminalTC])),'final_mean_CE':enc(plus(*[(F(1,4),x) for x in terminalCE])),'net_endpoint_debit':enc(net)}
def general(mask):
 g=tuple(1 if mask&(1<<s) else -1 for s in range(4));t=carrier(g);R=[F(x,11) for x in (1,2,3,5)]
 Q=[]
 for s in range(16):
  su=s&1;oldcore=(s>>2)^(3 if su else 0);Q.append(R[oldcore]/4)
 _,_,rr,oo,_,_,ref=transport(t,1,Q);ck(rr==[F(1,2),F(1,2)],'nonproduct nonmatching lifted reference');eq(oo,{})
 p,ds,hh,mm,tc=stats(t);qq=product(ds);cs,_,rr,oo,_,_,_=transport(t,1,qq)
 D=plus((1,oo),(F(1,2),stats(cs[0])[4]),(F(1,2),stats(cs[1])[4]),(-1,tc))
 eq(D,plus((1,stats(g)[3]),(-1,constant(2))),'general product reset exact refund')
 return {'mask':mask,'reference_only_mass':str(ref),'product_debit':enc(D)}
def main():
 mode=sys.argv[1];ls=[2] if mode=='pilot' else [2,3];ms=[0,7] if mode=='pilot' else list(range(16))
 ck(2**22>3**3*5**5*7**2,'positive delta power certificate')
 ck(2**703<3**96*5**160*7**64,'delta<1/64 power certificate')
 ck(3**12>2**19,'h2(1/4)<13/16 power certificate')
 records=[fieldcase(l) for l in ls];gens=[general(m) for m in ms]
 ck(time.perf_counter()-START<55,'frozen runtime')
 result={'status':'PASS','mode':mode,'field_widths':ls,'general_core_masks':ms,'exact_assertions':COUNT,'seconds':time.perf_counter()-START,'field_records':records,'carrier_records':gens,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (ROOT/'out').mkdir(exist_ok=True);(ROOT/'out'/f'{mode.upper()}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['field_records','carrier_records']}))
if __name__=='__main__':main()
