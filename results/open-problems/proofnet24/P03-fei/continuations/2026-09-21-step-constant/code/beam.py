"""Beam search over read-once AND/OR trees maximising the restriction-step constant
   rho_0(f) = min_i Delta_i H / Inf_i.
The implication to test: for a restriction-closed class C,
   sup_{f in C} rho_0(f) >= C_FEI(C),
so on read-once (C_RO = beta(1/2) = 6.4547837 numerically) the sup must reach 6.4548.
Exhaustive search reaches only 5.77 at n=11 and balanced trees plateau near 6.08,
so the witness is deep. This grows trees leaf by leaf, keeping the best."""
import sys, time, pickle
import ro
from fast import rho0_fast, canon, ceiling

def positions(t, path=()):
    """every subtree location, as a path of 1/2 child indices"""
    yield path
    if t[0] in ('and', 'or'):
        yield from positions(t[1], path+(1,))
        yield from positions(t[2], path+(2,))

def get(t, path):
    for k in path: t = t[k]
    return t

def put(t, path, new):
    if not path: return new
    k = path[0]
    kids = [t[1], t[2]]
    kids[k-1] = put(t[k], path[1:], new)
    return (t[0], kids[0], kids[1])

def grow(t, nxt):
    """all trees obtained by replacing one subtree S with (S op newleaf)"""
    out = []
    leaf = ro.lit(nxt)
    for pth in positions(t):
        sub = get(t, pth)
        for op in ('and', 'or'):
            out.append(put(t, pth, (op, sub, leaf)))
    return out

def run(nmax=46, beam=40, budget=3000):
    t0 = time.time()
    frontier = [ro.lit(0)]
    best_overall = (0.0, None)
    log = open("beam_log.txt", "w")
    for n in range(2, nmax+1):
        cand = {}
        for t in frontier:
            for c in grow(t, n-1):
                key = canon(c)
                if key in cand: continue
                r, rows, (p, I, H) = rho0_fast(c)
                if r is None: continue
                cand[key] = (r, c, p, I, H, max(x[0] for x in rows))
        if not cand: break
        ranked = sorted(cand.values(), key=lambda z: -z[0])
        frontier = [z[1] for z in ranked[:beam]]
        r, c, p, I, H, delta = ranked[0]
        if r > best_overall[0]: best_overall = (r, c)
        line = ("n=%-3d cands=%-7d best rho_0=%9.6f   H/I=%7.4f  Pr=%.4f  maxInf=%.6f  ceil=%8.2f  [%.0fs]"
                % (n, len(cand), r, H/I if I else 0, p, delta, ceiling(delta), time.time()-t0))
        print(line); log.write(line+"\n"); log.flush(); sys.stdout.flush()
        if time.time()-t0 > budget:
            log.write("BUDGET REACHED\n"); break
    log.write("BEST rho_0 = %.6f  (target beta(1/2)=6.4547837)\n" % best_overall[0])
    log.close()
    with open("beam_best.pkl","wb") as fh: pickle.dump(best_overall, fh)
    print("BEST rho_0 = %.6f" % best_overall[0])

if __name__ == '__main__':
    run(nmax=int(sys.argv[1]) if len(sys.argv)>1 else 46,
        beam=int(sys.argv[2]) if len(sys.argv)>2 else 40,
        budget=float(sys.argv[3]) if len(sys.argv)>3 else 3000)
