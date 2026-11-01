#!/usr/bin/env python3
from __future__ import annotations
import hashlib, itertools, json
from collections import Counter
from pathlib import Path
import networkx as nx

N=9
HERE=Path('/mnt/data')
OUT=HERE/'hard10_n9_dense_m33_36.g6'
MAN=HERE/'hard10_n9_dense_m33_36_manifest.json'
EDGES=list(itertools.combinations(range(N),2))
assert len(EDGES)==36

counts=Counter()
with OUT.open('wb') as f:
    for missing_k in range(4):
        for missing_idx in itertools.combinations(range(36),missing_k):
            missing=set(missing_idx)
            g=nx.Graph()
            g.add_nodes_from(range(N))
            g.add_edges_from(e for i,e in enumerate(EDGES) if i not in missing)
            m=g.number_of_edges()
            assert m==36-missing_k
            line=nx.to_graph6_bytes(g,header=False)
            f.write(line)
            counts[m]+=1

data=OUT.read_bytes()
lines=data.splitlines()
expected={36:1,35:36,34:630,33:7140}
assert dict(counts)==expected,(counts,expected)
assert len(lines)==sum(expected.values())==7807
# The generation is labelled rather than isomorph-free: every missing-edge set is distinct.
# That redundancy is intentional; it gives an elementary complete coverage proof for this dense sector.
assert len(set(lines))==len(lines)
manifest={
    'scope':'all labelled simple graphs on vertex set {0,...,8} with 33,34,35,36 edges',
    'coverage_method':'start from K9 and delete every subset of 0,1,2,3 of the 36 labelled edges',
    'reason_complete':'every labelled 9-vertex graph with m>=33 is uniquely K9 minus its 36-m missing-edge set',
    'expected_counts_by_edges':{str(k):v for k,v in sorted(expected.items())},
    'actual_counts_by_edges':{str(k):counts[k] for k in sorted(counts)},
    'graph6_lines':len(lines),
    'graph6_unique_lines':len(set(lines)),
    'graph6_sha256':hashlib.sha256(data).hexdigest(),
    'networkx_version':nx.__version__,
    'result':'PASS'
}
MAN.write_text(json.dumps(manifest,sort_keys=True,indent=2)+'\n',encoding='utf-8')
print(json.dumps(manifest,sort_keys=True))
