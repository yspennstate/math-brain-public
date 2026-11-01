from collections import defaultdict
from math import factorial

CASES = [(3,24),(4,18)]


def event_dists(n,K):
    ds=[]
    dist={tuple([0]*n):1}
    ds.append(dist)
    for _ in range(K):
        nxt=defaultdict(int)
        for a,c in dist.items():
            for i in range(n):
                b=list(a)
                if i==0 or a[i-1]>a[i]:
                    b[i]+=1
                nxt[tuple(b)]+=c
        dist=dict(nxt)
        ds.append(dist)
    return ds


def check_case(n,K):
    ds=event_dists(n,K)
    facts=[factorial(k) for k in range(K+1)]
    checks=0
    for k1 in range(K+1):
        A=list(ds[k1].items())
        for k2 in range(k1,K+1):
            B=list(ds[k2].items())
            km=(k1+k2)//2
            kp=(k1+k2+1)//2
            dm,dp=ds[km],ds[kp]
            for a,ca in A:
                for b,cb in B:
                    sums=tuple(x+y for x,y in zip(a,b))
                    if any(s&1 for s in sums):
                        continue
                    m=tuple(s//2 for s in sums)
                    # Exact inequality for H_n(k,a)=C_{n,k}(a)/k!:
                    # H(k1,a)H(k2,b) <= H(km,m)H(kp,m).
                    lhs=ca*cb*facts[km]*facts[kp]
                    rhs=dm.get(m,0)*dp.get(m,0)*facts[k1]*facts[k2]
                    checks += 1
                    if lhs > rhs:
                        raise AssertionError((n,k1,a,ca,k2,b,cb,km,kp,m,dm.get(m,0),dp.get(m,0),lhs,rhs))
    return checks,max(len(d) for d in ds)


if __name__ == '__main__':
    total=0
    for n,K in CASES:
        checks,max_states=check_case(n,K)
        total += checks
        print(f'n={n}, k<= {K}: joint floor/ceil clock-kernel midpoint inequalities={checks}; max_states={max_states}; PASS')
    print(f'TOTAL_EXACT_JOINT_CHECKS={total}')
    print('SELF-CHECK ONLY: bounded enumeration is evidence for the joint-kernel route, not a proof for n>=3.')
    print('ALL_EXACT_P0281_JOINT_DMLC_CHECKS_PASS')
