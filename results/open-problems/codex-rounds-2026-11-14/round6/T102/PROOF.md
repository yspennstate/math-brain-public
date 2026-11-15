# Nested circuit peeling and finite resistance measurements

The statements here concern finite triangular-lattice configurations. They
do not identify the resistance exponent of the incipient infinite cluster.

## 1. Finite law and circuit rule

Use triangular coordinates v=(a,b), embedded at
(a+b/2,sqrt(3)b/2). Neighbor differences, in cyclic order, are

    (1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1).

Put |v|=max(|a|,|b|,|a+b|) and B_R={v:|v|<=R}. Fix the origin open and
retain every other site in B_R independently with probability 1/2. Reject
unless the open origin connects to a vertex of radius R. This gives exactly
Bernoulli percolation conditioned on that connection: the event already
implies that the origin is open. Retain every open component, including
components disconnected from the origin. Every open nearest-neighbor edge
has resistance 1. All open radius-R sites form the wired sink.

The scripts use reproducible pseudorandom bits for this prescription, not
an exact enumeration. The stated conditional law describes the ideal
independent-bit sampling rule; the finite outputs prove no probability
estimate for that law.

For circuit selection only, start with

    V_0={v open:1<=|v|<R}.

The origin and the stopping boundary are excluded from this selection
graph. They are retained in the electrical network.

For a finite remaining set V, form its induced open graph. Order neighbors
in the cyclic order above. A directed edge (u,v) has successor (v,w), where
w is the neighbor immediately clockwise from u at v. This is a permutation
of directed edges, and its orbits are face boundary walks. Trace every
orbit. Within each walk, keep a stack of distinct vertices. When a vertex
repeats, split off the closed segment between its two occurrences. Keep
segments of length at least three whose simple polygon strictly encloses
the origin; discard two-edge backtracks. Canonicalize a cycle by starting
at its least vertex and taking the lexicographically smaller orientation.
Let K(V) be the resulting finite set of enclosing simple cycles.

If K(V) is empty, stop. Otherwise select the canonical cycle C minimizing

    (T(C), C),
    T(C)=|sum_j (a_j b_(j+1)-a_(j+1) b_j)|,

in lexicographic order, with cyclic indexing. T(C) is twice coordinate
area. The Euclidean area is sqrt(3)T(C)/4, so this orders by enclosed
geometric area. The minimum is over the extracted candidates. No assertion
that this finds a minimum-area cycle among all graph cycles is needed.
Replace V by its vertices strictly outside C and repeat. All comparisons
and point-in-polygon tests use integers. No electrical quantity enters.

The selected cycles, in order, are C_1,...,C_k. Their complete ordered
vertex lists and the candidate counts at every step, including termination,
are saved. The rule is fixed for the pilot and the new ensemble.

## 2. Existence detection, termination and nesting

**Lemma 1.** K(V) is nonempty if and only if the induced graph on V has a
simple cycle strictly enclosing the origin, provided the origin is not a
vertex of that graph.

**Proof.** Every element of K(V) is such a cycle, proving one direction.
For the other, choose a connected component containing an enclosing cycle.
The origin belongs to the bounded interior of that cycle and is not on
any edge of the component: in the triangular lattice no nearest-neighbor
edge passes through the origin unless it has the origin as an endpoint.
The boundary walk of the component's unbounded face has winding number
+1 or -1 about the origin. One can see this by following the outer boundary
of a sufficiently thin planar neighborhood of the component; the origin
lies in a bounded complementary component. Bridges are traversed in both
directions and contribute zero winding.

Splitting a closed walk at repeated vertices partitions its directed edges
into simple closed subwalks and backtracks. Winding is additive under this
partition, since it is the integral of change of argument along directed
edges. Backtracks contribute zero. At least one retained simple closed
subwalk has nonzero winding about the origin. A simple polygon has nonzero
winding precisely at its interior points, so it is in K(V). This proves
the lemma. The face tracing includes separate components and both sides
of bridges, as required. QED.

**Lemma 2.** Peeling terminates after finitely many selections and produces
vertex-disjoint strictly nested cycles surrounding the origin.

**Proof.** At each selection at least the chosen cycle's vertices are
removed. The remaining set is finite, so termination follows. Every later
cycle uses only vertices strictly outside every previously selected cycle.
Nearest-neighbor edges in this planar embedding have disjoint interiors
unless they are the same edge. Thus distinct selected cycles cannot cross
or share vertices. Two disjoint Jordan curves surrounding the same point
are nested: each connected curve lies in a single complementary component
of the other, and their bounded interiors cannot be disjoint because both
contain the origin. A later curve cannot lie inside an earlier one, since
all its vertices lie strictly outside. Hence it surrounds the earlier
curve strictly. QED.

