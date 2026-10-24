# Independent obstruction, saved before reading w402's proof

2026-10-10. This note tests a topological bridge in honeycomb SAW scaling-limit routes. Primary context: Bauerschmidt--Duminil-Copin--Goodman--Slade, arXiv:1206.2092, Conjecture 1.5; Duminil-Copin--Smirnov, arXiv:1007.0575; Lawler--Schramm--Werner, arXiv:math/0204277, sections 2.2 and 3.4.5. This note was derived and saved without reading the paired prover's ATTEMPT or proof. Source-scope correction after recovery: P0003's own cited source is Grimmett, arXiv:2205.07318, Question 2.2, about uniform n-step walks from the origin; the critical, variable-length chordal formulation is a related distinct conjecture and no equivalence is claimed here.

## Bridge being tested

False auxiliary implication: laws viewed on C([0,1],C) with the uniform metric, supported on self-avoiding honeycomb paths in a fixed simply connected Jordan domain and with distinct limiting boundary endpoints, must have simple limiting traces merely because the laws are tight. Even uniform convergence and a common bound on speed do not imply this. Here the compact set consisting of the whole convergent sequence and its limit carries every deterministic law, so tightness in the ambient continuous-curve space is explicit.

This implication is relevant when trying to apply the conformal-restriction characterization of SLE(8/3): support on simple paths is a separate premise. The example below has deterministic laws, not the critical Boltzmann SAW law. It refutes only the stated auxiliary implication, never P0003 itself.

## Exact regular honeycomb construction

Label vertices by (i,j) in Z^2. Join horizontal neighbors (i,j),(i+1,j), and join (i,j) to (i,j+1) when i+j is even. Embed

    H(i,j) = (sqrt(3)*i/2, 3*j/2 - ((i+j) mod 2)/2).

Every edge has length one and the faces are regular hexagons. For even N >= 8, scale H by 1/N. Concatenate the following seven routes, counting shared corner vertices only once:

1. Row 0 from (-4N,0) to (-4,0).
2. Ascend 2N rows, using columns -4,-3: take the available upward edge; after each ascent except the last, switch columns horizontally. End at (-3,2N).
3. Row 2N rightward to (2N-1,2N).
4. Descend 2N rows using columns 2N-1,2N: take the downward edge; after each descent except the last, switch columns. End at (2N,0).
5. Row 0 leftward to (3,0).
6. Descend N rows using columns 3,4, with the same rule. End at (4,-N).
7. Row -N rightward to (4N,-N).

The seven regions have disjoint vertices except the consecutive corners: the incoming row-0 track uses i <= -4; the returning row-0 track uses i >= 3; the upward strip has negative columns and positive rows; the right downward strip has columns >= 2N-1; the final downward strip has negative rows. Within a vertical strip, j moves strictly at each vertical step, and the single horizontal step in a row uses two distinct vertices. Hence the walk is self-avoiding. The parity rule makes every indicated step a honeycomb edge. There are exactly 22N-12 edges.

All intermediate vertices lie in the fixed domain

    D = (-2sqrt(3),2sqrt(3)) x (-2,4),

with endpoints a=(-2sqrt(3),0) and b=(2sqrt(3),-3/2). The boundary is smooth near a and b. Corners of D can be rounded away from the paths if a globally smooth boundary is desired.

Give each of the seven routes duration 1/7 and each edge in a route equal duration. The speed is at most 28, since no route has more than 4N edges of length 1/N. The limiting polygon visits the anchors

    a, (0,0), (0,3), (sqrt(3),3), (sqrt(3),0),
    (0,0), (0,-3/2), b

at times 0,1/7,...,1. For horizontal routes, x differs from the corresponding linear interpolation by at most 2sqrt(3)/N and y by at most 1/(2N). For the vertical routes, the two columns stay within 2sqrt(3)/N of the limiting column; vertical progress differs from the linear interpolation by at most 1/N (the vertical and horizontal increments alternate with magnitudes 1/N and 1/(2N)). Thus a conservative uniform error bound is 5/N. This estimate is to be checked independently, together with the route parity.

The limiting trace contains the entire rectangle boundary [0,sqrt(3)] x [0,3], attached at (0,0). It cannot be the image of an injective arc: an arc contains no subspace homeomorphic to a circle. Filling bounded complementary components adds a rectangle of area 3sqrt(3). This is a macroscopic loop, not merely a repeated parametrization of an otherwise simple trace.

## Missing premise in probabilistic form

For a parametrized path gamma, define E(r,q) to mean that there are s<t with |gamma(s)-gamma(t)| <= r and diam(gamma([s,t])) >= q. A sufficient condition against a nonconstant self-return in any uniform subsequential limit is

    for every q>0, lim_{r downarrow 0} limsup_{delta downarrow 0}
        P_delta(E(r,q)) = 0.

To see the necessity of an extra condition, take s=1/7,t=5/7 in the construction. The two finite-mesh anchors are at distance sqrt(37)/N, while the excursion has diameter tending to 2sqrt(3). For q=1, these deterministic laws have E(r,q) probability 1 for every sufficiently large N, for every r>0. Nevertheless they converge uniformly and have speed at most 28.

For sufficiency, realize a uniformly convergent subsequence on a common probability space. A limit self-return with excursion diameter >q forces E(r,q/2) in all sufficiently close approximants, for each fixed r>0. Its probability is bounded by limsup P_delta(E(r,q/2)); let r decrease to zero. Apply a countable sequence of positive q. This excludes nonconstant self-returns. Constant waiting intervals are harmless after quotienting by reparametrization. This conditional lemma does not assert that the estimate is available for critical honeycomb SAW, and does not establish avoidance of the domain boundary.

Reproduction completed: check_honeycomb_pinch.py checked N=8,16,32,64,128, with 5,401 vertices total, in 0.450 seconds. All exact rational edge, uniqueness, domain and uniform-bound assertions passed. Uniform error decreased from 0.4412145344 at N=8 to 0.0276830673 at N=128; neck distance decreased from 0.7603453163 to 0.0475215823. These finite checks support reproducibility; the all-N argument above carries the proof.

NEXT: Obtain w404's independent mathematical audit and test the strongest step of w402's boundary-kernel route.
