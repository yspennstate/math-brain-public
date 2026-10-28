SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T17:30:34Z.
attacking: the exact diagonal-plus-rank-two survivor from the latest account02/B13 max-volume skeleton, via a Schur-volume DPP disjointness identity and the unconditional pair-volume half-Riesz receiver.

# account01/B13 — Schur rank-two volume disjointness and exact star/triangle endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.

Run: `20260923T173034Z-account01-B13-qform-auto11`.

Status: **PROVED SUPPORTING TARGET-LEVEL IMPLICATION / FULL QFORM OPEN / FULL CONTINUITY OPEN / WITHOUT_VERIFIED_BRAIN**.

MODEL: GPT-5.6 Sol (self-report).

THINKING LEVEL: UNKNOWN; source=not_exposed; requested=maximum actually supported.

THINKING USAGE: reasoning tokens NOT_EXPOSED; provider thinking time NOT_EXPOSED; coverage=unavailable.

All random variables below remain ORIGINAL independent coordinates. Deterministic whitening is used only on coefficient matrices and exterior-volume identities; no rotated random variables are declared independent. No support, moment, centering, interval, bounded-diameter, fixed-fragment, or log-concavity assumption is used.

## 1. Fresh control and source-pinned inputs


### 1.1 Latest designated partner account02/B13

Completed source actually applied:

`yspennstate/math-open-problems@eeabf558e96ea803514f8e438b49c18fe9ee789a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T171027Z-account02-B13-rank2core/REPORT.md`.

The partner's maximum-volume hierarchy defines

`Delta=max{|det A[P,Q]|: |P|=|Q|=2, P cap Q=empty}`.

In its exact endpoint `Delta=0`, the source-valid zero-minor structure gives

`A=D+R,    D diagonal,    rank(R)<=2`.                              (1.1)

This is the branch treated below. The partner's nonzero-Delta branch remains the explicit at-most-four-hub rank-at-most-four skeleton plus a retained max-norm twist; I do not delete that twist perturbatively.

### 1.2 Unconditional pair-volume half-Riesz theorem

Source:

`yspennstate/math-open-problems@55255bcb25271145aa9f5a1a93a0cc84ad8e1c3d`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T030821Z-account01-B01-qform-auto11/REPORT.md`.

For any quadratic form `R0` on independent cap-one ORIGINAL coordinates and any disjoint physical cross block `M` with

`E2=e_2(M^T M)>0`,                                                  (1.2)

the completed theorem gives

`sup_s E |R0-s|^(-1/2) <= C_E2 E2^(-1/8),`                         (1.3)

with

`C_E2 <= 12*2^(5/6)*e^(5/24) = 26.3340461808... .`                (1.4)

There is no leverage gate in (1.3), and arbitrary same-side curvature is retained.

### 1.3 Exact extremal-product purification

Source:

`yspennstate/math-open-problems@d9f6bcd057b7804ea7ba06fea8dad5f54e357990`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260923T121154Z-account04-B13-nonattained-bathtub-r1/REPORT.md`.

For every nonnegative measurable kernel `K`,

`sup_(0<=f_i<=1, int f_i=1) int K prod_i f_i
 = sup_(|E_i|=1) int_(prod E_i) K`.                                (1.5)

No optimizer, interval, center, diameter or uniform fragment count is asserted.

## 2. Exact Schur normalization inside the partner's rank-two endpoint

Assume the genuine rank-two case of (1.1):

`R=U Lambda U^T`,                                                  (2.1)

where `U` is `n x 2`, `U^T U=I_2`, and `Lambda` is invertible symmetric `2 x 2`.

Fix one ORIGINAL coordinate `z`. Write its row of `U` as `u^T`, and put

`c=||u||^2`, `d=D_zz`, `a=A_zz=d+u^T Lambda u`.                    (2.2)

Assume for the moment

`a!=0`, `d!=0`, `c<1`.                                             (2.3)

Let `S` be the genuine scalar Schur complement after pivoting coordinate `z`:

`S=A[-z,-z]-a^(-1)A[-z,z]A[z,-z]`.                                (2.4)

