"""Finite grid stable allocation on a flat torus, with independently audited stability.

Centre-proposing Gale--Shapley; every site has mass h^2 and each centre an
integer quota round(alpha/h^2). Preference lists use periodic Euclidean distance.
No cutoff in the allocation: lists double on demand up to the entire site set.
"""
import os
for _key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)

from collections import deque
import argparse
import csv
import json
from pathlib import Path
import resource
import time
import numpy as np
from scipy.spatial import cKDTree
from scipy import ndimage

ROOT = Path(__file__).resolve().parents[1]

def sites_for(L, resolution):
    n = round(L * resolution)
    axis = (np.arange(n) + .5) / resolution
    xx, yy = np.meshgrid(axis, axis)
    return np.column_stack((xx.ravel(), yy.ravel())), n

class Preferences:
    def __init__(self, centres, sites, L, initial_k):
        self.centres, self.sites, self.L = centres, sites, L
        self.tree = cKDTree(sites, boxsize=L)
        k = min(len(sites), max(2, initial_k))
        self.dist, self.idx = self.tree.query(centres, k=k, workers=1)
        self.extra = {}

    def get(self, centre, rank):
        dist, idx = self.extra.get(centre, (self.dist[centre], self.idx[centre]))
        if rank >= len(idx):
            k = min(len(self.sites), max(rank + 1, len(idx) * 2))
            dist, idx = self.tree.query(self.centres[centre], k=k, workers=1)
            self.extra[centre] = (dist, idx)
        return int(idx[rank]), float(dist[rank])

def allocate(pref, quota):
    ncentres, nsites = len(pref.centres), len(pref.sites)
    owner = np.full(nsites, -1, dtype=np.int32)
    distance = np.full(nsites, np.inf)
    held = np.zeros(ncentres, dtype=np.int64)
    rank = np.zeros(ncentres, dtype=np.int64)
    queue = deque(range(ncentres))
    queued = np.ones(ncentres, dtype=bool)
    proposals = 0
    while queue:
        centre = queue.popleft()
        queued[centre] = False
        while held[centre] < quota and rank[centre] < nsites:
            site, dist = pref.get(centre, int(rank[centre]))
            rank[centre] += 1
            proposals += 1
            previous = owner[site]
            if dist < distance[site] or (dist == distance[site] and centre < previous):
                if previous >= 0:
                    held[previous] -= 1
                    if not queued[previous]:
                        queued[previous] = True
                        queue.append(int(previous))
                owner[site] = centre
                distance[site] = dist
                held[centre] += 1
    return owner, distance, held, proposals

def audit_stability(pref, quota, owner, distance, held):
    """Enumerate geometric balls independently of the proposal preference lists."""
    radius = np.zeros(len(pref.centres))
    assigned = owner >= 0
    np.maximum.at(radius, owner[assigned], distance[assigned])
    radius[held < quota] = np.sqrt(2) * pref.L
    violations, checked = 0, 0
    # Audit one centre at a time to avoid storing millions of Python integers.
    for centre in range(len(pref.centres)):
        neighbours_c = pref.tree.query_ball_point(pref.centres[centre], radius[centre] + 1e-11, workers=1)
        idx = np.asarray(neighbours_c, dtype=np.int64)
        delta = np.abs(pref.sites[idx] - pref.centres[centre])
        delta = np.minimum(delta, pref.L - delta)
        ds = np.sqrt(np.einsum("ij,ij->i", delta, delta))
        desires = (owner[idx] != centre) & (ds < distance[idx] - 1e-10)
        covets = (held[centre] < quota) | (ds < radius[centre] - 1e-10)
        violations += int(np.count_nonzero(desires & covets))
        checked += len(idx)
    actual = np.bincount(owner[assigned], minlength=len(held))
    assert np.array_equal(actual, held)
    assert np.all(held <= quota)
    assert int(assigned.sum()) == min(len(owner), len(held) * quota)
    assert violations == 0, violations
    return {"blocking_pairs": violations, "audit_pairs": checked,
            "max_audit_radius": float(radius.max(initial=0))}

class PeriodicComponents:
    """Contract planar labels, then add seams with integer winding potentials."""
    def __init__(self, sizes):
        n = len(sizes)
        self.parent = np.arange(n)
        self.size = sizes.astype(np.int64)
        self.shift = np.zeros((n, 2), dtype=np.int64)
        self.wrap = np.zeros((n, 2), dtype=bool)

    def find(self, x):
        p = self.parent[x]
        if p != x:
            r, sh = self.find(int(p))
            self.shift[x] += sh
            self.parent[x] = r
        return int(self.parent[x]), self.shift[x].copy()

    def join(self, a, b, offset):
        if a == 0 or b == 0:
            return
        ra, sa = self.find(int(a))
        rb, sb = self.find(int(b))
        discrepancy = sa + np.asarray(offset) - sb
        if ra == rb:
            self.wrap[ra] |= discrepancy != 0
        else:
            if self.size[ra] < self.size[rb]:
                self.parent[ra] = rb
                self.shift[ra] = -discrepancy
                self.size[rb] += self.size[ra]
                self.wrap[rb] |= self.wrap[ra]
            else:
                self.parent[rb] = ra
                self.shift[rb] = discrepancy
                self.size[ra] += self.size[rb]
                self.wrap[ra] |= self.wrap[rb]

