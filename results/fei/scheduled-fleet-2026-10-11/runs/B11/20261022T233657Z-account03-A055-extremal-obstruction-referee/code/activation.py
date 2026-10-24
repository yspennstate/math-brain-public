from exact import fw,add,mul,log,enc,sgn,put
from path_tensor import rank,collision,restrict
from fractions import Fraction as Q
from collections import Counter
import json,time,sys
checks=0
def ck(x):
 global checks
 assert x;checks+=1
def h(x):return mul(log(x*x),-x*x) if x else {}
def H(ws,N):
 out={}
 for w,c in Counter(abs(x) for x in ws if x).items():out=add(out,h(Q(w,N)),c)
 return out
def AH(H0,mu,k):
 p=Q(1,1<<k);b=1-mu
 out=mul(H0,p);out=add(out,h(1-p*b));out=add(out,h(mu),-p);out=add(out,h(b),p*(1-p));return add(out,{2:2*k*p*((1-mu*mu)+(1-p)*b*b)})
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;C=[0,1,3,12,6,24,48,32];pathv=[-1 if ((x&63)&C[x>>6]).bit_count()%2 else 1 for x in range(512)];M=8;cases=[]
 params=[(2,14,1,2)] if pilot else [(d,mask,t,k) for d,mask in [(2,14),(3,254)] for t in [1,2] for k in [2,3]]
 actual=0
 for d,mask,t,k in params:
  seed=[1 if mask>>x&1 else -1 for x in range(1<<d)];core=[]
  for x in range(1<<(d*t)):
   val=1
   for j in range(t):val*=seed[(x>>(d*j))&((1<<d)-1)]
   core.append(val)
  g=[pathv[x&511]*core[x>>9] for x in range(1<<(9+d*t))];NG=len(g);n=NG.bit_length()-1;wg=fw(g);HG=H(wg,NG);IG=Q(sum(s.bit_count()*w*w for s,w in enumerate(wg)),NG*NG);mu=Q(wg[0],NG);p=Q(1,1<<k);NF=NG<<k
  raw={s:w for s,w in enumerate(wg) if w};raw[0]=raw.get(0,0)-NG
  spectrum={s|(u<<n):w for s,w in raw.items() if w for u in range(1<<k)};spectrum[0]=spectrum.get(0,0)+NF
  HF=H(spectrum.values(),NF);IF=Q(sum(s.bit_count()*w*w for s,w in spectrum.items()),NF*NF)
  ck(HF==AH(HG,mu,k));ck(IF==p*(IG+k*(1-mu)));ck(sum(w*w for w in spectrum.values())==NF*NF)
  support=list(spectrum);ck(rank([s^support[0] for s in support])==n+k)
  ck(all((s^4) not in spectrum and (s^8) not in spectrum for s in support))
  ci,cj,cij=collision({s:Q(w,NF) for s,w in spectrum.items()},2,3);ck(ci==cj==0);ck(cij>=2*p*Q(M-1,M*M));ck(cij>0)
  ck(Q(sum(w*w for s,w in spectrum.items() if s&4),NF*NF)==p*Q(2,M))
  # Direct parity mass checks for every coordinate and named mixed forms, not a full orbit census.
  dataforms=list(1<<j for j in range(n))+[12,(1<<n)-1]
  for v in dataforms:
   w0=Q(sum(w*w for s,w in enumerate(wg) if (s&v).bit_count()%2),NG*NG)
   for u in [0,1,3]:
    form=v|(u<<n);ww=Q(sum(w*w for s,w in spectrum.items() if (s&form).bit_count()%2),NF*NF)
    ck(ww==(p*(1-mu) if u else p*w0));ck(ww<=Q(1,2))
  pairHs=[];pairIs=[]
  for z in range(4):
   gz=restrict(g,[2,3],z);wz=fw(gz);mz=Q(wz[0],len(gz));ck(mz==(0 if z in [1,2] else 2*mu));ck(H(wz,len(gz))==add(HG,{2:Q(-4,M)}))
   ez=AH(add(HG,{2:Q(-4,M)}),mz,k);iz=p*(IG-Q(4,M)+k*(1-mz));pairHs.append(ez);pairIs.append(iz)
  avgH={}
  for q in pairHs:avgH=add(avgH,q,Q(1,4))
  L=add(HF,avgH,-1);ck(sum(pairIs)/4==IF-p*Q(4,M))
  for K in [2,8]:
   D=add(HF,{2:-K*IF});S={}
   for hz,iz in zip(pairHs,pairIs):S=add(S,add(hz,{2:-K*iz}),Q(-1,4))
   ck(add(D,S)==add(L,{2:-K*p*Q(4,M)}))
   si=add(mul(D,-1),{2:-K*p*Q(2,M)});ck(add(D,si)=={2:-K*p*Q(2,M)})
  if k==2 and (d,t) in [(2,1),(3,1),(2,2)]:
   f=g+[1]*(NF-NG);ck(fw(f)==[spectrum.get(s,0) for s in range(NF)])
   ck(Q(sum(f[x]!=f[x^(1<<j)] for x in range(NF) for j in range(n+k)),NF)==IF)
   for z in range(2):
    child=restrict(f,[2],z);wc=fw(child);ck(H(wc,len(child))==HF);ck(Q(sum(s.bit_count()*w*w for s,w in enumerate(wc)),len(child)**2)==IF-p*Q(2,M))
   actual+=1
  cases.append({'seed_n':d,'seed_mask':mask,'copies':t,'controls':k,'I':str(IF),'mu_core_path':str(mu),'C_i':'0','C_j':'0','C_ij':str(cij),'singleton_I':str(p*Q(2,M)),'pair_L':enc(L),'pair_terminal_H':[enc(x) for x in pairHs],'pair_terminal_I':[str(x) for x in pairIs]})
  ck(time.perf_counter()-start<55)
 out={'status':'PASS','pilot':pilot,'assertions':checks,'fixtures':len(cases),'actual_full_roots':actual,'actual_singleton_children':2*actual,'cases':cases,'elapsed_seconds':time.perf_counter()-start}
 put('ACTIVATION_PILOT.json' if pilot else 'ACTIVATION.json',out);print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
if __name__=='__main__':main()
