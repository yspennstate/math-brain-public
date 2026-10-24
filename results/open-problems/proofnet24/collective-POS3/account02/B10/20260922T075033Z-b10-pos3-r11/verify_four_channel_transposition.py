#!/usr/bin/env python3
from itertools import permutations
from collections import defaultdict
from fractions import Fraction

def closure_from_mask(n, mask):
    rel = [[False]*n for _ in range(n)]
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    for bit,(i,j) in enumerate(pairs):
        if (mask >> bit) & 1:
            rel[i][j] = True
    for k in range(n):
        for i in range(n):
            if rel[i][k]:
                for j in range(n):
                    if rel[k][j]:
                        rel[i][j] = True
    return tuple(tuple(row) for row in rel)

def incomparable(rel,a,b):
    return a != b and not rel[a][b] and not rel[b][a]

def is_cover(rel,a,b):
    if not rel[a][b]:
        return False
    return not any(rel[a][z] and rel[z][b]
                   for z in range(len(rel)) if z not in (a,b))

def width(rel):
    n = len(rel)
    best = 0
    for mask in range(1 << n):
        xs = [i for i in range(n) if (mask >> i) & 1]
        ok = True
        for i in range(len(xs)):
            for j in range(i+1,len(xs)):
                a,b = xs[i],xs[j]
                if rel[a][b] or rel[b][a]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            best = max(best,len(xs))
    return best

def linear_extensions(rel):
    n = len(rel)
    ans = []
    for perm in permutations(range(n)):
        pos = [0]*n
        for k,v in enumerate(perm):
            pos[v] = k
        if all((not rel[i][j]) or pos[i] < pos[j]
               for i in range(n) for j in range(n)):
            ans.append(perm)
    return ans

def valid_extension(perm,rel):
    pos = [0]*len(rel)
    for k,v in enumerate(perm):
        pos[v] = k
    return all((not rel[i][j]) or pos[i] < pos[j]
               for i in range(len(rel)) for j in range(len(rel)))

def swap_positions(perm,a,b):
    out = list(perm)
    ia,ib = out.index(a),out.index(b)
    out[ia],out[ib] = out[ib],out[ia]
    return tuple(out)

posets_checked = 0
strong_pairs_checked = 0
channel_hist = defaultdict(int)
minimum_selected_share = None
minimum_record = None

for n in range(3,7):
    closures = set()
    for mask in range(1 << (n*(n-1)//2)):
        closures.add(closure_from_mask(n,mask))
    for rel in closures:
        if width(rel) > 3:
            continue
        posets_checked += 1
        exts = linear_extensions(rel)
        E = len(exts)
        for p in range(n):
            for q in range(n):
                if not incomparable(rel,p,q):
                    continue
                M = [L for L in exts if L.index(p) < L.index(q)]
                if 3*len(M) <= 2*E:
                    continue
                strong_pairs_checked += 1
                minority = E-len(M)

                U = [r for r in range(n)
                     if is_cover(rel,p,r) and incomparable(rel,r,q)]
                D = [r for r in range(n)
                     if is_cover(rel,r,q) and incomparable(rel,p,r)]
                assert len(U) <= 2
                assert len(D) <= 2
                assert set(U).isdisjoint(D)

                outgoing = []
                incoming = []
                assigned = defaultdict(int)

                for L in M:
                    S = swap_positions(L,p,q)
                    if valid_extension(S,rel):
                        continue
                    outgoing.append(L)
                    pos = {v:i for i,v in enumerate(L)}
                    witnesses = []
                    for r in U:
                        if pos[p] < pos[r] < pos[q]:
                            witnesses.append(("U",r))
                    for r in D:
                        if pos[p] < pos[r] < pos[q]:
                            witnesses.append(("D",r))
                    assert witnesses
                    assigned[min(witnesses)] += 1

                for L in exts:
                    if L.index(q) < L.index(p):
                        S = swap_positions(L,p,q)
                        if not valid_extension(S,rel):
                            incoming.append(L)

                # Exact complement-bijection identity.
                assert len(outgoing)-len(incoming) == len(M)-minority
                # Since M/E > 2/3, the outgoing defect set has mass > 1/3.
                assert 3*len(outgoing) > E

                # Width <= 3 leaves at most four Hasse witness channels.
                channel_hist[len(U)+len(D)] += 1
                max_marks = max(assigned.values())
                assert 12*max_marks > E

                # Every selected mark is a genuine order event for its
                # associated incomparable pair.
                for (kind,r),count in assigned.items():
                    if kind == "U":
                        event_count = sum(L.index(r) < L.index(q) for L in exts)
                        assert incomparable(rel,r,q)
                    else:
                        event_count = sum(L.index(p) < L.index(r) for L in exts)
                        assert incomparable(rel,p,r)
                    assert count <= event_count

                share = Fraction(max_marks,E)
                if minimum_selected_share is None or share < minimum_selected_share:
                    minimum_selected_share = share
                    minimum_record = (
                        n,E,len(M),p,q,len(U),len(D),
                        len(outgoing),len(incoming),max_marks
                    )

print("naturally_labelled_width_le_3_posets_n3_to_n6 =", posets_checked)
print("strong_ordered_incomparable_pairs_checked =", strong_pairs_checked)
print("witness_channel_histogram =", dict(sorted(channel_hist.items())))
print("minimum_observed_selected_channel_share =", minimum_selected_share)
print("minimum_record(n,E,M,p,q,|U|,|D|,out,in,maxmarks) =", minimum_record)
print("POS3_FOUR_CHANNEL_TRANSPOSITION_CHECK_PASS")
