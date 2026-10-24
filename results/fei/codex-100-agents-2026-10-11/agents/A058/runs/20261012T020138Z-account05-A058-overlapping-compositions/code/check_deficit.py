from pathlib import Path
import json,time
from check_coherent import walsh,table
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;count=0
def ck(c):
    global checks
    checks+=1
    if not c:raise AssertionError((count,checks))
b=[1,1,1,-1]
for m in [2,3]:
    M=1<<m;Nold=M*4;Nnew=Nold//2
    for ft in range(1<<M):
        F=table(ft,m)
        for row in range(M):
            for sign in [1,-1]:
                old=[];new=[]
                for x in range(Nold):
                    y=x&(M-1)
                    if sign<0:y^=2
                    if b[x>>m]<0:y^=row
                    old.append(F[y])
                for x in range(Nnew):
                    y=3*(x&1)+4*((x>>1)&((1<<(m-2))-1))
                    if sign<0:y^=2
                    if b[x>>(m-1)]<0:y^=row
                    new.append(F[y])
                wo,wn=walsh(old),walsh(new)
                Io=sum(a*a*S.bit_count() for S,a in enumerate(wo))
                In=4*sum(a*a*S.bit_count() for S,a in enumerate(wn))
                L=2*sum(a*a for S,a in enumerate(wo) if S&3==3)
                cross_degree=0
                for T in range(M):
                    if T&2:continue
                    U=(T&1)|((T>>2)<<1)
                    for S in range(4):
                        y=U+(S<<(m-1));i=T+(S<<m);j=(T^3)+(S<<m)
                        v,w=wo[i],wo[j]
                        ck(2*wn[y]==v+w)
                        cross_degree+=2*v*w*y.bit_count()
                ck(In-Io==cross_degree-L)
                # Lost frequency cardinality is exactly 2 for old private pair 11.
                projected=sum(a*a*(((S&1)^((S>>1)&1))+(S>>2).bit_count()) for S,a in enumerate(wo))
                ck(Io-projected==L)
                count+=1
ck(count==4224)
result={'status':'PASS','case_count':count,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'identity':'Delta I=sum delta physical_degree-2Pr(both old private labels selected)','implementation':'direct independent truth tables for original and merged cubes'}
(R/'out/deficit_results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
