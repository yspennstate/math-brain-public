import numpy as np, math
rng=np.random.default_rng(20260924)

CT=759375/2
H0SQ=1536*math.e**2
C0=CT/H0SQ
K4=C0/2
KUNIV=K4*4/81
KAVG=12*2*C0/81

assert abs(C0-33.45385114186288)<1e-12
assert abs(K4-16.72692557093144)<1e-12
assert abs(KUNIV-0.8260210158484661)<1e-12
assert abs(KAVG-9.912252190181594)<1e-12

max_id_err=0.0
min_positive_delta=1.0
checked_delta=0
for _ in range(5000):
    n=12
    M=rng.normal(size=(n,2))
    G=M.T@M
    w,V=np.linalg.eigh(G)
    U=M@V@np.diag(w**-0.5)@V.T
    d=rng.normal(size=n)
    idx=rng.choice(n,5,replace=False)
    k,r,s,t,u=map(int,idx)
    def p(i,j):
        return np.linalg.det(np.stack([U[i],U[j]]))
    def q(i,j):
        return p(i,j)**2
    def tau(a,b):
        return d[k]*q(a,b)+d[a]*q(k,b)+d[b]*q(k,a)
    lhs=q(k,t)*q(k,u)*tau(r,s)+q(k,r)*q(k,s)*tau(t,u)-q(k,s)*q(k,u)*tau(r,t)-q(k,r)*q(k,t)*tau(s,u)
    rhs=-2*d[k]*p(k,r)*p(k,s)*p(k,t)*p(k,u)*p(r,u)*p(s,t)
    err=abs(lhs-rhs)/(1+abs(lhs)+abs(rhs))
    max_id_err=max(max_id_err,err)

    lev=np.sum(U*U,axis=1)
    if lev.max()<=1/3+1e-12 and q(r,s)>1e-10:
        rest=[j for j in range(n) if j not in (k,r,s)]
        delta=np.linalg.det(U[rest].T@U[rest])
        if delta<=-1e-10:
            raise AssertionError('negative complement determinant')
        min_positive_delta=min(min_positive_delta,delta)
        checked_delta+=1
        if delta<=1e-12:
            raise AssertionError('q_rs positive but complement determinant numerically zero')

assert max_id_err<1e-12
assert checked_delta>100

dk=1.7
z1,z2,z3=-1.2,0.4,2.0
A1=-dk*(z1-z2)*(z1-z3)
A2=-dk*(z2-z1)*(z2-z3)
A3=-dk*(z3-z1)*(z3-z2)
for za,Aa,zb,Ab in [(z1,A1,z2,A2),(z1,A1,z3,A3),(z2,A2,z3,A3)]:
    val=Aa+Ab+dk*(za-zb)**2
    assert abs(val)<1e-12

print('QFORM_B13_R39_NATURAL_SUPPORT_CHECK_PASS')
print(f'C0={C0:.15f}')
print(f'K4={K4:.15f}')
print(f'KUNIV={KUNIV:.15f}')
print(f'KAVG={KAVG:.15f}')
print(f'max_fourpoint_identity_error={max_id_err:.3e}')
print(f'checked_positive_complements={checked_delta}')
print(f'minimum_sampled_positive_complement={min_positive_delta:.3e}')
