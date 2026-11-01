from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import itertools,math,json,time,sys
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();PILOT='--pilot' in sys.argv;checks=0
def ck(x):
 global checks
 checks+=1;assert x,checks
 assert time.perf_counter()-START<(60 if PILOT else 180)
def prod(xs):
 z=Q(1)
 for x in xs:z*=x
 return z
def trans(tab,ps):
 c=list(map(Q,tab));n=len(ps)
 for i,p in enumerate(ps):
  for a in range(1<<n):
   if a>>i&1:continue
   x,y=c[a],c[a|(1<<i)];c[a]=(1-p)*x+p*y;c[a|(1<<i)]=(y-x)/2
 v=[4*p*(1-p) for p in ps];vs=[prod(v[i] for i in range(n) if a>>i&1) for a in range(1<<n)]
 P=[x*x*y for x,y in zip(c,vs)]
 return c,P,vs
@lru_cache(None)
def core(x):
 z=(x-1)/(x+1);term=z;lo=Q(0)
 for j in range(24):lo+=2*term/(2*j+1);term*=z*z
 return lo,lo+2*term/(49*(1-z*z))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,k):return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
@lru_cache(None)
def ln(x):
 k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 iv=add(core(x),scale(core(Q(2)),k));den=10**24
 return Q(iv[0].numerator*den//iv[0].denominator,den),Q(-((-iv[1].numerator*den)//iv[1].denominator),den)
def enc(iv):return [str(x) for x in iv]
def logs_add(z,arg,coef):
 if arg!=1 and coef:z[arg]=z.get(arg,Q(0))+coef
 return {x:y for x,y in z.items() if y}
def logs_eval(z):
 v=(Q(0),Q(0))
 for arg,c in z.items():v=add(v,scale(ln(arg),c))
 return v
rows=[];profile_checks=0;tax_positive=0;max_diag_ratio=Q(0)
rs=[(2,2)] if PILOT else [(r,s) for r in range(1,4) for s in range(1,4) if r+s<=5]
with (ROOT/'out'/('PILOT_CASES.jsonl' if PILOT else 'CASES.jsonl')).open('w',encoding='utf-8') as f:
 for r,s in rs:
  for w in [2,3]:
   for t in range(w*r+s+2):
    for mode in range(3):
     ps=[Q(1,2)]*(r+s) if mode==0 else ([Q(1,4)]*r+[Q(3,4)]*s if mode==1 else [Q(1,4) if i%2==0 else Q(3,4) for i in range(r+s)])
     tab=[1 if w*(x&((1<<r)-1)).bit_count()+(x>>r).bit_count()>=t else -1 for x in range(1<<(r+s))]
     c,P,vs=trans(tab,ps);ck(sum(P)==1)
     tails=[trans([1 if x.bit_count()>=j else -1 for x in range(1<<r)],ps[:r]) for j in range(1,r+1)]
     tailI=[sum(u.bit_count()*m for u,m in enumerate(g[1])) for g in tails]
     tailV=[sum(g[1][1:]) for g in tails]
     profiles=[trans([1 if w*k+y.bit_count()>=t else -1 for y in range(1<<s)],ps[r:])[0] for k in range(r+1)]
     K={};B=Z=M=Q(0);Bdirect=Q(0);TVmax=Q(0)
     for T in range(1,1<<s):
      h=[p[T] for p in profiles];alpha=[(h[j]-h[j-1])/2 for j in range(1,r+1)]
      TV=sum(abs(a) for a in alpha)*2;TVmax=max(TVmax,TV);ck(TV<=2)
      hc,hP,hvs=trans([h[x.bit_count()] for x in range(1<<r)],ps[:r]);vT=vs[T<<r]
      for U in range(1,1<<r):
       amp=sum(a*g[0][U] for a,g in zip(alpha,tails));ck(amp==hc[U]==c[U|(T<<r)])
       kval=vT*sum(a*a*g[1][U] for a,g in zip(alpha,tails));K[U|(T<<r)]=kval
       m=P[U|(T<<r)];M+=m;Bdirect+=U.bit_count()*m
       if m:ck(kval>0)
      B+=vT*sum(a*a*i for a,i in zip(alpha,tailI));Z+=vT*sum(a*a*v for a,v in zip(alpha,tailV))
      # Physical edge differences identify exactly one tail at each edge.
      physical=Q(0)
      for i,p in enumerate(ps[:r]):
       others=[j for j in range(r) if j!=i]
       for y in range(1<<(r-1)):
        wt=prod(ps[j] if y>>k&1 else 1-ps[j] for k,j in enumerate(others));k=y.bit_count()
        physical+=4*p*(1-p)*wt*((h[k+1]-h[k])/2)**2
      ck(physical==sum(u.bit_count()*hP[u] for u in range(1,1<<r)))
      ck(physical==sum(a*a*i for a,i in zip(alpha,tailI)))
      profile_checks+=1
     Delta=sum((k.bit_count()-1)*m for k,m in enumerate(P) if k)
     ck(B==Bdirect);ck(Z==sum(K.values()));ck(0<=Z<=B<=Delta)
     row={'r':r,'s':s,'w':w,'t':t,'mode':mode,'M':str(M),'B_quad':str(B),'Z':str(Z),'Delta':str(Delta),'TVmax':str(TVmax)}
     if M:
      ck(Z>0);q={k:v/Z for k,v in K.items()};ck(sum(q.values())==1)
      E={};CE={};kl={}
      for k,m in enumerate(P):
       if not (k&((1<<r)-1) and k>>r and m):continue
       E=logs_add(logs_add(E,vs[k],m),m,-m)
       CE=logs_add(logs_add(CE,vs[k],m),K[k],-m)
       for arg,coef in [(m,m/M),(Z,m/M),(M,-m/M),(K[k],-m/M)]:kl=logs_add(kl,arg,coef)
      rhs=dict(CE)
      for arg,coef in [(Z,M),(M,-M)]:rhs=logs_add(rhs,arg,coef)
      for arg,coef in kl.items():rhs=logs_add(rhs,arg,-M*coef)
      ck(E==rhs)
      tax=scale(ln(Z/M),M);ck(tax[1]<=Q(3,8)*Delta or Z==M)
      row['normalizer_tax_interval']=enc(tax)
      if Z>M:tax_positive+=1
      max_diag_ratio=max(max_diag_ratio,B/Delta)
     else:ck(B==Z==0)
     f.write(json.dumps(row)+'\n');f.flush();rows.append(row)
     (ROOT/'out'/('PILOT_CHECKPOINT.json' if PILOT else 'CHECKPOINT.json')).write_text(json.dumps({'cases':len(rows),'checks':checks}))

def walsh(tab):
 z=list(tab);N=len(z);stride=1
 while stride<N:
  for start in range(0,N,2*stride):
   for j in range(stride):a,b=z[start+j],z[start+j+stride];z[start+j]=a+b;z[start+j+stride]=a-b
  stride*=2
 return [Q(a,N) for a in z]
family=[]
for rr in [1,2]:
 n=4*rr+1;g=[1 if x.bit_count()>n//2 else -1 for x in range(1<<n)];gh=walsh(g)
 F=[]
 for x in range(1<<(n+2)):
  a=x&3;y=x>>2;F.append(-1 if a==0 else (1 if a==3 else g[y]))
 fh=walsh(F);P=[a*a for a in fh];Ig=sum(k.bit_count()*a*a for k,a in enumerate(gh));D=sum((k.bit_count()-1)*p for k,p in enumerate(P) if k)
 L1=sum(abs(a) for a in gh);ck(D==Ig/2)
 M=sum(p for k,p in enumerate(P) if k&3 and k>>2);Bq=sum((k&3).bit_count()*p for k,p in enumerate(P) if k&3 and k>>2)
 ck(M==Q(1,4));ck(Bq==Q(1,2));ck(Q(3,8)<=Bq<=D)
 for T,a in enumerate(gh):
  if T:ck(fh[3|(T<<2)]==-a/2);ck(fh[1|(T<<2)]==fh[2|(T<<2)]==0)
 ck(sum(abs(a)/4 for a in gh)==L1/4)
 family.append({'r':rr,'n_light':n,'I_majority':str(Ig),'Delta':str(D),'B_abs':str(L1/4),'B_quad':'1/2','Z':'3/8','M':'1/4'})
central=[]
for rr in range(1,9):
 n=4*rr+1;k=2*rr+1
 # Independent truth-table signed level sum for coefficient at fixed k.
 numerator=sum((-1)**a*math.comb(k,a)*math.comb(n-k,b)*(1 if a+b>n//2 else -1) for a in range(k+1) for b in range(n-k+1))
 mag=abs(Q(numerator,2**n));ck(mag==Q(math.comb(2*rr,rr),2**(4*rr)))
 levelL=math.comb(n,k)*mag
 lower=Q(2**(2*rr),2*(4*rr+1)*(2*rr+1)**2)
 ck(levelL/(2*n)>=lower)
 central.append({'r':rr,'n':n,'coefficient_magnitude':str(mag),'L1_level_lower':str(levelL),'ratio_lower':str(lower)})
out={'status':'PASS','pilot':PILOT,'threshold_cases':len(rows),'profile_checks':profile_checks,'assertions':checks,'positive_normalizer_tax_cases':tax_positive,'max_Bquad_over_Delta':str(max_diag_ratio),'obstruction_family':family,'central_coefficient_certificates':central,'runtime_seconds':time.perf_counter()-START}
(ROOT/'out'/('PILOT.json' if PILOT else 'CHECK_OUTPUT.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
