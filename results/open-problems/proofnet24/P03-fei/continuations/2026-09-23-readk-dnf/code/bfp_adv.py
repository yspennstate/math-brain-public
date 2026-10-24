import math, numpy as np
from biased_feiplus import feiplus
from readk_nonmono import random_nonmono
from feicore import polite
polite()
rng = np.random.default_rng(77)
def ratio(n, terms, mu):
    Hp, Inf, Var, _ = feiplus(n, terms, mu)
    ex = Inf - Var
    return Hp / ex if ex > 1e-13 else 0.0
best_overall = (0, None)
for trial in range(40):
    n = int(rng.choice([8, 10, 12])); k = int(rng.choice([1, 2, 3]))
    wl = list(rng.integers(1, 5, size=int(rng.integers(3, 9))))
    terms = random_nonmono(n, k, wl, rng, pneg=float(rng.choice([0.0, 0.5])))
    if not terms: continue
    # logit-parametrised biases, hill climb
    z = rng.normal(size=n) * 2
    mu = np.tanh(z); r = ratio(n, terms, mu)
    for it in range(150):
        z2 = z.copy(); j = rng.integers(n); z2[j] += rng.normal() * 1.5
        z2 = np.clip(z2, -6, 6)
        mu2 = np.tanh(z2); r2 = ratio(n, terms, mu2)
        if r2 > r: z, mu, r = z2, mu2, r2
    if r > best_overall[0]:
        best_overall = (r, (n, k, [(int(m), int(v)) for m, v in terms], [round(float(x), 5) for x in mu]))
    if trial % 10 == 9: print('trial', trial + 1, 'best so far', round(best_overall[0], 3), flush=True)
print('BEST ratio', round(best_overall[0], 4))
print('instance', best_overall[1])
