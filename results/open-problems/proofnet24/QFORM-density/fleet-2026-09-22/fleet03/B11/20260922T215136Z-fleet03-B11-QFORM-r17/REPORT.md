SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-22T21:51:36Z.
attacking: the null-frame pair-or-ridge aggregate: pay either a transverse physical null pair or a diffuse rank-three original-coordinate cross cut, then identify the precise heavy-star residual.

# fleet03/B11 QFORM r17 — indefinite pair-or-ridge compiler and null-frame trace consequence

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet03/B11` — Indefinite signatures  
Run: `20260922T215136Z-fleet03-B11-QFORM-r17`  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_COMPILER / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The full conjecture remains open. This run gives a correction-safe quantitative compiler for a large arbitrary-rank indefinite branch and converts the designated partner's exact parabolic trace identity into a genuine dimension-free trace inequality under two explicit original-coordinate certificates. It also isolates the remaining null-frame obstruction as either cross-rank-at-most-two at the tested scale or a quantitatively many-small-pair heavy star.

No step below assumes independence after a spectral rotation, a pointwise law-uniform Fresnel estimate, the refuted arbitrary-joint rank-three coarea bound, a conditional-density cap as a substitute for independence, a scalar conditional supremum, bounded support, moments, log-concavity, or a uniformly good fixed principal triple.

## 1. Source-pinned inputs

### 1.1 Full-matrix indefinite physical-pair theorem

Use the complete supporting theorem at

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

If `s_3(A)>=s>0` and an ORIGINAL-coordinate principal pair `B` is invertible and indefinite, with

`D=|det B|`, `kappa=sigma_min(B)`,

then for independent cap-one coordinates, with arbitrary affine terms and arbitrary remaining spectrum/couplings,

`||p_Q||_infinity <= 3*400^(1/3) (D^2*kappa*s)^(-1/6)`.       (1.1)

This is an essential-boundedness theorem; continuity is not supplied by this branch.

### 1.2 One-scale ridge theorem

Use the complete supporting theorem at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For an ORIGINAL-coordinate cut `I,J`, let `B=A[I,J]`. For `gamma>0`, set

`K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`,
`theta_gamma=tr K_gamma`.

If for some `1<=q<=2`

`max_i (K_gamma)_ii <= q/2`, `theta_gamma>2q`,                 (1.2)

then the full form, with arbitrary self blocks/outside coordinates/couplings, has a continuous `C_0` density. The simplified bound is

`||p_Q||_infinity <= sqrt(e)/(sqrt(2q)*gamma) * theta/(theta-2q)`. (1.3)

### 1.3 Designated partner fleet04/B11

Use the completed designated-partner report

`yspennstate/math-open-problems@797dcde430e982a020d7642b54cadc281cbc9bc1`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260922T191727Z-fleet04-B11-nullgraph-obstruction-r2/REPORT.md`.

For

`H0=[[0,0,1],[0,1,0],[1,0,0]]`, `T=Y^T H0 Y=2 Z W+V^2`,

with joint density `h(z,v,w)`, it proves the exact identity

`p_T(t)=(1/2) integral_{w!=0} h((t-v^2)/(2w),v,w) dv dw/|w|`. (1.4)

Thus, writing

`N(h)=sup_t integral_{w!=0} h((t-v^2)/(2w),v,w) dv dw/|w|`,

one has

`N(h)=2 ||p_T||_infinity`                                      (1.5)

for the resulting density representative. The same partner report gives an explicit nonlinear dependent construction with bounded transverse density and bounded conditional `Z|(V,W)` density for which `N(h)=infinity`. Therefore a valid compiler must retain the ORIGINAL product-linear provenance; marginal/conditional caps alone are not enough.

## 2. Main compiler

### Theorem 2.1 — `QFORM-INDEFINITE-PAIR-OR-DIFFUSE-RIDGE-COMPILER-v1`

Let `A` be any real symmetric `n x n` matrix with

`s_3(A)>=s>0`,                                                 (2.1)

and let `X_1,...,X_n` be independent real random variables whose densities are bounded by one. Arbitrary affine terms may be added to `X^T A X`.

Fix positive parameters `delta,sigma`. Either one of the following certificates is sufficient for a universal quantitative density bound.

**(P) Quantitative indefinite physical pair.** There are original coordinates `i!=j` such that the principal pair `B=A[{i,j},{i,j}]` is invertible indefinite and, with `D=|det B|`, `kappa=sigma_min(B)`,

`(D^2*kappa)^(1/5) >= delta*s`.                                (2.2)

Then

`||p_Q||_infinity <= 3*400^(1/3) delta^(-5/6) s^(-1)`          (2.3)

and numerically the coefficient is

`3*400^(1/3)=22.1041889918...`.                                (2.4)

