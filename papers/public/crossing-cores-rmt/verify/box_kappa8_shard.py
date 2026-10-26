"""Research-box shard runner for the kappa_8^T exact volume sweep.

Takes the orbit file, selects keys[shard::nshards] in sorted order, computes
each dihedral representative's exact Toeplitz polytope volume with a process
pool, and checkpoints results atomically.  Stdlib only.

Run:  python3 -u box_kappa8_shard.py --shard 0 --nshards 4 --workers 8
"""
import sys, os, json, time, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

def _worker(key):
    from exact_volume import pairing_volume_exact
    pm = tuple(int(x) for x in key.split("-"))
    return key, str(pairing_volume_exact(pm, "T"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orbits", default=os.path.join(HERE, "kappa8_orbits_T.json"))
    ap.add_argument("--shard", type=int, required=True)
    ap.add_argument("--nshards", type=int, required=True)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    out = a.out or os.path.join(HERE, f"kappa8_T_shard{a.shard}of{a.nshards}.json")

    with open(a.orbits, encoding="utf-8") as f:
        orbits = json.load(f)["orbits"]
    keys = sorted(orbits)[a.shard::a.nshards]
    done = {}
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            done = json.load(f)
    todo = [k for k in keys if k not in done]
    print(f"shard {a.shard}/{a.nshards}: {len(keys)} keys, {len(done)} done, "
          f"{len(todo)} to go, workers {a.workers}", flush=True)
    if todo:
        import multiprocessing as mp
        t0 = time.time()
        with mp.Pool(a.workers) as pool:
            for i, (key, vol) in enumerate(
                    pool.imap_unordered(_worker, todo, chunksize=8)):
                done[key] = vol
                if (i + 1) % 200 == 0 or (i + 1) == len(todo):
                    with open(out + ".tmp", "w", encoding="utf-8") as f:
                        json.dump(done, f)
                    os.replace(out + ".tmp", out)
                    rate = (i + 1) / (time.time() - t0) * 3600
                    eta = (len(todo) - i - 1) / max(rate, 1) * 60
                    print(f"{i+1}/{len(todo)} ({rate:.0f}/h, eta {eta:.0f} min)",
                          flush=True)
    with open(out + ".tmp", "w", encoding="utf-8") as f:
        json.dump(done, f)
    os.replace(out + ".tmp", out)
    print(f"SHARD {a.shard} DONE: {len(done)} volumes", flush=True)

if __name__ == "__main__":
    main()
