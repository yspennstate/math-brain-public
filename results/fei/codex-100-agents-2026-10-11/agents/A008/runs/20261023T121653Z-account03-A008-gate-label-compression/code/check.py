from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import math,itertools,json,time,sys
RUN=Path(__file__).resolve().parents[1];START=time.monotonic();CHECKS=0
def ck(v):
 global CHECKS
 assert v
 CHECKS+=1
 if CHECKS%500==0 and time.monotonic()-START>55:raise RuntimeError('frozen55-second limit')
def ln_unit(x,L=16):
 z=(x-1)/(x+1);s=sum(z**(2*k+1)/F(2*k+1) for k in range(L))*2
 return s,s+2*z**(2*L+1)/(F(2*L+1)*(1-z*z))
LN2=ln_unit(F(2))
@lru_cache(None)
def logbounds(x):
 x=F(x);assert x>0;e=x.numerator.bit_length()-x.denominator.bit_length()
 scale=F(2)**e;m=x/scale
 if m<1:e-=1;m*=2
 if m>=2:e+=1;m/=2
 lo,hi=ln_unit(m);return F(e)+lo/LN2[1],F(e)+hi/LN2[0]
def up(x):
 z=logbounds(x)[1]*(1<<40);return F(-((-z.numerator)//z.denominator),1<<40)
def low(x):
 z=logbounds(x)[0]*(1<<40);return F(z.numerator//z.denominator,1<<40)
def entropy_upper(ps):return sum(p*up(1/p) for p in ps if p)
def fwht(xs):
 a=xs[:];step=1
 while step<len(a):
  for st in range(0,len(a),2*step):
   for i in range(st,st+step):x,y=a[i],a[i+step];a[i],a[i+step]=x+y,x-y
  step*=2
 return a
def common(widths,enumerate_anchor=True):
 r=len(widths);n=1+sum(widths);M=1<<n;pos=1;blocks=[];masks=[];weights=[];den=1;rho=F(0)
 for w in widths:
  block=((1<<w)-1)<<pos;blocks.append(block);support=[0]+list(range(pos,pos+w));pos+=w;d=w+1;v=1<<d
  masks.append([sum(1<<support[i] for i in range(d) if b>>i&1) for b in range(v)])
  weights.append([(v-1)**2]+[1]*(v-1));den*=v*(v-1);rho+=F(1,v)
 U={0:1};V={0:0}
 for ms,ws in zip(masks,weights):
  u={};v={}
  for a in U:
   for b,weight in zip(ms,ws):
    dest=a|b;u[dest]=u.get(dest,0)+U[a]*weight
    v[dest]=v.get(dest,0)+(V[a]+bool(b)*U[a])*weight
  U,V=u,v
 q=[F(V.get(a,0),den)/rho for a in range(M)];ck(q[0]==0 and sum(q)==1);ck(all(q[1:]))
 runs=0
 if enumerate_anchor:
  direct=[0]*M
  for anchor in range(r):
   total=0
   choices=[range(1,len(masks[j])) if j==anchor else range(len(masks[j])) for j in range(r)]
   for tupleidx in itertools.product(*choices):
    dest=0;weight=1
    for j,i in enumerate(tupleidx):dest|=masks[j][i];weight*=weights[j][i] if j!=anchor else 1
    direct[dest]+=weight;total+=weight;runs+=1
   ck(F(total,den)==F(1,1<<(widths[anchor]+1)))
  for a in range(M):ck(direct[a]==V.get(a,0))
 truth=[1 if (x&1) or all(x&b for b in blocks) else -1 for x in range(M)]
 wh=fwht(truth);P=[F(z*z,M*M) for z in wh];ck(sum(P)==1)
 eps=[F(1,1<<w) for w in widths];a=math.prod(1-e for e in eps);J=a*sum(w*e/(1-e) for w,e in zip(widths,eps));I=1-a+J
 ck(P[0]==a*a and P[1]==(1-a)**2)
 ck(sum(P[s]*s.bit_count() for s in range(M))==I)
 ck(F(sum(truth[x]!=truth[x^(1<<i)] for i in range(n) for x in range(M)),M)==I)
 for j,b in enumerate(blocks):ck(sum(P[s] for s in range(M) if s&b)==2*a*eps[j])
 for B in range(2,M,2):
  L=sum(bool(B&b) for b in blocks);prod=F(L,1)/rho
  for j,b in enumerate(blocks):
   t=eps[j]/2;prod*=t*t/(1-t) if B&b else 1-t
  ck(q[B]==prod);ck(q[B|1]>=(2**L-1)*prod);ck(P[B]==P[B|1])
 R=[v/2 for v in q];R[1]+=F(1,2);ck(sum(R)==1)
 grouped={}
 for s in range(1,M):grouped[R[s]]=grouped.get(R[s],0)+P[s]
 C=sum(p*up(1/v) for v,p in grouped.items() if p)
 ck(C<=F(29,2)*I)
 return {'widths':widths,'n':n,'actual_anchor_runs':runs,'influence':str(I),'repaired_C_upper':str(C),'ratio_upper':str(C/I)}
def obstruction():
 result=[]
 for r in range(4,65):
  a=F(3,4)**r;I=1-a+F(r,2)*F(3,4)**(r-1);qz=F(1,7)*F(25,28)**(r-1)
  ck(I<2 and (1-a)**2>F(1,4));ck(low(F(28,25))>=F(3,28))
  lower=(1-a)**2*low(1/qz);ck(lower/I>F(3*(r-1),224))
  Hnu=r*(2-F(1,2)*low(3));Hb=entropy_upper([a,1-a]);H=2*a*Hnu+2*(1-a)*Hb
  ck(H<6*I)
  if r in [4,5,6]:
   n=2*r+1;M=1<<n;blocks=[3<<(1+2*j) for j in range(r)]
   truth=[1 if (x&1) or all(x&b for b in blocks) else -1 for x in range(M)];wh=fwht(truth)
   ck(F(wh[1]**2,M*M)==(1-a)**2);ck(F(sum(z*z*s.bit_count() for s,z in enumerate(wh)),M*M)==I)
  result.append({'r':r,'Q_core':str(qz),'C_source_lower_over_I':str(lower/I),'I':str(I)})
 return result
def paired(ws):
 dim=sum(ws);n=2*dim;M=1<<n;pos=0;bx=[]
 for w in ws:bx.append(((1<<w)-1)<<pos);pos+=w
 by=[b<<dim for b in bx]
 truth=[1 if all(x&b for b in bx) and any((x&b)==b for b in by) else -1 for x in range(M)]
 wh=fwht(truth);P=[F(z*z,M*M) for z in wh];eps=[F(1,1<<w) for w in ws];a=math.prod(1-e for e in eps);rho=sum(eps)*2;I=2*a*sum(w*e/(1-e) for w,e in zip(ws,eps));ck(sum(P)==1)
 ck(sum(p*s.bit_count() for s,p in enumerate(P))==I)
 ck(F(sum(truth[x]!=truth[x^(1<<i)] for i in range(n) for x in range(M)),M)==I)
 grouped={};norm=F(0)
 for s in range(1,M):
  active=0;mu=F(1)
  for b,e in zip(bx+by,eps+eps):
   if s&b:active+=1;mu*=e*e/(1-e)
   else:mu*=1-e
  q=active*mu/rho;norm+=q;grouped[q]=grouped.get(q,0)+P[s]
 ck(norm==1)
 for j,b in enumerate(bx):ck(sum(P[s] for s in range(M) if s&b)+sum(P[s] for s in range(M) if s&by[j])==4*a*eps[j])
 C=sum(p*up(1/q) for q,p in grouped.items() if p);ck(C<F(155,24)*I)
 return {'widths':ws,'n':n,'C_upper_over_I':str(C/I)}
def interface(pilot):
 num=0;domain=range(1,4) if pilot else range(1,15)
 refs=[(F(1,3),F(1,3),F(1,3)),(F(1,2),F(1,3),F(1,6))]
 for u,v in itertools.product(domain,repeat=2):
  us=[int(u>>x&1) for x in range(4)];vs=[int(v>>x&1) for x in range(4)];a=F(sum(us),4);b=F(sum(vs),4)
  gu=fwht([2*t-1 for t in us]);gv=fwht([2*t-1 for t in vs]);pg=[F(t*t,16) for t in gu];ph=[F(t*t,16) for t in gv]
  wf=fwht([2*us[x&3]*vs[x>>2]-1 for x in range(16)]);P=[F(t*t,256) for t in wf];num+=1
  for s in range(1,4):ck(sum(P[s|(t<<2)] for t in range(4))==b*pg[s])
  for t in range(1,4):ck(sum(P[s|(t<<2)] for s in range(4))==a*ph[t])
  ck(sum(p*s.bit_count() for s,p in enumerate(P))==b*sum(pg[s]*s.bit_count() for s in range(4))+a*sum(ph[t]*t.bit_count() for t in range(4)))
  for qg,qh in [refs,refs[::-1]]:
   qs=[]
   for s in range(4):
    for t in range(4):
     if s or t:qs.append((qg[s-1] if s else 1)*(qh[t-1] if t else 1)/3)
   ck(sum(qs)==1)
 return num
def local_cases(pilot):
 num=0
 for w in ([4] if pilot else [4,5,6]):
  r=1<<w;rho=F(1,2*r);Z=1-(1-rho)**r
  for k in range(r+1):
   es=[F(1,1<<w)]*(r-k)+[F(1,1<<(w+1))]*k;ds=[w]*(r-k)+[w+1]*k;a=math.prod(1-e for e in es);I=2*a*sum(d*e/(1-e) for d,e in zip(ds,es));var=4*a*(1-a)
   C=var*(r*up(1/(1-rho))+up(Z))+sum(4*a*e*(up((1-rho)/rho)+up((1<<d)-1)) for d,e in zip(ds,es))
   ck(C<=F(11,2)*I);ck((1-rho)**r>=F(1,2));num+=1
 return num
if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'pilot';res={'mode':mode}
 if mode in ['pilot','full']:
  lists=[list(ws) for r in range(1,3 if mode=='pilot' else 4) for ws in itertools.product(range(1,3 if mode=='pilot' else 4),repeat=r)]
  res['heterogeneous']=[common(ws) for ws in lists]
  if mode=='full':res['source_obstruction']=obstruction()
 else:
  pilot=mode=='review_pilot';lists=[list(ws) for r in range(1,3 if pilot else 4) for ws in itertools.product(range(1,3 if pilot else 4),repeat=r) if sum(ws)<=6]
  res['paired']=[paired(ws) for ws in lists];res['indicator_pairs']=interface(pilot);res['local_moment_cases']=local_cases(pilot)
 res.update(status='PASS',checks=CHECKS,elapsed_seconds=time.monotonic()-START)
 (RUN/'out'/f'{mode}.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({'mode':mode,'status':'PASS','checks':CHECKS,'elapsed_seconds':res['elapsed_seconds'],'functions':len(res.get('heterogeneous',res.get('paired',[]))),'indicator_pairs':res.get('indicator_pairs'),'local_moment_cases':res.get('local_moment_cases')}))
