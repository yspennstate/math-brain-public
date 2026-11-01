"""Deterministic checks of phase-real full-Hermitian curvature identities."""
from pathlib import Path
from itertools import combinations
import json
import numpy as np

I=np.eye(3)
def adj(A):
    h=np.trace(A)
    return A@A-h*A+(h*h-np.trace(A@A))/2*I

def geom(V):
    U=[np.outer(v,v.conj()) for v in V]
    t=[np.trace(u).real for u in U]
    pairs=[]
    W=np.zeros((3,3),complex)
    e2=0
    for i,j in combinations(range(len(V)),2):
        w=np.cross(V[i],V[j]); b=np.vdot(w,w).real
        if b<1e-25: continue
        P=np.outer(w,w.conj())/b
        pairs.append((b,P))
        W+=b*np.log(t[i]*t[j]/b)*P
        e2-=b*np.log(b)
    e1=-sum(x*np.log(x) for x in t if x>0)
    e3=0
    for ijk in combinations(range(len(V)),3):
        r=abs(np.linalg.det(V[list(ijk)]))**2
        if r>1e-25:e3-=r*np.log(r)
    return W,e1-e2+e3,lambda A:sum(np.trace(u@A).real**2/x for u,x in zip(U,t)),lambda A:sum(b*np.trace(p@A).real**2 for b,p in pairs)

def real_design():
    phi=(1+np.sqrt(5))/2
    return np.array([[0,1,phi],[0,1,-phi],[1,phi,0],[1,-phi,0],[phi,0,1],[phi,0,-1]])/np.sqrt(2*(1+phi*phi))

def nearparallel(b):
    return np.array([[2**-.5,0,np.sqrt(b)],[-2**-.5,0,np.sqrt(b)],[0,2**-.5,-np.sqrt(.5-b)],[0,-2**-.5,-np.sqrt(.5-b)]])

def basis():
    R=[np.diag([1.,0,0]),np.diag([0,1.,0]),np.diag([0,0,1.])]
    J=[]
    for i,j in combinations(range(3),2):
        a=np.zeros((3,3)); a[i,j]=a[j,i]=2**-.5;R.append(a)
        a=np.zeros((3,3),complex);a[i,j]=1j*2**-.5;a[j,i]=-1j*2**-.5;J.append(a)
    return R,J

def matrix(f,B):
    d=[f(x) for x in B];M=np.diag(d)
    for i,j in combinations(range(len(B)),2): M[i,j]=M[j,i]=(f(B[i]+B[j])-d[i]-d[j])/2
    return M

def main():
    D=real_design(); assert np.linalg.norm(D.T@D-I)<1e-14
    R,J=basis();B0=[np.diag([1.,-1,0])/np.sqrt(2),np.diag([1.,1,-2])/np.sqrt(6)]+R[3:]
    wd,taud,fvd,fwd=geom(D)
    assert np.linalg.norm(wd-np.log(5/4)*I)<1e-14
    assert np.linalg.norm(matrix(fvd,B0)-.4*np.eye(5))<1e-14
    theta=5/16
    results=[]
    for b in [1e-8,1e-4,.001,.01,.1,.25]:
        V=np.vstack([np.sqrt(theta)*D,np.sqrt(1-theta)*nearparallel(b)])
        W,tau,fv,fw=geom(V)
        c=np.trace(W).real/3;E=W-c*I;e=np.linalg.eigvalsh(E)
        dm=min(c,c+tau);dp=max(c,c+tau)
        iso_gap=dm-2*e[-1]-np.trace(E@E).real/(3*(4-2*dp))
        fisher=matrix(fv,B0)
        rr=dict(b=b,real_traceless_moment_min=np.linalg.eigvalsh(fisher)[0],all_traceless_moment_min=0.,W_eigenvalues=np.linalg.eigvalsh(W).tolist(),tau=tau,X008_frame_only_gap=iso_gap,checks=[])
        for s in [.1,.5,.9]:
            T=W+s*tau*I
            curv=lambda A:fv(A)/s+fw(A)/(1-s)-2*np.trace(T@adj(A)).real
            H=matrix(curv,R+J)
            vals=np.linalg.eigvalsh(H)
            assert np.max(np.abs(H[:6,6:]))<1e-12
            assert np.linalg.eigvalsh(H[:6,:6])[0]>=1/26-1e-12
            for Y in J:
                assert abs(curv(Y)+2*np.trace(T@adj(Y)).real)<1e-12
            lower=min(1/26,(1-s)*theta**2*np.log(5/4))
            assert vals[0]>=lower-1e-12
            rr['checks'].append(dict(s=s,min_full_curvature_eigenvalue=vals[0],proven_lower_bound=lower,max_real_imaginary_cross=abs(H[:6,6:]).max()))
        results.append(rr)
    out=dict(design_W=np.diag(wd).real.tolist(),design_tau=taud,frames=results)
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()


