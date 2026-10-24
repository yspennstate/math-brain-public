"""Reproduce C024's correction identities and its dense three-site corridor."""
import itertools
import json
import math
import numpy as np
from scipy.linalg import qr

rng = np.random.default_rng(20260915024)

def channel(U):
    n = len(U)
    subsets = [[i for i in range(n) if s >> i & 1] for s in range(1 << n)]
    W = np.zeros((1 << n, 1 << n))
    for s, S in enumerate(subsets):
        for t, T in enumerate(subsets):
            if len(S) == len(T):
                W[s,t] = abs(np.linalg.det(U[np.ix_(S,T)]))**2 if S else 1.
    return W

def data(U, lam, a, W=None):
    n = len(lam)
    if W is None: W = channel(U)
    z = np.array([[bool(s >> i & 1) for i in range(n)] for s in range(1 << n)], dtype=float)
    q = np.prod(np.where(z, lam, 1-lam), axis=1)
    v = lam*(1-lam)
    scores = (z-lam)*a/v
    total = scores.sum(axis=1)
    accscore = total**2-(scores**2).sum(axis=1)
    p = W@q
    dp = W@(q*total)
    ddp = W@(q*accscore)
    lp = np.log(p)
    mean = p@z
    C = (z-mean).T @ (p[:,None]*(z-mean))
    centered = lp-p@lp
    d = (z-mean).T@(p*centered)
    resid = centered-(z-mean)@np.linalg.solve(C,d)
    Vperp = p@(resid**2)
    G_i = a*a/v
    G = G_i.sum()
    second_quantum = 2*(G*G-G_i@G_i)
    second_measured = (ddp*ddp/p).sum()
    pair = ddp@lp
    gM = (dp*dp/p).sum()
    lower = a.sum()**2/v.sum()
    return dict(p=p, dp=dp, ddp=ddp, pair=pair, gM=gM, G=G,
                second_quantum=second_quantum,
                second_measured=second_measured, Vperp=Vperp,
                norm_identity_error=abs(q@(accscore**2)-second_quantum),
                measured_fisher_lower=lower,
                Hsecond=-gM-pair,
                spectral_certificate=-lower+math.sqrt(max(0,second_quantum)*Vperp))

metrics = dict(samples=0, max_acceleration_norm_identity_error=0.,
               max_fisher_saturation_error=0., max_two_site_sharpness_error=0.,
               min_measured_acceleration_contraction_slack=math.inf,
               min_measured_cauchy_slack=math.inf,
               min_fisher_lower_slack=math.inf)
for n in range(2,6):
    for trial in range(12):
        U = qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]
        W = channel(U)
        lam = rng.uniform(.04,.96,n)
        a = rng.normal(size=n)
        x = data(U,lam,a,W)
        sat = data(U,lam,lam*(1-lam),W)
        metrics['samples'] += 1
        metrics['max_acceleration_norm_identity_error'] = max(metrics['max_acceleration_norm_identity_error'],x['norm_identity_error'])
        metrics['max_fisher_saturation_error'] = max(metrics['max_fisher_saturation_error'],abs(sat['gM']-sat['G']))
        metrics['min_measured_acceleration_contraction_slack'] = min(metrics['min_measured_acceleration_contraction_slack'],x['second_quantum']-x['second_measured'])
        metrics['min_measured_cauchy_slack'] = min(metrics['min_measured_cauchy_slack'],x['second_measured']*x['Vperp']-x['pair']**2)
        metrics['min_fisher_lower_slack'] = min(metrics['min_fisher_lower_slack'],x['gM']-x['measured_fisher_lower'])
        if n == 2:
            metrics['max_two_site_sharpness_error'] = max(metrics['max_two_site_sharpness_error'],abs(abs(x['pair'])-math.sqrt(x['second_measured']*x['Vperp'])))
        assert x['second_quantum']+1e-8 >= x['second_measured']
        assert x['second_measured']*x['Vperp']+1e-8 >= x['pair']**2
        assert x['gM']+1e-8 >= x['measured_fisher_lower']
        assert abs(sat['gM']-sat['G']) < 1e-10

U = np.array([[1,2,2],[2,-2,1],[2,1,-2]],dtype=float)/3
W = channel(U)
eps=1/1024
lam0=np.array([1/4,eps,3*eps/2])
lam1=np.array([3/4,3*eps/2,2*eps])
a=lam1-lam0
B= (3*math.log(2))**2+2
curve=[]
for t in np.linspace(0,1,201):
    x=data(U,(1-t)*lam0+t*lam1,a,W)
    universal=-x['measured_fisher_lower']+math.sqrt(x['second_quantum']*B)
    curve.append(dict(t=float(t),Hsecond=float(x['Hsecond']),
                      interaction_variance=float(x['Vperp']),
                      measured_acceleration_bound=float(math.sqrt(x['second_measured']*x['Vperp'])),
                      spectral_residual_certificate=float(x['spectral_certificate']),
                      universal_certificate=float(universal)))
    assert x['Hsecond'] <= universal+1e-10
    assert universal <= -.5
example=dict(epsilon=eps, epsilon_allowed=1/(64*2*B),
             K0=((U*lam0)@U.T).tolist(), K1=((U*lam1)@U.T).tolist(),
             direction=((U*a)@U.T).tolist(),
             max_Hsecond=max(row['Hsecond'] for row in curve),
             max_universal_certificate=max(row['universal_certificate'] for row in curve),
             max_spectral_residual_certificate=max(row['spectral_residual_certificate'] for row in curve),
             grid=curve)
results=dict(seed=20260915024, identity_checks=metrics, example=example,
             statement='The numerical grid verifies formulas but is not the proof of the continuum corridor; see agents/C024.md.')
with open('computations/C024/results.json','w') as f: json.dump(results,f,indent=2)
print(json.dumps({'identity_checks':metrics,'example_summary':{k:v for k,v in example.items() if k!='grid'}},indent=2))
