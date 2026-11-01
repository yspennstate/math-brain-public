import itertools, math
import numpy as np
import mpmath as mp


def e2_singular_sq(C):
    s=np.linalg.svd(C,compute_uv=False)
    ss=s*s
    return sum(ss[i]*ss[j] for i in range(len(ss)) for j in range(i+1,len(ss)))


def e2_minors(C):
    m,n=C.shape
    total=0.0
    for I in itertools.combinations(range(m),2):
        for J in itertools.combinations(range(n),2):
            total += np.linalg.det(C[np.ix_(I,J)])**2
    return total

rng=np.random.default_rng(20260924)
max_schur_rel=0.0
max_cb_rel=0.0
for _ in range(1000):
    n=7
    M=rng.normal(size=(n,n))
    A=(M+M.T)/2
    h=0
    if abs(A[h,h])<0.2:
        A[h,h]+=1.25
    a=A[h,h]
    R=list(range(1,n))
    b=A[R,h]
    D=A[np.ix_(R,R)]
    S=D-np.outer(b,b)/a
    pick=rng.choice(len(R),4,replace=False)
    I=tuple(pick[:2]); J=tuple(pick[2:])
    rows=[h]+[R[i] for i in I]
    cols=[h]+[R[j] for j in J]
    lhs=np.linalg.det(A[np.ix_(rows,cols)])
    rhs=a*np.linalg.det(S[np.ix_(I,J)])
    max_schur_rel=max(max_schur_rel,abs(lhs-rhs)/(1+abs(lhs)+abs(rhs)))
    cb1=e2_singular_sq(S)
    cb2=e2_minors(S)
    max_cb_rel=max(max_cb_rel,abs(cb1-cb2)/(1+cb2))

# Exact random-bipartition expectation E e2(S[Y,Z])=D2(S)/16.
m=6
M=rng.normal(size=(m,m)); S=(M+M.T)/2
subs=list(itertools.combinations(range(m),2))
D2=0.0
for I in subs:
    for J in subs:
        if set(I).isdisjoint(J):
            D2 += np.linalg.det(S[np.ix_(I,J)])**2
vals=[]
for mask in range(1<<m):
    Y=[i for i in range(m) if (mask>>i)&1]
    Z=[i for i in range(m) if not ((mask>>i)&1)]
    vals.append(e2_minors(S[np.ix_(Y,Z)]))
partition_error=abs(float(np.mean(vals))-D2/16)

# Constants and stress family.
B18=mp.beta(mp.mpf(1)/8,mp.mpf(1)/8)
K1=mp.sqrt(mp.e)*2**(-mp.mpf(7)/4)*B18
K32=mp.sqrt(mp.e)*2**(-mp.mpf(7)/4)*(mp.mpf(3)/2)**(-mp.mpf(1)/4)*mp.beta(mp.mpf(1)/8,mp.mpf(1)/24)

stress=[]
for r in (2,4,8):
    m=2*r
    U=np.vstack([np.eye(r),np.eye(r)])/math.sqrt(2)
    for eps in (1e-2,1e-8):
        sv=np.array([2.0,2.0]+[eps]*(r-2))
        C=U@np.diag(sv)@U.T
        leverage=float(np.max(np.diag(U@U.T)))
        E2=e2_singular_sq(C)
        E2_exact=16+8*(r-2)*eps**2+math.comb(r-2,2)*eps**4
        A=np.zeros((1+2*m,1+2*m))
        A[0,0]=1
        A[1:1+m,1+m:]=C
        A[1+m:,1:1+m]=C.T
        eig=np.linalg.eigvalsh(A)
        count=int(np.sum(np.abs(eig)>=1-1e-10))
        stress.append((r,eps,leverage,E2,E2_exact,count,float(np.min(eig)),float(np.max(eig))))
        assert leverage <= 0.5+1e-12
        assert abs(E2-E2_exact) <= 1e-10*(1+E2_exact)
        assert count >= 3

partner=3*12**(-1/3)
print(f'max_schur_minor_relative_error={max_schur_rel:.3e}')
print(f'max_cauchy_binet_e2_relative_error={max_cb_rel:.3e}')
print(f'random_partition_identity_abs_error={partition_error:.3e}')
print(f'Beta(1/8,1/8)={float(B18):.15f}')
print(f'K_q(q=1)={float(K1):.15f}')
print(f'K_q(q=3/2)={float(K32):.15f}')
print(f'stress_uniform_bound_q1={float(K1/(16**(mp.mpf(1)/8))):.15f}')
for row in stress:
    print('stress',row)
print(f'partner_bound_Kdiag_6_2_1={partner:.15f}')
assert max_schur_rel < 1e-12
assert max_cb_rel < 1e-12
assert partition_error < 1e-12
print('ALL_ASSERTIONS_PASSED')
