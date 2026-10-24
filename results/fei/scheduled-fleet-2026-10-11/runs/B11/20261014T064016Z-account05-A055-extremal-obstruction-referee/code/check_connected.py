from pathlib import Path
from fractions import Fraction as Q
from collections import Counter,defaultdict
import exact_library as e
import json,sys,time
ROOT=Path(__file__).resolve().parents[1];MODE=sys.argv[1];START=time.perf_counter();CHECKS=0
def ck(v):
 global CHECKS
 assert v,CHECKS
 CHECKS+=1
 assert time.perf_counter()-START<55
def fw(f):
 w=list(f);s=1
 while s<len(w):
  for b in range(0,len(w),2*s):
   for j in range(b,b+s):w[j],w[j+s]=w[j]+w[j+s],w[j]-w[j+s]
  s*=2
 return w
def stats(f):
 N=len(f);n=N.bit_length()-1;w=fw(f)
 ck(sum(a*a for a in w)==N*N)
 inf=[Q(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N) for i in range(n)]
 ck(inf==[Q(sum(w[t]*w[t] for t in range(N) if t>>i&1),N*N) for i in range(n)])
 H=e.add(*(e.scale(e.ent([Q(a*a,N*N)]),cnt) for a,cnt in Counter(w).items() if a))
 return H,inf,w
def components(f,sign):
 n=len(f).bit_length()-1;seen=bytearray(len(f));out=[]
 for start,v in enumerate(f):
  if v!=sign or seen[start]:continue
  stack=[start];seen[start]=1;component=[]
  while stack:
   x=stack.pop();component.append(x)
   for i in range(n):
    y=x^(1<<i)
    if f[y]==sign and not seen[y]:seen[y]=1;stack.append(y)
  out.append(component)
 return out
def tensor(h,m):
 f=[1]
 for _ in range(m):f=[a*b for b in h for a in f]
 return f
def project(f,mask,assignment):
 n=len(f).bit_length()-1;fixed=[i for i in range(n) if mask>>i&1];free=[i for i in range(n) if not mask>>i&1]
 base=sum(((assignment>>j)&1)<<i for j,i in enumerate(fixed))
 return tuple(f[base|sum(((v>>j)&1)<<i for j,i in enumerate(free))] for v in range(1<<len(free)))
def mean_child(f,mask):
 count=1<<mask.bit_count();counts=Counter(project(f,mask,v) for v in range(count));H={};I=Q(0)
 for child,cnt in counts.items():
  h,inf,_=stats(child);H=e.add(H,e.scale(h,Q(cnt,count)));I+=Q(cnt,count)*sum(inf)
 return H,I
def geometry_review():
 cuts=roots=0
 for n in (1,2,3):
  N=1<<n
  for word in range(1<<N):
   f=[-1 if word>>x&1 else 1 for x in range(N)];comps=components(f,-1);roots+=1
   for mask in range(1,N-1):
    r=mask.bit_count();counters=[Counter(x&~mask for x in comp) for comp in comps]
    totals=Counter()
    for c in counters:totals.update(c)
    W={};Qcost={};Omega={}
    for c in counters:
     for y,ct in c.items():
      mass=Q(ct,N);W=e.add(W,{2:r*mass},e.scale(e.lg(Q(ct)),-mass))
      Omega=e.add(Omega,e.scale(e.lg(Q(totals[y],ct)),mass))
    for ct in totals.values():
     mass=Q(ct,N);Qcost=e.add(Qcost,{2:r*mass},e.scale(e.lg(Q(ct)),-mass))
    ck(W==e.add(Qcost,Omega))
    energy=Q(sum(f[x]!=f[x^(1<<i)] for x in range(N) for i in range(n) if mask>>i&1),4*N)
    ck(not W or e.iv(e.add({2:2*energy},e.scale(W,-1)))[0]>=0)
    labelled=sum(sum((x^(1<<i)) not in set(comp) for x in comp for i in range(n) if mask>>i&1) for comp in comps)
    ck(Q(labelled,2*N)==energy)
    cuts+=1
 return {'roots':roots,'proper_cuts':cuts,'verdict':'A054 physical fiber identities and edge credit HOLDS at scope; raw/sign transfer not audited'}