**(R) Diffuse rank-three original-coordinate cross cut.** There is a disjoint original-coordinate cut `I,J` whose cross block `B=A[I,J]` has

`tau:=s_3(B) >= sigma*s`,                                      (2.5)

and, after choosing one of the two orientations `B` or `B^T`, every row in that orientation obeys

`max_i ||B_{i,*}||_2 <= tau/sqrt(12)`.                         (2.6)

Then `Q` has a continuous `C_0` density and

`||p_Q||_infinity <= (9/2)*sqrt(3e)/(sigma*s)`                 (2.7)

with coefficient

`(9/2)*sqrt(3e)=12.8505105377...`.                             (2.8)

These alternatives allow arbitrary sign pattern and arbitrary additional spectrum. In particular they apply to genuinely rotated `(+,+,-)` and `(+,-,-)` situations and do not require exact rank three.

### Proof of (P)

Apply (1.1). Define the pair scale

`zeta=(D^2*kappa)^(1/5)`.

Then

`(D^2*kappa*s)^(-1/6)=zeta^(-5/6)s^(-1/6)`.

By `zeta>=delta*s`,

`zeta^(-5/6)s^(-1/6) <= delta^(-5/6)s^(-1)`.

Substitution into (1.1) proves (2.3). No condition is imposed on any coordinate outside the physical pair. QED.

### Proof of (R)

Set

`gamma=tau/sqrt(6)`                                            (2.9)

and form `K_gamma` from the chosen orientation of the cut. Since for every positive semidefinite matrix `M`,

`M(gamma^2 I+M)^(-1) <= M/gamma^2`,                            (2.10)

we have, row by row,

`(K_gamma)_ii <= ||B_{i,*}||_2^2/gamma^2`
`              <= (tau^2/12)/(tau^2/6)=1/2`.                  (2.11)

Let the singular values of `B` be `b_1>=b_2>=b_3>=...`. Since `b_3=tau`,

`theta_gamma=sum_k b_k^2/(gamma^2+b_k^2)`
`           >=3 tau^2/(tau^2/6+tau^2)=18/7>2`.                (2.12)

Thus the ridge theorem applies with `q=1`. The function `x/(x-2)` decreases for `x>2`, so

`theta/(theta-2) <= (18/7)/(18/7-2)=9/2`.                     (2.13)

Using `gamma=tau/sqrt6` in (1.3),

`||p_Q||_infinity`
` <= sqrt(e)/(sqrt2*(tau/sqrt6)) * 9/2`
` = (9/2)*sqrt(3e)/tau`
` <= (9/2)*sqrt(3e)/(sigma*s)`.                               (2.14)

The cited ridge theorem also supplies continuity and vanishing at infinity. QED.

## 3. Null physical diagonal: a clean pair-versus-many-small-pair corollary

Suppose additionally

`A_ii=0` for every original coordinate `i`.                    (3.1)

Every nonzero physical pair is then automatically indefinite:

`B_ij=[[0,a_ij],[a_ij,0]]`,

with

`D=|a_ij|^2`, `kappa=|a_ij|`, `(D^2*kappa)^(1/5)=|a_ij|`.      (3.2)

Hence if some `|a_ij|>=delta*s`, branch (P) gives immediately

`||p_Q||_infinity <=22.104189 delta^(-5/6)/s`.                 (3.3)

Now assume no such pair exists, so

`max_{i!=j}|a_ij|<delta*s`.                                    (3.4)

Consider any cut `I,J` with `tau=s_3(A[I,J])>=sigma*s`. If the ridge certificate (2.6) fails in both orientations, at least one side contains a row `r` with

`||r||_2>tau/sqrt(12)>=sigma*s/sqrt(12)`.                      (3.5)

Because each entry of that row has magnitude `<delta*s`, its effective support satisfies

`(# {j:r_j !=0}) * delta^2 s^2 > ||r||_2^2 > sigma^2 s^2/12`,

and therefore

`# {j:r_j !=0} > sigma^2/(12 delta^2)`.                        (3.6)

More invariantly,

`||r||_2^2/||r||_infinity^2 > sigma^2/(12 delta^2)`.           (3.7)

Thus a zero-diagonal target which escapes both paid branches has a precise residual form at every rank-three cut scale: either no cut has `s_3>=sigma*s` (a quantitative cross-rank-at-most-two obstruction), or every such cut contains a genuinely many-small-pair heavy star with effective support exceeding `sigma^2/(12 delta^2)`.

This is the correct aggregation target; it does not pretend that one uniformly conditioned physical pair or one good fixed triple must exist. The known singleton-plus-two-banks obstruction belongs exactly to this residual geometry.

## 4. Actual application of fleet04/B11: a parabolic null-graph trace bound

The partner obstruction is naturally expressed in a product-linear null frame. Let

