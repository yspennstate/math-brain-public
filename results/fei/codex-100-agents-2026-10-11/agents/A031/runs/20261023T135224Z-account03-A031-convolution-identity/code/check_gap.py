from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,sys,time,hashlib
R=Path(__file__).resolve().parent.parent
checks=0
def ck(v,msg='check'):
 global checks
 checks+=1
 if not v: raise AssertionError(msg)
def fw(v):
 a=list(map(F,v));k=1
 while k<len(a):
  for s in range(0,len(a),2*k):
   for j in range(k):u,w=a[s+j],a[s+j+k];a[s+j],a[s+j+k]=u+w,u-w
  k*=2
 return [x/len(a) for x in a]
@lru_cache(None)
def factor(n):
 out={};d=2
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,F(0))+1;n//=d
  d+=1
 if n>1:out[n]=out.get(n,F(0))+1
 return out
def addlog(out,c,x):
 if not c:return
 ck(x>0,'positive log')
 for n,sgn in [(x.numerator,1),(x.denominator,-1)]:
  for p,e in factor(n).items():out[p]=out.get(p,F(0))+c*sgn*e
def clean(d):return {p:c for p,c in d.items() if c}
def kl(p,q):
 d={}
 for a,b in zip(p,q):
  if a:addlog(d,a,a/b)
 return clean(d)
def combine(*parts):
 d={}
 for c,part in parts:
  for p,v in part.items():d[p]=d.get(p,F(0))+c*v
 return clean(d)
def rawln(x):
 w=(x-1)/(x+1);power=w;s=F(0)
 for k in range(40):s+=2*power/(2*k+1);power*=w*w
 tail=2*abs(power)/(81*(1-w*w))
 return s-tail,s+tail
LN2=rawln(F(2))
@lru_cache(None)
def lnprime(p):
 k=p.bit_length()-1;lo,hi=rawln(F(p,1<<k))
 return lo+k*LN2[0],hi+k*LN2[1]
def interval(d):
 lo=hi=F(0)
 for p,c in d.items():
  l,h=lnprime(p)
  if c<0:l,h=h,l
  lo+=c*l;hi+=c*h
 return lo,hi
def partitions(n):
 def go(a):
  if len(a)==n:yield [[i for i,z in enumerate(a) if z==k] for k in range(max(a)+1)];return
  for z in range(max(a)+2):yield from go(a+[z])
 yield from go([0])
def profile(v,bs):return [sum((v[i] for i in b),F(0)) for b in bs]
def invoice(p,m,bs,r):
 a=[profile(v,bs) for v in p];phi=F(0);criterion=True;detail=[]
 for z,b in enumerate(bs):
  occ=[t for t in [0,1] if a[t][z]]
  if len(occ)==2:
   e=[sum(r[t][z]*p[t][i]/a[t][z] for t in [0,1])-2*m[i] for i in b]
   w=sum(r[t][z]**2/a[t][z] for t in [0,1]);term=sum(abs(x) for x in e)**2/(4*w)
   criterion &=all(x==0 for x in e)
  elif occ:
   t=occ[0];o=sum(max(F(0),r[t][z]*p[t][i]/a[t][z]-2*m[i]) for i in b)
   term=a[t][z]*o*o/r[t][z]**2;criterion &=o==0
  else:term=F(0)
  phi+=term;detail.append(term)
 ck((phi==0)==criterion,'quantitative iff fine criterion')
 return phi,a,combine((F(1,2),kl(a[0],r[0])),(F(1,2),kl(a[1],r[1])))
def verify(p,m,bs,r,refs):
 phi,a,L=invoice(p,m,bs,r)
 for q in refs:
  ck(all(sum(v)==1 and all(x>=0 for x in v) for v in q),'normalized refs')
  ck(all(q[0][i]+q[1][i]==2*m[i] for i in range(4)),'full mean')
  ck([profile(v,bs) for v in q]==r,'profiles')
  M=combine((F(1,2),kl(p[0],q[0])),(F(1,2),kl(p[1],q[1])))
  gap=combine((1,M),(-1,L));lo,hi=interval(gap)
  ck(lo>=phi or (not gap and phi==0),'quantitative fine bound')
 return phi
