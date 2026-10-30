import math
import random


def det3(rows):
    (a,b,c),(d,e,f),(g,h,i)=rows
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def mat_outer(v):
    return [[v[i]*v[j] for j in range(3)] for i in range(3)]


def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]


def scale(a,A):
    return [[a*A[i][j] for j in range(3)] for i in range(3)]


def check_rho(rho):
    p=math.sqrt(rho)
    q=math.sqrt(1-rho)
    sp=[1,p,0]
    sm=[1,-p,0]
    tp=[0,q,1]
    tm=[0,q,-1]
    values=[det3([sp,sm,tp])**2,det3([sp,sm,tm])**2,
            det3([sp,tp,tm])**2,det3([sm,tp,tm])**2]
    targets=[4*rho,4*rho,4*(1-rho),4*(1-rho)]
    assert max(abs(a-b) for a,b in zip(values,targets))<1e-10
    G=[[0.0]*3 for _ in range(3)]
    for r in (sp,sm,tp,tm):
        G=add(G,scale(0.5,mat_outer(r)))
    assert max(abs(G[i][j]-(1.0 if i==j else 0.0)) for i in range(3) for j in range(3))<1e-10
    if rho>=0.5:
        assert 2*rho*(1/8)*(1/8)>=1/64-1e-15
    if rho<=0.5:
        assert 2*(1-rho)*(1/8)*(1/8)>=1/64-1e-15


for rho in (1e-6,0.1,0.499,0.5,0.501,0.9,0.999999):
    check_rho(rho)

C_S=128*(32/3)**0.25
C_T=128*(16*math.sqrt(2)/3)**0.25
assert C_S<232 and C_T<232

for _ in range(10000):
    m23=random.uniform(-3,3)
    m33=random.uniform(-3,3)
    if abs(m23)+abs(m33)<1e-9:
        continue
    u=random.uniform(-5,5)
    v=random.uniform(-5,5)
    kappa=math.hypot(2*m23,m33)
    d0=abs(v)
    d1=abs(2*m23*u+m33*v)/kappa
    lhs=min(d0,d1)**2
    rhs=abs(v*(2*m23*u+m33*v))/kappa
    assert lhs<=rhs+1e-12

print('QFORM_B11_WEIGHTED_FOUR_RAY_NULL_RULING_CHECK_PASS')
print('C_S=',repr(C_S))
print('C_T=',repr(C_T))
print('global=',repr(max(24,C_S,C_T)))
print('ruled_pi_sqrt2=',repr(math.pi*math.sqrt(2)))
