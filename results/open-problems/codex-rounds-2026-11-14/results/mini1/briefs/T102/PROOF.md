# Resistance across interfaces

The result here is deterministic. It identifies a boundary-current correction
in a decomposition of resistance into annular pieces. It does not determine
an exponent for percolation.

## 1. Flow convention and the minimum-energy principle

Let a finite network have positive resistances r(e). Choose one orientation
for each edge. A flow f assigns a real number to each oriented edge; its
divergence at a vertex is outgoing current minus incoming current. Write

    E(f) = sum_e r(e) f(e)^2,
    <f,g>_r = sum_e r(e) f(e) g(e).

For disjoint terminal sets U,V, let F(U,V) be the affine space of flows with
zero divergence outside U union V, total divergence +1 on U, and total
divergence -1 on V. Individual terminal divergences are unrestricted real
numbers. Suppose F(U,V) is nonempty. Its unique minimum-energy element
theta has energy equal to the effective resistance with U wired and V wired.

For completeness, consider the graph after identifying U and identifying V,
and keep the component containing these two terminals. Its Laplacian is
L = B C B^T, where B is the incidence matrix and C has entries 1/r(e).
Solve L v = b, where b is +1 at the source terminal, -1 at the sink, and
zero elsewhere, fixing one additive constant. Then f = C B^T v has divergence
b. For any other such flow f+h, B h=0 and

    <f,h>_r = v^T B h = 0.

Consequently E(f+h)=E(f)+E(h), so f uniquely minimizes energy. Also
E(f)=v^T b, the voltage difference for one unit of current, which is effective
resistance. Edges collapsed into loops carry zero in the minimizer and may
be discarded. Components containing neither terminal also carry zero.
This proves the asserted principle, including its interpretation before
wiring.

The same argument can be expressed without potentials. If H is the vector
space parallel to F(U,V), then theta+t h belongs to F(U,V) for every real t
and every h in H. Differentiating its energy at t=0 gives

    <theta,h>_r = 0,
    E(theta+h) = E(theta)+E(h).                         (1)

This orthogonality will give an exact correction rather than an inequality.

## 2. Two pieces with a common interface

Let A,B be connected finite networks, sharing exactly the vertex set S and
having disjoint edge sets. Let x belong to A outside S, and y to B outside S.
The network G is their union. Set

    R_A = R_A(x,S wired),   R_B = R_B(S wired,y).

Let theta_A, theta_B be their optimal unit flows. Define interface vectors

    q_A(s) = -div theta_A(s),
    q_B(s) =  div theta_B(s),       s in S.

Both vectors have coordinate sum 1. Put H={h in R^S: sum_s h(s)=0}.
For h in H define Q_A(h) to be the minimum energy of a flow in A with
divergence h on S and zero everywhere else, including x. Define Q_B(h)
in the same way in B, with zero divergence at y. Connectivity makes these
flows feasible. These are positive definite quadratic forms on H: the
minimum-energy flow depends linearly on the divergence, and zero energy
forces every edge current, hence the divergence, to vanish. The sign of h
does not matter because Q_A(-h)=Q_A(h), and similarly for B.

**Proposition 1.** The exact identity is

    R_G(x,y) = R_A + R_B + D,
    D = min_{sum q=1} [Q_A(q-q_A)+Q_B(q-q_B)].          (2)

In particular, D is nonnegative and vanishes exactly when q_A=q_B.

**Proof.** Restrict any unit x-to-y flow in G to A and B. Conservation off
the terminals and interface implies that its restrictions belong to
F_A({x},S) and F_B(S,{y}). Conservation at each vertex of S says that the
outgoing profile from A and incoming profile into B agree at some vector q
of sum 1. Conversely, any two such flows with the same profile combine into
a unit x-to-y flow. No nonnegativity restriction on q is needed.

For fixed q, subtract theta_A from the A flow. Its divergence on S is
-(q-q_A) and is zero elsewhere. By (1), the minimum possible A energy is
R_A+Q_A(q-q_A). The B minimum is R_B+Q_B(q-q_B). The edges are disjoint,
so these energies add. Minimizing over q proves (2). Strict positivity of
the forms implies the last assertion. The minimum is attained since the
objective is a positive definite quadratic function on the affine space
of q. This proves the proposition.

There is a matrix form useful for finite calculations. Use an orthonormal
basis of H and let M_A,M_B be the matrices of Q_A,Q_B. With
delta=q_A-q_B, (2) gives

    D = delta^T (M_A^{-1}+M_B^{-1})^{-1} delta.         (3)

To verify the formula without assuming commutativity of the matrices, put
z=q-q_A. The expression to minimize is
z^T M_A z+(z+delta)^T M_B(z+delta). At its minimizer,

    M_A z + M_B(z+delta)=0.

Set w=M_B(z+delta)=-M_A z. Then
delta=(M_A^{-1}+M_B^{-1})w. The minimum energy is
w^T(M_A^{-1}+M_B^{-1})w=delta^T w, which is (3).
If S has one vertex then H has dimension zero and D=0.

## 3. A unit-resistance planar obstruction

For an integer L>=1, take four internally disjoint paths with endpoints and
lengths

    x--u: 1,    x--v: L,    u--y: L,    v--y: 1.

All edges have resistance 1. This is a simple cycle with 2(L+1) edges,
maximum degree 2, and a planar embedding. Let A be the two paths incident
to x, B the two paths incident to y, and S={u,v}.

After wiring S, each piece consists of paths of resistances 1 and L in
parallel. Hence

    R_A=R_B=L/(L+1).

In the unmodified cycle the two x-to-y paths both have length L+1, so

    R_G(x,y)=(L+1)/2,
    D=(L-1)^2/[2(L+1)],
    R_G/(R_A+R_B)=(L+1)^2/(4L).                       (4)

