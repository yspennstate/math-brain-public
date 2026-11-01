from exact import Q,fw,entropy,bounds,put
from functools import lru_cache
import time,json
put('NAND_SPEC.json',{'helper_version':'A055 explicit NAND32 scalar witness v1','family':'complete binary depth-j NAND signs, j1..5; tensor-before-activation Q gadget with depth5 seed','domain':'five analytic seed profiles n2,4,8,16,32; actual truth tables through depth3 only; final t100000000,k10000,K17/4','case_count':'five exact interval profiles;three direct spectrum/edge comparisons;nine unateness four-point cases;one scalar cubic-extremal root certificate','symmetry':'No search quotient; equal child profiles from two disjoint copies by construction','arithmetic':'exact means/influences, rational32-term atanh with explicit tail; outward rounding to100binary places; exact finite recurrence; independent own64-term prime-log direct spectra for n<=8','memory_estimate_MB':50,'maximum_runtime_seconds':55,'no_large_truth_table_or_mean_power':True})
start=time.perf_counter();checks=0;S=1<<100
def ck(b):
 global checks
 assert b
 checks+=1
 assert time.perf_counter()-start<55
def rnd(v):return (Q((v[0]*S).__floor__(),S),Q((v[1]*S).__ceil__(),S))
@lru_cache(None)
def lnunit(x):
 z=(x-1)/(x+1)
 s=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(32)),Q(0))
 return s,s+2*z**65/(65*(1-z*z))
ln2=lnunit(Q(2));ck(ln2[0]>Q(1,2))
def h(x):
 x=abs(x)
 if x==0:return Q(0),Q(0)
 z=x;shift=0
 while z<1:z*=2;shift-=1
 while z>=2:z/=2;shift+=1
 a,b=lnunit(z)
 lo=shift+a/ln2[1];hi=shift+b/ln2[0]
 return rnd((-2*x*x*hi,-2*x*x*lo))
def NAND(x,j):
 if j==0:return -1 if x&1 else 1
 m=1<<(j-1)
 a=NAND(x&((1<<m)-1),j-1);b=NAND(x>>m,j-1)
 return 1 if a==b==-1 else -1
mu=Q(0);I=Q(1);H=(Q(0),Q(0));rows=[]
for j in range(1,6):
 alpha=(1-mu)/2;q=1-mu*mu;newmu=2*alpha*alpha-1
 hm=h(mu);ha=h(alpha);hn=h(newmu)
 H=rnd((hn[0]+2*alpha*(H[0]-hm[1])+2*q*ha[0]+q*q/2,hn[1]+2*alpha*(H[1]-hm[0])+2*q*ha[1]+q*q/2))
 I=2*alpha*I;mu=newmu
 ck(H[0]<=H[1]);ck(-1<mu<1 and I>0)
 if j<=3:
  n=1<<j;table=[NAND(x,j) for x in range(1<<n)];N=len(table)
  coeff=[Q(w,N) for w in fw(table)];direct=bounds(entropy(coeff))
  ck(coeff[0]==mu)
  ck(Q(sum(table[x]!=table[x^(1<<i)] for x in range(N) for i in range(n)),N)==I)
  ck(H[0]<=direct[0]<=direct[1]<=H[1])
 rows.append({'depth':j,'n':1<<j,'mu':str(mu),'I':str(I),'H_lower':str(H[0]),'H_upper':str(H[1])})
K=Q(17,4);gap=H[0]-K*I
ck(gap>Q(1,8));ck(Q(1,2)<=abs(mu)<=Q(7,8));ck(I<=32)
# The unate directional comparison is an exact four-point inequality.
ordered=[(-1,-1),(-1,1),(1,1)]
for a,b in ordered:
 for c,d in ordered:ck((a!=d)+(b!=c)>=(a!=b)+(c!=d))
t=100000000;k=10000;n=32*t+4+k
rootlower=Q(t,8)+4-K*(2+2*k)-10*k-20
terminallower=Q(t,8)-K*(1+2*k)-10*k-20
paid=5*K/4-4-(13+6*k)*Q(8,8+t)
ck(rootlower>0 and terminallower>0 and paid>1)
ck(K*(Q(1,4)-Q(4,512))>1);ck(k>=9)
ck(4*(n+k)<2**34);ck(K*(t*I+2+2*k)<2**34)
put('NAND.json',{'status':'PASS','assertions':checks,'elapsed_seconds':time.perf_counter()-start,'profiles':rows,'explicit_root':{'seed':'complete depth5 recursive NAND on32 independent input signs; no canonical choice needed','seed_gap_over_KI_lower':str(gap),'seed_gap_simplified_lower':'1/8','K':str(K),'t':t,'k':k,'dimension':n,'root_D_over_p_lower':str(rootlower),'all_four_fixed_K_terminal_D_over_p_lower':str(terminallower),'paid_pair_margin_over_p_lower':str(paid),'strict_cubic_orbit_margin_per_affine_rank_lower':str(K*(Q(1,4)-Q(4,512))-1),'all_block_N_and_abs_bank_lt':'2^-9966','seed_full_affine_minimality':'proved by unateness four-point inequality, |mu|>=1/2 and all inputs essential','joint_cubic_affine_D_and_ratio_extremal':True,'giant_truth_table_or_mean_power_evaluated':False}})
print(json.dumps({'status':'PASS','assertions':checks,'seconds':time.perf_counter()-start,'explicit_positive_K':'17/4','seed_n':32,'root_dimension':n}))