def components(mask, connectivity=4):
    n = mask.shape[0]
    structure = ndimage.generate_binary_structure(2, 1 if connectivity == 4 else 2)
    labels, _ = ndimage.label(mask, structure)
    sizes = np.bincount(labels.ravel())
    sizes[0] = 0
    uf = PeriodicComponents(sizes)
    offsets = [0] if connectivity == 4 else [-1, 0, 1]
    for i in range(n):
        for delta in offsets:
            j = (i + delta) % n
            tile = (i + delta) // n
            uf.join(labels[i, -1], labels[j, 0], (1, tile))
            uf.join(labels[-1, i], labels[0, j], (tile, 1))
    roots = np.flatnonzero(uf.parent == np.arange(len(sizes)))
    roots = roots[roots != 0]
    total = int(mask.sum())
    largest = int(uf.size[roots].max(initial=0))
    wraps = uf.wrap[roots].any(axis=0) if len(roots) else np.zeros(2, dtype=bool)
    return {"largest": largest, "largest_fraction_torus": largest / mask.size,
            "largest_fraction_phase": largest / total if total else 0.,
            "components": len(roots), "wrap_x": int(wraps[0]),
            "wrap_y": int(wraps[1]), "wrap_any": int(wraps.any())}

def run(L, resolution, seeds, alphas, output):
    sites, n = sites_for(L, resolution)
    output = ROOT / "data" / output
    rows = []
    for seed in seeds:
        rng = np.random.default_rng(seed)
        ncentres = int(rng.poisson(L * L))
        centres = rng.uniform(0, L, (ncentres, 2))
        np.savetxt(ROOT / "data" / f"centres_L{L:g}_seed{seed}.csv", centres,
                   delimiter=",", header="x,y", comments="", fmt="%.17g")
        initial_k = int(max(alphas) * resolution**2 * 4) + 16
        pref = Preferences(centres, sites, L, initial_k)
        for alpha in alphas:
            start = time.monotonic()
            quota = int(np.floor(alpha * resolution**2 + .5))
            owner, distance, held, proposals = allocate(pref, quota)
            audit = audit_stability(pref, quota, owner, distance, held)
            row = {"L": L, "resolution": resolution, "grid_n": n, "seed": seed,
                   "centres": ncentres, "density": ncentres / L**2,
                   "alpha_requested": alpha, "quota": quota,
                   "alpha_grid": quota / resolution**2,
                   "claimed_fraction": float(np.mean(owner >= 0)),
                   "unsated_centres": int(np.count_nonzero(held < quota)),
                   "proposals": proposals, **audit}
            for conn in (4, 8):
                for phase, mask in (("claimed", owner >= 0), ("vacant", owner < 0)):
                    values = components(mask.reshape(n, n), conn)
                    row.update({f"{phase}{conn}_{k}": v for k, v in values.items()})
            row["seconds"] = round(time.monotonic() - start, 3)
            # ru_maxrss is bytes on macOS, KiB on Linux; record platform too.
            row["peak_rss_native"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            rows.append(row)
            with output.open("w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)
            print(json.dumps({k: row[k] for k in ("L", "resolution", "seed", "alpha_requested", "alpha_grid", "claimed_fraction", "claimed4_wrap_any", "vacant4_wrap_any", "seconds")}), flush=True)
            if L == 64 and seed == 100 and alpha in (.7, .9):
                np.savez_compressed(ROOT / "data" / f"allocation_L64_r{resolution}_seed100_a{alpha}.npz",
                                    owner=owner.reshape(n, n), centres=centres, L=L, resolution=resolution, quota=quota)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--L", type=float, default=64)
    parser.add_argument("--resolution", type=int, default=8)
    parser.add_argument("--seeds", type=int, nargs="+", default=[100, 101, 102, 103])
    parser.add_argument("--alphas", type=float, nargs="+", default=[.2, .4, .55, .6, .65, .68, .7, .72, .75, .8, .9, .95])
    parser.add_argument("--output", default="torus_L64_r8.csv")
    args = parser.parse_args()
    run(args.L, args.resolution, args.seeds, args.alphas, args.output)
