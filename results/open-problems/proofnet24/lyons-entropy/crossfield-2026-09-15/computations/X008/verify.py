"""Deterministic checks of X008 exterior identities, bounds, and new frame class.

The report contains the proofs. This script is only a reproducible self-check.
"""
from itertools import combinations
import json
from pathlib import Path

import numpy as np


def adj(a):
    h = np.trace(a)
    return a @ a - h * a + (h*h - np.trace(a@a)) / 2 * np.eye(3)


def frame_data(v):
    n = len(v)
    t = np.sum(abs(v)**2, axis=1)
    uu = [np.outer(z.conj(), z) for z in v]
    ww = {}
    bb = {}
    rr = {}
    for pair in combinations(range(n), 2):
        z = np.cross(v[pair[0]], v[pair[1]])
        b = np.vdot(z, z).real
        if b > 1e-24:
            ww[pair] = np.outer(z, z.conj())
            bb[pair] = b
    for triple in combinations(range(n), 3):
        r = abs(np.linalg.det(v[list(triple)]))**2
        if r > 1e-24:
            rr[triple] = r
    e1 = sum((-np.log(t[i])*uu[i] for i in range(n) if t[i]>1e-24), np.zeros((3,3),complex))
    e2 = sum((-np.log(bb[p])*ww[p] for p in ww), np.zeros((3,3),complex))
    e3 = -sum(r*np.log(r) for r in rr.values())
    w = sum((np.log(t[i]*t[j]/bb[(i,j)])*ww[(i,j)] for i,j in ww), np.zeros((3,3),complex))
    sx = sum((t[i]*t[j]/bb[(i,j)]*ww[(i,j)] for i,j in ww), np.zeros((3,3),complex))
    tau = np.trace(e1-e2).real+e3
    z3 = sum(t[i]*t[j]*t[k] for i,j,k in combinations(range(n),3))
    d3 = sum(r*np.log(r*z3/(t[i]*t[j]*t[k])) for (i,j,k),r in rr.items())
    return t,uu,ww,bb,rr,e1,e2,e3,w,sx,tau,z3,d3


def basis():
    ans = []
    for i in range(3):
        a=np.zeros((3,3),complex);a[i,i]=1;ans.append(a)
    for i,j in combinations(range(3),2):
        a=np.zeros((3,3),complex);a[i,j]=a[j,i]=1/np.sqrt(2);ans.append(a)
        a=np.zeros((3,3),complex);a[i,j]=1j/np.sqrt(2);a[j,i]=-1j/np.sqrt(2);ans.append(a)
    return ans


def independent_curvature(v,s,a,data):
    t,uu,ww,bb,rr,*_=data
    n=len(v);q=1-s
    sets=[()]+[(i,) for i in range(n) if t[i]>1e-24]+list(ww)+list(rr)
    k=s*v@v.conj().T; b=v@a@v.conj().T
    # Differentiate inclusion minors, then apply exact Mobius inversion.
    inc1={():0.}; inc2={():0.}
    for subset in sets[1:]:
        kk=k[np.ix_(subset,subset)]; ba=b[np.ix_(subset,subset)]
        if len(subset)==1:
            inc1[subset]=ba[0,0].real;inc2[subset]=0.
        elif len(subset)==2:
            inc1[subset]=np.trace((np.trace(kk)*np.eye(2)-kk)@ba).real
            inc2[subset]=2*np.linalg.det(ba).real
        else:
            inc1[subset]=rr[subset]*s*s*np.trace(a).real
            inc2[subset]=2*rr[subset]*s*np.trace(adj(a)).real
    inc1[()]=0.;inc2[()]=0.
    p={():q**3}
    p.update({(i,):s*q*q*t[i] for i in range(n) if t[i]>1e-24})
    p.update({pair:s*s*q*b0 for pair,b0 in bb.items()})
    p.update({triple:s**3*r for triple,r in rr.items()})
    dp={subset:sum((-1)**(len(top)-len(subset))*inc1[top] for top in sets if set(subset)<=set(top)) for subset in sets}
    ddp={subset:sum((-1)**(len(top)-len(subset))*inc2[top] for top in sets if set(subset)<=set(top)) for subset in sets}
    fi=sum(dp[subset]**2/p[subset] for subset in sets)
    minus_h2=fi+sum(ddp[subset]*np.log(p[subset]) for subset in sets)
    return fi,minus_h2


