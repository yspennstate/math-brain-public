"""Exact resolvent obstruction and independent scalar-Laplace checks for C005.

Only the standard library, NumPy and SciPy are required.  Run from any directory.
"""
from fractions import Fraction as F
import itertools as it
import json
import numpy as np
from scipy.integrate import quad
from exterior_search import OUT, operator, wedge

def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def transpose(A):return list(map(list,zip(*A)))
def mul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def inv(A):
    n=len(A);M=[list(row)+e for row,e in zip(A,eye(n))]
    for i in range(n):
        j=next(j for j in range(i,n) if M[j][i]);M[i],M[j]=M[j],M[i]
        q=M[i][i];M[i]=[a/q for a in M[i]]
        for j in range(n):
            if j!=i:
                q=M[j][i];M[j]=[a-q*b for a,b in zip(M[j],M[i])]
    return [row[n:] for row in M]
def det(A):
    if not A:return F(1)
    n=len(A);M=[row[:] for row in A];d=F(1)
    for i in range(n):
        j=next((j for j in range(i,n) if M[j][i]),None)
        if j is None:return F(0)
        if j!=i:M[i],M[j]=M[j],M[i];d=-d
        q=M[i][i];d*=q
        for j in range(i+1,n):
            c=M[j][i]/q
            for k in range(i+1,n):M[j][k]-=c*M[i][k]
    return d
def quadratic(u,A,v):return sum(u[i]*A[i][j]*v[j] for i in range(len(u)) for j in range(len(v)))
def principal(A,S):return [[A[i][j] for j in S] for i in S]
def fstr(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(list,tuple)):return [fstr(a) for a in x]
    if isinstance(x,dict):return {k:fstr(v) for k,v in x.items()}
    return x

def exact_example(n):
    L3=[[F(a) for a in row] for row in [[6,-5,5],[-5,6,-5],[5,-5,10]]]
    L=eye(n)
    for i in range(3):
        for j in range(3):L[i][j]=L3[i][j]
    I=eye(n);IpL=[[I[i][j]+L[i][j] for j in range(n)] for i in range(n)]
    IpLi=inv(IpL);K=[[I[i][j]-IpLi[i][j] for j in range(n)] for i in range(n)]
    u=[F(a) for a in [1,1,0]+[0]*(n-3)]
    v=[F(a) for a in [0,0,1]+[0]*(n-3)]
    q=F(0);mass=F(0);coeffsum=F(0);rows=[]
    for m in range(1<<n):
        S=[i for i in range(n) if m>>i&1]
        Q=[[K[i][j]-F(i==j and i not in S) for j in range(n)] for i in range(n)]
        Qinv=inv(Q);p=(-1)**(n-len(S))*det(Q)
        assert p>0
        c=p*(quadratic(u,Qinv,u)*quadratic(v,Qinv,v)-quadratic(u,Qinv,v)**2)
        LS=principal(L,S)
        g=sum(inv(LS)[i][i] for i in range(len(S))) if S else F(0)
        q+=c*g;mass+=p;coeffsum+=c
        rows.append({'mask':m,'p':p,'mixed_atom_derivative':c,'resolvent_trace_s0':g})
    assert mass==1 and coeffsum==0 and q==F(-1,308)
    return {'n':n,'L':L,'K':K,'u':u,'v':v,'q_s0':q,'mass':mass,'coefficient_sum':coeffsum,'atoms':rows}

def laplace_q(K,weights,u,v,sign):
    # sign=+1 represents L=D+aa*, sign=-1 represents L=D-aa*.
    def integrand(t):
        if t==0:return 0.
        if t>1000:return 0. # Below double-precision tails in the retained examples.
        C=-np.expm1(-t*weights) if sign==1 else np.expm1(t*weights)
        root=np.sqrt(C)
        M=np.eye(len(K))+(-1 if sign==1 else 1)*(root[:,None]*K*root[None,:])
        R=root[:,None]*np.linalg.inv(M)*root[None,:]
        gram=np.vdot(u,R@u).real*np.vdot(v,R@v).real-abs(np.vdot(u,R@v))**2
        sg,ld=np.linalg.slogdet(M)
        assert sg>0
        return np.exp(-t+ld)*gram/t
    value,error=quad(integrand,0,np.inf,epsabs=1e-10,epsrel=1e-10,limit=250)
    return value,error

def integral_checks():
    records=[]
    for sign in [1,-1]:
        D=np.array([1.,2.,3.,4.,5.,6.])
        a=np.array([1.,-2.,1.,3.,-1.,2.])*(1 if sign==1 else .1)
        L=np.diag(D)+sign*np.outer(a,a)
        assert np.linalg.eigvalsh(L)[0]>0
        K=np.linalg.solve(np.eye(6)+L,L)
        u=np.array([1.,2.,-1.,1.,0.,1.]);v=np.array([0.,1.,1.,-2.,1.,1.])
        T,p=operator(K)
        w=wedge(u,v);direct=float(w@T@w)
        integrated,error=laplace_q(K,a*a/D,u,v,sign)
        assert direct>=0 and abs(direct-integrated)<1e-8
        records.append({'sign':sign,'D':D.tolist(),'a':a.tolist(),'u':u.tolist(),'v':v.tolist(),'q_logdet_direct':direct,'q_positive_integral':integrated,'quad_error_estimate':error,'absolute_difference':abs(direct-integrated),'mineig_T':float(np.linalg.eigvalsh(T)[0])})
    return records

def main():
    examples=[exact_example(3),exact_example(6)]
    integrals=integral_checks()
    out={'exact_resolvent_examples':fstr(examples),'laplace_checks':integrals}
    (OUT/'exact_and_integral_results.json').write_text(json.dumps(out,indent=2))
    print('Exact n=3 and n=6 resolvent mixed derivatives: -1/308.')
    for r in integrals:print(json.dumps(r))

if __name__=='__main__':main()
