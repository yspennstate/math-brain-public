SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-24T06:30:07Z.
attacking: pair-completion cross collapse; prove a stronger universal one-decoupling quadratic concentration bound, retain the Schur third-curvature resource, and average the physical-pair logarithmic singularity.

# account03/B01 — square-root-log quadratic concentration and cross-collapse payment

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T063007Z-account03-B01-qform-auto11-r46`  
Role: Oscillatory replacement / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW UNIVERSAL DISTRIBUTION-FUNCTION THEOREM + NEW PHYSICAL-PAIR DENSITY RECEIVER / FULL QFORM OPEN**

## 1. Scope and correction boundary

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `0<=f_i<=1`. No moment, compact-support, connected-support, Gaussian, iid, log-concavity, or smoothness assumption is made. Every conditioning or decoupling below is in the original coordinates. Deterministic singular vectors are used only to estimate coefficient norms; no rotated random coordinates are declared independent.

The owner target assumes a real symmetric `A` with `s_3(A)>=1` and asks for one universal bound on the density of `Q=X^T A X`. The unrestricted conjecture remains OPEN.

The live correction ledger was refreshed. In particular this run does not use law-uniform pointwise quadratic-phase decay, the false arbitrary-joint rank-three coarea bound, conditional projected-density caps, naive fibre suprema, post-rotation independence, or a uniformly good fixed physical minor. The newest two-hub correction also requires retaining genuine third curvature on the indefinite near-null branch; Section 5 below does exactly that through an exact Schur rank-two identity.

## 2. Sources actually used

### 2.1 Designated partner account04/B01

Source:

`yspennstate/math-open-problems@f7e82d169badc671968036252d351b8533cdd425`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260924T012155Z-account04-B01-lr-residual-r1/REPORT.md`.

For independent cap-one original coordinates `U,V`, every `c!=0`, every `1<r<=2`, and arbitrary affine coefficients,

`Z=2cUV+beta U+gamma V+delta`,

account04/B01 proves, with `a_r=(r-1)/r`,

`||p_Z||_r <= 2^(a_r) |c|^(-a_r)`.                              (2.1)

This is applied at an actual inequality in Section 7.

### 2.2 Product linear-form density theorem

The product linear-form cap used below is the programme theorem used in the completed account02/B04 report

`yspennstate/math-open-problems@dfe442ee899867f5677e5ced85a196eca922fe64`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260923T211520Z-account02-B04-qform/REPORT.md`.

If `Z_j` are independent with scalar densities bounded by one and `v` is deterministic, then

`||p_(v dot Z)||_infinity <= sqrt(2)/||v||_2`.                   (2.2)

The same applies to coordinatewise differences `Z_j-Z_j'`, since their densities remain at most one.

### 2.3 Logarithmic physical-pair theorem

Source:

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

For an invertible indefinite original-coordinate `2x2` pair `P`, let

`D=|det P|`, `kappa=sigma_min(P)`.

After completing the pair, if the critical remainder is `R`, then for every cutoff `r_0>0`,

`p_Q(t) <= 2sqrt(2)/r_0`
` + D^(-1/2) E log_+(2r_0^2/(kappa |t-R|))`.                    (2.3)

The shifts of the pair coordinates may depend arbitrarily on the variables producing `R`.

## 3. Preserve the phase-aligned obstruction

Fix `s!=0` and `eta in (0,pi/2)`. The set

`E={x: dist(sx^2,2pi Z)<=eta}`

has infinite Lebesgue measure: around the roots of `|s|x^2=2pi k` the allowed component lengths are comparable to `k^(-1/2)`, whose sum diverges. Choose a finite union `E_0 subset E` of total measure one and put `f=1_(E_0)`. Then `f` is an admissible probability density and

`Re E exp(i s X^2) >= cos(eta)`.                                 (3.1)

Thus no positive law-uniform pointwise power decay in `|s|` is available. The replacement below is a distribution-function estimate obtained after one product-preserving difference.

## 4. Main new distribution-function theorem

### Theorem 4.1 — `QFORM-UNIVERSAL-QUADRATIC-SQRTLOG-CONCENTRATION-v1`

Let `S` be any nonzero real symmetric matrix, `b` any real vector, `gamma` any real number, and

`R=X^T S X+b^T X+gamma`, `s=||S||_op`.

