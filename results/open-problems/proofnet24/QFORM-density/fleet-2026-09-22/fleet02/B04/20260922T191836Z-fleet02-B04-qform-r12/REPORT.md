SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-22T19:18:36Z.
attacking: product-space aggregation for the near-isotropic/off-diagonal branch via two-coordinate logarithmic smoothing and integrated overlap mass.

# fleet02/B04 — one-sided bilinear-bank Lp smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T191836Z-fleet02-B04-qform-r12`  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and first unpaid implication

The full target remains open: for independent real physical coordinates with densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension-free density bound for `X^T A X`, or produce a true target-level counterexample.

Fresh owner control was revision `2026-09-22.13`. The live correction ledger was read before the proof. In particular, nothing below uses law-uniform pointwise quadratic Fourier decay, arbitrary-joint coarea, positive conditional projection moments, post-rotation independence, a universal good principal triple, a single Schur extraction, or a constant-size physical mixed entry.

The previous B04 frontier paid an aligned rank-one pair of disjoint original-coordinate banks. The first missing interface was misaligned/multi-direction cross coupling and quadratic leakage. This run removes the rank-one/alignment restriction completely on one side: an arbitrary-rank physical cross block is paid only through its operator norm, while the conditioned bank may carry arbitrary self-quadratic leakage. The remaining obstruction is two-sided quadratic leakage.

