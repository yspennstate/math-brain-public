"""Frozen exact scalar and actual Boolean family checks; no search enlargement."""
import json,time
from pathlib import Path
import arith as A
import check as P
F=A.F
start=time.perf_counter(); cases=0
L3,L13,L15=(A.logq(x) for x in (3,13,15))
A.ck(3**9<13**4,'j0 negative base integer certificate')
A.ck(3**9>2**14,'L3 >14/9')
A.ck(13**4<2**15,'L13 <15/4')
A.ck(15**6>2**23,'L15 >23/6')
A.ck(13**3>2**11,'partial one-query bank >5/6')
for u in range(8):
    for j in range(3):
        # t=2 suffices to extract the local seed type; alpha endpoints.
        for alpha in (F(0),F(1)):
            e=P.ell_formula(2,u,j,alpha,F(1,2))
            A.ge(A.add(A.c(P.loss_bound(2,j)),A.scale(e,-1)),'all local seed types')
            cases+=1
for t in range(2,129):
    for d in range(3*(t//2)+3):
        A.ge(A.add(A.c(P.floor_bound(t,d)-P.loss_bound(t,d)),A.c(-F(13*t,576))),'same source rational reserve')
        cases+=1
witnesses=[]
for t in (2,3,4):
    n=3*t+1; N=2**n; delta=F(1,8**t)
    f=[]
    for X in range(N):
        x=X&((1<<(3*t))-1); z=X>>(3*t)
        b=(-1)**sum(((x>>(3*k))&7)==0 for k in range(t))
        f.append(b*(-1 if x==0 and z else 1))
    p=P.law(tuple(f)); influence=sum(F(s.bit_count())*q for s,q in enumerate(p))
    physical=sum(A.physical(tuple(f),i) for i in range(n))
    A.ck(influence==physical==F(3*t,4)-3*t*delta+delta,'actual Boolean family exact influence')
    A.ge(A.add(A.c(5*influence),A.scale(A.ent(p),-1)),'actual family H <5I')
    witnesses.append({'t':t,'dimension':n,'influence':str(influence),'charge':'log2(15)/8','entropy_upper':n,'fei_constant_upper':'224/45'})
    cases+=1
result={'status':'PASS','cases':cases,'assertions':A.count,'seconds':time.perf_counter()-start,'actual_boolean_family':witnesses}
(Path(__file__).resolve().parents[1]/'out/scalar.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