For every interval `I` of length `h` with `0<h<=s/12`,

`boxed:
 P(R in I)
 <= sqrt(12(h/s)[1+log(s/(12h))]).
}`                                                                    (4.1)

For `h>s/12` use the trivial bound one.

Consequently, for every fixed `0<alpha<1/2`, all `h>0` satisfy

`boxed:
 P(R in I) <= C_alpha (h/s)^alpha,
 C_alpha=(12/e)^alpha / sqrt(1-2alpha).
}`                                                                    (4.2)

This allows arbitrary affine terms and all signs/ranks of `S`.

### Proof

Split into two exhaustive original-coordinate cases.

**Case A: a physical diagonal is large.** If some `|S_ii|>=s/3`, condition on all other original coordinates. The remaining map in `X_i` is

`a x^2+d x+e`, `|a|>=s/3`.

For every output interval of length `h`, completing the square shows that its inverse image has total Lebesgue length at most `2 sqrt(h/|a|)`. Since the conditional input density is bounded by one,

`P(R in I | X_{-i}) <= 2sqrt(3h/s)=sqrt(12h/s)`,               (4.3)

which is at most (4.1).

**Case B: every physical diagonal is small.** Assume `max_i|S_ii|<s/3`. Write `S=D+O`, with `O` zero diagonal. The sign-cut identity from the earlier B01 run gives a literal partition of the original coordinates `I_0 disjoint_union J_0` for which the physical cross block

`B=S[I_0,J_0]`

satisfies

`sigma=||B||_op >= s/3`.                                        (4.4)

Write the two original-coordinate banks as `Y=X_{I_0}`, `Z=X_{J_0}`. Then

`R=F(Y)+2Y^T B Z+G(Z)`                                         (4.5)

where affine terms have been absorbed into `F,G`.

Let `Y'` be an independent copy of `Y` and set `p=P(R in I)`. Conditional Cauchy-Schwarz in the `Z` bank gives

`p^2 <= P(|R(Y,Z)-R(Y',Z)|<=h)`.                               (4.6)

Condition on `Y,Y'` and put `U=Y-Y'`. The random difference in (4.6) is a deterministic constant plus the linear form

`2 U^T B Z`.                                                     (4.7)

By (2.2), conditional on `U`,

`P(|R(Y,Z)-R(Y',Z)|<=h | U)`
` <= min(1, sqrt(2)h/||B^T U||_2)`.                            (4.8)

Let `u` be a top left singular vector of `B`. Its top right singular vector is `v`, so the `v`-component of `B^T U` is exactly `sigma (u dot U)`. Hence

`||B^T U||_2 >= sigma |u dot U|`.                              (4.9)

The coordinates of `U` are independent and each has density at most one. Therefore `W=u dot U` has density bounded by `K=sqrt(2)` by (2.2). Put

`a=sqrt(2)h/sigma`, `x=2Ka=4h/sigma`.                          (4.10)

For a scalar probability density bounded by `K`, the expectation of the symmetric decreasing kernel `min(1,a/|w|)` is maximized by the cap-saturated centered interval. Thus, for `x<=1`,

`E min(1,a/|W|) <= x[1+log(1/x)]`;                              (4.11)

for `x>=1`, it is at most one. Since `sigma>=s/3`, when `h<=s/12` we have `x<=12h/s<=1`, and `x(1+log(1/x))` is increasing on `(0,1]`. Therefore

`p^2 <= 12(h/s)[1+log(s/(12h))]`,                              (4.12)

which proves (4.1).

For (4.2), write `z=12h/s=e^{-q}`. Dividing the right side of (4.1) by `(h/s)^alpha` gives

`12^alpha exp(-(1/2-alpha)q) sqrt(1+q)`.                        (4.13)

Its maximum for `q>=0` is attained at

`q=2alpha/(1-2alpha)`

and equals `(12/e)^alpha/sqrt(1-2alpha)`. For `h>s/12`, the trivial probability bound one is also dominated by the same expression because `e^(-2alpha)>=1-2alpha`. QED.

### Numerical specialization

At `alpha=1/3`,

`C_(1/3)=2.841337885233845...`.                                 (4.14)

This strictly strengthens the previous B01 `h^(1/8)` universal quadratic concentration result: the new estimate reaches every fixed power below `1/2`, with the sharper square-root-log form (4.1) retained.

