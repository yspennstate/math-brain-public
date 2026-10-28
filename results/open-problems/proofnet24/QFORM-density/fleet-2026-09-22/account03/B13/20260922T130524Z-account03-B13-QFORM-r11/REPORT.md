# account03/B13 — affine completion and a target-level no-localization theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T130524Z-account03-B13-QFORM-r11`  
**Assignment:** Extremal product laws  
**Classification:** `PROVED TARGET-LEVEL REDUCTION + REFUTED LOCALIZATION ROUTE / FULL CONJECTURE OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and corrections retained

The full target remains: for every finite `n`, every independent real `X_i` with densities `0 <= f_i <= 1`, every real symmetric `A` with at least three eigenvalues satisfying `|lambda_j(A)| >= 1`, every interval `I`,

\[
  \Pr\{X^TAX\in I\}\le C|I|
\]

for one finite universal `C` independent of `n`, `A`, the laws, and `I`.

This report does not use the refuted law-uniform pointwise oscillatory-decay bound, does not rotate the independent coordinates and keep false independence, does not use the dimension-losing fiber-supremum argument, and does not use a cross-minor-alone implication.

## 2. Completed partner mathematics actually consumed

I read and use the complete account04/B14 proof:

`yspennstate/math-open-problems@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`.

At the exact scope used here it proves, with zero constant loss:

1. for every fixed quadratic form and interval, the supremum over all independent marginal densities `0<=f_i<=1`, `int f_i=1`, equals the supremum over product indicators `f_i=1_{E_i}`, `|E_i|=1`;
2. the same supremum is unchanged if each `E_i` is required to be a compact finite union of intervals of total measure one.

This run applies that theorem to a further exact normalization, and then shows a sharp obstruction to any attempted bounded-diameter or single-interval continuation of that localization.

## 3. The optimal pure-quadratic constant equals the optimal affine-quadratic constant

Define `C_quad` to be the optimal (possibly infinite) constant in the owner small-ball inequality for the pure forms `x^T A x`. Define `C_aff` by allowing in addition an arbitrary deterministic linear term and constant,

\[
     x^TAx+b^Tx+c,
\]

while keeping exactly the same hypotheses on `A` and on the independent input laws.

### Theorem 3.1 — affine completion costs exactly zero

\[
\boxed{C_{\rm aff}=C_{\rm quad}.}
\]

In particular, any finite constant valid for the original pure-quadratic conjecture is automatically valid, with the same value, after arbitrary linear tilts.

### Proof

The inequality `C_aff >= C_quad` is immediate by taking `b=0` and `c=0`.

For the reverse direction, fix any finite `C` that is valid for all pure forms in the target class, and fix `A,b,c` in the affine class. Let `P_0` be the orthogonal projection onto `ker A`. For `epsilon>0`, set

\[
       A_\epsilon=A+\epsilon P_0.
\]

Because `A` is symmetric, `P_0` commutes with `A`; the nonzero eigenvalues of `A` are unchanged in `A_epsilon`, while every zero eigenvalue is replaced by `epsilon`. Hence the original three eigenvalues of absolute value at least one remain exactly unchanged. Moreover `A_epsilon` is invertible.

Put

\[
       h_\epsilon={1\over2}A_\epsilon^{-1}b.
\]

Then, by direct completion of the square,

\[
 x^TA_\epsilon x+b^Tx+c
 = (x+h_\epsilon)^TA_\epsilon(x+h_\epsilon)
   +c-h_\epsilon^TA_\epsilon h_\epsilon.
\tag{3.1}
\]

Coordinatewise deterministic translation preserves independence and preserves every marginal density cap. Therefore the assumed pure-quadratic bound gives, for every bounded interval `J`,

\[
 \Pr\{X^TA_\epsilon X+b^TX+c\in J\}\le C|J|.
\tag{3.2}
\]

Now

\[
 Z_\epsilon-Z
 =\epsilon\,\|P_0X\|_2^2,
\]

where `Z_epsilon=X^TA_epsilon X+b^TX+c` and `Z=X^TAX+b^TX+c`. Every coordinate of `X` is a finite real random variable almost surely, so `Z_epsilon -> Z` almost surely as `epsilon downarrow 0`; no moment assumption is used.

For `J=[a,a+ell]` and any `delta>0`,

\[
 \Pr\{Z\in J\}
 \le \Pr\{Z_\epsilon\in[a-\delta,a+\ell+\delta]\}
     +\Pr\{|Z_\epsilon-Z|>\delta\}.
\]

Take `epsilon downarrow 0`, use (3.2), and then `delta downarrow 0` to get

\[
       \Pr\{Z\in J\}\le C\ell.
\]

Thus every admissible pure constant is also an affine constant, proving `C_aff<=C_quad`. QED.

### Why this is useful

Linear terms produced by original-coordinate conditioning or by translating a finite-fragment extremal set do not constitute an extra target. They can be admitted globally at zero loss, even when `A` is singular and even when the input laws have no moments. The kernel regularization above is the step needed to avoid silently assuming `b in range(A)`.

## 4. Exact median-zero finite-fragment normalization

Combine Theorem 3.1 with the account04/B14 bang-bang/finite-fragment theorem.

Let `E subset R` be measurable with `|E|=1`. The function

\[
       F_E(t)=|E\cap(-\infty,t]|
\]

is continuous (Lebesgue measure has no atoms), tends to `0` at `-infinity`, and tends to `1` at `+infinity`. Hence there exists `m(E)` with `F_E(m(E))=1/2`. Translation by `m(E)` produces a unit-measure set with exactly one half of its mass on each side of zero.

For a product set `E_1 x ... x E_n`, choose these medians coordinatewise and write `m=(m_1,...,m_n)`, `Y=X-m`. Then

\[
 X^TAX=Y^TAY+2(Am)^TY+m^TAm.
\tag{4.1}
\]

By Theorem 3.1 the linear term in (4.1) costs no constant. Translations preserve compact finite-union structure. Therefore:

### Corollary 4.1 — median-zero extreme-product reduction

The full owner conjecture is equivalent, with exactly the same best constant, to proving the affine small-ball inequality on the class where every marginal is `1_{E_i}` with `E_i` a compact finite union of intervals, `|E_i|=1`, and

\[
 |E_i\cap(-\infty,0]|=|E_i\cap[0,\infty)|={1\over2}.
\]

This removes arbitrary coordinate drift without introducing moments, connectedness, diameter bounds, or a false interval-extremality claim.

## 5. A genuine target-level obstruction to every bounded-diameter localization

The preceding normalization is essentially as far as one may go by pure translation. In particular there is **no universal finite support-diameter bound** that preserves the extremal small-ball problem, even for the positive-definite target matrix `A=I_3`.

### Theorem 5.1 — separated branches force unbounded extremal diameter

Fix any finite `D>=1`. There exist a target matrix with three eigenvalues equal to one, a target interval, and two fixed admissible one-dimensional marginals such that:

* an admissible compact finite-fragment set `E_1` of measure one attains conditional small-ball mass `2M>0`;
* every admissible set `F_1` of measure one and diameter at most `D` has small-ball mass at most `M`.

Thus any reduction to supports of uniformly bounded diameter loses at least a factor two. The special case `D=1` rules out a reduction to single unit intervals or centered uniforms inside the exact owner target.

### Construction and proof

Take

\[
 A=I_3,
 \qquad E_2=E_3=[-1/2,1/2],
 \qquad J_R=[R^2,R^2+1/4],
\]

where `R>=1` will be chosen large. With `X_2,X_3` uniform on their unit intervals, write

\[
  S=X_2^2+X_3^2\in[0,1/2]
\]

and define the one-coordinate fiber

\[
 g_R(x)=\Pr\{R^2\le x^2+S\le R^2+1/4\}.
\]

The function is even. Its essential support is exactly the two bands

\[
 B_+(R)=\left[\sqrt{R^2-1/2},\sqrt{R^2+1/4}\right],
 \qquad B_-(R)=-B_+(R).
\tag{5.1}
\]

Indeed `S` has support `[0,1/2]` and gives positive mass to every nonempty open subinterval of this range. Set

\[
 L_R=|B_+(R)|
 =\sqrt{R^2+1/4}-\sqrt{R^2-1/2}.
\]

Then

\[
 2L_R={3/2\over \sqrt{R^2+1/4}+\sqrt{R^2-1/2}}<1
 \qquad(R\ge1).
\tag{5.2}
\]

The gap between the two bands is

\[
       2\sqrt{R^2-1/2},
\tag{5.3}
\]

which tends to infinity. Choose `R` so that (5.3) is greater than `D`.

Let

\[
  M_R=\int_{B_+(R)}g_R(x)\,dx>0.
\]

By evenness the integral over the negative band is the same. Since the total support length is below one, choose a finite-union set `E_1` of total measure one containing both bands and fill the unused measure in the zero region of `g_R`. Then

\[
 \int_{E_1}g_R(x)\,dx=2M_R.
\tag{5.4}
\]

In fact one may choose the filler symmetrically around zero, so `E_1` itself has median zero and is a compact union of three intervals.

On the other hand, every set `F_1` with `diam(F_1)<=D` intersects at most one of the two support bands by (5.3). Therefore

\[
 \int_{F_1}g_R(x)\,dx\le M_R.
\tag{5.5}
\]

This proves the factor-two separation. For a single unit interval take `D=1`; because each band has length `<1`, one unit interval can capture one complete band but not both, so the best interval value is exactly `M_R`, while the disconnected admissible set gives `2M_R`.

The matrix `I_3` has exactly three eigenvalues `|lambda|=1`, so this is not a surrogate one-dimensional kernel; it is a genuine instance of the exact target.

### Concrete numerical control at `R=2`

For `R=2`,

\[
 B_+(2)=[\sqrt{7/2},\sqrt{17}/2],
 \qquad 2L_2=\sqrt{17}-\sqrt{14}=0.381448\ldots<1,
\]

and the separation of the two bands is `sqrt(14)=3.741657...`. Direct deterministic quadrature gives

\[
 M_2=0.06285284447661851\ldots,
 \qquad 2M_2=0.12570568895323703\ldots.
\]

These decimal values are only a sanity check; the proof needs only symmetry, positivity, (5.2), and (5.3). Positivity can be certified without numerical integration: for

\[
 x\in[2,\sqrt{33/8}],\qquad |X_2|,|X_3|\le1/4,
\]

one has `4<=x^2+X_2^2+X_3^2<=17/4`, so

\[
 M_2\ge {1\over4}(\sqrt{33/8}-2)>0.
\]

## 6. What is now paid, refuted, and still open

**PROVED:**

1. arbitrary linear tilts and constants are equivalent to the original pure-quadratic target at exactly the same optimal constant;
2. after the completed partner bang-bang theorem, every marginal may additionally be median-normalized to zero while retaining compact finite-fragment form, if arbitrary affine terms are retained;
3. this median normalization is compatible with every original target quantifier and uses no moments.

**REFUTED as a reduction:**

1. single-interval or centered-uniform extremality;
2. any universal bound on support diameter of the extremal product sets.

The refutation occurs already at `A=I_3` with three threshold eigenvalues and therefore cannot be dismissed as a non-target toy kernel.

**OPEN:** the universal dimension-free slab estimate for arbitrary separated finite fragments. This report does not bound that slab and does not prove the full conjecture.

## 7. Next target-relevant attack

Because support diameter and fragment separation cannot be localized, the next proof mechanism must be **fragment-blind**: it should depend on the unit mass/height constraints and product structure, not on a compactness radius. The most useful next step is to combine the median-zero affine formulation with the completed local principal-pair/triple bounds and the diffuse/separable-phase theorem to prove a structural dichotomy in which every matrix either pays one of those existing branches or enters an explicitly described high-cardinality aggregation branch. Any argument whose constant grows with support diameter is now ruled out at the reduction level.

Primary handoff recipients: account04/B14 (localization consistency) and B19 synthesis workers. The full conjecture remains **OPEN / NOT PROVED**.

## 8. Source pins

* partner proof consumed: `yspennstate/math-open-problems@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322:proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`;
* live owner programme remains `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`.

No novelty or publication-priority claim is made.
