SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-24T11:21:59Z.
attacking: the DET49 aggregate-extraction frontier: turn exact-rank-three Pluecker mass into either a real cross-volume exit or an explicitly source-aggregatable near-coloop obstruction.

# fleet02/B11 r14 — disjoint Pluecker currency and the exact no-disjoint-base reduction

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: indefinite signatures / complementary constructions and source-valid counterexamples.
Status: `NEW SUPPORTING STRUCTURAL THEOREM + PARTNER RESULT APPLIED / FULL QFORM OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred, but no distinct native authenticated brain receiver was exposed or verified).

## 0. First unpaid implication

The first unpaid implication is now

`QFORM-NEAR-COLOOP-STABILITY-v1`:

> Quantitatively stabilize the exact theorem below. If the rank-three Pluecker law has small disjoint-pair mass and no large atom, force a near-coloop / one-line-plus-bounded-exceptions source decomposition strong enough for the existing hub/physical-triple receivers, or else produce a partition whose cross 3-volume has the pinned Theorem D/D' marginal gate.

The exact zero-disjoint-mass endpoint is proved here except for the pure-coloop chamber. This is strictly narrower than the previous `DET49-AGGREGATE-EXTRACTION` debt.

No moment, support, log-concavity, connected-support, identical-law, diagonal-basis, or post-rotation-independence assumption is used.

## 1. Exact-rank-three setup and Pluecker law

Let

`A = R M R^T`, `R^T R = I_3`,

where `M` is a real invertible `3x3` matrix of indefinite inertia `(2,1)` or `(1,2)`. Put

`s = min_j |lambda_j(M)|`, `D = |det M| >= s^3`.

Write `r_i^T` for the `i`th row of `R`. For every physical triple `S`, define

`w_S = det(R_S)^2`.

Cauchy-Binet gives

`sum_{|S|=3} w_S = det(R^T R) = 1`.                                      (1.1)

Thus `w` is a probability law on physical triples. Moreover

`det A_SS = det(R_S M R_S^T) = det(M) det(R_S)^2`,

hence

`boxed: |det A_SS| = D w_S.`                                               (1.2)

Therefore the previous B11 theorem `QFORM-INDEFINITE-PHYSICAL-TRIPLE-DET49-v1` immediately gives the large-atom exit

`boxed: max_S w_S >= omega  =>  ||p_Q||_infinity <= 49 D^(-1/3) omega^(-1/3) <= 49 s^(-1) omega^(-1/3).`  (1.3)

This is a literal-original-coordinate statement; no rotated random variables are declared independent.

## 2. Disjoint Pluecker mass is exactly averaged cross-volume

Let `S,T` be independent triples sampled from `w` and put

`eta = P(S intersect T = emptyset)
     = sum_{S intersect T = emptyset} w_S w_T`.                            (2.1)

For a physical partition `[n]=I union J`, set

`G_I = R_I^T R_I`, `G_J = R_J^T R_J = I_3-G_I`.

Cauchy-Binet gives

`det G_I = sum_{S subset I, |S|=3} w_S`,
`det G_J = sum_{T subset J, |T|=3} w_T`.                                  (2.2)

Choose `I` by independent fair coin flips and `J=I^c`. A fixed ordered pair `(S,T)` contributes to (2.2) iff `S subset I` and `T subset J`; this is impossible when the triples intersect, and has probability `2^(-6)=1/64` when they are disjoint. Hence

`boxed: E_I[det G_I det G_J] = eta/64.`                                    (2.3)

Consequently some partition obeys

`boxed: det G_I det G_J >= eta/64.`                                        (2.4)

Now let `B=A_IJ=R_I M R_J^T`. Its rank-three squared volume is

`Z_3(B) = sum_{|S|=|T|=3} det(B_ST)^2`.

For each `S subset I`, `T subset J`,

`det(B_ST)=det(R_S)det(M)det(R_T)`,

so

`boxed: Z_3(A_IJ)=D^2 det G_I det G_J.`                                    (2.5)

Combining (2.4)-(2.5),

`boxed: there exists I|J with Z_3(A_IJ) >= D^2 eta/64.`                    (2.6)

This converts a combinatorial property of the exact rank-three frame into an actual original-coordinate cross-volume currency.

### 2.1 Real inequality from the required pinned source

The required pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`, proves Theorem D' for a cross block with 3-volume `Z`: if its I-side volume-sampling marginals are at most `h<3/4`, then

