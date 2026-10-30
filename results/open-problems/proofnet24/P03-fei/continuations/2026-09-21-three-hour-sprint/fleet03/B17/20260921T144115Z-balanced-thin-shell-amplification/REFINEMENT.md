# Refinement — exact-level case is already solved; thin-shell stability is false

**Status:** **PROVED reduction + REFUTED naive stability lemma; full FEI remains OPEN.**  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

This note supersedes the sentence in Section 8 of this run's `REPORT.md` that proposed the exact single-level class as a first open subproblem. A fresh cross-account repository read found that fleet01/B17 had already proved a stronger theorem earlier today:

* if the nonzero Fourier support of a Boolean function is an antichain, then `H(f)<=2I(f)`;
* in particular, if the spectrum is supported on one exact level `k`, then `H(f)<=2(k-1)<2I(f)`.

That earlier theorem uses Boolean Fourier granularity at inclusion-maximal support atoms. I do **not** re-prove or re-audit it here. Instead, combine it with the tensor-amplification theorem of this run.

## 1. PROVED: maximal-support mass tensorizes to zero unless the base support is an antichain

Let

\[
\mathcal C_f=\{A:\widehat f(A)\ne0\}
\]

and let `Max(C_f)` be its inclusion-maximal members. Define

\[
q_f:=\Pr(S_f\in \operatorname{Max}(\mathcal C_f)). \tag{1.1}
\]

For the disjoint-block tensor product `G_m=prod_j f(x^(j))`, and likewise for the balanced version `F_m=z G_m`, the support poset is the Cartesian product of the base support posets (with the compulsory `z` coordinate appended in the latter case). A tuple is inclusion-maximal if and only if every block component is inclusion-maximal. Therefore

\[
\boxed{q_{F_m}=q_{G_m}=q_f^m}. \tag{1.2}
\]

If the base support is not an antichain then `q_f<1`, so the spectral mass covered directly by the maximal-atom/antichain theorem decays exponentially under amplification.

Conversely, `q_f=1` means every support atom is maximal, i.e. the support is an antichain, and the prior fleet01 theorem already gives `H(f)<=2I(f)`. Thus every base with ratio strictly above `2` necessarily satisfies `q_f<1`, and its tensor amplifications move essentially all spectral mass into **buried** coefficients.

Targeted exact checks on the admissible stress cases give:

* two-bit one-point defect: `q_f=1/4`, and the two-copy amplification has `q=1/16`;
* three-bit majority: `q_f=1/4`, and the two-copy amplification has `q=1/16`;
* a character: `q_f=1`, consistent with antichain support and entropy zero.

These are checks of (1.2), not a finite search for FEI.

## 2. REFUTED-LEMMA: relative thinness does not approach the exact-level constant 2

A natural reaction to the exact-level `2` theorem would be to conjecture a stability principle such as

\[
\frac{H(f)}{I(f)}\le 2+o(1)
\]

whenever the Fourier degree is highly concentrated around its mean. The amplification theorem refutes every such principle based only on degree concentration.

For any Boolean base `f` with positive entropy, the balanced amplifications satisfy

\[
\frac{\operatorname{Var}K_{F_m}}{I(F_m)^2}\to0,
\qquad
\frac{H(K_{F_m})}{I(F_m)}\to0,
\qquad
p_*(F_m)\to0,
\]

while

\[
\frac{H(F_m)}{I(F_m)}\to\frac{H(f)}{I(f)}. \tag{2.1}
\]

The fresh FEI task state records an unrestricted lower bound strictly above `6.521845710923046575`. Hence, taking finite Boolean functions with ratios arbitrarily close to that lower-bound sequence and then applying (2.1), one obtains balanced Fourier-diffuse sequences with vanishing relative level variance and vanishing level-entropy fraction whose FEI ratios stay above any fixed `c<6.521845710923046575` for all sufficiently good choices.

Therefore the following candidate mechanisms are **REFUTED** as universal routes:

1. `Var(K)/I^2 -> 0` forces `H/I -> 2`;
2. `H(K)/I -> 0` forces `H/I -> 2`;
3. Fourier diffuseness `p_* -> 0`, even together with either of the preceding properties, forces an FEI constant below the true sharp constant.

The exact-level antichain theorem is consequently **not stable under relative shell concentration alone**. Arbitrarily thin relative annuli can still carry the full hard FEI ratio because the obstruction is multilevel and buried.

## 3. PROVED: the amplified entropy is genuinely localized to a sublinear-width shell

The preceding report used only variance. For a fixed base `f`, one can strengthen the statement to entropy localization.

Let `K_1,...,K_m` be the iid base spectral sizes, each lying in `[0,n]`, and let

\[
K_{F_m}=1+\sum_{j=1}^m K_j.
\]

For a nonzero base spectral atom define

\[
L(A)=\log_2\frac1{p_f(A)},
\qquad
L_{\max}=\max_{p_f(A)>0}L(A)<\infty.
\]

The information content of an amplified atom is exactly the sum of the block information contents, hence is at most `m L_max`. Hoeffding's inequality gives

\[
\Pr\left(\left|K_{F_m}-(1+mI(f))\right|>n\sqrt{m\log m}\right)
\le 2m^{-2} \tag{3.1}
\]

for `m>=2` (natural logarithm in the displayed width only changes an inessential constant). Consequently the Fourier entropy carried by the complement of that shell is bounded by

\[
\sum_{A\ \mathrm{outside}}p_{F_m}(A)\log_2\frac1{p_{F_m}(A)}
\le 2L_{\max}/m=o(1), \tag{3.2}
\]

and its influence contribution is at most

\[
(1+mn)\,2m^{-2}=O(1/m). \tag{3.3}
\]

Thus the amplification does more than make the degree variance relatively small: **all but `o(1)` bits of spectral entropy and `o(1)` influence mass lie in an `O(sqrt(m log m))`-width shell around a degree of order `m`.**

This makes the discontinuity with the exact-level constant-2 theorem especially sharp.

## 4. Next attack — buried-chain geometry, not shell width

The surviving object is now precise. Exact-level/antichain support is FEI-good with constant `2`, but a sublinear-width multilevel annulus can retain the full hard ratio while almost all maximal-support mass disappears.

A tensor-stable way to measure the missing vertical structure is the **burial depth**

\[
d_f(A):=\max\{|B|-|A|:B\in\mathcal C_f,\ A\subseteq B\}. \tag{4.1}
\]

For disjoint-block products the support poset is a Cartesian product, so

\[
\boxed{
 d_{G_m}(A_1\sqcup\cdots\sqcup A_m)
 =\sum_{j=1}^m d_f(A_j),
} \tag{4.2}
\]

and hence

\[
\mathbb E d_{G_m}(S)=m\,\mathbb E d_f(S). \tag{4.3}
\]

The next genuinely new target is therefore not an `almost one level => almost constant 2` statement; that is false. It is a **buried-atom charging theorem** that uses the Boolean convolution equations and upper-cone masses to pay the entropy of nonmaximal coefficients with bounded congestion along long support jumps. Any proposed charge must be tensor-stable enough to survive (4.2)-(4.3), must recover the existing constant-2 antichain theorem at burial depth zero, and must be stress-tested on the known high-ratio recursive constructions before promotion.

Full FEI remains **OPEN / NOT PROVED**.
