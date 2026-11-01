# Full affine child release in the original influence account

Uniform finite Boolean signs; Fourier entropy H in bits; I is total
influence. All finite minima below include the identity map. No optimizer
over unbounded dimension is used. Write

    a(g)=min {I(g transformed by an invertible affine spectral map)}.

Such a map is a linear change of input variables and multiplication by a
character. It preserves Booleanity and H. A minimum exists in the finite
orbit (including dimension zero). The earlier affine-basis theorem
computes it by a cheapest independent parity basis with majority centering.

## 1. Directional perturbation and a quantitative release bound

Let f be AFFINE-INFLUENCE MINIMAL in its current physical coordinates.
Put p_i=Inf_i(f), and w(v)=P[f(X)!=f(X+v)] for a physical translation
direction v. This equals P[v dot S=1] for its squared Fourier law.
For v_i=0 let w_b(v) be the same directional influence in the actual
child f|X_i=b. Then

    (w_0(v)+w_1(v))/2=w(v),
    |w_b(v)-w(v)|<=p_i.                                      (1)

To prove the second assertion, write d_v(x)=1[f(x)!=f(x+v)].
The absolute difference of d_v(x) and d_v(x+e_i) is at most
d_ei(x)+d_ei(x+v). Average over the two i-fibers; because v_i=0,
this gives |w_0-w_1|<=2p_i. No independence of spectral bits is used.
As t -> min(t,1-t) is 1-Lipschitz, child minority parity costs satisfy

    m_b(v)>=m(v)-p_i>=max_{j:v_j=1}(p_j-p_i).

Nonnegativity improves the right side to max_{j:v_j=1}(p_j-p_i)_+.
For every child parity basis, threshold rank counting (as in the earlier
minimum-basis proof) now gives

    a(f|X_i=b)>=sum_{j!=i}(p_j-p_i)_+.

Define its expected FULL affine release

    rho_i=E_b[I(f|X_i=b)-a(f|X_i=b)].

Since E I(child)=sum_{j!=i}p_j, we obtain the all-dimensional bound

    0<=rho_i<=sum_{j!=i}min(p_j,p_i).                         (2)

The coefficient one is sharp: the two-bit point defect has p_1=p_2=1/2;
one child is constant and one a literal. Their affine minima are both
zero, so rho_i=1/2. The affine-minimal-parent hypothesis matters: query
a dummy coordinate of a two-bit parity padded to three bits. Then p_i=0
but rho_i=2, contradicting (2) without that hypothesis. Constants,
zero p_i, rank-zero children, and tied bases are included.

There is an explicit near-extremal version. If I(f)<=a(f)+delta,
delta>=0, each one-row comparison gives m(v)>=p_j-delta whenever v_j=1.
The same threshold-rank proof therefore yields

    rho_i<=sum_{j!=i}min(p_j,p_i+delta).                    (2a)

An epsilon-near finite D_K maximum has delta<=epsilon/K for K>0:
the best affine orbit point preserves H and its possible gain in D_K
is K[I(f)-a(f)]<=epsilon. Thus (2a) has a concrete epsilon/K tolerance,
not an unquantified stationarity assumption. It applies also when the
parent is only affine-orbit near-minimal. At K=0 no such division or
forced orbit minimality is asserted.

## 2. Complete child banks and the all-block critical budget

For a nonempty physical block A, set

    I_A=sum_{i in A}p_i,
    L_A=H(f)-E_u H(f|X_A=u),
    rho_A=E_u[I(child)-a(child)],
    S_A^*=E_u[K a(child)-H(child)],
    S_A=E_u[K I(child)-H(child)], D=H(f)-K I(f).

The exact same-bank identities are

    S_A=S_A^*+K rho_A,
    D+S_A^*=L_A-K(I_A+rho_A).                               (3)

No branch is removed. Each child entropy in (3) is its original complete
entropy; all phase/mixed-refund interactions remain inside exact L_A.

Now assume f is a LEAST-ESSENTIAL-DIMENSION positive K-violation, K>0.
Every transformed proper child is an actual smaller Boolean function,
so S_A^*>=0 for proper A. This uses nonviolation of ALL smaller Boolean
functions, not merely the unoptimized displayed children. For A equal
to all coordinates the children are constants and S_A^*=rho_A=0.

Let 1<=k<=n, M=binomial(n,k), t=binomial(n-1,k-1). Define

    B_A=H(S_A | S_Ac),
    J_A=L_A-B_A,
    T_k=t H(f)-sum_{|A|=k}B_A.

Here S inside B_A denotes the random Fourier set, not a child reserve.
For any law on subsets, T_k>=0: expand each conditional entropy in the
same coordinate order. Each summand conditions on all earlier coordinates
and possibly more, hence is at most H(S_i|S_<i). Each coordinate occurs
in exactly t blocks; summation proves the bound, including k=n.

