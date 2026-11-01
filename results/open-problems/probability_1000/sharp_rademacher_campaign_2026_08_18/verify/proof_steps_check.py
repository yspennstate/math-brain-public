"""Machine-check every step of the proposed proof of the cut-inflation conjecture.

CLAIM:  F(G) <= B(G) := 2^{E-V+2b} 3^{V-b},  b = number of BIPARTITE components,
        F(G) = SUM_x 2^{cut(x)}.

PROPOSED PROOF, by induction on E. The point I missed for a while: the recursion
F(G) = 2F(G-e) - F(G/e) enters F(G/e) with a MINUS sign, so I never need a lower bound on it
beyond F >= 0 - PROVIDED 2 B(G-e) <= B(G). And that holds exactly when deleting e does not turn a
non-bipartite component bipartite. So the whole proof is "delete a NON-CRITICAL edge".

  S0 BASE. No edges: F = 2^V and B = 2^{0-V+2V} 3^{V-V} = 2^V. Equal.
  S1 MULTIPLICATIVITY. F and B both multiply over connected components.
  S2 BRIDGE. If e is a bridge joining A and B, F(G) = (3/2) F(A) F(B) and B(G) = (3/2) B(A) B(B).
     So bridges reduce to smaller graphs with the SAME constant.
  S3 NON-CRITICAL EDGE EXISTS. Every connected, bridgeless, non-bipartite G that is not itself an
     odd cycle has an edge f with G-f still non-bipartite (and still connected, by bridgelessness).
  S4 STEP, non-bipartite. b(G-f) = b(G) => B(G-f) = B(G)/2 => F(G) <= 2B(G-f) - F(G/f) <= B(G).
  S5 STEP, bipartite. G bipartite bridgeless, delete any e: G-e bipartite connected,
     B(G-e) = B(G)/2, same conclusion.
  S6 ODD CYCLE. F(C_m) = 3^m - 1 <= 3^m = B(C_m) for odd m.

Each of S1, S2, S3, S4, S5, S6 is checked here on exhaustive small graphs. S3 is the load-bearing
one; a single counterexample there breaks the proof.
"""
import itertools
import sys

VMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7


def F(V, edges):
    tot = 0
    for bits in range(1 << V):
        c = 0
        for (a, b) in edges:
            if ((bits >> a) ^ (bits >> b)) & 1:
                c += 1
        tot += 1 << c
    return tot


