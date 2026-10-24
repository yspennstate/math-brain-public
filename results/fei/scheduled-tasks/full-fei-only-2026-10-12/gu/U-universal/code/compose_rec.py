"""Exact recursion for H, U, I of read-once compositions (EVIDENCE: floating logs).
For f = g(h_1,...,h_k) with independent inner functions of means mu_j, the spectral law of f is
P_g^{mu}(J) * prod_{j in J} q_j(T_j)  (q_j = nonempty-normalised spectral law of h_j), so
H(f) = H(P_g^mu) + sum_j P(j in J) H(q_j),  U(f) = U(P_g^mu) + sum_j P(j in J) U(q_j),  I(f) = sum_j P(j in J) E_{q_j}|T|.
(U factorises because upper sets factorise: pi(S) = pi_g(J) prod_{j in J} pi_{q_j}(T_j).)"""
import numpy as np, itertools, math

def biased_spectrum(g, mus):
    """g: dict from tuple of +-1 to +-1; mus: input means.  Returns dict J(tuple of 0/1) -> ghat(J)."""
    k = len(mus); sig = [math.sqrt(1 - m * m) for m in mus]; out = {}
    for J in itertools.product([0, 1], repeat=k):
        s = 0.0
        for y in itertools.product([1, -1], repeat=k):
            w = 1.0; ph = 1.0
            for j in range(k):
                w *= (1 + mus[j] * y[j]) / 2
                if J[j]: ph *= (y[j] - mus[j]) / sig[j]
            s += w * g[y] * ph
        out[J] = s
    return out

def law_stats(P):
    """P: dict J->prob on subsets of [k] (tuples). Returns H, U (with upper sets), P(j in J)."""
    H = -sum(p * math.log2(p) for p in P.values() if p > 0)
    U = 0.0
    for J, p in P.items():
        if p <= 0: continue
        pi = sum(q for K, q in P.items() if all(K[j] >= J[j] for j in range(len(J))))
        U += p * math.log2(pi / p)
    k = len(next(iter(P)))
    marg = [sum(p for J, p in P.items() if J[j]) for j in range(k)]
    return H, U, marg

def compose_step(g, inputs):
    """inputs: list of dicts with keys mu, Hq, Uq, Iq.  Returns the same summary for f = g(inputs) plus H,U,I of f."""
    mus = [d['mu'] for d in inputs]
    gh = biased_spectrum(g, mus); P = {J: c * c for J, c in gh.items()}
    Hg, Ug, marg = law_stats(P)
    H = Hg + sum(marg[j] * inputs[j]['Hq'] for j in range(len(inputs)))
    U = Ug + sum(marg[j] * inputs[j]['Uq'] for j in range(len(inputs)))
    I = sum(marg[j] * inputs[j]['Iq'] for j in range(len(inputs)))
    p0 = P[tuple([0] * len(inputs))]; mu = gh[tuple([0] * len(inputs))]
    hb = 0.0 if p0 in (0.0, 1.0) else -(p0 * math.log2(p0) + (1 - p0) * math.log2(1 - p0))
    Hq = (H - hb) / (1 - p0); Uq = (U - (p0 * math.log2(1 / p0) if p0 > 0 else 0.0)) / (1 - p0); Iq = I / (1 - p0)
    return dict(mu=mu, Hq=Hq, Uq=Uq, Iq=Iq, H=H, U=U, I=I, Var=1 - p0)

X = dict(mu=0.0, Hq=0.0, Uq=0.0, Iq=1.0)
AND = {(a, b): (-1 if (a == -1 and b == -1) else 1) for a in (1, -1) for b in (1, -1)}
OR = {(a, b): (-1 if (a == -1 or b == -1) else 1) for a in (1, -1) for b in (1, -1)}

def chain(pattern, n):
    """lexicographic-type chain: f_1 = x; f_{t+1} = gate_t(x_new, f_t)."""
    cur = dict(X); res = None
    for t in range(n - 1):
        gate = AND if pattern[t % len(pattern)] == 'A' else OR
        res = compose_step(gate, [dict(X), cur]); cur = res
    return res

if __name__ == "__main__":
    # sanity: compare with brute force for small chains
    import sys; sys.path.insert(0, '.')
    from feilib import spectrum, entropy, total_influence
    from upward import Uprime
    def brute_chain(pattern, n):
        N = 1 << n; xs = np.arange(N); vals = 1 - 2 * (xs & 1)
        for t in range(1, n):
            xt = 1 - 2 * ((xs >> t) & 1)
            if pattern[(t - 1) % len(pattern)] == 'A': vals = np.where((xt == -1) & (vals == -1), -1, 1)
            else: vals = np.where((xt == -1) | (vals == -1), -1, 1)
        p = spectrum(vals); return float(entropy(p)), float(Uprime(p, n)), float(total_influence(p, n))
    for pat in ['A', 'AO', 'AAO']:
        r = chain(pat, 8); b = brute_chain(pat, 8)
        print('check', pat, 'rec H,U,I =', round(r['H'], 9), round(r['U'], 9), round(r['I'], 9), ' brute =', [round(v, 9) for v in b])
    best = []
    for L in range(1, 8):
        for pat in itertools.product('AO', repeat=L):
            pat = ''.join(pat); r = chain(pat, 400)
            best.append((r['H'] / r['I'], pat, r['U'] / r['I']))
    best.sort(reverse=True)
    for b in best[:8]: print('pattern', b[1], 'H/I=%.4f U/I=%.4f' % (b[0], b[2]))
