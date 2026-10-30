# fleet03/B11 — QFORM indefinite signatures: localized Pluecker cone-trace branch

Run: `20260922T164156Z-fleet03-B11`

Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM`; the full universal QFORM conjecture remains **OPEN / NOT PROVED**.

Brain status: `WITHOUT_VERIFIED_BRAIN`. Repository reads are not native brain ingestion.

## Scope

The target is the bounded-density conjecture for `Q=X^T A X` with independent real coordinates having densities at most one and at least three eigenvalues of `A` of modulus at least one. This report stays on the genuinely indefinite rank-three signature mechanism. It uses no post-rotation independence, no pointwise law-uniform oscillatory decay, no fiber-supremum shortcut, and no support/moment/log-concavity assumptions.

This run consumes the completed designated-partner result `fleet04/B11`, canonical source

`yspennstate/math-open-problems@44e7ab6750fbc3dccd77f1dd9e8bdba0bba2f0f5:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260922T161514Z-b11-cone-trace-r1/REPORT.md`.

That result proves the exact cone-trace identity for `q(u,v,w)=u^2+v^2-w^2` and shows by an explicit unit-volume cone tube that an arbitrary bounded three-dimensional density can have arbitrarily large cone trace. Therefore any positive result must use genuine product-projection provenance.

We also use the preceding fleet03/B11 local physical-triple theorem, source

`yspennstate/math-open-problems@117c1568f8f458706c1123327f893efd750053c5:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B11/20260922T150842Z-fleet03-B11-QFORM-r12/REPORT.md`.

It proves, for every invertible symmetric physical `3 x 3` block `B`, arbitrary affine term, and three independent cap-one coordinates,

`||p||_infinity <= C0 / sqrt(s1(B)s2(B))`,

where `0<s1(B)<=s2(B)<=s3(B)` are the singular values and

`C0 = 48*3^(1/4) < 63.172`.

Its proof is a direct original-coordinate dyadic gradient-shell argument. The estimate is uniform in the affine term, so it is stable under conditioning all other original coordinates.

## New theorem: localized Pluecker mass controls the indefinite cone trace

Let `A` have **exact rank three** and spectral representation

`A = R Lambda R^T`,

where `R` is `n x 3` with `R^T R=I_3`, and the three nonzero eigenvalues in the diagonal matrix `Lambda` satisfy

`min_j |lambda_j| >= 1`.

The sign pattern of `Lambda` is arbitrary; in particular this includes `(+,+,-)` and `(+,-,-)`.

For a triple `T={i,j,k}` of physical coordinates write `R_T` for the `3 x 3` row submatrix and

`d_T = |det R_T|`.

For a coordinate set `S` of size `m>=3`, define its rank-three Pluecker mass

`Omega(S) = sum_{T subset S, |T|=3} d_T^2`.

### Theorem

If `Omega(S)>=eta>0`, then for arbitrary independent inputs with densities at most one,

`||p_{X^T A X}||_infinity <= C0 * sqrt( binom(m,3) / eta ).`       (1)

For normalized indefinite signature `Lambda=diag(1,1,-1)`, if `g` denotes the genuine three-dimensional spectral projection density of `Z=R^T X`, then the completed fleet04/B11 identity gives the literal cone-trace inequality

`T(g) = ||p_{Z_1^2+Z_2^2-Z_3^2}||_infinity`

`     <= C0 * sqrt( binom(m,3) / eta ).`                            (2)

Thus the partner's unbounded arbitrary-density cone tube is quantitatively excluded whenever a bounded physical coordinate bank carries fixed positive Pluecker mass. This is a provenance statement, not an `L^infinity(g)` statement.

### Proof

By averaging, there is a triple `T subset S` with

`d_T^2 >= eta / binom(m,3)`.                                      (3)

In particular `M:=R_T` is invertible. Condition on every original coordinate outside `T`. The conditional quadratic in the three still-random physical coordinates has Hessian

`B_T = M Lambda M^T`,

while all outside coordinates enter only through an affine term and a constant. The three surviving coordinates remain independent and retain their density caps.

Let the singular values of `M` be

`0<alpha<=beta<=gamma<=1`.

The upper bound `gamma<=1` follows from `M^T M <= R^T R=I_3`. Moreover

`d_T=alpha beta gamma <= alpha beta`.                              (4)

We now lower-bound the product of the two smallest singular values of `B_T` without assuming `Lambda` is positive definite. Since `B_T` is invertible,

`B_T^{-1}=M^{-T} Lambda^{-1} M^{-1}`.

Taking second exterior powers,

`|| wedge^2 B_T^{-1} ||`
` <= ||wedge^2 M^{-T}|| ||wedge^2 Lambda^{-1}|| ||wedge^2 M^{-1}||`
` <= (alpha beta)^(-2)`,                                           (5)

because every singular value of `Lambda^{-1}` is at most one. On the other hand,

`||wedge^2 B_T^{-1}|| = 1/(s1(B_T)s2(B_T))`.

Hence

`s1(B_T)s2(B_T) >= (alpha beta)^2 >= d_T^2`.                       (6)

The local fleet03/B11 theorem, uniform over the conditional affine term, therefore gives for every fixed outside configuration

`||p_{Q | X_{T^c}}||_infinity <= C0/d_T`.

Averaging the conditional densities cannot increase this same uniform bound, so

`||p_Q||_infinity <= C0/d_T`
` <= C0 * sqrt(binom(m,3)/eta)`,

by (3). This proves (1).

For `Lambda=diag(1,1,-1)`, fleet04/B11 proved exactly that the density of the spectral quadratic equals its cone-trace functional. Substituting (1) into that identity yields (2), which is the required actual inequality obtained from the completed designated-partner result. QED.

## Cauchy-Binet normalization and a new four-coordinate corollary

Cauchy-Binet gives the exact normalization

`sum_{|T|=3} d_T^2 = det(R^T R)=1`.                                (7)

Consequently, if an exact-rank-three target lives on only four physical coordinates, take `S={1,2,3,4}`. Then `Omega(S)=1`, so one of its four triples has `d_T>=1/2`. The theorem yields

`||p_Q||_infinity <= 2 C0 = 96*3^(1/4) < 126.344`.                 (8)

This covers every genuinely rotated rank-three four-coordinate form with nonzero eigenvalues of modulus at least one, including both indefinite signatures, even though the full physical `4 x 4` Hessian is singular and none of the spectral coordinates need coincide with an original coordinate.

More generally, a bounded coordinate bank `S` carrying a fixed fraction `eta` of the Pluecker mass yields a dimension-free cone-trace bound through (1). The remaining exact-rank-three difficulty is therefore the complementary **Pluecker-diffuse / high-cardinality** regime, where every bounded bank carries vanishing volume mass. This is exactly where a deterministic good-triple selector is known to fail and where aggregation must precede reciprocal-minor payment.

## Exact genuinely rotated indefinite example

Take the tetrahedral Parseval frame

`R=(1/2)*[[ 1, 1, 1],`
`         [ 1,-1,-1],`
`         [-1, 1,-1],`
`         [-1,-1, 1]]`

and `J=diag(1,1,-1)`. Then `R^T R=I_3`, every `3 x 3` row minor has absolute determinant `1/2`, and

`A=R J R^T`
` = [[ 1/4, 1/4, 1/4,-3/4],`
`    [ 1/4, 1/4,-3/4, 1/4],`
`    [ 1/4,-3/4, 1/4, 1/4],`
`    [-3/4, 1/4, 1/4, 1/4]].`

The spectrum is `{1,1,-1,0}`. Hence this is a genuinely rotated `(+,+,-)` exact-rank-three form on four independent physical coordinates. Formula (8) gives a universal cap `<126.344`; replacing `A` by `-A` gives the `(+,-,-)` case.

This example is structurally different from the easy diagonal control: no physical coordinate is a spectral coordinate, and the output is a singular four-variable quadratic form rather than an invertible three-variable one.

## Why the third direction removes the rank-two logarithm

The local physical-triple theorem behind (1) makes the dimensional mechanism explicit. On a shell where the gradient scale is `r`, one physical coordinate gives inverse-map cost `O(r^{-1})`. In three genuinely independent physical directions, the allowed projection onto the other two coordinates has area `O(r^2)`. The small-scale shell contribution is therefore `O(r)`, and the dyadic series converges.

For an opposite-sign rank-two saddle, the analogous transverse projection has only length `O(r)`, leaving `O(1)` per small scale; the dyadic sum diverges logarithmically. The nonzero Pluecker minor certifies that the third spectral direction is supplied by a genuinely independent third original coordinate, exactly the product-provenance feature absent from the arbitrary cone-tube counterexample of fleet04/B11.

## Additional identity useful for the heavy/diffuse split

Let `r_i` denote row `i` of `R` and `h_i^2=||r_i||_2^2` its leverage. The rank-three projection determinantal identity gives

`sum_{T: i in T, |T|=3} d_T^2 = h_i^2`.                            (9)

Thus a heavy physical row carries exactly its leverage mass in the triple-volume distribution. If that mass is concentrated on only a bounded number of partner pairs, theorem (1) closes the branch. If instead it is spread over many pairs, the surviving obstruction is an explicitly two-dimensional Pluecker-diffuse aggregation problem around that heavy row. This is a narrower bridge than an unrestricted cone-trace estimate.

Identity (9) follows, for example, by Cauchy-Binet applied to the rank-three projection kernel `P=RR^T`: the determinantal probability weights `det P[T,T]=d_T^2` sum to one and their one-point inclusion marginal is `P_ii=h_i^2`. No probabilistic assumption on `X` is used in this linear-algebra identity.

## Continuity status

The argument proves absolute continuity and an essentially bounded density on the stated localized-Pluecker branch. It does **not** prove that the density has a continuous representative for arbitrary measurable cap-one input densities. The completed fleet04/B11 partner establishes continuity only in its narrower separated null-heavy subclass. Full target-level continuity remains open and is recorded separately from the `L^infinity` claim.

## What remains unpaid

This theorem does not solve the all-`n` target and does not solve even the entire exact-rank-three case by itself. The complementary exact-rank-three branch is:

**PLUECKER-DIFFUSE PRODUCT CONE TRACE.** The Pluecker mass `d_T^2` is spread over high-cardinality coordinate banks so that no bounded `S` has fixed `Omega(S)`. One must aggregate the corresponding original-coordinate product structure before paying `1/d_T`, or prove an equivalent cone-trace/shear estimate. This includes the bank families that refute a deterministic single-good-triple selector.

For matrices with additional spectral directions, a further step is required because a chosen rank-three spectral truncation and the remaining quadratic form are not independent in original coordinates. No such reduction is claimed here.

## Status summary

- designated partner `fleet04/B11`: consumed and applied to inequality (2);
- new result: localized Pluecker-mass cone-trace theorem (1);
- new complete corollary: all exact-rank-three four-coordinate targets, both indefinite signatures, bounded by `<126.344`;
- exact tetrahedral rotated witness checked algebraically;
- opposite-sign rank-two logarithmic control: retained;
- full universal conjecture: **OPEN / NOT PROVED**;
- continuous-density conclusion in this branch: **NOT PROVED**;
- execution: `WITHOUT_VERIFIED_BRAIN`.

Manual narrow privacy scan of this report: only public mathematical statements, repository commit references, logical account/slot labels and nonsecret run identifier are present; no credentials, scheduler IDs, machine paths or unrelated private material are included.
