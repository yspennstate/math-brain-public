"""Independent, infinite-support h-transform simulation and estimate audit.

Sampling is by an envelope, NOT by cutting off and renormalizing rows.
For b a probability on positive m, put nu(m)=b_m/h(m+1).
To sample nu: sample M~b and Q~Sibuya(1/2); return -Q with
probability M/(M+Q), otherwise return +M. Indeed
Pr(Q=k)=d(k)/(2k-1), and
E[Q/(M+Q)|M=m]=1/h(m+1), by the beta integral.

Envelope: nu(j) + 1{j>0} b_j/h(p), total mass 1+1/h(p).
Acceptance at j>0 is h(p+j)/(h(p)+h(j+1)); at j<0 it is
h(p+j)/h(p), with rejection for p+j<=0.
The bound h(p+m)<=h(p)+h(m+1) follows from decreasing increments
h(r+1)-h(r)=d(r). All tails remain infinite.
"""
import json
import math
import resource
import signal
import time
from functools import lru_cache
from pathlib import Path
import numpy as np
import mpmath as mp

signal.alarm(240)
resource.setrlimit(resource.RLIMIT_CPU, (220, 230))
started = time.monotonic()
N_TABLE = 200000
index = np.arange(1, N_TABLE+1, dtype=float)
d = np.r_[1., np.cumprod((2*index-1)/(2*index))]
h_table = 2*np.arange(N_TABLE+1)*d

def logh(n):
    if n <= N_TABLE:
        return math.log(h_table[n])
    inv = 1/n
    return math.log(2/math.sqrt(math.pi)) + .5*math.log(n)-inv/8+inv**3/192-inv**5/640

def h(n):
    if n <= 0:
        return 0.
    return h_table[n] if n <= N_TABLE else math.exp(logh(n))

def sibuya(rng, alpha):
    if alpha == 1:
        return 1
    # Beta-geometric mixture. Work with gamma variables to retain tiny 1-t.
    x, y = rng.gamma(1-alpha), rng.gamma(alpha)
    if x == 0:
        return 1
    rate = math.log1p(y/x)
    if rate == math.inf:
        return 1
    if rate == 0:
        raise ArithmeticError('beta-geometric draw underflow')
    return 1+int(rng.exponential()/rate)

class Model:
    def __init__(self, name, alpha=None):
        self.name, self.alpha = name, alpha
        self.rho = .4
        self.T_table = None
        if alpha is not None:
            # T(1)=1/(1+alpha), T(p+1)/T(p)=(p+1)/(p+1+alpha).
            self.T_table = np.empty(N_TABLE+1)
            self.T_table[0] = float('nan')
            self.T_table[1:] = np.r_[1/(1+alpha), (1/(1+alpha))*np.cumprod(index[1:]/(index[1:]+alpha))]
            self.coeffs = [float((-1)**(k+1)*(mp.bernpoly(k+1, 1)-mp.bernpoly(k+1, 1+alpha))/(k*(k+1))) for k in range(1, 5)]
        self.atoms = [(16**j, (1-self.rho)*self.rho**j) for j in range(80)]

    def sample_b(self, rng):
        if self.alpha is not None:
            return sibuya(rng, self.alpha)
        j = int(rng.exponential()/(-math.log(self.rho)))
        return 16**j

    @lru_cache(maxsize=50000)
    def T(self, p):
        if self.alpha is None:
            return math.fsum(b/(1+p/m) for m, b in self.atoms)
        if p <= N_TABLE:
            return self.T_table[p]
        return math.exp(math.lgamma(1+self.alpha)-self.alpha*math.log(p)+sum(c/p**k for k, c in enumerate(self.coeffs, 1)))

    def negative(self, p):
        # Equivalent to independent disk formulas verified in audit_exact.py.
        dp = d[p] if p <= N_TABLE else h(p)/(2*p)
        return dp/(2*p-1)*self.T(p)

    def sample_nu(self, rng):
        m = self.sample_b(rng)
        k = sibuya(rng, .5)
        return -k if rng.random() < m/(m+k) else m

    def next(self, p, rng):
        hp = h(p)
        for _ in range(100000):
            j = self.sample_b(rng) if rng.random() < 1/(hp+1) else self.sample_nu(rng)
            y = p+j
            if y <= 0:
                continue
            accept = h(y)/(hp+h(j+1)) if j>0 else h(y)/hp
            if accept > 1+1e-12:
                raise ArithmeticError(('envelope failed', p, j, accept))
            if rng.random() <= accept:
                return y
        raise RuntimeError('too many rejections')

