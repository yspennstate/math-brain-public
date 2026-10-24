from reconstruct import F,fw,ck,add,scale,logq,product2,RUN,OUT
from itertools import product
import reconstruct as core
import json,time
def divergence(p,q):return add(*(scale(logq(m/q[s]),m) for s,m in p.items() if m))
def main():
    start=time.perf_counter(); cases=0
    for n in range(1,4):
        for word in range(1<<(1<<n)):
            if word.bit_count()!=1<<(n-1):continue
            table=[1 if word>>x&1 else -1 for x in range(1<<n)]
            pg={s:c*c for s,c in fw(table).items()};ck(not pg.get(0,0));ck(sum(pg.values())==1)
            for r in range(1,4):
                p=F(1,2**r); v=p*(2-p); beta=F(1,2-p); mask=(1<<r)-1
                activated=[1 if x&mask else table[x>>r] for x in range(1<<(r+n))]
                full={s:c*c for s,c in fw(activated).items() if s};P={s:q/v for s,q in full.items()}
                ck(sum(P.values())==1)
                for mode in ['uniform','biased-product']:
                    if mode=='uniform':Q={s:F(1,(1<<(r+n))-1) for s in range(1,1<<(r+n))}
                    else:
                        theta=[F(1,3) if j%2==0 else F(2,3) for j in range(r+n)]
                        empty=product2(*(1-t for t in theta))
                        Q={s:product2(*(t if s>>j&1 else 1-t for j,t in enumerate(theta)))/(1-empty) for s in range(1,1<<(r+n))}
                    ck(sum(Q.values())==1)
                    qt={};qc={}
                    for s,m in Q.items():
                        T=s>>r;U=s&mask;qt[T]=qt.get(T,0)+m;qc[(T,U)]=m
                    gamma=sum(q for T,q in qt.items() if T);qg={T:q/gamma for T,q in qt.items() if T}
                    binary=divergence({1:beta,0:1-beta},{1:gamma,0:1-gamma})
                    dg=divergence(pg,qg)
                    controls={}
                    uniform_nonempty={U:F(1,(1<<r)-1) for U in range(1,1<<r)}
                    q0={U:qc[(0,U)]/qt[0] for U in range(1,1<<r)}
                    controls=scale(divergence(uniform_nonempty,q0),v*(1-beta))
                    uniform_all={U:F(1,1<<r) for U in range(1<<r)}
                    for T,m in pg.items():
                        qT={U:qc[(T,U)]/qt[T] for U in range(1<<r)}
                        controls=add(controls,scale(divergence(uniform_all,qT),p*m))
                    left=scale(divergence(P,Q),v)
                    right=add(scale(binary,v),scale(dg,p),controls)
                    ck(left==right)
                    # Generalized reference scaled by 1/2 adds exactly v bits.
                    half={s:m/2 for s,m in Q.items()}
                    ck(scale(divergence(P,half),v)==add(right,{2:v}))
                    if mode=='uniform':ck(controls=={})
                    cases+=1
    result={'cases':cases,'assertions':core.N,'failures':0,'seconds':time.perf_counter()-start,'statement':'v D(Pplus||Q)=v D_Ber(beta||gamma)+p D(Pg||qg)+nonnegative control divergence; Q/2 adds v bits','arithmetic':'exact Fraction and prime-log linear forms'}
    (OUT/'BRIDGE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