Since `D` is diagonal,

`S=D_- + U_- M U_-^T`,                                            (2.5)

where

`M=Lambda-a^(-1)Lambda u u^T Lambda`.                              (2.6)

Put

`G=U_-^T U_-=I_2-u u^T`,                                          (2.7)

which is positive definite by `c<1`, and define

`W=U_- G^(-1/2)`, `N=G^(1/2) M G^(1/2)`.                          (2.8)

Then

`W^T W=I_2`,                                                       (2.9)

and the Schur residual has the exact normalized form

`boxed: S=D_-+W N W^T.`                                           (2.10)

The determinant transport is exact. By the matrix determinant lemma,

`det M = det Lambda * (1-u^T Lambda u/a)
       = det Lambda * d/a`,                                       (2.11)

while

`det G=1-c`.                                                       (2.12)

Therefore

`boxed: det N=(1-c)d det(Lambda)/a.`                               (2.13)

This identity is algebraic and uses only the ORIGINAL scalar pivot `z`.

## 3. Rank-two physical volume law and its disjointness parameter

For every physical two-set `H` in `-z`, define

`q_H=det(W_H)^2`.                                                   (3.1)

Cauchy--Binet and (2.9) give

`sum_(|H|=2) q_H=1`,                                               (3.2)

so `q` is a probability law on physical pairs. Let `H,K` be independent draws from this law and define

`delta_z=P(H cap K=empty)
       =sum_(H cap K=empty)q_H q_K`.                               (3.3)

This quantity is deterministic coefficient geometry, not a random-coordinate rotation.

The one-point marginal of this rank-two volume law is

`ell_i=P(i in H)=||w_i||^2`,                                       (3.4)

and for `q_ij=det(w_i,w_j)^2` one has the exact collision identity

`boxed:
 delta_z
 =1-sum_i ell_i^2+sum_(i<j) q_ij^2.
}`                                                                  (3.5)

Indeed, for two two-sets the intersection size is zero, one or two; its expectation is `sum_i ell_i^2`, while probability of intersection size two is `P(H=K)=sum q_H^2`.

The normalized quantities can also be written before whitening:

`ell_i=u_i^T(I-u u^T)^(-1)u_i
       =||u_i||^2+(u_i.u)^2/(1-c)`,                                (3.6)

and

`q_ij=det(U_{ij})^2/(1-c)`.                                        (3.7)

Thus `delta_z` is an explicitly computable normalized disjoint second-exterior volume.

## 4. A random physical cut captures exactly delta_z/16 of the rank-two pair volume

Partition the ORIGINAL coordinates in `-z` independently red/blue with probability `1/2`, obtaining a deterministic realization `I sqcup J=-z`. Put

`P_I=W_I^T W_I`, `P_J=W_J^T W_J=I_2-P_I`.                         (4.1)

By Cauchy--Binet,

`det P_I=sum_(H subset I, |H|=2) q_H`,                             (4.2)

and similarly for `J`. Therefore

`E_partition[det P_I det P_J]
 = (1/16) sum_(H cap K=empty)q_H q_K
 = delta_z/16`.                                                     (4.3)

Hence some ORIGINAL-coordinate partition satisfies

`boxed: det P_I det P_J >= delta_z/16.`                            (4.4)

Now use (2.10). Since `D_-` is diagonal and `I,J` are disjoint, the physical cross block of the Schur residual is

`B=S[I,J]=W_I N W_J^T`.                                            (4.5)

Its complete pair exterior energy is exactly

`E2(B)=e_2(B^T B)
     =det(N)^2 det(P_I)det(P_J)`.                                  (4.6)

The quickest proof is to take second exterior powers: `wedge^2 N` is scalar multiplication by `det N`, and the squared Hilbert--Schmidt norms of `wedge^2 W_I` and `wedge^2 W_J` are `det P_I` and `det P_J`.

Combining (4.4)-(4.6),

`boxed:
 E2(B) >= (delta_z/16) |det N|^2.
}`                                                                  (4.7)

This is aggregate-before-inversion: no tiny physical pair is selected.

