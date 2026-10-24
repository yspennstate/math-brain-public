SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-23T16:30:43Z.
attacking: an exact countable-core reduction for the universal height problem, keeping fixed-instance C0 regularity separate and applying the completed account04/B15 pivoted-convolution branch to the reduced heat functional.

# account03/B15 auto23 — countable-core heat normal form and regularity ledger

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account03/B15`  
Run: `20260923T163043Z-account03-B15-qform-auto23`  
Fresh control before publication: `yspennstate/math-research-brain@dbca08a6ad1efaa70bbb9c5124bdb22dfc1fc874`, OWNER CONTROL revision `2026-09-22.15`  
Live correction inbox blob at refresh: `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`  
Execution context: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW EXACT TARGET REDUCTION / PARTNER APPLIED / FULL UNIVERSAL HEIGHT OPEN`.

## 1. First missing implication and result of this run

Write `s_3(A)` for the third singular value of a real symmetric matrix. The central unpaid statement is

\[
C_{\rm full}:=
\sup_{\substack{n\ge3,\ s_3(A)\ge1\\ X_i\ \mathrm{independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty <\infty.
\tag{1.1}
\]

The completed account04/B15 heat-height theorem gives, in the extended sense (value `+infinity` if a bounded density does not exist),

\[
\mathfrak h(\mu)
:=\sup_{\varepsilon>0,\ y\in\mathbb R}(\mu*\gamma_\varepsilon)(y)
=\|p_\mu\|_\infty,
\qquad
\gamma_\varepsilon(u)=\frac{e^{-u^2/(2\varepsilon^2)}}{\sqrt{2\pi}\varepsilon}.
\tag{1.2}
\]

I prove the following zero-loss normal form for (1.1).

> **Theorem (countable-core normal form).** Let `R` be the countable class of finite unions of bounded half-open intervals with rational endpoints and total Lebesgue measure exactly one. Let `G_n` be the countable class of rational symmetric `n x n` matrices which have simple spectrum, all entries nonzero, and all principal minors nonzero. Then
> \[
> \boxed{
> C_{\rm full}
> =\sup_{\substack{n\ge3,\ B\in G_n,\ s_3(B)>1\\
> E_1,\dots,E_n\in R\\
> \varepsilon\in\mathbb Q_{>0},\ y\in\mathbb Q}}
> \int_{E_1\times\cdots\times E_n}
> \gamma_\varepsilon(x^TBx-y)\,dx.
> }
> \tag{1.3}
> \]
> The equality holds in `[0,+infinity]` and uses no moment, support, connectedness, smoothness, Gaussian, sign, or post-rotation-independence assumption.

Thus the full rough-input conjecture is exactly equivalent to a uniform estimate on a **countable family of compact finite-fragment product laws and algebraically generic rational matrices**. The number of interval fragments is not bounded uniformly; it is allowed to grow arbitrarily with the instance, consistent with the live correction `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`.

This does not solve the universal height problem, but it removes three possible sources of endpoint ambiguity with zero constant loss: arbitrary measurable marginal densities, algebraically degenerate matrices, and uncountable heat/output parameters.

## 2. One-coordinate bathtub purification

Let

\[
\mathcal K:=\{f\in L^1(\mathbb R):0\le f\le1,\ \int f=1\}.
\]

For a bounded nonnegative measurable function `g`,

\[
\boxed{
\sup_{f\in\mathcal K}\int f(x)g(x)\,dx
=
\sup_{|E|=1}\int_E g(x)\,dx.
}
\tag{2.1}
\]

A standard threshold/bathtub proof is enough and does not require attainment. For every `eta>0`, choose a level `c` so that the set above `c` has measure at most one while a suitable near-level enlargement has measure at least one. Since `f<=1` and `int f=1`, moving mass from points with smaller `g` to points with larger `g` cannot decrease the integral. Filling a measurable set of measure one at the top levels gives an indicator `1_E` whose integral is within `eta` of the supremum. Equivalently, (2.1) is the Hardy--Littlewood bathtub identity

\[
\sup_{f\in\mathcal K}\int fg
=\int_0^1 g^*(s)\,ds.
\]

Now fix `n,A,epsilon,y` and put

\[
G(x_1,\ldots,x_n)=\gamma_\varepsilon(x^TAx-y).
\]

For fixed `f_2,...,f_n`, integrating the other coordinates gives a bounded nonnegative measurable payoff `g_1(x_1)`. Apply (2.1) to replace `f_1` by an indicator of a unit-measure set, losing at most `eta/n`. Repeat coordinate by coordinate. Since `n` is finite,

\[
\boxed{
\sup_{f_1,\ldots,f_n\in\mathcal K}
\int G(x)\prod_i f_i(x_i)\,dx
=
\sup_{|E_1|=\cdots=|E_n|=1}
\int_{\prod_iE_i}G(x)\,dx.
}
\tag{2.2}
\]

No claim is made that a single optimizer exists, that an optimizer is an interval, or that a bounded number of components suffices.

## 3. Finite rational interval sets are dense with no loss

Let `E subset R` be measurable with `|E|=1`. For every `delta>0` there exists `F in R` such that

\[
|E\triangle F|<\delta.
\tag{3.1}
\]

Proof: first truncate `E` to a large bounded interval, losing arbitrarily little mass. By regularity of Lebesgue measure, approximate the bounded remainder in symmetric difference by a finite union `U` of intervals; perturb its endpoints to rationals, preserving a small symmetric-difference error. The number `|U|` is then rational. If `|U|<1`, add a disjoint rational interval of length `1-|U|`; if `|U|>1`, shave a total rational length `|U|-1` from finitely many component intervals. The resulting finite union has rational endpoints, exact mass one, and remains arbitrarily close to `E` in symmetric difference.

For unit-mass one-dimensional densities `f_i,g_i`, the product-density telescoping identity gives

\[
\left\|
\prod_{i=1}^n f_i-\prod_{i=1}^n g_i
\right\|_{L^1(\mathbb R^n)}
\le
\sum_{i=1}^n\|f_i-g_i\|_1.
\tag{3.2}
\]

With indicator densities this is

\[
\left\|
\prod_i1_{E_i}-\prod_i1_{F_i}
\right\|_1
\le\sum_i|E_i\triangle F_i|.
\tag{3.3}
\]

Since `||gamma_epsilon||_infinity=(sqrt(2pi) epsilon)^(-1)`,

\[
\left|
\int G\prod_i1_{E_i}-
\int G\prod_i1_{F_i}
\right|
\le
\frac1{\sqrt{2\pi}\varepsilon}
\sum_i|E_i\triangle F_i|.
\tag{3.4}
\]

Hence the right side of (2.2) has the same supremum if every `E_i` is required to lie in `R`.

The live no-fixed-fragment correction is respected: (3.1) uses a finite number of intervals depending on `E` and `delta`; no uniform component count appears anywhere.

## 4. Generic rational matrices are dense inside the target after an arbitrarily small outward spectral dilation

Fix a dimension `n`. The conditions

- every matrix entry is nonzero,
- every principal minor is nonzero,
- the characteristic polynomial has no repeated root,

are the nonvanishing of finitely many nonzero polynomials in the `n(n+1)/2` symmetric matrix entries. Their simultaneous complement is therefore an open dense Zariski-generic subset of `Sym_n(R)`. Rational points are dense in it, so the class `G_n` defined in Section 1 is dense in `Sym_n(R)`.

Now let `A` satisfy `s_3(A)>=1`. For `delta>0` set

\[
A^{(\delta)}=(1+\delta)A.
\]

Then

\[
s_3(A^{(\delta)})\ge1+\delta.
\tag{4.1}
\]

Choose `B_delta in G_n` with

\[
\|B_\delta-A^{(\delta)}\|_{op}<\delta/2.
\tag{4.2}
\]

Weyl's singular-value inequality gives

\[
s_3(B_\delta)>1+\delta/2>1.
\tag{4.3}
\]

Also `B_delta -> A` as `delta ->0` (after choosing the rational approximation error to tend to zero).

For fixed `E_i in R`, the product support

\[
K=E_1\times\cdots\times E_n
\]

is compact. Hence `x^TB_delta x -> x^TAx` uniformly on `K`, and therefore for fixed positive `epsilon` and real `y`,

\[
\int_K\gamma_\varepsilon(x^TB_\delta x-y)\,dx
\longrightarrow
\int_K\gamma_\varepsilon(x^TAx-y)\,dx.
\tag{4.4}
\]

This is the correct way to remove exact algebraic degeneracies here: the compact finite-fragment reduction is performed first, so no moment or bounded-support assumption is imposed on the original target law.

## 5. Rational heat scales and output centers

For each compact core instance `(B,E_1,...,E_n)`, the map

\[
(\varepsilon,y)\mapsto
\int_{\prod E_i}\gamma_\varepsilon(x^TBx-y)\,dx
\tag{5.1}
\]

is continuous on `(0,infinity) x R`, by uniform continuity of the Gaussian kernel on compact parameter neighborhoods and dominated convergence. Therefore

\[
\sup_{\varepsilon>0,y\in\mathbb R}(5.1)
=
\sup_{\varepsilon\in\mathbb Q_{>0},y\in\mathbb Q}(5.1).
\tag{5.2}
\]

The core parameter family in (1.3) is consequently countable.

## 6. Proof of the countable-core theorem

The right side of (1.3) is at most `C_full`, because every core marginal `1_E` is an admissible cap-one probability density and every core matrix satisfies `s_3(B)>1`.

For the reverse inequality, fix an arbitrary target instance, positive heat scale `epsilon`, center `y`, and `eta>0`.

1. By Section 2, replace the arbitrary cap-one marginals successively by unit-measure indicator sets, losing less than `eta/4`.
2. By Section 3, approximate those sets by members of `R`, losing less than `eta/4` in the heat expectation.
3. By Section 4, approximate `A` by a matrix `B in G_n` with `s_3(B)>1`, losing less than `eta/4`.
4. By Section 5, approximate `(epsilon,y)` by positive-rational/rational parameters, losing less than `eta/4`.

Thus every heat value from every rough target instance lies within `eta` of a value in the countable core. Taking suprema and then `eta downarrow0` gives (1.3).

Combining this with the completed account04/B15 heat-height identity (1.2) proves that **a single uniform bound on the countable core is logically equivalent to the full universal essential-density bound**. This is exact, not a compactness heuristic or a finite numerical certification.

## 7. Absolute continuity, bounded density, and continuity are separate assertions

Three levels should not be conflated.

### 7.1 Absolute continuity

For any nonzero symmetric `A` and any absolutely continuous joint input law, the pushforward by `q(x)=x^TAx` is absolutely continuous. The coarea argument on the sets

\[
\{x:|x|\le k,\ |\nabla q(x)|\ge1/k\}
\]

shows that the preimage of every one-dimensional null set is null away from `ker A`; the critical linear subspace `ker A` is itself null when `A!=0`. Product structure is not needed for this qualitative statement.

### 7.2 Essential boundedness

The universal assertion is exactly finiteness of (1.3), via (1.2). The countable-core reduction does not establish finiteness; it only removes irrelevant rough/generic endpoints with zero constant loss.

### 7.3 Continuous representative

A completed existing-worker theorem, account02/B15 at

`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`,

proves for every fixed real symmetric `A` with `rank(A)>=3` and every cap-one independent product law that

\[
\boxed{p_{X^TAX}\in C_0(\mathbb R)\cap L^\infty(\mathbb R),}
\tag{7.1}
\]

with an instance-dependent constant. I read the complete report in this run. I use it as a completed existing-worker premise, not as a second independent end-to-end review of its entire dependency chain.

Therefore, under the target hypothesis `s_3(A)>=1`, the stronger qualitative continuity assertion is already separated from the missing universal height: once (1.3) is bounded by a universal `C`, the same fixed-instance `C_0` representative automatically satisfies

\[
\max_x p_Q(x)=\|p_Q\|_\infty\le C.
\tag{7.2}
\]

No universal modulus of continuity is needed to obtain the owner's `continuous density + universal height` formulation. This is materially stronger than trying to deduce continuity from an abstract `L^infinity` estimate, which would be false in general.

The shared `CLAIMS.json` still lists `QFORM-CONTINUOUS-REPRESENTATIVE` as open; this run does not edit the protected/shared claim ledger. The source-complete fixed-instance theorem above should be distinguished from the still-open universal-height claim by the authorized consolidator.

## 8. Actual application of completed partner account04/B15

The newest completed partner result is account04/B15 r6:

`yspennstate/math-open-problems@cff8e1368d32302e6d649f776579a5c1951929b1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T151702Z-account04-B15-pivoted-convolution-r6/REPORT.md`.

For independent cap-one `X,Y`, arbitrary `a,u,v,c`, and `b!=0`, it proves

\[
\|p_{aX^2+2bXY+2uX+2vY+c}\|_3
\le3|b|^{-2/3}.
\tag{8.1}
\]

For an independent cap-one `Z`, arbitrary linear term and `gamma!=0`, it proves

\[
\|p_{\gamma Z^2+2wZ}\|_{3/2}
\le2|\gamma|^{-1/3}.
\tag{8.2}
\]

On the physical principal block

\[
\begin{pmatrix}
a&b&0\\
b&0&0\\
0&0&\gamma
\end{pmatrix},
\tag{8.3}
\]

with arbitrary outside block and arbitrary couplings to the three selected original coordinates, conditioning on the outside variables creates only affine terms. Conjugate-exponent convolution therefore gives the actual target inequality

\[
\boxed{
\|p_Q\|_\infty
\le6|b|^{-2/3}|\gamma|^{-1/3}.
}
\tag{8.4}
\]

Applying the completed account04/B15 heat-height identity (1.2) to (8.4) yields, for every such instance,

\[
\boxed{
\sup_{\varepsilon>0,y}
\mathbb E\gamma_\varepsilon(Q-y)
\le6|b|^{-2/3}|\gamma|^{-1/3}.
}
\tag{8.5}
\]

Hence on the countable core the same inequality holds after restricting `epsilon,y` to rationals. If

\[
b^2\ge|a|+1,\qquad |\gamma|\ge1,
\]

then the three displayed physical-block eigenvalues have modulus at least one and

\[
\boxed{
\sup_{\varepsilon\in\mathbb Q_{>0},y\in\mathbb Q}
\mathbb E\gamma_\varepsilon(Q-y)\le6.
}
\tag{8.6}
\]

This is a genuine application of the designated partner result to the exact functional used in the new reduction, not merely a citation.

## 9. What the reduction does and does not buy

The reduction has two concrete consequences for future full-target work.

First, one may prove the universal constant on compact finite-fragment indicator inputs and algebraically generic rational matrices only. Rough densities, exact zero pivots, repeated eigenvalues, irrational coefficients, and arbitrary heat centers then follow automatically with the **same constant**.

Second, this cannot be turned into a finite computation. The component count of the rational interval sets is unbounded, dimension is unbounded, the matrix denominator/conditioning can degenerate, and `epsilon` may tend to zero. The live fragmented-support corrections remain fully active.

Thus the first unpaid implication remains mathematical rather than regularity-theoretic:

\[
\boxed{
\sup_{\text{countable core in (1.3)}}
\mathbb E\gamma_\varepsilon(X^TBX-y)<\infty.
}
\tag{9.1}
\]

The strongest next use of (1.3) is to attack (9.1) with a product-preserving grouped-bank/ridge inequality while freely assuming generic physical coefficients and finite-fragment compact sources. Any estimate must remain independent of the number and separation of fragments and must survive degeneration back to the excluded algebraic boundary.

## 10. Integrity ledger

- Full universal QFORM constant: **OPEN / NOT PROVED / NOT DISPROVED**.
- New theorem: exact countable-core heat normal form (1.3).
- Absolute continuity: qualitatively true for every nonzero quadratic under any absolutely continuous joint input.
- Fixed-instance bounded `C_0` density for rank `>=3`: source-complete existing-worker theorem read in full; constants are not universal.
- Universal continuity modulus: not claimed and not needed for the owner's continuous-density conclusion once universal height is proved.
- Partner actually applied: account04/B15 r6 at (8.4)--(8.6), together with account04/B15 r4 heat-height identity.
- No post-rotation independence, pointwise van-der-Corput decay, arbitrary-joint coarea height bound, conditional projection positive moment, fiber supremum, fixed fragment-count, or small-random-error argument is used.
- No moment, support, connected-support, log-concavity, Gaussian, centering, or same-sign assumption is added to the full reduction.
- The new generic/compact assumptions are only a dense **test core** under a zero-loss supremum identity; they are not silently imposed on the target itself.
