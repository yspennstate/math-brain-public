"""Full recomputation of every moment in the paper, two independent lanes.

Lane 1 (direct): for each order 2k <= 14 and each ensemble, sweep ALL pairings
(dihedral-orbit reduced), compute each polytope volume exactly, and sum.
This reproduces Theorem 11.1 from scratch.

Lane 2 (core): sweep only the REDUCED pairings at r <= 7 pairs, compute the
primitive masses kappa_r^E geometrically, and rebuild every moment through
order fourteen via the Catalan inflation formula (6.2),
    m_{2k} = Cat_k + sum_{r=2}^{k} C(2k, k-r) kappa_r^E.
The two lanes traverse different polytopes; their agreement, plus the match
with the printed table, is the cross-derivation.

Checkpointed per stage: results land in rerun_moments_results.json atomically;
a rerun skips completed stages after verifying the stored payload parses.

Run:  python -u rerun_moments_full.py
"""
import sys, os, json, time
from fractions import Fraction as Fr
from math import comb, factorial

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact

OUT = os.path.join(HERE, "rerun_moments_results.json")

def cat(k):
    return comb(2 * k, k) // (k + 1)

def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r

EXPECT_T = {2: Fr(1), 4: Fr(8, 3), 6: Fr(11), 8: Fr(908, 15), 10: Fr(415),
            12: Fr(23840, 7), 14: Fr(325719, 10)}
EXPECT_H = {2: Fr(1), 4: Fr(2), 6: Fr(11, 2), 8: Fr(281, 15), 10: Fr(2717, 36),
            12: Fr(1052, 3), 14: Fr(1331087, 720)}
EXPECT_KT = {2: Fr(2, 3), 3: Fr(2), 4: Fr(178, 15), 5: Fr(253, 3),
             6: Fr(24798, 35), 7: Fr(206797, 30)}
EXPECT_KH = {2: Fr(0), 3: Fr(1, 2), 4: Fr(11, 15), 5: Fr(131, 36),
             6: Fr(83, 5), 7: Fr(63907, 720)}

def load():
    if os.path.exists(OUT):
        with open(OUT, encoding="utf-8") as f:
            return json.load(f)
    return {}

def save(res):
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1, sort_keys=True)
    os.replace(tmp, OUT)

def is_reduced(pm):
    n = len(pm)
    return all(pm[i] != (i + 1) % n and pm[i] != (i - 1) % n for i in range(n))

def sweep(pairings, kind):
    orbits = tk_core.orbit_reps(pairings)
    total = Fr(0)
    hist = {}
    per_orbit = {}
    for rep, size in orbits.items():
        v = pairing_volume_exact(rep, kind)
        total += size * v
        key = str(v)
        hist[key] = hist.get(key, 0) + size
        per_orbit["-".join(str(x) for x in rep)] = [str(v), size]
    return total, hist, per_orbit, len(orbits)

def word_key(tag):
    return tag

def main():
    res = load()
    stages = []
    for k in (2, 3, 4, 5):
        stages.append(("direct", "T", 2 * k))
        stages.append(("direct", "H", 2 * k))
    for r in range(2, 8):
        stages.append(("reduced", "T", r))
        stages.append(("reduced", "H", r))
    stages.append(("direct", "H", 12))
    stages.append(("direct", "H", 14))
    stages.append(("direct", "T", 12))
    stages.append(("direct", "T", 14))

    for mode, kind, nn in stages:
        tag = f"{mode}_{kind}{nn}"
        if tag in res:
            print(f"skip {tag} (checkpointed)", flush=True)
            continue
        t0 = time.time()
        if mode == "direct":
            gen = tk_core.all_pairings(nn) if kind == "T" else tk_core.parity_pairings(nn)
            total, hist, per_orbit, norb = sweep(gen, kind)
            npair = sum(hist.values())
            expect = (EXPECT_T if kind == "T" else EXPECT_H)[nn]
            status = "OK" if total == expect else f"MISMATCH expected {expect}"
            print(f"{tag}: m = {total}  [{status}]  pairings={npair} orbits={norb} "
                  f"({time.time()-t0:.1f}s)", flush=True)
            res[tag] = {"moment": str(total), "match": total == expect,
                        "pairings": npair, "orbits": norb, "hist": hist,
                        "per_orbit": per_orbit, "elapsed_s": round(time.time() - t0, 1)}
        else:
            n2 = 2 * nn
            gen = tk_core.all_pairings(n2) if kind == "T" else tk_core.parity_pairings(n2)
            reduced = (pm for pm in gen if is_reduced(pm))
            total, hist, per_orbit, norb = sweep(reduced, kind)
            npair = sum(hist.values())
            expect = (EXPECT_KT if kind == "T" else EXPECT_KH)[nn]
            status = "OK" if total == expect else f"MISMATCH expected {expect}"
            print(f"{tag}: kappa_{nn} = {total}  [{status}]  reduced={npair} orbits={norb} "
                  f"({time.time()-t0:.1f}s)", flush=True)
            res[tag] = {"kappa": str(total), "match": total == expect,
                        "reduced_words": npair, "orbits": norb, "hist": hist,
                        "per_orbit": per_orbit, "elapsed_s": round(time.time() - t0, 1)}
        save(res)

    # final synthesis: lane-2 moments from geometric kappas
    print("\n--- lane 2: moments rebuilt from geometric primitive masses ---", flush=True)
    ok_all = True
    for kind, expect_m in (("T", EXPECT_T), ("H", EXPECT_H)):
        kap = {}
        for r in range(2, 8):
            tag = f"reduced_{kind}{r}"
            kap[r] = Fr(res[tag]["kappa"])
        for k in range(1, 8):
            m = cat(k) + sum(comb(2 * k, k - r) * kap[r] for r in range(2, min(k, 7) + 1))
            want = expect_m[2 * k]
            ok = (m == want)
            ok_all &= ok
            print(f"lane2 m_{2*k}^{kind} = {m}  [{'OK' if ok else 'FAIL, expected ' + str(want)}]",
                  flush=True)
    # lane 1 vs lane 2 vs paper
    print("\nRERUN COMPLETE:", "ALL MOMENTS MATCH" if ok_all and
          all(res[f"direct_{kk}{2*k}"]["match"] for kk in "TH" for k in range(2, 8))
          else "MISMATCHES PRESENT", flush=True)

if __name__ == "__main__":
    main()
