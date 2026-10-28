from pathlib import Path
from fractions import Fraction as Q
import json,time
start=time.monotonic(); rows=[];checks=0
def walsh(t):
 w=list(t);step=1
 while step<len(w):
  for a in range(0,len(w),2*step):
   for j in range(a,a+step):p,q=w[j],w[j+step];w[j]=p+q;w[j+step]=p-q
  step*=2
 return w
for m in [2,4,6,8,10,12]:
 N=1<<m; r=1<<(m//2)
 g=[(-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(m//2)) for y in range(N)]
 h=list(g);h[0]*=-1
 wg,wh=walsh(g),walsh(h)
 assert all(abs(w)==r for w in wg);checks+=N
 assert all(v==u-2 for u,v in zip(wg,wh));checks+=N
 a=[w-1 for w in wg]
 norm=sum(w*w for w in a); fourth=sum(w**4 for w in a)
 assert norm==N*(N-1) and fourth==N*(N-1)*(N+3);checks+=2
 chi=Q(N*fourth,norm*norm)-1
 assert chi==Q(4,N-1);checks+=1
 f=[g[x>>1] if x%2==0 else h[x>>1] for x in range(2*N)]
 wf=walsh(f)
 assert all(wf[2*s]==2*wg[s]-2 and wf[2*s+1]==2 for s in range(N));checks+=N
 inf=[]
 for j in range(m+1):
  v=Q(sum(f[x]!=f[x^(1<<j)] for x in range(2*N)),2*N)
  assert v==(Q(1,N) if j==0 else Q(1,2)+Q(1,N));checks+=1
  inf.append(v)
 assert sum(inf)==Q(m,2)+Q(m+1,N);checks+=1
 assert Q(m+1,1)/sum(inf)<=3;checks+=1
 positive=[]
 for C in [2,4]:
  # Analytic proof: d_C > (m-C-6)/N, since ln2>2/3.
  if m>=C+6:assert Q(m-C-6,N)>=0;positive.append(C)
  checks+=1
 rows.append({'m':m,'N':N,'I':str(sum(inf)),'selector_influence':str(inf[0]),'A_raw_norm':norm,'A_raw_fourth_moment':fourth,'chi_square_to_uniform':str(chi),'certified_positive_local_debt_rates':positive,'H_upper_over_I':str(Q(m+1,1)/sum(inf))})
 assert time.monotonic()-start<20
out={'status':'PASS','cases':rows,'exact_assertions':checks,'seconds':time.monotonic()-start,'proof_of_all_m_and_all_tensor_orders':'NO_GO.md; finite checks are not the all-dimensional proof'}
(Path(__file__).resolve().parents[1]/'out/nogo.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'status':'PASS','cases':len(rows),'exact_assertions':checks,'seconds':out['seconds']}))
