# Strassen deficit: max over up-sets U of mu(U) - P(U) = 1 - (max mass of a monotone sub-coupling),
# computed by integer max-flow on {x} -> {y : y subset of x}.  P dominates mu iff deficit == 0.
import numpy as np
import networkx as nx

SCALE = 10 ** 12


def _graph(P, mu):
    N = len(P)
    G = nx.DiGraph()
    for x in range(N):
        cx = int(round(P[x] * SCALE))
        if cx > 0:
            G.add_edge('s', ('x', x), capacity=cx)
    for y in range(N):
        cy = int(round(mu[y] * SCALE))
        if cy > 0:
            G.add_edge(('y', y), 't', capacity=cy)
    for x in range(N):
        if P[x] <= 0:
            continue
        sub = x
        while True:
            if mu[sub] > 0:
                G.add_edge(('x', x), ('y', sub), capacity=4 * SCALE)
            if sub == 0:
                break
            sub = (sub - 1) & x
    return G


def deficit(P, mu):
    G = _graph(P, mu)
    fv, _ = nx.maximum_flow(G, 's', 't')
    return 1.0 - fv / SCALE


def worst_upset(P, mu):
    """(deficit, list of masks y on the sink side of a min cut): the up-set where mu beats P most"""
    G = _graph(P, mu)
    cut, (S, Tt) = nx.minimum_cut(G, 's', 't')
    U = [y for y in range(len(P)) if ('y', y) in Tt]
    return 1.0 - cut / SCALE, U