def main():
 start=time.monotonic();pilot='--pilot' in sys.argv;count=16 if pilot else 256
 bslist=list(partitions(4));ck(len(bslist)==15)
 cases=strict=single=0;witness=[]
 for table in range(count):
  vals=[1 if table>>i&1 else-1 for i in range(8)];ar=fw(vals)
  for U in range(8):ck(sum(ar[S]*ar[S^U] for S in range(8))==int(U==0),'full signed convolution')
  p=[]
  for u in [0,1]:
   ac=fw([vals[(y<<1)|u] for y in range(4)])
   ck(all(ac[t]==ar[t<<1]+(-1)**u*ar[(t<<1)|1] for t in range(4)),'signed physical child')
   p.append([x*x for x in ac])
  mid=[(p[0][i]+p[1][i])/2 for i in range(4)]
  means=[[F(1,4)]*4,[(x+F(1,4))/2 for x in mid]]
  for m in means:
   for bs in bslist:
    for template in [0,1]:
     delta=min(m[0],m[1])/2 if template else F(0)
     q0=[[m[i]+sgn*(delta if i==0 else -delta if i==1 else 0) for i in range(4)] for sgn in [1,-1]]
     r=[profile(v,bs) for v in q0]
     prop=[[F(0)]*4 for _ in range(2)]
     for t in [0,1]:
      for z,b in enumerate(bs):
       for i in b:prop[t][i]=r[t][z]*m[i]/sum(m[j] for j in b)
     phi=verify(p,m,bs,r,[q0,prop]);strict+=phi>0;cases+=1
     ck(time.monotonic()-start<(55 if pilot else 180),'frozen runtime')
 # Independently stated review witness checks, full references retained.
 p=[[F(1,4)]*4,[F(0),F(1),F(0),F(0)]];bs=[[0,1],[2,3]]
 for name,m,q in [
  ('A033',[F(1,8),F(5,8),F(1,8),F(1,8)],[[F(1,4),F(1,2),F(1,8),F(1,8)],[0,F(3,4),F(1,8),F(1,8)]]),
  ('A035',[F(1,4)]*4,[[F(5,12),F(1,12),F(1,4),F(1,4)],[F(1,12),F(5,12),F(1,4),F(1,4)]])]:
  q=[list(map(F,v)) for v in q];r=[profile(v,bs) for v in q];phi=verify(p,m,bs,r,[q]);M=combine((F(1,2),kl(p[0],q[0])),(F(1,2),kl(p[1],q[1])))
  mid=[(p[0][i]+p[1][i])/2 for i in range(4)];JS=combine((F(1,2),kl(p[0],mid)),(F(1,2),kl(p[1],mid)))
  net=combine((1,M),(-1,JS),(-1,kl(mid,m)));ck(interval(net)[1]<0,'full net negative')
  if name=='A035':ck(interval(combine((1,M),(-1,JS)))[0]>0,'lost old KL false positive')
  witness.append({'review':name,'Phi_nats':str(phi),'full_net_negative':True,'KL_prime_form':{str(k):str(v) for k,v in M.items()}})
 sharp=[]
 for s in [F(1,4),F(1,8),F(1,16),F(1,32)]:
  p=[[F(1,4)]*4]*2;m=[(1+2*s)/4]*2+[(1-2*s)/4]*2;q=[m,m]
  phi=verify(p,m,[list(range(4))],[[F(1)],[F(1)]],[q]);ck(phi==2*s*s)
  M=kl(p[0],m);ck(combine((1,M),(-1,kl(p[0],m)))=={},'sharp full bill exactly zero')
  lo,hi=interval(M);ck(lo>=phi and hi<=phi/(1-4*s*s))
  sharp.append({'s':str(s),'Phi':str(phi),'ratio_lower':'1','ratio_upper':str(1/(1-4*s*s)),'full_transaction':'0'})
 out={'status':'PASS','cases':cases,'strict_fine_gap_cases':strict,'checks':checks,'seconds':time.monotonic()-start,'witnesses':witness,'sharpness':sharp,'scope':'generic quantitative reference theorem; actual Boolean sharpness, no universal initial source','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 name='PILOT.json' if pilot else'CHECK.json';(R/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:out[k] for k in ['status','cases','strict_fine_gap_cases','checks','seconds']}))
if __name__=='__main__':main()
