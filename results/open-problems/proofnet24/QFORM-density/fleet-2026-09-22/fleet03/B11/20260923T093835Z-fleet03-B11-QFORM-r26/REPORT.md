# fleet03/B11 r26 — balanced near-rank-one chamber cannot be closed by any fixed-size packet

Status: `PROVED_STRUCTURAL_OBSTRUCTION / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

## Target and scope

The full conjecture remains open. This report addresses the B11 indefinite-signature survivor after the already-paid opposite-sign-pair, sign-frustrated-triangle, localized-block, and fixed-packet branches. It gives an explicit target-valid family showing that **no fixed number of original coordinates can carry a uniform-scale second/third direction** in the balanced near-rank-one chamber, even when all physical diagonals are exactly one and every physical pair is positive semidefinite.

This rules out the proposed next step “extract a fixed-scale eight-coordinate packet” as a universal structural closure. The correct next mechanism must aggregate a number of original coordinates that can grow as the normalized edge defect shrinks.

## The family

Let `n` be divisible by 4. Choose vectors `u,v in {+1,-1}^n` so that

- `<u,1>=<v,1>=0`,
- `<u,v>=0`,
- each of the four sign pairs `(u_i,v_i)` occurs exactly `n/4` times.

For `0<delta<1/4`, define

`A=(1-2 delta) J + delta v v^T - delta u u^T + 2 delta I`,

where `J=11^T`.

The four vectors/subspaces `span{1}`, `span{v}`, `span{u}`, and `{1,u,v}^perp` are mutually orthogonal and invariant. Hence the spectrum is exactly

- `lambda_1=(1-2 delta)n+2 delta`, on `1`;
- `lambda_v=delta n+2 delta`, on `v`;
- `lambda_u=-delta n+2 delta=-delta(n-2)`, on `u`;
- `lambda_perp=2 delta`, with multiplicity `n-3`.

Taking `delta=n^{-1/2}` and `n>=16` gives one negative eigenvalue of magnitude at least 1 and at least two positive eigenvalues of magnitude at least 1. Thus this is a genuine target family of signature containing a macroscopic `(+,+,-)` core.

## Every physical pair is PSD and the sign pattern is balanced

For every coordinate `i`,

`A_ii=(1-2delta)+delta-delta+2delta=1`.

For `i!=j`, write `a=u_i u_j` and `b=v_i v_j`, each in `{+1,-1}`. Then

`A_ij=(1-2delta)+delta b-delta a`,

so the only possible off-diagonal values are

`1`, `1-2delta`, `1-4delta`.

Therefore `0<A_ij<=1` for `delta<1/4`, and every physical 2x2 principal block is

`[[1,rho],[rho,1]]`, `0<rho<=1`,

hence PSD. All edge signs are positive, so every triangle sign product is `+1`: the sign-frustrated branch is absent.

Moreover

`1-rho^2 <= 1-(1-4delta)^2 = 8delta-16delta^2 <= 8delta`.

For `delta<=1/128`, every pair defect is at most `1/16`, so the coarse definite-pair defect exit used in the preceding B11 packet theorem is also absent.

## No fixed-size original-coordinate packet sees the large spectral directions

Let `S` be any set of `k` original coordinates. Since `J_S` has rank one and every entry of `A_S-J_S` has absolute value at most `4delta`,

`||A_S-J_S||_op <= ||A_S-J_S||_F <= 4delta k`.

By the singular-value perturbation inequality, for every `j>=2`,

`s_j(A_S) <= 4delta k`.

Consequently, for every fixed `K`,

`max_{|S|<=K} s_2(A_S) <= 4K delta`,
`max_{|S|<=K} s_3(A_S) <= 4K delta`.

In particular these quantities tend to zero when `delta=n^{-1/2}` and `n->infinity`.

The same statement holds for fixed-size cross blocks. For disjoint row and column sets `P,Q`, the all-ones matrix `J_{P,Q}` has rank one and

`||A_{P,Q}-J_{P,Q}||_op <= 4delta sqrt(|P||Q|)`.

Thus

`s_2(A_{P,Q}) <= 4delta sqrt(|P||Q|)`

(and similarly `s_3`). For the eight-coordinate packet from r23, every 2x2 child cross block therefore satisfies

`s_2 <= 8delta`.

Hence no universal constant `c>0` can be forced in the r23 hypothesis `s_2(C),s_2(D)>=c`: choosing `n>(8/c)^2` defeats it while the full matrix still has the required three large eigenvalues.

This is not a counterexample to QFORM. It is a counterexample only to the proposed **fixed-size packet extraction** as a universal structural implication.

## Why the obstruction is genuinely collective

The large minority directions are accumulated from `O(delta)` entrywise defects over `Theta(n)` coordinates. With `delta=n^{-1/2}`, every fixed physical block approaches rank one, yet the `v` and `u` eigenvalues have size about `+sqrt(n)` and `-sqrt(n)`. Thus the third-direction curvature is macroscopic but bank-level: it cannot be detected by a bounded number of coordinates.

The four sign classes `(u_i,v_i)` give four independent original-coordinate banks. This identifies the appropriate next scale: aggregate whole banks (or blocks whose cardinality is at least on the order of `1/delta`) before paying reciprocal singular values or minors. Any proof that first fixes `K` original coordinates and then seeks a `K x K` uniformly conditioned witness cannot close the full target.

## Designated partner result applied to an actual inequality

Use the completed fleet04/B11 sign-frustrated-triangle theorem at

`yspennstate/math-open-problems@572f6cd066c9cdef7b5a509917b4dcd79cea2fda`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T021512Z-fleet04-B11-sign-frustrated-triangle-r4/REPORT.md`.

