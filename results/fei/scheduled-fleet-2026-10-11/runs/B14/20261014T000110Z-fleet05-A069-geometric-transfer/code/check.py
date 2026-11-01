from pathlib import Path
from fractions import Fraction as F
import json,time
RUN=Path(__file__).resolve().parents[1]
start=time.monotonic();checks=0
def ck(q):
 global checks
 assert q
 checks+=1
def guard():
 if time.monotonic()-start>55:raise RuntimeError('55-second frozen guard')
def fwht(a):
 a=a[:];h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
  h*=2
 return a
def binary(ids):
 if len(ids)==1:return ids[0]
 k=len(ids)//2
 return binary(ids[:k]),binary(ids[k:])
def cell(t):return 1<<t if isinstance(t,int) else sum(cell(c) for c in t)
def nodes(t):return [] if isinstance(t,int) else [(cell(t),len(t))]+[v for c in t for v in nodes(c)]
def table(mask,size):return [-1 if mask>>x&1 else 1 for x in range(size)]
def xor_product(*ts):return [prod_at(ts,x) for x in range(len(ts[0]))]
def prod_at(ts,x):
 p=1
 for t in ts:p*=t[x]
 return p
def cost(t,ns):
 a=fwht(t);size=len(t)
 return F(sum(a[s]**2*sum(b for c,b in ns if s&c) for s in range(size)),size**2)
def influence(t,N):return F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t)) for i in range(N)),len(t))
def paired_bits(t,c):
 bits=0;j=0;den=0
 for x in range(len(t)):
  for y in range(len(t)):
   if (x^y)&~c==0:
    if t[x]!=t[y]:bits|=1<<j
    j+=1
 return bits,j
def refund(ts,ns):
 answer=F()
 for c,b in ns:
  events=[paired_bits(t,c) for t in ts];den=events[0][1]
  if len(ts)==2:ev=events[0][0]&events[1][0]
  else:
   x,y,z=[e[0] for e in events];ev=(x&y)|(x&z)|(y&z)
  answer+=4*b*F(ev.bit_count(),den)
 return answer
def census():
 ns=nodes((0,(1,2)));ts=[table(m,8) for m in range(256)]
 ws=[cost(t,ns) for t in ts]
 events=[[paired_bits(t,c) for c,b in ns] for t in ts]
 for u in range(256):
  guard()
  for v in range(256):
   R=sum((4*b*F((events[u][j][0]&events[v][j][0]).bit_count(),events[u][j][1]) for j,(c,b) in enumerate(ns)),F())
   ck(ws[u^v]==ws[u]+ws[v]-R);ck(ws[u^v]<=ws[u]+ws[v])
 for j in range(4096):
  u=j%256;v=j//256;w=(17*j+3)%256
  R=F()
  for k,(c,b) in enumerate(ns):
   x,y,z=events[u][k][0],events[v][k][0],events[w][k][0]
   R+=4*b*F(((x&y)|(x&z)|(y&z)).bit_count(),events[u][k][1])
  ck(ws[u^v^w]==ws[u]+ws[v]+ws[w]-R)
 return 65536,4096
def overlapping():
 cases=0;rows=[]
 for r,s,t,k in [(1,1,1,1),(2,1,1,1),(1,2,1,1),(1,1,2,1),(1,1,1,2)]:
  C=list(range(r));U=list(range(r,r+s));V=list(range(r+s,r+s+t));Y=list(range(r+s+t,r+s+t+k))
  N=r+s+t+k;size=1<<N;ns=nodes((binary(Y),(binary(C),(binary(U),binary(V)))))
  c,a,b=F(1,1<<r),F(1,1<<s),F(1,1<<t)
  def bits(x,ids):return sum(((x>>i)&1)<<j for j,i in enumerate(ids))
  for assignment in range(1<<(r+s+t)):
   guard();cs=assignment&((1<<r)-1);us=(assignment>>r)&((1<<s)-1);vs=assignment>>(r+s)
   A=[int(bits(x,C)==cs and bits(x,U)==us) for x in range(size)]
   B=[int(bits(x,C)==cs and bits(x,V)==vs) for x in range(size)]
   q1=[1-2*v for v in A];q2=[1-2*v for v in B];q=xor_product(q1,q2)
   W1,W2,Wq=cost(q1,ns),cost(q2,ns),cost(q,ns)
   I1,I2,Iq=influence(q1,N),influence(q2,N),influence(q,N)
   ck(Iq==2*c*(s*a+t*b+r*(a+b-2*a*b)))
   ck(I1+I2==2*c*(s*a+t*b+r*(a+b)))
   ck(I1+I2<=2*Iq);ck(W1<=6*I1);ck(W2<=6*I2);ck(Wq<=12*Iq)
   seeds=[[1]*size,[(-1)**x.bit_count() for x in range(size)],[1 if not (x>>Y[-1]&1) else -1 for x in range(size)],q]
   for g in seeds:
    f=xor_product(g,q1,q2);Wg=cost(g,ns);Wf=cost(f,ns)
    R3=refund([g,q1,q2],ns)
    ck(Wf==Wg+W1+W2-R3);ck(Wf<=Wg+12*Iq)
    ck(R3==refund([q1,q2],ns)+refund([g,q],ns))
    ck(R3==refund([g,q1],ns)+refund([xor_product(g,q1),q2],ns))
    for x in range(size):
     e1=-2*g[x]*A[x];e2=-2*g[x]*B[x];e12=-2*g[x]*A[x]*B[x]
     ck(f[x]-g[x]==e1+e2-2*e12)
    if g==seeds[2]:ck(influence(f,N)==influence(g,N)+Iq)
    if g==q:ck(influence(f,N)==0 and Wf==0)
    cases+=1
  rows.append({'r':r,'s':s,'t':t,'core_bits':k,'I_net':str(Iq),'W_net':str(Wq),'ratio_W_I':str(Wq/Iq)})
 ck(cases==256)
 return cases,rows
def fixtures():
 ns=[(3,2)];g=[1,-1,1,-1]
 A=[1,0,0,0];B=[0,1,0,0];q1=[1-2*a for a in A];q2=[1-2*b for b in B]
 e1=[-2*x*a for x,a in zip(g,A)];e2=[-2*x*b for x,b in zip(g,B)]
 x,y=fwht(e1),fwht(e2)
 cross=F(sum(x[s]*y[s]*(1+(2 if s else 0)) for s in range(4)),16)
 ck(cross==F(1,2));ck(refund([g,q1,q2],ns)==3)
 ck(cost(xor_product(g,q1,q2),ns)==cost(g,ns)==2)
 # Identical masks are outside private-block hypothesis and have zero net influence.
 q=[-1,1,1,1];ck(influence(xor_product(q,q),2)==0);ck(influence(q,2)>0)
 return {'A070_positive_cross':'1/2','simultaneous_refund':'3','identical_mask_boundary':'net I=0, input I>0'}
def main():
 (RUN/'out').mkdir(exist_ok=True)
 p,t=census();n,rows=overlapping();f=fixtures();guard()
 result={'helper_version':'A069-stage3-resampling-v1','result':'PASS','cases':p+t+n+2,'pair_cases':p,'triple_cases':t,'overlapping_cases':n,'assertions':checks,'seconds':time.monotonic()-start,'controller_rows':rows,'fixtures':f,'arithmetic':'integer FWHT, Fraction, direct resampling and physical edges'}
 (RUN/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
