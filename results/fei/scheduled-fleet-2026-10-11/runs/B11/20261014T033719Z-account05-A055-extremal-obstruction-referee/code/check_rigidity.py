from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import product,combinations
import exact_library as e
import json,sys,time
ROOT=Path(__file__).resolve().parents[1]; MODE=sys.argv[1]; START=time.perf_counter(); CHECKS=0
def ck(x):
 global CHECKS
 assert x,CHECKS
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
 n=len(f).bit_length()-1;N=len(f);w=fw(f);den=N*N
 ck(sum(a*a for a in w)==den)
 I=Q(sum(s.bit_count()*a*a for s,a in enumerate(w)),den)
 ck(I==Q(sum(f[x]!=f[x^(1<<i)] for x in range(N) for i in range(n)),N))
 H=e.add(*(e.scale(e.ent([Q(a*a,den)]),count) for a,count in Counter(w).items() if a))
 if n<=3:ck([Q(a,N) for a in w]==e.fw(f))
 return w,H,I
def part(a,b):return Q(4*a*a*b*b,a*a+b*b) if a or b else Q(0)
def quartet(v):
 a,b,c,d=v;q=sum(x*x for x in v)
 if not q:return [Q(0)]*7
 ci=part(a,b)+part(c,d);cj=part(a,c)+part(b,d)
 mi=ci-Q(4*(a*b+c*d)**2,q);mj=cj-Q(4*(a*c+b*d)**2,q)
 parity=Q(4*(a*d+b*c)**2,q)
 joint=Q(4*((a*b+c*d)**2+(a*c+b*d)**2+(a*d+b*c)**2),q)
 o=sum(max(x,0) for x in (b*b-a*a,d*d-c*c,c*c-a*a,d*d-b*b))
 ck(mi>=0 and mj>=0);ck(joint==ci+cj+parity-mi-mj)
 ck(joint<=2*(ci+cj)+2*o)
 if o==0 and mi+mj==0:ck(a*d==b*c)
 return ci,cj,mi,mj,parity,joint,o
def tensor(f,m):
 g=[1]
 for _ in range(m):g=[a*b for b in f for a in g]
 return g
def activation(m):
 h=[-1]+[1]*7;hm=tensor(h,m);g=hm+[-x for x in hm]
 r=((m+1)**4-1).bit_length()
 return g+[1]*((1<<r)-1)*len(g),hm,r
