import math
from fractions import Fraction

TOL=2e-10

def h2(x):
    if x<=0.0 or x>=1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def entropy(probs):
    return -sum(p*math.log2(p) for p in probs if p>0.0)

def fwht(vals):
    a=[float(x) for x in vals]
    n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y; a[j+h]=x-y
        h*=2
    return [x/n for x in a]

def analyze(vals,n):
    N=1<<n
    hat=fwht(vals)
    mu=[x*x for x in hat]
    deg=[s.bit_count() for s in range(N)]
    H=entropy(mu)
    I=sum(deg[s]*mu[s] for s in range(N))
    tau=sum(mu[s] for s in range(1,N))
    if tau<TOL:
        return 0
    r=[]
    card=0.0
    row_within=0.0
    checks=0
    for i in range(n):
        pi=sum(mu[s] for s in range(N) if (s>>i)&1)
        ri=sum(mu[s]/deg[s] for s in range(1,N) if (s>>i)&1)
        r.append(ri)
        if ri>TOL:
            q=[(s,mu[s]/(deg[s]*ri)) for s in range(1,N) if ((s>>i)&1) and mu[s]>0]
            kap=sum((deg[s]-1)*qq for s,qq in q)
            assert abs(ri*(1+kap)-pi) < TOL
            checks += 1
            level={}
            for s,qq in q:
                level[deg[s]-1]=level.get(deg[s]-1,0.0)+qq
            HL=entropy(level.values())
            assert HL <= 1+kap+TOL
            card += ri*HL
            checks += 1
            for ell,mass in level.items():
                if mass>0:
                    row_within += ri*mass*entropy([qq/mass for s,qq in q if deg[s]-1==ell])
    assert abs(sum(r)-tau)<TOL
    assert card <= I+TOL
    checks += 2
    Hmarker=entropy([x/tau for x in r if x>0])
    ElogK=sum(mu[s]*math.log2(deg[s]) for s in range(1,N))
    Rrow=row_within-ElogK
    levelmass={}
    for s in range(1,N):
        if mu[s]>0:
            levelmass[deg[s]]=levelmass.get(deg[s],0.0)+mu[s]
    H_S_given_K=0.0
    H_M_given_K=0.0
    for k,w in levelmass.items():
        H_S_given_K += (w/tau)*entropy([mu[s]/w for s in range(1,N) if deg[s]==k and mu[s]>0])
        mk=[]
        for i in range(n):
            z=sum(mu[s] for s in range(1,N) if deg[s]==k and ((s>>i)&1))/(k*w)
            if z>0:
                mk.append(z)
        H_M_given_K += (w/tau)*entropy(mk)
    Rdirect=tau*(H_S_given_K-H_M_given_K)
    assert abs(Rrow-Rdirect)<3e-10
    assert abs(H-(h2(tau)+tau*Hmarker+card+Rdirect))<3e-10
    checks += 2
    return checks

def majority_metrics(n):
    assert n%2==1
    N=1<<n
    vals=[]
    half=n//2
    for x in range(N):
        vals.append(1 if x.bit_count()>half else -1)
    hat=fwht(vals)
    mu=[x*x for x in hat]
    deg=[s.bit_count() for s in range(N)]
    r=sum(mu[s]/(deg[s]+1) for s in range(N))
    q=[mu[s]/((deg[s]+1)*r) for s in range(N)]
    H=entropy(q)
    kap=sum(deg[s]*q[s] for s in range(N))
    return H,kap,r

def main():
    funcs=0; checks=0
    for n in range(1,5):
        N=1<<n
        for bits in range(1<<(N-1)):
            vals=[1]
            for x in range(1,N):
                vals.append(-1 if ((bits>>(x-1))&1) else 1)
            funcs+=1
            checks+=analyze(vals,n)
    print('exhaustive_boolean_sign_normalized', funcs)
    print('exact_decomposition_and_cardinality_checks', checks)
    wallis_checks=0
    for m in range(1,501):
        a=Fraction(math.comb(2*m,m),4**m)
        assert a*a >= Fraction(1,4*m)
        W1=Fraction(2*m+1,1)*a*a
        assert W1 >= Fraction(1,2)
        wallis_checks += 2
    print('majority_exact_wallis_checks', wallis_checks)
    print('majority_local_target_analytic_bounds')
    for n in (3,11,51,201,401,1001):
        print('n',n,'H_Q_lower',f'{0.25*math.log2(n):.12f}','kappa_upper','3.000000000000')
    print('majority_actual_small_n')
    for n in (3,5,7,9,11,13,15):
        H,kap,r=majority_metrics(n)
        print('n',n,'H_Q',f'{H:.12f}','kappa',f'{kap:.12f}','r',f'{r:.12f}','H_minus_2k',f'{H-2*kap:.12f}')
    C=3+(2+math.exp(-1))/math.log(2)
    print('paid_constant_before_R_inc',f'{C:.15f}')
    print('PASS')

if __name__=='__main__':
    main()
