"""Exact finite SAW counts and finite-memory upper bounds on the Hanoi Cayley graph.

Meet in the middle finds EVERY reduced identity word up to length 2*half.
An Aho-Corasick automaton forbids those words and aa,bb,cc. Its counts are exact
through 2*half, and upper estimates thereafter. This is not a finite group quotient.
"""
import argparse
import collections
import json
import math
import pathlib
import resource
import time

from saw_counts import Hanoi, write_counts

ROOT = pathlib.Path(__file__).resolve().parents[1]


def reduced(word):
    stack = []
    for s in word:
        if stack and s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    return bytes(stack)


def identity_words(half):
    graph = Hanoi()
    words = collections.defaultdict(list)

    def visit(v, w):
        words[v].append(w)
        if len(w) == half:
            return
        for s in range(3):
            if not w or w[-1] != s:
                visit(graph.product(v, s+1), w+bytes([s]))

    visit(0, b"")
    relators = set()
    for ws in words.values():
        for i, u in enumerate(ws):
            for v in ws[:i]:
                w = reduced(u + v[::-1])
                if w:
                    relators.add(w)
                    relators.add(w[::-1])
    return graph, relators


def automaton(relators):
    children = [{}]
    terminal = [False]
    # Keep all words: redundant forbidden words do not affect the exact language.
    for word in sorted(relators | {bytes([s,s]) for s in range(3)}):
        node = 0
        for s in word:
            if s not in children[node]:
                children[node][s] = len(children)
                children.append({})
                terminal.append(False)
            node = children[node][s]
        terminal[node] = True
    fail = [0] * len(children)
    q = collections.deque(children[0].values())
    while q:
        v = q.popleft()
        terminal[v] |= terminal[fail[v]]
        for s, w in children[v].items():
            f = fail[v]
            while f and s not in children[f]:
                f = fail[f]
            fail[w] = children[f].get(s, 0)
            q.append(w)
    live = {i: j for j, i in enumerate(i for i in range(len(children)) if not terminal[i])}
    trans = []
    for v in live:
        row = []
        for s in range(3):
            f = v
            while f and s not in children[f]:
                f = fail[f]
            w = children[f].get(s, 0)
            row.append(-1 if terminal[w] else live[w])
        trans.append(row)
    return trans


def language_counts(trans, n):
    # Forward counts from the empty history.
    current = [0] * len(trans)
    current[0] = 1
    result = [1]
    for _ in range(n):
        nxt = [0] * len(trans)
        for row, number in zip(trans, current):
            if number:
                for j in row:
                    if j >= 0:
                        nxt[j] += number
        current = nxt
        result.append(sum(current))
    return result


def block_upper(trans, length):
    # Maximum number of legal k-step continuations over ALL automaton states.
    # mu <= rho(A) <= ||A^k||_infinity^(1/k). Counts are exact integers.
    v = [1] * len(trans)
    for _ in range(length):
        v = [sum(v[j] for j in row if j >= 0) for row in trans]
    maximum = max(v)
    av = [sum(v[j] for j in row if j >= 0) for row in trans]
    # Zero entries are states from which no k-step continuation exists.
    # They also have (Av)_i=0. For n>=k, e_0 A^n 1=e_0 A^(n-k) v,
    # so a componentwise Av<=qv still bounds the language growth.
    assert v[0] > 0
    numerator, denominator = 0, 1
    for a, b in zip(av, v):
        if b == 0:
            assert a == 0
            continue
        if a * denominator > numerator * b:
            numerator, denominator = a, b
    return {"k": length, "max_row_sum_A_power": str(maximum),
            "upper_bound_float": math.exp(math.log(maximum)/length),
            "collatz_numerator": str(numerator), "collatz_denominator": str(denominator),
            "collatz_upper_float": numerator/denominator,
            "zero_entries_in_v": v.count(0),
            "certificate": "A v <= (numerator/denominator) v, v=A^k 1, v_0>0; hence mu <= numerator/denominator"}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--half", type=int, default=14)
    p.add_argument("--block", type=int, default=200)
    args = p.parse_args()
    start = time.monotonic()
    graph, relators = identity_words(args.half)
    print('found', len(relators), 'identity words; states', len(graph.states), flush=True)
    trans = automaton(relators)
    print('automaton states', len(trans), flush=True)
    counts = language_counts(trans, 2*args.half)
    write_counts('hanoi_language', counts, time.monotonic()-start, graph)
    cert = block_upper(trans, args.block)
    output = {"half": args.half, "exact_through_n": 2*args.half,
              "forbidden_identity_words": len(relators),
              "girth": min(map(len, relators)) if relators else None,
              "automaton_states": len(trans), "upper_certificate": cert,
              "elapsed_seconds": time.monotonic()-start,
              "peak_rss_bytes_macos": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    (ROOT/'data/hanoi_language_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
    (ROOT/'data/hanoi_relators.txt').write_text('\n'.join(''.join('abc'[s] for s in w)
        for w in sorted(relators,key=lambda x:(len(x),x)))+'\n')
    print(json.dumps(output), flush=True)
