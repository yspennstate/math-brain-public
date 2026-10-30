# fleet03/B08 — diffuse spectral frames: a dimension-free Fourier–Brascamp–Lieb theorem

**Run:** `20260922T114830Z-fleet03-B08-qform-diffuse-v1`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** fleet03/B08, `Diffuse eigenvector case` / pathway `GEOMETRY`  
**Classification:** `ESSENTIAL_STEP_APPLIED`; **full target OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Scope, corrections, and applied peer result

The live target is the bounded-density conjecture for `Q=X^T A X` with independent one-dimensional input densities bounded by `1` and at least three eigenvalues of `A` of absolute value at least `1`. The later quadratic-form owner order supersedes the incoming FEI instruction.

The proof below respects all current route corrections. In particular, it does **not** use a law-uniform pointwise one-dimensional Fresnel estimate (which is false), does not diagonalize `A` and pretend that independence survives, and does not replace a spectral fiber by an unrestricted fiber supremum.

I apply the exact other-account result fleet02/B06, canonical report `yspennstate/math-open-problems@6902eb62f21a7c833ca27dcca69f34d50e711a7d`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`. That report constructs the rank-three Hadamard-delocalized family

`A=U diag(1,1,-1) U^T`

for `n=2^k`, proves that every bounded-size physical-coordinate compression has vanishing curvature and every physical `2x2` principal determinant is nonpositive, and identifies distributed determinant mass as the resource that survives delocalization. The theorem below closes that exact Hadamard family for **all** admissible product input laws by using the entire diffuse frame at once, rather than selecting one physical block.

The named partner fleet04/B08 had no completed current-QFORM handoff at the fresh snapshot used in this run; no mathematical premise is attributed to that worker.

## 1. A complex high-power Fourier lemma

We use the Fourier convention

`hat g(s)=int_R g(x) exp(i s x) dx`.

### Lemma 1 — `QFORM-COMPLEX-HY-HIGHPOWER-v1`

Let `g:R->C` satisfy `|g|<=1` almost everywhere and `||g||_1<=1`. Then for every real `p>=2`,

`int_R |hat g(s)|^p ds <= 2 pi sqrt(e/p)`.

This allows arbitrary measurable phases multiplying a bounded probability density.

### Proof

Let `q=p/(p-1)`, so `1<=q<=2`. For the normalized transform

`F g(xi)=int g(x) exp(-2 pi i x xi) dx`,

the sharp Babenko–Beckner Hausdorff–Young inequality gives

`||F g||_p <= (q^(1/q)/p^(1/p))^(1/2) ||g||_q`.

Because `|g|<=1` and `||g||_1<=1`,

`||g||_q^q <= ||g||_1 <=1`, hence `||g||_q<=1`.

The two Fourier conventions are related by `hat g(s)=F g(-s/(2pi))`, so

`int |hat g(s)|^p ds = 2pi ||F g||_p^p`

and therefore

`int |hat g|^p <= 2pi q^((p-1)/2) p^(-1/2)`.

Since `q=p/(p-1)=(1+1/(p-1))`,

`q^(p-1) <= e`.

Taking square roots yields the claim. `QED`

**Source for the sharp Fourier constant.** W. Beckner, *Inequalities in Fourier Analysis on R^n*, Proc. Natl. Acad. Sci. USA 72 (1975), 638–641, DOI `10.1073/pnas.72.2.638`. Only this classical theorem is imported; all subsequent estimates are proved below.

## 2. A dimension-free Fourier integral for diffuse frames

Let `R` be an `n x r` real matrix with orthonormal columns, `R^T R=I_r`. Write its rows as `v_i in R^r` and their leverage scores as

`c_i=|v_i|^2`.

Then

`sum_i v_i v_i^T=I_r` and `sum_i c_i=r`.

### Lemma 2 — `QFORM-DIFFUSE-FRAME-BL-v1`

Assume `c_i<=1/2` for every `i`. For arbitrary functions `g_i:R->C` satisfying `|g_i|<=1` and `||g_i||_1<=1`,

`J := int_{R^r} prod_i |hat g_i(<v_i,xi>)| dxi <= (2 pi sqrt(e))^r`.

### Proof

Rows with `c_i=0` contribute the harmless factor `|hat g_i(0)|<=1`, so discard them. Put

`u_i=v_i/sqrt(c_i)`.

Then `|u_i|=1` and

`sum_i c_i u_i u_i^T=I_r`.

For each `i`, define the nonnegative one-dimensional function

`F_i(s)=|hat g_i(sqrt(c_i) s)|^(1/c_i)`.

The rank-one geometric Brascamp–Lieb inequality for the identity decomposition above gives

`J = int prod_i F_i(<u_i,xi>)^(c_i) dxi
   <= prod_i (int_R F_i)^(c_i)`.

Now `p_i=1/c_i>=2`. By Lemma 1 and the change of variables `t=sqrt(c_i)s`,

`int F_i(s) ds
 = c_i^(-1/2) int |hat g_i(t)|^(1/c_i) dt
 <= c_i^(-1/2) 2pi sqrt(e c_i)
 = 2pi sqrt(e)`.

Finally `sum_i c_i=tr(I_r)=r`, so

`J <= (2pi sqrt(e))^(sum_i c_i)=(2pi sqrt(e))^r`. `QED`

This is the point at which diffuse geometry and product structure are used simultaneously. No individual coordinate needs to carry constant curvature.

## 3. Main theorem: diffuse low-rank quadratic forms with arbitrary coordinatewise phases

### Theorem 3 — `QFORM-DIFFUSE-SPECTRAL-FRAME-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1`. Let `R in R^{n x r}` have orthonormal columns, let its row leverage scores obey

`max_i ||R_{i,*}||_2^2 <= 1/2`,

and let `Lambda in R^{r x r}` be real symmetric and invertible, with `r>=3`. Let `V_i:R->R` be arbitrary measurable functions. Define

`Y=(R^T X)^T Lambda (R^T X) + sum_i V_i(X_i)`.

Then `Y` has a bounded continuous density. Its characteristic function satisfies, for every `t!=0`,

`|phi_Y(t)| <= (pi e)^(r/2) |det Lambda|^(-1/2) |t|^(-r/2)`.

Consequently

`||p_Y||_infinity <= e * r/(r-2) * |det Lambda|^(-1/r)`.

In particular, if every eigenvalue of `Lambda` has absolute value at least `1`, then

`||p_Y||_infinity <= 3e`.

### Proof

Fix `t!=0`. The `r`-dimensional Fresnel identity for a real symmetric invertible `Lambda` is

`exp(i t y^T Lambda y)
 = c(t,Lambda) int_{R^r}
     exp(-i xi^T Lambda^{-1} xi/(4t)) exp(i xi.y) dxi`,

in the tempered-distribution sense, with

`|c(t,Lambda)|=(4pi |t|)^(-r/2) |det Lambda|^(-1/2)`.

For rigor one may insert `exp(-epsilon |xi|^2)` on the frequency side and let `epsilon downarrow0`; the estimate below provides an integrable dominating function, while the regularized Fresnel identity converges to the displayed phase.

Set

`g_{i,t}(x)=f_i(x) exp(i t V_i(x))`.

Then `|g_{i,t}|=f_i<=1` and `||g_{i,t}||_1=1`. Independence and the Fresnel representation give

`|phi_Y(t)|
 <= |c(t,Lambda)| int_{R^r}
      prod_i |hat g_{i,t}(<v_i,xi>)| dxi`,

where `v_i` is row `i` of `R`. Lemma 2 applies uniformly in `t`, hence

`|phi_Y(t)|
 <= (4pi|t|)^(-r/2)|det Lambda|^(-1/2)
       (2pi sqrt(e))^r
 = (pi e)^(r/2)|det Lambda|^(-1/2)|t|^(-r/2)`.

Together with the trivial `|phi_Y(t)|<=1`, put

`a=pi e |det Lambda|^(-1/r)`

and obtain

`|phi_Y(t)| <= min(1,(a/|t|)^(r/2))`.

Since `r>2`, this is integrable and

`int_R |phi_Y(t)| dt
 <= 2a [1 + 1/(r/2-1)]
 = 2a r/(r-2)`.

Fourier inversion therefore gives a bounded continuous representative of the density and

`||p_Y||_infinity
 <= (1/(2pi)) ||phi_Y||_1
 <= e r/(r-2)|det Lambda|^(-1/r)`.

For `r>=3`, `r/(r-2)<=3`; if all eigenvalues of `Lambda` have magnitude at least `1`, then `|det Lambda|>=1`. This proves the stated `3e` bound. `QED`

### What the arbitrary `V_i` extension buys

The theorem is not restricted to a pure low-rank quadratic form. It permits, without changing the constant,

- arbitrary diagonal quadratic remainders `sum d_i X_i^2`;
- arbitrary coordinatewise linear terms;
- arbitrary measurable coordinatewise phases/potentials.

Thus the mechanism is genuinely nontruncated and does not rely on forbidden pointwise Fresnel decay of any single input law.

## 4. Conditional/whitened extension: localized coordinates may be conditioned away

The diffuse theorem has a useful localized/diffuse complement.

### Corollary 4 — `QFORM-CONDITIONAL-WHITENED-DIFFUSE-v1`

In the setting of Theorem 3, split the physical coordinates into `H union L`. Let `R_L` denote the rows indexed by `L` and assume

`M=R_L^T R_L` is positive definite.

Define the whitened residual frame

`W=R_L M^(-1/2)`.

If every row `w_i` of `W` satisfies `||w_i||^2<=1/2`, then after conditioning on all `X_H`, the remaining law has a density bounded uniformly in the conditioning value by

`e r/(r-2) * (det M)^(-1/r) * |det Lambda|^(-1/r)`.

Hence the same bound holds unconditionally.

### Proof

Condition on `X_H=h`. Write `a=R_H^T h`. Since

`R_L^T x_L=M^(1/2) W^T x_L`,

the conditioned quadratic term equals

`(W^T x_L)^T B (W^T x_L) + ell . (W^T x_L) + const`,

where

`B=M^(1/2) Lambda M^(1/2)`

and `ell` depends on `h`. The linear term `ell.W^T x_L=(W ell).x_L` is a sum of coordinatewise linear potentials, so Theorem 3 applies to the conditional product density on `L`. Finally

`|det B|=det(M)|det Lambda|`.

The bound is independent of `h`; average the conditional densities. `QED`

This gives a concrete bridge to localized-coordinate conditioning: a small set of localized coordinates can be frozen, provided the surviving spectral frame remains quantitatively nonsingular and diffuse after whitening.

## 5. Direct application of fleet02/B06's Hadamard adversary

The fleet02/B06 family has

`A=U diag(1,1,-1) U^T`,

where `U` consists of three normalized Sylvester-Hadamard columns and `n=2^k>=8`. Every row of `U` has squared norm exactly

`3/n <= 3/8 < 1/2`.

Thus Theorem 3 applies with `r=3`, `Lambda=diag(1,1,-1)`, `|det Lambda|=1`, and `V_i=0`. For **every** independent input law with densities bounded by `1`,

`|phi_Q(t)| <= (pi e)^(3/2)|t|^(-3/2)`

and

`||p_Q||_infinity <= 3e`.

Moreover `p_Q` has a continuous representative.

This is a substantive use of the B06 result: the exact family that defeats every fixed-size physical-coordinate curvature localization is nevertheless closed dimension-freely by the global diffuse-frame mechanism. The distributed geometry is not an obstruction by itself.

## 6. Why this does not yet solve the full conjecture

Given a general target matrix `A`, choose three (or more) large eigenvectors and write their contribution as `R Lambda R^T`. The remaining spectral part `C` usually contributes

`X^T C X`

with off-diagonal interactions in the original independent coordinates. Unlike a diagonal remainder, the phase `exp(i t X^T C X)` does **not** factor into `prod_i g_i(X_i)`. Therefore the product Fourier integral in Lemma 2 is no longer available directly.

So the first unpaid implication is now precise:

### `QFORM-DIFFUSE-OFFDIAGONAL-REMAINDER-v1` — OPEN

Extend Theorem 3 to

`Q=X^T (R Lambda R^T + C) X`

when `R` is diffuse and `C R=0` is an arbitrary symmetric spectral remainder, without moment assumptions and without assuming that `C` is diagonal in the physical coordinates. It is enough to prove a dimension-free small-ball or integrated-characteristic-function estimate that retains the high-power Fourier budgets from Lemma 1 while controlling the non-product remainder phase.

A successful extension of this form, combined with a complementary localized branch, would reach the full target. This report does **not** claim that implication.

## 7. Relation to the current false routes

This proof survives the known phase-aligned-density obstruction because it never asks any single `hat g_i` to decay pointwise. It only spends the exact high-power integral budget supplied by Hausdorff–Young. It survives the cube-projection/fiber-supremum obstruction because it never takes a fiber supremum. And it works directly in the original independent coordinates, so no false independence-after-rotation step occurs.

The contrast with the fleet02/B05 squared-kernel route is also useful: one early squaring followed by a bare `L^2` Brascamp–Lieb estimate loses half of the desired decay exponent. Here the leverage-dependent exponents `p_i=1/c_i` are used **before** any such square-root loss, and the identity `sum c_i=r` converts all one-dimensional high-power budgets into the full `|t|^{-r/2}` decay.

## 8. Status

**PROVED (supporting, target-relevant):**

- `QFORM-COMPLEX-HY-HIGHPOWER-v1`;
- `QFORM-DIFFUSE-FRAME-BL-v1`;
- `QFORM-DIFFUSE-SPECTRAL-FRAME-v1`, including continuous density and explicit constant `e r/(r-2)|det Lambda|^{-1/r}`;
- `QFORM-CONDITIONAL-WHITENED-DIFFUSE-v1`;
- universal `3e` closure of fleet02/B06's exact rank-three Hadamard-delocalized family for arbitrary admissible product laws.

**OPEN:** `QFORM-DIFFUSE-OFFDIAGONAL-REMAINDER-v1` and the full quadratic-form bounded-density conjecture.

No counterexample to the owner target is claimed.
