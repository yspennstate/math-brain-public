"""Independent check of F5's LTF theorem and its extension to regular (2-monotone) functions.
Written from the statements only (not from F5's code)."""
import math, numpy as np
from feicore import spectrum, entropy, total_influence, popcounts, polite
polite()
L1 = 2*math.log(3*math.sqrt(3/math.pi)) + 2
a = (1+math.sqrt(1+4/L1))/2
C1 = 3 + (1 + math.log(a/(a-1)) + a*L1)/math.log(2)


def ltf(w, theta, n):
    xs = np.arange(1 << n)
    bits = ((xs[:, None] >> np.arange(n)[None, :]) & 1)*2-1  # +-1
    s = bits @ w - theta
    return np.where(s > 0, 1, -1).astype(np.int8)    # sgn with sgn(0) = -1


def shifted_upset(n, rng, m=None, maxsize=None):
    """up-closure of the left-shift closure of a random family: regular monotone,
    coordinate 0 most desirable.  Returns tt with -1 = true."""
    N = 1 << n
    m = m or int(rng.integers(1, 6))
    fam = set()
    for _ in range(m):
        k = int(rng.integers(1, (maxsize or n)+1))
        A = 0
        for j in rng.choice(n, size=k, replace=False):
            A |= 1 << int(j)
        fam.add(A)
    stack = list(fam)
    while stack:
        A = stack.pop()
        for j in range(n):
            if A >> j & 1:
                for i in range(j):
                    if not (A >> i & 1):
                        B = (A & ~(1 << j)) | (1 << i)
                        if B not in fam:
                            fam.add(B)
                            stack.append(B)
    true = np.zeros(N, dtype=bool)
    xs = np.arange(N)
    for A in fam:
        true |= (xs & A) == A
    return np.where(true, -1, 1).astype(np.int8)


def is_regular_order(tt, n):
    """i < j  =>  i at least as desirable as j (true = -1)."""
    xs = np.arange(1 << n)
    T = (tt == -1)
    for i in range(n):
        for j in range(i+1, n):
            base = xs & ~((1 << i) | (1 << j))
            a1 = T[base | (1 << i)]
            a2 = T[base | (1 << j)]
            if np.any(a2 & ~a1):
                return False
    return True


def pivotal_antichain_ok(tt, n, order):
    """For every i and every assignment outside U_i u {i}: pivotal set of i inside the
    U_i cube (U_i = predecessors) is an antichain, for the orientation 'true is up'."""
    T = (tt == -1)
    pos = {c: k for k, c in enumerate(order)}
    xs = np.arange(1 << n)
    for i in range(n):
        piv = T[xs | (1 << i)] & ~T[xs & ~(1 << i)]
        for j in order[:pos[i]]:
            # a covering pair y < y + e_j inside the pivotal set would break the antichain
            lo = xs[(xs >> j & 1) == 0]
            if np.any(piv[lo] & piv[lo | (1 << j)]):
                return False
    return True


def check(tt, n, order):
    """order: coordinates, most desirable first. U_i = predecessors of i."""
    P = spectrum(tt)
    H = entropy(P)
    I = total_influence(P, n)
    if I < 1e-12:
        return None
    pc = popcounts(n)
    idx = np.arange(1 << n)
    pos = {c: k for k, c in enumerate(order)}
    worst3 = 0.0
    worst2 = 0.0
    Sigma = 0.0
    for i in range(n):
        Umask = 0
        for c in order[:pos[i]]:
            Umask |= 1 << c
        N = pos[i] + 1
        sel = (idx >> i) & 1 == 1
        Pi = P[sel]
        Ti = idx[sel] & ~(1 << i)
        Inf = Pi.sum()
        if Inf < 1e-15 or N < 2:
            continue
        k = pc[Ti & Umask]
        lhs3 = float((Pi*np.log(N/(k+1))).sum())
        worst3 = max(worst3, lhs3/(L1*Inf))
        for c in (0.5, 1, 2, 4, N/3):
            if c > N:
                continue
            rho = 1 - c/N
            stab = float((Pi * rho**k).sum())
            worst2 = max(worst2, stab/((2/math.sqrt(math.pi))*c**-0.5*Inf))
    r = np.zeros(n)
    for c, k in pos.items():
        r[c] = k+1
    for S in np.nonzero(P > 1e-300)[0]:
        s = pc[S]
        if s == 0:
            continue
        Sigma += P[S]*sum(max(0.0, math.log(r[j]/s)) for j in range(n) if S >> j & 1)
    return dict(H=H, I=I, HI=H/I, L2=worst2, L3=worst3, L4=Sigma/(L1*I), T1=H/(C1*I))


if __name__ == '__main__':
    rng = np.random.default_rng(11)
    print('C1 =', C1, ' L1 =', L1)
    agg = {}

    def upd(tag, res):
        if res is None:
            return
        a_ = agg.setdefault(tag, {k: 0.0 for k in ('HI', 'L2', 'L3', 'L4', 'T1')})
        a_.setdefault('cnt', 0)
        for k in ('HI', 'L2', 'L3', 'L4', 'T1'):
            a_[k] = max(a_[k], res[k])
        a_['cnt'] += 1

    bad_anti = 0
    for n in range(3, 13):
        for t in range(60):
            kind = t % 3
            if kind == 0:
                w = rng.normal(size=n)
            elif kind == 1:
                w = rng.integers(-6, 7, size=n).astype(float)
            else:
                w = np.sign(rng.normal(size=n)) * rng.pareto(1.0, size=n)
            if np.all(w == 0):
                continue
            theta = rng.normal()*np.sqrt((w**2).sum())*0.7
            tt = ltf(w, theta, n)
            order = list(np.argsort(-np.abs(w), kind='stable'))
            upd('LTF', check(tt, n, order))
    for n in range(3, 14):
        for t in range(40):
            tt = shifted_upset(n, rng, m=int(rng.integers(1, 8)))
            assert is_regular_order(tt, n)
            if not pivotal_antichain_ok(tt, n, list(range(n))):
                bad_anti += 1
            upd('regular', check(tt, n, list(range(n))))
    print('regular functions whose pivotal sets failed the antichain test:', bad_anti)
    for k, v in agg.items():
        print(k, {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()})