## 5. Main theorem — leverage-free Schur-DPP density certificate

### Theorem 5.1 — `QFORM-RANK2-SCHUR-DPP-DISJOINTNESS-v1`

Under (2.1)-(2.3), for arbitrary independent cap-one input laws,

`boxed:
 ||p_(X^T A X)||_infinity
 <= sqrt(2) C_E2 delta_z^(-1/8)
    [(1-c)|a d det Lambda|]^(-1/4).
}`                                                                  (5.1)

Numerically,

`sqrt(2) C_E2 <=37.2419652611.`                                    (5.2)

No leverage upper bound is required. In particular (5.1) still applies in heavy-leverage regimes excluded from the diffuse rank-two Brascamp--Lieb route, provided only that `delta_z>0`.

### Proof

Complete the square only in the ORIGINAL coordinate `X_z`:

`X^T A X
 =a (X_z+a^(-1)A[z,-z]X_-z)^2 + X_-z^T S X_-z`.                 (5.3)

The translation-uniform scalar-square shell inequality gives, for every output interval `J`,

`P{X^TAX in J}
 <= |J| |a|^(-1/2)
    sup_s E|X_-z^T S X_-z-s|^(-1/2).`                              (5.4)

Use the physical cut from Section 4 in the unconditional pair-volume half-Riesz theorem (1.3):

`sup_s E|X_-z^T S X_-z-s|^(-1/2)
 <=C_E2 E2(B)^(-1/8)
 <=C_E2 (16/delta_z)^(1/8)|det N|^(-1/4).`                         (5.5)

Since `16^(1/8)=sqrt(2)` and (2.13) holds,

`|a|^(-1/2)|det N|^(-1/4)
 =[(1-c)|a d det Lambda|]^(-1/4).`                                 (5.6)

Substitute into (5.4), then use interval domination to obtain (5.1). QED.

A slab witness of ratio

`rho=P{X^TAX in J}/|J|`                                            (5.7)

therefore necessarily satisfies the actual inequality

`boxed:
 delta_z [(1-c)|a d det Lambda|]^2
 <= (sqrt(2) C_E2/rho)^8.
}`                                                                  (5.8)

This is the most useful high-density form of the theorem.

## 6. Exact zero-disjointness endpoint = star or triangle

The case `delta_z=0` is not left as an unspecified leverage failure.

Let `G_q` be the graph whose vertices are physical coordinates in `-z` and whose edges are exactly the pairs `H` with `q_H>0`, equivalently the pairs of nonparallel nonzero rows of `W`. Since `delta_z=0`, no two positive-mass edges are disjoint: `G_q` has matching number one.

### Lemma 6.1 — `QFORM-RANK2-INTERSECTING-BASES-CLASSIFICATION-v1`

Every such graph is either

1. a star: every positive edge contains one common physical coordinate `h`; or
2. a triangle on exactly three vertices.

Proof: choose an edge `{a,b}`. If every edge contains `a`, it is a star. Otherwise an edge not containing `a` must be `{b,c}`. If every edge contains `b`, it is a star. Otherwise an edge not containing `b` must intersect both previous edges and hence is `{a,c}`. Any further edge meeting all three edges `{a,b},{b,c},{a,c}` is one of those three. QED.

For a rank-two frame this graph classification has an exact coefficient interpretation:

- in the star case, all non-center nonzero rows of `W` are mutually parallel; the rank-two geometry is one physical coloop plus one parallel family;
- in the triangle case, every row outside those three physical coordinates is zero. Indeed any fourth nonzero row is nonparallel to at least two of the three pairwise nonparallel triangle rows and would create an edge disjoint from the opposite triangle edge.

Thus the previously vague heavy-leverage endpoint becomes the explicit finite-center alternative

`boxed: delta_z=0 => one-coloop star OR three-coordinate rank-two support.`       (6.1)

The quantitative near-zero stability of this star/triangle classification remains unpaid.

## 7. Actual application of the latest account02/B13 result

Apply the latest partner theorem in its exact `Delta=0` branch (1.1). If `rank R=2`, normalize it as (2.1). The target spectral hypothesis gives an additional exact resource:

