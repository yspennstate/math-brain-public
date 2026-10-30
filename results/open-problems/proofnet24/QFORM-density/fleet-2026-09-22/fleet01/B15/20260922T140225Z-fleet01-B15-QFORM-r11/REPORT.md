# fleet01/B15 — exact Lipschitz regularization reduction for the full QFORM density target

**Run:** `20260922T140225Z-fleet01-B15-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Absolute continuity and regularity  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_REGULARITY_REDUCTION / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source pins

The full target remains open: find one finite universal constant `C` such that for every `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues with absolute value at least `1`, the law of

\[
Q=X^TAX
\]

has a density with essential supremum at most `C`.

A continuous representative is a separate stronger conclusion.

Fresh control source at the start of the run:

- `yspennstate/math-research-brain@da63bbaba29461947597c208482f78df70fb4e59`, later refreshed through `1c72889ff03a7a863e29de9f16ec267b83ac2590` before the scientific write;
- owner-control revision `2026-09-22.5`;
- live corrections include failure of law-uniform pointwise quadratic Fourier decay, naive fiber-supremum dimension-free bounds, conditional-cap substitutes for independence, and the local-good-block/rank-three-cross-cut dichotomy. None of those false statements is used below.

### Named partner result applied

I use the completed `fleet02/B15` result

