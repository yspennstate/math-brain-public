from pathlib import Path
from fractions import Fraction as Q
from math import comb,isqrt
from functools import lru_cache
import json,time,hashlib

R=Path(__file__).resolve().parents[1];O=R/'out';O.mkdir(exist_ok=True)
FULL=(1,2,3,4,8,16);TOP=(1,2,3,4,8,16,32,64,128,256,512,1024)
spec={'helper':'A041-unbounded-jump-v1','family':'actual strict majority F_m=2*1{N_A+N_B>=m+1}-1, |A|=|B|=m','domains':{'full_fair_count_spectra':list(FULL),'top_atom_count_formulas':list(TOP),'direct_product_checks':'m=1,2,3,4 fair; m=3,4 at three additional prescribed labeled bias profiles','A045_review':'all proper retained counts r=1..2^d-2 at d=2,3,4,8; both endpoints at each d'},'case_count':{'full_count':6,'top_count':12,'direct':10,'admission_proper':276,'admission_endpoints':8},'symmetry':'exact permutation symmetry inside each group for FAIR count formulas only; direct product checks retain labels','arithmetic':'integers and Fraction; natural-log intervals from 20-term atanh with rigorous remainder','memory_estimate_MB':120,'maximum_runtime_seconds':60,'targets':['top P/Kstar unbounded','actual averaged positive log coherence <=3D and complete Cstar<28D on the fair family','source admission theorem scope']}
src=R.parent/'20261014T083216Z-fleet05-A041-weighted-threshold-fei/code/check_stage.py'
source=src.read_text(encoding='utf-8');spec['direct_helper_sha256']=hashlib.sha256(source.encode()).hexdigest()
(O/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8',newline='\n')
ns={'__file__':str(__file__)};exec(compile(source.split('parser=')[0],str(src),'exec'),ns)
transform=ns['transform'];reference=ns['reference'];ln=ns['ln'];start=time.monotonic();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def C(n,k):return comb(n,k) if 0<=k<=n else 0
@lru_cache(None)
def tail(n,k,u):
 if not 1<=k<=n:return Q(0)
 if u==0:return Q(2*sum(C(n,l) for l in range(k,n+1)),2**n)-1
 return Q(sum((-1)**(u-1-l)*C(u-1,l)*C(n-u,k-1-l) for l in range(u)),2**(n-1))
def top_record(m):
 weights=[C(m-1,d)*C(m,m-1-d) for d in range(m)]
 V=C(2*m-1,m-1);S=sum(x*x for x in weights);ck(sum(weights)==V)
 L=Q(V*V,S);qm=Q(max(weights),V)
 ck(qm*qm<=Q(16,m));ck(Q(S,V*V)<=qm);ck(L*L>=Q(m,16));ck(L<=m)
 return {'m':m,'ratio_P_Kstar':str(L),'ratio_squared_lower':str(Q(m,16)),'collision':str(Q(S,V*V)),'max_hypergeometric_atom':str(qm),'coefficient_list_sha256':hashlib.sha256(','.join(map(str,weights)).encode()).hexdigest()}
tops=[top_record(m) for m in TOP]
full=[]
for m in FULL:
 n=2*m;V=Q(C(2*m,m),4**m);I=2*m*V
 ck(V*V>=Q(1,4*m));ck(I*I>=m)
 atom=Q(max(C(m,k) for k in range(m+1)),2**m);ck(atom<=Q(1,2))
 matrices={};M=D=Z=I_mix=I_pure=Q(0);GammaL=GammaU=CL=CU=EL=EU=Q(0)
 for u in range(m+1):
  for t in range(m+1):
   P=tail(n,m+1,u+t)**2;mult=C(m,u)*C(m,t)
   if not u or not t:
    if u+t:I_pure+=mult*(u+t)*P
    continue
   alphas=[(tail(m,m+1-j,t)-tail(m,m+2-j,t))/2 for j in range(1,m+1)]
   betas=[(tail(m,m+1-j,u)-tail(m,m+2-j,u))/2 for j in range(1,m+1)]
   KA=sum(alphas[j-1]**2*tail(m,j,u)**2 for j in range(1,m+1))
   KB=sum(betas[j-1]**2*tail(m,j,t)**2 for j in range(1,m+1))
   K=max(KA,KB);ck(KA<=1 and KB<=1);ck(P<=m*K)
   matrices[u,t]=(P,KA,KB)
   M+=mult*P;D+=mult*(u+t-1)*P;I_mix+=mult*(u+t)*P;Z+=mult*K
   if P:
    ck(K>0)
    l,h=ln(1/P);EL+=mult*P*l;EU+=mult*P*h
    l,h=ln(1/K);CL+=mult*P*l;CU+=mult*P*h
    if P>K:
     l,h=ln(P/K);GammaL+=mult*P*l;GammaU+=mult*P*h
 ck(I_pure+I_mix==I);ck(I_pure<=atom*I);ck(I_mix>=I/2)
 ck(M<=I_mix/2);ck(D==I_mix-M);ck(D>=I/4);ck(16*D*D>=m)
 ck(Z<=D+M);ck(GammaU<3*D);ck(CU<28*D)
 ck(matrices[m,m][0]==V*V)
 top=next(x for x in tops if x['m']==m)
 ck(matrices[m,m][0]/max(matrices[m,m][1:])==Q(top['ratio_P_Kstar']))
 # Complete ordinary-KL identity, including every off-support K atom in Z.
 KLL=KLU=Q(0)
 for (u,t),(P,KA,KB) in matrices.items():
  if P:
   K=max(KA,KB);mult=C(m,u)*C(m,t);q=P*Z/(M*K)
   ck((1/K)*(Z/M)/q==1/P)
   l,h=ln(q);KLL+=mult*P*l/M;KLU+=mult*P*h/M
 ck(KLL>=0)
 def interval(lo,hi):
  scale=1<<80
  return [str(Q((lo*scale).__floor__(),scale)),str(Q((hi*scale).__ceil__(),scale))]
 full.append({'m':m,'M':str(M),'D':str(D),'I':str(I),'I_pure':str(I_pure),'Zstar':str(Z),'Gamma_over_D_interval':interval(GammaL/D,GammaU/D),'Cstar_over_D_interval':interval(CL/D,CU/D),'E_mix_over_D_interval':interval(EL/D,EU/D),'ordinary_KL_interval':interval(KLL,KLU),'matrix':{f'{u},{t}':list(map(str,x)) for (u,t),x in matrices.items()}})
 ck(time.monotonic()-start<60)
direct=[]
for m in (1,2,3,4):
 profiles=[(Q(1,2),)*(2*m)]
 if m>=3:profiles +=[(Q(1,4),)*(2*m),(Q(1,16),)*m+(Q(1,2),)*m,tuple(Q(1,4) if i%2 else Q(3,4) for i in range(2*m))]
 for p in profiles:
  vals=[2*int(x.bit_count()>=m+1)-1 for x in range(1<<(2*m))]
  _,P,v=transform(vals,p);KA,JA=reference(vals,p,m,'A');KB,JB=reference(vals,p,m,'B')
  V=C(2*m-1,m-1);S=sum((C(m-1,d)*C(m,m-1-d))**2 for d in range(m))
  scale=v[-1]/4**(2*m-1)
  ck(P[-1]==scale*V*V);ck(KA[-1]==scale*S);ck(KB[-1]==scale*S)
  if all(q==Q(1,2) for q in p):
   f=next(x for x in full if x['m']==m)
   for s,z in enumerate(P):
    u=(s&((1<<m)-1)).bit_count();t=(s>>m).bit_count()
    ck(z==tail(2*m,m+1,u+t)**2)
    if u and t:ck([str(z),str(KA[s]),str(KB[s])]==f['matrix'][f'{u},{t}'])
  direct.append({'m':m,'p':list(map(str,p)),'top_P':str(P[-1]),'top_Kstar':str(KA[-1]),'exact_ratio':str(Q(V*V,S))})
 ck(time.monotonic()-start<60)
admission=[]
for d in (2,3,4,8):
 a=2**(d-1)
 for r in range(1,2*a-1):
  N=(a-1)**2+r;q=Q((a-1)**2,N)
  ck((a-1)**2<N<a*a);ck(isqrt(N)**2!=N)
  ck(isqrt(q.numerator)**2!=q.numerator or isqrt(q.denominator)**2!=q.denominator)
  admission.append({'d':d,'r':r,'empty_mass':str(q),'denominator':N})
 ck(Q((a-1)**2,(a-1)**2)==1)
 ck(Q((a-1)**2,(a-1)**2+2*a-1)==Q((a-1)**2,a*a))
ck(Q(56,81)+Q(1,540)<Q(25,36)) # rigorous ln2 upper via z=1/3, first two terms+tail
ck(Q(1)+Q(1)+Q(1,2)+Q(1,6)==Q(8,3))
elapsed=time.monotonic()-start;ck(elapsed<60)
out={'helper':spec['helper'],'assertions':checks,'runtime_seconds':elapsed,'full_count_cases':len(full),'top_formula_cases':len(tops),'direct_cases':len(direct),'admission_proper_cases':len(admission),'admission_endpoint_cases':8,'top_records':tops,'full_records':full,'direct_records':direct,'admission_records':admission,'scope':'pointwise obstruction all interior biases; averaged/full reference payment proved only for the fair balanced split family; full FEI OPEN'}
(O/'EXACT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('top_records','full_records','direct_records','admission_records')}))
