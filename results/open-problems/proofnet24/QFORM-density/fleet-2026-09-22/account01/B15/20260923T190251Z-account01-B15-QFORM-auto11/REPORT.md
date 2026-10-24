SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T19:02:51Z.
attacking: zero-loss closure to smooth/analytic cap-one sources and generic physical matrices; separate essential L-infinity closure from continuity and apply account02/B15's Gaussian-mixture obstruction to the exact closure topology.

# account01/B15 auto11 — zero-loss generic/analytic core for the exact QFORM constant

Programme: `QFORM-DENSITY-3EIG-20260922`, activation revision `2026-09-22.5`.
Fresh control read before mathematics: `yspennstate/math-research-brain@d17c1533474a2107cc16189027e53776911e1d2d`, then rechecked on newer main `9f4943c284ef94dabf8c3337b9accb825b45e59f`; OWNER CONTROL revision remains `2026-09-22.15` and no later B15 stop appeared.
Execution context: `WITHOUT_VERIFIED_BRAIN`.
Status: `NEW TARGET-LEVEL REGULARITY LEMMA / ZERO-LOSS DENSE CORE / FULL QFORM OPEN`.

The main new result is that the sharp universal density constant is unchanged if one simultaneously restricts to (i) strictly positive real-analytic Schwartz cap-one marginals and (ii) a countable dense generic class of rational symmetric matrices with simple spectrum and every principal minor nonzero. This removes rough-source and algebraic-degeneracy issues from the quantitative theorem without using continuity. A second result shows, using the completed `account02/B15` theorem, that this valid dense core cannot be replaced by Gaussian location-scale mixtures with any fixed inverse-scale budget.

## 1. Exact height functional on measures

For a finite positive Borel measure `mu` on `R`, define

\[
D_\infty(\mu):=\inf\{C\in[0,\infty]:\mu(E)\le C|E|\text{ for every Borel }E\}.
\]

Equivalently,

\[
\boxed{
D_\infty(\mu)=\sup_{I\subset\mathbb R\text{ bounded open interval}}\frac{\mu(I)}{|I|}.
}
\tag{1.1}
\]

Indeed `mu<=C dx` implies the interval inequalities. Conversely, if every bounded open interval obeys `mu(I)<=C|I|`, then every open set, as a countable disjoint union of intervals, obeys the same domination, and outer regularity yields `mu(E)<=C|E|` for every Borel set. Hence `mu=p dx` with `0<=p<=C` a.e.

Thus `D_infty(mu)` is exactly the essential `L^infty` density height when a bounded density exists, and is `+infinity` otherwise. No continuity representative is involved.

## 2. New lemma: weak lower semicontinuity of density height

### Lemma 2.1 — `QFORM-HEIGHT-WEAK-LSC-v1`

If finite positive measures `mu_m => mu` weakly, then

\[
\boxed{
D_\infty(\mu)\le \liminf_{m\to\infty}D_\infty(\mu_m).
}
\tag{2.1}
\]

### Proof

Let `L=liminf D_infty(mu_m)` and pass to a subsequence along which the liminf is attained. For every bounded open interval `I`, Portmanteau gives

\[
\mu(I)\le\liminf_m\mu_m(I)
\le |I|\liminf_mD_\infty(\mu_m)=L|I|.
\]

Taking the supremum in (1.1) gives (2.1). QED.

This is the correct closure principle for the central theorem. Uniform essential-height bounds survive weak limits with **zero loss**. By contrast, continuity does not survive weak convergence even under a common `L^infty` bound; see Section 7.

## 3. Joint stability under source and matrix approximation

Let `A_m -> A` in operator norm in fixed dimension `n`, and let product probability laws

\[
P_m=\bigotimes_{i=1}^n\mu_{i,m},\qquad
P=\bigotimes_{i=1}^n\mu_i,
\]

satisfy `mu_{i,m} => mu_i` for each `i`. Then `P_m=>P`. Since

\[
q_m(x)=x^TA_mx\to q(x)=x^TAx
\]

uniformly on every bounded subset of `R^n`, tightness of `P_m` and the usual compact truncation argument imply

\[
\boxed{
(q_m)_\#P_m\Rightarrow q_\#P.
}
\tag{3.1}
\]

Combining with Lemma 2.1 gives

