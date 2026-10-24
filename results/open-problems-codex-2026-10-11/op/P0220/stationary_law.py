"""P0220 finite-determinant stationary joint survival law.
Observations are (threshold, particle_index), with index >= 1 and threshold >= 0.
Requires mpmath. Proof: FINITE_DETERMINANT.md. No historical novelty claim.
"""
import mpmath as mp
from fractions import Fraction

def number(x):
    if isinstance(x, Fraction):
        return mp.mpf(x.numerator)/x.denominator
    if isinstance(x, str) and '/' in x:
        return number(Fraction(x))
    return mp.mpf(str(x))

def prepare(observations):
    at = {}
    for t, k in observations:
        if isinstance(k, bool) or int(k) != k or k < 1:
            raise ValueError('particle index must be a positive integer')
        t = number(t)
        if not mp.isfinite(t) or t < 0:
            raise ValueError('threshold must be finite and nonnegative')
        if t:
            at[t] = min(int(k), at.get(t, int(k)))
    obs = sorted(at.items())
    ks = [k for t, k in obs]
    for a in range(len(ks)-2, -1, -1):
        ks[a] = min(ks[a], ks[a+1])
    return [(obs[a][0], ks[a]) for a in range(len(obs))]

def poisson_entry(u, y, x):
    return u**(y-x)/mp.factorial(y-x) if y >= x else mp.mpf(0)

def terminal_entry(u, a, b):
    if not u:
        return 1/mp.factorial(a-b) if a >= b else mp.mpf(0)
    return u**(mp.mpf(b-a)/2)*mp.besseli(abs(a-b), 2*mp.sqrt(u))

def matrix_for(observations):
    obs = prepare(observations)
    if not obs:
        return None, mp.mpf(0), 0, 0
    T, final_k = obs[-1]
    d = final_k-1
    markers = [(t, x) for t, k in obs[:-1] for x in range(d-k+1)]
    q = len(markers)
    if not d:
        return None, T, d, q
    M = mp.matrix(d+q)
    for i in range(d):
        for j in range(d):
            M[i,j] = terminal_entry(T,i,j)
        for a,(t,x) in enumerate(markers):
            M[i,d+a] = poisson_entry(t,x,i)
    for a,(t,x) in enumerate(markers):
        for j in range(d):
            M[d+a,j] = -terminal_entry(T-t,x,j)
        for b,(s,y) in enumerate(markers):
            M[d+a,d+b] = -poisson_entry(s-t,y,x) if t < s else 0
    return M,T,d,q

def survival(observations, precision=60):
    with mp.workdps(precision):
        M,T,d,q = matrix_for(observations)
        return mp.exp(-T)*(mp.det(M) if M is not None else 1)

if __name__ == '__main__':
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('observations',help='JSON list of [threshold,index] pairs')
    parser.add_argument('--precision',type=int,default=60)
    args=parser.parse_args()
    obs=json.loads(args.observations)
    with mp.workdps(args.precision):
        M,T,d,q=matrix_for(obs)
        value=mp.exp(-T)*(mp.det(M) if M is not None else 1)
        print(json.dumps({'survival_probability':mp.nstr(value,args.precision),
                          'matrix_dimension':d+q,'terminal_row_cap':d},indent=2))