`Y=L X in R^3`,                                                (4.1)

where the columns `ell_i` of `L` are coefficient vectors of the independent original coordinates, and let

`A=L^T H0 L`.                                                   (4.2)

Assume every source column is `H0`-null,

`ell_i^T H0 ell_i=0`.                                         (4.3)

Then `A_ii=0` exactly, while

`A_ij=ell_i^T H0 ell_j`                                       (4.4)

measures the transverse pairing of two null rays. Assume also `s_3(A)>=s>0`. This includes genuinely rotated indefinite product-linear realizations of the canonical `(+,+,-)` form; negating `H0` gives `(+,-,-)`.

Let `h` be the joint density of `Y` (in the rank-three case; the partner identity can equivalently be read through the induced pushforward density). Since

`T=Y^T H0Y=X^TAX`,                                            (4.5)

the designated partner identity (1.5) converts Theorem 2.1 into the following **actual trace inequalities**.

If some null-ray pair satisfies

`|ell_i^T H0 ell_j|>=delta*s`,                                 (4.6)

then

`N(h)=2||p_T||_infinity`
` <=6*400^(1/3) delta^(-5/6)s^(-1)`
` <44.208378 delta^(-5/6)s^(-1)`.                             (4.7)

If instead an original-coordinate cut obeys the diffuse rank-three certificate (2.5)-(2.6), then

`N(h)=2||p_T||_infinity`
` <=9*sqrt(3e)/(sigma*s)`
` <25.701022/(sigma*s)`.                                      (4.8)

These are not consequences of a marginal cap for `(V,W)` plus a conditional cap for `Z`. They use product provenance before the nonlinear trace: either a true original-coordinate indefinite pair plus the third singular scale of the full matrix, or three effective cross singular directions with ridge leverage below the Hausdorff--Young threshold. Therefore they exclude the partner's multiscale null-graph tracking mechanism on both certified branches without contradicting its nonlinear counterexample.

## 5. Exactly how the third direction removes the opposite-sign rank-two logarithm

The mandatory rank-two control survives untouched. For independent

`X,Y ~ Uniform[-1/2,1/2]`,

`p_{2XY}(t)=log(1/(2|t|))`, `0<|t|<1/2`,                      (5.1)

so an opposite-sign rank-two saddle is unbounded at zero.

The two branches above expose two rigorous ways in which a third direction removes this singularity.

**Physical-pair branch.** The pair theorem first retains the logarithmic two-coordinate density envelope. Completing that pair leaves a Schur remainder whose operator norm is at least `s_3(A)>=s`, because the completed part has rank two. The arbitrary-rank quarter-small-ball estimate for that remainder turns

`log_+(a/|t-R|)`

into a finite averaged quantity. Thus the third singular direction is used exactly to randomize the critical value of the logarithm; it is not hidden inside a rotated independence claim.

**Diffuse-ridge branch.** Three cross singular values `>=tau` and `gamma=tau/sqrt6` force

`theta_gamma>=18/7`.                                          (5.2)

The ridge characteristic-function bound therefore decays with exponent

`beta=theta_gamma/2>=9/7>1`,                                  (5.3)

which is integrable in time. With only two such directions the corresponding critical effective dimension cannot be forced above two, so the same `q=1` mechanism sits at the nonintegrable `|t|^-1` endpoint. This is the Fourier counterpart of the rank-two logarithm.

Both explanations preserve the original-coordinate product law.

## 6. What remains unpaid

The compiler is not an exhaustive theorem under the bare hypothesis `s_3(A)>=1`. A full proof must still show that every matrix not already handled elsewhere enters one of the paid branches, or directly control the complement.

For the null-frame / zero-diagonal geometry, the complement is now quantitative:

1. all physical null-ray pairings are small at scale `delta*s`; and
2. either every cross cut has third singular value below `sigma*s`, or any cut with a third singular direction has a row of effective support `>sigma^2/(12 delta^2)`.

The next B11 implication is therefore **many-small-pair heavy-star aggregation before inversion**: exploit the independent original coordinates across that large effective support to pay the parabolic trace without replacing product-linear provenance by a conditional-density cap. This is exactly where the fleet04/B11 obstruction says a proof must use more than marginal bounds.

The universal conjecture remains **OPEN / NOT PROVED**. The new pair branch proves essential boundedness; the ridge branch proves a continuous `C_0` density. No continuity claim is made outside the ridge-certified branch.

## 7. Deterministic checks

The accompanying `VERIFY.py` checks the exact threshold values

`theta=18/7`, `max K_ii=1/2`,

and the numerical constants in (2.4), (2.8), (4.7), (4.8). These finite algebra checks are not proof certificates; the proofs are the inequalities above and the source-pinned analytic inputs.
