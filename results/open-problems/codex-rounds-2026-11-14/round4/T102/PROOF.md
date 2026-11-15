# Repairing boundary currents on open circuits

These are finite-network statements. They do not identify the resistance
exponent of planar critical percolation.

## 1. Setup and the earlier bound

Choose an orientation for each edge of a finite network with positive
resistances r(e). Divergence is outgoing minus incoming current, and

    E(f) = sum_e r(e) f(e)^2.

Let G_1,...,G_m be edge-disjoint layers with pairwise disjoint interfaces
S_0,...,S_m. Only consecutive layers intersect, at S_i; G_i has terminal
sets S_{i-1},S_i. Set S_0={x} and wire S_m as sink. Assume the union has an
x-to-S_m path. Retain all layer components and all interface vertices,
including vertices isolated within a particular layer.

Let theta_i be the minimum-energy wired unit flow through G_i. Write

    R_i = E(theta_i),
    l_i = div theta_i on S_{i-1},
    r_i = -div theta_i on S_i,
    delta_i = r_i - l_{i+1}  (1 <= i < m),
    A = sum_i R_i.

Both l_i and r_i have total mass 1 and are nonnegative. One way to see this
is to fix a common positive voltage on the left terminal set and zero on
the right. The harmonic maximum principle puts all interior voltages
between them; currents therefore leave each source vertex and enter each
sink vertex with nonnegative sign. Components meeting only one terminal
set have constant voltage and zero current. Components meeting neither
terminal set also have zero current. Normalize the total current to 1.
In particular delta_i has sum zero and

    t_i = (1/2) sum_{v in S_i} |delta_i(v)| <= 1.

For later use, theta_i is zero on every edge with both endpoints in one
of its terminal sets: those endpoints have the same wired voltage.

For a flow eta_i with zero divergence off the terminals and zero total
divergence on each terminal set, theta_i+s eta_i is a wired unit flow for
every real s. Differentiating its energy at s=0 gives

    <theta_i,eta_i>_r = 0,
    E(theta_i+eta_i) = R_i + E(eta_i).                 (1)

Any global unit flow restricts to a wired unit flow in each layer. Indeed,
summing its divergence over all layers to the left of an interface shows
that the net current through the interface is 1. Subtract theta_i in every
layer and use (1). Conversely, layer flows whose individual interface
divergences cancel concatenate into a global unit flow. Thus

    R_G(x,S_m) = A + D,   D >= 0,                    (2)

where D is the least total energy of corrections that cancel the mismatch.
The least-energy property used here follows directly from Kirchhoff's
equations: for prescribed divergence b, solve Lv=b after grounding one
vertex in each component. The resulting flow f(e)=(v(u)-v(w))/r(e) is
orthogonal to any zero-divergence flow h because
<f,h>_r=sum_z v(z) div h(z)=0. Its energy is therefore minimal. The same
argument applies after wiring each terminal set.

The preceding report bounds D by twice a sum of diameter-based repair
costs. The next result treats a geometric case where disjoint supports
give a smaller and directly computable bound.

## 2. Repair entirely within each interface

Suppose that for each i=1,...,m-1 a connected subgraph H_i has vertex set
S_i, and that all its edges belong to the union of G_i and G_{i+1}.
Each such edge has both endpoints in S_i. Different H_i have disjoint
vertices and hence disjoint edges. Edges of an H_i may be assigned to
either adjacent layer, provided every physical edge occurs exactly once.

For a zero-sum demand h on S_i, let Q_{H_i}(h) be the minimum energy of a
flow on H_i with divergence h. Connectivity ensures existence: fix a
vertex o and sum flows from each other vertex v to o with coefficients
h(v). Positive definite edge energy on the finite affine feasible space
ensures a unique minimum.

**Proposition.** Under these hypotheses,

    0 <= D <= sum_{i=1}^{m-1} Q_{H_i}(delta_i).       (3)

This does not require either adjacent layer to connect S_i in its own
unwired network.

**Proof.** Put the theta_i on their respective edge sets to form a global
edge assignment theta. Its divergence is +1 at x, has total -1 on S_m,
and is zero off these terminals and the interfaces. At v in S_i its
divergence is -r_i(v)+l_{i+1}(v)=-delta_i(v).

For each i take a minimum-energy flow h_i on H_i with divergence delta_i
and extend it by zero to the other edges. Then

    f = theta + sum_i h_i

is a global unit flow. Each theta_i is zero on every interface edge in
its layer, as observed in Section 1. Hence theta is zero on every H_i.
The h_i also have mutually disjoint edge supports. Expanding the energy
therefore gives the exact identity

    E(f) = A + sum_i Q_{H_i}(delta_i).

