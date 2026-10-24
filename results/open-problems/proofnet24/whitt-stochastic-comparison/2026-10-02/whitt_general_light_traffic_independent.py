from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from antivoter_independent_audit import solve
import json

def check(probs,means):
    p=list(map(F,probs));a=list(map(F,means));k=len(p)
    assert len(a)==k and sum(p)==1 and min(p)>0 and min(a)>0
    mu=[1/x for x in a]
    pairs=list(combinations_with_replacement(range(k),2))
    states=[(0,())]+[(1,(i,))for i in range(k)]+[(n,pair)for n in (2,3)for pair in pairs]
    ix={s:i for i,s in enumerate(states)};d=len(states)
    Q0=[[F(0)for _ in range(d)]for _ in range(d)]
    Q1=[[F(0)for _ in range(d)]for _ in range(d)]
    for x,(n,phase) in enumerate(states):
        if n<3:
            Q1[x][x]-=1
            if n<2:
                for j in range(k):
                    to=(n+1,tuple(sorted(phase+(j,))))
                    Q1[x][ix[to]]+=p[j]
            else:
                Q1[x][ix[(3,phase)]]+=1
        if n:
            for slot in range(len(phase)):
                rate=mu[phase[slot]]
                Q0[x][x]-=rate
                remain=phase[:slot]+phase[slot+1:]
                if n==3:
                    for j in range(k):
                        to=(2,tuple(sorted(remain+(j,))))
                        Q0[x][ix[to]]+=rate*p[j]
                else:
                    Q0[x][ix[(n-1,remain)]]+=rate
    assert all(sum(row)==0 for row in Q0+Q1)
    A=[[Q0[j][i]for j in range(d)]for i in range(d)]
    A[0]=[F(1)]*d
    coeff=[F(0)];prev=[F(1)]+[F(0)]*(d-1)
    for order in range(1,4):
        rhs=[-sum(prev[j]*Q1[j][i]for j in range(d))for i in range(d)]
        rhs[0]=0
        cur=solve(A,rhs)
        assert sum(cur)==0
        assert all(sum(cur[j]*Q0[j][i]for j in range(d))==-sum(prev[j]*Q1[j][i]for j in range(d))for i in range(d))
        coeff.append(sum(cur[i]for i,(n,phase) in enumerate(states)if n>=2))
        prev=cur
    m=sum(p[i]*a[i]for i in range(k));size=[p[i]*a[i]/m for i in range(k)]
    K=m**3*sum(size[i]*size[j]*size[l]*a[i]**2/((a[i]+a[j])*(a[i]+a[l]))for i,j,l in product(range(k),repeat=3))
    delta=K-m**3/4
    assert coeff==[F(0),F(0),m*m/2,K-m**3/2]
    assert (delta>0)==(min(a)<max(a))
    eps=None;targetdelta=None
    if delta:
        b=max(a)
        eps=min(min(a)/2,b*delta/(m*m*(b-m)))
        targetdelta=eps*b*m*(b-m)*(m-eps)/(4*(b+eps)**2)
        assert 0<eps<min(a) and targetdelta<=delta/4
    return {'means':list(map(str,a)),'probabilities':list(map(str,p)),'coefficients':list(map(str,coeff)),'K':str(K),'Delta':str(delta),'epsilon':None if eps is None else str(eps),'target_Delta':None if targetdelta is None else str(targetdelta),'passed':True}

cases=[([F(3,7),F(4,7)],[F(1,5),F(8,5)]),
       ([F(1,6),F(1,3),F(1,2)],[F(1,10),F(3,4),F(7,3)]),
       ([F(1,4)]*4,[F(1,3),F(2,3),F(5,4),F(3)]),
       ([F(1,5),F(1,5),F(3,5)],[F(2),F(2),F(2)])]
if __name__=='__main__':
    out=[check(*case)for case in cases]
    print(json.dumps(out,indent=2))
    with open('/workspace/scratch/61b7096f9f41/whitt_general_light_traffic_independent_checks.json','w')as f:json.dump(out,f,indent=2)
