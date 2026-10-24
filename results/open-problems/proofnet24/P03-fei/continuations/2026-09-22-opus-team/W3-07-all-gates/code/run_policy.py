"""Policy check of a gate set against a stored fixed point.

usage: run_policy.py POT.npz SET [tag] [nstart]
  POT.npz  a potential on vicore's default grid (keys G, C) or any npz with xs, G, C (then that grid is used)
  SET      comma list of: and, xor, npn3, npn4, mono5, restr:<k>[-<k2>] (restrictions of Numaro's g by essential arity),
           g7, g
Writes logs/policy_<tag>.json and prints the gates sorted by their minimal defect D.
"""
import os, sys, json, time, pickle, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vicore as V
V.lowprio(4)
import policy as PO

TEAM = os.path.join(HERE, "..", "..")
REF = os.path.join(TEAM, "..", "2026-09-22-gate-reformulation")


class G_from:
    def __init__(self, path):
        d = np.load(path)
        self.C = float(d["C"])
        if "xs" in d.files and len(d["xs"]) != V.Grid().N:
            self.grid = V.Grid()
            self.grid.xs = np.asarray(d["xs"], float)
            self.grid.K = float(self.grid.xs[-1])
            self.grid.ps = 2.0 ** (-self.grid.xs)
            self.grid.N = len(self.grid.xs)
        else:
            self.grid = V.Grid()
        self.G = np.asarray(d["G"], float)


def g7_table():
    MIN = [(1, 3), (0, 4), (2, 3, 4), (0, 1, 5), (1, 4, 6), (2, 4, 6), (1, 5, 6)]
    return np.array([-1.0 if any(all((x >> i) & 1 for i in m) for m in MIN) else 1.0 for x in range(128)])


def depends_all(tt, k):
    n = 1 << k
    for i in range(k):
        if all(((tt >> x) & 1) == ((tt >> (x ^ (1 << i))) & 1) for x in range(n)):
            return False
    return True


def mono5_tables():
    """all monotone functions of 5 variables depending on every input, one per permutation class"""
    k = 5
    n = 32
    # monotone functions = up-sets; enumerate antichains via recursion on the Dedekind lattice (7581 functions)
    ups = []
    cells = list(range(n))
    subset = [[y for y in range(n) if (x & y) == x] for x in range(n)]     # supersets of x
    # generate all up-sets by closure of antichains: brute force over the 2^32 tables is too big; use the standard
    # recursion f(x5=0) <= f(x5=1) with monotone 4-variable functions
    def mono(kk):
        if kk == 0:
            return [0, 1]
        prev = mono(kk - 1)
        out = []
        m = 1 << (kk - 1)
        for a in prev:
            for b in prev:
                if a & ~b == 0:            # a <= b pointwise
                    out.append(a | (b << m))
        return out
    allm = mono(k)
    perms = list(itertools.permutations(range(k)))
    seen = set()
    reps = []
    for tt in allm:
        if tt in seen or not depends_all(tt, k):
            continue
        orb = set()
        for pm in perms:
            v = 0
            for x in range(n):
                if (tt >> x) & 1:
                    y = 0
                    for i in range(k):
                        if (x >> i) & 1:
                            y |= 1 << pm[i]
                    v |= 1 << y
            orb.add(v)
        seen |= orb
        reps.append(tt)
    return [V.pm_from_int(tt, k) for tt in reps], len(allm)


