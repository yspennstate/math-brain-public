"""E0110: O'Connell-Yor-type GRBM  dX_i = (mu_i + e^{-X_i} - e^{-X_{i-1}}) dt + dB_i, Gamma = I,
with the convention e^{-X_0} = 0.  Two drift families:
  F (fixed drifts):  mu_i = -theta for all i        -> m_i := sum_{k<=i}|mu_k| = i*theta
  T (tandem-like):   mu = (-theta, -eps, ..., -eps)  -> m_i = theta + (i-1)*eps
Measured:
  (a) synchronous coupling distance Delta_i(t) = X_i - X'_i for X(0) = X'(0) + e_1  (a unit kick of coordinate 1),
      averaged over paths; compare with the pure-birth-chain prediction with rates m_i.
  (b) relaxation of E exp(-X_d(t)) to its exact stationary value m_d from an 'empty' start x_i = -log m_i + 2.
Euler-Maruyama, vectorised over paths.  Kept polite: one process, a few minutes.
"""
import numpy as np, time, json, sys
rng = np.random.default_rng(20260909)

def drift(X, mu):
    E = np.exp(-X)
    Eprev = np.concatenate([np.zeros((X.shape[0],1)), E[:, :-1]], axis=1)
    return mu + E - Eprev

def simulate_pair(x0, x0p, mu, T, dt, npaths, record_every):
    d = len(mu)
    X = np.tile(x0, (npaths,1)); Xp = np.tile(x0p, (npaths,1))
    nsteps = int(round(T/dt)); sq = np.sqrt(dt)
    times=[]; delta=[]; eX=[]
    for n in range(nsteps+1):
        if n % record_every == 0:
            times.append(n*dt); delta.append((X-Xp).mean(0)); eX.append(np.exp(-X).mean(0))
        if n == nsteps: break
        dB = rng.standard_normal((npaths,d))*sq
        X  = X  + drift(X,mu)*dt + dB
        Xp = Xp + drift(Xp,mu)*dt + dB
    return np.array(times), np.array(delta), np.array(eX)

def birth_chain(rates, T, dt):
    """pure birth chain on 1..d with rates m_i, killed after d; returns mass at each site vs time (matrix exp by RK4)."""
    d=len(rates); A=np.zeros((d,d))
    for i in range(d):
        A[i,i]=-rates[i]
        if i+1<d: A[i+1,i]=rates[i]
    from scipy.linalg import expm
    ts=np.arange(0,T+1e-9,dt); out=[]
    for t in ts:
        out.append(expm(A*t)[:,0])
    return ts, np.array(out)

def run(family, d, theta=1.0, eps=0.02, T=None, dt=None, npaths=400):
    if family=='F': mu = -theta*np.ones(d)
    else: mu = np.concatenate([[-theta], -eps*np.ones(d-1)])
    m = np.cumsum(-mu)
    if T is None: T = 4*np.sum(1/m)+8
    if dt is None: dt = min(0.5/m.max(), 0.01)*0.5
    rec = max(1,int(round(0.05/dt)))
    xfix = -np.log(m)
    t0=time.time()
    # (a) unit kick of coordinate 1 on top of the fluid fixed point (close to stationary-typical for the nonlinear system)
    x0p = xfix.copy(); x0 = xfix.copy(); x0[0]+=1.0
    ta, delta, _ = simulate_pair(x0, x0p, mu, T, dt, npaths, rec)
    # (b) relaxation of E e^{-X_d} from the empty start
    tb, _, eX = simulate_pair(xfix+2.0, xfix+2.0, mu, T, dt, npaths//2, rec)
    tc, mass = birth_chain(m, T, 0.05)
    # summary numbers
    mass_sim = delta.sum(1)            # total coupling mass sum_i Delta_i(t)
    def t_half(ts, y, y0, yinf):        # first time y is within half of its way from y0 to yinf... use 'below 0.5 of initial'
        idx = np.where(np.abs(y-yinf) <= 0.5*np.abs(y0-yinf))[0]
        return float(ts[idx[0]]) if len(idx) else np.nan
    def t_frac(ts, y, y0, yinf, frac):
        idx = np.where(np.abs(y-yinf) <= frac*np.abs(y0-yinf))[0]
        return float(ts[idx[0]]) if len(idx) else np.nan
    res = dict(family=family, d=d, theta=theta, eps=(eps if family=='T' else None), dt=dt, T=T, npaths=npaths,
        sum_inv_m=float(np.sum(1/m)),
        # coupling mass half-life and 10% time, simulated vs birth-chain
        t_mass_half_sim=t_frac(ta, mass_sim, 1.0, 0.0, 0.5), t_mass_10_sim=t_frac(ta, mass_sim, 1.0, 0.0, 0.1),
        t_mass_half_chain=t_frac(tc, mass.sum(1), 1.0, 0.0, 0.5), t_mass_10_chain=t_frac(tc, mass.sum(1), 1.0, 0.0, 0.1),
        # last coordinate: peak time of Delta_d, simulated vs chain
        t_peak_last_sim=float(ta[np.argmax(delta[:,-1])]), t_peak_last_chain=float(tc[np.argmax(mass[:,-1])]),
        # observable e^{-X_d}: time to get within 10% of stationary m_d, and the endpoint ratio (check of E e^{-X_d} = m_d)
        t_obs_10=t_frac(tb, eX[:,-1], eX[0,-1], m[-1], 0.1), eXd_end_over_md=float(eX[-1,-1]/m[-1]),
        eX1_end_over_m1=float(eX[-1,0]/m[0]), seconds=time.time()-t0)
    return res, (ta, delta, tb, eX, tc, mass, m)

if __name__=='__main__':
    out=[]
    for fam in ['F','T']:
        for d in [4,8,16,32,64]:
            r,_ = run(fam, d)
            print(json.dumps(r)); sys.stdout.flush(); out.append(r)
    json.dump(out, open('sim_results.json','w',encoding='utf-8'), indent=1)
