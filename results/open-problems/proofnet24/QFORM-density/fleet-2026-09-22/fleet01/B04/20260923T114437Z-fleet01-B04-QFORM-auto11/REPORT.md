SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T11:44:37Z.
attacking: lift translation-uniform hyperbolic-square smoothing to three disjoint original-coordinate product banks, preserving the one-sided curvature H(T), then compare it on one delocalized target family with fleet02/B04's rank-one-bank Holder transfer.

# fleet01/B04 — aligned aggregate hyperbolic-square C0/Fourier-L2 compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T114437Z-fleet01-B04-QFORM-auto11`  
**Fresh owner control before publication:** revision `2026-09-22.15`; QFORM only.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`.  
**Continuity:** proved for the branch below (`C_0` representative); full-target continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-match pivot and exact new scope

I first checked the existing three-bank literature in the fleet before claiming novelty.

1. fleet03/B04 already proved `QFORM-SQUARE-HYPERBOLIC-THREEBANK-v1` at `yspennstate/math-open-problems@f8c400b6278ed70e1bf3eb9b7d0ccf4920f1cb06`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260922T215045Z-r19/REPORT.md`. It allows an aggregate square whose center can overlap both hyperbolic variables, but its residual after square completion must be independent of the active hyperbolic banks; it gives essential boundedness through an L6/half-Riesz route and does not claim continuity.

2. fleet01/B09 already proved the physical-square theorem `QFORM-THREEBANK-SQUARE-HYPERBOLIC-v1` at `yspennstate/math-open-problems@19a5e6e88d2d5756ebd92e85b00122ec0bdec699`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/B09-20260922T164451Z-r14/REPORT.md`. Its square variable is one original physical coordinate.

3. fleet02/B10 proved the scalar translation-uniform theorem `QFORM-HYPERBOLIC-SQUARE-v1` at `yspennstate/math-open-problems@1eba911614ef9f6683f8eacb5d6608a0f9a4b833`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T1147Z-qform-rank3-coupled-B10-r1/REPORT.md`: for independent cap-one scalars X,Y,Z,

`T=2aXY+H(Y)+b(Z+theta(Y))^2`, `ab!=0`,

one has `||p_T||_infinity <=4/sqrt(|ab|)`.

4. My earlier B04 run upgraded that scalar theorem to `p_T in C_0` and

`int |phi_T(t)|^2 dt <=8 pi/sqrt(|ab|)`

at `yspennstate/math-open-problems@5efc99f63966f32da63506320c424e1ccbe47f81`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T085400Z-fleet01-B04-QFORM-auto11/REPORT.md`.

The new scope here is the intersection not covered by those existing three-bank endpoints: **the square itself is a delocalized original-coordinate bank projection, while the post-completion residual may retain arbitrary measurable curvature `H(T)` in one of the hyperbolic aggregate variables.** This one-sided leakage is exactly allowed by the scalar B10 theorem but not by the older overlap-safe aggregate theorem. The proof is an exact density-cap rescaling plus the completed fleet02/B04 projection theorem; no new pointwise oscillatory decay is asserted.

The newest designated-partner handoff was also read: fleet02/B04's `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1` (brain handoff commit `6bee170a82a1252e22b2a10c6ff6466b5baaa802`, canonical math report bundle tail `febf0c97f0f85e802b6bc2ab4a475c15109de013`). It closes the exact support-infeasible third-volume branch. The present run therefore does not duplicate that support branch; it pays a low-rank aligned-bank endpoint where third-volume currency need not be the natural certificate.

## 2. General density-cap scaling of hyperbolic-square smoothing

### Lemma 2.1 — `QFORM-HYPERBOLIC-SQUARE-GENERAL-CAPS-C0-v1`

Let X,Y,Z be independent real random variables having probability densities bounded by finite positive numbers `M_X,M_Y,M_Z`. Let `a,b` be nonzero real numbers and let `H,theta:R->R` be arbitrary measurable functions. Put

`T=2aXY+H(Y)+b(Z+theta(Y))^2`.

Then T has a representative `p_T in C_0(R)` and

`boxed:
 ||p_T||_infinity
 <= 4 M_Z sqrt(M_X M_Y) / sqrt(|ab|).