\[
D_\infty(\mathcal L(X^TAX))
\le
\liminf_mD_\infty(\mathcal L((X^{(m)})^TA_mX^{(m)})).
\tag{3.2}
\]

Because the third singular value `s_3(A)` is continuous,

\[
\boxed{
s_3(A)D_\infty(\mathcal L(X^TAX))
\le
\liminf_m s_3(A_m)
D_\infty(\mathcal L((X^{(m)})^TA_mX^{(m)}))
}
\tag{3.3}
\]

whenever `s_3(A)>0`.

Equation (3.3) is a scale-covariant lower-semicontinuity statement for the exact QFORM objective.

## 4. Every cap-one source has a cap-preserving analytic Schwartz approximation

### Lemma 4.1 — `QFORM-CAP1-ANALYTIC-DENSITY-CORE-v1`

Let `f` be any probability density on `R` with `0<=f<=1`. There exist strictly positive real-analytic Schwartz probability densities `g_m` such that

\[
0<g_m\le1,
\qquad
\|g_m-f\|_1\to0.
\tag{4.1}
\]

The same is true with `g_m in C_c^infinity` if strict positivity/analyticity is not required.

### Proof

Choose `R` so that

\[
\delta_R:=\int_{|x|>R}f(x)\,dx\to0.
\]

Take an interval `J_R` of length `delta_R` lying outside `[-R,R]` and define

\[
h_R=f\mathbf1_{[-R,R]}+\mathbf1_{J_R}.
\]

Then `0<=h_R<=1`, `int h_R=1`, `h_R` has compact support, and

\[
\|h_R-f\|_1\le2\delta_R.
\tag{4.2}
\]

Let `gamma_epsilon` be a Gaussian probability kernel. Then

\[
g_{R,\varepsilon}=h_R*\gamma_\varepsilon
\]

has mass one, satisfies `0<g_{R,epsilon}<=1`, is real analytic and Schwartz, and tends to `h_R` in `L^1` as `epsilon downarrow0`. Choosing `epsilon=epsilon(R)` gives (4.1). Replacing the Gaussian by a compactly supported smooth approximate identity gives the `C_c^infinity` version. QED.

For a fixed number of coordinates, the product approximation is also `L^1`:

\[
\left\|\prod_{i=1}^ng_{i,m}-\prod_{i=1}^nf_i\right\|_1
\le\sum_{i=1}^n\|g_{i,m}-f_i\|_1.
\tag{4.3}
\]

Thus independence and the coordinate density cap are preserved exactly throughout the approximation; no rotation is used.

## 5. Generic matrices form a dense target-valid core

For fixed `n`, let `G_n` be the set of real symmetric matrices with

1. simple spectrum, and
2. every nonempty principal minor nonzero.

The complement of `G_n` is a finite union of zero sets of nonzero polynomials: the spectral discriminant and the principal-minor determinants. Hence `G_n` is open dense. Since rational symmetric matrices are dense, `G_n cap Sym_n(Q)` is dense as well.

Given any target matrix `A` with `s_3(A)>=1`, set `A^(epsilon)=(1+epsilon)A`. Then `s_3(A^(epsilon))>=1+epsilon`. Choose a rational generic symmetric matrix `B_epsilon` so close to `A^(epsilon)` that Weyl's inequality gives

\[
s_3(B_\varepsilon)>1.
\]

As `epsilon downarrow0` one may choose

\[
B_\varepsilon\to A.
\tag{5.1}
\]

Therefore every target matrix is a limit of target-valid matrices with rational entries, simple spectrum, and no singular physical principal block of any order.

This reduction does **not** assert that a reciprocal-minor proof may pay constants that blow up near the excluded algebraic hypersurfaces. It says that a genuinely universal estimate established on the generic class, with the same constant independent of the approaching minors, automatically extends to the degenerate class.

## 6. Main theorem: exact sharp constant on the generic analytic core

Let

\[
C_*:=\sup s_3(A)D_\infty(\mathcal L(X^TAX)),
\tag{6.1}
\]

where the supremum ranges over all dimensions, all real symmetric `A` with `s_3(A)>0`, and all independent probability densities `f_i<=1`. Equivalently one may normalize `s_3(A)>=1`.

Let `C_gen` be the same supremum restricted simultaneously to

