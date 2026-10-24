SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-22T20:16:18Z.
attacking: two-sided quadratic leakage: integrate a bilinear-bank Fourier/rearrangement estimate before taking any reciprocal local minor.

# account02/B04 — square-assisted weighted determinant half-Riesz transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T201618Z-account02-B04-qform-r13`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Corrected scope and the first debt attacked

The full target remains open: for arbitrary independent real original coordinates with probability densities bounded by one and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one dimension-free density bound for `X^T A X`, or give a valid counterexample.

This run attacks the previous B04 debt `QFORM-TWO-SIDED-QUADRATIC-LEAKAGE-ROUTING-v1`. The r12 one-clean-side theorem allowed arbitrary rank and cross-direction misalignment but required one physical bank to enter linearly. The present argument removes that analytic clean-side condition whenever a residual physical cross cut carries sufficiently many aggregate singular directions. Both banks may contain arbitrary quadratic leakage, and all additional coordinates and couplings remain present.

No step below uses law-uniform pointwise Fresnel decay, independence after spectral rotation, arbitrary-joint coarea, a positive conditional projection-density moment, a worst conditional scalar density cap, a uniformly good physical principal minor, or a single rank-two Schur extraction. Those interfaces are all excluded by the current correction ledger.

The Fourier input actually used is the source-pinned regularized determinant theorem

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

Its relevant statement is: for a quadratic form `R(Y)` and a disjoint ORIGINAL-coordinate cut `I,J` with physical cross block `B`, for `1<=q<2`, if the coordinate diagonal of the projection onto `range(B)` on one cut side is at most `q/2`, then

`|phi_R(t)| <= det(I + 2q t^2 B B^T/(pi^2 e^2))^(-1/(4q))`;     (1.1)

for `q=2`, the same formula with `2q=4` holds with no leverage hypothesis. Arbitrary self quadratic terms, outside couplings and induced affine terms are allowed. This is a joint product-space estimate; it is not a scalar pointwise oscillatory-decay assertion.

## 2. A Fourier representation of the half-Riesz kernel

We first record the weighted-integral interface needed after a physical scalar square is completed.

### Lemma 2.1 — Abel-regularized half-Riesz estimate

Let `T` be any real random variable with characteristic function `phi_T`. If

`integral_R |t|^(-1/2) |phi_T(t)| dt < infinity`,                 (2.1)

then, for every real `x`,

`E |T-x|^(-1/2)`
` <= (1/sqrt(2 pi)) integral_R |t|^(-1/2)|phi_T(t)| dt`.        (2.2)

#### Proof

For `eps>0` set

`K_eps(y)=sqrt(2/pi) integral_0^infinity exp(-eps t) cos(ty) t^(-1/2) dt`.

The Laplace integral gives

`K_eps(y)=sqrt(2) Re (eps-i y)^(-1/2) >=0`,                     (2.3)

and `K_eps(y)->|y|^(-1/2)` for every `y!=0`, while both sides diverge at `y=0`. Fatou and Fubini therefore give

`E|T-x|^(-1/2)`
` <= liminf_(eps->0) E K_eps(T-x)`
` <= sqrt(2/pi) integral_0^infinity t^(-1/2)|phi_T(t)|dt`,

which is (2.2). QED.

This is an integrated Fourier statement. It neither asserts nor requires a law-uniform pointwise decay for a one-dimensional square transform.

## 3. Main theorem: a scalar square plus arbitrary two-sided leakage

Let `Z` be one original input coordinate and let `Y` denote all remaining original coordinates, so `Z` is independent of `Y` and has density at most one. Let `a!=0`, let `d(Y)` be any measurable finite shift, and let `R(Y)` be a real quadratic-plus-affine form. Define

`Q = a (Z+d(Y))^2 + R(Y)`.                                     (3.1)

Choose a disjoint original-coordinate cut `I,J` inside the `Y` variables and let `B` be the cross block of the quadratic part of `R` across that cut.

For `1<=q<2`, assume

`max_i (P_range(B))_(ii) <= q/2`                               (3.2)

on one cut side; for `q=2`, impose no leverage condition. Define

`J_q(B) = (1/sqrt(2 pi)) integral_R |t|^(-1/2)
          det(I+2q t^2 B B^T/(pi^2 e^2))^(-1/(4q)) dt`.        (3.3)

### Theorem 3.1 — `QFORM-SQUARE-WEIGHTED-DETERMINANT-HALFRIESZ-v1`

Whenever `J_q(B)<infinity`, the law of `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= |a|^(-1/2) J_q(B).`                (3.4)

In particular, if `B` has at least `r` singular values at least `sigma>0` and

`r>q`,                                                                  (3.5)

then

`boxed:
 ||p_Q||_infinity <= C_(r,q) / sqrt(|a| sigma),`               (3.6)

where

`C_(r,q)=sqrt(e/2) (2q)^(-1/4)
          Beta(1/4, r/(4q)-1/4).`                              (3.7)

For `q=2`, three physical cross singular directions suffice with **no leverage condition**:

