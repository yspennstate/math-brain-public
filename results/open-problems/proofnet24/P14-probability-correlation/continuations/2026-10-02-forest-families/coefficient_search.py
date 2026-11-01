"""Exact random-cluster pairwise coefficient search; standard-library only.

No positive evaluation is a proof of the unrestricted conjecture.
For a rational common edge activity a/b, rescaled masses are integers.
"""
import itertools
import json
import random
from fractions import Fraction
from pathlib import Path


def product(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def subset_data(n, edges):
    data = []
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        count = n
        chosen = []
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                chosen.append(i)
                a, b = root(u), root(v)
                if a != b:
                    parent[a] = b
                    count -= 1
        data.append((count, tuple(chosen)))
    return data


def coefficients(n, edges, data, activity):
    m = len(edges)
    a, b = activity.numerator, activity.denominator
    weights = [a**k * b**(m-k) for k in range(m+1)]
    Z = [0] * (n+1)
    Zi = [[0]*(n+1) for _ in edges]
    Zij = {ij: [0]*(n+1) for ij in itertools.combinations(range(m), 2)}
    for k, chosen in data:
        w = weights[len(chosen)]
        Z[k] += w
        for i in chosen:
            Zi[i][k] += w
        for ij in itertools.combinations(chosen, 2):
            Zij[ij][k] += w
    for (i, j), z in Zij.items():
        positive, negative = product(Zi[i], Zi[j]), product(Z, z)
        delta = [x-y for x,y in zip(positive, negative)]
        quotient = []
        running = 0
        for x in delta:
            running += x
            quotient.append(running)
        assert running == 0, "independence at q=1 must give exact divisibility"
        yield (i, j), delta, quotient


def main():
    rng = random.Random(20261002)
    graphs = [
        (5, list(itertools.combinations(range(5),2))),
        (6, list(itertools.combinations(range(6),2))),
        (6, [(i,j) for i in range(3) for j in range(3,6)]),
    ]
    for n,m in [(7,12),(8,13),(9,14),(10,15)]:
        for _ in range(20):
            graphs.append((n, rng.sample(list(itertools.combinations(range(n),2)),m)))
    activities = [Fraction(1,10),Fraction(1,2),Fraction(1),Fraction(2),Fraction(10)]
    tests = 0
    counterexamples = []
    for graph_index,(n,edges) in enumerate(graphs):
        data = subset_data(n,edges)
        for activity in activities:
            for pair,delta,quotient in coefficients(n,edges,data,activity):
                tests += 1
                if min(quotient)<0:
                    counterexamples.append(dict(n=n,edges=edges,activity=str(activity),pair=pair,delta=delta,quotient=quotient))
                    print("NEGATIVE COEFFICIENT",json.dumps(counterexamples[-1]),flush=True)
                    break
        if graph_index%10==0:
            print("progress",graph_index+1,"graphs",tests,"pair tests",flush=True)
    result=dict(graph_count=len(graphs),tests=tests,activities=list(map(str,activities)),seed=20261002,counterexamples=counterexamples)
    Path(__file__).with_name("coefficient_search_results.json").write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!="counterexamples"}),flush=True)
    print("negative coefficient examples",len(counterexamples),flush=True)


if __name__ == "__main__":
    main()
