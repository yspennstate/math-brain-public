from __future__ import annotations
import hashlib, json, math
from decimal import Decimal, getcontext
from fractions import Fraction
import numpy as np

EXPECTED_SHA = 'f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839'
CORE_HEX = 'fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000'
HOSTS = [[78,79],[113,121],[228,484],[170,186],[149,151],[338,466],[284,316],[291,295],[393,457]]
C_SEED_LOWER = '6.521845710923046575658143972948578468366662292'


def fwht(a: np.ndarray) -> np.ndarray:
    a = np.array(a, dtype=np.int64, copy=True)
    h = 1
    while h < a.size:
        x = a.reshape(-1, 2*h)
        l = x[:, :h].copy(); r = x[:, h:].copy()
        x[:, :h] = l + r; x[:, h:] = l - r
        h *= 2
    return a


def entropy(p: np.ndarray) -> float:
    z = p[p > 0]
    return float(-np.sum(z*np.log2(z)))


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0: return 0.0
    return -p*math.log2(p) - (1-p)*math.log2(1-p)


def eta(p: float) -> float:
    s = min(p, 1-p)
    q = 0.5 + math.sqrt(max(0.0, s*(1-s)))
    return 1.0 - h2(q)


def make_seed() -> np.ndarray:
    base = int(CORE_HEX, 16)
    core = np.array([-1 if (base >> x) & 1 else 1 for x in range(512)], dtype=np.int64)
    tab = np.tile(core, (1 << 9, 1))
    aux = np.arange(1 << 9)
    for j, cells in enumerate(HOSTS):
        mask = (aux & (1 << j)) != 0
        tab[np.ix_(mask, np.array(cells, dtype=int))] = -1
    tab = tab.ravel()
    digest = hashlib.sha256(','.join(map(str, tab)).encode()).hexdigest()
    assert digest == EXPECTED_SHA
    return tab


def selector_metrics(tab: np.ndarray) -> dict:
    N = tab.size; n = N.bit_length()-1; idx = np.arange(N)
    W = fwht(tab); p = (W.astype(np.float64)/N)**2
    assert int(np.dot(W.astype(object), W.astype(object))) == N*N
    H = entropy(p)
    alpha = []
    bitmask = []
    for i in range(n):
        b = ((idx >> i) & 1).astype(bool); bitmask.append(b)
        alpha.append(float(p[b].sum()))
    Phi = sum(eta(a) for a in alpha)
    rows = []
    for i in range(n):
        b = bitmask[i]
        vp = tab[~b]; vm = tab[b]
        Wp = fwht(vp); Wm = fwht(vm)
        pp = (Wp.astype(np.float64)/(N//2))**2
        pm = (Wm.astype(np.float64)/(N//2))**2
        dH = H - 0.5*(entropy(pp)+entropy(pm))
        low = idx[~b]
        x = p[low]; y = p[low + (1 << i)]; m = x+y
        nz = m > 0; q = np.zeros_like(m); q[nz] = y[nz]/m[nz]
        hh = np.zeros_like(m); mid = (q > 0) & (q < 1)
        hh[mid] = -q[mid]*np.log2(q[mid])-(1-q[mid])*np.log2(1-q[mid])
        B = float(np.sum(m*hh)); JS = dH-B
        phip = 0.0; phim = 0.0; ridx = np.arange(N//2)
        for ri in range(n-1):
            rb = ((ridx >> ri) & 1).astype(bool)
            phip += eta(float(pp[rb].sum())); phim += eta(float(pm[rb].sum()))
        dPhi = Phi - 0.5*(phip+phim)
        dE = dH-dPhi
        rows.append({'coordinate':i,'alpha':alpha[i], 'B_over_alpha':B/alpha[i],
                     'JS_over_alpha':JS/alpha[i], 'DeltaPhi_over_alpha':dPhi/alpha[i],
                     'Delta_corrected_over_alpha':dE/alpha[i]})
    return {'truth_table_sha256':EXPECTED_SHA, 'H_float':H, 'I_float':sum(alpha),
            'Phi_float':Phi, 'rows':rows,
            'existential_corrected_ratio_float':min(r['Delta_corrected_over_alpha'] for r in rows)}


def ln2_fraction_bounds(N: int = 80) -> tuple[Fraction,Fraction]:
    z = Fraction(1,3)
    s = 2*sum(z**(2*k+1)/Fraction(2*k+1) for k in range(N))
    R = 2*z**(2*N+1)/((2*N+1)*(1-z*z))
    return s, s+R


def decimal_fraction(q: Fraction) -> Decimal:
    return Decimal(q.numerator)/Decimal(q.denominator)


def exact_decimal_fraction(s: str) -> Fraction:
    a,b = s.split('.')
    return Fraction(int(a+b), 10**len(b))


def barrier_certificate() -> dict:
    getcontext().prec = 90
    llo,lhi = ln2_fraction_bounds(80)
    c_lo = Fraction(2,1)/lhi
    c_hi = Fraction(2,1)/llo
    C = exact_decimal_fraction(C_SEED_LOWER)
    barrier = C-c_hi
    infl = Fraction(261,128)
    finite = {}
    for r in [1,2,3,5,8,10,15,20]:
        factor = 1-Fraction(1,1)/(infl**r)
        finite[str(r)] = str(decimal_fraction(C*factor-c_hi))
    return {
      'ln2_lower':str(decimal_fraction(llo)), 'ln2_upper':str(decimal_fraction(lhi)),
      'two_over_ln2_lower':str(decimal_fraction(c_lo)), 'two_over_ln2_upper':str(decimal_fraction(c_hi)),
      'external_seed_amplified_H_over_I_lower':C_SEED_LOWER,
      'corrected_selector_asymptotic_lower':str(decimal_fraction(barrier)),
      'finite_r_corrected_ratio_lower_using_Phi_le_2_over_ln2_I':finite,
      'note':'All numbers in this certificate are obtained from exact Fractions; C_SEED_LOWER is the already-rigorous lower endpoint from the external-seed reconstruction.'
    }


if __name__ == '__main__':
    out = {'selector_diagnostic':selector_metrics(make_seed()), 'rigorous_barrier':barrier_certificate()}
    rows = out['selector_diagnostic']['rows']
    out['selector_diagnostic']['core_type'] = rows[0]
    out['selector_diagnostic']['aux_type'] = rows[9]
    del out['selector_diagnostic']['rows']
    print(json.dumps(out, indent=2, sort_keys=True))