`boxed:
 ||p_Q||_infinity
 <= [sqrt(e)/2 * Beta(1/4,1/8)] / sqrt(|a| sigma)
 = 9.499315272418066... / sqrt(|a| sigma).`                    (3.8)

For `q=1`, two directions suffice under range leverage at most `1/2`:

`||p_Q||_infinity <= 7.270461147134127... / sqrt(|a| sigma).`  (3.9)

#### Proof

Conditional on `Y=y`, the only random source left is `Z`. For either sign of `a`, the density of `a(Z+d(y))^2` obeys the translation-uniform envelope

`p_(a(Z+d)^2)(u) <= |a|^(-1/2)|u|^(-1/2)`                     (3.10)

on the appropriate output half-line and is zero on the other half-line. Hence the mixture density of (3.1) satisfies

`p_Q(x) <= |a|^(-1/2) E |R(Y)-x|^(-1/2).`                     (3.11)

Apply Lemma 2.1 to `T=R(Y)`, then apply the regularized determinant estimate (1.1). This gives (3.4).

If `B` has `r` singular values at least `sigma`, discard all other determinant factors, each of which is at least one. Thus

`|phi_R(t)| <= (1+beta t^2)^(-r/(4q))`,
`beta=2q sigma^2/(pi^2 e^2)`.                                  (3.12)

The weighted time integral is explicit:

`integral_R |t|^(-1/2)(1+beta t^2)^(-r/(4q)) dt`
` = beta^(-1/4) Beta(1/4, r/(4q)-1/4)`,                       (3.13)

which is finite exactly when `r>q`. Since

`beta^(-1/4)/sqrt(2pi)
 = sqrt(e/2)(2q)^(-1/4) sigma^(-1/2)`,                         (3.14)

(3.6)-(3.9) follow. QED.

### What this pays

The source theorem has already absorbed arbitrary self phases on **both** sides of the cut before the absolute value is taken. Therefore Theorem 3.1 has no quadratically-clean-side hypothesis. The square shift `d(Y)` may reuse every residual variable. Extra residual eigenvalues and arbitrarily small cross singular directions stay present and do not produce a determinant-denominator loss.

At the unconditional `q=2` endpoint, `r=2` is exactly critical for this **absolute weighted determinant envelope**: its right side behaves like `|t|^-1` after the `|t|^-1/2` weight and is logarithmically nonintegrable. This is a limitation of this sufficient estimate, not a counterexample to QFORM and not a claim that two-direction residuals are uncontrolled by other mechanisms.

## 4. Scalar-Schur corollary in an arbitrary matrix

For an arbitrary symmetric physical matrix choose an original coordinate `i` with `a=A_ii!=0` and write

`A = [[a,b^T],[b,C]]`.

Then, without rotating the inputs,

`X^T A X = a (X_i + b^T X_(-i)/a)^2
          + X_(-i)^T S X_(-i)`,                               (4.1)

where

`S=C-bb^T/a`.                                                   (4.2)

Thus any original-coordinate cross cut of this Schur residual satisfying Theorem 3.1 gives the same density bound. This is the direct full-matrix interface: the scalar completion creates a correlated shift, but the translation-uniform square kernel handles it; arbitrary quadratic leakage inside both residual banks is then handled by the joint regularized determinant estimate.

This does **not** prove that every matrix with `s_3(A)>=1` has a scalar pivot and a residual cut with `r>q` at uniform scale. That structural routing remains open.

## 5. Explicit genuinely rotated indefinite full-rank target form

Let

`H=(1/3)[[1,2,2],[2,1,-2],[2,-2,1]]`,
`B=2H`,
`C=(3/10) I_3`,
`D=-(2/5) I_3`,
`u=(1,1,1)/sqrt(3)`,
`eta=1/5`.

The matrix `H` is symmetric orthogonal, so all three singular values of `B` are exactly `2`, while every entry of `B` is nonzero. On original coordinates `(z,x_1,x_2,x_3,y_1,y_2,y_3)`, take

`Q=(z+eta u^T x)^2 + x^T Cx + 2x^TBy + y^T D y`.              (5.1)

Equivalently its physical matrix has

- scalar entry `A_zz=1`,
- dense `z-x` coupling `eta u`,
- `x-x` block `C+eta^2 uu^T`,
- dense cross block `B`,
- nonzero `y-y` block `D`.

Thus it is not diagonal in the independent coordinates; both physical banks carry quadratic leakage, the completed square shift reuses a bank variable, and the form is indefinite.

After completing the `z` square, the residual is

`S=[[C,B],[B,D]]`.                                               (5.2)

Because `H` is orthogonal and symmetric, `S` is orthogonally similar (only for the deterministic spectral check) to three `2x2` blocks

`[[3/10, +/-2],[+/-2,-2/5]]`,                                  (5.3)

whose eigenvalues are

`(-1 +/- sqrt(1649))/20`.                                       (5.4)

To verify the **full** seven-dimensional target without assuming any probabilistic independence after this rotation, compare its matrix with `diag(1,S)`. Their difference is supported on `span(z,u)` and has matrix

