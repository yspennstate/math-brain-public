import sys,json,time
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
R=Path(__file__).resolve().parents[1];MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot';START=time.perf_counter();COUNT=0
def ck(b,label):
 global COUNT
 COUNT+=1
 if not b:raise AssertionError(label)
 if time.perf_counter()-START>(55 if MODE=='pilot' else 180):raise TimeoutError(label)
def exact(x):return F(x),F(x)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,k):return (x[0]*k,x[1]*k) if k>=0 else (x[1]*k,x[0]*k)
def sub(x,y):return add(x,mul(y,-1))
def rounded(x):
 d=1<<90
 return F(x[0].numerator*d//x[0].denominator,d),F(-((-x[1].numerator*d)//x[1].denominator),d)
@lru_cache(None)
def ln(x):
 z=(x-1)/(x+1);assert 0<=z<=F(1,3)
 v=2*sum((z**(2*j+1)/(2*j+1) for j in range(28)),F())
 return v,v+2*z**57/(57*(1-z*z))
@lru_cache(None)
def log(x):
 x=F(x);k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 a,b=ln(x);c,d=ln(F(2))
 return rounded((k+a/d,k+b/c))
def weighted_log(terms):
 out=exact(0)
 for weight,x in terms:
  if weight:out=add(out,mul(log(x),weight))
 return rounded(out)
def enc(x):return {'lo':str(x[0]),'hi':str(x[1]),'approx':float((x[0]+x[1])/2)}
def intersects(x,y):return x[0]<=y[1] and y[0]<=x[1]
def counts(k):
 N=1<<(2*k);B=F(1,1<<k)
 return [(1,(N+(1<<k))//2),(-1,(N-(1<<k))//2)]
def state(m,h):
 A=F(1,1<<m);d=A*A;B=(1<<h)*A;alpha=A/(1<<h);u=1+d;k=m-h
 entries=[]
 for W in (0,1):
  for sig,n in counts(k):
   p=B**4 if W else B*B*(1-B*sig)**2
   q=B*B*d if W else B*B*(u-2*alpha*sig)
   entries.append((p,q,n))
 ck(sum(p*n for p,q,n in entries)==sum(q*n for p,q,n in entries)==1,'complete-state normalization')
 ce=weighted_log([(p*n,1/q) for p,q,n in entries]);H=weighted_log([(p*n,1/p) for p,q,n in entries if p]);K=sub(ce,H)
 for p,q,n in entries:ck(p<=F(4**h)*q,'complete-state likelihood cap')
 return ce,H,K
rows=[];cuts=[];finals=[];cache={}
for m in ([2] if MODE=='pilot' else range(2,21)):
 A=F(1,1<<m);d=A*A;u=1+d;E=exact(0);Kexits=exact(0);J=F()
 ce0,H0,_=state(m,0)
 for h in range(m):
  k=m-h;B=(1<<h)*A;alpha=A/(1<<h);reach=F(1,2*4**h)
  terms0=[];terms1=[];norm0=norm1=F();moment0=moment1=F()
  for W in (0,1):
   for b in (0,1):
    for sig,n in counts(k-1):
     q1=2*B*B*d if W else 2*B*B*(u-(2*alpha*sig if b==0 else 0))
     q2=4*B*B*d if W else 4*B*B*(u-alpha*sig)
     p1=4*B**4 if W or b else 4*B*B*(1-B*sig)**2
     terms1.append((p1*n,q2/q1));moment1+=p1*n*(q2/(2*q1)-1);norm1+=p1*n
     for a in (0,1):
      s=sig*((-1)**(a*b))
      p=B**4 if W else B*B*(1-B*s)**2
      q=B*B*d if W else B*B*(u-2*alpha*s)
      terms0.append((p*n,q1/q));moment0+=p*n*(q1/(2*q)-1);norm0+=p*n
  ck(norm0==norm1==1,'query-parent normalized')
  den=u*u-4*alpha*alpha
  M0=2*alpha*(alpha*(1+B*B)-B*u)/den
  M1=2*alpha*alpha*(1-3*B*B+4*B**3*alpha/u)/den
  ck(moment0==M0 and moment1==M1,'independent exact likelihood moments')
  ck(M0<=0,'first moment nonpositive')
  if h==0:ck(M1==2*d/u,'source first partner moment')
  else:ck(M1<=F(32,15)*alpha*alpha<=F(2,15)*B*B,'later partner moment bound')
  L0=weighted_log(terms0);L1=weighted_log(terms1)
  ck(L0[1]<1,'first CE drop <=1 (strict in numerical profiles)')
  if h==0:ck(L1[1]<1+3*d/u,'source partner bound')
  else:ck(L1[1]<1+B*B/5,'later partner bound')
  e0=sub(L0,exact(3*(F(1,2)+B*B)));e1=sub(L1,exact(6*B*B))
  block=mul(add(e0,mul(e1,F(1,2))),reach)
  bound=-F(9,4)*d if h==0 else -F(59,20)*d
  ck(block[1]<bound,'root-weighted completed block credit')
  E=add(E,block);J+=reach*(F(1,2)+2*B*B)
  # Both clean exits, with FULL original marginalized references.
  Kfirst=sub(exact(1),log(u))
  Ksecond=weighted_log([(F(n,1<<(2*(k-1))),1/(u-alpha*sig)) for sig,n in counts(k-1)])
  ck(Kfirst[1]<1 and Ksecond[1]<F(1,2),'clean exit KL caps')
  Kexits=add(Kexits,mul(add(mul(Kfirst,F(1,2)),mul(Ksecond,F(1,4))),reach))
  cn,hn,kn=state(m,h+1);Ktotal=add(Kexits,mul(kn,reach/4))
  ck(Ktotal[1]<F(9,16),'one global KL earmark for every completed cut')
  EH=add(E,Ktotal)
  ck(EH[1]<F(9,16),'one original extra reserve funds whole entropy history')
  ck(J==F(1,3)*(1-F(1,4**(h+1)))+(h+1)*d,'all original rate2 influence invoices retained')
  ck(add(EH,exact(J))[1]<F(17,16),'legacy rate2 invoice bound')
  c={'m':m,'completed':h+1,'E_Q3':enc(E),'terminal_KL':enc(Ktotal),'E_H3':enc(EH),'removed_influence':str(J)};cuts.append(c)
  cache[m,h]=(L0,L1,block,E,Ktotal)
  rows.append({'m':m,'h':h,'moment0':str(M0),'moment1':str(M1),'L0':enc(L0),'L1':enc(L1),'block_Q3':enc(block)})
 # The remaining edited function is a character of w. Pay final w using old credits.
 wcharge=F(d,2)*(2*m-3);Et=add(E,exact(wcharge));Kt=Kexits;Ht=add(Et,Kt)
 ck(Et[1]<0,'final w paid from SAME accumulated credit')
 ck(Kt[1]<F(5,12) and Ht[1]<F(5,12),'final full KL and entropy invoice bound')
 ck(J+d/2<F(1,2),'all removed influence <1/2 including final w')
 ck(add(Ht,exact(J+d/2))[1]<F(17,16),'final legacy rate2 invoice bound')
 finals.append({'m':m,'w_charge':str(wcharge),'E_Q3':enc(Et),'terminal_KL':enc(Kt),'E_H3':enc(Ht)})

# Independent literal Walsh and original-Q lane; no grouped formula creates its tables.
def fw(v):
 v=list(v);h=1
 while h<len(v):
  for j in range(0,len(v),2*h):
   for i in range(j,j+h):v[i],v[i+h]=v[i]+v[i+h],v[i]-v[i+h]
  h*=2
 return [F(x,len(v)) for x in v]
def law(v):return [a*a for a in fw(v)]
def child(v,b):return [a for x,a in enumerate(v) if (x&1)==b]
def marginal(q):return [q[i]+q[i+1] for i in range(0,len(q),2)]
def ce(p,q):return weighted_log([(a,1/b) for a,b in zip(p,q) if a])
def inf(v):return F(sum(v[x]!=v[x^1] for x in range(len(v))),len(v))
literal=[]
for m in ([2] if MODE=='pilot' else range(2,6)):
 v=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m))-2*(x==0) for x in range(1<<(2*m+1))]
 q=law(v);E=exact(0);Kex=exact(0)
 for h in range(m):
  drop=[]
  for j in (0,1):
   p=law(v);a=child(v,0);b=child(v,1);pa=law(a);pb=law(b);qn=marginal(q);pm=marginal(p)
   ck(all(x in (-1,1) for x in v+a+b),'literal Boolean parent and BOTH children')
   ck(all((x+y)/2==z for x,y,z in zip(pa,pb,pm)),'literal physical two-child mean spectrum')
   I=inf(v);B=F(1,1<<(m-h))
   ck(I==(F(1,2)+B*B if j==0 else 2*B*B),'literal physical influence')
   L=sub(ce(p,q),mul(add(ce(pa,qn),ce(pb,qn)),F(1,2)))
   ck(intersects(L,cache[m,h][j]),'direct full-child CE vs grouped drop')
   E=add(E,mul(sub(L,exact(3*I)),F(1,2*4**h*(1<<j))))
   kb=sub(ce(pb,qn),ce(pb,pb));Kex=add(Kex,mul(kb,F(1,4*4**h*(1<<j))))
   v=a;q=qn
  kp=sub(ce(law(v),q),ce(law(v),law(v)));K=add(Kex,mul(kp,F(1,2*4**(h+1))))
  ck(intersects(E,cache[m,h][3]) and intersects(K,cache[m,h][4]),'literal full frontier and total CE debit')
  literal.append([m,h])
 ck(len(v)==2 and inf(v)==1,'final w is actual Boolean character')
 ck(intersects(sub(ce(law(v),q),exact(3)),exact(2*m-3)),'literal inherited final w debit')
out={'status':'PASS','mode':MODE,'checks':COUNT,'runtime_seconds':time.perf_counter()-START,'grouped_blocks':len(rows),'completed_cuts':len(cuts),'literal_blocks':len(literal),'blocks':rows,'cuts':cuts,'final_w':finals,'arithmetic':'Exact Fraction, 28-term atanh rigorous tail; log endpoints outward 2^-90'}
(R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json' if MODE=='pilot' else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','checks','runtime_seconds','grouped_blocks','completed_cuts','literal_blocks']}))
