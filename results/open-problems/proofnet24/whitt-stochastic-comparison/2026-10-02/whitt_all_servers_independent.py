from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import factorial
from antivoter_independent_audit import solve
import json

def check(c,probs,means):
    p=list(map(F,probs));a=list(map(F,means));k=len(p);mu=[1/x for x in a]
    assert c>=2 and len(a)==k and sum(p)==1 and min(p)>0 and min(a)>0
    states=[(n,s)for n in range(c+1)for s in combinations_with_replacement(range(k),n)]
    states +=[(c+1,s)for s in combinations_with_replacement(range(k),c)]
    ix={s:i for i,s in enumerate(states)};d=len(states)
    Q0=[[F(0)for _ in range(d)]for _ in range(d)]
    Q1=[[F(0)for _ in range(d)]for _ in range(d)]
    for x,(n,phase)in enumerate(states):
        if n<c+1:
            Q1[x][x]-=1
            if n<c:
                for j in range(k):Q1[x][ix[(n+1,tuple(sorted(phase+(j,))))]]+=p[j]
            else:Q1[x][ix[(c+1,phase)]]+=1
        if n:
            for slot in range(len(phase)):
                rate=mu[phase[slot]];Q0[x][x]-=rate
                remain=phase[:slot]+phase[slot+1:]
                if n==c+1:
                    for j in range(k):Q0[x][ix[(c,tuple(sorted(remain+(j,))))]]+=rate*p[j]
                else:Q0[x][ix[(n-1,remain)]]+=rate
    lossQ1=[row.copy()for row in Q1]
    for x,(n,phase)in enumerate(states):
        if n==c:lossQ1[x]=[F(0)]*d
    assert all(sum(row)==0 for row in Q0+Q1+lossQ1)
    A=[[Q0[j][i]for j in range(d)]for i in range(d)];A[0]=[F(1)]*d
    def stationary_coefficients(up):
        out=[F(0)];vectors=[[F(1)]+[F(0)]*(d-1)]
        for order in range(1,c+2):
            prev=vectors[-1]
            rhs=[-sum(prev[j]*up[j][i]for j in range(d))for i in range(d)];rhs[0]=0
            cur=solve(A,rhs)
            assert sum(cur)==0
            assert all(sum(cur[j]*Q0[j][i]for j in range(d))==-sum(prev[j]*up[j][i]for j in range(d))for i in range(d))
            vectors.append(cur);out.append(sum(cur[i]for i,(n,phase)in enumerate(states)if n>=c))
        return out,vectors
    waiting,wvec=stationary_coefficients(Q1)
    loss,lvec=stationary_coefficients(lossQ1)
    assert wvec[:c+1]==lvec[:c+1]
    m=sum(p[i]*a[i]for i in range(k));size=[p[i]*a[i]/m for i in range(k)]
    n=c+1;expect=F(0)
    for labels in product(range(k),repeat=n):
        weight=F(1)
        for i in labels:weight*=size[i]
        rates=[mu[i]for i in labels];total=sum(rates)
        odds=[x/(total-x)for x in rates]
        ordered=sum(odds)**2-sum(x*x for x in odds)
        assert F(n,c)<=ordered<=2
        expect+=weight*ordered
    K=m**n*expect/(factorial(c)*n)
    baseline=m**n/(c*factorial(c));delta=K-baseline
    assert waiting[:c]==[F(0)]*c
    assert waiting[c]==m**c/factorial(c)
    assert waiting[c+1]==K-m**n/factorial(c)
    assert loss[c+1]==-m**n/factorial(c)
    assert waiting[c+1]-loss[c+1]==K
    assert (delta>0)==(min(a)<max(a))
    b=max(a);eps=None;excess=None
    if delta:
        eps=min(min(a)/2,delta*factorial(c)*c*b/(8*m**c*(c-1)*(b-m)))
        shortp=(b-m)/(b-eps);t=shortp*eps/m
        ev=F(0)
        for h in range(n+1):
            from math import comb
            weight=F(comb(n,h))*t**h*(1-t)**(n-h)
            if h==0:ordered=F(n,c)
            elif h==n:ordered=F(n,c)
            else:
                rf=b/((h-1)*b+(n-h)*eps)
                rs=eps/(h*b+(n-h-1)*eps)
                ordered=h*(h-1)*rf*rf+(n-h)*(n-h-1)*rs*rs+2*h*(n-h)*rf*rs
            assert F(n,c)<=ordered<=2
            ev+=weight*ordered
        excess=m**n*ev/(factorial(c)*n)-baseline
        assert 0<eps<min(a) and excess<=delta/4
    return {'servers':c,'classes':k,'state_count':d,'means':list(map(str,a)),'probabilities':list(map(str,p)),'waiting_coefficients':list(map(str,waiting)),'loss_next_coefficient':str(loss[c+1]),'K':str(K),'strict_excess':str(delta),'epsilon':None if eps is None else str(eps),'target_excess':None if excess is None else str(excess),'passed':True}

if __name__=='__main__':
    cases=[(c,[F(3,7),F(4,7)],[F(1,5),F(8,5)])for c in (2,3,4,6)]
    cases += [(3,[F(1,6),F(1,3),F(1,2)],[F(1,10),F(3,4),F(7,3)]),
              (3,[F(1,4),F(3,4)],[F(2),F(2)])]
    out=[]
    for case in cases:
        row=check(*case);out.append(row);print(json.dumps(row),flush=True)
    with open('/workspace/scratch/61b7096f9f41/whitt_all_servers_independent_checks.json','w')as f:json.dump(out,f,indent=2)