Here is a separate derivation of D from interface currents. In the order
(u,v), the wired optimal profiles are

    q_A=(L/(L+1),1/(L+1)),
    q_B=(1/(L+1),L/(L+1)).

For h=(t,-t), transferring current between u and v inside either piece
requires the unique path of length L+1. Thus Q_A(h)=Q_B(h)=(L+1)t^2.
Writing q=(a,1-a), the objective in (2) is

    (L+1)[(a-L/(L+1))^2+(a-1/(L+1))^2].

Its minimizer is a=1/2. Substitution gives the value of D in (4).

Thus no universal constant C satisfies

    R_{A union B}(x,y) <= C [R_A(x,S wired)+R_B(S wired,y)]

even for simple planar networks of maximum degree 2 with unit resistances.
For L=1 the profiles match and D=0. As L tends to infinity, the sum of
wired resistances tends to 2 while the full resistance tends to infinity.
This example has no percolation probability attached to it. In particular,
it does not rule out an estimate that holds with high IIC probability.

## 4. Several pieces, including disconnected annuli

Let G_1,...,G_m have disjoint edge sets and interface sets S_0,...,S_m.
These sets are pairwise disjoint. Consecutive pieces intersect exactly on
S_i, and nonconsecutive pieces do not intersect. Piece G_i contains its
left terminal set S_{i-1} and its right terminal set S_i. Set S_0={x};
the final set S_m is wired as the sink. A piece need not be connected.
Assume the union G has a path from x to S_m.

Write F_i=F_{G_i}(S_{i-1},S_i), let theta_i minimize its energy, and put
R_i=E(theta_i). These affine spaces are nonempty: a path through the union
must cross each layer and contains a subpath in G_i joining its terminal
sets. For a flow f in F_i write

    l_i(f)= div f restricted to S_{i-1},
    r_i(f)=-div f restricted to S_i.

Both profiles have sum 1. Let H_i be the linear space of flows eta with
zero divergence off the two terminal sets and total divergence zero on
each terminal set. Define

    D_m = min sum_{i=1}^m E(eta_i),                    (5)

where eta_i is in H_i and, for every i<m, the full coordinate vectors obey

    r_i(theta_i+eta_i)=l_{i+1}(theta_{i+1}+eta_{i+1}).

**Proposition 2.** With these definitions,

    R_G(x,S_m wired) = sum_{i=1}^m R_i + D_m.          (6)

**Proof.** A global unit flow restricts to a flow in each F_i. To see that
its net current through each layer is one, sum divergence over all vertices
on the source side of an interface; the only net injection is at x. Its
restrictions satisfy the matching equations above by vertex conservation.
Conversely, matching flows in the F_i combine into a global unit flow,
since the two interface divergences cancel at every interface vertex.

Write the restrictions as theta_i+eta_i. Equation (1) holds in each affine
space F_i, independently of connectedness. Disjoint edge sets therefore give

    E(global flow)=sum_i R_i+sum_i E(eta_i).

Minimization proves (6). Feasibility follows from the assumed global path;
the minimum exists because the correction energy is strictly positive
definite on the finite-dimensional edge variables. This also proves D_m>=0.
Disconnected components impose componentwise conservation automatically
through H_i; they must not be replaced by unrestricted interface vectors.

## 5. A precise sufficient estimate for an annular approach

Suppose G^(m) is a network exhausted at radius 2^m, decomposed as above into
an inner piece and consecutive dyadic shells. Assign edges within an
interface to one adjacent piece only, so that edge sets remain disjoint.
Stop at the outer interface: vertices and edges outside it do not enter
the rooted, wired exit resistance. Retain every component of each shell
that occurs in this finite graph. Formula (6) then applies even if a shell
is disconnected. Let A_m=sum_{i=1}^m R_i and use D_m from (5).

**Corollary.** For a fixed realization, suppose b>=0 and

    log A_m / (m log 2) -> b,
    log(1+D_m) / (m log 2) has limsup <= b.            (7)

Then log R_{G^(m)}(x,S_m)/(m log 2) -> b.

**Proof.** The lower bound follows from R=A_m+D_m>=A_m. For every eps>0,
eventually A_m<=2^{m(b+eps)} and 1+D_m<=2^{m(b+eps)}. Consequently
R<=2*2^{m(b+eps)}. Taking logarithms gives upper limiting exponent at most
b+eps; let eps decrease to zero. This proves the corollary.

The second condition of (7) cannot be discarded on deterministic grounds,
as (4) shows. It is enough, for example, to prove

    D_m <= 2^{o(m)} A_m

together with the first condition of (7). Indeed this bounds
1+D_m by 1+2^{o(m)}A_m, whose upper exponent is at most b when b>=0.
Neither estimate is proved here for the IIC. In particular, estimates for
one typical shell do not imply the required simultaneous almost-sure
estimates for the shells of one rooted cluster.

For the triangular-lattice IIC, the existing results of Irina Đanković,
Maarten Markering, Jason Miller, Yizheng Yuan,
*The scaling limit of random walk and the intrinsic metric on planar
critical percolation*, [arXiv:2604.14122](https://arxiv.org/abs/2604.14122),
Corollaries 1.3–1.4, give the rooted resistance exponent and

    d_w=91/48+beta_res,   d_s=2(91/48)/(91/48+beta_res).

Thus an IIC proof of (7) with b>91/96 would imply d_s<4/3. Algebraically,
for D=91/48 and b>0,

    2D/(D+b)<4/3  iff  6D<4D+4b  iff  b>D/2=91/96.

The contribution of (2) and (6) is to specify the missing current-matching
quantity in this possible route. They give no numerical lower bound for
beta_res and make no claim of a new electrical-network principle.
