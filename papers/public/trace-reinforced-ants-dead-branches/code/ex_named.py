# The named examples of the paper, solved with the census solver. Usage: python3 ex_named.py
import networkx as nx
import ants_exact as X
def show(name, n, E, N, F):
    r = X.solve_case(n, E, N, F, 6, 5)
    G = nx.Graph(E)
    print(name, "connectivity", nx.node_connectivity(G), "dist(N,F)", nx.shortest_path_length(G, N, F))
    for s in r["sols"]:
        print("   ", "raw" if s["raw"] else "limit", "from", s["starts"], "starts:", [(E[k], round(x, 6)) for k, x in enumerate(s["w"])])
        print("    zero edges", [E[k] for k in s["zero"]], "largest real part on the support", s.get("maxre"))
# Example 3, the paw: N=0, x=1, y=2, F=3
show("paw", 4, [(0, 1), (1, 2), (1, 3), (2, 3)], 0, 3)
# Example 4, the 4-cycle N,a,F,b with a detour a-y-F: N=0, a=1, F=2, b=3, y=4
show("C4 with a detour", 5, [(0, 1), (1, 2), (2, 3), (3, 0), (4, 1), (4, 2)], 0, 2)
# Theorem 5: the 4-cycle N,a,F,b with c joined to a, b and F: N=0, a=1, b=2, F=3, c=4
show("C4 with a shadowed neighbour", 5, [(0, 1), (0, 2), (1, 3), (2, 3), (4, 1), (4, 2), (4, 3)], 0, 3)
# Theorem 5: K_{3,3} with parts {a,b,c}={1,2,3} and {N,F,x}={0,4,5}, plus the edge {x,F}
show("K33 plus {x,F}", 6, [(i, j) for i in (1, 2, 3) for j in (0, 4, 5)] + [(5, 4)], 0, 4)
# Remark 6: a triangle hanging at a neighbour u of F stays alive: N=0, u=1, F=2, triangle 1,3,4
show("triangle pocket", 5, [(0, 1), (1, 2), (1, 3), (1, 4), (3, 4)], 0, 2)
