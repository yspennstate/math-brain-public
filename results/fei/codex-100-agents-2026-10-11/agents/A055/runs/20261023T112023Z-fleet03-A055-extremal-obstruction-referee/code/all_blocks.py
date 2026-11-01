from exact import Q,fw,entropy,add,mul,sgn,log,put,enc
from functools import lru_cache
from collections import Counter
import time,sys,json
start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
 assert time.perf_counter()-start<55,'frozen cap'
def h2(x):
 return add(mul(log(x),-x) if x else {},mul(log(1-x),x-1) if x!=1 else {})
@lru_cache(None)
def stat(v):
 N=len(v);n=N.bit_length()-1;W=fw(v);a=[Q(w,N) for w in W]
 H=entropy(a);mu=a[0]
 I=Q(sum(v[x]!=v[x^(1<<j)] for x in range(N) for j in range(n)),N)
 ck(I==sum(s.bit_count()*q*q for s,q in enumerate(a)))
 B=fw([w*w for w in W]);costs=[min(Q(N*N-b,2*N*N),Q(N*N+b,2*N*N)) for b in B]
 # Actual finite greedy minimum parity basis; output shifts center each selected row.
 piv={};amin=Q(0)
 for c,s in sorted((costs[s],s) for s in range(1,N)):
  v0=s
  while v0:
   j=v0.bit_length()-1
   if j in piv:v0^=piv[j]
   else:piv[j]=v0;amin+=c;break
  if len(piv)==n:break
 ck(len(piv)==n);ck(0<=amin<=I)
 # Alphabet entropy bound via nonempty spectral mass, checked at every unique child.
 nonempty=1-mu*mu
 ck(sgn(add(add(h2(nonempty),{2:nonempty*n}),H,-1))>=0)
 D={};Dp={}
 for K in [Q(0),Q(15,4),Q(8)]:
  d=add(H,{2:-K*amin});D[K]=d;Dp[K]=d if sgn(d)>0 else {}
 return H,I,amin,mu,D,Dp
def root(seed):
 out=[];nseed=len(seed).bit_length()-1;nd=4+nseed
 for x in range(1<<(nd+3)):
  a,b,c,z=[(x>>j)&1 for j in range(4)]
  out.append((-1)**(a*b+a*c+b*c+z*a)*seed[(x>>4)&(len(seed)-1)] if x>>nd==0 else 1)
 return tuple(out)
def children(v,A):
 n=len(v).bit_length()-1;J=[j for j in range(n) if A&(1<<j)];C=[j for j in range(n) if not A&(1<<j)]
 offsets=[sum(((u>>j)&1)<<c for j,c in enumerate(C)) for u in range(1<<len(C))]
 for b in range(1<<len(J)):
  base=sum(((b>>j)&1)<<c for j,c in enumerate(J))
  yield tuple(v[base|off] for off in offsets)
pilot='--pilot' in sys.argv
seeds=[[1]] if pilot else [[1],[-1,1,1,1],[1,-1,-1,-1]]
rows=[];totalblocks=totalterm=0
for seed in seeds:
 v=root(seed);n=len(v).bit_length()-1;N=len(v);p=Q(1,8)
 H,I,amin,mu,_,_=stat(v);ck(I==amin)
 delta=Q(v.count(-1),N);ck(delta<=p)
 blockcount=termcount=0;mins={K:None for K in [Q(0),Q(15,4),Q(8)]}
 for A in range(1,(1<<n)-1):
  a=A.bit_count();d=n-a;reach=Q(1,1<<a)
  allchildren=list(children(v,A));groups=Counter(allchildren)
  ck(sum(groups.values())==1<<a)
  EH={};EI=Ea=Eq=Q(0);bank={K:{} for K in mins};negative={K:{} for K in mins}
  for ch,m in groups.items():
   h,i,aa,mm,D,Dp=stat(ch);weight=reach*m
   EH=add(EH,h,weight);EI+=weight*i;Ea+=weight*aa;Eq+=weight*(1-mm*mm)
   for K in bank:bank[K]=add(bank[K],D[K],-weight);negative[K]=add(negative[K],Dp[K],weight)
  ck(Eq<=4*delta);ck(EI<=I);ck(Ea<=EI)
  exact_bound=add(h2(4*p),{2:4*p*d});rational_bound=4*p*(d+3)
  ck(sgn(add(exact_bound,EH,-1))>=0)
  ck(sgn(add({2:rational_bound},exact_bound,-1))>=0)
  for K in bank:
   ck(bank[K]==add({2:K*Ea},EH,-1))
   ck(sgn(add({2:rational_bound},negative[K],-1))>=0)
   ck(sgn(add(bank[K],{2:rational_bound}))>=0)
   ck(sgn(add({2:K*I},bank[K],-1))>=0)
  blockcount+=1;termcount+=1<<a
 totalblocks+=blockcount;totalterm+=termcount
 ck(blockcount==(1<<n)-2);ck(termcount==3**n-1-(1<<n))
 rows.append({'seed':seed,'n':n,'original_blocks':blockcount,'complete_terminals':termcount,'I':str(I),'negative_mass':str(delta),'uniform_H_bank_error_bound':str(4*p*(n+3))})
 put('CHECKPOINT.json',{'completed_roots':len(rows),'assertions':checks,'rows':rows})
# Reconstruct the unconditional finite negative-bank fixture, without a giant table.
g=tuple([-1]+[1]*255);H,q,aa,mu,_,_=stat(g);K=Q(15,4)
ck(q==Q(1,16) and aa==q and mu==Q(127,128))
ck(sgn(add(H,{2:-K*q-Q(1,256)}))>0)
t=100000000;k=10000;n=8*t+4+k
payment=5*K/4-4-(13+6*k)*Q(128,128+t)
terminal=Q(t,256)-K*(1+2*k)-10*k-20
rootlower=Q(t,256)+4-K*2-K*2*k-10*k-20
bank_coefficient=4*(n+k)
I_upper_coefficient=t*q+2+2*k
ck(payment>0 and terminal>0 and rootlower>0)
ck(bank_coefficient<2**32);ck(K*I_upper_coefficient<2**32)
result={'status':'PASS','pilot':pilot,'assertions':checks,'roots':len(rows),'original_blocks':totalblocks,'complete_terminals':totalterm,'unique_tables_checked':stat.cache_info().currsize,'elapsed_seconds':time.perf_counter()-start,'rows':rows,'finite_scalar_certificate':{'seed':'point defect8','t':t,'k':k,'dimension':n,'K':str(K),'all_proper_optimized_child_banks_absolute_lt':'2^-9968','B_over_p':bank_coefficient,'KI_upper_over_p':str(K*I_upper_coefficient),'root_deficit_over_p_lower':str(rootlower),'all_four_explicit_terminal_deficits_over_p_lower':str(terminal),'paid_margin_over_p_lower':str(payment),'huge_power_or_table_computed':False}}
put('PILOT.json' if pilot else 'CHECK.json',result)
print(json.dumps({k:v for k,v in result.items() if k not in ['rows','finite_scalar_certificate']}))
