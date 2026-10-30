import math


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


def entropy(ps):
    return -sum(p*math.log2(p) for p in ps if p>0.0)


def gated_majority(n):
    assert n%2==1
    N=1<<n
    vals=[1 if x.bit_count()>n//2 else -1 for x in range(N)]
    hat=fwht(vals)
    mu=[a*a for a in hat]
    deg=[s.bit_count() for s in range(N)]
    Imaj=sum(mu[s]*deg[s] for s in range(N))
    W1=sum(mu[s] for s in range(N) if deg[s]==1)

    # Normalized squared spectrum of g(y,z)=1_{y=0} Maj_n(z):
    # gate-frequency B is uniform and independent of majority frequency A.
    unnormalized_q=[]
    a=0.0
    for B in (0,1):
        for s in range(N):
            if mu[s]>0.0:
                nu=0.5*mu[s]
                w=nu/(1+B+deg[s])
                unnormalized_q.append(w)
                a+=w
    q=[w/a for w in unnormalized_q]
    Hq=entropy(q)
    kappa=1/a-1

    j=0.5
    d=0.25+0.5*Imaj
    delta=d/j-0.5*math.log2(1/j)

    assert W1>=0.5-1e-12
    assert a>=5/24-1e-12
    assert kappa<=19/5+1e-12
    assert Hq>=5/24*math.log2(n)-1e-12
    assert abs(delta-Imaj)<1e-12
    assert abs(4*d-(1+2*Imaj))<1e-12
    return Imaj,W1,a,kappa,Hq,delta,4*d


def main():
    checks=0
    for n in (3,5,7,9,11,13,15):
        Imaj,W1,a,kappa,Hq,delta,curvature=gated_majority(n)
        checks+=6
        print(
            'n',n,
            'Imaj',f'{Imaj:.12f}',
            'W1',f'{W1:.12f}',
            'a',f'{a:.12f}',
            'kappa_harm',f'{kappa:.12f}',
            'H_Q',f'{Hq:.12f}',
            'depth_defect',f'{delta:.12f}',
            'mixed_curvature_sum',f'{curvature:.12f}'
        )
    print('checks',checks)
    print('PASS')


if __name__=='__main__':
    main()
