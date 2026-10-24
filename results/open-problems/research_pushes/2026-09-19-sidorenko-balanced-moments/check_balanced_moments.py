"""Exact examples for the balanced-transfer moment inequality.

Python standard library only. All decisions use integers/Fraction arithmetic.
The general theorem is proved in BALANCED_MOMENTS.md; these are self-checks,
not an independent audit or a proof of the full Sidorenko conjecture.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, hashlib


def mm(A, B):
    cols=list(zip(*B))
    return [[sum((a*b for a,b in zip(row,col) if a and b),F(0))
             for col in cols] for row in A]


def mv(A, v):
    return [sum((a*b for a,b in zip(row,v)),F(0)) for row in A]


def tr(A):
    return sum((A[i][i] for i in range(len(A))),F(0))


def traces(A):
    A2=mm(A,A);A3=mm(A2,A);A4=mm(A2,A2)
    t5=sum((A4[i][j]*A[j][i] for i in range(len(A))
            for j in range(len(A))),F(0))
    return {2:tr(A2),3:tr(A3),4:tr(A4),5:t5}


def from_flow(Q):
    Q=[[F(x) for x in row] for row in Q]
    n=len(Q);r=[sum(row) for row in Q];Z=sum(r)
    assert all(r_i>0 for r_i in r)
    p=[r_i/Z for r_i in r]
    W=[[Z*Q[i][j]/(r[i]*r[j]) for j in range(n)] for i in range(n)]
    return W,p


def value_bound(t, beta, a):
    r2=t[2]-beta**2;r3=t[3]-beta**3;r4=t[4]-beta**4
    D=r3+a*r2;N=r4+a*r3
    assert D>=0
    if D:
        b=min(beta,max(F(0),N/D))
    else:
        assert N==0
        b=F(0)
    L=beta**5+(2*b-a)*r4+(2*a*b-b*b)*r3-a*b*b*r2
    # Second, independent polynomial expansion of the same expression.
    p_beta=beta**2*(beta-b)**2*(beta+a)
    L2=(2*b-a)*t[4]+(2*a*b-b*b)*t[3]-a*b*b*t[2]+p_beta
    assert L==L2 and 0<=b<=beta
    return L,b


def gram_check(C,p,T,z):
    n=len(p);pairs=list(product(range(n),repeat=2));N=n*n
    Z=sum(p[i]*z[i]**3 for i in range(n))
    pg=[p[i]*z[i]**3/Z for i in range(n)]
    cg={(i,j,k):Z*C[i,j,k]/(z[i]*z[j]*z[k]) for i,j,k in C}
    q={(i,j):sum(p[k]*C[i,j,k]*z[k]**2 for k in range(n))/(z[i]*z[j])
       for i,j in pairs}
    Tg=[[pg[k]*cg[i,j,k] if j==v else F(0) for v,k in pairs] for i,j in pairs]
    s=[z[i]*z[j]**2 for i,j in pairs]
    assert all(Tg[a][b]==T[a][b]*s[b]/s[a] for a in range(N) for b in range(N))
    mu=[pg[i]*pg[j] for i,j in pairs]
    G=[[mu[a]*Tg[a][b]+mu[b]*Tg[b][a]+(mu[a]*q[pairs[a]] if a==b else 0)
        for b in range(N)] for a in range(N)]
    S=[[F(0) for _ in range(N)] for _ in range(N)]
    for i,j,k in product(range(n),repeat=3):
        w=pg[i]*pg[j]*pg[k]*cg[i,j,k]/3
        assert w>=0
        ids=[i*n+j,j*n+k,k*n+i]
        for a in ids:
            for b in ids:S[a][b]+=w
    assert G==S
    return max(q.values())


def check_case(name,Q,z,steps,threshold):
    W,p=from_flow(Q);n=len(p);pairs=list(product(range(n),repeat=2))
    assert sum(p)==1
    assert all(W[i][j]>=0 and W[i][j]==W[j][i] for i,j in pairs)
    assert all(sum(p[j]*W[i][j] for j in range(n))==1 for i in range(n))
    C={(i,j,k):sum(p[u]*W[u][i]*W[u][j]*W[u][k] for u in range(n))
       for i,j,k in product(range(n),repeat=3)}
    T=[[p[k]*C[i,j,k] if j==v else F(0) for v,k in pairs] for i,j in pairs]
    ts=traces(T)
    active=[(u,i) for u,i in pairs if W[u][i]>0]
    nu=[p[u]*p[i]*W[u][i] for u,i in active]
    assert sum(nu)==1
    L=[[p[v]*p[j]*W[v][j]*W[u][j]*W[v][i] for v,j in active] for u,i in active]
    assert all(nu[i]*L[i][j]==nu[j]*L[j][i] for i in range(len(active))
               for j in range(len(active)))
    assert traces(L)==ts
    A=[[p[j]*W[i][j] for j in range(n)] for i in range(n)]
    beta0=tr(mm(mm(A,A),mm(A,A)))
    h=[F(1) for _ in active];lower_betas=[]
    for k in range(steps+1):
        hn=mv(L,h)
        beta=sum(nu[i]*h[i]*hn[i] for i in range(len(active)))/sum(nu[i]*h[i]**2 for i in range(len(active)))
        if k==0:assert beta==beta0 and beta>=1
        lower_betas.append(beta);h=hn
    beta=max(lower_betas)
    a0=gram_check(C,p,T,[F(1)]*n)/2
    a=gram_check(C,p,T,list(map(F,z)))/2
    bound,b=value_bound(ts,beta,a)
    unbalanced,_=value_bound(ts,beta,a0)
    # A direct cyclic contraction independently checks the trace identity.
    direct=F(0)
    for x in product(range(n),repeat=5):
        term=F(1)
        for k in range(5):term*=p[x[k]]*C[x[k],x[(k+1)%5],x[(k+2)%5]]
        direct+=term
    assert direct==ts[5]
    assert bound<=direct and bound>=threshold
    wp3=mm(mm(A,A),A)
    W3=[[wp3[i][j]/p[j] for j in range(n)] for i in range(n)]
    m2=sum(p[i]*p[j]*W[i][j]*W3[i][j]**2 for i,j in pairs)
    assert m2>=beta0**2
    delta=max(abs(W[i][j]-1) for i,j in pairs)
    result={'name':name,'n':n,'flow':Q,'gauge':list(map(str,z)),
            'weights':list(map(str,p)),'amplitude':str(delta),'beta0':str(beta0),
            'beta_used':str(beta),'krylov_steps':steps,'rayleigh_bounds':list(map(str,lower_betas)),
            'q_unbalanced':str(2*a0),'q_balanced':str(2*a),'b':str(b),
            'trace_moments':{str(k):str(v) for k,v in ts.items()},
            'bound':str(bound),'bound_without_balance':str(unbalanced),
            'certified_threshold':str(threshold),'threshold_margin':str(bound-threshold),
            'm2':str(m2),'direct_trace_identity':True,'cyclic_gram_identity':True,
            'algebraic_float_sign_tests':False}
    print(name+': EXACT PASS; bound >= '+str(threshold),flush=True)
    return result


def main():
    old=[[547845,22,30967151,932390],[22,27,5,2177],
         [30967151,5,870744517,32344047],[932390,2177,32344047,216028]]
    generic=[[32,1,2,3,4],[1,23,5,6,7],[2,5,18,8,9],[3,6,8,15,10],[4,7,9,10,12]]
    cases=[('constant',[[1,1],[1,1]],[1,1],0,F(1)),
           ('triangle_host',[[0,1,1],[1,0,1],[1,1,0]],[1,1,1],0,F(2)),
           ('old_offdiagonal_Gram_obstruction',old,
            [F(1),F(2143535544,10**8),F(99592757,10**8),F(101314111,10**8)],0,F(33,25)),
           ('generic_five_block',generic,[1]*5,0,F(39))]
    results=[check_case(*case) for case in cases]
    # An abstract nonnegative real-spectrum example: the lower-moment facts
    # alone do not imply the target. This is NOT a kernel-derived T.
    abstract=[F(1),F(-1,2),F(-1,2)]+[F(3,10)]*10
    ts={k:sum(x**k for x in abstract) for k in range(1,6)}
    assert ts[1]>=1 and ts[3]>1 and ts[4]>1 and ts[5]<1
    # It is realized by a stochastic triangle block and ten positive loops.
    assert ts[5]==F(4809,5000)
    out={'status':'ALL_EXACT_CHECKS_PASS','general_claim':'balanced-transfer quantitative lower bound',
         'full_Sidorenko_proof':False,'independent_audit':False,'cases':results,
         'abstract_not_a_kernel_transfer':{'eigenvalues':list(map(str,abstract)),
                                          'moments':{str(k):str(v) for k,v in ts.items()}},
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('balanced_moments_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print('ALL_EXACT_CHECKS_PASS')

if __name__=='__main__':main()
