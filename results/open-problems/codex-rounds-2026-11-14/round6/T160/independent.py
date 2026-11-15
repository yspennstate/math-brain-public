"""Independent cluster/cut recursion and cluster-conditioned reconstruction.

Recomputes every saved cluster and residual atom from induced-subgraph
connectivity probabilities and closed edge boundaries. No audit imports.
"""
from collections import defaultdict
from fractions import Fraction as Q
import json
import os
from pathlib import Path
import resource
import signal
import time

signal.alarm(120)
start = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"

# Graphs deliberately transcribed independently of audit.py's data structures.
cases = [
    ("inner_return", ((0,1),(2,3),(0,3),(1,4),(4,2),(3,5),(4,6),(5,6),(6,7)), (7,)),
    ("outer_return", ((0,1),(0,2),(1,3),(2,4),(3,5),(5,4),(4,6)), (6,)),
    ("background_cycle", ((0,1),(0,2),(2,3),(1,3),(1,4),(2,5),(3,5),(4,5),
                           (4,6),(5,7),(6,7),(7,8),(6,8)), (8,)),
    ("two_targets", ((0,1),(0,2),(2,3),(1,4),(2,5),(3,6),
                      (4,7),(5,8),(6,9),(7,8),(8,9)), (7,9)),
    ("isolated_background", ((0,1),(0,2),(2,3),(1,4),(2,5),(3,5),
                             (4,6),(5,7),(7,8),(8,5),(6,9)), (9,)),
]
regions = {
    "inner_return": (3,6,(0,1,2,3),(1,2,3),(4,5)),
    "outer_return": (2,4,(0,1,2),(1,2),(3,4)),
    "background_cycle": (4,8,(0,1,2,3),(1,2,3),(4,5)),
    "two_targets": (3,6,(0,1,2,3),(1,2,3),(4,5,6)),
    "isolated_background": (3,6,(0,1,2,3),(1,2,3),(4,5)),
}


def closure(edges,mask,size):
    rows = [1 << j for j in range(size)]
    for j,(u,v) in enumerate(edges):
        if mask >> j & 1:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
    for k in range(size):
        for i in range(size):
            if rows[i] >> k & 1:
                rows[i] |= rows[k]
    return rows


def probability(mask,size,p):
    return p**mask.bit_count()*(1-p)**(size-mask.bit_count())