`||p_Q||_infinity <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) Z^(-1/6)`.

Apply this to a partition satisfying (2.6), whenever that same partition has the D' marginal gate. Then

`boxed:
 ||p_Q||_infinity
 <= 12 sqrt(e) (2h)^(-1/2) (3-4h)^(-1)
    D^(-1/3) eta^(-1/6)
 <= 12 sqrt(e) (2h)^(-1/2) (3-4h)^(-1)
    s^(-1) eta^(-1/6).`                                                   (2.7)

Thus a quantitative disjoint-Pluecker branch is already paid as soon as its authentic cross-volume partition is not locally concentrated. The remaining issue is precisely concentration of the conditional triple law, not absence of volume.

There is also the exact inclusion-exclusion identity. Put

`q_i=P(i in S)`, `q_ij=P(i,j in S)`.

For the projection determinantal law `q_i=||r_i||^2` and `q_ij=det((RR^T)_{ij,ij})`. Since two triples have intersection size at most three,

`boxed:
 eta = 1 - sum_i q_i^2 + sum_{i<j} q_ij^2 - sum_S w_S^2.`                  (2.8)

In particular, if `omega=max_S w_S`, then

`eta >= 1-sum_i q_i^2-omega`.                                             (2.9)

Equations (1.3), (2.7), and (2.9) give a concrete atom / diffuse-disjoint-volume split. They do not by themselves prove the D' marginal gate.

## 3. Exact zero-disjoint-mass structure

The next theorem is the main new structural result.

### Theorem 3.1 — `QFORM-PLUCKER-NODISJOINT-BASE-v1`

Assume `eta=0`, equivalently there are no two disjoint physical triples with nonzero Pluecker determinant. Then one of the following holds.

1. **Pure coloop.** Some physical coordinate `h` has leverage `||r_h||^2=1`; equivalently all other rows lie in the plane `r_h^perp`.

2. **One line plus at most five exceptions.** There is a one-dimensional subspace `L subset R^3` and an exceptional set `E` with `|E|<=5` such that `r_i in L` for every `i notin E`.

#### Proof

Choose one row basis `B={b1,b2,b3}` with `det R_B !=0`; it exists by (1.1). Let `O=[n]\B`.

If `span{r_i:i in O}` had rank three, it would contain a basis disjoint from `B`, contradicting `eta=0`. Hence its rank is at most two.

If that rank is at most one, all rows outside the three indices in `B` lie on one line, giving alternative 2 with at most three exceptions.

Suppose its rank is two and write `W=span{r_i:i in O}`. At least one element of `B` lies outside `W` because the full row family has rank three.

If exactly one element `h` of `B` lies outside `W`, then every row except `r_h` lies in `W`. Let `nu` be a unit normal to `W`. Parseval gives

`1 = nu^T I_3 nu = sum_i <nu,r_i>^2 = <nu,r_h>^2 <= ||r_h||^2 <= 1`.

Therefore `||r_h||^2=1` and `r_h=+/-nu`, giving alternative 1.

It remains that at least two elements of `B` lie outside `W`. If `O` contained two disjoint independent pairs `P,Q`, then choosing two distinct `h1,h2 in B\W` would make `P union {h1}` and `Q union {h2}` two disjoint row bases, contradiction. So `O` has no two disjoint independent pairs. Choose one independent pair `P subset O` (possible because `rank O=2`). Then `O\P` has rank at most one, for otherwise it contains an independent pair disjoint from `P`. Thus every row outside `B union P` lies on one line, and `|B union P|<=5`. QED.

The theorem is elementary rank-three base-packing specialized to the actual Pluecker support; no abstract matroid theorem is needed.

## 4. The non-coloop eta=0 branch is already bounded after source aggregation

Alternative 2 of Theorem 3.1 is not a genuine remaining obstruction.

Let `E` be the at-most-five exceptional original coordinates and write, for `i notin E`,

`r_i=a_i v`

with `v` a unit vector. Put