- rational symmetric `A` with `s_3(A)>1`, simple spectrum and every principal minor nonzero;
- independent strictly positive real-analytic Schwartz probability densities `f_i<=1`.

### Theorem 6.1 — `QFORM-GENERIC-ANALYTIC-ZERO-LOSS-REDUCTION-v1`

\[
\boxed{C_*=C_{gen}.}
\tag{6.2}
\]

The same equality holds if the source class is instead restricted to `C_c^infinity` cap-one probability densities.

### Proof

The inequality `C_gen<=C_*` is immediate. For the reverse, fix an arbitrary target instance `(A,f_1,...,f_n)`. Apply Lemma 4.1 to choose analytic cap-one product approximants and Section 5 to choose generic rational target-valid matrices `A_m->A`. By (3.1), the corresponding output laws `mu_m` converge weakly to the original output law `mu`. Lemma 2.1 and continuity of `s_3` give

\[
s_3(A)D_\infty(\mu)
\le\liminf_m s_3(A_m)D_\infty(\mu_m)
\le C_{gen}.
\]

Taking the supremum over the original target class proves `C_*<=C_gen`. QED.

### Consequence

To prove the full universal QFORM theorem with constant `C`, it is enough to prove it for the following extremely regular dense core:

\[
\boxed{
A\in Sym_n(Q),\ s_3(A)>1,\ A\text{ generic as above};\qquad
f_i>0\text{ real analytic Schwartz},\ f_i\le1.
}
\tag{6.3}
\]

No rough source, singular physical block, repeated eigenvalue, or zero diagonal/minor needs to be treated separately **provided the estimate obtained on this core is uniform**. This is a zero-loss target reduction, not a proof of the missing universal estimate.

## 7. Exact separation from continuity

The completed `account02/B15` source-pinned target regularity theorem at

`yspennstate/math-open-problems@d7711eb8aa9ec8d3a908960bb1fa60334614f79d`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T160529Z-account02-B15-qform-r4/REPORT.md`

proves that every fixed product target with `rank(A)>=3` has a bounded density in `C_0(R)`, with a matrix-dependent physical-block constant. I use that theorem only as a qualitative regularity input; it does not provide the universal constant.

Therefore, at target scope, once a universal essential estimate

\[
D_\infty(\mu_Q)\le C/s_3(A)
\]

is proved, the canonical continuous representative automatically satisfies the **same pointwise constant**:

\[
\boxed{
\max_t p_Q(t)=\|p_Q\|_{\infty,\mathrm{ess}}\le C/s_3(A).
}
\tag{7.1}
\]

Indeed if a continuous representative exceeded the essential bound at one point, it would exceed it on an interval of positive measure.

But continuity is not supplied by the closure theorem itself. Even

\[
p_m=\mathbf1_{[0,1]}*\eta_{1/m}
\]

with a smooth compactly supported approximate identity satisfies `0<=p_m<=1`, `p_m in C_c^infinity`, and `p_m->1_[0,1]` in `L^1`, while the limit has no continuous representative. Thus bounded density is weakly/L1 closed at fixed height; `C_0` regularity is not. This is why continuity must remain a separate theorem and must not be smuggled into the universal-height proof.

Combining the partner's `C_0` theorem with Theorem 6.1 gives an attained-maximum version of the dense core:

\[
\boxed{
C_*=\sup_{\text{generic analytic core}} s_3(A)\max_{t\in\mathbb R}p_Q(t).
}
\tag{7.2}
\]

## 8. Required partner application: a fixed inverse-scale Gaussian-mixture core is NOT dense

The newest completed `account02/B15` theorem is at

`yspennstate/math-open-problems@ff206f9526f7feabb1132bf73f6304535f4c49ec`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260923T180250Z-account02-B15-qform-auto12/REPORT.md`,

with the fractional strengthening at `2ac62a78dee18a04890763dbe299690b9f42600e`.

For a Gaussian location-scale mixture

\[
g(x)=\int\gamma_\sigma(x-m)\,\Pi(dm,d\sigma),
\qquad K(\Pi)=\int\sigma^{-1}\,d\Pi,
\]

that completed theorem proves

\[
\operatorname{Var}(g)\le\sqrt{2/\pi}\,K(\Pi),
\tag{8.1}
\]

and the same inequality lower-semicontinuously at weak limits:

