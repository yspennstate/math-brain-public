# QFORM B15 — raw-output regularity is not uniformly compact; fixed-scale heat regularity is exact and safe

**Run:** `20260922T230327Z-account01-B15-QFORM-r14`  
**Account/slot:** account01/B15  
**Assignment:** Absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / RAW-REGULARITY-COMPACTNESS-OBSTRUCTION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-22T23:03:27Z.

attacking: separate the already-qualitative continuity theorem from the still-open universal height by proving exactly which stronger uniform regularity/compactness statements are impossible, then retain only the exact fixed-scale heat normal form.

## 1. Target and source state

The owner target remains: for every dimension, every independent real input with one-dimensional densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite constant `C` such that

\[
\|p_{X^TAX}\|_\infty\le C.
\]

Continuity is a separate stronger conclusion. The fresh control branch remained on owner revision `2026-09-22.15`; the full target is still open. The live correction inbox was consumed, in particular the refutations of law-uniform pointwise quadratic Fourier decay, post-rotation independence, arbitrary-joint rank-three coarea, positive conditional projection-height moments, and one-local-block/cross-rank-three extraction.

The assigned partner result actually used below is account02/B15 r11:

- repository/commit: `yspennstate/math-open-problems@4fc6472947c7e5551592974a34e7bc4bfe78def0`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T220230Z-account02-B15-qform-r11/REPORT.md`.

That report constructs, already for the fixed target matrix `A=I_3`, a sequence of iid strictly positive analytic-Schwartz cap-one marginals whose output densities `p_m` satisfy

\[
\|p_m\|_\infty\le 2\pi,
\qquad \{p_m\}\text{ is uniformly tight},
\]

and there are frequencies `\tau_m\to\infty` with

\[
\boxed{|\widehat p_m(\tau_m)|\ge a:=\frac{27}{512}.}
\tag{1.1}
\]

The same report proves that no common pointwise continuity modulus exists. I now apply (1.1) to obtain strictly stronger quantitative obstructions.

## 2. Main new theorem — no uniform L1 translation modulus

Let `T_h p(x)=p(x+h)`. For every probability density `p\in L^1` and every frequency `\xi`,

\[
\widehat{T_h p-p}(\xi)
=(e^{-i\xi h}-1)\widehat p(\xi),
\]

while the elementary Fourier bound gives

\[
|\widehat g(\xi)|\le \|g\|_1.
\]

Apply this to the partner sequence and take

\[
h_m=\frac{\pi}{\tau_m}.
\]

Then `h_m\to0` and `|e^{-i\tau_m h_m}-1|=2`. Therefore

\[
\boxed{
\|T_{h_m}p_m-p_m\|_1
\ge 2|\widehat p_m(\tau_m)|
\ge \frac{27}{256}.
}
\tag{2.1}
\]

Hence there is **no** function `\omega_1(h)\downarrow0` such that

\[
\|T_h p-p\|_1\le \omega_1(|h|)
\]

uniformly over the target class, even after restricting to the fixed matrix `A=I_3`, iid strictly positive analytic-Schwartz cap-one marginals, uniformly tight output laws, and the already-uniform height bound `\|p\|_\infty\le2\pi`.

This is stronger than the partner's absence of a common pointwise modulus: the raw target-output family is not even uniformly translation-continuous in `L^1`.

### Consequence 2.2 — no L1 compactness of the raw target densities

By the Kolmogorov-Riesz compactness criterion, uniform tightness together with relative compactness in `L^1` would force a common `L^1` translation modulus. Since the partner family is uniformly tight but violates (2.1),

\[
\boxed{\{p_m\}\text{ is not relatively compact in }L^1(\mathbb R).}
\tag{2.2}
\]

Thus a compactness proof of the universal height cannot proceed by first extracting a uniformly regular raw-output subsequence from tightness plus the existing `C_0\cap L^\infty` conclusion.

## 3. Quantitative BV and Besov blow-up

For a function `p` of bounded variation, its distributional derivative is a finite signed measure `Dp`, so

\[
i\xi\widehat p(\xi)=\widehat{Dp}(\xi),
\qquad
|\widehat{Dp}(\xi)|\le |Dp|(\mathbb R)=\operatorname{TV}(p).
\]

Using (1.1), with the convention `TV(p)=+\infty` when `p\notin BV`, gives

\[
\boxed{
\operatorname{TV}(p_m)
\ge \tau_m|\widehat p_m(\tau_m)|
\ge \frac{27}{512}\tau_m
\longrightarrow\infty.
}
\tag{3.1}
\]

So there is no target-uniform BV or `W^{1,1}` estimate, even in the fixed `I_3` analytic-Schwartz source subclass.

More generally, for every `0<\alpha\le1`, define the translation Besov seminorm

\[
[p]_{B^{\alpha}_{1,\infty}}
:=\sup_{h\ne0}\frac{\|T_h p-p\|_1}{|h|^\alpha}.
\]

Equation (2.1) at `h_m=\pi/\tau_m` yields the exact lower bound

\[
\boxed{
[p_m]_{B^{\alpha}_{1,\infty}}
\ge \frac{27}{256}\left(\frac{\tau_m}{\pi}\right)^\alpha
\to\infty.
}
\tag{3.2}
\]

Thus **every positive-order target-uniform translation-regularity estimate of this form is false**. This is not a counterexample to the density-height conjecture; the same family has the uniform height bound `2\pi`.

## 4. Uniform desmoothing is also false

Let

\[
\gamma_\varepsilon(x)=\frac1{\sqrt{2\pi}\varepsilon}
 e^{-x^2/(2\varepsilon^2)}.
\]

Then

\[
\widehat{p*\gamma_\varepsilon}(\xi)
=e^{-\varepsilon^2\xi^2/2}\widehat p(\xi).
\]

Choose `\varepsilon_m=1/\tau_m`. At the partner frequency `\tau_m`,

\[
\begin{aligned}
\|p_m*\gamma_{\varepsilon_m}-p_m\|_1
&\ge
\left|e^{-1/2}-1\right|\,|\widehat p_m(\tau_m)|\\
&\ge
\left(1-e^{-1/2}\right)\frac{27}{512}.
\end{aligned}
\]

Therefore

\[
\boxed{
\|p_m*\gamma_{1/\tau_m}-p_m\|_1
\ge \left(1-e^{-1/2}\right)\frac{27}{512}>0
}
\tag{4.1}
\]

for all `m`. In particular,

\[
\boxed{
\sup_{\text{target }p}\|p*\gamma_\varepsilon-p\|_1
\not\longrightarrow0
\qquad(\varepsilon\downarrow0).
}
\tag{4.2}
\]

So the exact heat reduction must **not** be interpreted as a uniform approximation of raw target densities by mollification. The reduction is valid only because spectral homogeneity makes one fixed heat scale exactly equivalent to the height problem.

## 5. Positive counterpart — exact uniformly smooth heat normal form

The compatible completed account03/B15 theorem at

`yspennstate/math-open-problems@ae1acd1eb774e59dd80eb9ddfb8ea9c7e72b79a1:proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T213701Z-account03-B15-qform-r18/REPORT.md`

proves the exact identity

\[
\boxed{
C_*
=
\sup_{s_3(A)>0,\,f}
 s_3(A)\,\|\mu_{X^TAX}*\gamma_1\|_\infty.
}
\tag{5.1}
\]

This fixed-scale heat family has universal regularity completely independent of the target matrix and input law. If

\[
H_{A,f}(y):=(\mu_{X^TAX}*\gamma_1)(y),
\]

then for every integer `k>=0`, differentiation under the convolution gives

\[
H_{A,f}^{(k)}(y)=\int \gamma_1^{(k)}(y-u)\,d\mu_{X^TAX}(u),
\]

hence

\[
\boxed{
\|H_{A,f}^{(k)}\|_\infty
\le \|\gamma_1^{(k)}\|_\infty=:c_k.
}
\tag{5.2}
\]

In particular,

\[
\boxed{
\operatorname{Lip}(H_{A,f})
\le c_1
=\frac1{\sqrt{2\pi e}}.
}
\tag{5.3}
\]

Thus the entire universal-height conjecture can be attacked on a family of output profiles with a **common `C^\infty` regularity hierarchy**, without asserting any corresponding uniform regularity of the raw densities. The only unpaid quantity in this smooth normal form is the spectral decay of the height itself:

\[
\boxed{
\sup_{A,f}s_3(A)\,\|H_{A,f}\|_\infty<\infty.
}
\tag{5.4}
\]

Equations (2.1)-(4.2) show why this distinction matters: the raw outputs admit neither a common pointwise modulus nor a common `L^1` translation modulus, BV bound, positive Besov translation bound, or uniform Gaussian desmoothing rate, while the exact fixed-scale heat profiles enjoy all derivative bounds for free.

## 6. Small discrete-center consequence

The common Lipschitz constant in (5.3) gives a harmless discretization of the center variable. Put `s=s_3(A)>0`. For any `y`, choose `k\in\mathbb Z` with

\[
|y-k/s|\le \frac1{2s}.
\]

Then

\[
 sH_{A,f}(y)
\le sH_{A,f}(k/s)+\frac{1}{2\sqrt{2\pi e}}.
\tag{6.1}
\]

Consequently finiteness of the full QFORM constant is equivalent to finiteness of

\[
\sup_{A,f,k\in\mathbb Z}
 s_3(A)H_{A,f}\!\left(\frac{k}{s_3(A)}\right),
\]

up to the explicit additive constant `1/(2sqrt(2 pi e))`. This removes the continuum supremum over output centers if a grouped-coordinate argument naturally produces estimates on an adaptive lattice.

## 7. Exact implication ledger

The current regularity picture is therefore:

1. **Absolute continuity:** qualitatively available for nonconstant quadratic pushforwards of absolutely continuous joint inputs; this alone gives no uniform height.
2. **Fixed-instance boundedness and continuity:** under the target rank/product hypotheses, the completed regularity chain gives a bounded `C_0` representative with a matrix-dependent constant. Continuity is qualitatively separate from the universal-height problem.
3. **Raw target-uniform regularity:** false beyond height itself. The partner family plus this run proves failure of common pointwise modulus, common `L^1` translation modulus, common BV/`W^{1,1}` control, common positive Besov translation control, and uniform Gaussian desmoothing.
4. **Fixed-scale heat regularity:** universally `C^\infty` with the explicit derivative bounds (5.2), and exactly target-equivalent through spectral homogeneity.
5. **Universal height:** still OPEN and exactly the bound (5.4), equivalently the unit-window normal form from account03/B15.

No rotated-independence, law-uniform pointwise oscillatory decay, projection-only shortcut, arbitrary-joint coarea estimate, or positive conditional-height moment is used anywhere in these deductions.

## 8. First unpaid implication

The regularity issue is now cleanly separated from the central theorem. The next mathematical payment should be made directly in the fixed heat/window normal form:

\[
\boxed{
\sup_{A,f,y}s_3(A)\,\mathbb E\gamma_1(X^TAX-y)<\infty,
}
\]

or equivalently

\[
\boxed{
\sup_{A,f,y}\frac{s_3(A)}2\Pr\{|X^TAX-y|\le1\}<\infty.
}
\]

Any successful grouped-coordinate, ridge, physical-pivot, or aggregate-cross argument should estimate that positive fixed-scale quantity directly. Raw-output compactness or a uniform desmoothing passage cannot supply the missing constant.

Full QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**.