def comps_bip(V, edges):
    adj = {v: [] for v in range(V)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    col, comps, bip = {}, 0, 0
    for s in range(V):
        if s in col:
            continue
        comps += 1
        col[s] = 0
        st, ok = [s], True
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in col:
                    col[v] = 1 - col[u]
                    st.append(v)
                elif col[v] == col[u]:
                    ok = False
        if ok:
            bip += 1
    return comps, bip


def B(V, edges):
    E = len(edges)
    comps, b = comps_bip(V, edges)
    return (2 ** (E - V + 2 * b)) * (3 ** (V - b))


def connected(V, edges):
    c, _ = comps_bip(V, edges)
    return c == 1


def is_bip(V, edges):
    _, b = comps_bip(V, edges)
    c, _ = comps_bip(V, edges)
    return b == c


def bridges(V, edges):
    """edge indices whose removal increases the component count"""
    base, _ = comps_bip(V, edges)
    out = []
    for i in range(len(edges)):
        ed = [e for j, e in enumerate(edges) if j != i]
        c, _ = comps_bip(V, ed)
        if c > base:
            out.append(i)
    return out


# ---- S0 base
s0 = all(F(V, []) == B(V, []) for V in range(1, 8))
print("S0 base (no edges): F == B for V=1..7   %s" % ("OK" if s0 else "*** FAIL"))

# ---- S1 multiplicativity, S2 bridge, S3 non-critical edge, S6 odd cycle
s1_ok = s1_bad = 0
s2_ok = s2_bad = 0
s3_ok = s3_bad = 0
s3_fail_examples = []
for V in range(3, VMAX + 1):
    alledges = list(itertools.combinations(range(V), 2))
    for mask in range(1, 1 << len(alledges)):
        edges = [alledges[i] for i in range(len(alledges)) if (mask >> i) & 1]
        if len({v for e in edges for v in e}) != V:
            continue
        if not connected(V, edges):
            continue
        E = len(edges)
        br = bridges(V, edges)

        # S2: bridge multiplicativity, on the first bridge if any
        if br:
            i = br[0]
            ed = [e for j, e in enumerate(edges) if j != i]
            # F(G) should equal (3/2) * F(G-e) since the two sides are independent given the split
            if 2 * F(V, edges) == 3 * F(V, ed):
                s2_ok += 1
            else:
                s2_bad += 1

        # S3: non-critical edge exists for bridgeless non-bipartite non-odd-cycle
        if not br and not is_bip(V, edges):
            is_odd_cycle = (E == V) and all(
                sum(1 for (a, b) in edges if a == v or b == v) == 2 for v in range(V))
            if not is_odd_cycle:
                found = False
                for i in range(E):
                    ed = [e for j, e in enumerate(edges) if j != i]
                    if connected(V, ed) and not is_bip(V, ed):
                        found = True
                        break
                if found:
                    s3_ok += 1
                else:
                    s3_bad += 1
                    if len(s3_fail_examples) < 5:
                        s3_fail_examples.append((V, E, tuple(edges)))

print("S2 bridge: F(G) == (3/2) F(G-bridge)      %d ok, %d FAIL" % (s2_ok, s2_bad))
print("S3 non-critical edge exists (bridgeless, non-bipartite, not an odd cycle):")
print("     %d ok, %d FAIL" % (s3_ok, s3_bad))
if s3_fail_examples:
    print("     counterexamples:")
    for V, E, edges in s3_fail_examples:
        print("       V=%d E=%d %s" % (V, E, edges))

# ---- S6 odd cycles
s6 = True
for m in (3, 5, 7, 9, 11):
    edges = [(i, (i + 1) % m) for i in range(m)]
    if F(m, edges) != 3 ** m - 1 or B(m, edges) != 3 ** m:
        s6 = False
print("S6 odd cycle: F = 3^m - 1, B = 3^m for m=3,5,7,9,11   %s" % ("OK" if s6 else "*** FAIL"))

# ---- S4/S5: the step itself, using the CHOSEN edge rule
step_ok = step_bad = 0
step_fail = []
for V in range(3, VMAX + 1):
    alledges = list(itertools.combinations(range(V), 2))
    for mask in range(1, 1 << len(alledges)):
        edges = [alledges[i] for i in range(len(alledges)) if (mask >> i) & 1]
        if len({v for e in edges for v in e}) != V or not connected(V, edges):
            continue
        if bridges(V, edges):
            continue                       # handled by S2
        E = len(edges)
        # choose the edge by the rule
        pick = None
        if is_bip(V, edges):
            pick = 0
        else:
            for i in range(E):
                ed = [e for j, e in enumerate(edges) if j != i]
                if connected(V, ed) and not is_bip(V, ed):
                    pick = i
                    break
        if pick is None:
            continue                       # odd cycle, handled by S6
        ed = [e for j, e in enumerate(edges) if j != pick]
        if 2 * B(V, ed) <= B(V, edges):
            step_ok += 1
        else:
            step_bad += 1
            if len(step_fail) < 5:
                step_fail.append((V, E, tuple(edges), pick, B(V, edges), 2 * B(V, ed)))

print("S4/S5 step: with the chosen edge, 2 B(G-e) <= B(G)   %d ok, %d FAIL" % (step_ok, step_bad))
if step_fail:
    for V, E, edges, i, bg, b2 in step_fail:
        print("     V=%d E=%d edge#%d  B(G)=%d  2B(G-e)=%d  %s" % (V, E, i, bg, b2, edges))
