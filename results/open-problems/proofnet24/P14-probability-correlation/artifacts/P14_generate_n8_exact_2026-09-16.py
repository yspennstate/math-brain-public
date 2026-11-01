#!/usr/bin/env python3
"""Resumable exact isomorph-free generation of all simple graphs on 8 vertices.

Coverage argument: every 8-vertex graph is obtained by deleting one vertex,
choosing the isomorphism class of the resulting 7-vertex graph, then choosing
one of the 2^7 neighbourhoods of the new vertex.  NetworkX graph_atlas_g()
contains all 1044 unlabeled simple 7-vertex graphs.  Isomorphism invariants are
used only as a prefilter; every candidate in the same invariant bucket is
compared with nx.is_isomorphic(), so no nonisomorphic candidate is discarded.

Run repeatedly with a chunk size, e.g.
  python P14_generate_n8_exact_2026-09-16.py --reset --chunk 250
  python P14_generate_n8_exact_2026-09-16.py --chunk 250   # repeat to done
The state and final graph6 catalog are deterministic for NetworkX 3.6.1.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, os, pickle, platform, time
from pathlib import Path
import networkx as nx
from networkx.algorithms.graph_hashing import weisfeiler_lehman_graph_hash

HERE = Path(__file__).resolve().parent
STATE = HERE / "P14_n8_generation_state.pkl"
CATALOG = HERE / "P14_forest_rayleigh_n8_2026-09-16.g6"
MANIFEST = HERE / "P14_forest_rayleigh_n8_generation_2026-09-16.json"
EXPECTED_N7 = 1044
EXPECTED_N8 = 12346  # McKay/nauty all-simple-graph count, independently checked in report.


def invkey(g: nx.Graph):
    deg = dict(g.degree())
    tri = nx.triangles(g)
    nbr = {v: set(g[v]) for v in range(8)}
    vertex_profile = tuple(sorted(
        (deg[v], tri[v], sum(deg[u] for u in nbr[v]),
         tuple(sorted(deg[u] for u in nbr[v]))) for v in range(8)
    ))
    pair_profile = tuple(sorted(
        (1 if g.has_edge(u, v) else 0, *sorted((deg[u], deg[v])),
         len(nbr[u] & nbr[v]))
        for u in range(8) for v in range(u + 1, 8)
    ))
    # WL hashes are only isomorphism-invariant prefilters, never certificates.
    return (
        g.number_of_edges(), vertex_profile, pair_profile,
        weisfeiler_lehman_graph_hash(g, iterations=4),
        weisfeiler_lehman_graph_hash(nx.complement(g), iterations=4),
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunk", type=int, default=250)
    ap.add_argument("--reset", action="store_true")
    args = ap.parse_args()
    if args.reset:
        for p in (STATE, CATALOG, MANIFEST):
            if p.exists(): p.unlink()

    base = [nx.convert_node_labels_to_integers(g) for g in nx.graph_atlas_g()
            if len(g) == 7]
    assert len(base) == EXPECTED_N7

    if STATE.exists():
        reps, buckets, done, iso_tests = pickle.loads(STATE.read_bytes())
    else:
        reps, buckets, done, iso_tests = [], {}, 0, 0

    start = done
    end = min(len(base), start + args.chunk)
    t0 = time.time()
    for bi in range(start, end):
        g7 = base[bi]
        for mask in range(1 << 7):
            g = g7.copy()
            g.add_node(7)
            for v in range(7):
                if mask >> v & 1:
                    g.add_edge(7, v)
            key = invkey(g)
            bucket = buckets.setdefault(key, [])
            found = False
            for idx in bucket:
                iso_tests += 1
                if nx.is_isomorphic(g, reps[idx]):
                    found = True
                    break
            if not found:
                bucket.append(len(reps))
                reps.append(g)
    done = end
    STATE.write_bytes(pickle.dumps((reps, buckets, done, iso_tests), pickle.HIGHEST_PROTOCOL))

    rec = {
        "chunk_start": start, "chunk_end": end,
        "n7_classes_consumed": done, "representatives_so_far": len(reps),
        "exact_isomorphism_tests": iso_tests,
        "elapsed_seconds_this_chunk": time.time() - t0,
    }
    print(json.dumps(rec, sort_keys=True))

    if done == len(base):
        assert len(reps) == EXPECTED_N8
        with CATALOG.open("wb") as f:
            for g in reps:
                f.write(nx.to_graph6_bytes(g, header=False))
        data = CATALOG.read_bytes()
        lines = data.splitlines()
        assert len(lines) == EXPECTED_N8 and len(set(lines)) == EXPECTED_N8
        manifest = {
            "generator": "7-vertex atlas + all 2^7 new-vertex neighbourhoods + exact isomorphism deduplication",
            "networkx_version": nx.__version__,
            "python_version": platform.python_version(),
            "n7_unlabeled_classes": len(base),
            "candidate_extensions": len(base) * (1 << 7),
            "n8_unlabeled_representatives": len(reps),
            "expected_n8_mckay_count": EXPECTED_N8,
            "exact_isomorphism_tests": iso_tests,
            "invariant_bucket_count": len(buckets),
            "maximum_nonisomorphic_representatives_in_one_prefilter_bucket": max(map(len, buckets.values())),
            "graph6_lines": len(lines),
            "graph6_unique_lines": len(set(lines)),
            "graph6_sha256": hashlib.sha256(data).hexdigest(),
            "edge_count_min": min(g.number_of_edges() for g in reps),
            "edge_count_max": max(g.number_of_edges() for g in reps),
            "result": "PASS",
        }
        MANIFEST.write_text(json.dumps(manifest, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(manifest, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