def check(v,label,isotropic=False):
    assert np.linalg.norm(v.conj().T@v-np.eye(3))<2e-12
    data=frame_data(v)
    t,uu,ww,bb,rr,e1,e2,e3,w,sx,tau,z3,d3=data
    frame_identity_error=np.linalg.norm(w-(e1+e2-np.trace(e1)*np.eye(3)))
    assert frame_identity_error<2e-12
    contraction_error=max(np.linalg.norm(sum((ww[p] for p in ww if i in p),np.zeros((3,3),complex))-(t[i]*np.eye(3)-uu[i])) for i in range(len(v)))
    assert contraction_error<2e-12
    assert abs(tau+np.trace(w).real-(np.log(z3)-d3))<2e-12
    assert np.linalg.eigvalsh(sx)[-1]<2+2e-12
    assert np.linalg.eigvalsh(w)[-1]<np.log(2)+2e-12
    evals,evecs=np.linalg.eigh(sx)
    logs=(evecs*np.log(evals))@evecs.conj().T
    assert np.linalg.eigvalsh(logs-w)[0]>-2e-12
    # Integrate the actual compression correction with u=z/(1-z).
    nodes,weights=np.polynomial.legendre.leggauss(80)
    integral=np.zeros((3,3),complex)
    for node,weight in zip(nodes,weights):
        z=(node+1)/2;u=z/(1-z)
        compression=sum((ww[p]/(t[p[0]]*t[p[1]]/bb[p]+u) for p in ww),np.zeros((3,3),complex))
        integral+=weight/(2*(1-z)**2)*(compression-np.linalg.inv(sx+u*np.eye(3)))
    integral_error=np.linalg.norm(integral-(logs-w))
    assert integral_error<2e-10
    residual=np.linalg.norm(w-np.trace(w)/3*np.eye(3))
    if isotropic: assert residual<2e-12
    a=np.array([[.4,.2-.1j,.07j],[.2+.1j,-.15,.11],[-.07j,.11,.31]])
    rows=[]
    for s in (.15,.5,.85):
        q=1-s;T=w+s*tau*np.eye(3)
        fi,minus_h2=independent_curvature(v,s,a,data)
        fv=sum(np.trace(u@a).real**2/t[i] for i,u in enumerate(uu))
        fw=sum(np.trace(ww[p]@a).real**2/bb[p] for p in ww)
        assert abs(fi-fv/s-fw/q)<3e-12
        assert abs(minus_h2-(fi-2*np.trace(T@adj(a)).real))<3e-12
        bound=q*np.log(2)+s*np.log(4.5)
        assert np.linalg.eigvalsh(T)[0]>-2e-12
        assert np.linalg.eigvalsh(T)[-1]<bound+2e-12
        h=np.trace(a).real;B=a-h/3*np.eye(3);d=np.trace(T).real/3;E=T-d*np.eye(3)
        fiB=independent_curvature(v,s,B,data)[0]
        anisotropic=fiB+d*np.trace(B@B).real-2*np.trace(E@B@B).real
        anisotropic+=2*h/3*np.trace(E@B).real+(1/(3*s*q)-2*d/3)*h*h
        assert abs(minus_h2-anisotropic)<3e-12
        if isotropic:
            bs=basis();diag=[independent_curvature(v,s,b,data)[1] for b in bs]
            mat=np.diag(diag)
            for i,j in combinations(range(9),2):
                val=independent_curvature(v,s,bs[i]+bs[j],data)[1]
                mat[i,j]=mat[j,i]=(val-diag[i]-diag[j])/2
            assert np.linalg.eigvalsh(mat)[0]>1e-9
            h=np.trace(a).real;B=a-h/3*np.eye(3);tt=np.trace(T).real/3
            fiB=independent_curvature(v,s,B,data)[0]
            exact=fiB+tt*np.trace(B@B).real+(1/(3*s*q)-2*tt/3)*h*h
            assert abs(minus_h2-exact)<3e-12
            mineig=np.linalg.eigvalsh(mat)[0]
        else: mineig=None
        rows.append(dict(s=s,T_eigenvalues=np.linalg.eigvalsh(T).tolist(),
                         upper_bound=bound,identity_error=abs(minus_h2-(fi-2*np.trace(T@adj(a)).real)),
                         negative_hessian_minimum_eigenvalue=mineig))
    return dict(label=label,frame_identity_error=frame_identity_error,
                contraction_identity_error=contraction_error,W_eigenvalues=np.linalg.eigvalsh(w).tolist(),
                S_eigenvalues=np.linalg.eigvalsh(sx).tolist(),compression_gap_eigenvalues=np.linalg.eigvalsh(logs-w).tolist(),
                compression_integral_error=integral_error,
                tau=tau,top_product_mass=z3,top_relative_entropy=d3,
                entropy_isotropy_residual=residual,scalar_checks=rows)


z=np.array([0,1,1j,-1+.5j,2-1j,.5+.75j])
raw=np.column_stack((np.ones(6),z,z*z))
ev,uv=np.linalg.eigh(raw.conj().T@raw)
generic=raw@((uv/np.sqrt(ev))@uv.conj().T)
omega=np.exp(2j*np.pi/3)
fourier=np.array([[omega**(i*j) for j in range(3)] for i in range(3)])/np.sqrt(3)
two_bases=np.vstack((np.eye(3),fourier))/np.sqrt(2)
u=np.array([1,2,1j])/np.sqrt(6)
shift=np.roll(np.eye(3),1,axis=0);phase=np.diag([1,omega,omega**2])
weyl=np.array([(np.linalg.matrix_power(phase,a)@np.linalg.matrix_power(shift,b)@u).conj()/np.sqrt(3) for a in range(3) for b in range(3)])
results=[check(generic,'fixed generic complex six-row frame'),
         check(two_bases,'two mutually unbiased orthonormal bases',True),
         check(weyl,'generic Weyl-Heisenberg orbit, fiducial (1,2,i)/sqrt(6)',True)]
twodata=frame_data(two_bases)
assert np.linalg.norm(twodata[8]-.5*np.log(1.5)*np.eye(3))<2e-12
assert abs(twodata[10]-.75*np.log(4/3))<2e-12
output=Path(__file__).with_name('results.json')
output.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
