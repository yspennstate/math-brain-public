"""Independent direct computation of m_16(gamma_H): sweep ALL 8! = 40320
parity-mixing pairings on sixteen slots (dihedral-orbit reduced), sum exact
polytope volumes.  Cross-checks the reduced-core route
    m_16 = Cat_8 + sum_r C(16, 8-r) kappa_r^H
computed by compute_kappa8.py through a different set of polytopes.

Checkpointed like the kappa sweep.  Run:  python -u direct_H16.py [workers]
"""
import sys, os, json, time
from fractions import Fraction as Fr
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
import tk_core

ORB = os.path.join(HERE, "H16_direct_orbits.json")
RES = os.path.join(HERE, "H16_direct_volumes.json")

def cat(k):
    return comb(2 * k, k) // (k + 1)

def enumerate_orbits():
    if os.path.exists(ORB):
        with open(ORB, encoding="utf-8") as f:
            return json.load(f)
    t0 = time.time()
    orbits = {}
    n = 0
    for pm in tk_core.parity_pairings(16):
        n += 1
        c = tk_core.canonical(pm)
        orbits[c] = orbits.get(c, 0) + 1
    d = {"n_words": n, "n_orbits": len(orbits),
         "orbits": {"-".join(map(str, k)): v for k, v in orbits.items()}}
    with open(ORB + ".tmp", "w", encoding="utf-8") as f:
        json.dump(d, f)
    os.replace(ORB + ".tmp", ORB)
    print(f"enumerated {n} parity words, {len(orbits)} orbits "
          f"({time.time()-t0:.1f}s)", flush=True)
    return d

def _worker(key):
    from exact_volume import pairing_volume_exact
    pm = tuple(int(x) for x in key.split("-"))
    return key, str(pairing_volume_exact(pm, "H"))

def main(workers):
    d = enumerate_orbits()
    orbits = d["orbits"]
    done = {}
    if os.path.exists(RES):
        with open(RES, encoding="utf-8") as f:
            done = json.load(f)
    todo = [k for k in orbits if k not in done]
    print(f"{len(done)} done, {len(todo)} to compute", flush=True)
    if todo:
        import multiprocessing as mp
        t0 = time.time()
        with mp.Pool(workers) as pool:
            for i, (key, vol) in enumerate(
                    pool.imap_unordered(_worker, todo, chunksize=4)):
                done[key] = vol
                if (i + 1) % 50 == 0 or (i + 1) == len(todo):
                    with open(RES + ".tmp", "w", encoding="utf-8") as f:
                        json.dump(done, f)
                    os.replace(RES + ".tmp", RES)
                    rate = (i + 1) / (time.time() - t0) * 3600
                    print(f"{i+1}/{len(todo)} ({rate:.0f}/h)", flush=True)
    m16 = Fr(0)
    for key, size in orbits.items():
        m16 += Fr(done[key]) * size
    print(f"\nDIRECT m_16(gamma_H) = {m16}  (= {float(m16):.6f})", flush=True)
    print(f"words counted: {sum(orbits.values())} (expect 40320)", flush=True)

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
