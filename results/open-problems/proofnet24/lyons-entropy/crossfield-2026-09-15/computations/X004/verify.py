"""Deterministic self-checks of X004 identities; numerical checks are not proofs."""
from itertools import combinations
import json
import numpy as np


def adj(x):
    # Polynomial adjugate, valid for singular 3x3 Hermitian matrices as well.
    return x @ x - np.trace(x) * x + .5 * (np.trace(x)**2 - np.trace(x @ x)) * np.eye(3)


def frame_data(v, m):
    n = len(v)
    sets = [()] + [s for k in (1,2,3) for s in combinations(range(n), k)]
    ell = m @ np.linalg.inv(np.eye(3)-m)
    g = v @ ell @ v.conj().T
    det0 = np.linalg.det(np.eye(3)-m).real
    atom = {():det0}
    for s in sets[1:]:
        atom[s] = det0 * max(0., np.linalg.det(g[np.ix_(s,s)]).real)
    f = {s:-np.log(p) for s,p in atom.items() if p>1e-14}
    c = {}
    for s in sets:
        if s not in f:
            continue
        c[s] = f[s] - sum(c[t] for k in range(len(s)) for t in combinations(s,k))
    w = {s:np.cross(v[s[0]],v[s[1]]) for s in combinations(range(n),2)}
    r = {s:abs(np.linalg.det(v[list(s)]))**2 for s in combinations(range(n),3)}
    bigw = sum((c[s]*np.outer(z,z.conj()) for s,z in w.items()), np.zeros((3,3),complex))
    tau = sum(c.get(s,0.)*r[s] for s in r if r[s]>1e-14)
    return sets,atom,f,c,w,r,bigw,tau


def atom_derivatives(v,m,a,sets):
    k=v@m@v.conj().T
    b=v@a@v.conj().T
    first={():0.}
    second={():0.}
    for s in sets[1:]:
        ksub=k[np.ix_(s,s)]
        bsub=b[np.ix_(s,s)]
        if len(s)==1:
            first[s]=bsub[0,0].real
            second[s]=0.
        elif len(s)==2:
            adj2=np.trace(ksub)*np.eye(2)-ksub
            first[s]=np.trace(adj2@bsub).real
            second[s]=2*np.linalg.det(bsub).real
        else:
            r=abs(np.linalg.det(v[list(s)]))**2
            first[s]=r*np.trace(adj(m)@a).real
            second[s]=2*r*np.trace(m@adj(a)).real
    dp={s:sum((-1)**(len(t)-len(s))*first[t] for t in sets if set(s)<=set(t)) for s in sets}
    ddp={s:sum((-1)**(len(t)-len(s))*second[t] for t in sets if set(s)<=set(t)) for s in sets}
    return dp,ddp


def check(v,m,a,label):
    sets,p,f,c,w,r,bigw,tau=frame_data(v,m)
    t=bigw+tau*m
    dp,ddp=atom_derivatives(v,m,a,sets)
    frozen=sum(ddp[s]*f[s] for s in f)
    expected=2*np.trace(t@adj(a)).real
    fi=sum(dp[s]**2/p[s] for s in f)
    assert abs(sum(p.values())-1)<2e-12
    assert abs(frozen-expected)<2e-11
    assert np.linalg.eigvalsh(bigw)[0]>-1e-11
    assert np.linalg.eigvalsh(bigw+tau*np.eye(3))[0]>-1e-11
    assert np.linalg.eigvalsh(t)[0]>-1e-11
    return dict(label=label,normalization=sum(p.values()),tau=tau,
                W_eigenvalues=np.linalg.eigvalsh(bigw).tolist(),
                W_plus_tau_eigenvalues=np.linalg.eigvalsh(bigw+tau*np.eye(3)).tolist(),
                T_eigenvalues=np.linalg.eigvalsh(t).tolist(),
                frozen_identity_error=abs(frozen-expected),
                fisher=fi,entropy_second_derivative=-fi+frozen)

# A fixed complex six-row frame, with a non-scalar noncommuting active covariance.
z=np.array([0,1,1j,-1+.5j,2-1j,.5+.75j])
raw=np.column_stack((np.ones(6),z,z*z))
e,u=np.linalg.eigh(raw.conj().T@raw)
v=raw@((u/np.sqrt(e))@u.conj().T)
m=np.array([[.32,.04+.03j,-.01j],[.04-.03j,.56,.06], [.01j,.06,.43]])
a=np.array([[.4,.2-.1j,.07j],[.2+.1j,-.15,.11],[-.07j,.11,.31]])
results=[check(v,m,a,'non-scalar generic six-row frame')]

# Verify the primitive identity at the same non-scalar base.
*_,bigw,tau=frame_data(v,m)
t=bigw+tau*m
e,u=np.linalg.eigh(t)
sq=(u*np.sqrt(e))@u.conj().T
b=a-np.trace(a)/3*np.eye(3)
a0=sq@b@sq
out=check(v,m,a0,'primitive six-row direction')
assert abs(out['entropy_second_derivative']+out['fisher']+np.linalg.det(t).real*np.trace(b@b).real)<2e-12
results.append(out)

# Explicit nine-row equal-norm equiangular frame, theta=pi/9.
theta=np.pi/9
om=np.exp(2j*np.pi/3)
v9=np.array([[0,1,-np.exp(1j*theta)*om**j] for j in range(3)] +
            [[-np.exp(1j*theta)*om**j,0,1] for j in range(3)] +
            [[1,-np.exp(1j*theta)*om**j,0] for j in range(3)])/np.sqrt(6)
assert np.linalg.norm(v9.conj().T@v9-np.eye(3))<1e-12
pp=v9@v9.conj().T
assert max(abs(abs(pp[i,j])**2-1/36) for i in range(9) for j in range(i))<1e-12
for s in (.15,.5,.85):
    out=check(v9,s*np.eye(3),a,f'equiangular nine-row scalar s={s}')
    *_,w,r,bigw,tau=frame_data(v9,s*np.eye(3))
    cv=np.log(4/3)
    assert np.linalg.norm(bigw-cv*np.eye(3))<1e-12
    tt=cv+s*tau
    bound=(4/3-np.log(2))*np.trace(a).real**2+tt*np.trace(a@a).real
    assert -out['entropy_second_derivative']>=bound-1e-11
    # Root's exact scalar-base Fisher decomposition.
    fv=sum((v9[i]@a@v9[i].conj()).real**2/np.vdot(v9[i],v9[i]).real for i in range(9))
    fw=sum((z.conj()@a@z).real**2/np.vdot(z,z).real for z in w.values())
    assert abs(out['fisher']-(fv/s+fw/(1-s)))<2e-11
    out['strict_theorem_lower_bound']=bound
    out['positive_triple_atom_weights']=sorted({round(x,12) for x in r.values() if x>1e-12})
    results.append(out)
print(json.dumps(results,indent=2))