`tau=sum_{i notin E} a_i^2`.

If `tau>0`, define the **source-bank aggregate**

`T=tau^(-1/2) sum_{i notin E} a_i X_i`.                             (4.1)

It is independent of all `X_e`, `e in E`, because it uses a disjoint original-coordinate bank. By the checked product-projection theorem in the required pinned `FOURIER_ROUTE_REPORT.md` (LPP, k=1),

`||p_T||_infinity <= sqrt(2).`                                           (4.2)

Moreover

`R^T X = sqrt(tau) v T + sum_{e in E} r_e X_e`.                          (4.3)

Thus the exact-rank-three quadratic form depends only on at most six independent variables `(T,(X_e)_{e in E})`. Their effective frame rows are

`c_0=sqrt(tau)v`, `c_e=r_e`,

and satisfy

`sum c_j c_j^T=I_3`.                                                      (4.4)

So the effective coefficient matrix `A_eff=C M C^T` has the same three nonzero eigenvalues as `M`, the same indefinite inertia, and by Cauchy-Binet its triple weights sum to one. Since there are at most `binom(6,3)=20` triples, some effective physical triple has

`|det (A_eff)_SS| >= D/20`.                                               (4.5)

Only `T` may have density cap larger than one. Replace it by `T'=sqrt(2)T`; its density is cap one. This congruence divides the determinant of a triple containing `T` by exactly two and leaves other triple determinants unchanged. Hence in the cap-one effective system there is an indefinite literal physical triple with

`boxed: |det B_3| >= D/40.`                                               (4.6)

Apply `QFORM-INDEFINITE-PHYSICAL-TRIPLE-DET49-v1`:

`boxed:
 ||p_Q||_infinity
 <=49 (D/40)^(-1/3)
 =49*40^(1/3) D^(-1/3)
 <=167.577643/s.`                                                         (4.7)

If `tau=0`, all active frame rows already lie among at most five original coordinates; the same argument has at most ten physical triples and is stronger than (4.7).

Therefore:

`boxed: eta=0 and no leverage-one coordinate  => ||p_Q||_infinity <168/s.` (4.8)

This is the first exact structural extraction statement in this B11 chain that pays every non-coloop no-disjoint-base configuration without requiring a large original minor in advance.

Continuity is not claimed in (4.7); DET49 is an essential-density theorem.

## 5. A source-valid pure-coloop obstruction family, and partner r55 applied

The pure-coloop alternative is real and cannot be removed by a large-Pluecker-atom argument. Consider

`A_m = [1] direct_sum (J_m/m) direct_sum (-J_m/m)`,                         (5.1)

on `1+2m` original coordinates. Its nonzero spectrum is exactly

`{1,1,-1}`.                                                               (5.2)

An eigenframe is

`r_0=(1,0,0)`,
`r_{Y_j}=(0,m^(-1/2),0)`,
`r_{Z_j}=(0,0,m^(-1/2))`.

Hence the only nonzero Pluecker weights are

`w_{ {0,Y_i,Z_j} } = 1/m^2`.                                             (5.3)

Thus

`omega=1/m^2 ->0`, but every supported triple contains the hub `0`, so

`boxed: eta=0.`                                                           (5.4)

Correspondingly every literal invertible physical triple determinant has magnitude `1/m^2`, and DET49 alone gives only a diverging `m^(2/3)` bound. This is a genuine structural obstruction to any theorem demanding one uniformly large literal determinant.

But it is not a QFORM counterexample. Define the two disjoint bank aggregates

`S_m=m^(-1/2) sum_j Y_j`, `T_m=m^(-1/2) sum_j Z_j`.

Then

`Q_m=X_0^2+S_m^2-T_m^2`.                                                  (5.5)

The variables `X_0,S_m,T_m` are genuinely independent because their original-coordinate banks are disjoint. The pinned product-projection theorem gives

`||p_{S_m}||_infinity, ||p_{T_m}||_infinity <=sqrt(2)`.                   (5.6)

Now apply the newest completed designated partner fleet03/B11 r55 theorem `QFORM-INDEFINITE-PAIR-L3-v1` (`math-open-problems@bc05973cb71eb6707de7342cafeef36af6a99230`) to the indefinite pair `S_m^2-T_m^2`, whose determinant currency is one. It gives

