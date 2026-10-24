import numpy as np
from math import sqrt, log, e

rng=np.random.default_rng(43)

def counts(M):
    z=np.linalg.eigvalsh(M)
    return int(np.sum(z>=1-1e-10)), int(np.sum(z<=-1+1e-10))

viol=0
tests=0
minimum=10**9
for n in range(5,13):
    for case in ('five','fourpos','fourneg'):
        for _ in range(100):
            Z=rng.normal(size=(n,n))
            U,_=np.linalg.qr(Z)
            lam=rng.uniform(-0.8,0.8,size=n)
            if case=='five':
                I=rng.choice(n,5,replace=False)
                lam[I]=rng.choice([-1,1],size=5)*rng.uniform(1.2,3,size=5)
            elif case=='fourpos':
                I=rng.choice(n,4,replace=False)
                lam[I]=rng.uniform(1.2,3,size=4)
            else:
                I=rng.choice(n,4,replace=False)
                lam[I]=-rng.uniform(1.2,3,size=4)
            A=U@np.diag(lam)@U.T
            p,q=counts(A)
            if case=='five' and p+q<5:
                continue
            for i in range(n):
                B=np.delete(np.delete(A,i,axis=0),i,axis=1)
                pp,qq=counts(B)
                minimum=min(minimum,pp+qq)
                tests+=1
                viol += (pp+qq<3)

partner=34*sqrt(log(e*2**40))
print('deletion_tests =',tests)
print('violations =',viol)
print('minimum_large_count_after_deletion =',minimum)
print('partner_2^-40_bound =',repr(partner))
assert viol==0
assert minimum>=3
assert partner<183
print('QFORM_B19_R43_CHECK_PASS')
