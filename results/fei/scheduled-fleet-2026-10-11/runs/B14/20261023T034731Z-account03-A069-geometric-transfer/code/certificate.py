from pathlib import Path
from fractions import Fraction as R
from rational import fw, add, log, h, interval
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
 assert time.monotonic()-start<55,'frozen55s'
def spectrum(v):
 n=len(v);return [R(x*x,n*n) for x in fw(v)]
def cost(v,q):
 p=spectrum(v);ck(sum(p)==1);ck(sum(q)==1)
 ck(all(not x or q[i]>0 for i,x in enumerate(p)))
 return add(*[(-x,log(q[i])) for i,x in enumerate(p) if x])
def marginal(q,i):
 bit=1<<i
 return [q[(s&(bit-1))|((s>>(i))<<(i+1))]+q[(s&(bit-1))|((s>>(i))<<(i+1))|bit] for s in range(len(q)//2)]
def child(v,i,b):
 bit=1<<i
 return [v[(s&(bit-1))|((s>>i)<<(i+1))|(b<<i)] for s in range(len(v)//2)]
def influence(v,i):return R(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def original(m,d):
 n=1<<m;t=R(1,n*n);alpha=1-t*d;q=[];v=[]
 for s in range(4*n):
  c=s&1;u=(s>>1)&1;z=s>>2
  if z:qq=alpha*R(7,160*(n-1))*(4 if u==0 else 1)
  elif c==u==0:qq=t*d
  else:qq=alpha*(R(1,16) if c==u==1 else R(1,4))
  q.append(qq);v.append((-1 if (u if d==0 else c) else 1)*(-1 if c==0 and z==0 else 1))
 return v,q
def profile(m,d,k):
 n=1<<m;hh=1<<k;M=n//hh;rho=R(1,n);eta=R(1,M);t=rho*rho
 a=(1+3*t*d)/4;b=5*(1-t*d)/16;r=7*(1-t*d)/R(32*(n-1))
 a+=(hh-1)*r;b+=(hh-1)*r;r*=hh
 return M,eta,a,b,r
def price(M,eta,a,b,r,d):
 p0,p1=((1-eta)**2,eta*eta) if d==0 else (eta*eta,(1-eta)**2)
 return add((p0,log(1+r/a)),(p1,log(1+r/b)),(eta*eta,log((1+a/r)*(1+b/r))),(2*(M-2)*eta*eta,log(2)))
ell=log(R(5,4));u_checks=0;direct_parents=direct_children=0;boundary=[]
for m in range(1,7):
 rho=R(1,1<<m);t=rho*rho
 for d in (0,1):
  v,q=original(m,d);ck(sum(q)==1);ck(sum(spectrum(v))==1)
  C=cost(v,q);qu=marginal(q,1)
  cs=[child(v,1,b) for b in (0,1)]
  delta=add((1,C),*[(-R(1,2),cost(w,qu)) for w in cs])
  eu=add((1,delta),(-4*influence(v,1),log(2)))
  if d==0:
   ck(delta==add((2*rho-t,log(5))));ck(interval(eu)[1]<0)
  else:
   wanted=add((t,log((1+3*t)/(4*t))),(1-t,ell))
   ck(delta==wanted);ck(influence(v,1)==0);ck(interval(delta)[1]<1)
  ck(all(any(x!=w[0] for x in w) for w in cs))
  qc=marginal(q,0);cc=[child(v,0,b) for b in (0,1)]
  deltac=add((1,C),*[(-R(1,2),cost(w,qc)) for w in cc])
  if d==0:
   ec=add((1,deltac),(-4*influence(v,0),log(2)))
   ck(ec==add((1-2*rho+2*t,ell),(-2*rho,log(2))))
  u_checks+=1
  for ub,w in enumerate(cs):
   qr=qu
   for k in range(m):
    M,eta,a,b,r=profile(m,d,k)
    ck(qr==[a,b]+[r]*(2*(M-1)))
    p=spectrum(w);p0,p1=((1-eta)**2,eta*eta) if d==0 else (eta*eta,(1-eta)**2)
    ck(p==[p0,p1]+[eta*eta]*(2*(M-1)))
    ck(influence(w,1)==eta)
    qq=marginal(qr,1);kids=[child(w,1,z) for z in (0,1)]
    dc=add((1,cost(w,qr)),*[(-R(1,2),cost(kid,qq)) for kid in kids])
    ck(dc==price(M,eta,a,b,r,d));ck(interval(add((1,dc),(-4*eta,log(2))))[1]<0)
    # The signed physical identity keeps BOTH complete child costs,
    # including the constant child. It does not erase a stopped terminal.
    def totalI(tab):return sum(influence(tab,j) for j in range((len(tab)-1).bit_length()))
    ck(totalI(w)==eta+sum(totalI(kid) for kid in kids)/2)
    for kid in kids:cost(kid,qq);direct_children+=1
    if k<m-1:
     ck(influence(kids[1],1)==0)
     ck(sum(spectrum(kids[1]))==1)
    w=kids[0];qr=qq;direct_parents+=1
profiles=[]
for m in range(1,13):
 for d in (0,1):
  for k in range(m):
   M,eta,a,b,r=profile(m,d,k);L=R(8*(M-1),7);U=1+R(10*M,7)
   ck(L<=a/r<=U);ck(L<=b/r<=U)
   e=add((1,price(M,eta,a,b,r,d)),(-4*eta,log(2)))
   lo,hi=interval(e);ck(hi<0)
   profiles.append({'m':m,'d':d,'zero_prefix':k,'excess_upper':str(hi)})
for l in (1,2,3):
 M=1<<l;eta=R(1,M);L=R(8*(M-1),7);U=1+R(10*M,7)
 bound=add((1-2*eta+2*eta*eta,log(1+1/L)),(2*eta*eta,log(1+U)),(2*(M-2)*eta*eta,log(2)))
 lo,hi=interval(bound);ck(hi<4*eta);boundary.append({'residual_width':l,'Delta_upper':str(hi),'4Inf':str(4*eta)})
ck(R(53,16)+R(1,2)+R(21,16*240)<4)
ck(R(5,8)-R(3,5)-R(1,512)==R(59,2560))
ck(5**10>8*4**10);ck(25<32)
old=RUN.parent/'20261022T224704Z-account03-A069-geometric-transfer/out/CERTIFICATE.json'
receipt=json.loads(old.read_text(encoding='utf-8'));plo=R(receipt['positive_core_excess_interval'][0])
margin=add((1,{2:plo-R(5,8)}),(R(511,512),ell));ck(interval(margin)[0]>R(3,16))
# Concrete obstruction to a second unselected private query: m2, d0,
# after first private outcome1, inherited full cost remains positive.
M,eta,a,b,r=profile(2,0,1)
irrelevant=log(1+r/a);ilo,ihi=interval(irrelevant)
ck(ilo>R(1,2));ck(R(511,1024)*ilo>R(59,2560))
ck(plo+R(511,1024)*ilo>R(5,8))
# Independent normalized-real guard, including direct squared norms.
real_fixtures=0
for m in (1,2):
 N=1<<m;tab=[]
 for x in range(8*N):
  c=x&1;u=(x>>1)&1;z=(x>>2)&(N-1);y=1 if x>>(m+2) else -1
  aa=R(3+4*y,5);bb=R(1)
  tab.append([aa,bb,-bb,-aa][c+2*u]*(-1 if c==0 and z==0 else 1))
 P=spectrum(tab);ck(sum(P)==1)
 ck(sum(p for s,p in enumerate(P) if s&((1<<(m+2))-1)==0)==R(1,5*N*N))
 norms=[sum(x*x for x in child(tab,m+2,b))/len(child(tab,m+2,b)) for b in (0,1)]
 ck(norms==[R(13,25),R(37,25)]);real_fixtures+=2
ck(len(profiles)==156);ck(direct_parents==84);ck(direct_children==168);ck(u_checks==12)
out={'status':'PASS','assertions':checks,'compressed_spine_profiles':len(profiles),'direct_parent_profiles':direct_parents,'direct_child_profiles':direct_children,'review_terminal_profiles':u_checks,'real_fixtures':real_fixtures,'small_residual_width_certificates':boundary,'all_residual_width_ge4_coefficient':str(R(53,16)+R(1,2)+R(21,16*240)),'original_bank':'5/8','old_reserved_spend':'3/5+1/512','new_private_positive_spend':'0','same_residual':'>59/2560','second_irrelevant_query_m2_d0_lower':str(ilo),'c_obstruction_margin_lower':str(interval(margin)[0]),'elapsed_seconds':time.monotonic()-start,'spec_sha256':hashlib.sha256((RUN/'FROZEN_CERTIFICATE_SPEC.json').read_bytes()).hexdigest()}
(RUN/'out/CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
(RUN/'out/PROFILES.json').write_text(json.dumps(profiles,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['small_residual_width_certificates','second_irrelevant_query_m2_d0_lower','c_obstruction_margin_lower']}))