saved = {(row["graph"],row["p"]): row for row in json.loads(Path("certificates.json").read_text())}
values = recurrences = distributions = 0
for name,edges,targets in cases:
    vertex_count = 1+max(v for e in edges for v in e)
    full = (1 << vertex_count)-1
    target_bits = sum(1 << v for v in targets)
    ni,nr,I,S,R = regions[name]
    Ibits,Rbits = sum(1 << v for v in I),sum(1 << v for v in R)
    edge_bits = [(1 << u,1 << v) for u,v in edges]
    for p in (Q(1,3),Q(1,2),Q(2,3)):
        closed_powers = [(1-p)**j for j in range(len(edges)+1)]
        conn = {}
        # For an induced set W containing 0, its root component A partitions
        # all configurations: 1=sum_{A subset W,0 in A} conn(A)*(1-p)^cut_W(A).
        # Invert this triangular identity to compute conn(W).
        for W in range(1,1 << vertex_count,2):
            subtotal = Q(0)
            subset = (W-1) & W
            while subset:
                if subset & 1:
                    other = W ^ subset
                    cut = sum(bool((a & subset and b & other) or (b & subset and a & other))
                              for a,b in edge_bits)
                    subtotal += conn[subset]*closed_powers[cut]
                    recurrences += 1
                subset = (subset-1) & W
            conn[W] = 1-subtotal
            assert 0 <= conn[W] <= 1
        unnormalized = {}
        outside = {}
        for W,c in conn.items():
            if not W & target_bits or not c:
                continue
            notW = full ^ W
            cut = sum(bool((a & W and b & notW) or (b & W and a & notW))
                      for a,b in edge_bits)
            unnormalized[W] = c*closed_powers[cut]
            outside[W] = sum(1 << j for j,(a,b) in enumerate(edge_bits)
                             if a & notW and b & notW)
        arm = sum(unnormalized.values())
        record = saved[name,str(p)]
        assert arm == Q(record["event"])
        values += 1
        cluster = {W:v/arm for W,v in unnormalized.items()}
        assert {str(k):str(v) for k,v in cluster.items()} == record["cluster_mass"]
        values += len(cluster)
        record_sum = defaultdict(Q)
        bad = trace_error = Q(0)
        exact_joint, local_joint = defaultdict(Q),defaultdict(Q)
        for key,value in record["root_record_mass"].items():
            W,tau = map(int,key.split(":"))
            notW = full ^ W
            internal = sum(1 << j for j,(a,b) in enumerate(edge_bits) if a & W and b & W)
            assert tau & internal == tau
            reached = 1
            while True:
                nxt = reached
                for j,(a,b) in enumerate(edge_bits):
                    if tau >> j & 1 and (a | b) & reached:
                        nxt |= a | b
                if nxt == reached:
                    break
                reached = nxt
            assert reached == W and W & target_bits
            cut = sum(bool((a & W and b & notW) or (b & W and a & notW))
                      for a,b in edge_bits)
            expected = p**tau.bit_count()*(1-p)**(internal.bit_count()-tau.bit_count()+cut)/arm
            assert expected == Q(value)
            record_sum[W] += expected
            values += 1
            local_root = closure(edges,tau & ((1 << nr)-1),vertex_count)[0]
            mismatch = (local_root & Ibits) != (W & Ibits)
            trace_error += expected*mismatch
            free = outside[W]
            sigma = free
            while True:
                weight = expected*p**sigma.bit_count()*(1-p)**(free.bit_count()-sigma.bit_count())
                configuration = tau | sigma
                annulus_mask = (configuration >> ni) & ((1 << (nr-ni))-1)
                rows = closure(edges[ni:nr],annulus_mask,vertex_count)
                N = len({rows[s] for s in S if rows[s] & Rbits})
                bad += weight*(N >= 2)
                imask = configuration & ((1 << ni)-1)
                exact_joint[imask,W & Ibits] += weight
                local_joint[imask,local_root & Ibits] += weight
                if sigma == 0:
                    break
                sigma = (sigma-1) & free
        assert record_sum == cluster
        joint_tv = sum(abs(exact_joint.get(k,0)-local_joint.get(k,0))
                       for k in exact_joint.keys() | local_joint.keys())/2
        assert trace_error == Q(record["trace_error"])
        assert bad == Q(record["conditional_bad"])
        assert joint_tv == Q(record["joint_TV"])
        assert conn[Ibits] == Q(record["a_star"])
        for end,label,targets_bits in ((nr,"local_arm",Rbits),(len(edges),"far_arm",target_bits)):
            total = Q(0)
            for mask in range(1 << (end-ni)):
                rows = closure(edges[ni:end],mask,vertex_count)
                total += probability(mask,end-ni,p)*any(rows[s] & targets_bits for s in S)
            assert total == Q(record[label])
        values += 6
        residual = defaultdict(Q)
        for W,c in cluster.items():
            free = outside[W]
            nfree = free.bit_count()
            sigma = free
            while True:
                assert sigma & free == sigma
                residual[sigma] += c*p**sigma.bit_count()*(1-p)**(nfree-sigma.bit_count())
                if sigma == 0:
                    break
                sigma = (sigma-1) & free
        assert dict(residual) == {int(k):Q(v) for k,v in record["residual_mass"].items()}
        assert sum(cluster.values()) == sum(residual.values()) == 1
        values += len(residual)
        distributions += 1
print(f"PASS: {recurrences} independent induced-subgraph connectivity recurrence terms")
print(f"PASS: {values} exact event, cluster, full-record, residual and localization values independently reproduced")
print(f"PASS: {distributions} cluster/cut factorizations and residual product-mixture laws")
print("Vertex-set recursion, closed cuts and cluster-conditioned reconstruction; no audit imports.")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
print(f"Priority: {os.getpriority(os.PRIO_PROCESS,0)}; OMP_NUM_THREADS=1")
print(f"Elapsed seconds: {time.monotonic()-start:.3f}")
print(f"Peak RSS bytes: {rss}")
print("PASS: all independent cluster-background checks")
