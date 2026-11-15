# Bounds for the cost of matching boundary currents

All statements below concern finite electrical networks. They give no new
numerical bound on the resistance exponent of the incipient infinite cluster.

## 1. Conventions and the gluing identity

Give every edge e a positive resistance r(e) and choose an orientation.
For an edge flow f, let div f be outgoing minus incoming current and put

    E(f)=sum_e r(e)f(e)^2,
    <f,g>_r=sum_e r(e)f(e)g(e).

For disjoint vertex sets U,V, a wired unit flow has zero divergence outside
U union V and total divergences +1 on U and -1 on V. Its individual boundary
divergences are unrestricted. Assume such a flow exists. Its unique
energy minimizer theta has energy R(U,V), with each terminal set wired.
If eta has zero divergence off U union V and zero total divergence on
each terminal set, theta+t eta is feasible for every real t. Minimization
of this quadratic in t gives

    <theta,eta>_r=0,
    E(theta+eta)=E(theta)+E(eta).                      (1)

The minimum-energy characterization follows directly from Kirchhoff's
law: on the wired graph, solve Lv=b for a unit source and sink. The flow
f(e)=(v(e^-)-v(e^+))/r(e) has the required divergence. For every zero-divergence
flow h, <f,h>_r=sum_v v(v)div h(v)=0, so E(f+h)=E(f)+E(h).
Its energy is the unit-current voltage drop, hence the resistance. Components
with no source-to-sink path carry zero current. The same argument applies
before wiring and proves (1).

Consider m layers G_1,...,G_m with disjoint edge sets and pairwise disjoint
interface sets S_0,...,S_m. Only consecutive layers meet, and their common
vertices are exactly S_i. Layer G_i contains S_{i-1} and S_i. Set S_0={x}
and wire S_m as the sink. Assume their union G contains an x-to-S_m path.
Every layer then has a feasible wired unit flow: a global path must contain
a crossing of that layer. Layers may be disconnected.

Let theta_i be the wired minimizer on G_i and let

    R_i=E(theta_i),
    l_i= div theta_i restricted to S_{i-1},
    r_i=-div theta_i restricted to S_i.

These profiles have coordinate sum 1. In fact they are nonnegative. To see
this, set the wired source voltage to R_i and the sink voltage to zero in
every component meeting both sides. The harmonic maximum principle places
all other voltages between these values. Each source boundary vertex has
nonnegative outgoing current and each sink vertex has nonnegative incoming
current. Components meeting only one terminal set have constant voltage
and zero flow. Edges within a wired terminal set also carry zero flow.
This proves the assertion, including the disconnected case.

Define H_i to be the space of flows on G_i with zero divergence off its two
terminal sets and zero total divergence on each terminal set. Put

    D_m = min sum_i E(eta_i),                         (2)

where eta_i belongs to H_i and the profiles of theta_i+eta_i match at every
interface. Such corrections exist by restriction of any global unit flow.
The feasible set is an affine subspace of finite-dimensional edge space,
and the positive definite energy is coercive, so the minimum exists.

The earlier result, independently re-derived here, is

    R_G(x,S_m)=sum_i R_i+D_m.                         (3)

Indeed a global unit flow restricts to one unit of net current in each
layer, by summing divergence on the source side of each interface. The
restricted flows have matching profiles. Conversely matching local unit
flows combine into a global one. Subtract theta_i in each layer and use
(1); minimizing gives (3). This argument retains componentwise constraints
when layers are disconnected.

## 2. A boundary transport bound

For a network N and vertices u,v, let R_N(u,v) be their ordinary effective
resistance: no other vertices or boundary sets are wired together. Put
R_N(u,v)=infinity if u,v lie in different components, and R_N(u,u)=0.
For a nonempty vertex set S define

    diam_N(S)=max_{u,v in S} R_N(u,v).

Let h be supported on S with sum_s h(s)=0, and let Q_N(h) be the least energy
of a flow with divergence h on S and zero elsewhere. Suppose a=diam_N(S)
is finite. Write

    t=TV(h)=(1/2)sum_s |h(s)|.