`                                                               (2.1)

Moreover, with `phi_T(t)=E exp(itT)`, 

`boxed:
 int_R |phi_T(t)|^2 dt
 <= 8 pi M_Z sqrt(M_X M_Y)/sqrt(|ab|).
`                                                               (2.2)

#### Proof

Define

`X'=M_X X`, `Y'=M_Y Y`, `Z'=M_Z Z`.

Their densities are bounded by one. Rewriting T in the primed variables gives

`T = 2 a' X'Y' + H'(Y') + b'(Z'+theta'(Y'))^2`,

where

`a'=a/(M_X M_Y)`, `b'=b/M_Z^2`,
`H'(y)=H(y/M_Y)`,
`theta'(y)=M_Z theta(y/M_Y)`.

Apply the completed scalar `C_0` hyperbolic-square theorem to obtain

`||p_T||_infinity <=4/sqrt(|a'b'|)
 =4 M_Z sqrt(M_XM_Y)/sqrt(|ab|)`,

and `p_T in C_0`. Since p_T is a probability density,

`||p_T||_2^2 <= ||p_T||_infinity ||p_T||_1 <= ||p_T||_infinity`.

Plancherel with the convention above gives

`int |phi_T|^2 =2pi ||p_T||_2^2`,

which proves (2.2). QED.

This is an integrated Fourier statement, not a law-uniform pointwise decay estimate.

## 3. New aggregate theorem over three disjoint product banks

Let `I,J,K` be pairwise disjoint sets of ORIGINAL independent coordinates. Put

`S=c^T X_I`, `T=d^T X_J`, `U=e^T X_K`,

where `c,d,e` are nonzero. The completed fleet02/B04 product-projection theorem gives

`||p_S||_infinity <= sqrt(2)/||c||_2`,
`||p_T||_infinity <= sqrt(2)/||d||_2`,
`||p_U||_infinity <= sqrt(2)/||e||_2`.                         (3.1)

Because the banks are disjoint, S,T,U are genuinely independent; no spectral rotation of the random vector is used.

### Theorem 3.1 — `QFORM-ALIGNED-THREEBANK-HYPERBOLIC-SQUARE-C0-v1`

Let `a,b!=0` and let `H,theta` be arbitrary measurable functions. For

`Q = 2a S T + H(T) + b[U+theta(T)]^2`,                         (3.2)

every admissible cap-one product input law satisfies

`boxed:
 ||p_Q||_infinity
 <= 8 / [ ||e||_2 sqrt(||c||_2||d||_2) sqrt(|ab|) ].
`                                                               (3.3)

The density has a representative in `C_0(R)`, and

`boxed:
 int_R |phi_Q(t)|^2 dt
 <= 16 pi / [ ||e||_2 sqrt(||c||_2||d||_2) sqrt(|ab|) ].
`                                                               (3.4)

Equivalently, define the aggregate spectral currencies

`Lambda_h = |a| ||c||_2 ||d||_2`,
`Lambda_s = |b| ||e||_2^2`.

Then

`boxed: ||p_Q||_infinity <= 8 / sqrt(Lambda_h Lambda_s)`,       (3.5)

`boxed: ||phi_Q||_2 <= 4 sqrt(pi) (Lambda_h Lambda_s)^(-1/4)`. (3.6)

#### Proof

Apply Lemma 2.1 with the three density caps from (3.1). Their exact product is

`M_U sqrt(M_S M_T)
 <= [sqrt(2)/||e||] * sqrt(2/(||c||||d||))
 = 2/[||e|| sqrt(||c||||d||)].`

Substitution in (2.1)-(2.2) gives (3.3)-(3.4). Equations (3.5)-(3.6) are algebraic rewrites. QED.

### Conditional ambient version

Let W be any further disjoint original-coordinate bank. If, after conditioning on W=w, the active dependence can be written