Summing (3) gives the EXACT account

    T_k+(M-t)D+sum_A S_A^*+K sum_A rho_A = sum_A J_A.        (4)

The established finite-cube log-Sobolev channel inequality is
J_A<=kappa I_A, kappa=2/ln2 (B11 lead R1; conditional majority gives a
stronger version). Its direct interpretation is
J_A=sum_T Ent_u(w_T(u)^2), where w_T are the actual child Fourier rows;
log-Sobolev on the queried cube gives kappa sum_{U,T}|U| fhat(U,T)^2.
Thus sum_A J_A<=kappa t I(f). In particular a genuine critical source obeys

    K sum_{|A|=k}rho_A+(M-t)D <= kappa t I(f).               (5)

For k=1 this reads K sum_i rho_i+(n-1)D<=kappa I. For k=2,
K sum_pairs rho_pair+[(n-1)(n-2)/2]D<=kappa(n-1)I.
These are upper budgets on a POSSIBLE release, not a lower funding bound
for a prescribed pair. If n<2 no pair assertion is made. No division by
K, I, or n-k is required in (4)--(5). At a canonical finite maximal
critical witness, both (2) and (5) apply. Character-only release may
vanish at high K, while (4) still retains full affine basis release.

## 3. Adaptive trees: a reset spends influence exactly once

Consider a finite adaptive tree. At a node g in its CURRENT physical
coordinate chart, query a nonempty block A; on each branch apply any
entropy-preserving affine transform with I(g'_u)<=I(g_u). This may be a
full minimum but need not be. Define r_v=E_u[I(g_u)-I(g'_u)]>=0 and
q_v=I_A(g). Let w_v be the original probability of reaching the node.
Use the transformed children for all later queries. Direct telescoping,
with every original branch reach retained, gives

    sum_v w_v(q_v+r_v)=I(root)-E I(leaves),
    sum_v w_v L_v=H(root)-E H(leaves).                      (6)

Indeed the first one-node identity is I(g)=q_v+r_v+E I(g'_u);
the second holds since the resets preserve each child entropy. There is
no multiplication of conditional estimates and no claimed common global
linear chart after different branches reset. Finite dimension decreases
at every query; all required orbit choices are finite.

Consequently any such tree with leaves satisfying H<=K I and actual
local L_v<=K(q_v+r_v) proves H(root)<=K I(root). The global signed bank is

    K I(root)-H(root)
      =E[K I(leaf)-H(leaf)]+sum_v w_v[K(q_v+r_v)-L_v].       (7)

A previously booked reset is part of r_v and cannot be reused at a later
node. Changed directions in a descendant belong to that descendant's
actual chart. This proves the ownership and telescope, not existence of
a uniformly paid tree. For nonconstant roots a singleton tree terminates
in constants, so a complete finite construction can always be evaluated;
whether its signed bills are paid at a dimension-independent K is OPEN.

The two-bit point defect shows a real prescribed-query gain: L_i=2,
q_i=1/2, rho_i=1/2. The physical-only price is4; query plus affine child
reset has price2. Both reset leaves are constants. This pays H=2 at
the SAME original I=1, not an added influence resource. The root is a
genuine least-dimension maximal positive witness at K=1; at K=2 it is
on the sharp finite FEI boundary, not a positive violation.

## 4. Exact obstruction and next unpaid line

The A052 path spectrum and A055 rare tensor extensions are full-span
affine minima but fail smaller-child eligibility; in the hidden data
direction L_i=0 and D+S_i=-K p_i<0. Neither S_i nor S_i^* can be replaced
by a nonnegative critical reserve there. This new budget does not admit
those arbitrary cores or remove A055's mixed entropy refund T.

FIRST UNSUPPORTED LINE: select an ORIGINAL proper physical pair A on
every genuine critical source for which L_A<=K(I_A+rho_A), or derive
another signed comparison that exhausts the SAME unused S_A^* bank.
Equations (2),(5) upper-bound release and (6) prevents double spending;
none provides the missing lower bound or a uniformly paid selection.

## 5. Verification scope

Analytic proof, with the already established channel log-Sobolev
inequality as the one external mathematical premise. Independent review
is pending. Checks target the Fourier/physical translation identity,
the factor2 in (1), full affine minima (including zero rank), critical
admission, exact entropy-bank coefficients and all adaptive reaches.
The frozen finite checker uses every truth table through3bits; full
orbit minima independently check the greedy parity basis. Named point2
and dummy-parity negative controls test sharpness and the essential
hypothesis. Exact entropy expressions and rational logarithm enclosures
are used wherever a sign, rather than an identity, is needed.
