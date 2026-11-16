# Row CO06 (the cycle double cover conjecture): the linear-algebra proof read and checked

12 Nov 2026. Sources: arXiv 2607.15399v1 (J. Geelen, 16 Jul 2026, "OpenAI's proof of the Cycle Double Cover
Theorem"), read in full; the introduction and the last section of arXiv 2607.16356v3 (S. Oum, exposition). The
proof is credited to GPT 5.6 (OpenAI, "A proof of the cycle double cover conjecture", July 2026); that text is
not on arXiv and was not read.

## The statement

Every bridgeless graph has a list of cycles covering every edge exactly twice.

## The proof, as checked by hand

Two standard inputs: the reduction to cubic graphs, and Jaeger's theorem that a bridgeless graph has a
nowhere-zero flow f with values in F_2^3. Neither was re-proved here.

1. At a vertex v with edges a, b, c the values f_a, f_b, f_c are nonzero, distinct and sum to 0. Put
   alpha_{v,a} = f_b, alpha_{v,b} = f_c, alpha_{v,c} = f_a and beta_{v,e} = alpha_{v,e} + f_e. For a potential
   p : V -> F_2^3 give the edge e, seen from v, the two colours p_v + alpha_{v,e} and p_v + beta_{v,e}. At v each
   of the three colours p_v + f_a, p_v + f_b, p_v + f_c lies on exactly two edges. So if the two ends of every
   edge agree on its pair, each colour class is 2-regular and every edge is in two classes: a cycle double
   cover with at most 8 classes.
2. The two pairs at an edge e = uv have the same difference f_e, so they agree exactly when
   p_u + p_v + z_e f_e = alpha_{u,e} + alpha_{v,e} for some z_e in F_2. This is a linear system over F_2.
3. If it has no solution, some y : E -> F_2^3 has sum_{e ~ v} y_e = 0 at every vertex, f_e . y_e = 0 on every
   edge, and sum_e (alpha_{u,e} + alpha_{v,e}) . y_e = 1.
4. At a vertex, alpha_{v,a} . y_a + alpha_{v,b} . y_b = (f_a + f_c) . y_a + f_c . (y_a + y_c)
   = f_a . y_a + f_c . y_c = 0, so alpha_{v,e} . y_e takes one value delta_v on the three edges at v.
5. If delta_v = 0 then y_a, y_b, y_c are orthogonal to the plane spanned by the flow values at v, so each is 0 or
   the one nonzero vector w of the orthogonal line; they sum to 0, so none or exactly two of them are nonzero.
6. Let X be the set of vertices with delta_v = 0 and G+ the edges with y_e nonzero. Vertices of X have even
   degree in G+, so G+ has an even number of edges leaving X. An edge with exactly one end in X has
   alpha_{v,e} . y_e = 1 at its other end, so it is in G+. Hence the sum in step 3, which counts the edges with
   exactly one end in X, is even. Contradiction.

Every step holds. The proof gives a double cover by at most 8 even subgraphs.

## The computer check (co06_check.py, co06_check.out)

The script does not use steps 3 to 6. For a graph and a flow it solves the system of step 2 by elimination,
builds the colour classes and tests directly that each class has degree 0 or 2 at every vertex and each edge
lies in exactly two classes.

- All nowhere-zero F_2^3-flows of K_4 (210), K_{3,3} (1092), the prism (1050), the cube (5712) and the Petersen
  graph (28560); the counts equal the flow polynomials at 8. Solvable and a valid cover every time. On the
  Petersen graph the cover uses 5 colours for 26880 flows and 6 for 1680, never fewer than 5, as it must.
- Random flows on the Heawood graph, the flower snarks J3, J5, J7, the dodecahedron, the Desargues and
  Möbius–Kantor graphs, and 40 random bridgeless cubic graphs on 8 to 24 vertices (all flows when the cycle
  space has dimension at most 5): no failure.
- Control: nonzero edge labels that are not flows, 2000 trials each on the Petersen graph and the cube: the
  system is unsolvable in 1775 and 1771 trials and gives no cover in the rest.

## Other literature (lit/search/s1.xml, s2.xml; titles only unless stated)

No correction or objection in two dated arXiv searches. Since July 2026: Hušek and Šámal 2607.24724
(exponentially many circuit double covers); Zhang 2609.10618 (early results of Tutte, 1948); Kintali 2607.14140
(three-bit flows and cycle covers, posted three days before the first exposition; not read). Oum's last section
lists what the method does not give: Bondy's small cycle double cover conjecture, the 5-cycle double cover
conjecture (Celmins, Preissmann), the orientable 5-cycle double cover conjecture (Archdeacon, Jaeger; it implies
Tutte's 5-flow conjecture), the strong embedding conjecture for non-cubic graphs, and Berge–Fulkerson.

## Proposal for the row

The conjecture is a theorem; remove the row. Candidates for the slot, in the order I would vet them: the
orientable 5-cycle double cover conjecture, the 5-cycle double cover conjecture, the strong embedding conjecture.
The 5-flow conjecture and Berge–Fulkerson may already be on the list.
