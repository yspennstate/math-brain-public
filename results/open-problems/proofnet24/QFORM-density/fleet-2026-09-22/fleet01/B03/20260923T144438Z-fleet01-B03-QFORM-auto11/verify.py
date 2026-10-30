#!/usr/bin/env python3
import math, random

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def check_crossblock(seed=260923, trials=5000):
    rng=random.Random(seed)
    for _ in range(trials):
        nl,nr=5,6
        a=rng.uniform(-2,2)
        if abs(a)<0.2: a=0.7
        sigma=rng.uniform(-2,2)
        if abs(sigma)<0.2: sigma=-0.8
        h=[rng.uniform(-2,2) for _ in range(nl)]
        u=[rng.uniform(-2,2) for _ in range(nl)]
        k=[rng.uniform(-2,2) for _ in range(nr)]
        v=[rng.uniform(-2,2) for _ in range(nr)]
        ell=rng.randrange(nl); r=rng.randrange(nr)
        hm=h[:ell]+h[ell+1:]; um=u[:ell]+u[ell+1:]
        km=k[:r]+k[r+1:]; vm=v[:r]+v[r+1:]
        A=dot(hm,hm); B=dot(um,um); C=dot(hm,um)
        D=dot(km,km); E=dot(vm,vm); F=dot(km,vm)
        alpha=sigma*u[ell]; beta=sigma*v[r]
        G=[[A+D,alpha*F,beta*C],[alpha*F,alpha*alpha*E,0.0],[beta*C,0.0,beta*beta*B]]
        lhs=det3(G)
        L=A*B-C*C; R=D*E-F*F
        rhs=sigma**4*u[ell]**2*v[r]**2*(B*R+E*L)
        if abs(lhs-rhs)>1e-8*max(1.0,abs(lhs),abs(rhs)):
            raise AssertionError((lhs,rhs,ell,r))

def check_right_special(seed=260924, trials=5000):
    rng=random.Random(seed)
    for _ in range(trials):
        n=7
        # Gram-Schmidt to make unit orthogonal v,q.
        v=[rng.uniform(-1,1) for _ in range(n)]
        nv=math.sqrt(dot(v,v)); v=[x/nv for x in v]
        q=[rng.uniform(-1,1) for _ in range(n)]
        proj=dot(q,v); q=[q[i]-proj*v[i] for i in range(n)]
        nq=math.sqrt(dot(q,q)); q=[x/nq for x in q]
        beta0=rng.uniform(-2,2); m=rng.uniform(0.2,2.0)
        k=[beta0*v[i]+m*q[i] for i in range(n)]
        r=rng.randrange(n)
        km=k[:r]+k[r+1:]; vm=v[:r]+v[r+1:]
        R=dot(km,km)*dot(vm,vm)-dot(km,vm)**2
        rhs=m*m*(1.0-v[r]**2-q[r]**2)
        if abs(R-rhs)>1e-8*max(1.0,abs(R),abs(rhs)):
            raise AssertionError((R,rhs,r))

if __name__ == '__main__':
    check_crossblock(); check_right_special()
    print('density_constant',3*math.sqrt(math.e))
    print('collision_constant',(24/5)*math.sqrt(math.pi)*math.exp(0.25))
    print('QFORM_B03_PIVOT_LEFT_RIGHT_SELECTOR_PASS')