That theorem says: for a physical triple with positive diagonals `a_i`, if normalized off-diagonals are within `eta<1/2` of a sign pattern whose triangle product is `-1`, then `sigma_min >= min_i a_i (1-2eta)` and the full ambient quadratic form has

`||p_Q||_infinity <= 6 sqrt(pi)/sigma_min`

(up to taking the minimum with its Schur alternative).

In the present near-rank-one magnitude geometry, every normalized edge magnitude lies in `[1-4delta,1]`. Therefore if **one triangle had the same magnitudes but a frustrated sign pattern**, we could take `eta=4delta`, `min a_i=1`, and obtain

`||p_Q||_infinity <= 6 sqrt(pi)/(1-8delta)`.

For `delta<=1/128`,

`||p_Q||_infinity <= 6 sqrt(pi) * 16/15 < 11.344`.

Thus the partner theorem pays the sign-frustrated version uniformly even as `delta->0`. The obstruction isolated here is specifically the globally balanced sign configuration, not near-singularity of the pair magnitudes by itself.

## Rank-two logarithmic control and the third direction

The mandatory control remains the exact rank-two saddle: for independent `X,Y~Unif[-1/2,1/2]`,

`p_{2XY}(t)=log(1/(2|t|))`

on `0<|t|<1/2`, so rank two is genuinely unbounded.

In this family the third direction is not local: it is the collective bank contrast `v` (together with the opposite bank contrast `u`). Their eigenvalues are `+delta n+2delta` and `-delta n+2delta`. At the critical scaling `delta=n^{-1/2}`, these directions diverge in strength while every fixed physical block loses them. Therefore any successful uniform smoothing argument in this chamber must aggregate product structure across many coordinates before applying the rank-three mechanism.

## Remaining implication

`QFORM-BALANCED-FOUR-BANK-AGGREGATION-v1`: starting from balanced positive near-rank-one physical correlations, compile the collective defect into disjoint original-coordinate banks and prove a product-preserving density bound before any reciprocal-minor payment. The explicit family above is the normalization test: a valid compiler must remain uniform for `delta=n^{-1/2}`.

Continuity is not proved here. The full conjecture remains open.
