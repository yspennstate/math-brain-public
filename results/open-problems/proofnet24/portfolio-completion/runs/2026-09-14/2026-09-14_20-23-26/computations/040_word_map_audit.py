"""Worker 040: independent exact finite checks for the two word maps.

Only Python's standard library is used. This is not a Lean build and does
not prove the all-size claims. Every assert has a witness-bearing payload.
Run: python3 computations/040_word_map_audit.py
"""
from itertools import combinations, permutations
from math import factorial
import json
import time


def prefix_mask(word, length):
    return sum(1 << v for v in word[:length])


def family_has(family, subset):
    return bool(family & (1 << subset))


def gluing_audit(max_m=3):
    stats = {"max_outer_letters": max_m, "family_pairs": 0,
             "mark_instances": 0, "rotated_states": 0}
    for m in range(max_m + 1):
        words = list(permutations(range(m)))
        subsets = range(1 << m)
        members = [[s for s in subsets if family_has(f, s)]
                   for f in range(1 << (1 << m))]
        # For every pair of arbitrary (not necessarily monotone) families,
        # take C to be all disjoint unions from A and B.
        for a, amem in enumerate(members):
            for b, bmem in enumerate(members):
                c = 0
                for r in amem:
                    for x in bmem:
                        if r & x == 0:
                            c |= 1 << (r | x)
                if c & ~a:
                    continue  # The source theorem explicitly requires C subset A.
                stats["family_pairs"] += 1
                for marks in subsets:
                    stats["mark_instances"] += 1
                    images = {}
                    count_a = count_b = count_c = allowed = 0
                    for word in words:
                        allowed += 1  # The empty cut.
                        for k in range(1, m + 1):
                            if not (marks & (1 << word[k - 1])):
                                continue
                            allowed += 1
                            support = prefix_mask(word, k)
                            in_a = family_has(a, support)
                            in_b = family_has(b, support)
                            in_c = family_has(c, support)
                            count_a += in_a
                            count_b += in_b
                            count_c += in_c
                            if not in_a or in_c:
                                continue
                            j = next(j for j in range(1, k + 1)
                                     if marks & (1 << word[j - 1])
                                     and family_has(a, prefix_mask(word, j))
                                     and not family_has(c, prefix_mask(word, j)))
                            outword = word[j:k] + word[:j] + word[k:]
                            outcut = k - j
                            witness = (m, a, b, c, marks, word, k, j)
                            assert outcut == 0 or marks & (1 << outword[outcut - 1]), witness
                            assert not family_has(b, prefix_mask(outword, outcut)), witness
                            image = (outword, outcut)
                            assert image not in images, (witness, images.get(image))
                            images[image] = (word, k)
                            tail = outword[outcut:]
                            back_j = next(q for q in range(1, len(tail) + 1)
                                          if marks & (1 << tail[q - 1])
                                          and family_has(a, prefix_mask(tail, q))
                                          and not family_has(c, prefix_mask(tail, q)))
                            recovered = (tail[:back_j] + outword[:outcut] + tail[back_j:],
                                         back_j + outcut)
                            assert recovered == (word, k), witness
                            stats["rotated_states"] += 1
                    assert len(images) == count_a - count_c
                    assert len(images) <= allowed - count_b
                    assert count_a + count_b <= allowed + count_c
    return stats


def graphs(n):
    pairs = list(combinations(range(n), 2))
    for bits in range(1 << len(pairs)):
        yield tuple(pair for i, pair in enumerate(pairs) if bits & (1 << i))


def adjacency(n, edges):
    out = [0] * n
    for u, v in edges:
        out[u] |= 1 << v
        out[v] |= 1 << u
    return out


def supports(n, host_adj, s, source_edges, root):
    """Existential injective homomorphisms, stored by host root and support."""
    out = [[False] * (1 << n) for _ in range(n)]
    for f in permutations(range(n), s):
        if all(host_adj[f[u]] & (1 << f[v]) for u, v in source_edges):
            image = sum(1 << v for v in f)
            out[f[root]][image] = True
    for b in range(n):
        for bit in range(n):
            for support in range(1 << n):
                if support & (1 << bit):
                    out[b][support] |= out[b][support ^ (1 << bit)]
    return out


def qualifies(word, k, adj, supp):
    return bool(k > 0 and adj[word[0]] & (1 << word[k])
                and supp[word[0]][prefix_mask(word, k + 1)])


def leaf_move_audit(max_n=4):
    stats = {"max_host_vertices": max_n, "host_graphs": 0,
             "rooted_source_graph_cases": 0, "source_states": 0,
             "first_states": 0, "reversed_states": 0}
    for n in range(2, max_n + 1):
        words = list(permutations(range(n)))
        for host_edges in graphs(n):
            stats["host_graphs"] += 1
            adj = adjacency(n, host_edges)
            for s in range(1, n):
                for source_edges in graphs(s):
                    for root in range(s):
                        stats["rooted_source_graph_cases"] += 1
                        old = supports(n, adj, s, source_edges, root)
                        new_edges = source_edges + ((root, s),)
                        new = supports(n, adj, s + 1, new_edges, s)
                        source_count = target_count = first_count = 0
                        images = set()
                        for word in words:
                            cuts = [k for k in range(1, n)
                                    if qualifies(word, k, adj, old)]
                            source_count += len(cuts)
                            target_count += sum(qualifies(word, k, adj, new)
                                                for k in range(1, n))
                            first_count += bool(cuts)
                            for k in cuts[1:]:
                                outword = word[:k + 1][::-1] + word[k + 1:][::-1]
                                payload = (n, host_edges, source_edges, root, word, k)
                                assert qualifies(outword, k, adj, new), payload
                                assert outword[:k + 1][::-1] + outword[k + 1:][::-1] == word
                                assert (outword, k) not in images, payload
                                images.add((outword, k))
                        assert first_count <= factorial(n)
                        assert len(images) == source_count - first_count
                        assert len(images) <= target_count
                        assert source_count <= target_count + factorial(n)
                        stats["source_states"] += source_count
                        stats["first_states"] += first_count
                        stats["reversed_states"] += len(images)
    return stats


def main():
    started = time.monotonic()
    result = {"status": "PASS_FINITE_EXHAUSTIVE_MAP_CHECKS",
              "gluing": gluing_audit(), "leaf_move": leaf_move_audit()}
    result["elapsed_seconds"] = round(time.monotonic() - started, 3)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