`boxed: s_3(A)<=||D||_op=max_i |d_i|.`                             (7.1)

This is the standard singular-value rank-perturbation inequality because `rank R<=2`. Since the target has `s_3(A)>=1`,

`boxed: max_i |d_i|>=1.`                                           (7.2)

Hence a hypothetical high-ratio witness in the partner's exact rank-two endpoint has at least one physical decomposition coordinate `z` with `|d_z|>=1`. For every such `z` satisfying `a_z!=0` and `c_z<1`, (5.8) gives

`boxed:
 delta_z [(1-c_z)|a_z det Lambda|]^2
 <= (sqrt(2) C_E2/rho)^8,
}`                                                                  (7.3)

where the factor `|d_z|>=1` was dropped only to weaken the left side.

Consequently a counterexample sequence with `rho->infinity` cannot remain a generic diagonal-plus-rank-two matrix. Along every nondegenerate large-`|d_z|` pivot it must force at least one of

- `delta_z->0`, i.e. the leave-one-out rank-two volume law approaches an intersecting star/triangle configuration;
- `(1-c_z)|a_z det Lambda|->0`;
- the exact degeneracies `a_z=0` or `c_z=1`;
- or `rank R<2`.

When `c_z=1`, `U_-^T U_-=I-u_zu_z^T` has rank one, so one latent rank-two direction is already completely localized at the physical coordinate `z`; this is itself a coloop-type finite-center degeneration, not a diffuse survivor.

This is a real application of the designated partner result at an inequality, not only a restatement of its theorem.

## 8. Extremal-product geometric form

By the exact positive-kernel purification (1.5), Theorem 5.1 is equivalent with zero constant loss to the geometric slab estimate for arbitrary measurable unit-measure sets `|E_i|=1`:

`boxed:
 |{x in prod_i E_i: x^T A x in J}|
 <= sqrt(2) C_E2 delta_z^(-1/8)
    [(1-c)|a d det Lambda|]^(-1/4) |J|.
}`                                                                  (8.1)

No set `E_i` is assumed to be an interval, centered, bounded in diameter, or a union of a bounded number of fragments. The same purification also applies to the half-Riesz kernel after truncation.

## 9. Finite diagnostic scope

I numerically checked, on 100 independent random orthonormal two-frames and random invertible symmetric diagonal `Lambda`, the two new exact algebraic identities

`det N=(1-c)d det Lambda/a`                                        (9.1)

and

`delta_z=1-sum ell_i^2+sum q_H^2`.                                (9.2)

The largest relative/algebraic errors were respectively `3.50e-15` and `2.83e-15`. A separate exhaustive partition check on 100 random frames verified

`E_partition[det P_I det P_J]=delta_z/16`                          (9.3)

with maximum absolute error `4.52e-17`. These computations are only sanity checks; Sections 2-6 are the proofs.

## 10. What remains unpaid

The sharpened first unpaid implication for this branch is

`QFORM-RANK2-NEAR-INTERSECTING-STARTRIANGLE-GLUE-v1`:

> Prove a quantitative stability/routing theorem for small `delta_z`: either extract a physical coloop/star or three-coordinate packet carrying the rank-two currency at target scale, or route the residual to an already-paid scalar/pair/grouped-bank receiver. Simultaneously handle the exact `a_z=0`, `rank R<2`, and small `|det Lambda|` degeneracies without perturbatively deleting any diagonal or max-norm residual.

For the partner's `Delta>0` branch, its retained max-norm twist remains a genuine quadratic term and is not addressed by the theorem above. The full arbitrary-matrix conjecture therefore remains OPEN.

## 11. Operational note

An early immutable checkpoint was successfully written to this run folder. The required actual-hour login write to the math-research-brain status path was attempted at the beginning of the run but the connector blocked that specific write before any commit; no login success is claimed. Repository transport is not native brain ingestion, so execution remains `WITHOUT_VERIFIED_BRAIN`. No scheduler mutation, new task, email/push, public release, paid call, cross-account authentication, or permission expansion was performed.