def case(h,m,name):
 hm=tensor(h,m);d=len(hm).bit_length()-1;r=((m+1)**4-1).bit_length();p=Q(1,1<<r)
 U=[-1]*len(hm)+hm+[1]*(2*len(hm));F=U+[1]*((1<<r)-1)*len(U)
 G=F*4;N=len(G).bit_length()-1;s=Q(1,len(G));vertex=1<<(d+2);ck(G[vertex]==1);G[vertex]=-1
 H,inf,w=stats(G);IU=sum(inf);mu=Q(sum(hm),len(hm));c=(3-mu)/4
 hn=sum(x<0 for x in hm);neg=4*(len(hm)+hn)+1
 compsm=components(G,-1);compsp=components(G,1)
 ck(len(compsm)==len(compsp)==1);ck(len(compsm[0])==neg)
 ck(neg%2==1);ck(all(a%4==2 for a in w));ck(all(a>0 for a in inf))
 ck(max(inf)<=p+2*s)
 giants=[neg*neg>1<<(N-1),(len(G)-neg)**2>1<<(N-1)]
 if name.startswith('pd3'):ck(all(giants))
 A=((1<<r)-1)<<(d+2); B=((1<<N)-1)^((1<<d)-1)
 fibers=Counter(x&~A for x in compsm[0]);ck(Counter(fibers.values())==Counter({1:neg-2,2:1}))
 eta=Q(neg,len(G));W=r*eta-2*s;ck(W>=r*eta/2)
 hc,ic=mean_child(G,A);IA=sum(inf[i] for i in range(N) if A>>i&1)
 ck(IA==r*p*c+2*s*(r-2));L=e.add(H,e.scale(hc,-1));ck(e.iv(e.add({2:6*IA},e.scale(L,-1)))[0]>0)
 HU,iU,_=stats(U);pdret=[-1]+[1]*((1<<(d+4))-1);HP,ip,_=stats(pdret)
 ck(hc==e.add(e.scale(HU,p),e.scale(HP,p)));ck(ic==p*(sum(iU)+sum(ip)))
 hb,ib=mean_child(G,B);HH,iH,_=stats(hm);pd=[-1]+[1]*(len(hm)-1);HPd,iPd,_=stats(pd)
 weight=Q(1,1<<(r+4));ck(hb==e.add(e.scale(HH,p/4),e.scale(HPd,weight)));ck(ib==p*sum(iH)/4+weight*sum(iPd))
 DK=e.add(H,{2:-2*IU});SB=e.scale(e.add(hb,{2:-2*ib}),-1)
 if name.startswith('pd3'):ck(e.iv(DK)[0]>0);ck(e.iv(SB)[1]<0)
 result={'name':name,'m':m,'r':r,'N':N,'negative_size':neg,'positive_size':len(G)-neg,'both_connected':True,'giant_tests':giants,'prime':'odd negative count','full_support':'Walsh2 mod4','I':str(IU),'max_Inf':str(max(inf)),'W_controls':str(W),'fiber_entropy_times_density':str(2*s),'control_price_interval':e.bits(e.scale(L,1/IA)),'root_D_K2_interval':e.bits(DK),'actual_terminal_S_B_K2_interval':e.bits(SB),'terminal_H':e.enc(hb),'terminal_I':str(ib),'K2_scope':'Named pd3 core violates K2; two-bit controls are geometry tests only'}
 (ROOT/'out'/f'{MODE}_{name}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 return result
def main():
 results=[case([-1]+[1]*7,1,'pd3_m1')]
 review=None
 if MODE=='full':
  review=geometry_review()
  for word in range(1,15):results.append(case([-1 if word>>x&1 else 1 for x in range(4)],1,f'two_bit_mask{word}'))
  results.append(case([-1]+[1]*7,2,'pd3_m2'))
 out={'status':'PASS','helper_version':'A055-two-sided-giant-embedding-v1','mode':MODE,'fixture_roots':len(results),'geometry_review':review,'assertions':CHECKS+e.N,'runtime_seconds':time.perf_counter()-START,'cases':results}
 (ROOT/'out'/f'{MODE.upper()}_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
if __name__=='__main__':main()