Then

    Q_N(h) <= a t^2.                                 (4)

Here TV(h) denotes the total positive mass of the zero-sum demand, not a
probability assumption.

Proof. If t=0 take the zero flow. Otherwise write h=h_+-h_-, with each
part of total mass t. Choose any nonnegative coupling pi(u,v) of h_+ to
h_-, for example pi(u,v)=h_+(u)h_-(v)/t. For every pair choose the unit
minimum-energy u-to-v flow f_uv. The flow

    f=sum_{u,v} pi(u,v) f_uv

has divergence h. The triangle inequality for the edge-energy norm gives

    sqrt(E(f)) <= sum_{u,v} pi(u,v)sqrt(R_N(u,v))
               <= t sqrt(a).

Taking the minimum proves (4). A slightly stronger bound follows by
minimizing the first sum over couplings; the diameter bound suffices here.

The coefficient a is optimal: choose a pair u,v attaining the diameter
and take h=t(1_u-1_v). The definition of resistance gives Q_N(h)=t^2 a.
In particular, on a two-vertex boundary every zero-sum demand attains (4).

No terminal sets may be shorted when computing this diameter. Shorting the
boundary itself would give zero diameter, although nonzero redistribution
can cost positive energy. Shorting the opposite terminal set may also
reduce resistance and is not justified by this proof, since every other
vertex must have zero divergence during a repair.

## 3. Two layers: the sharp harmonic coefficient

Let connected networks A,B have disjoint edge sets and common vertex set S.
Take x in A outside S and y in B outside S. Let R_A,R_B be their separately
wired resistances from x to S and S to y. Let q_A,q_B be their optimal
outgoing and incoming profiles on S. Put

    delta=q_A-q_B,
    t=TV(delta),
    a=diam_A(S),  b=diam_B(S).

If S has at least two vertices, a,b>0. Then

    0 <= R_{A union B}(x,y)-R_A-R_B
      <= [ab/(a+b)] t^2.                             (5)

For a singleton S the correction is zero.

Proof. For any common profile q of coordinate sum 1, the least energies
in A and B are respectively

    R_A+Q_A(q-q_A),  R_B+Q_B(q-q_B).

The signs of the first repair demand do not affect its energy. This follows
from (1), and any two fixed-profile minimizers concatenate. Therefore

    D_2=min_{sum q=1}{Q_A(q-q_A)+Q_B(q-q_B)}.          (6)

Choose q=lambda q_A+(1-lambda)q_B. By (4),

    D_2 <= [a(1-lambda)^2+b lambda^2]t^2.

Completing the square gives

    a(1-lambda)^2+b lambda^2
      =(a+b)(lambda-a/(a+b))^2+ab/(a+b).

Set lambda=a/(a+b), proving (5).

For |S|=2 the inequality in (5) is an equality. Indeed write S={u,v} and
q-q_A=z(1_u-1_v), delta=d(1_u-1_v). The objective in (6) is
az^2+b(z+d)^2, whose minimum is ab d^2/(a+b). Here |d|=t.
Thus the coefficient in (5) cannot be reduced universally.

For example take paths x-u and v-y of resistance 1 and paths x-v and u-y
of resistance L. Then a=b=L+1 and

    t=(L-1)/(L+1),
    D_2=(L-1)^2/[2(L+1)].

Independently, each wired half has resistance L/(L+1), while the two global
paths both have resistance L+1 and so give (L+1)/2 in parallel. Subtraction
yields the same D_2. This verifies the earlier planar obstruction and equality
in (5) for every integer L>=1.

## 4. Many layers: a uniform and sharp factor 2

Use the setup of Section 1. For 1<=i<m define

    delta_i=r_i-l_{i+1},  t_i=TV(delta_i),
    a_i=diam_{G_i}(S_i),
    b_i=diam_{G_{i+1}}(S_i),
    k_i=a_i b_i/(a_i+b_i).

