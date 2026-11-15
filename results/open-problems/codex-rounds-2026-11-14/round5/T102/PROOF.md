# Finite percolation measurements of circuit repair costs

The computation concerns finite conditioned critical site percolation. It
does not determine a resistance exponent. The deterministic bound used
below is the preceding session's result, independently checked here.

## 1. Network and sampling law

Write a triangular-lattice vertex as (a,b), embedded at
(a+b/2, sqrt(3)b/2). Its six neighbors differ by
(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1). Put

    |(a,b)|_hex = max(|a|,|b|,|a+b|),
    B_R = {v: |v|_hex <= R}.

Independently retain every site of B_R with probability 1/2, fixing the
origin open. Join every pair of neighboring open sites with a unit resistor.
Reject a configuration unless the origin has an open path to a vertex of
hexagonal radius R. Keep all open sites and all their edges, including
components disconnected from that path. The sink is the entire set of
open sites of radius R, wired together.

This rejection rule targets Bernoulli site percolation conditioned on
0 connected to the radius-R boundary. Indeed that event already implies
that 0 is open. Conditioning first on its being open and then on the
connection gives the same conditional law. Rejection does not refer to
circuits or electrical quantities. The implementation is a reproducible
pseudorandom sample with seed 202611150821, not an exact enumeration.

There are 40 accepted configurations at each R=12,24,48. The first circuit
search used annuli [max(2,floor(R/8)),floor(R/4)] and
[floor(R/2),floor(5R/6)]. It found no circuits. The reported nontrivial
measurements instead replay these same configurations with search annuli

    [1,floor(R/4)] and [floor(R/4)+1,R-1].

No realization is removed when either search fails. Both versions are
saved. This revision followed inspection of the first pass and is not a
prespecified statistical test. In particular the inner annulus in the
second pass has an increasing ratio of outer to inner radius.

## 2. Selecting and splitting at circuits

In each annulus take its induced open graph. At a directed edge (u,v),
continue along the edge from v immediately clockwise from (v,u) in the
six-direction cyclic ordering. This permutation of directed edges traces
all face boundary walks, including boundaries of separate components and
walks containing bridges. When a vertex repeats within a walk, split off
the closed segment between its occurrences. A stack with distinct vertices
implements this split and produces simple cycles, discarding two-edge
backtracks. Test each resulting cycle for nonzero winding about the origin.

The search detects a surrounding open cycle whenever one exists in the
induced annulus graph. To see this, choose a component containing such a
cycle. The origin lies in a bounded component of its planar complement.
The boundary walk of its unbounded face consequently has winding +1 or -1
about the origin, according to orientation. Winding is additive when a
closed walk is split at a repeated vertex: both its directed edges and
their contributions to winding are partitioned. Backtracks have winding
zero. At least one resulting simple cycle therefore has nonzero winding
and surrounds the origin. The converse follows because every output is
a cycle of the induced open graph.

Of these candidates choose the one of minimum edge count, breaking ties
lexicographically after canonical rotation and reversal. This is a minimum
over the extracted candidates; it need not be a shortest surrounding cycle
among all cycles of the graph. The choice uses no currents. The two annuli
are disjoint, so any two selected circuits are vertex-disjoint and nested.

Stop the network at the original radius-R boundary, rather than at a chosen
circuit. Partition physical edges by which selected circuits surround their
midpoints. An edge on a circuit belongs to its inner layer. Chords with
both endpoints on the circuit are assigned according to their midpoint;
they are not automatically treated as circuit edges. Planarity implies
that an edge not on a circuit cannot cross it except at an endpoint.
Thus these edge assignments form successive layers. Explicitly include
every interface vertex in both adjacent layers, even if isolated on one
side. Nonconsecutive layers are disjoint; consecutive layers intersect
in precisely their shared circuit vertices. All other components remain.

The code checks these vertex intersections and the edge partition in every
sample. The audit independently classifies edges and vertices by flooding
the dual graph of all triangular faces from outside B_R, blocking just the
selected circuit edges. This avoids relying twice on the midpoint winding
calculation. Closed-site radial crossing searches also agree with the
presence or absence of every circuit in both passes. Explicit simple-cycle
enumeration gives a further check on 256 small random annuli.

## 3. Circuit repair bound

For each layer let theta_i be the optimal unit flow when its two terminal
sets are separately wired. Let R_i be its energy and A=sum_i R_i. At an
interface C_i define

    r_i(v) = -div theta_i(v),
    l_{i+1}(v) = div theta_{i+1}(v),
    delta_i = r_i-l_{i+1}.

Divergence means outgoing minus incoming current. Both profiles sum to 1,
so delta_i sums to zero. The concatenated local optima have divergence
-delta_i at the interface.

Here is the lower bound with disconnected layers included. A global unit
flow has net current 1 in each layer, by conservation on the union of all
layers to the source side of a cut. Its restriction is therefore a feasible
local wired unit flow. Summing their minimum energies gives A<=R_full.

