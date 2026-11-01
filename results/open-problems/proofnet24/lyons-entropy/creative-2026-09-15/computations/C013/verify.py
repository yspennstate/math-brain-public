"""C013: exact rational checks and independent full-Hessian diagnostics.

Standard library only.  Analytic proofs are in agents/C013.md.
"""
import itertools
import json
import math
import random
from fractions import Fraction as F
from explore import inv, eig

PERMS = list(itertools.permutations(range(3)))
SIGNS = [(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in PERMS]

def detpoly(K,A,mask):
    out=[0j]*4
    for perm,sign in zip(PERMS,SIGNS):
        v=[complex(sign)]
        for i,j in enumerate(perm):
            a=K[i][j]-(1 if i==j and not(mask>>j&1) else 0)
            b=A[i][j]
            z=[0j]*(len(v)+1)
            for k,x in enumerate(v):z[k]+=a*x;z[k+1]+=b*x
            v=z
        for k,x in enumerate(v):out[k]+=x
    sign=(-1)**(3-mask.bit_count())
    assert max(abs(z.imag) for z in out)<1e-8
    return [sign*z.real for z in out]

def adj(A):
    out=[[0j]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rows=[k for k in range(3) if k!=j]
            cols=[k for k in range(3) if k!=i]
            out[i][j]=(-1)**(i+j)*(A[rows[0]][cols[0]]*A[rows[1]][cols[1]]-A[rows[0]][cols[1]]*A[rows[1]][cols[0]])
    return out

def dot(A,B):return sum((A[i][j]*B[j][i]).real for i in range(3) for j in range(3))
def add(A,B):return [[A[i][j]+B[i][j] for j in range(3)] for i in range(3)]
def zero():return [[0j]*3 for _ in range(3)]

def basis():
    out=[]
    for i in range(3):
        a=zero();a[i][i]=1;out.append(a)
    for i,j in [(0,1),(0,2),(1,2)]:
        a=zero();a[i][j]=a[j][i]=1;out.append(a)
        a=zero();a[i][j]=1j;a[j][i]=-1j;out.append(a)
    return out

def curv(K,A):
    jets=[detpoly(K,A,s) for s in range(8)]
    p=[v[0] for v in jets]
    fi=sum(v[1]**2/v[0] for v in jets)
    h=-fi-sum(2*v[2]*math.log(v[0]) for v in jets)
    cs=[math.log(p[1<<j]*p[1<<k]/(p[0]*p[(1<<j)|(1<<k)])) for j,k in [(1,2),(0,2),(0,1)]]
    tau=math.log(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
    M=[[tau*K[i][j]+(cs[i] if i==j else 0) for j in range(3)] for i in range(3)]
    alt=-fi+2*dot(M,adj(A))
    return h,fi,p,cs,tau,abs(h-alt)

def hessian(K):
    bs=basis();ds=[curv(K,a)[0] for a in bs];H=[[0.]*9 for _ in range(9)]
    for i in range(9):
        H[i][i]=ds[i]
        for j in range(i):H[i][j]=H[j][i]=(curv(K,add(bs[i],bs[j]))[0]-ds[i]-ds[j])/2
    return H

def family(u,epsilon,diag):
    a,b,c=diag
    phase=complex(1-(1+u)*epsilon/2,math.sqrt(u*epsilon-(1+u)**2*epsilon**2/4))
    L=[[a,math.sqrt(a*b*(1-u)),math.sqrt(a*c*(1-u))],
       [math.sqrt(a*b*(1-u)),b,math.sqrt(b*c)*phase],
       [math.sqrt(a*c*(1-u)),math.sqrt(b*c)*phase.conjugate(),c]]
    J=inv([[L[i][j]+int(i==j) for j in range(3)] for i in range(3)])
    return [[int(i==j)-J[i][j] for j in range(3)] for i in range(3)]

def tau_zero_general(ui,diag):
    # ui indexed by complementary site; normalized edges 12,23,31.
    from explore import state
    return state([1-ui[2],1-ui[0],1-ui[1]],diag)

def marg(p,i):
    j,k=[z for z in range(3) if z!=i]
    x=p[0]+p[1<<i]
    y=p[1<<j]+p[(1<<j)|(1<<i)]
    z=p[1<<k]+p[(1<<k)|(1<<i)]
    w=p[(1<<j)|(1<<k)]+p[7]
    return x,y,z,w

def atom_budget(p):
    cs=[math.log(p[1<<j]*p[1<<k]/(p[0]*p[(1<<j)|(1<<k)])) for j,k in [(1,2),(0,2),(0,1)]]
    m=min(cs)
    T=[(y+z)/(2*math.sqrt(x*w)) for x,y,z,w in [marg(p,i) for i in range(3)]]
    costs=[(c-m)/(2*(1+t)) for c,t in zip(cs,T)]
    mean=sum(s.bit_count()*p[s] for s in range(8))
    var=sum(s.bit_count()**2*p[s] for s in range(8))-mean*mean
    return {'m':m,'F':sum(costs),'var':var,'margin':1-sum(costs)-m*var,'T':T}

def fraction_inverse(a):
    n=len(a);z=[list(a[i])+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if z[i][k]);z[k],z[p]=z[p],z[k]
        d=z[k][k];z[k]=[x/d for x in z[k]]
        for i in range(n):
            if i!=k:
                d=z[i][k];z[i]=[x-d*y for x,y in zip(z[i],z[k])]
    return [row[n:] for row in z]

def exact_obstruction(n=100):
    ep=F(8,16*n*n+9)
    weights=[F(1),F(2),F(1),F(1),F(1),F(1),ep,ep/2]
    z=sum(weights);p=[x/z for x in weights]
    mu=[sum(p[s] for s in range(8) if s>>i&1) for i in range(3)]
    cov=[[sum(p[s] for s in range(8) if s>>i&1 and s>>j&1)-mu[i]*mu[j] for j in range(3)] for i in range(3)]
    ci=fraction_inverse(cov);v=[F(0),F(1),F(1)]
    q=sum(v[i]*ci[i][j]*v[j] for i in range(3) for j in range(3))
    # log(1/ep)>9 log 3>9; logarithmic inequality is proved in report.
    assert ep<F(1,3**9)
    assert q<17
    assert p[0]*p[3]*p[5]*p[6]==p[1]*p[2]*p[4]*p[7]
    assert F(49,30)<F(169,100) # 7/sqrt(30)<13/10.
    assert 1-F(3,5)-F(3,8)==F(1,40)
    assert 1-F(3,10)-F(9,16)==F(11,80)
    # An exact rational K for n=1 is obtained by complex-pair arithmetic
    # in a separate small elimination, where i is represented in Q[i].
    return {'n':n,'epsilon':str(ep),'occupation_quadratic':str(q),'occupation_quadratic_float':float(q),'strict_surrogate_upper_bound':'17 - 2*9 = -1','exact_checks':'PASS'}

def main():
    output={'exact_obstruction':exact_obstruction(),'families':[]}
    max_identity=0.;rng=random.Random(130013)
    for u,ep,diag in [(.5,8/25,[2,1,1]),(.5,8/160009,[2,1,1]),(.5,.45,[.003,7,20]),(.8,.004,[.5,2,5]),(.95,.9,[4,.1,2]),(.5,1e-7,[1,1,1])]:
        K=family(u,ep,diag);H=hessian(K);e=eig(H);p=curv(K,zero())[2];b=atom_budget(p)
        assert b['margin']>11/80-1e-6
        assert e[-1]<0
        max_local=0.
        for _ in range(15):
            v=[rng.uniform(-1,1) for _ in range(9)];A=zero()
            for weight,B in zip(v,basis()):
                A=add(A,[[weight*z for z in row] for row in B])
            h,fi,_,_,tau,err=curv(K,A);max_identity=max(max_identity,err)
            rhs=-(11/80)*fi-min(curv(K,zero())[3])*dot(A,A)
            assert h<=rhs+1e-6*(1+abs(h))
            max_local=max(max_local,h-rhs)
        output['families'].append({'u':u,'epsilon':ep,'L_diagonal':diag,'largest_Hessian_eigenvalue':e[-1],'budget':b})
    accepted=0;min_margin=1.;worst_eig=-float('inf')
    for _ in range(600):
        ui=[math.exp(-10**rng.uniform(-1.5,1.2)) for _ in range(3)]
        if min(-math.log(x) for x in ui)>.5:continue
        diag=[10**rng.uniform(-1.5,1.5) for _ in range(3)]
        s=tau_zero_general(ui,diag)
        if s is None:continue
        K=s[1];p=curv(K,zero())[2];b=atom_budget(p)
        assert b['margin']>1/40-1e-6
        he=eig(hessian(K))[-1]
        assert he<1e-7
        accepted+=1;min_margin=min(min_margin,b['margin']);worst_eig=max(worst_eig,he)
    output['generic_tau_zero']={'accepted':accepted,'minimum_actual_budget_margin':min_margin,'largest_Hessian_eigenvalue':worst_eig}
    L=[[2,1,1],[1,1,complex(19,9)/25],[1,complex(19,-9)/25,1]]
    J=inv([[L[i][j]+int(i==j) for j in range(3)] for i in range(3)])
    K=[[int(i==j)-J[i][j] for j in range(3)] for i in range(3)]
    _,_,p,cs,tau,_=curv(K,zero());b=atom_budget(p)
    mu=min(cs)+tau/2
    output['nonzero_tau_example']={'tau':tau,'mu':mu,'F':b['F'],'variance':b['var'],'FI_margin':1-b['F']-mu*b['var'],'Frobenius_margin_without_spectral_refinement':mu-abs(tau),'largest_Hessian_eigenvalue':eig(hessian(K))[-1]}
    assert 1-b['F']-mu*b['var']>1/16
    assert mu-abs(tau)>115/237
    output['maximum_frozen_identity_error']=max_identity
    output['status']='PASS (finite diagnostics; not a substitute for analytic proof)'
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