## 5. Exact third-curvature persistence after any invertible physical pair

### Lemma 5.1 — `QFORM-PAIR-SCHUR-S3-PERSISTENCE-v1`

Reorder an arbitrary invertible physical `2x2` principal pair to the final coordinates and write

`A=[[C,K],[K^T,P]]`,

with `P` invertible. Let

`S=C-KP^(-1)K^T`.                                               (5.1)

Then

`boxed: ||S||_op >= s_3(A).`                                    (5.2)

### Proof

There is an exact additive decomposition

`A = diag(S,0_2) + R_2`,                                       (5.3)

where

`R_2=[[KP^(-1)K^T,K],[K^T,P]]`
`   =[K;P] P^(-1) [K^T,P]`.                                    (5.4)

Therefore `rank R_2<=2`. By Eckart-Young,

`s_3(A)=inf_{rank R<=2} ||A-R||_op <= ||diag(S,0_2)||_op=||S||_op`.  (5.5)

QED.

This is exactly the curvature resource required by the live correction: the third singular direction is not discarded when the indefinite pair is completed.

## 6. Main new density receiver for an indefinite physical pair

### Theorem 6.1 — `QFORM-INDEFINITE-PAIR-THIRDCURVATURE-v1`

Assume an original-coordinate physical pair `P` is invertible and indefinite. Put

`D=|det P|`, `kappa=sigma_min(P)`, `lambda=s_3(A)>0`.

