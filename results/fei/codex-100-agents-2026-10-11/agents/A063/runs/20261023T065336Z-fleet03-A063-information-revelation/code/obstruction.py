from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,importlib.util,time
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1];HP=R.parents[2]/'A039/runs/20261014T055326Z-fleet05-A039-projection-under-restrictions/code/mixed.py'
sp=importlib.util.spec_from_file_location('mixed',HP);M=importlib.util.module_from_spec(sp);sp.loader.exec_module(M);L=M.L
start=time.perf_counter();checks=0
def ck(b):
 global checks
 checks+=1
 assert b,checks
def meet(a,b):ck(a[0]<=b[1] and b[0]<=a[1])
def avg(v):return M.scale(F(1,2),M.sumiv(v))
def rank(rows,n):
 a=rows[:];r=0
 for c in range(n):
  pivot=next((j for j in range(r,n) if a[j]>>c&1),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r]
  for j in range(n):
   if j!=r and a[j]>>c&1:a[j]^=a[r]
  r+=1
 return r
pilot='--pilot' in sys.argv;domain=[6] if pilot else [4,6,8,10]
spec={'helper_version':'A039 mixed.py SHA256 '+hashlib.sha256(HP.read_bytes()).hexdigest(),'actual_Boolean_family':'selector of tensor quadratic bent gates versus the same gate on two parity blocks','parameter_domain':domain,'case_count':len(domain),'additional_cases':'rank(I+J) for r=2..40, exact F2 elimination','symmetry':'none; full source and both physical children','arithmetic':'integer Walsh/Fraction; rigorous rational log intervals; exact rational outcome probabilities','memory_estimate_MB':140,'maximum_runtime_seconds':60 if pilot else 300,'no_automatic_dimension_increase':True}
(R/'out'/('OBSTRUCTION_PILOT_SPEC.json' if pilot else 'OBSTRUCTION_SPEC.json')).write_text(json.dumps(spec,indent=2),encoding='utf-8',newline='\n')
for r in range(2,41):ck(rank([((1<<r)-1)^(1<<j) for j in range(r)],r)==r-(r%2))
out=[]
for n in domain:
 N=1<<n;r=n//2;U=sum(1<<(2*j) for j in range(r));V=sum(1<<(2*j+1) for j in range(r))
 dense=[(-1)**sum(((z>>(2*j))&1)*((z>>(2*j+1))&1) for j in range(r)) for z in range(N)]
 sparse=[(-1)**(((z&U).bit_count()%2)*((z&V).bit_count()%2)) for z in range(N)]
 tab=[dense[t>>1] if not(t&1) else sparse[t>>1] for t in range(2*N)]
 p,d,H,TC,S=M.info(tab);f0=M.info(dense);f1=M.info(sparse)
 ck(f0[0]==[F(1,N)]*N);ck(f1[0]==[F(1,4) if j in [0,U,V,U|V] else F(0) for j in range(N)])
 ck(f0[1]==f1[1]==[F(1,2)]*n);ck(d[1:]==[F(1,2)]*n)
 dx=(1-F(1,2**(r-r%2)))/2;ck(d[0]==dx)
 q=[(x,x) for x in L.product(d)];ts,qs,E,O,zero=M.step(tab,q,0)
 ck(ts==[dense,sparse]);ck(zero==0)
 # Direct normalization of the ACTUAL coherent channel under uniform erased Q.
 fused=[(x+y)/2 for x,y in zip(f0[0],f1[0])]
 pi=[sum((f[0][j]/(2*fused[j]*N) for j in range(N)),F(0)) for f in [f0,f1]]
 ck(pi==[F(N,N+4),F(4,N+4)])
 Oformula=M.scale(F(1,2),L.log2(F((N+4)**2,16*N)));meet(O,Oformula)
 J=M.sub(L.evalformal(L.ent(fused)),avg([f0[2],f1[2]]))
 inherited=avg([M.kl(f[0],q1) for f,q1 in zip([f0,f1],qs)])
 sigma=M.sub(avg([f0[3],f1[3]]),inherited);meet(sigma,M.plus(J,O))
 ck(sigma[0]>F(n-4,2));ck(J[1]<1);ck(O[0]>F(n-4,2))
 B=M.sub(H,L.evalformal(L.ent(fused)));ck(B[1]<=1)
 hm=L.evalformal(L.h(dx));Mroot=M.sumiv(L.evalformal(L.h(x)) for x in d);Mchild=(F(n),F(n));meet(M.sub(Mroot,Mchild),hm)
 if n>=6:ck(sigma[0]>hm[1])
 if n>=8:ck(O[0]>1)
 out.append({'n':n,'N':N,'d_x':str(dx),'reference_outcomes':[str(x) for x in pi],'actual_physical_information_J':M.enc(J),'spectral_erasure_B':M.enc(B),'reference_outcome_mismatch_O':M.enc(O),'conditional_erasure_KL_E':M.enc(E),'actual_positive_reset_sigma':M.enc(sigma),'marginal_entropy_loss':M.enc(hm),'source_full_KL':M.enc(TC),'children_full_H':[M.enc(f0[2]),M.enc(f1[2])],'children_fresh_KL':[M.enc(f0[3]),M.enc(f1[3])],'children_inherited_KL':[M.enc(M.kl(f[0],q1)) for f,q1 in zip([f0,f1],qs)]})
 L.log2.cache_clear();ck(time.perf_counter()-start<(60 if pilot else 300))
result={'status':'PASS','assertions':checks,'helper_assertions':M.checks,'cases':out,'seconds':time.perf_counter()-start,'all_dimensional_certificate':'two-bit exact Walsh tensor/parity pullback; pi=(N,4)/(N+4); sigma=J+O >=(n-4)/2; DeltaM<=1','not_refuted':['FEI','existence of a good query','payment from an unused original global influence owner']}
(R/'out'/('OBSTRUCTION_PILOT.json' if pilot else 'OBSTRUCTION.json')).write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
