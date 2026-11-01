# Root independent audit of the all-graph high-fugacity argument

Research checkpoint, 2 October 2026. I read the entire assembled
`ALL_GRAPH_HIGH_FUGACITY_INDUCTION_DRAFT.md`, the complete H2 and H3 proofs,
and the separate induction, closure and K transfer audits. This note records
an analytic audit, independently reconstructed below. It does not certify
historical priority or replace external mathematical review.

## Verdict and exact scope

The induction passes this internal analytic audit, subject to the explicit
local-score invariant in the full proof. For every fixed finite weighted
loopless graph and distinct marked edges, its conclusion is a nonnegative
Rayleigh difference for all sufficiently large common scale lambda. A pair
on a common cycle has a strictly positive first surviving coefficient;
edges in different graphic-matroid components are exactly independent.
No sign at an arbitrary fixed positive lambda follows from this argument.

## 1. Normalize before expanding

For connected G, put Z(lambda c)=lambda^(n-1) tau F(1/lambda). Derivatives
of Z on the left are activity derivatives; those of tau and F on the right
are conductance derivatives. Hence

    R_ef(lambda c)=-lambda^(2n-4) tau^2 F(t)^2
                    partial_ef(log tau+log F(t)), t=1/lambda.

The factor lambda^(-2) from the two marked derivatives is necessary. If all
earlier coefficients of the mixed logarithmic derivative vanish, multiplication
by F(t)^2, whose constant is one, leaves the first surviving coefficient
unchanged. There is no extra c_e c_f factor in this coefficient; that factor
belongs to the edge covariance formula instead.

The grounded Grassmann identity for F has a direct all-orders feature proof:
each non-root forest component chooses a vertex with sign plus or an edge
with sign minus; removing selected edges gives the principal-minor rooted
forest. Its total feature multiplicity is |V(component)|-|E(component)|=1.
The root component is already rooted and supplies no feature. This verifies
F(t)=<exp(t[sum q_x-sum c_xy q_x q_y])> at every order, not just order three.

## 2. The scalar invariant prevents hidden lower-order products

At level ell the exact local marked scores have the form

    U_e=C_e(t)+t^ell Q_Be+t^(ell+1)P_e+O(t^(ell+2)),
    U_f=C_f(t)+t^ell Q_Bf+t^(ell+1)P_f+O(t^(ell+2)).

Each coefficient in C is an actual boundary-field scalar. The local Gaussian
Schur complements and harmonic rows are fixed under either mark: the
physical original current has compact support in its interior and the
endpoint harmonic rows agree. With separated interiors, only the e local
factor depends on e and only the f local factor on f. Thus the mixed
derivative is exactly the tilted boundary covariance of these scores.
Covariance removes every scalar at every order. This is stronger than merely
knowing that a finite list of global coefficients vanishes.

The order 2ell term is -tr(T Be T Bf), a nonpositive square sum. If zero,
every pair of Gram source charges is Green-orthogonal. At order 2ell+1,
the only terms are Cov(P_e,Q_Bf), Cov(Q_Be,P_f), and the triple cumulant
of Q_Be,Q_Bf with the first tilt. There is no ell-dependent multiplier.
The H3 calculation is therefore reusable algebraically at arbitrary ell.
The translation-invariant part of P has zero rank-one derivative when the
opposite response potential is constant on its ports. The remaining Ward
part supplies exactly the constant-mode correction. Discrete integration
by parts completes it with the unshifted wedge energy to the shifted
nonnegative wedge square. I independently checked these signs in the
earlier H3 root derivation.

## 3. Reconstruct the transfer, including higher-degree terms

Use free intrinsic local ports before grounding. For symmetric B with B1=0,
the next Ward equations have the particular solution

    P_B=sum_(a<b) B_ab q_a q_b.

With left derivatives, d_psi q=-barpsi and d_barpsi q=psi. Direct
differentiation verifies both equations. Thus P=P_B+R, where R is invariant
under both ordinary uniform odd translations; no restriction on its degree
is assumed.

After absorbing the supports of the shifted physical response potentials,
all old port harmonic rows equal one row pi. Successive normalized Gaussian
conditioning gives U_new=E_tilt[U_old] exactly, because the intervening Schur
law and its determinant normalization are mark-independent. Consequently
all earlier scalar coefficients remain scalar. At the next order the only
possible nonconstant term is E_0[P]+Cov_0(Q_B,W_1).

