"""Independent numerical normalization check; not a substitute for proof.

Evaluate the delta-free, finite-time Gaussian recursion and compare with
ordinary full-batch logistic GD on actual Gaussian tanh random features.
Finite-network A,Q are asymptotically equivalent covariance proxies, not
exact conditional finite-dimensional moments. Label randomness in the recursion
is integrated exactly. All random seeds
are fixed. The script writes machine-readable output beside itself.
"""
import json
from pathlib import Path
import numpy as np
from scipy.special import expit, ndtri
from scipy.stats import qmc
from numpy.polynomial.hermite import hermgauss


def constants(beta):
    x, w = hermgauss(100)
    x, w = np.sqrt(2) * x, w / np.sqrt(np.pi)
    a = np.sum(w * x * np.tanh(x))
    v = np.sum(w * np.tanh(x) ** 2)
    mu = np.sum(w * x * (expit(beta * x) - 0.5))
    return a, v, v - a * a, mu


def state_evolution(alpha, gamma, beta, c, horizon=5, power=18, seed=1729):
    a, v, nu, mu = constants(beta)
    lam, spike = c / alpha, a * np.sqrt(gamma)
    base = qmc.Sobol(horizon + 1, scramble=True, seed=seed).random_base2(power)
    base = ndtri(np.clip(base, 1e-15, 1 - 1e-15))
    z, normal = base[:, 0], base[:, 1:]
    prob = expit(beta * z)
    weights = np.stack((1 - prob, prob), axis=1)
    labels = np.array([0.0, 1.0])[None, :]
    count = len(z)
    residual = np.zeros((count, 2, horizon + 1))
    residual[:, :, 0] = labels - 0.5
    jac = np.zeros((count, 2, horizon + 1, horizon))
    psi = np.zeros((horizon, horizon))
    overlap = np.zeros(horizon)
    gram = np.zeros((horizon, horizon))
    history = []
    for t in range(1, horizon + 1):
        rr = residual[:, :, :t]
        delta = alpha * np.einsum('ny,nyi,nyj->ij', weights, rr, rr) / count
        phi = alpha * np.einsum('ny,nyij->ij', weights, jac[:, :, :t, :t]) / count
        ell = alpha * np.einsum('ny,n,nyi->i', weights, z, rr) / count
        ps = psi[:t, :t].copy()
        gm = gram[:t, :t].copy()
        left = np.linalg.inv(np.eye(t) - a * a * phi @ ps)
        omega = (nu * delta + a*a * left @ (delta + a*a * phi @ gm @ phi.T) @ left.T) / gamma
        back = (nu * phi + a*a * left @ phi) / gamma
        prev = ps[t-2].copy() if t > 1 else np.zeros(t)
        ps[t-1] = prev + lam * (np.eye(t)[t-1] + back[t-1] @ ps)
        qprev = overlap[t-2] if t > 1 else 0.0
        overlap[t-1] = qprev + lam * (back[t-1] @ overlap[:t] + spike * ell[t-1] / gamma)
        psi[:t, :t] = ps
        gm = ps @ omega @ ps.T + np.outer(overlap[:t], overlap[:t])
        gram[:t, :t] = gm
        right = np.linalg.inv(np.eye(t) - a*a * ps @ phi)
        sigma = nu * gm + a*a * right @ (gm + a*a * ps @ delta @ ps.T) @ right.T
        sigma = (sigma + sigma.T) / 2
        forward = nu * ps + a*a * right @ ps
        eig = np.linalg.eigvalsh(sigma)
        if eig.min() <= 0:
            raise ArithmeticError(f'Nonpositive finite-time covariance: {eig}')
        fields = normal[:, :t] @ np.linalg.cholesky(sigma).T
        mean = spike * overlap[t-1]
        score = fields[:, t-1, None] + np.einsum('nyi,i->ny', rr, forward[t-1]) + mean * z[:, None]
        pred = expit(score)
        residual[:, :, t] = labels - pred
        ds = np.einsum('nyij,i->nyj', jac[:, :, :t, :t], forward[t-1])
        ds[:, :, t-1] += 1
        jac[:, :, t, :t] = -pred[:, :, None] * (1 - pred[:, :, None]) * ds
        history.append(dict(time=t, A=float(mean), Q=float(mean**2 + sigma[t-1,t-1]),
                            norm2=float(gm[t-1,t-1]), residual_variance=float(sigma[t-1,t-1]),
                            min_covariance_eigenvalue=float(eig.min())))
    tau2 = mu*mu*a*a*v/gamma + (a**4 + v*v/gamma)/(4*alpha)
    target = np.array([c*a*a*mu, c*c*(a**4*mu*mu+tau2)])
    observed = np.array([history[0]['A'], history[0]['Q']])
    return dict(parameters=dict(alpha=alpha,gamma=gamma,beta=beta,c=c), history=history,
                first_step_closed_form=target.tolist(), first_step_abs_error=np.abs(target-observed).tolist())


def direct_rf(alpha, gamma, beta, c, d, repetitions=12, horizon=5, seed=20261024):
    a, v, nu, mu = constants(beta)
    n, m = round(alpha*d), round(gamma*d)
    rng = np.random.default_rng(seed + d)
    out = np.zeros((repetitions,horizon,3))
    for rep in range(repetitions):
        x = rng.standard_normal((n,d))
        f = rng.standard_normal((m,d))/np.sqrt(d)
        y = rng.binomial(1,expit(beta*x[:,0]))
        h = np.tanh(x @ f.T)
        b = np.zeros(m)
        for t in range(horizon):
            b += (c*d/(n*m)) * h.T @ (y-expit(h @ b))
            fb = f.T @ b
            out[rep,t] = [a*fb[0], a*a*np.dot(fb,fb)+nu*np.dot(b,b),np.dot(b,b)]
    return dict(d=d,repetitions=repetitions,columns=['A','Q','norm2'],
                mean=out.mean(axis=0).tolist(),standard_error=(out.std(axis=0,ddof=1)/np.sqrt(repetitions)).tolist())


def main():
    results = []
    for params in [(2.,1.,1.5,.8),(1.,2.,1.,1.1)]:
        se = state_evolution(*params)
        se['qmc_repeat'] = state_evolution(*params,seed=2718)['history']
        se['direct_rf'] = [direct_rf(*params,d=d) for d in (250,500,1000)]
        results.append(se)
        print(json.dumps({'parameters':se['parameters'],'first_step_abs_error':se['first_step_abs_error'],
                          'finite_time_target':se['history'][-1], 'd1000':se['direct_rf'][-1]['mean'][-1]}),flush=True)
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps({'purpose':'Numerical normalization check only; proof is analytic.',
                                 'finite_network_A_Q':'Asymptotically equivalent covariance proxies, not exact finite-dimensional conditional moments.',
                                 'results':results},indent=2)+'\n')


if __name__ == '__main__':
    main()
