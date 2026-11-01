"""Order-sixteen primitive masses: exact computation of kappa_8^H and
kappa_8^T, the only unknowns in

    m_16 = Cat_8 + sum_{r=2}^{8} C(16, 8-r) kappa_r,

with kappa_2..kappa_7 already verified twice (paper table (6.6), and the
geometric reduced-core sweep).  This decides the paper's stated next target:
by (13.2), gamma_T fails the order-sixteen free conditional-positivity test
iff  m_16(gamma_T) < 3863516832738344459/10908088231950.  The known part of
m_16 is Cat_8 + sum_{r<8} C(16,8-r) kappa_r = 29362422/105, so the test
comes down to whether kappa_8^T reaches roughly 74546.15; the exact
comparison is done at synthesis below.

Method: enumerate the reduced (ear-free) pairings on sixteen slots, reduce
by the dihedral group, compute each core polytope volume exactly with the
frozen engine, and sum size-weighted volumes.  Hankel first (4738 reduced
parity-mixing words), then Toeplitz (c_8^T words).  Checkpointed; a pool of
worker processes computes volumes in parallel at inherited BelowNormal
priority.

Run:  python -u compute_kappa8.py [workers]
"""
import sys, os, json, time
from fractions import Fraction as Fr
from math import comb, factorial

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
import tk_core

def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r

def cat(k):
    return comb(2 * k, k) // (k + 1)

KAPPA = {  # verified r <= 7 (identities + geometric rerun)
    "T": {2: Fr(2, 3), 3: Fr(2), 4: Fr(178, 15), 5: Fr(253, 3),
          6: Fr(24798, 35), 7: Fr(206797, 30)},
    "H": {2: Fr(0), 3: Fr(1, 2), 4: Fr(11, 15), 5: Fr(131, 36),
          6: Fr(83, 5), 7: Fr(63907, 720)},
}
THRESH = Fr(3863516832738344459, 10908088231950)  # (13.2)

def is_reduced(pm):
    n = len(pm)
    return all(pm[i] != (i + 1) % n and pm[i] != (i - 1) % n for i in range(n))

def orbit_file(kind):
    return os.path.join(HERE, f"kappa8_orbits_{kind}.json")

def result_file(kind):
    return os.path.join(HERE, f"kappa8_volumes_{kind}.json")

def enumerate_orbits(kind):
    path = orbit_file(kind)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        print(f"{kind}: orbit file present ({d['n_orbits']} orbits, "
              f"{d['n_words']} words)", flush=True)
        return d
    t0 = time.time()
    gen = tk_core.all_pairings(16) if kind == "T" else tk_core.parity_pairings(16)
    orbits = {}
    n_words = 0
    for pm in gen:
        if not is_reduced(pm):
            continue
        n_words += 1
        c = tk_core.canonical(pm)
        orbits[c] = orbits.get(c, 0) + 1
    d = {"kind": kind, "n_words": n_words, "n_orbits": len(orbits),
         "orbits": {"-".join(map(str, k)): v for k, v in orbits.items()}}
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(d, f)
    os.replace(tmp, path)
    print(f"{kind}: enumerated {n_words} reduced words, {len(orbits)} orbits "
          f"({time.time()-t0:.1f}s)", flush=True)
    return d

def _vol_worker(args):
    key, kind = args
    from exact_volume import pairing_volume_exact
    pm = tuple(int(x) for x in key.split("-"))
    v = pairing_volume_exact(pm, kind)
    return key, str(v)

def compute(kind, workers):
    d = enumerate_orbits(kind)
    orbits = d["orbits"]
    res_path = result_file(kind)
    done = {}
    if os.path.exists(res_path):
        with open(res_path, encoding="utf-8") as f:
            done = json.load(f)
    todo = [k for k in orbits if k not in done]
    print(f"{kind}: {len(done)} done, {len(todo)} to compute", flush=True)
    if todo:
        import multiprocessing as mp
        t0 = time.time()
        with mp.Pool(workers) as pool:
            batch = []
            for i, (key, vol) in enumerate(
                    pool.imap_unordered(_vol_worker, [(k, kind) for k in todo],
                                        chunksize=4)):
                done[key] = vol
                if (i + 1) % 200 == 0 or (i + 1) == len(todo):
                    tmp = res_path + ".tmp"
                    with open(tmp, "w", encoding="utf-8") as f:
                        json.dump(done, f)
                    os.replace(tmp, res_path)
                    rate = (i + 1) / (time.time() - t0)
                    eta = (len(todo) - i - 1) / rate / 3600
                    print(f"{kind}: {i+1}/{len(todo)} volumes "
                          f"({rate*3600:.0f}/h, eta {eta:.2f}h)", flush=True)
        tmp = res_path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(done, f)
        os.replace(tmp, res_path)
    # synthesis
    kap = Fr(0)
    for key, size in orbits.items():
        kap += Fr(done[key]) * size
    print(f"\nkappa_8^{kind} = {kap}  (= {float(kap):.6f})", flush=True)
    m16 = cat(8) + sum(comb(16, 8 - r) * KAPPA[kind][r] for r in range(2, 8)) + kap
    print(f"m_16(gamma_{kind}) = {m16}  (= {float(m16):.6f})", flush=True)
    if kind == "T":
        print(f"threshold (13.2)  = {THRESH}  (= {float(THRESH):.4f})", flush=True)
        if m16 < THRESH:
            print("VERDICT: m16 BELOW the Schur threshold -> gamma_T is NOT "
                  "freely infinitely divisible (order-16 test fails)", flush=True)
        else:
            print("VERDICT: m16 at or above the threshold -> the order-16 "
                  "conditional-positivity test PASSES; free infinite "
                  "divisibility of gamma_T remains open", flush=True)
    return kap, m16

if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    print(f"workers: {workers}", flush=True)
    compute("H", workers)
    compute("T", workers)
    print("KAPPA8 COMPUTATION COMPLETE", flush=True)
