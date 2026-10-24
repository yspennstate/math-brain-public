"""Find a witness for the step constant by descending a restriction tree.

For any f, max over f's OWN restriction tree of rho_0 >= H(f)/I(f):  if every g met on the
way down had rho_0(g) < R, induction would give H(f) < R I(f).  So:
  step 1  build read-once trees with H/I as large as we can (beam on the ratio; cheap, no restrictions)
  step 2  descend from the best, always taking the minimising coordinate, recording max rho_0 seen.
"""
import sys, time
import ro
from fast import rho0_fast, analyse_c, canon, ceiling
from beam import grow

def ratio_beam(nmax, beam, budget):
    t0 = time.time()
    frontier = [ro.lit(0)]; best = (0.0, None)
    for n in range(2, nmax+1):
        cand = {}
        for t in frontier:
            for c in grow(t, n-1):
                k = canon(c)
                if k in cand: continue
                p, I, H = analyse_c(c)
                if I <= 0: continue
                cand[k] = (H/I, c)
        if not cand: break
        ranked = sorted(cand.values(), key=lambda z: -z[0])
        frontier = [z[1] for z in ranked[:beam]]
        if ranked[0][0] > best[0]: best = ranked[0]
        if n % 10 == 0 or n == nmax:
            print("  ratio beam n=%-4d best H/I = %.6f   [%.0fs]" % (n, ranked[0][0], time.time()-t0))
            sys.stdout.flush()
        if time.time()-t0 > budget: break
    return best

def descend(t, log):
    """always restrict the minimising coordinate; record the max rho_0 met"""
    best = 0.0; best_t = None; depth = 0
    while True:
        r, rows, (p, I, H) = rho0_fast(t)
        if r is None: break
        if r > best: best, best_t = r, t
        n = len(set(ro.leaves(t)))
        log.write("  depth %-4d n=%-6d H/I=%8.5f  rho_0=%9.6f  maxInf=%.6f\n"
                  % (depth, n, H/I if I else 0, r, max(x[0] for x in rows)))
        # rebuild the row table with coordinate ids to pick the argmin
        argmin = None; bestr = None
        for i in sorted(set(ro.leaves(t))):
            t0 = ro.restrict(t, i, 0); t1 = ro.restrict(t, i, 1)
            p0, I0, H0 = analyse_c(t0); p1, I1, H1 = analyse_c(t1)
            inf_i = abs(p1-p0)
            if inf_i <= 1e-15: continue
            rr = (H - (H0+H1)/2.0)/inf_i
            if bestr is None or rr < bestr: bestr, argmin = rr, i
        if argmin is None: break
        # descend into the child that keeps the larger ratio
        c0 = ro.restrict(t, argmin, 0); c1 = ro.restrict(t, argmin, 1)
        pick = None; bestq = -1
        for c in (c0, c1):
            pc, Ic, Hc = analyse_c(c)
            if Ic > 1e-12 and Hc/Ic > bestq: bestq, pick = Hc/Ic, c
        if pick is None: break
        t = pick; depth += 1
        if depth > 400: break
    return best, best_t

if __name__ == '__main__':
    nmax = int(sys.argv[1]) if len(sys.argv)>1 else 120
    log = open("descend_log.txt", "w", encoding="utf-8")
    print("step 1: maximise H/I over read-once trees")
    ratio, t = ratio_beam(nmax, 30, 900)
    print("best H/I found: %.6f" % ratio)
    log.write("best H/I = %.6f on n=%d\n" % (ratio, len(set(ro.leaves(t)))))
    print("step 2: descend its restriction tree (guaranteed rho_0 >= %.4f somewhere)" % ratio)
    best, bt = descend(t, log)
    import pickle
    with open("witness.pkl","wb") as fh: pickle.dump({"root": t, "witness": bt, "rho0": best}, fh)
    msg = ("witness found: rho_0 = %.6f   (guarantee was >= H/I = %.6f; target beta(1/2) = 6.4547837)"
           % (best, ratio))
    print(msg); log.write(msg+"\n"); log.close()