Named partner actually applied: fleet03/B04, `QFORM-SQUARE-L32-v1` and its source-valid one-dimensional product-projection estimate, from `yspennstate/math-open-problems@3fd5603c1e86cc028fb4330392f471c2f450cf39`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260922T185416Z-r16/REPORT.md`.

## 2. Rearranged inverse fractional moment

### Lemma 2.1

If a real random variable `T` has density bounded by `M`, then for every `0<alpha<1` and every real `c`,

`E |T-c|^(-alpha) <= (2M)^alpha/(1-alpha)`.                       (2.1)

Proof. Among all probability densities bounded by `M`, the integral against the symmetric decreasing kernel `|t-c|^(-alpha)` is maximized by filling the interval of length `1/M` centered at `c` at height `M`. Therefore

`E |T-c|^(-alpha)
 <= 2M integral_0^(1/(2M)) r^(-alpha) dr
 = (2M)^alpha/(1-alpha)`.

This is a decreasing-rearrangement/bathtub estimate, not a pointwise Fourier estimate.

## 3. Arbitrary-rank bilinear bank in Lp

Let `I,J` be disjoint original-coordinate banks. Write `X_I,X_J` for their independent cap-one coordinates. Let `B` be a nonzero real `|I| x |J|` matrix and put `s=||B||_op`. Let `r(X_I)` be arbitrary measurable and let `b` be a fixed vector on the `J` bank. Define

`H = r(X_I) + 2 X_I^T B X_J + b^T X_J`.                         (3.1)

### Theorem 3.1 — `QFORM-BILINEAR-BANK-LP-OPNORM-v1`

For every `p>1`, `H` has a density `h` satisfying

`boxed: ||h||_p <= p 2^((p-1)/p) s^(-(p-1)/p)`.                (3.2)

Proof. Set `alpha=(p-1)/p`. Conditional on `X_I=x`, the `J`-dependent part is the linear form

`2 (B^T x+b/2)^T X_J`.

The completed one-dimensional product-projection estimate used by fleet03/B04 gives, for every nonzero coefficient vector `w`,

`||p_(w^T X_J)||_infinity <= sqrt(2)/||w||_2`.

Hence the conditional density cap for `2w^T X_J` is at most

`M_x = 1/(sqrt(2)||w||_2)`, `w=B^T x+b/2`.                    (3.3)

A probability density with cap `M_x` has `L^p` norm at most `M_x^alpha`. Choose unit left/right singular vectors `u,v` for the top singular value `s`, so `Bv?` equivalently `B^T u = s v`. Then

`||B^T x+b/2||_2 >= |v^T(B^T x+b/2)| = |s u^T x+c|`            (3.4)

for a scalar `c`. The unit projection `u^T X_I` has density at most `sqrt(2)`, so `s u^T X_I` has density at most `sqrt(2)/s`. Applying Lemma 2.1 gives

`E ||B^T X_I+b/2||^(-alpha)
 <= p 2^(3alpha/2) s^(-alpha)`.                                (3.5)

Multiplying by the factor `2^(-alpha/2)` from (3.3), and using Minkowski on the mixture over `X_I`, yields (3.2). QED.

Remarks. The rank of `B` is arbitrary. Small additional singular directions are retained. The entire self-quadratic or nonlinear term `r(X_I)` is harmless because it is a conditional output translation. What is essential is that the unconditioned `J` bank enters linearly.

## 4. General translated-square endpoint

Let `Z` have density at most one, `a!=0`, and let `d` be deterministic. For `p>2`, put `q=p/(p-1)`. The density `g` of `a(Z+d)^2` obeys the pointwise cap `g(y)<=|a y|^(-1/2)` on the appropriate half-line and has mass one. Filling the highest-cap part of that envelope gives

`boxed:
 ||g||_q
 <= 2^(1/p) ((p-1)/(p-2))^((p-1)/p) |a|^(-1/p).`             (4.1)

At `p=3`, (4.1) becomes exactly the completed partner endpoint

`||g||_(3/2) <= 2 |a|^(-1/3)`.                                (4.2)

Thus the partner theorem is used as an actual endpoint below, not merely cited.

## 5. Main theorem: one clean bilinear side plus a square

Let `I,J,{0},W` be mutually disjoint original-coordinate groups. Conditional on `W=w`, suppose the quadratic form can be written

`Q = a (Z+d(X_I,w))^2
    + r(X_I,w)
    + 2 X_I^T B X_J
    + b(w)^T X_J
    + c(w)`,                                                   (5.1)

where `a!=0`, `B!=0`, `d,r` are arbitrary measurable functions of the displayed variables, and there is no quadratic `X_J` term and no `Z-X_J` coupling. Put `s=||B||_op`.

### Theorem 5.1 — `QFORM-ONE-SIDED-BILINEAR-SQUARE-LP-v1`

For every `p>2`, `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= C_p |a|^(-1/p) s^(-(p-1)/p),`                             (5.2)

where

`C_p = 2p ((p-1)/(p-2))^((p-1)/p)`.                           (5.3)

Proof. Condition on `W=w` and `X_I=x`. Then the square variable `Z` and the entire `J` bank remain independent original-coordinate sources. Young at conjugate exponents `q=p/(p-1)` and `p` bounds the conditional output density by the product of (4.1) and the `L^p` norm of the linear `J` term. Averaging in `x`, and applying exactly the inverse-moment estimate from Theorem 3.1, cancels the powers of two to give (5.2)-(5.3). The bound is uniform in `w`; averaging over `W` preserves it. QED.

For the named-partner endpoint `p=3`, fleet03/B04's `L^(3/2)` square estimate combines with the new bilinear-bank `L^3` estimate to give the explicit actual inequality

`boxed:
 ||p_Q||_infinity
 <= 6*2^(2/3) |a|^(-1/3) s^(-2/3)
 = 9.5244063118... |a|^(-1/3) s^(-2/3).`                      (5.4)

A convenient slightly better exact choice is `p=11/4`:

`boxed:
 ||p_Q||_infinity
 <= (11/2)(7/3)^(7/11) |a|^(-4/11) s^(-7/11)
 < 9.431 |a|^(-4/11) s^(-7/11).`                              (5.5)

Numerical optimization of (5.3) gives `p approximately 2.7686440787` and `C_p approximately 9.4295942087`; no optimized constant is needed for the theorem.

This is the substantive advance: the previous rank-one/aligned-bank hypothesis is replaced by an arbitrary-rank, arbitrarily misaligned physical cross block. Only one side must be quadratically clean.

## 6. Explicit genuinely rotated indefinite full-rank target example

Let

`H4=(1/2)[[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]`.

Set

`B=H4 diag(6/5,3/5,1/20,1/50) H4^T`

so

`B=(1/400)[[187,63,173,57],[63,187,57,173],[173,57,187,63],[57,173,63,187]]`,

and set

`C=H4 diag(1/10,-1/12,1/20,-1/25) H4^T`

so

`C=(1/600)[[4,41,1,14],[41,4,14,1],[1,14,4,41],[14,1,41,4]]`.

On original coordinates `(z,x_1,...,x_4,y_1,...,y_4)`, define

`A=[[1,0,0],[0,C,B],[0,B,0]]`.                                (6.1)

Then

`Q=z^2+x^T Cx+2x^TBy`.                                        (6.2)

This matrix is full rank, physically non-diagonal, dense on the `x` block and on every `x-y` cross entry, and indefinite. The Walsh output rotation is used only to check its spectrum; no rotated-coordinate independence enters the probability proof.

The `k=1` Walsh mode has the two eigenvalues

`(1+sqrt(577))/20` and `(1-sqrt(577))/20`,                     (6.3)

whose moduli are both greater than one; together with the singleton eigenvalue `1`, this gives at least three target-scale eigenvalues. The remaining modes are nonzero as well, so `A` is full rank.

Here `a=1` and `s=||B||_op=6/5`. Applying (5.5), for every allowed product input law,

`boxed:
 ||p_(X^T A X)||_infinity
 <= (11/2)(35/18)^(7/11)
 = 8.3973386720... .`                                         (6.4)

At the named-partner `p=3` endpoint the bound is `8.4343266531...`.

This is an explicit estimate for a genuinely rotated indefinite full-rank form with arbitrary independent density-capped inputs.

## 7. Relation to the near-isotropic frontier

A fresh fleet03/B02 result, `QFORM-RANK3-OVERLAP1-INTEGRATED-FOURIER-v1`, shows that exact-rank-three overlap-one mass is paid unless it concentrates on near-zero physical pivots; there the off-diagonal row energy is forced and must be combined with residual exterior mass before any reciprocal-pivot payment. Theorem 5.1 provides the analytic endpoint for such a packet once the product-preserving decomposition exposes a quadratically clean side. It does not by itself prove that this clean side always exists.

The first unpaid implication is therefore

`QFORM-TWO-SIDED-QUADRATIC-LEAKAGE-ROUTING-v1`:

> In every unresolved high-leverage / near-isotropic configuration, either expose disjoint original-coordinate banks with cross operator norm bounded below and with one bank entering linearly after a product-preserving completion, so Theorem 5.1 applies, or route quantitatively to the completed ridge, pair-log, diffuse-rank-two, principal-block, or multi-bank mechanisms. If both sides carry essential quadratic leakage, aggregate or absorb that leakage without a vanishing local-minor payment.

Misalignment and arbitrary cross rank are no longer the obstruction in the one-clean-side branch. The remaining structural debt is two-sided quadratic leakage plus the separate arbitrary-extra-spectrum routing outside completed branches.

## 8. Integrity and status

This report proves a supporting theorem and an explicit target-valid family estimate. It does not prove the full conjecture. Essential boundedness is proved in the stated branch; continuity is not claimed here. No moments, compact support, connected support, diagonal-basis reduction, Gaussianity, post-rotation independence, or law-uniform pointwise oscillatory decay is used.

Exact finite arithmetic for the displayed matrix and constants is saved with this report. No private data, credentials, scheduler identifiers, benchmark material, email, Drive, paid calls, public release, remote workflows, or permission changes were used.