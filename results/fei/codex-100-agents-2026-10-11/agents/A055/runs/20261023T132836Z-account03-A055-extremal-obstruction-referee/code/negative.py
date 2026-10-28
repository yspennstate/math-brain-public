from exact import Q,fw,entropy,add,sgn,put,enc
from pathlib import Path
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
put('NEGATIVE_SPEC.json',{'helper_version':'A055 two independent scope controls v1','family':'point3 cubic self-cancellation; activated two-data parity with k6 and explicit physical shear','domain':'two fixed roots dimensions3,8 and complete transformed roots','case_count':2,'symmetry':'none','arithmetic':'integer Walsh, physical edges, Fraction, prime-log vectors and rigorous rational atanh sign','memory_estimate_MB':40,'maximum_runtime_seconds':55,'helper_sha256':hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest()})
t=time.perf_counter();count=0
def ck(x):
 global count
 assert x
 count+=1
 assert time.perf_counter()-t<55
def stat(v):
 N=len(v);n=N.bit_length()-1
 a=[Q(w,N) for w in fw(v)]
 I=Q(sum(v[x]!=v[x^(1<<j)] for x in range(N) for j in range(n)),N)
 ck(I==sum(s.bit_count()*x*x for s,x in enumerate(a)))
 return entropy(a),I
K=Q(6);f=[-1]+[1]*7
H,I=stat(f);hc,ic=stat([1]*8)
delta=Q(1,8);gamma=Q(1,4)-4*delta
ck(gamma<0);ck(I==Q(3,4))
D=add(H,{2:-K*I});ck(sgn(D)<0);ck(sgn(add(add(hc,{2:-K*ic}),D,-1))>0)
# A genuinely rare root can fail raw joint-orbit maximality if not affine-minimal.
k=6;p=Q(1,1<<k)
v=[(-1)**((x&1)+((x>>1)&1)) if x>>2==0 else 1 for x in range(1<<(k+2))]
shear=[v[x^((x>>1)&1)] for x in range(len(v))]
h,i=stat(v);hs,is_=stat(shear)
ck(h==hs);ck(i==(k+2)*p);ck(is_==(k+1)*p)
ck(i-is_==p);ck(K*(Q(1,4)-4*p/2)>1)
gain=add(add(hs,{2:-K*is_}),add(h,{2:-K*i}),-1)
ck(gain=={2:K*p});ck(sgn(gain)>0)
put('NEGATIVE.json',{'status':'PASS','assertions':count,'elapsed_seconds':time.perf_counter()-t,'missing_rarity':{'n':3,'delta':str(delta),'gamma':str(gamma),'phase':'P=f cubic point3; fP=constant1','root_D':enc(D),'comparison_improves':True},'missing_affine_minimality':{'n':8,'k':6,'delta':str(p/2),'physical_I':str(i),'sheared_I':str(is_),'exact_D_gain':str(K*p),'strict_rarity_margin_holds':True}})
print(json.dumps({'status':'PASS','assertions':count,'seconds':time.perf_counter()-t}))