The output is not asserted to maximize the number of disjoint cycles.
Termination certifies that no further enclosing cycle remains strictly
outside the last selected cycle, by Lemma 1. It does not certify that no
other cycle could be inserted between two selected interfaces.

An independent existence test uses the dual of the full triangulation of
B_R. Block dual crossings of every edge whose endpoints are in the
remaining open set. Flood from exterior triangular faces across unblocked
edges. Since the origin is absent from the selection graph, all triangles
incident to it are mutually reachable around it. There is an enclosing
open cycle exactly when these triangles cannot be reached from outside.
Indeed a simple open cycle blocks every dual crossing between its interior
and exterior. Conversely a finite face component containing the origin
has a boundary made of blocked edges; its boundary walks split into cycles,
one of which surrounds the origin. This gives a check independent of face
walk enumeration and of winding-number evaluation. The audit applies it
before every selection and again at termination.

## 3. Partition into electrical layers

Use the original open graph, including its origin, radius-R sites and all
other components. For every edge assign it to the layer specified by which
C_i enclose its midpoint. On a circuit itself, assign the edge to its
inner layer. An edge not on the circuit cannot cross it away from an
endpoint, by planarity. An edge whose two endpoints are on a circuit may
be an interior or exterior chord, so it is assigned by its midpoint rather
than by its endpoints alone.

The boundaries are S_0={0}, S_i=V(C_i), and S_(k+1) the open radius-R
sites. Include every vertex of S_i in both adjacent layers, even if it is
isolated on one side. Nonconsecutive layers are disjoint; consecutive ones
intersect exactly at their common S_i. Every physical edge occurs exactly
once. The origin-to-boundary connection crosses every enclosing circuit,
so every layer has a crossing between its terminal sets after wiring.
No disconnected component is dropped.

The production code checks the edge partition and all layer intersections.
The audit independently classifies vertices and edges by flooding the
triangular-face dual while blocking only the chosen circuit's edges. An
edge on that circuit is treated as boundary; every other edge's incident
triangles must have the same interior/exterior status. This checks the
midpoint classification without repeating its winding calculation.

## 4. Exact finite energy bound

Orient physical edges arbitrarily. Divergence means outgoing minus incoming
current, and E(f)=sum_e f(e)^2. For each layer G_j, minimize energy over flows
with divergence zero off S_(j-1) union S_j and total divergences +1 and -1
on those two sets. Let theta_j be this unique minimum and R_j its energy.
It is the separately wired resistance. Existence follows by sending current
along a layer crossing; strict convexity gives uniqueness.

For completeness, the wired minimizer is a gradient: identify each terminal
set to one vertex, ground the sink, and solve the Laplacian equation for
unit source current. Summation by parts gives

    sum_e theta_j(e) h(e)=sum_v potential(v) div h(v)=0

whenever h has zero divergence off the terminal sets and zero total on each.
The potential is constant on each terminal set. Therefore theta_j is
orthogonal to every admissible correction, and

    E(theta_j+h)=R_j+E(h).

This argument also handles disconnected layers: components without a
source-to-sink crossing carry zero current unless wiring connects them
through a terminal. Components meeting neither terminal carry zero current.

Put A=sum_j R_j. Every global unit flow restricts to one unit of net
current through each layer, by summing its divergence over the source side
of each interface. Its layer restriction is an admissible wired unit flow.
Thus its energy is at least A, and minimization gives A<=R_full.

At C_i put

    delta_i(v)=-div theta_i(v)-div theta_(i+1)(v).

The two interface profiles each have total mass 1, so sum_v delta_i(v)=0.
Their concatenation has divergence -delta_i at the interface. Every circuit
edge has both endpoints in a wired terminal set of its owning layer, so
its local optimum current is zero.

Both profiles are nonnegative. Set the wired source voltage to a positive
constant and the sink voltage to zero. The harmonic maximum principle
places every interior voltage between them, so currents leave each source
vertex and enter each sink vertex with nonnegative sign. Normalize their
total to one. Components meeting only one terminal have constant potential.
Consequently t_i=(1/2)sum_v |delta_i(v)|<=1.

On a unit circuit v_0,...,v_(N-1), let h sum to zero and set

    H_j=sum_(l=0)^j h(v_l),  Hbar=(1/N)sum_j H_j.

A flow f_j on the oriented edge v_j to v_(j+1) has divergence h exactly
when f_j-f_(j-1)=h(v_j). Every solution is f_j=c+H_j. Its energy is

    sum_j(c+H_j)^2=N(c+Hbar)^2+sum_j(H_j-Hbar)^2.