\[
\operatorname{Var}(g)\le\sqrt{2/\pi}\liminf_mK(\Pi_m).
\tag{8.2}
\]

Apply it to the explicit smooth cap-one density

\[
f_{N,\delta}=\mathbf1_{E_N}*\eta_\delta,
\]

where `E_N` is a union of `N` separated intervals of total length one and the compact mollifier neighborhoods of the `2N` endpoints are disjoint. Then

\[
0\le f_{N,\delta}\le1,
\qquad \int f_{N,\delta}=1,
\qquad
\boxed{\operatorname{Var}(f_{N,\delta})=2N.}
\tag{8.3}
\]

If Gaussian mixtures `g_m` with `K(Pi_m)<=K_0` converged weakly to this member of the valid smooth QFORM core, (8.2) would give the actual inequality

\[
2N\le\sqrt{2/\pi}K_0,
\]

or equivalently

\[
\boxed{K_0\ge N\sqrt{2\pi}.}
\tag{8.4}
\]

For any fixed finite `K_0`, choose `N>K_0/sqrt(2*pi)`. Then (8.4) is impossible.

Hence the zero-loss reduction of Theorem 6.1 **cannot** be implemented by first shrinking the source class to Gaussian mixtures with any fixed inverse-scale budget. The topological closure mechanism is valid; that proposed restricted approximating class is not dense in the topology it needs. This applies the completed partner result to an exact quantitative obstruction rather than merely citing it.

The fractional partner addendum is stronger: a uniform bound on `E sigma^{-r}` for any fixed `r>0` already prevents weak approximation of compactly supported cap-one laws. Thus replacing the first inverse-scale moment by a smaller positive power does not repair the approximation route.

## 9. Absolute continuity ledger

The central density-height problem should be distinguished from basic existence. If `A!=0` and the joint input law is absolutely continuous, then `X^TAX` is absolutely continuous. One direct original-coordinate proof is:

- if some `A_ii!=0`, condition on all other coordinates; the remaining one-dimensional map is a nonconstant quadratic, and the pushforward of an absolutely continuous one-dimensional law under a nonconstant quadratic polynomial is absolutely continuous;
- if every diagonal entry vanishes, choose `A_ij!=0`; conditioning on all coordinates except `X_i` leaves an affine function `B X_i+C`, where `B=2 sum_{k!=i}A_ikX_k`. Since `B=2A_ijX_j+W` with `X_j` independent of `W` and absolutely continuous, `P(B=0)=0`, so almost every conditional affine map is nonconstant.

Therefore

\[
\boxed{A\ne0,\ X\text{ absolutely continuous product}\Longrightarrow X^TAX\ll dx.}
\tag{9.1}
\]

No density cap, rank-three condition, continuity, post-rotation independence, or Fourier decay is needed for this qualitative statement.

Under the owner target `rank(A)>=3`, the source-pinned partner theorem upgrades (9.1) instance-by-instance to a bounded `C_0` density, but with a matrix-dependent constant. The full conjecture is precisely the missing uniformity of that height over all dimensions and target matrices.

## 10. What this pays and what remains

The new closure theorem removes two kinds of false difficulty from the central quantitative problem:

1. **rough source edges are not an essential obstruction** to proving the universal height constant: one may work on positive analytic Schwartz cap-one sources and pass the bound back with zero loss;
2. **algebraically singular matrix configurations are not an essential obstruction** either: one may work on a dense generic rational matrix class and pass a truly uniform bound back with zero loss.

What it does **not** do is pay any estimate that deteriorates with small principal minors, leverage, dimension, or condition numbers. Those quantities can still degenerate along the approximating generic sequence, so reciprocal-minor arguments remain insufficient unless they are aggregated before inversion or routed into another product-preserving branch.

The first unpaid implication is therefore still the full uniform estimate on the regular core (6.3):

\[
\boxed{
\sup_{\text{generic analytic core}}
s_3(A)\max_t p_{X^TAX}(t)<\infty.
}
\tag{10.1}
\]

If this is proved with one constant, Theorem 6.1 closes all rough and degenerate targets with exactly the same constant. The current corrections remain in force: no law-uniform pointwise quadratic Fourier decay, no independence after spectral rotation, and no projection/X-ray-only shortcut for the minority two-sheet geometry.