Suppose first that all layers are connected and every interface has at
least two vertices. Then

    0 <= D_m <= 2 sum_{i=1}^{m-1} k_i t_i^2.          (7)

Consequently, because the profiles are probability vectors and t_i<=1,

    sum_i R_i <= R_G(x,S_m)
              <= sum_i R_i+2 sum_i k_i.              (8)

For m=2 the factor 2 in (7) can be replaced by 1, as in (5).

Proof. Set lambda_i=a_i/(a_i+b_i). In layer G_i choose a right repair
f_i^R with divergence (1-lambda_i)delta_i on S_i and zero elsewhere.
In layer G_{i+1} choose a left repair f_{i+1}^L with divergence
lambda_i delta_i on S_i and zero elsewhere. By (4) these may be chosen
with

    E(f_i^R) <= a_i(1-lambda_i)^2 t_i^2,
    E(f_{i+1}^L) <= b_i lambda_i^2 t_i^2.             (9)

Let f_1^L=f_m^R=0 and eta_i=f_i^L+f_i^R. Each eta_i belongs to H_i.
The uncorrected total divergence at S_i is -delta_i; the two repairs add
exactly delta_i, so the corrected profiles match. The profile shared by
the two corrected flows is lambda_i r_i+(1-lambda_i)l_{i+1}.

For any two flows f,g on the same edges, positivity of E(f-g) gives

    E(f+g)<=2E(f)+2E(g).

Thus (2), (9), and the completed-square identity in Section 3 imply

    D_m <= sum_i E(eta_i)
        <= 2 sum_i [E(f_i^R)+E(f_{i+1}^L)]
        <= 2 sum_i k_i t_i^2.

At the two end layers only one repair appears, but using the common
factor 2 is valid. When m=2 each layer has only one repair, and no factor
2 is needed. This proves (7) and (8).

Disconnected layers and singleton interfaces. The same proof works whenever
at least one of a_i,b_i is finite at every interface with t_i>0. Use

    k_i=a_i if b_i=infinity and a_i<infinity,
    k_i=b_i if a_i=infinity and b_i<infinity.

Put the entire repair on the finite-diameter side: choose lambda_i=0 in
the first case and lambda_i=1 in the second. No flow needs to be constructed
on the other side. If t_i=0 choose both repairs zero and its summand zero,
regardless of diameters. A singleton interface always has t_i=0. If both
diameters are infinite and t_i>0, this bound gives no finite estimate.
Some such cases still admit finite repairs, since a particular demand
might balance separately in each component; no necessity is asserted.

The factor 2 in (7) is optimal over finite planar unit-resistance networks,
even with three layers and maximum degree 3.

Proof of sharpness. Let L,K be positive integers and construct the layers
from internally disjoint paths with the following endpoints and lengths:

    G_1: x-u=1, x-v=K;
    G_2: u-p=1, v-q=1, p-q=L;
    G_3: p-y=K, q-y=1.

Take S_1={u,v}, S_2={p,q}. Every path has unit-resistance edges. The network
is planar: draw x to the left of u,v, p,q to their right, and y farther
right, with u,p above v,q. Draw p-q vertically and subdivide edges as
specified. Each vertex has degree at most 3.

The outside wired resistances are K/(K+1). In the middle, wiring both
terminal sets leaves two unit edges in parallel; the p-q path has both
ends at sink potential and carries zero current. Consequently

    sum_i R_i=2K/(K+1)+1/2,
    l_2=r_2=(1/2,1/2).

In the orders (u,v) and (p,q), the outside profiles are

    r_1=(K/(K+1),1/(K+1)),
    l_3=(1/(K+1),K/(K+1)).

Both mismatches have total variation t=(K-1)/(2(K+1)). Each layer is a
tree, so resistance within a layer equals the unique path length. The
four diameters are

    a_1=K+1, b_1=L+2, a_2=L, b_2=K+1.