def evaluate(f,name,activation_info=None):
 n=len(f).bit_length()-1;w,H,I=stats(f);den=len(f)**2
 O=Q(0);C=[];Os=[]
 for i in range(n):
  rows=Counter((w[t],w[t|(1<<i)]) for t in range(len(w)) if not t>>i&1)
  ci=sum((cnt*part(a,b) for (a,b),cnt in rows.items()),Q(0))/den
  oi=Q(sum(cnt*max(b*b-a*a,0) for (a,b),cnt in rows.items()),den)
  ii=Q(sum(w[t]**2 for t in range(len(w)) if t>>i&1),den)
  ck(ci<=4*ii);ck(oi<=ii);C.append(ci);Os.append(oi);O+=oi
 R=Q(0);pairrecords=[]
 for i,j in combinations(range(n),2):
  rows=Counter((w[t],w[t|1<<i],w[t|1<<j],w[t|1<<i|1<<j]) for t in range(len(w)) if not(t>>i&1 or t>>j&1))
  s=[Q(0)]*7
  for row,count in rows.items():
   z=quartet(row)
   for k in range(7):s[k]+=count*z[k]/den
  ck(s[0]==C[i]);ck(s[1]==C[j]);ck(s[6]==Os[i]+Os[j])
  ck(s[2]+s[3]<=C[i]+C[j]);R+=s[2]+s[3]
  if n<=3 and O==0 and s[2]+s[3]==0:
   ck(all(row[0]*row[3]==row[1]*row[2] for row in rows))
  pairrecords.append({'i':i,'j':j,'refund':str(s[2]+s[3]),'joint_collision':str(s[5])})
 T=O+R;ck((T==0)==(I==0));ck(T<=(4*n-3)*I)
 if I and n>=2:ck(T>=Q(2)**(10-8*n))
 if I and n==1:ck(T==1)
 row={'name':name,'n':n,'I':str(I),'O_total':str(O),'R_total':str(R),'T':str(T),'H_over_I_interval':e.bits(e.scale(H,1/I)) if I else None,'orientation_zero':O==0,'refund_zero':R==0,'pair_records':pairrecords}
 if activation_info:
  hm,r=activation_info;p=Q(1,1<<r);_,hh,hi=stats(hm)
  Ap=e.add(e.scale(e.lg((1-p)**2),-(1-p)**2),e.scale(e.lg(p*p),p*p))
  ck(H==e.add(e.scale(hh,p),{2:4*r*p},Ap));ck(I==p*(hi+1+r))
  K=2;terminalD=e.add(hh,{2:-K*hi});ck(e.iv(terminalD)[0]>0)
  # Complete physical control+z cut, independently projecting every assignment.
  k=len(hm).bit_length()-1;children=[f[x*len(hm):(x+1)*len(hm)] for x in range(len(f)//len(hm))]
  counts=Counter(tuple(c) for c in children)
  EH={};EI=Q(0)
  for child,cnt in counts.items():
   _,hc,ic=stats(list(child));weight=Q(cnt,len(children))
   EH=e.add(EH,e.scale(hc,weight));EI+=weight*ic
  ck(EH==e.scale(hh,p));ck(EI==p*hi)
  SA=e.scale(e.add(EH,{2:-K*EI}),-1);ck(e.iv(SA)[1]<0)
  rootD=e.add(H,{2:-K*I});ck(e.iv(rootD)[0]>0)
  L=e.add(H,e.scale(EH,-1));IA=I-EI
  ck(e.add(rootD,SA)==e.add(L,{2:-K*IA}))
  row.update({'m':k//3,'r':r,'p':str(p),'K':K,'root_D_interval':e.bits(rootD),'actual_S_controls_plus_z_interval':e.bits(SA),'terminal_entropy':e.enc(EH),'terminal_influence':str(EI),'criticality':'FAILS: actual averaged child deficit is positive'})
 (ROOT/'out'/f'{MODE}_{name}.json').write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8')
 return row
def main():
 values=(-1,0,1) if MODE=='pilot' else (-2,-1,0,1,2)
 real_count=0
 for row in product(values,repeat=4):quartet(row);real_count+=1
 records=[];summary={}
 for n in ([1,2] if MODE=='pilot' else [1,2,3]):
  rows=[]
  for word in range(1<<(1<<n)):
   f=[-1 if word>>x&1 else 1 for x in range(1<<n)]
   rows.append(evaluate(f,f'n{n}_mask{word}'))
  summary[str(n)]={'tables':len(rows),'nonconstant_min_T':str(min(Q(x['T']) for x in rows if Q(x['I']))),'nonconstant_orientation_zero':sum(x['orientation_zero'] and Q(x['I'])>0 for x in rows),'nonconstant_joint_zero':sum(Q(x['T'])==0 and Q(x['I'])>0 for x in rows)}
  records.extend(rows)
 for n in ([3,4] if MODE=='pilot' else [4,5,6,7,8]):records.append(evaluate([-1]+[1]*((1<<n)-1),f'point_defect{n}'))
 for m in ([1] if MODE=='pilot' else [1,2]):
  f,hm,r=activation(m);records.append(evaluate(f,f'activation_m{m}',(hm,r)))
 out={'status':'PASS','helper_version':'A055-global-zero-rigidity-v1','mode':MODE,'real_quartets_algebra_only':real_count,'roots':len(records),'assertions':CHECKS+e.N,'runtime_seconds':time.perf_counter()-START,'small_domain':summary,'activation_certificates':[x for x in records if x['name'].startswith('activation')],'arithmetic':'integer FWHT/direct character crosscheck, physical edges, Fraction; canonical prime-log 32-term atanh outward bounds'}
 (ROOT/'out'/f'{MODE.upper()}_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k!='activation_certificates'}))
if __name__=='__main__':main()
