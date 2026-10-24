# Aggregate the exact/MC results for P0133 and compare with the candidate formula
#   P_tau{a,b,a+b}  propto  exp(-(pi/2) (|a|^2+|b|^2+|a+b|^2) / y),  |c|^2 = |j + k tau|^2 for c=(j,k), tau = x+iy.
# For the n x m torus (n wide, m tall) tau = i m/n, so |(j,k)|^2/y = (j^2 (n/m) + k^2 (m/n)).
import json, glob, math, sys
from collections import defaultdict

def load(fn):
    d = json.load(open(fn, encoding="utf-8"))
    counts = {eval(k): v for k, v in d["counts"].items()}
    tot = d["ntrees"] if "ntrees" in d else d["nsamp"]
    return d, counts, tot

def orbit_key_square(key):
    # canonical representative of the D4 orbit of a triple (square torus only)
    def norm(c):
        cx, cy = c
        if cx < 0 or (cx == 0 and cy < 0): cx, cy = -cx, -cy
        return (cx, cy)
    best = None
    for (p, q, r, s) in [(1,0,0,1),(0,-1,1,0),(-1,0,0,-1),(0,1,-1,0),(1,0,0,-1),(-1,0,0,1),(0,1,1,0),(0,-1,-1,0)]:
        img = tuple(sorted(norm((p*c[0]+q*c[1], r*c[0]+s*c[1])) for c in key))
        if best is None or img < best: best = img
    return best

def cand_weight(key, n, m):
    if len(key) != 3: return 0.0
    y = m / n
    s = 0.0
    for (j, k) in key:
        s += (j*j + k*k*y*y) / y
    return math.exp(-(math.pi/2) * s)

def report(fn):
    d, counts, tot = load(fn)
    n, m = d["n"], d["m"]
    print(f"\n=== {fn}: {n}x{m}, total={tot}" + (f", bad={d['bad']}" if "bad" in d else ""))
    theta = sum(v for k, v in counts.items() if len(k) == 3)
    eight = sum(v for k, v in counts.items() if len(k) == 2)
    print(f"  P(theta)={theta/tot:.5f}  P(figure-eight)={eight/tot:.5f}")
    if n == m:
        orb = defaultdict(int)
        for k, v in counts.items():
            if len(k) == 3: orb[orbit_key_square(k)] += v
        Z = sum(cand_weight(k, n, m) * osize(k) for k in orb)  # candidate normalisation over observed orbits only
        print("  orbit (rep) : count  P  | candidate P (normalised over observed orbits)")
        for k, v in sorted(orb.items(), key=lambda kv: -kv[1])[:8]:
            cp = cand_weight(k, n, m) * osize(k) / Z
            err = math.sqrt(v) / tot
            print(f"   {k}: {v}  {v/tot:.5f} +- {err:.5f} | {cp:.5f}")
        # ratio of the two leading orbits
        k0 = ((0, 1), (1, 0), (1, 1)); k1 = ((1, 0), (1, 1), (2, 1))
        if k0 in orb and k1 in orb:
            r = orb[k1] / orb[k0]
            print(f"  ratio P(orbit {k1})/P(orbit {k0}) = {r:.5f}  (+- {r*math.sqrt(1/orb[k1]+1/orb[k0]):.5f});"
                  f" candidate = {cand_weight(k1,n,m)*osize(k1)/(cand_weight(k0,n,m)*osize(k0)):.5f}")
    else:
        # rectangular: classify theta triples of the form {(1,0),(k,1),(k+1,1)} by twist k
        tw = defaultdict(int); other = 0
        for key, v in counts.items():
            if len(key) != 3: continue
            ks = [c for c in key if c[1] == 1]
            if (1, 0) in key and len(ks) == 2 and abs(ks[0][0] - ks[1][0]) == 1:
                tw[min(ks[0][0], ks[1][0])] += v
            else:
                other += v
        T = sum(tw.values())
        print(f"  twist-type theta triples: {T/tot:.5f}; other theta: {other/tot:.5f}")
        mean = sum(k * v for k, v in tw.items()) / T
        var = sum((k + 0.5)**2 * v for k, v in tw.items()) / T
        # the triple {(1,0),(k,1),(k+1,1)} is symmetric under k -> -1-k; centre at -1/2
        print(f"  twist k: E[k]={mean:.4f}  E[(k+1/2)^2]={var:.4f}   L=m/n={m/n}: candidate L/(2 pi)+1/4={m/n/(2*math.pi)+0.25:.4f}"
              f"  [alt L/pi+1/4={m/n/math.pi+0.25:.4f}]")
        for k in sorted(tw): print(f"    k={k}: {tw[k]/tot:.5f}")

def osize(k):
    # orbit size under D4 of a triple (square torus)
    def norm(c):
        cx, cy = c
        if cx < 0 or (cx == 0 and cy < 0): cx, cy = -cx, -cy
        return (cx, cy)
    imgs = set()
    for (p, q, r, s) in [(1,0,0,1),(0,-1,1,0),(-1,0,0,-1),(0,1,-1,0),(1,0,0,-1),(-1,0,0,1),(0,1,1,0),(0,-1,-1,0)]:
        imgs.add(tuple(sorted(norm((p*c[0]+q*c[1], r*c[0]+s*c[1])) for c in k)))
    return len(imgs)

if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob("exact_*.json")) + sorted(glob.glob("mc_*.json"))
    for fn in files: report(fn)