def gate_list(spec):
    out = []
    for item in spec.split(","):
        if item == "and":
            out.append(("AND2", np.array([1.0, 1.0, 1.0, -1.0])))
        elif item == "xor":
            out.append(("XOR2", np.array([1.0, -1.0, -1.0, 1.0])))
        elif item in ("npn3", "npn4"):
            k = int(item[-1])
            reps = np.load(os.path.join(REF, "npn_reps_k%d.npy" % k))
            for tt in reps:
                tt = int(tt)
                if depends_all(tt, k):
                    out.append(("npn%d_%d" % (k, tt), V.pm_from_int(tt, k)))
        elif item == "mono5":
            tabs, nall = mono5_tables()
            print("monotone 5-input functions: %d in all, %d permutation classes depending on every input" % (nall, len(tabs)))
            for i, t in enumerate(tabs):
                out.append(("mono5_%d" % i, t))
        elif item.startswith("restr:"):
            rng = item.split(":")[1]
            a, b = (rng.split("-") + [rng])[:2]
            d = pickle.load(open(os.path.join(TEAM, "F3-small-arity", "logs", "restr_gates.pkl"), "rb"))
            for k in range(int(a), int(b) + 1):
                for j, (vals, fr, asg) in enumerate(d.get(k, [])):
                    out.append(("restr%d_%d" % (k, j), np.asarray(vals, float)))
        elif item.startswith("restrtop:"):
            # the strongest violators of the read-once potential h96k40 in F3's restriction optimisation, one per
            # mirror pair (classes with equal D), N of them
            N = int(item.split(":")[1])
            d = pickle.load(open(os.path.join(TEAM, "F3-small-arity", "logs", "restr_gates.pkl"), "rb"))
            js = []
            for f in ("restr_opt_h96_k2_7.json", "restr_opt_h96_k8_10.json"):
                js += json.load(open(os.path.join(TEAM, "F3-small-arity", "logs", f)))
            js.sort(key=lambda r: r["D"])
            seenD = []
            for r in js:
                if len(seenD) >= N:
                    break
                if any(abs(r["D"] - x) < 1e-9 for x in seenD):
                    continue
                seenD.append(r["D"])
                vals = d[r["k"]][r["cls"]][0]
                out.append(("restr%d_%d" % (r["k"], r["cls"]), np.asarray(vals, float)))
        elif item == "g7":
            out.append(("G7", g7_table()))
        elif item == "g":
            g = np.load(os.path.join(TEAM, "inputs", "numaro18_pm1_table.npy")).astype(float)
            out.append(("g18", g))
    return out


if __name__ == "__main__":
    pot = G_from(sys.argv[1])
    spec = sys.argv[2]
    tag = sys.argv[3] if len(sys.argv) > 3 else "x"
    nstart = int(sys.argv[4]) if len(sys.argv) > 4 else 24
    gates = gate_list(spec)
    grid, G = pot.grid, pot.G
    print("potential %s  C = %.15f  V(1/2) = %.12f  gates: %d" % (sys.argv[1], pot.C, float(grid.V(G, 0.5)[0]), len(gates)),
          flush=True)
    rows = []
    t0 = time.time()
    for name, tab in gates:
        k = int(round(np.log2(len(tab))))
        if k > 12:
            continue
        r = PO.check_gate(tab, k, grid, G, nstart=nstart, maxsub=(None if k <= 10 else 3))
        c = -r["D"] / r["W"] if r["W"] > 1e-12 else float("nan")
        # smallest influence-weight at the optimum (a dead input means a smaller gate in disguise)
        buf = np.empty(1 << k); It = np.empty(k)
        V.gstats(tab, k, r["p"], buf, It)
        rows.append(dict(name=name, k=k, D=r["D"], c=c, W=r["W"], pout=r["pout"], p=[float(x) for x in r["p"]],
                         minIt=float(It.min()), screen=r["screen_min"]))
        print("  %-12s k=%2d  D_min %+.6e  c %+.4e  p_out %.6f  min It %.1e  (%.0f s)" % (name, k, r["D"], c, r["pout"],
              It.min(), time.time() - t0), flush=True)
    rows.sort(key=lambda z: z["D"])
    json.dump(dict(pot=sys.argv[1], C=pot.C, spec=spec, rows=rows), open(os.path.join(HERE, "..", "logs", "policy_%s.json" % tag), "w"),
              indent=1)
    print("sorted by D_min (most negative first):")
    for z in rows[:25]:
        print("  %-12s k=%2d  D %+.6e  c %+.4e  p_out %.6f  minIt %.1e  p=%s" % (z["name"], z["k"], z["D"], z["c"], z["pout"], z["minIt"],
              "[" + ", ".join("%.4f" % x for x in z["p"]) + "]"))