On an oriented unit circuit with vertices v_0,...,v_{N-1}, write

    H_j = sum_{k=0}^j delta(v_k),
    Hbar = (1/N) sum_j H_j.

Every flow with divergence delta is f_j=c+H_j, because
f_j-f_{j-1}=delta(v_j), including the cyclic closing equation. The energy
sum_j(c+H_j)^2 is minimized at c=-Hbar. Consequently

    Q_C(delta) = sum_j(H_j-Hbar)^2
              = (1/N) sum_{j<k}(H_j-H_k)^2.             (1)

The second equality follows by expanding the squares: the numerator is
N sum H_j^2-(sum H_j)^2. It supplies a separate numerical evaluation.

Every theta_i vanishes on edges having both endpoints in one terminal set,
because those endpoints have equal wired voltage. Thus theta vanishes on
every circuit edge. Add the minimizing circuit flow of divergence delta_i
on each interface. The resulting global flow is feasible; its interface
divergences cancel. Its energy is exactly A+sum_i Q_Ci(delta_i), since the
repairs have disjoint supports and theta vanishes there. Minimization gives

    0 <= R_full-A <= C,    C = sum_i Q_Ci(delta_i).    (2)

For t=(1/2)sum|delta(v)|, any difference of two H_j is a sum of a subset
of delta, hence has absolute value at most t. If a=min H_j and b=max H_j,
then (H_j-a)(b-H_j)>=0. Averaging and subtracting Hbar^2 gives variance
at most (b-Hbar)(Hbar-a)<=(b-a)^2/4<=t^2/4. Therefore

    Q_C(delta) <= N t^2/4.                            (3)

The saved circuit data contain N, t, Q, Q/N (the cumulative-current
variance), and Nt^2/4 separately. They do not substitute a typical circuit
or a separately generated cluster into either side of (2).

## 4. Electrical solve and independent checks

Wire the terminal sets to a source s and sink t. Remove quotient loops;
they carry zero current. Ground t and solve the unit-source Laplacian with
diagonally preconditioned conjugate gradients. Quotient components disjoint
from both terminals carry zero flow; their physical edges are retained with
flow zero. Components meeting just one terminal are harmless dangling pieces.

Two variational evaluations check each solve. Let v be any grounded
potential, g its edge differences, b=1_s-1_t, and R the true resistance.
For a feasible unit flow theta, summation by parts and Cauchy–Schwarz give

    b dot v = sum_e theta(e)g(e),
    (b dot v)^2 <= R sum_e g(e)^2.

Thus L=(v(s))^2/sum g^2 is a lower bound on R. To get an upper bound, form
d=b-div g. Its sum is zero. Choose a spanning tree rooted at t. For every
nonroot vertex u, send the sum of d over its descendant subtree from u to
its parent. The divergence of this tree flow h is d: at u, the outgoing
subtree total minus the incoming child subtree totals is d(u); the root
equation follows by total sum zero. Hence f=g+h is a feasible unit flow,
and U=sum f^2 is an upper bound. If a quotient tree edge has several
parallel physical representatives, put its correction on just one of them.

These are exact inequalities in real arithmetic. Their floating evaluations
are diagnostic bounds, with roundoff slack, not outward-rounded interval
certificates. The code checks divergence, relative U-L, and convergence.
The exact rational audit independently recomputes R, A, the profiles and C
in every nontrivial radius-12 configuration.

For the numerical local flows f_i, circuit edges still carry exactly zero
because they were quotient loops. Constructing their actual interface
mismatch and repairing it as above gives energy sum U_i+C_hat. This
identity does not require the f_i to be optimal. The code checks that the
repaired global flow conserves current and has that energy. The CSV field
A is sum U_i, R is the midpoint of its full-network diagnostic bounds, and
D=R-A. The ideal quantities in (2) are approximated by these fields; the
three exact rational sample checks validate their accuracy independently.

## 5. Interpretation

The wider pass contains 22 one-circuit configurations and no two-circuit
configuration. It measures the one-interface cost on actual finite
percolation configurations and supplies a reproducible implementation for
more interfaces. It does not measure accumulation of repair costs across
a growing sequence of circuits. Comparisons restricted to samples with a
circuit are explicitly conditional descriptive subsets of the original 120.

Neither finite conditioning nor these small radii justify replacing this
ensemble by the infinite IIC. There is no tail bound, no almost-sure estimate
C_R<=R^{o(1)} A_R, and no identification of an exponent for A_R. No exponent
is fitted.

For context, Irina Đanković, Maarten Markering, Jason Miller, Yizheng Yuan,
*The scaling limit of random walk and the intrinsic metric on planar critical
percolation*, [arXiv:2604.14122](https://arxiv.org/abs/2604.14122),
Corollaries 1.3–1.4, express the triangular-lattice IIC exponents as

    d_w = 91/48 + beta_res,
    d_s = 2(91/48)/(91/48 + beta_res).

Setting d_s=4/3 gives 6(91/48)=4(91/48+beta_res), so beta_res=91/96
and d_w=91/32. Substitution checks the same values independently. This
computation supplies no new bound on beta_res and does not decide AO.
