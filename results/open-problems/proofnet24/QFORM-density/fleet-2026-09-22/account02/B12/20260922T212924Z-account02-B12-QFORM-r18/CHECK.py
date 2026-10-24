import itertools, math
import numpy as np


def build(n, tau, phi):
    th = 2*np.pi*np.arange(n)/n
    R = np.column_stack([
        np.ones(n)/np.sqrt(n),
        np.sqrt(2/n)*np.cos(th),
        np.sqrt(2/n)*np.sin(th),
    ])
    w = np.sqrt(2/n)*np.cos(2*th + phi)
    A = R@R.T + tau*np.outer(w,w)
    return A,R,w


def check_case(n,tau,phi):
    A,R,w=build(n,tau,phi)
    target=np.array(sorted([0.0]*(n-4)+[1.0,1.0,1.0,tau]))
    evals=np.linalg.eigvalsh(A)
    spectrum_err=float(np.max(np.abs(np.sort(evals)-target)))
    orth_err=max(float(np.max(np.abs(R.T@R-np.eye(3)))),
                 float(np.max(np.abs(R.T@w))),
                 float(abs(w@w-1)))
    dets=[np.linalg.det(A[np.ix_([i,j],[i,j])])
          for i in range(n) for j in range(i+1,n)]
    entry_bound=(3+2*abs(tau))/n
    max_entry=float(np.max(np.abs(A)))
    triples=list(itertools.combinations(range(n),3))
    if len(triples)>10000:
        rng=np.random.default_rng(0)
        triples=[tuple(sorted(rng.choice(n,3,replace=False))) for _ in range(10000)]
    max_core=max(float(np.linalg.norm(A[np.ix_(I,I)],2)) for I in triples)
    core_bound=3*entry_bound
    return dict(n=n,tau=tau,phi=phi,spectrum_err=spectrum_err,
                orth_err=orth_err,min_abs_pair_det=float(min(map(abs,dets))),
                max_entry=max_entry,entry_bound=entry_bound,
                max_sampled_core_opnorm=max_core,core_bound=core_bound)

cases=[]
for n in (11,31,101):
    for tau in (0.5,2.0,math.sqrt(n),-0.5,-2.0,-math.sqrt(n)):
        cases.append(check_case(n,tau,0.3712345))

assert max(c['spectrum_err'] for c in cases) < 1e-10
assert max(c['orth_err'] for c in cases) < 1e-10
assert min(c['min_abs_pair_det'] for c in cases) > 1e-12
assert max(c['max_entry']-c['entry_bound'] for c in cases) < 1e-10
assert max(c['max_sampled_core_opnorm']-c['core_bound'] for c in cases) < 1e-10
print('PASS')
print('cases',len(cases))
print('max_spectrum_error',max(c['spectrum_err'] for c in cases))
print('max_orthogonality_error',max(c['orth_err'] for c in cases))
print('min_abs_pair_det',min(c['min_abs_pair_det'] for c in cases))
print('max_entry_bound_violation',max(c['max_entry']-c['entry_bound'] for c in cases))
print('max_core_bound_violation',max(c['max_sampled_core_opnorm']-c['core_bound'] for c in cases))