Substitute old port fields chi_a+h with the same h=pi psi_new. B1=0 makes
Q_B a pure fluctuation bilinear. Uniform-translation invariance makes R
independent of h, even when it has degree six or higher. The Ward particular
solution contracts to -tr(C_AA B) q(h), with its uncontracted quartic zero.
A bilinear first tilt contributes only a scalar covariance. For a quartic
q_x q_y, rank-one covariance variation -a_x a_y gives the boundary bilinear
-Q_(a_x p_y-a_y p_x). Its negative physical edge coefficient therefore gives
the positive raw boundary Gram. Fully uncontracted quartics do not depend on
the covariance and have zero variation. Thus no new higher-degree boundary
term survives at this order.

For a source rho, La=rho and a is zero outside the enlarged interior. For
new harmonic h, h is constant k=pi z on old source ports. The flow
j_xy=c_xy(a_x h_y-a_y h_x) has divergence k rho, while the electrical
flow i_xy=c_xy(a_x-a_y) has divergence rho. Therefore

    <j,i>_energy=k rho^T a=k R_rho,
    ||j||^2-k^2 R_rho=||j-k i||^2.

This is exactly the Ward subtraction, so the next leading coefficient is
the PSD response Gram of a_x p_y-a_y p_x-(a_x-a_y)pi. It advances the first
nonconstant score from ell to ell+1. The next Ward identity remains exact.

## 4. Closure, boundary endpoints and termination

The new Gram's kernel consists exactly of functions constant on all its
geometric ports. For a zero-energy boundary function put k=h-pi z. On every
nonzero response-support component the vanishing wedge makes k/a constant.
Every such component meets an old source port, by the maximum principle;
there k=0. This proves k=0 on the support. A new port adjoining the added
support is forced zero by its joining edge. A port adjoining only dormant
old interior was already an old port and is zero there as well. This last
case is essential. The range is the complete new contrast space, regardless
of the signs of off-diagonal entries of the Gram.

At the initial equality decomposition, if an original marked endpoint has
zero potential and lies on the interface, its harmonic row is an identity
row. The other endpoint in the connected current-support region has the
same row. Harmonic exit probabilities from that interior vertex are strictly
positive at every geometric port, since every such port is reachable through
the connected interior. The geometric port set is consequently the singleton
zero-potential endpoint. The full one-port Ward identity makes the complete
score scalar, equivalently forest weights factor at that cut vertex. This
handles boundary endpoints before imposing the continuing invariant that
both marked endpoints lie in the interior.

For a nonzero contrast family at least one source port has nonzero response
potential. Otherwise the maximum principle forces every potential zero,
contradicting its nonzero source. Each zero-trace, zero-wedge continuing
step therefore strictly enlarges both interiors. The aggregate supports are
disjoint with no joining edge by the projective-direction maximum principle.
Union with the old interiors preserves this separation, compact original
currents, and connectivity. The separator remains nonempty. A finite graph
cannot continue indefinitely. A singleton port gives exact all-orders
factorization, and cannot separate two edges on a common simple cycle.
The only other termination is a strictly positive trace or wedge coefficient.

## 5. Exact checks and literature boundary

I reran the independent Fraction exterior-algebra local-score checker:
all five cases passed, with delayed orders 1,2,2,3,3 and leading eigenvalues
1/8,1/128,1/512,1/2048,1/51200. I also reran the complete forest-frontier
iteration checker; all four cases passed, including H4/H5/H6 chains and a
14-vertex asymmetric three-port H4 case whose response is not an M-matrix.
These checks corroborate normalization and powers; the general proof rests
on the preceding analytic identities.

The primary forest/Grassmann formula is classical (Caracciolo et al.,
arXiv:cond-mat/0403271, revised 4 September 2004, formula (13)); the grounded
variant above is proved explicitly. Huang, arXiv:2311.00965 (2 November
2023), Theorems 2.1 and 2.2, proves adjacent-edge and complete-graph parameter
regimes. The current full primary arXiv:2610.00549v1, checked 2 October 2026,
Theorem 1.5 and Corollary 1.7, covers the first two forest Rayleigh
coefficients and leaves their simultaneous-zero case. Its Section 6.1
connectivity covariance result is a different observable and does not by
itself settle negative edge correlation. This induction explicitly treats
arbitrarily long leading-zero strings. Priority remains unverified; a bounded
search and internal audits are not a literature-completeness certificate.