`Q_w=2a[S+s(w)][T+t(w)] + H_w(T+t(w))
    +b[U+theta_w(T+t(w))]^2+r(w)`,                              (3.7)

with the same nonzero a,b and arbitrary measurable shifts/functions, then the same bounds hold. For each fixed w, translations preserve the three density caps and Lemma 2.1 applies. Its L-infinity bound is independent of w. The conditional densities are `C_0`; dominated convergence against the W-law therefore yields a global `C_0` representative with the same bound.

This is the useful ambient form: arbitrary conditioned affine couplings that preserve the displayed rank-one alignment cost nothing.

## 4. Exact application of fleet02/B04 to the same packet

The completed designated-partner report

`yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T181702Z-dac07509/REPORT.md`,

proves `QFORM-RANK1-BANK-HOLDER-LIFT-v1`. If two disjoint aggregate banks have product scale `sigma=||u||_2||v||_2` and, after completing aligned shifts, the independent residual H obeys

`sup_t P(|H-t|<r)<=min(1,K r^alpha)`,

then

`||p_Q||_infinity <= (2/sigma)[1+alpha^(-1) Psi(K sigma^alpha)]`,

where `Psi(x)=x` for `x<=1` and `Psi(x)=1+log x` for `x>=1`.

I apply this theorem in Section 5 to the exact same matrix as the new theorem, so the partner input is used in a real all-input-law inequality rather than merely cited.

## 5. Genuinely rotated indefinite target family

For every `m>=2`, split `3m` original coordinates into three disjoint m-coordinate banks and let

`r_1=r_2=r_3=m^(-1/2)(1,...,1)`

on their respective banks. Put

`S=r_1^T X_I`, `T=r_2^T X_J`, `U=r_3^T X_K`.

Define

`Q_m = 3 S T + (1/2) T U + (3/2) U^2`.                        (5.1)

The physical coefficient matrix is

`A_m = R B R^T`, `R=[r_1 r_2 r_3]`,

with

`B = [[0,3/2,0],
      [3/2,0,1/4],
      [0,1/4,3/2]].`                                           (5.2)

The columns of R are orthonormal. Let

`B_0=[[0,3/2,0],[3/2,0,0],[0,0,3/2]]`.

Its eigenvalues are `-3/2,3/2,3/2`, while `||B-B_0||_op=1/4`. Weyl therefore gives

`lambda_min(B)<=-5/4`, and both positive eigenvalues are `>=5/4`. (5.3)

Hence A_m has exactly three nonzero eigenvalues, all of modulus at least `5/4`; it is a valid instance of the full owner target.

This family is genuinely delocalized in the original coordinates. Every nonzero physical coefficient is at most `3/(2m)` in magnitude, while every nonzero eigenvector has nonzero components in all three aggregate directions and is flat within each occupied bank. Thus no constant-size physical entry survives as `m->infinity`.

### 5.1 New aligned-three-bank estimate

Rewrite (5.1) exactly as

`Q_m = 3ST - T^2/24 + (3/2)(U+T/6)^2`.                        (5.4)

Thus Theorem 3.1 applies with

`a=b=3/2`, `||r_1||=||r_2||=||r_3||=1`,

so `Lambda_h=Lambda_s=3/2`. For every admissible independent product input law,

`boxed: ||p_(Q_m)||_infinity <= 16/3 = 5.333333333333333...`, (5.5)

and `p_(Q_m) in C_0(R)`. The integrated Fourier estimate is

`boxed: int |phi_(Q_m)(t)|^2 dt <= 32 pi/3
       =33.510321638291124...`,                                (5.6)

hence

`||phi_(Q_m)||_2 <= sqrt(32pi/3)
 =5.788810036466141...`.                                       (5.7)

### 5.2 Partner theorem on the identical matrix

Apply fleet02/B04's rank-one-bank Holder theorem with the first aggregate coefficient absorbed into its bank vector:

`U_1=(3/2)S`, `V_1=T`, `W=K`.

Then (5.1) is

`Q_m=2U_1V_1+2V_1 L_2(W)+R(W)`,