`yspennstate/math-open-problems@b1d930ff0fbc625393aebcd4a59f9ba1ead465ed`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T130201Z-fleet02-B15-qform-r2/REPORT.md`.

Its exact Choquet theorem states that every admissible one-dimensional density `f` (`0<=f<=1`, `int f=1`) is an exact probability barycenter of indicator densities `1_E` with `|E|=1`; independent representing measures give an exact mixture of product-indicator input laws. It also proves that no law-uniform modulus of continuity can hold even for fixed `A=I_3`, so continuity must not be closed by an equicontinuity argument.

The new result below uses that exact mixture at the level of the central interval inequality and removes continuity as an obstruction to proving the `L^infinity` theorem: the full target is equivalent, with **the same constant**, to a subclass whose output densities are automatically globally Lipschitz.

---

## 2. A fixed admissible one-coordinate smoothing law

Define

\[
\rho(z)=(1-|z-2|)_+.
\]

Then `rho` is supported on `[1,3]`, satisfies `0<=rho<=1`, and

\[
\int_{\mathbb R}\rho(z)\,dz=1.
\]

Thus a random variable `Z` with density `rho` is an admissible input under the owner's hypotheses.

Let `W=Z^2`. Since `Z>0`, `W` has density

\[
k(u)=\frac{\rho(\sqrt u)}{2\sqrt u}\,\mathbf 1_{[1,9]}(u).
\]

Explicitly,

\[
k(u)=
\begin{cases}
\frac12-\frac1{2\sqrt u},&1\le u\le4,\\[1mm]
\frac3{2\sqrt u}-\frac12,&4\le u\le9,\\[1mm]
0,&\text{otherwise}.
\end{cases}
\]

Hence `k` is compactly supported and continuous, with

\[
\boxed{\|k\|_\infty=\frac14.}
\]

Moreover, on `(1,4)` and `(4,9)`,

\[
k'(u)=\frac1{4u^{3/2}},\qquad
k'(u)=-\frac3{4u^{3/2}},
\]

respectively. The endpoint values match zero and the two formulas match continuously at `u=4`, so the piecewise derivative bound yields the global Lipschitz estimate

\[
\boxed{\operatorname{Lip}(k)\le\frac14.}
\]

For `0<\varepsilon<1`, the random variable `\varepsilon W=\varepsilon Z^2` has density

\[
k_\varepsilon(s)=\varepsilon^{-1}k(s/\varepsilon),
\]

supported on `[\varepsilon,9\varepsilon]`, with

\[
\boxed{
\|k_\varepsilon\|_\infty=\frac1{4\varepsilon},
\qquad
\operatorname{Lip}(k_\varepsilon)\le\frac1{4\varepsilon^2}.
}
\tag{2.1}
\]

The family `(k_\varepsilon)` is a one-sided approximate identity as `\varepsilon\downarrow0`.

---

## 3. Every target law has an automatically Lipschitz target-admissible regularization

Let `mu_Q` be the law of an arbitrary real random variable `Q`; no density is needed for this step. Take `Z` above independent of `Q` and set

\[
Q_\varepsilon=Q+\varepsilon Z^2.
\]

Then `Q_\varepsilon` has the density

\[
\boxed{
p_\varepsilon(t)=\int k_\varepsilon(t-q)\,d\mu_Q(q).
}
\tag{3.1}
\]

Because `mu_Q` is a probability measure and `k_\varepsilon` is bounded Lipschitz,

\[
\boxed{
\|p_\varepsilon\|_\infty\le\frac1{4\varepsilon},
\qquad
|p_\varepsilon(t+h)-p_\varepsilon(t)|
\le\frac{|h|}{4\varepsilon^2}.
}
\tag{3.2}
\]

So `p_\varepsilon` is globally Lipschitz, independently of any regularity of the original law.

Now return to the QFORM target. For an admissible base instance `(X,A)`, append the independent coordinate `Z` and define

\[
\widetilde A_\varepsilon=A\oplus[\varepsilon].
\]

Its eigenvalues are those of `A` together with `\varepsilon`. Since `0<\varepsilon<1`, the original three eigenvalues of modulus at least one remain unchanged. Therefore

\[
Q_\varepsilon=(X,Z)^T\widetilde A_\varepsilon(X,Z)
= X^TAX+\varepsilon Z^2
\]

is itself a **fully target-admissible quadratic-form instance**. Thus the owner target contains, for every base instance and every `\varepsilon`, a canonical globally Lipschitz regularization of that same base law.

---

## 4. Exact constant-preserving equivalence

### Theorem 4.1 — `QFORM-LIPSCHITZ-REGULARIZATION-EQUIVALENCE-v1`

Fix a finite constant `C`. The following are equivalent.

**(FULL-C)** For every target-admissible `(X,A)`, the law of `Q=X^TAX` has a density satisfying

\[
\|p_Q\|_\infty\le C.
\]

**(REG-C)** For every target-admissible `(X,A)` and every `0<\varepsilon<1`, the regularized target instance

\[
Q_\varepsilon=X^TAX+\varepsilon Z^2
\]

has a density satisfying

\[
\|p_\varepsilon\|_\infty\le C,
\]

where `Z` has the fixed density `rho` from Section 2.

Every density appearing in (REG-C) is automatically globally Lipschitz by (3.2).

#### Proof

`FULL-C => REG-C` is immediate because `\widetilde A_\varepsilon` is target-admissible and `rho<=1`.

For the reverse implication, fix one base target instance and let `mu_\varepsilon` and `mu` denote the laws of `Q_\varepsilon` and `Q`. Since `Z` is finite almost surely,

\[
\varepsilon Z^2\to0\quad\text{a.s.},
\]

hence `Q_\varepsilon=>Q` and `mu_\varepsilon=>mu` weakly as `\varepsilon\downarrow0`.

For every bounded open interval `I`, Portmanteau and (REG-C) give

\[
\mu(I)
\le \liminf_{\varepsilon\downarrow0}\mu_\varepsilon(I)
\le C|I|.
\tag{4.1}
\]

By countable decomposition of open sets into intervals and outer regularity,

\[
\boxed{\mu(B)\le C|B|\quad\text{for every Borel }B.}
\tag{4.2}
\]

Therefore `mu<<Leb` and its Radon--Nikodym density satisfies `||p_Q||_infinity<=C`. This is (FULL-C). `QED`.

### Exact norm recovery when the base density is bounded

If `mu_Q=p_Q dt` with `p_Q in L^infinity`, then

\[
p_\varepsilon=p_Q*k_\varepsilon.
\]

Because `(k_\varepsilon)` is an approximate identity,

\[
\|p_\varepsilon-p_Q\|_1\to0,
\]

and at every Lebesgue point of `p_Q`, `p_\varepsilon(t)\to p_Q(t)`. Convolution gives the contraction

\[
\|p_\varepsilon\|_\infty\le\|p_Q\|_\infty.
\]

Given `eta>0`, by the definition of essential supremum there is a Lebesgue point `t` with

\[
p_Q(t)>\|p_Q\|_\infty-\eta.
\]

Hence

\[
\liminf_{\varepsilon\downarrow0}\|p_\varepsilon\|_\infty
\ge p_Q(t)
>\|p_Q\|_\infty-\eta.
\]

Letting `eta\downarrow0` gives the exact identity

\[
\boxed{
\lim_{\varepsilon\downarrow0}\|p_Q*k_\varepsilon\|_\infty
=\|p_Q\|_\infty.
}
\tag{4.3}
\]

Thus the regularization loses **no density constant at all** in the limit.

---

## 5. Applying the named fleet02/B15 Choquet theorem to the central inequality

The partner theorem gives, for each admissible marginal `f_i`, a probability measure `Pi_i` on measure-one sets `E_i` such that `f_i` is the exact barycenter of `1_{E_i}`. Let

\[
\Pi=\Pi_1\otimes\cdots\otimes\Pi_n.
\]

Hold the fixed auxiliary variable `Z` from Section 2 independent of everything. The partner's exact product-law mixture then gives, at the level of output probability measures,

\[
\boxed{
\mu_{f,\varepsilon}
=
\int \mu_{E,\varepsilon}\,d\Pi(E),
}
\tag{5.1}
\]

where

\[
Q_{E,\varepsilon}=X_E^TAX_E+\varepsilon Z^2,
\qquad
X_{E,i}\sim\mathbf 1_{E_i},\quad |E_i|=1.
\]

Consequently, if one proves for all such regularized extreme inputs that

\[
\mu_{E,\varepsilon}(I)\le C|I|
\quad\text{for every interval }I,
\tag{5.2}
\]

then (5.1) immediately yields

\[
\mu_{f,\varepsilon}(I)
=
\int\mu_{E,\varepsilon}(I)d\Pi(E)
\le C|I|.
\tag{5.3}
\]

Theorem 4.1 then lets `\varepsilon\downarrow0` and recovers the full original target with the **same** `C`.

Therefore the full QFORM conjecture is exactly equivalent to the following apparently stronger-looking but actually lossless regularized-extreme statement:

> For every target matrix `A`, every product of measure-one indicator marginals, and every `0<\varepsilon<1`, the target-admissible output `X_E^TAX_E+\varepsilon Z^2` has density at most one universal `C`.

Every output in this reduced class is already globally Lipschitz before the hard estimate is proved.

This is a direct mathematical use of the completed partner result: its exact barycentric identity is inserted into the interval inequality (5.2)--(5.3), not merely cited.

---

## 6. What this does and does not solve about continuity

The reduction removes continuity as a prerequisite for proving the central `L^infinity` theorem. One may, without loss of the target constant, attack only globally Lipschitz regularized outputs and then remove the regularizer by weak convergence.

It does **not** prove that the unregularized density `p_Q` itself has a continuous representative. The Lipschitz constant in (3.2) is `O(\varepsilon^{-2})`, so there is intentionally no equicontinuity as `\varepsilon\downarrow0`. This is fully compatible with fleet02/B15's target-valid construction showing that no law-uniform modulus of continuity exists even on the extreme diagonal family.

Thus the regularity ledger is now:

1. qualitative absolute continuity of the unregularized target is already known from the earlier nonconstant-polynomial/coarea argument;
2. the universal `L^infinity` conjecture is **exactly equivalent** to its globally Lipschitz one-small-eigenvalue regularization, with no loss of `C`;
3. original-output continuity remains a genuinely separate stronger question;
4. if individual continuity is eventually proved for every extreme unregularized output, the partner Choquet theorem transfers it to arbitrary admissible marginals without a common modulus.

---

## 7. First unpaid implication after this run

This run does not close the universal constant. It changes the admissible proof target without weakening it.

The next central implication may now be attacked under the additional, free output regularity

\[
Q\mapsto Q+\varepsilon Z^2,
\qquad p_\varepsilon\in C^{0,1},
\]

while retaining arbitrary dimension, arbitrary product marginals, arbitrary rotated/indefinite `A`, and the exact three-large-eigenvalue hypothesis. In particular, any argument that needed pointwise evaluation, continuous representatives, or a legitimate mollified density may work at fixed `\varepsilon`; **all constants must remain independent of `\varepsilon`** before passing to the limit.

The hard unpaid inequality is therefore:

\[
\boxed{
\sup_{0<\varepsilon<1}
\sup_{A,E,t,h}
\frac{\Pr\{X_E^TAX_E+\varepsilon Z^2\in[t,t+h]\}}{h}
<\infty,
}
\]

where `A` ranges over the full target spectral class and each `E_i` is an arbitrary measurable set of measure one.

The existing corrections still forbid replacing this by law-uniform pointwise Fourier decay, rotated independence, conditional density caps, a single coordinate minor, or a fixed cross-rank dichotomy.

**Full QFORM status:** `OPEN_NOT_PROVED`.