models = [Model('type_2', .5), Model('type_2.45', .95), Model('lacunary'), Model('type_2.5', 1.)]
all_rows = []
# Finite parts of all inequalities plus analytically summed positive tails.
# The negative tail is computed by conservation for small p only, where
# cancellation is mild; independently checked probability normalization is used.
for model in models:
    maxs = dict(a=0., b=0., c=0., d=0., big=0., mean=0., second=0., delta=0.)
    minswallow = 1.
    rowerr = 0.
    for p in [1, 2, 3, 4, 8, 16, 31, 64, 255, 1024, 4096]:
        ks = np.arange(1, p+1)
        neg = np.array([model.negative(int(k)) for k in ks])
        R = model.T(p)/math.sqrt(p)
        # Positive harmonic sum through the b distribution, without nu(-k).
        if model.alpha is None:
            plusmass = sum(b/h(m+1) for m, b in model.atoms)
        else:
            plusmass = 2*model.alpha/(2*model.alpha+1)
        totalneg = 1-plusmass
        aa = totalneg-float(neg[:p//2].sum())
        delta = totalneg-float(neg[:p-1].sum())
        maxs['a'] = max(maxs['a'], aa/R)
        maxs['delta'] = max(maxs['delta'], delta/R)
        maxs['b'] = max(maxs['b'], float(np.sum(ks*ks*neg))/(p*p*R))
        # Positive finite part computed from b, separately from negative law.
        if model.alpha is None:
            pos = [(m, b/h(m+1)) for m, b in model.atoms if m<=p]
            # Weighted tail bounded by its first 80 atoms: residual <= rho**80/sqrt(p).
            dd = sum(b*math.sqrt(m/p)/h(m+1) for m, b in model.atoms if m>p/2)
        else:
            alpha = model.alpha
            bm = alpha
            pos = []
            for m in range(1, p+1):
                if m>1:
                    bm *= (m-1-alpha)/m
                pos.append((m, bm/h(m+1)))
            # An independent numerical bound for d: sqrt(m)/h(m+1)<=sqrt(pi)/2.
            # Sum_{m>p/2} b_m = Gamma(floor(p/2)+1-alpha)/(Gamma(1-alpha)*Gamma(floor(p/2)+1)).
            # Thus d <= sqrt(pi)/(2sqrt(p))*Pr_b(M>p/2). This is only an upper bound.
            cut = p//2
            if alpha == 1:
                survival = float(cut == 0)
            elif cut == 0:
                survival = 1.
            else:
                survival = math.exp(math.lgamma(cut+1-alpha)-math.lgamma(1-alpha)-math.lgamma(cut+1))
            dd = math.sqrt(math.pi)/(2*math.sqrt(p))*survival
        maxs['c'] = max(maxs['c'], sum(m*m*prob for m, prob in pos)/(p*p*R))
        maxs['d'] = max(maxs['d'], dd/R)
        negsteps = [(p-int(k), float(prob)*h(p-int(k))/h(p)) for k, prob in zip(ks[:-1], neg[:-1])]
        possteps = [(p+m, prob*h(p+m)/h(p)) for m, prob in pos if m<=p/2]
        smallsteps = [(y, prob) for y, prob in negsteps+possteps if abs(y-p)<=p/2]
        mu = sum(prob*(logh(y)-logh(p)) for y, prob in smallsteps)
        sec = sum(prob*(logh(y)-logh(p))**2 for y, prob in smallsteps)
        # All omitted positive steps and listed large negative steps are big.
        big = 1-sum(prob for _, prob in smallsteps)
        maxs['big'] = max(maxs['big'], big/R)
        maxs['mean'] = max(maxs['mean'], abs(mu)/R)
        maxs['second'] = max(maxs['second'], sec/R)
        if p>=16:
            swallow = .5*sum(model.negative(k+1)*h(p-k-1)/h(p) for k in range(math.ceil(p/2), p-1))
            minswallow = min(minswallow, swallow/R)
    print('bounds', model.name, json.dumps(maxs, sort_keys=True), 'min_b_over_R', minswallow)

checkpoints = [100, 1000, 10000, 50000]
for model in models:
    for seed in [1729, 2718, 31415]:
        rng = np.random.default_rng(seed)
        p, maxp, sumrate, sumr, bigcount = 1, 1, 0., 0., 0
        row = dict(model=model.name, seed=seed, checkpoints=[])
        for n in range(1, checkpoints[-1]+1):
            T = model.T(p)
            sumr += T/math.sqrt(p)
            sumrate += p*model.negative(p)
            y = model.next(p, rng)
            bigcount += abs(y-p)>p/2
            p = y
            maxp = max(p, maxp)
            if n in checkpoints:
                item = dict(n=n, P=p, sum_p_nu_negative=sumrate, sum_R=sumr, max_P=maxp, big_jumps=bigcount)
                row['checkpoints'].append(item)
                print('path', model.name, seed, n, 'P', p, 'sum_pnu', round(sumrate, 9), 'sum_R', round(sumr, 9), 'maxP', maxp, flush=True)
        all_rows.append(row)
        model.T.cache_clear()
Path('audit_simulation_results.json').write_text(json.dumps(all_rows, indent=2)+'\n')
print('seconds', round(time.monotonic()-started, 3), 'peak_rss_bytes', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