Writing B_L=sum_i k_i t_i^2 gives exactly

    B_L = [(K-1)/(2(K+1))]^2
          *[(K+1)(L+2)/(K+L+3)+(K+1)L/(K+L+1)].     (10)

Set K=L^2 and let L tend to infinity. Division of (10) by L gives
B_L/L -> (1/4)(1+1)=1/2.

The path x-u-p-q-y has length L+3, so R_G(x,y)<=L+3 by using its unit
flow. Contracting the four unit edges x-u,u-p,v-q,q-y reduces resistance and
leaves three parallel routes of resistances L,K,K. To justify the comparison,
project any original unit flow to the contracted graph and discard the
contracted edges; its energy cannot increase. Taking minima proves that
the contracted resistance is a lower bound. Hence

    [1/L+2/K]^(-1) <= R_G(x,y) <= L+3.               (11)

Both sides divided by L tend to 1 when K=L^2, so R_G/L -> 1. Since sum_i R_i
stays bounded, (3) gives D_3/L -> 1. Therefore

    D_3/B_L -> 2.

Every constant below 2 fails for a sufficiently large member of this
family. This proves the stated optimality of the coefficient in (7).

For a second verification of the resistance in (11), let alpha be current
on x-v and let gamma be current on p-y. Conservation determines the other
path currents, and the full unit-flow energy is

    2(1-alpha)^2+(K+1)alpha^2+K gamma^2
       +(1-gamma)^2+L(1-alpha-gamma)^2.

Its unique minimizer solves

    (K+L+3)alpha+L gamma=L+2,
    L alpha+(K+L+1)gamma=L+1.                         (12)

The coefficient matrix has positive diagonal and determinant
(K+L+3)(K+L+1)-L^2>0. Thus (12) gives the unique minimum, and its substituted
energy agrees with the independent full-network Dirichlet calculation in
check_matching.py. The limit argument itself uses only (10) and (11).

## 5. A sufficient shell criterion and its limitation

For a sequence of rooted finite networks stopped at scale 2^m, define

    A_m=sum_i R_i,
    B_m=sum_{i<m} k_i t_i^2.

Use all components of each layer and the finite-side convention above.
Assume for a fixed realization that b>=0 and

    A_m=2^{mb+o(m)},
    B_m<=2^{mb+o(m)}.                                (13)

Equations (3) and (7) give

    A_m<=R_G(x,S_m)<=A_m+2B_m=2^{mb+o(m)}.

Taking logarithms proves rooted resistance exponent b along these scales.
In particular it suffices to have B_m<=2^{o(m)} A_m. The unweighted,
stronger condition sum_i k_i<=2^{o(m)} A_m also suffices by t_i<=1.
A zero B_m is allowed in these upper-bound statements.

This replaces a condition on the abstract matching minimum D_m by a
condition on adjacent boundary profiles and ordinary within-layer
resistance diameters. It is sufficient, not necessary. Both the common
realization and the unshorted diameters matter. The example in Section 4
shows that local repairs in one layer can reinforce on the same edges;
adding their energies with coefficient 1 is invalid.

No estimate in (13) is proved here under an IIC law. In particular, a
geometrically round interface can meet several disconnected shell
components, giving infinite diameters, and even finite diameters need
not have the desired exponent. Bounding them may be harder than bounding
the particular demands. The criterion alone gives no new value or bound
for beta_res.

For critical site percolation on the triangular lattice, Corollaries 1.3–1.4
of Irina Đanković, Maarten Markering, Jason Miller, Yizheng Yuan,
*The scaling limit of random walk and the intrinsic metric on planar critical
percolation*, [arXiv:2604.14122](https://arxiv.org/abs/2604.14122), identify the
rooted resistance exponent and give

    d_w=91/48+beta_res,
    d_s=2(91/48)/(91/48+beta_res).

Thus d_s=4/3 is equivalent to beta_res=91/96, and beta_res>91/96 would give
d_s<4/3. Neither alternative is established by the deterministic estimates.