where

`L_2(W)=U/4`, `R(W)=(3/2)U^2`, `L_1=0`.                       (5.8)

The partner aggregate scale is

`sigma=||(3/2)r_1|| ||r_2||=3/2`.                              (5.9)

By the same fleet02/B04 projection theorem, `U=r_3^T X_K` has density cap at most `sqrt(2)`. The elementary square small-ball estimate therefore gives, uniformly in t,

`P(|(3/2)U^2-t|<r)
 <= min{1, [4/sqrt(3/2)] r^(1/2)}.`                            (5.10)

Thus the partner theorem has `alpha=1/2`, `K=4/sqrt(3/2)`, and

`K sigma^alpha=4`.                                             (5.11)

Its actual same-matrix all-input-law estimate is therefore

`boxed:
 ||p_(Q_m)||_infinity
 <= (4/3)[3+2 log 4]
 =7.696784962986375... .
`                                                               (5.12)

The new aligned-square theorem improves this exact partner certificate by the factor

`[(4/3)(3+2log4)]/(16/3)
 =(3+2log4)/4
 =1.4431471805599454...`,                                      (5.13)

and additionally proves a continuous `C_0` representative and the Fourier-L2 estimate (5.6).

This comparison also shows why the new route is not merely a restatement of the partner theorem: the partner pays the logarithmic hyperbolic kernel against a separate square small-ball modulus, while the new proof uses the stronger translation-uniform scalar hyperbolic-square rearrangement before lifting all three scalars to product-bank projections.

## 6. Relation to existing three-bank half-Riesz theorem

The fleet03/B04 aggregate theorem permits a square shift depending on both hyperbolic variables but, after the square is exposed, does not include an arbitrary residual `H(T)` living on an active hyperbolic bank. Formula (5.4) has exactly such a residual, `H(T)=-T^2/24`. The present theorem pays that one-sided curvature leakage because B10's scalar rearrangement is uniform over arbitrary measurable H(T).

Conversely, this run does **not** claim the stronger overlap-safe dependence `theta=theta(S,T)` handled by fleet03/B04. The two mechanisms are complementary. The present result is a sharper and regularity-improving endpoint when the square shift is aligned with a single hyperbolic aggregate.

## 7. What remains unpaid

The full QFORM conjecture remains OPEN. The new theorem does not show that every matrix with three large eigenvalues can be decomposed into three disjoint original-coordinate rank-one banks satisfying (3.7). Current corrections rule out several naive local extraction principles, and additional same-bank curvature or a second misaligned cross singular direction cannot be deleted merely because its coefficient is small.

The next exact implication is

`QFORM-ALIGNED-THREEBANK-OR-MULTIDEFECT-ROUTING-v1`:

> Starting only from `s_3(A)>=1`, obtain a product-preserving disjoint-bank packet with `Lambda_h Lambda_s >= c_0` in the scope of Theorem 3.1, or prove that failure forces a quantitatively paid weighted-third-volume, ridge, grouped-rank-two, hub, pair-log, or multi-defect endpoint without paying a reciprocal vanishing physical coefficient.

The newest fleet02/B04 support-defect theorem pays exact infeasibility of the strict third-volume support gate. The remaining global obstruction is quantitative higher-rank/multi-defect routing, not the aligned bank analytic endpoint proved here.

## 8. Integrity and status

No Gaussianity, log-concavity, moments, compact support, connected support, post-rotation independence, pointwise quadratic-phase decay, arbitrary-joint coarea estimate, conditional fiber supremum, or Monte Carlo extremality assertion is used. The finite spectral computation below is only a check of the explicit example, not evidence for the universal theorem.

**Final status:** `QFORM-ALIGNED-THREEBANK-HYPERBOLIC-SQUARE-C0-v1` proved as a supporting theorem; explicit target-valid delocalized family proved with cap `16/3` and `C_0` density; designated fleet02/B04 theorem applied to the same family with cap `(4/3)(3+2log4)`; full QFORM and full-target continuity remain OPEN.