def explicit_frame(epsilon):
    D=real_design();theta=5/16
    planar=np.array([[.5*np.cos(j*np.pi/4+sgn*epsilon),.5*np.sin(j*np.pi/4+sgn*epsilon),0.]
                     for j in range(4) for sgn in [-1,1]])
    C=np.vstack([planar,[0,0,1.]])
    return np.vstack([np.sqrt(theta)*D,np.sqrt(1-theta)*C])


def direct_atoms(V,s,A):
    """Independent odds atom log derivatives at a scalar active covariance.

    Uses row-subspace SVD, avoiding inverses of nearly singular pair Grams.
    """
    h=np.trace(A).real;q=1-s;norm=np.trace(A@A).real
    fi=0.;acc=0.;psum=0.
    for k in range(4):
        for ids in combinations(range(len(V)),k):
            if k:
                R=V[list(ids)]
                _,sig,vt=np.linalg.svd(R,full_matrices=False)
                if sig[-1]<1e-14:continue
                P=vt.T@vt
                gram=np.prod(sig**2)
            else:P=np.zeros((3,3));gram=1.
            p=s**k*q**(3-k)*gram
            score=-h/q+np.trace(P@A).real/(s*q)
            logsecond=-norm/q**2+2*np.trace(P@A@A).real/(s*q**2)-np.trace(P@A@P@A).real/(s*s*q*q)
            fi+=p*score**2
            acc+=p*(score**2+logsecond)*np.log(p)
            psum+=p
    assert abs(psum-1)<1e-13
    return fi,fi+acc


def explicit_check():
    V=explicit_frame(1e-8);W,tau,fv,fw=geom(V);R,J=basis();
    B0=[np.diag([1.,-1,0])/np.sqrt(2),np.diag([1.,1,-2])/np.sqrt(6)]+R[3:]
    c=np.trace(W).real/3;E=W-c*I;Delta=(W[2,2]-W[0,0]-W[1,1]).real
    assert np.linalg.norm(V.T@V-I)<1e-14
    assert np.max(abs(W-np.diag(np.diag(W))))<1e-14
    assert Delta>1/50
    assert abs(np.linalg.eigvalsh(matrix(fv,B0))[0]-.125)<1e-13
    n=V/np.linalg.norm(V,axis=1)[:,None]
    t=np.sum(V**2,axis=1);rowlogs=np.zeros(len(V))
    for i,j in combinations(range(len(V)),2):
        d=np.linalg.norm(np.cross(n[i],n[j]))**2
        if d>1e-25:
            rowlogs[i]+=t[j]*(-np.log(d));rowlogs[j]+=t[i]*(-np.log(d))
    assert max(rowlogs)>56/25
    checks=[]
    tests=[np.diag([.3,-.5,.7]),np.array([[.4,.2-.1j,.07j],[.2+.1j,-.15,.11],[-.07j,.11,.31]])]
    for s in [.01,.1,.5,.9]:
        T=W+s*tau*I;d=c+s*tau;Ls=1/(s*(1-s))-2*d
        curv=lambda A:fv(A)/s+fw(A)/(1-s)-2*np.trace(T@adj(A)).real
        H=matrix(curv,R+J)
        lower=min(1/26,(1-s)*(5/16)**2*np.log(5/4))
        assert np.linalg.eigvalsh(H)[0]>=lower-1e-12
        assert abs(H[:6,6:]).max()<1e-12
        atomerrs=[];squareerrs=[]
        for A in tests:
            afi,ac=direct_atoms(V,s,A)
            atomerrs.append(abs(ac-curv(A)))
            assert abs(ac-curv(A))<1e-10
            X=A.real;h=np.trace(X);B=X-h/3*I
            Q=fv(B)/s+fw(B)/(1-s)-2*np.trace(T@adj(B)).real-np.trace(E@B).real**2/(3*Ls)
            exact=Q+Ls/3*(h+np.trace(E@B).real/Ls)**2
            squareerrs.append(abs(exact-curv(X)))
            assert squareerrs[-1]<1e-10
        checks.append(dict(s=s,full_curvature_min=np.linalg.eigvalsh(H)[0],proven_bound=lower,max_independent_atom_error=max(atomerrs),max_trace_square_error=max(squareerrs)))
    res=dict(epsilon=1e-8,W_diagonal=np.diag(W).real.tolist(),tau=tau,Delta=Delta,real_traceless_moment_min=.125,imaginary_traceless_moment=0.,overlap_row_max=max(rowlogs),X008_pointwise_gap_at_s_001=c+.01*tau-2*np.linalg.eigvalsh(E)[-1],checks=checks)
    Path(__file__).with_name('explicit_results.json').write_text(json.dumps(res,indent=2)+'\n')
    print(json.dumps(res,indent=2))

if __name__=='__main__':explicit_check()
