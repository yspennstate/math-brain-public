"""Exact finite audits of cluster-mark localization and background factorization.

No earlier code is imported. Writes certificates.json only in this folder.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
import json
import os
from pathlib import Path
import resource
import signal
import time

signal.alarm(120)
started = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"


def component(edges, mask, seed):
    adj = defaultdict(list)
    for j, (u,v) in enumerate(edges):
        if mask >> j & 1:
            adj[u].append(v)
            adj[v].append(u)
    seen = {seed}
    stack = [seed]
    for u in stack:
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return frozenset(seen)


def bits(vertices):
    return sum(1 << v for v in vertices)


def mass(mask, size, p):
    return p**mask.bit_count()*(1-p)**(size-mask.bit_count())


def polynomial(counts, size, p):
    return sum((v*p**j*(1-p)**(size-j) for j,v in counts.items()), Q(0))


def tv(P, R):
    return sum(abs(P.get(k,0)-R.get(k,0)) for k in P.keys() | R.keys())/2


cases = [
    dict(name="inner_return", I=(0,1,2,3), S=(1,2,3), R=(4,5), T=(7,),
         inside=((0,1),(2,3),(0,3)), local=((1,4),(4,2),(3,5)),
         far=((4,6),(5,6),(6,7))),
    dict(name="outer_return", I=(0,1,2), S=(1,2), R=(3,4), T=(6,),
         inside=((0,1),(0,2)), local=((1,3),(2,4)),
         far=((3,5),(5,4),(4,6))),
    dict(name="background_cycle", I=(0,1,2,3), S=(1,2,3), R=(4,5), T=(8,),
         inside=((0,1),(0,2),(2,3),(1,3)),
         local=((1,4),(2,5),(3,5),(4,5)),
         far=((4,6),(5,7),(6,7),(7,8),(6,8))),
    dict(name="two_targets", I=(0,1,2,3), S=(1,2,3), R=(4,5,6), T=(7,9),
         inside=((0,1),(0,2),(2,3)), local=((1,4),(2,5),(3,6)),
         far=((4,7),(5,8),(6,9),(7,8),(8,9))),
    dict(name="isolated_background", I=(0,1,2,3), S=(1,2,3), R=(4,5), T=(9,),
         inside=((0,1),(0,2),(2,3)), local=((1,4),(2,5),(3,5)),
         far=((4,6),(5,7),(7,8),(8,5),(6,9))),
]

certificates = []
states = good_states = trace_changes = component_checks = pattern_checks = 0
normalizations = residual_atom_checks = 0
record_patterns = record_normalizations = 0
for case in cases:
    inside, local, far = case["inside"], case["local"], case["far"]
    I, S, R, T = map(set, (case["I"],case["S"],case["R"],case["T"]))
    near = inside+local
    edges = near+far
    vertices = {v for edge in edges for v in edge}
    assert {v for e in inside for v in e} == I
    assert ({v for e in inside for v in e} & {v for e in local for v in e}) <= S
    assert ({v for e in near for v in e} & {v for e in far for v in e}) <= R
    assert not T & {v for e in near for v in e}
    counts = {key: Counter() for key in ("E","H","HR","star","bad","error")}
    cluster_counts = defaultdict(Counter)
    background_counts = defaultdict(lambda: defaultdict(Counter))
    record_counts = defaultdict(Counter)
    record_background = defaultdict(lambda: defaultdict(Counter))
    residual_counts = defaultdict(Counter)
    exact_joint, local_joint = defaultdict(Counter), defaultdict(Counter)
    outside_masks = {}
    for mask in range(1 << len(edges)):
        states += 1
        C = component(edges, mask, 0)
        Qlocal = component(near, mask, 0)
        lm = mask >> len(inside)
        ex = local+far
        ext_components = {component(local, lm, s) for s in S}
        active = [c for c in ext_components if c & R]
        N = len(active)
        k = mask.bit_count()
        H = any(component(ex, lm, s) & T for s in S)
        HR = N > 0
        inner_C = component(inside, mask, 0)
        counts["H"][k] += H
        counts["HR"][k] += HR
        counts["star"][k] += S <= inner_C
        if not C & T:
            continue
        assert H and HR and Qlocal & R
        counts["E"][k] += 1
        counts["bad"][k] += N >= 2
        error = (C & I) != (Qlocal & I)
        counts["error"][k] += error
        trace_changes += error
        if N == 1:
            assert not error
            good_states += 1
            for v in I-Qlocal:
                Cv = component(near, mask, v)
                assert not Cv & R
                assert Cv == component(edges, mask, v)
                component_checks += 1
        imask = mask & ((1 << len(inside))-1)
        exact_joint[imask,bits(C & I)][k] += 1
        local_joint[imask,bits(Qlocal & I)][k] += 1
        cb = bits(C)
        cluster_counts[cb][k] += 1
        outside = sum(1 << j for j,(u,v) in enumerate(edges) if u not in C and v not in C)
        outside_masks[cb] = outside
        sigma = mask & outside
        internal = sum(1 << j for j,(u,v) in enumerate(edges) if u in C and v in C)
        record = (cb, mask & internal)
        record_counts[record][k] += 1
        record_background[record][sigma][k] += 1
        background_counts[cb][sigma][k] += 1
        residual_counts[sigma][k] += 1

    for p in (Q(1,3),Q(1,2),Q(2,3)):
        probs = {key: polynomial(c,len(edges),p) for key,c in counts.items()}
        arm, b, astar = probs["E"],probs["HR"],probs["star"]
        assert arm > 0 and astar > 0
        assert arm >= astar*probs["H"]
        bad, error = probs["bad"]/arm,probs["error"]/arm
        assert error <= bad <= b/astar
        P = {key: polynomial(c,len(edges),p)/arm for key,c in exact_joint.items()}
        L = {key: polynomial(c,len(edges),p)/arm for key,c in local_joint.items()}
        assert sum(P.values()) == sum(L.values()) == 1
        assert tv(P,L) <= error
        cmass = {cb: polynomial(c,len(edges),p)/arm for cb,c in cluster_counts.items()}
        rlaw = {s: polynomial(c,len(edges),p)/arm for s,c in residual_counts.items()}
        assert sum(cmass.values()) == sum(rlaw.values()) == 1
        for cb, cprob in cmass.items():
            outside = outside_masks[cb]
            free_indices = [j for j in range(len(edges)) if outside >> j & 1]
            group_sum = Q(0)
            for small_mask in range(1 << len(free_indices)):
                sigma = sum(1 << j for k,j in enumerate(free_indices) if small_mask >> k & 1)
                actual = polynomial(background_counts[cb][sigma],len(edges),p)/arm
                expected = cprob*mass(small_mask,len(free_indices),p)
                assert actual == expected
                group_sum += actual
                pattern_checks += 1
            assert group_sum == cprob
            normalizations += 1
        record_mass = {key: polynomial(c,len(edges),p)/arm
                       for key,c in record_counts.items()}
        assert sum(record_mass.values()) == 1
        for record, rprob in record_mass.items():
            cb, tau = record
            outside = outside_masks[cb]
            free_indices = [j for j in range(len(edges)) if outside >> j & 1]
            group_sum = Q(0)
            for small_mask in range(1 << len(free_indices)):
                sigma = sum(1 << j for k,j in enumerate(free_indices) if small_mask >> k & 1)
                actual = polynomial(record_background[record][sigma],len(edges),p)/arm
                assert actual == rprob*mass(small_mask,len(free_indices),p)
                assert not tau & sigma
                group_sum += actual
                record_patterns += 1
            assert group_sum == rprob
            record_normalizations += 1
        # Finite-dimensional coupling with an independent full Bernoulli field.
        coupled = defaultdict(Q)
        for zeta in range(1 << len(edges)):
            wz = mass(zeta,len(edges),p)
            for cb,cprob in cmass.items():
                sigma = zeta & outside_masks[cb]
                assert sigma & zeta == sigma
                coupled[sigma] += cprob*wz
        assert coupled == rlaw
        residual_atom_checks += len(rlaw)
        certificates.append(dict(
            graph=case["name"],p=str(p),event=str(arm),local_arm=str(b),
            far_arm=str(probs["H"]),a_star=str(astar),
            conditional_bad=str(bad),trace_error=str(error),joint_TV=str(tv(P,L)),
            cluster_mass={str(k):str(v) for k,v in cmass.items()},
            root_record_mass={f"{k[0]}:{k[1]}":str(v) for k,v in record_mass.items()},
            residual_mass={str(k):str(v) for k,v in rlaw.items()}))

assert trace_changes > 0
Path("certificates.json").write_text(json.dumps(certificates,indent=2)+"\n")
print(f"PASS: {len(cases)} finite graphs; {states} complete configurations")
print(f"PASS: {good_states} one-active root-trace reconstructions; {component_checks} frozen non-root components")
print(f"PASS: {trace_changes} genuine exterior-return trace changes, all charged to the bad event")
print(f"PASS: {len(certificates)} exact probability and joint-TV bounds")
print(f"PASS: {pattern_checks} conditional product-pattern identities; {normalizations} cluster normalizations")
print(f"PASS: {record_patterns} product-pattern identities given full root-cluster records; {record_normalizations} record normalizations")
print(f"PASS: {residual_atom_checks} residual-law atoms matched by explicit monotone coupling")
for row in certificates:
    if row["p"] == "1/2":
        print(row["graph"],"P(E)="+row["event"],"bad="+row["conditional_bad"],
              "trace_error="+row["trace_error"],"joint_TV="+row["joint_TV"])
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
print(f"Priority: {os.getpriority(os.PRIO_PROCESS,0)}; OMP_NUM_THREADS=1")
print(f"Elapsed seconds: {time.monotonic()-started:.3f}")
print(f"Peak RSS bytes: {rss}")
print("PASS: all exact cluster-background checks")
