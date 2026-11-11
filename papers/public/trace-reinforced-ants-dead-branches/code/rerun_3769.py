# The seven-vertex case 3769 of the census (N adjacent to F): the edge {1,4} lies in D and its weight decays like 1/t
# along the flow. At the census integration time one of the six runs does not yet classify it as zero; with ten times
# the time all six runs agree. Usage: python3 rerun_3769.py
import numpy as np, networkx as nx
import ants_exact as X
n = 7; E = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (4, 5), (5, 6)]; N, F = 3, 4
for T in (2000, 20000, 200000):
    r = X.solve_case(n, E, N, F, 6, 1000 + 3769, T=T)
    print("T", T, "flags", r["flags"])
    for s in r["sols"]:
        print("   raw", s["raw"], "starts", s["starts"], "zero", [E[k] for k in s["zero"]], "maxre", s.get("maxre"),
              "w", ["%.3g" % x for x in s["w"]])
# the weight of {1,4} along the flow, from the six initial conditions of the census
G, keep = X.reduce_graph(n, E, N, F); Er = [E[k] for k in keep]; m = len(Er); k14 = Er.index((1, 4))
rng = np.random.default_rng(1000 + 3769)
for s in range(6):
    rr = s % 3
    if rr == 0: w0 = rng.uniform(0.05, 1, m)
    elif rr == 1: w0 = np.exp(rng.uniform(-6, 0, m))
    else:
        w0 = np.exp(rng.uniform(-6, -3, m)); Hh = nx.Graph(Er)
        for (u, v) in Hh.edges(): Hh[u][v]["x"] = rng.uniform(0.5, 1.5)
        path = nx.shortest_path(Hh, N, F, weight="x"); on = set(frozenset(e) for e in zip(path, path[1:]))
        for k, e in enumerate(Er):
            if frozenset(e) in on: w0[k] = rng.uniform(0.5, 1)
    w = w0.copy(); row = []
    for T in (2000, 2000, 16000, 180000):
        w = X.flow(n, Er, w, N, F, T); row.append("%.3g" % w[k14])
    print("start", s, "w_{1,4} after 2000, 4000, 20000, 200000 steps:", row)