Taking the minimum over global unit flows and using (2) proves (3).

For a second verification, restrict the h_i to each layer. The restriction
of h_i to either adjacent layer has both endpoints of every edge in S_i,
so its total divergence on S_i is zero. It is therefore an admissible
correction in (1). Corrections from the two interfaces of one layer
have disjoint edge supports. Their energies add exactly, rather than
requiring E(a+b)<=2E(a)+2E(b). Summing (1) yields the same bound. This
also checks the component constraints in disconnected layers. QED.

In a planar network with disjoint nested open circuits surrounding x,
stop the graph at the outermost circuit and use the circuit vertices as
interfaces. Assign every edge in the intervening closed regions to its
layer; assign each circuit edge once to either adjacent layer. No edge
can skip a circuit: its embedded arc would have to cross that circuit
away from a shared vertex, contrary to planarity. Thus the layered
intersection conditions hold. All shell components can be retained.
Taking H_i to be the entire i-th circuit proves (3). In particular,
assigning that whole circuit to the inner layer guarantees that all its
vertices lie in one component there, so its ordinary resistance diameter
in that layer is finite. Other components need not be discarded.

## 3. Exact energy on a weighted circuit

Let C have distinct vertices v_0,...,v_{N-1}, N>=3, and oriented edges
e_j=(v_j,v_{j+1 mod N}) of resistance rho_j>0. Set

    W = sum_j rho_j,
    h_j = h(v_j),   sum_j h_j=0,
    H_j = sum_{k=0}^j h_k,
    Hbar = (sum_j rho_j H_j)/W.

Since H_{N-1}=0, every flow of divergence h has the form

    f_j = c + H_j.

Indeed f_j-f_{j-1}=h_j, including j=0 by cyclic indexing, and subtracting
two such flows gives a constant circulation. Its energy is

    sum_j rho_j(c+H_j)^2
      = W(c+Hbar)^2 + sum_j rho_j(H_j-Hbar)^2.

Minimizing in c proves

    Q_C(h) = sum_j rho_j(H_j-Hbar)^2
           = sum_j rho_j H_j^2 - (sum_j rho_j H_j)^2/W.       (4)

This expression is independent of the initial vertex and orientation,
since either change only reparametrizes flows with the same divergences.
An algebraically independent form follows by expanding all pairwise
differences:

    Q_C(h) = (1/W) sum_{j<k} rho_j rho_k (H_j-H_k)^2.        (5)

Indeed twice the numerator obtained by summing over ordered pairs equals
2W sum_j rho_j H_j^2 - 2(sum_j rho_j H_j)^2. Dividing by 2W gives (4).

Put t=(1/2)sum_j |h_j|. For any j<k, H_k-H_j is a sum of a subset of the
coordinates of h, whose positive and negative masses are each at most t.
Thus max H_j-min H_j<=t. Write a=min H_j and b=max H_j. Since
(H_j-a)(b-H_j)>=0, weighted averaging gives

    (sum rho_j H_j^2)/W <= (a+b)Hbar-ab.

Subtract Hbar^2. The result is at most
(b-Hbar)(Hbar-a) <= (b-a)^2/4 <= t^2/4. Consequently

    Q_C(h) <= W t^2/4.                               (6)

This constant is attained on a unit-resistance even circuit by a unit
dipole between antipodal vertices: each half-circuit has resistance N/2,
and the two halves in parallel have resistance N/4.

More generally, a dipole t(1_u-1_v) splitting a weighted circuit into arcs
of resistances s and W-s has energy

    t^2 s(W-s)/W.                                    (7)

This follows independently from the parallel-resistor law, and also from
(4), because the cumulative demand takes two values differing by t on
the two arcs.

The actual demand can matter much more than its total variation. On a
unit even circuit take h_j=2(-1)^j/N. Then t=1, H_j alternates between
2/N and 0, Hbar=1/N, and (4) gives Q_C(h)=1/N. For the antipodal unit
dipole on the same circuit, Q_C=N/4 with the same t=1. The coarse bound
(6) exceeds the alternating-demand energy by a factor N^2/4.

Combining (3) and (4), and then (6), gives

    A <= R_G(x,S_m)
      <= A + sum_i sum_{e_j in C_i} rho_j(H_{i,j}-Hbar_i)^2
      <= A + (1/4) sum_i W_i t_i^2.                  (8)

Formula (4) can be evaluated in linear time in each circuit length once
the two local wired profiles are known.

## 4. Equality and an obstruction with nested circuits