Then `Q=X^TAX` has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= 14.180833 D^(-3/10) (kappa lambda)^(-1/5).
}`                                                                    (6.1)

No post-completion cross block, source-disjoint residual, moment, or support hypothesis is required.

### Proof

Complete the physical pair. Its critical remainder is a quadratic-plus-affine function of the remaining original coordinates with Hessian equal to the Schur complement `S` in (5.1). By Lemma 5.1,

`||S||_op>=lambda`.                                             (6.2)

Apply Theorem 4.1 in its power form with `alpha=1/3`. For a symmetric interval of radius `rho` (length `2rho`),

`P(|R-t|<rho)
 <= H rho^(1/3)`,
`H=2^(1/3) C_(1/3) lambda^(-1/3)
 =3.579861411469905... lambda^(-1/3)`.                         (6.3)

For every `A_0>0`, layer cake gives

`E log_+(A_0/|t-R|)`
` = integral_0^infinity P(|t-R|<A_0 e^(-v)) dv`
` <= (H/alpha) A_0^alpha`, `alpha=1/3`.                         (6.4)

Insert `A_0=2r_0^2/kappa` into the physical-pair envelope (2.3):

`p_Q(t) <= 2sqrt(2)r_0^(-1)`
` + D^(-1/2)(H/alpha)2^alpha kappa^(-alpha)r_0^(2alpha)`.       (6.5)

For general `0<alpha<1/2`, minimizing `A r^(-1)+B r^(2alpha)` yields

`(1+2alpha)(2alpha)^(-2alpha/(1+2alpha))`
` * A^(2alpha/(1+2alpha)) B^(1/(1+2alpha))`.                   (6.6)

At `alpha=1/3`, after substituting (6.3), the constant is

`14.18083262050194...`,                                         (6.7)

and the scale factors are exactly `D^(-3/10)(kappa lambda)^(-1/5)`. This proves (6.1). Homogeneity is correct: `D` scales quadratically and `kappa,lambda` linearly, so the total scale exponent is `3/5+2/5=1`. QED.

For a definite invertible physical pair the existing elementary ellipse argument gives the separate bound `pi/sqrt(D)`, so every fixed invertible physical pair is analytically payable; the unresolved issue is obtaining a dimension-free aggregate physical certificate under only `s_3(A)>=1`.

## 7. The previous cross-collapse interface is paid

For a zero-diagonal hyperbolic physical pair

`P=[[0,c],[c,0]]`, `c!=0`,                                    (7.1)

we have `D=c^2` and `kappa=|c|`. Theorem 6.1 gives

`boxed:
 ||p_Q||_infinity
 <=14.180833 |c|^(-4/5) s_3(A)^(-1/5).
}`                                                                    (7.2)

In particular, under the owner target `s_3(A)>=1`,

`||p_Q||_infinity <=14.180833 |c|^(-4/5)`.                     (7.3)

This contains **no factor involving the post-completion hub-bank block**

`B_*=B-(a m^T+b ell^T)/(2c)`

from the preceding B01 run. Hence the exact case `B_*=0` and the entire near-collapse limit are no longer an analytic singularity. The prior local interface `QFORM-PAIR-COMPLETION-CROSS-COLLAPSE-v1` is paid whenever the physical hyperbolic pair itself is nonzero.

A useful numerical consequence in the previously isolated small-diagonal/large-edge chamber is: if `|A_ij|>=1/32` and both associated diagonal magnitudes are `<1/64`, then the pair is indefinite with

`D>=3/4096`, `kappa>=1/64`.

Under `s_3(A)>=1`, (6.1) yields

`||p_Q||_infinity <284.125`,                                    (7.4)

improving the prior B01 `<463` payment for that chamber.

## 8. Actual account04/B01 partner application: integrated frequency control

Still in the hyperbolic pair configuration (7.1), condition on every other original coordinate. The full quadratic form has the conditional shape

`2cUV+beta(W)U+gamma(W)V+delta(W)`.                              (8.1)

Apply account04/B01 (2.1) pointwise in `W`, then Minkowski. For every `1<r<=2`,

`boxed:
 ||p_Q||_r <=2^((r-1)/r)|c|^(-(r-1)/r).
}`                                                                    (8.2)

At `r=2`,

`||p_Q||_2 <=sqrt(2)|c|^(-1/2)`.                                (8.3)

Plancherel therefore gives the averaged-frequency estimate

`boxed:
 integral_R |phi_Q(t)|^2 dt <=4pi/|c|.
}`                                                                    (8.4)

Thus the same fully entangled pair that may have no pointwise decay still has a uniform integrated Fourier budget. Combining (8.4) with Cauchy-Schwarz on the triangular frequency window gives, for

`D_T mu(y)=(1/(2pi)) int_{-T}^T (1-|t|/T) Re(e^(-ity)phi_Q(t))dt`,

`boxed:
 sup_y |D_T law(Q)(y)| <= sqrt(2T/(3pi|c|)).
}`                                                                    (8.5)

The bounded endpoint (7.2), rather than the growing right side of (8.5), comes from retaining the third Schur curvature and averaging the logarithmic pair singularity.

## 9. Exact cross-collapse target witness

Take three original coordinates with

`A=[[1,0,0],[0,0,1],[0,1,0]]`.                                  (9.1)

Its eigenvalues are exactly `{-1,1,1}`, so it meets the owner target with equality. Completing the physical pair `(2,3)` leaves the scalar Schur remainder `[1]` and the post-completion cross block is exactly zero. Theorem 6.1 gives

`||p_Q||_infinity <=14.180833`                                  (9.2)

for every admissible product input law. This is only a scope witness, not evidence for the unrestricted structural reduction.

## 10. What remains

The new result removes the **analytic** cross-collapse obstruction after any nonzero invertible indefinite physical pair. It does not produce a uniformly conditioned pair from the bare spectral hypothesis. Families with spectral mass spread over many weak physical couplings can have every available local `D` or `kappa` tending to zero, and some exact structured families have no useful invertible pair at all.

The next B01 implication is therefore

`QFORM-AGGREGATE-PAIR-CURRENCY-BEFORE-INVERSION-v1`:

> Under `s_3(A)>=1`, aggregate many weak original-coordinate pair currencies before paying the new receiver (6.1), or route the complementary configuration to an already proved grouped-cross, grouped-square, three-hub, ridge, or fifth-volume endpoint. A single uniformly good minor must not be assumed.

The universal concentration theorem (4.1) is available as a new residual receiver in that aggregation problem.

## 11. Verification and status

The sibling deterministic checker verifies the constants, scaling, the exact Schur rank-two decomposition, `s_3(A)<=||S||_op` on 1000 seeded algebraic stress matrices, and the exact target witness. `CHECKS.txt` ends `STATUS=PASS`. These are algebraic checks, not numerical evidence for the universal density statement.

Continuity: Theorem 4.1 is only a distribution-function statement. Theorem 6.1 establishes essential boundedness through the pair-log density construction; it does **not** establish a continuous representative. Global continuity remains OPEN.

Full QFORM: OPEN. The results in this report are new supporting arguments pending independent review.