The least repair energy is consequently

    Q_C(h)=sum_j(H_j-Hbar)^2
          =(1/N)sum_(j<l)(H_j-H_l)^2.

The last equality follows by expanding the pairwise squares. Add these
minimizing circuit flows with h=delta_i to the concatenated theta_j. Their
divergences cancel every interface defect; the result is a global unit
flow. The repair supports are disjoint, and theta vanishes on every one
of their edges. Its energy is exactly

    A+C,  C=sum_i Q_(C_i)(delta_i).

Minimizing global energy proves

    0<=R_full-A<=C.

The recorded coarse cost also has a direct bound. For a zero-sum h put
t=(1/2)sum|h|. A difference of two cumulative values H_j is a sum over an
arc, whose positive and negative masses are each at most t. Thus their
range b-a is at most t. Averaging (H_j-a)(b-H_j)>=0 gives

    (1/N)sum H_j^2 <= (a+b)Hbar-ab.

Subtract Hbar^2 to obtain variance at most
(b-Hbar)(Hbar-a)<=(b-a)^2/4<=t^2/4. Therefore Q_C(h)<=Nt^2/4. The CSV
keeps N, t, Q_C, Q_C/N and Nt^2/4 separately.

There is no assumption about the number or connectedness of shell
components. The proof applies equally to zero, one or many selected
circuits. With no circuits, A=R_full and C=0, which gives no gluing test.

## 5. Independent electrical verification

Production measurements use the previous sparse PCG solver. Any grounded
potential v gives the resistance lower bound v(source)^2/E(gradient v),
by Cauchy–Schwarz against a unit flow. Routing its divergence residual
on a spanning tree gives an explicit feasible unit flow and hence an
upper bound. The actual circuit-repaired flow is checked for conservation
and energy equal to the sum of numerical layer energies plus numerical C.
These are floating diagnostic bounds; their differences at machine
roundoff are not rigorous outward-rounded error certificates.

The new independent exact solver uses rational sparse Schur elimination
on the grounded prescribed-current Laplacian. If v is a free vertex with
diagonal d>0, off-diagonal entries a_u and right-hand side b_v, its equation
is d x_v+sum_u a_u x_u=b_v. Substitution into the other equations gives

    L'_(u,w)=L_(u,w)-a_u a_w/d,
    b'_u=b_u-a_u b_v/d.

Store this equation and back-substitute after all free vertices are
eliminated. Positivity of the grounded Laplacian makes every pivot positive.
All operations use exact fractions. The resulting currents are checked
for exact vertex conservation, and their energy is checked against the
unit-current source voltage. Grounding is done on the quotient component
containing both terminals; other components carry zero flow. Wiring loops
have zero current.

This solver recomputes R_full, every R_j, every signed mismatch and each
Q_C exactly for the designated multi-interface samples. It verifies
0<=R_full-A<=C as a rational inequality and compares R,A,C with the saved
floating values. Ten smaller networks also compare this prescribed-current
solver with the previous independent dense unit-voltage solver.

## 6. Scope

The pilot reuses all 120 earlier accepted configurations without altering
or rejecting them. The new ensemble has a separately fixed seed and 200
accepted configurations at each R=12,24,48. The only sampling condition
is an origin-to-boundary connection. Samples lacking circuits remain in
the output. Statistics restricted to one or several circuits are explicitly
conditional descriptive subsets. Circuit locations are recorded as their
minimum and maximum hexagonal radii. Peeling does not impose a fixed
annular aspect ratio or separation of scales.

Neither these finite laws nor their small multi-interface subsets give
an almost-sure bound on the IIC. In particular they do not establish
C_R<=R^{o(1)}A_R or identify an exponent for A_R.

For context, Irina Đanković, Maarten Markering, Jason Miller, Yizheng Yuan,
*The scaling limit of random walk and the intrinsic metric on planar
critical percolation*, [arXiv:2604.14122](https://arxiv.org/abs/2604.14122),
Corollaries 1.3–1.4, give on the triangular-lattice IIC

    d_w=91/48+beta_res,
    d_s=2(91/48)/(91/48+beta_res).

Setting d_s=4/3 yields beta_res=91/96 and d_w=91/32 by cross multiplication;
substitution gives the same values. The resistance exponent and the
Alexander–Orbach question remain unidentified here.

The separate radius-48 census fixes 2,000 accepted configurations before
sampling. It stores every graph and peeling trace in compressed JSONL and
every circuit count in a census CSV. Electrical solves are performed on
all and only configurations with at least two selected circuits. Thus its
electrical summary describes the conditional subset k>=2; it does not
estimate unconditional electrical moments. The geometry census retains
the zero/one cases and can be replayed independently. The seed and full
allocation rule are recorded in LOG.md before its first random bit.