Fix k>=1 disjoint circuits C_1,...,C_k, nested in a planar embedding.
Give C_j length 2L_j of unit-resistance edges, with L_j>=2, and mark
antipodal vertices u_j,v_j. Add a unit edge from x to u_1, a unit edge
from v_j to u_{j+1} for each j<k, and a unit edge from v_k to y. The
circuits can be drawn concentrically with each connecting edge in the
appropriate complementary annulus. All other vertices have degree 2;
u_j,v_j have degree 3. Thus this is a planar unit-resistance network
of maximum degree 3. Each circuit separates x from y.

Take S_0={x}, S_j=V(C_j), and S_{k+1}={y}. Give G_j the entering bridge
and all edges of C_j for 1<=j<=k; G_{k+1} consists of the last bridge.
Include all vertices of each adjacent interface in its layer, even when
isolated there. Each separately wired layer is a single unit bridge;
its circuit edges have both ends wired and carry zero current. Therefore

    R_j=1 (1<=j<=k+1),   A=k+1.

The outgoing profile from G_j is a unit mass at u_j; the incoming profile
to G_{j+1} is a unit mass at v_j. Hence delta_j=1_{u_j}-1_{v_j} and

    Q_{C_j}(delta_j)=L_j/2.

Every global unit flow carries unit current across each bridge. Within
C_j it carries unit current from u_j to v_j, since those are the only
vertices of that circuit incident to edges outside it. If a and 1-a
are the currents on its two length-L_j arcs, their energy is

    L_j a^2 + L_j(1-a)^2
      = 2L_j(a-1/2)^2 + L_j/2.

The minimum is L_j/2, independently in each circuit. Thus

    R_G(x,y)=k+1+(1/2)sum_j L_j,
    D=(1/2)sum_j L_j=sum_j Q_{C_j}(delta_j).          (9)

This both proves sharpness of the coefficient 1 in (3) and shows that
the presence of nested open circuits alone cannot imply R_G<=C A for
a universal constant C: fix k and let any L_j increase. For k=2 and
L_1=L_2=L, A=3, R_G=L+3, and R_G/A=1+L/3.

Even the finite-side diameter assumption of the previous report need
not hold under another permissible circuit-edge assignment. For k=1,
use a square v_0v_1v_2v_3v_0. Put x-v_0 and edges v_0v_1,v_2v_3 in
the inner layer; put v_2-y and edges v_1v_2,v_3v_0 in the outer layer.
Both layers have infinite ordinary resistance diameter on S_1. Yet the
complete circuit connects S_1. The two unit bridges and two length-2
arcs give A=2, R_G=3, and D=Q_C(1_{v_0}-1_{v_2})=1. Proposition (3)
applies directly. No infinite diameter is used in its proof.

These examples are deterministic network obstructions. They are not
statements about the probability of such events in a percolation cluster.

## 5. What remains for the IIC

For a rooted exhaustion stopped at scale 2^n with nested circuit interfaces,
write A_n for its sum of wired layer resistances and

    C_n = sum_i Q_{C_i}(delta_i),

using the circuits and local profiles of that same realization. If b>=0,
A_n=2^{nb+o(n)}, and C_n<=2^{nb+o(n)}, then (8) sandwiches the rooted
resistance between 2^{nb+o(n)} and 2^{nb+o(n)}. Taking logarithms proves
the same exponent b. It suffices to have C_n<=2^{o(n)} A_n. One may use
sum_i W_i t_i^2<=2^{o(n)}A_n as a stronger sufficient condition.

No such estimate is proved under the IIC law here. A choice of nested
circuits must also control their Euclidean locations and their relation
to the stopping ball. Section 4 shows why circuit connectivity itself
cannot replace an estimate on the current mismatch energy.

For the triangular-lattice IIC, Irina Đanković, Maarten Markering, Jason
Miller, Yizheng Yuan, *The scaling limit of random walk and the intrinsic
metric on planar critical percolation*,
[arXiv:2604.14122](https://arxiv.org/abs/2604.14122), Corollaries 1.3–1.4,
express the exponents as

    d_w = 91/48 + beta_res,
    d_s = 2(91/48)/(91/48 + beta_res).

Their “Explicit lengths” discussion leaves beta_res unidentified. Solving
2d_f/(d_f+beta_res)=4/3 gives beta_res=d_f/2=91/96, and then
d_w=91/32. The deterministic circuit bound gives no new value or bound
for beta_res and does not decide whether d_s=4/3. The network arguments
above follow from minimum energy and explicit cycle flows; no claim of
prior unpublished status is made.
