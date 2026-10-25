"""What actually makes a random symmetric +-1 matrix singular / corank >= 2 at n = 8..13?

  'equal-or-opposite column pair' == a support-2 kernel vector e_i -+ e_j.
  Conjectural picture: singularity is dominated by ONE such pair (prob ~ n^2 2^{-n});
  corank >= 2 by TWO disjoint ones (prob ~ n^4 4^{-n}).  Test it.
  Rank is computed EXACTLY over GF(p) for a large prime p (an upper bound on the rational
  rank; equality fails only if p divides an elementary divisor, checked by using two primes).
"""
import numpy as np, sys, time
rng = np.random.default_rng(90210)
P1, P2 = 2147483647, 2147483629   # two large primes

def rank_modp(A, p):
    A = A.astype(np.int64) % p
    n, m = A.shape; r = 0
    for c in range(m):
        piv = None
        for i in range(r, n):
            if A[i, c] % p: piv = i; break
        if piv is None: continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), p-2, p)
        A[r] = (A[r]*inv) % p
        col = A[r+1:, c].copy()
        nz = np.nonzero(col)[0]
        if len(nz):
            A[r+1:][nz] = (A[r+1:][nz] - np.outer(col[nz], A[r])) % p
        r += 1
        if r == n: break
    return r

def run(n, trials, chunk=100000):
    c = dict(S1=0, S2=0, S1_has2=0, S2_has2disj=0, S2_no2=0, S2_has2=0, pairs_hist={})
    done = 0
    while done < trials:
        m = min(chunk, trials-done); done += m
        U = rng.integers(0,2,size=(m, n*(n+1)//2)).astype(np.int8)*2-1
        Ms = np.zeros((m,n,n), dtype=np.int8)
        t=0
        for i in range(n):
            for j in range(i,n):
                Ms[:,i,j]=U[:,t]; Ms[:,j,i]=U[:,t]; t+=1
        # exact screen for singularity: float det tiny
        d = np.abs(np.linalg.det(Ms.astype(np.float64)))
        cand = np.nonzero(d < 0.5)[0]
        for r in cand:
            A = Ms[r].astype(np.int64)
            rk = rank_modp(A.copy(), P1)
            rk2 = rank_modp(A.copy(), P2)
            rk = max(rk, rk2)          # rational rank >= max of the two mod-p ranks
            co = n - rk
            if co < 1: continue
            # support-2 kernel vectors: columns equal or opposite
            pairs = []
            for i in range(n):
                for j in range(i+1, n):
                    if np.array_equal(A[:,i], A[:,j]) or np.array_equal(A[:,i], -A[:,j]):
                        pairs.append((i,j))
            c['S1'] += 1
            if pairs: c['S1_has2'] += 1
            if co >= 2:
                c['S2'] += 1
                if pairs: c['S2_has2'] += 1
                else:     c['S2_no2'] += 1
                disj = any(len({a,b,x,y})==4 for ii,(a,b) in enumerate(pairs) for (x,y) in pairs[ii+1:])
                if disj: c['S2_has2disj'] += 1
                c['pairs_hist'][len(pairs)] = c['pairs_hist'].get(len(pairs),0)+1
    return c, done

for n, tr in [(8,400000),(9,400000),(10,600000),(11,800000),(12,1200000),(13,2000000)]:
    t0=time.time()
    c, done = run(n, tr)
    P1s = c['S1']/done; P2s = c['S2']/done
    print(f"n={n:2d} trials={done} ({time.time()-t0:.0f}s)")
    print(f"   P(singular)  = {P1s:.4e}   /(n^2 2^-n) = {P1s/(n*n*2.0**-n):7.3f}   with a support-2 kernel vector: {c['S1_has2']/max(c['S1'],1):.3f}")
    print(f"   P(corank>=2) = {P2s:.4e}   /(n^4 4^-n) = {P2s/(n**4*4.0**-n):7.3f}   has>=2 disjoint support-2: {c['S2_has2disj']/max(c['S2'],1):.3f}   has NO support-2: {c['S2_no2']/max(c['S2'],1):.3f}")
    print(f"   #support-2 pairs histogram among corank>=2: {dict(sorted(c['pairs_hist'].items()))}")
    sys.stdout.flush()