`[[0,1/5],[1/5,1/25]]`,                                        (5.5)

so its operator norm is

`(1+sqrt(101))/50`.                                             (5.6)

The third singular value of `diag(1,S)` is `(sqrt(1649)+1)/20`; Weyl's singular-value perturbation inequality therefore gives

`s_3(A) >= (sqrt(1649)+1)/20 - (sqrt(101)+1)/50`
`       = 1.859396538002277... >1`.                             (5.7)

This is a genuine target instance. Apply Theorem 3.1 with `a=1`, `q=2`, `r=3`, `sigma=2`. Uniformly over **all** admissible independent cap-one input laws,

`boxed:
 ||p_Q||_infinity <= 9.499315272418066/sqrt(2)
                   = 6.717030245755751... .`                   (5.8)

The finite checker saved with this report gives the full spectrum

`(-2.080394050425,-2.080394050425,-2.069277976784,
  0.982235081429,1.980394050425,1.980394050425,2.027042895355)`.

The numerical spectrum is only a check; (5.7) is the rigorous target certificate.

## 6. Named partner account03/B04 applied at the critical two-direction boundary

The latest completed designated-partner result visible at the fresh prepublication lookup is account03/B04 r17:

`yspennstate/math-open-problems@77c5654ee92f27e444b650ee1635c868af5f76c9`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T195110Z-r17/REPORT.md`.

Its theorem `QFORM-BANKED-SCHUR-HALFRIESZ-v1` states that, for a scalar square coupled to two disjoint aggregate product-bank projections with an invertible `2x2` residual bank matrix,

`||p_Q||_infinity
 <=16 sqrt(60)|a|^(-1/2) sigma_bank^(-1/2)|det B_2|^(-1/4)`.   (6.1)

This is complementary to Theorem 3.1 precisely where the unconditional absolute weighted determinant route is critical.

For disjoint normalized aggregate bank variables `U,V` set

`Q_crit=3[(Z+U)^2+U^2+2UV-V^2]`.                               (6.2)

On the active `(Z,U,V)` span the matrix is

`3[[1,1,0],[1,2,1],[0,1,-1]]`,                                (6.3)

whose eigenvalues are approximately

`(-4.028769248332,1.587949740387,8.440819507945)`,              (6.4)

so all three have modulus greater than one. In original coordinates `U,V` may be normalized averages of arbitrarily large disjoint banks, so individual coefficients can vanish.

Apply the partner theorem with

`a=3`, `sigma_bank=1`, `B_2=3[[1,1],[1,-1]]`, `|det B_2|=18`.

It gives the actual target-level inequality

`boxed:
 ||p_(Q_crit)||_infinity
 <= 16 sqrt(60)/(sqrt(3) 18^(1/4))
 = 34.73896332974030... .`                                     (6.5)

The natural physical `U-V` cross packet here has only one cross singular direction, so Theorem 3.1 does not subsume this estimate. The partner result is therefore used as a genuine complementary endpoint, not cited decoratively.

## 7. Revised first unpaid implication

The analytic two-sided-quadratic-leakage obstruction from r12 is now paid whenever, after a product-preserving scalar completion, one residual physical cut has more than `q` quantitatively large cross singular directions at the corresponding leverage level. The exact two-bank invertible residual packet is paid by account03/B04 r17; the rank-one square/hyperbolic packet is paid by its preceding r16 result and other existing pair/ridge branches.

The first remaining implication is therefore

**`QFORM-CROSS-RANK-LE2-FULL-LEVERAGE-ROUTING-v1`.** Given arbitrary symmetric `A` with `s_3(A)>=1`, prove that every unresolved scalar-Schur residual either

1. has an original-coordinate cut satisfying Theorem 3.1 with a universal reciprocal scale `(|a| sigma)^(-1/2)`, or
2. admits a product-preserving exact/aggregate two-bank or rank-one packet controlled by the completed partner/pair/ridge/diffuse mechanisms,

without selecting a vanishing local minor; and handle the zero/near-zero physical scalar-pivot branch in the same exhaustive reduction.

In particular, generic high-leverage residual cuts carrying at most two large cross singular directions remain the structural frontier. The theorem proved here is not a full-QFORM proof and no full-solution status is claimed.

## 8. Integrity and status

- Full QFORM: `OPEN`.
- New result: `ESSENTIAL_STEP_APPLIED`, supporting theorem proved conditional on the source-pinned regularized determinant theorem.
- Named partner: account03/B04 r17 applied to (6.2)-(6.5).
- Input laws: arbitrary independent original-coordinate densities bounded by one; no moments, support, smoothness, connectedness or identical-law assumptions.
- No post-rotation independence is used. Spectral rotations appear only in deterministic eigenvalue checks.
- Pointwise scalar Fresnel decay is not used.
- Arbitrary-joint coarea and worst conditional-density gates are not used.
- Essential bounded density is established in the stated branches; continuity is not claimed by the new half-Riesz transfer.
- Repository access is durable source transport, not verified native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