`||p_{S_m^2-T_m^2}||_3
 <=22 (sqrt(2)*sqrt(2))^(2/3)
 =22*2^(2/3).`                                                            (5.7)

The completed shifted-square theorem `QFORM-SHIFTED-SQUARE-L32-v1` gives

`||p_{X_0^2}||_(3/2)<=2`.                                                 (5.8)

Young's conjugate-exponent inequality therefore yields the uniform full-line estimate

`boxed:
 ||p_{Q_m}||_infinity
 <=44*2^(2/3)
 =69.8456462866...`                                                       (5.9)

for every `m` and every independent cap-one source law. This directly applies the partner result to the canonical coloop obstruction family.

### 5.1 The logarithmic saddle is retained, not hidden

For `m=1` and centered unit uniforms, the rank-two part is

`R=Y_1^2-Z_1^2=(Y_1-Z_1)(Y_1+Z_1)`

and has the standard logarithmic singularity at zero. More generally, whenever the bank-sum densities are bounded below in a neighborhood of zero (in particular for centered uniform banks), the change of variables

`u=s-t`, `v=s+t`, `s^2-t^2=uv`, `ds dt=(1/2)du dv`

shows that the density of `S_m^2-T_m^2` has a lower bound `c_m log(1/|x|)` near zero. Thus the rank-two saddle remains genuinely unbounded.

The third direction `X_0^2` removes it **without first bounding the saddle**: partner r55 places the saddle in `L^3`, the independent square lies in `L^(3/2)`, and `L^3 * L^(3/2) -> L^infinity` gives (5.9).

This is exactly the source-valid regularization mechanism required by the B11 assignment.

### 5.2 Sign-specific ruled geometry from the required pinned source

The family (5.1) has exact signature `(2,1)` at scale one. The required pinned Theorem C therefore gives the sharper one-sheet inequality

`boxed: p_{Q_m}(t) <= pi sqrt(2),  t>=0.`                                 (5.10)

I do not transfer this X-ray/ruling estimate to `t<0`: the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids that. The full-line L3/L3/2 estimate (5.9) pays the opposite two-sheet side in this family.

## 6. What the exact theorem says the quantitative proof must do

For exact rank three, the structural landscape is now:

- a large Pluecker atom is paid by DET49, (1.3);
- quantitative disjoint Pluecker mass creates a genuine original-coordinate cross 3-volume, (2.6), and pinned D' pays it whenever the authentic local marginal gate holds, (2.7);
- at the exact endpoint `eta=0`, every non-coloop support reduces by source aggregation to at most six independent variables and is paid uniformly by DET49, (4.8);
- the surviving exact endpoint is therefore a pure coloop (one leverage-one physical coordinate plus a residual two-dimensional product projection).

The next step is the quantitative stability version: small `eta` plus small `omega` must be converted either into a near-coloop with a controlled residual two-dimensional projection, a one-line-plus-bounded-exceptions approximation that can be aggregated before inversion, or a cross-volume partition satisfying the D' local marginal gate. One cannot discard a small residual quadratic matrix as a perturbation because the source laws have arbitrary unbounded support.

Arbitrary additional nonseparable spectrum remains a separate bridge from this exact-rank-three structural theorem to the owner's full target.

## 7. Sources and status

Required pinned source consumed at exact commit `e5f71d79eff325201dd0274053d20268ce65b837`:

- `RESULTS.md`;
- `FOURIER_ROUTE_REPORT.md` (Theorem D', product-projection density theorem);
- `COUNTEREXAMPLE_SEARCH.md` (ruled Theorem C and two-sheet limitation context).

Newest completed designated partner consumed:

- fleet03/B11 r55, `QFORM-INDEFINITE-PAIR-L3-v1`, `math-open-problems@bc05973cb71eb6707de7342cafeef36af6a99230`.

Previous B11 dependency actually used:

- `QFORM-INDEFINITE-PHYSICAL-TRIPLE-DET49-v1`, `math-open-problems@e65ea69496521e9d4f4469e8cc8366381d03473f`.

Full unrestricted QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity remains separate and OPEN.
