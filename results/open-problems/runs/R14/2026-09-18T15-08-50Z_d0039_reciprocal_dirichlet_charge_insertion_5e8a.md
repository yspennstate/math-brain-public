Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0039: `B_spectrum: 2 -> 2`; authoritative shared stagnation count remains UNKNOWN. The own immutable D0039 sequence now has three consecutive post-move flat runs, so the next D0039 invocation is SECTION-I STUCK-RECOVERY-1/2. Methods actually used: #4 PROVE SOMETHING WEAKER, COMPLETELY, #14 FIND THE GROUP ACTING, #19 MAKE IT AN ALGORITHM.**

# R14 HARD OUTSIDE — D0039 reciprocal-Dirichlet reduction, root charge insertion, and an explicit CMS-Moran target

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source problem OPEN.** This run preserves the terminal handoffs of the negative-margin spherical perceptron, H0017, and Bradley D0036. The active exclusive R14 hard-outside target remains `operations/claims/D0039.md`: Bálint Virág, *Operator limits of random matrices*, ICM 2014 / arXiv:1804.06953, Section 4, Question 1, asking whether the semi-infinite beta-Hermite spectral measure has the same multifractal spectrum as the Gaussian multiplicative cascade with the same Hausdorff dimension.

The frozen metric remains `B_spectrum=2`. I do **not** claim a beta-Hermite level-set theorem. The substantive result is a sharper reduction of the remaining level-3 obstruction: at beta 4 the independent endpoint-weight layer can be eliminated at polynomial-exponent scale, and moments of the remaining derivative-at-random-root field admit an exact charge-insertion identity into ordinary positive characteristic-polynomial moments of a GSE-type ensemble. This puts the missing theorem much closer to the current characteristic-polynomial GMC literature, but the quenched multiscale root-field theorem is still missing.

## 1. Continuity, source, exclusions, ownership, and current literature

Before new mathematics I reread/recovered the current campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the controlling owner directive, `operations/claims/D0039.md`, the newest own R14 D0039 report, the preceding level-2 and two-phase reports, the neighboring R15 D0039 source screen, and the D0039 correction in the intake ledger. I preserved all posted/retired exclusions and exclusive ownership.

Virág's source still asks the beta-**Hermite** question. The circular beta/GMC theorem is not a source closure. A fresh bounded primary-literature search on 2026-09-18 found no later theorem that states the requested beta-Hermite multifractal spectrum.

The most relevant current inputs found in this refresh are:

1. **Lambert--Paquette, arXiv:2508.01458 (2025)**: a bulk asymptotic description of the Gaussian-beta characteristic polynomial simultaneously resolving microscopic Sine-beta fluctuations and the global/mesoscopic log-correlated field. This remains the closest process-level bridge to the derivative field needed below.
2. **Pax Kivimae, arXiv:2012.09969 / EJP (2024)**: normalized positive powers of the GSE characteristic polynomial converge to GMC in a nontrivial subcritical range; Theorem 1.2 gives a multi-point moment relation linking GOE/GSE/GUE characteristic-polynomial powers. This is not a theorem about Virág's infinite spectral measure, but the charge-insertion identity in Section 6 below makes it directly relevant to the random-root derivative field.
3. **Junnila--Lambert--Webb, arXiv:2209.06548**: a general thick-point/GMC construction from exponential-moment asymptotics, including a CUE application using merging Fisher--Hartwig estimates. This supplies a plausible template once the corresponding root-conditioned GSE moment estimates are obtained.
4. **Fang, arXiv:2609.11543 (10 September 2026)**: fourth-order fusion asymptotics for Sine-beta correlations. Its proof uses characteristic-polynomial derivative bounds in the Hua--Pickrell/Sine-beta environment and records finite derivative moments. This is a new local ingredient since the earlier R14 literature screen, but it does not provide the required global quenched beta-Hermite root-field multifractal theorem.
5. **Nakano--Trinh--Trinh, arXiv:2601.13674 (2026)** studies a high-temperature regime `beta N -> 2c`, not the fixed-beta semi-infinite beta-Hermite model of D0039.

These are bounded negative/positive literature checks, not a novelty certificate. The reciprocal-simplex transformation, Gamma representation, charge insertion, Gaussian quadrature, CMS inequalities, and endpoint residue identities below are recorded as classical/elementary mechanisms or route reductions; I make no priority claim without a citation-graph audit.

## 2. Frozen metric and prior state

The admitted metric is

`B_spectrum in {0,1,2,3}`.

R14 has already proved the level-2 fixed-energy milestone at beta 4, `E=0`: the positive Christoffel kernel has a speed-`log N` LDP whose bulk rate is

\[
I_{\rm bulk}(x)=(x-\tfrac34)^2,\qquad x\ge0.
\tag{2.1}
\]

The newest preceding report then changed the level-3 route to the intrinsic Gaussian-quadrature mesh. If

\[
\xi_{1,n}<\cdots<\xi_{n,n},\qquad
q_{j,n}=K_{n-1}(\xi_{j,n},\xi_{j,n})^{-1},
\]

are the beta-Hermite Gaussian-quadrature nodes and weights, the deterministic CMS squeeze gives

\[
q_{j,n}
\le \mu_\beta((\xi_{j-1,n},\xi_{j+1,n}])
\le q_{j-1,n}+q_{j,n}+q_{j+1,n}.
\tag{2.2}
\]

For a finite Jacobi minor, with

\[
a_j:=|D_n'(\xi_j)|^{-2},
\]

and terminal endpoint weights `r_j`, the exact residue identity gave

\[
q_j=\frac{a_j/r_j}{\sum_k a_k/r_k}.
\tag{2.3}
\]

At beta 4, conditional on the eigenvalue cloud,

\[
(r_1,\ldots,r_n)\sim {\rm Dirichlet}(2,\ldots,2)
\]

and is independent of the eigenvalues.

The previous report left one broad stochastic blocker, `QUAD-GMC_4`: obtain a quenched multiscale exponent count and nested Frostman construction for the weights (2.3). This run splits that blocker cleanly into an exponent-neutral endpoint layer and a genuinely spatial derivative-root layer.

Therefore

`B_spectrum: 2 -> 2`.

## 3. Method #14 — FIND THE GROUP ACTING: an exact reciprocal-Dirichlet involution

The finite beta-4 weight field has an exact hidden `Z_2` symmetry on the simplex.

Fix positive numbers `a_1,...,a_n`, and for a point `r` in the open simplex define

\[
T_a(r)_j
:=\frac{a_j/r_j}{\sum_{k=1}^n a_k/r_k}.
\tag{3.1}
\]

Then (2.3) simply says `q=T_a(r)`.

### Proposition 3.1 — reciprocal involution and equivariance

For every `a>0`,

\[
\boxed{T_a(T_a(r))=r.}
\tag{3.2}
\]

Moreover the construction is permutation-equivariant: simultaneously permuting the coordinates of `a` and `r` permutes `T_a(r)` in the same way.

#### Proof

Put `q=T_a(r)` and `S=\sum_k a_k/r_k`. Then

\[
q_j=\frac{a_j}{r_jS},
\qquad
\frac{a_j}{q_j}=r_jS.
\]

Hence

\[
\sum_j\frac{a_j}{q_j}
=S\sum_jr_j=S,
\]

and applying (3.1) again gives `T_a(q)_j=r_j`. Equivariance is immediate from the symmetric formula. ∎

Thus the endpoint-to-quadrature map is not a generic nonlinear nuisance: it is an explicit involution.

### Proposition 3.2 — exact conditional density

Let

\[
r\sim {\rm Dirichlet}(\gamma,\ldots,\gamma),\qquad \gamma>0,
\]

and `q=T_a(r)`. Then `q`, conditional on `a`, has density on the open simplex

\[
\boxed{
 f_a(q)=
 \frac{\Gamma(n\gamma)}{\Gamma(\gamma)^n}
 \left(\prod_{j=1}^n a_j^{\gamma}\right)
 \left(\sum_{k=1}^n\frac{a_k}{q_k}\right)^{-n\gamma}
 \prod_{j=1}^n q_j^{-(\gamma+1)}.
}
\tag{3.3}
\]

The right side is invariant under common rescaling `a -> c a`, as it must be.

#### Proof

Use log-ratio coordinates

\[
y_i=\log(r_i/r_n),\qquad
z_i=\log(q_i/q_n),\qquad i<n.
\]

Equation (3.1) gives the affine reflection

\[
z_i=\log(a_i/a_n)-y_i.
\tag{3.4}
\]

The softmax Jacobian is

\[
\left|\frac{\partial(r_1,\ldots,r_{n-1})}
{\partial(y_1,\ldots,y_{n-1})}\right|
=\prod_{j=1}^n r_j,
\]

and the same formula holds for `q,z`. Since the Jacobian of (3.4) has absolute determinant one,

\[
\left|\frac{\partial r}{\partial q}\right|
=\frac{\prod_jr_j}{\prod_jq_j}.
\tag{3.5}
\]

Multiplying (3.5) by the Dirichlet density and substituting

\[
r_j=\frac{a_j/q_j}{\sum_k a_k/q_k}
\]

gives (3.3). ∎

At beta 4, `gamma=2`. Formula (3.3) gives an exact finite-dimensional law for the full quadrature-weight vector conditional on the beta-Hermite eigenvalues.

## 4. Method #4 — PROVE SOMETHING WEAKER, COMPLETELY: the beta-4 endpoint layer is exponent-neutral

The group calculation can be sharpened into a complete theorem eliminating the global endpoint normalization at the polynomial scale relevant to multifractals.

Normalize the derivative-only weights by

\[
\widetilde q_j:=\frac{a_j}{\sum_k a_k},
\qquad \sum_j\widetilde q_j=1.
\tag{4.1}
\]

For the actual Dirichlet endpoint vector define the intrinsic distortions

\[
H_j:=\frac{1}{n r_j},
\qquad
Z_n:=\sum_j\widetilde q_jH_j.
\tag{4.2}
\]

Then, identically,

\[
\boxed{q_j=\frac{\widetilde q_jH_j}{Z_n}.}
\tag{4.3}
\]

No auxiliary coupling is used in this identity.

### Theorem 4.1 — uniform polynomial neutrality of `Z_n`

At beta 4, conditional on **every** eigenvalue configuration (hence every deterministic vector `\widetilde q`), for every `epsilon>0`,

\[
\boxed{
\Pr\{Z_n>n^\epsilon\mid\xi\}\le 2n^{-\epsilon},
\qquad
\Pr\{Z_n<n^{-\epsilon}\mid\xi\}\le n^{-\epsilon}.
}
\tag{4.4}
\]

Consequently along the dyadic subsequence `n=2^k`, for the actual nested model,

\[
\boxed{\frac{\log Z_n}{\log n}\longrightarrow0\quad\text{a.s.}}
\tag{4.5}
\]

The conclusion uses only the marginal conditional Dirichlet law at each level; no independence across levels is assumed.

#### Proof

For `r_j~Beta(2,2n-2)` marginally,

\[
\mathbb E(r_j^{-1})=2n-1.
\]

Thus, conditional on `\xi`,

\[
\mathbb E Z_n
=\frac1n\sum_j\widetilde q_j\mathbb E(r_j^{-1})
=\frac{2n-1}{n}<2,
\]

and Markov gives the first inequality in (4.4).

For the lower tail, weighted Cauchy--Schwarz gives

\[
\left(\sum_j\frac{\widetilde q_j}{r_j}\right)
\left(\sum_j\widetilde q_jr_j\right)\ge1.
\]

Hence

\[
Z_n\ge\frac{1}{n\sum_j\widetilde q_jr_j}.
\tag{4.6}
\]

If `Z_n<n^{-\epsilon}`, then

\[
\sum_j\widetilde q_jr_j>n^{\epsilon-1}.
\]

But symmetry of the Dirichlet law gives

\[
\mathbb E\sum_j\widetilde q_jr_j=\frac1n.
\]

Another Markov bound gives the second inequality. Summing (4.4) over `n=2^k` and applying Borel--Cantelli for each rational `epsilon>0` proves (4.5). ∎

This is stronger than the preceding report's informal statement that the common Gamma normalization “should not matter”: at exponent scale it provably does not matter, uniformly over the entire derivative field.

### Theorem 4.2 — exact polynomial cost of a large endpoint multiplier

Use the standard Gamma representation at one fixed level,

\[
r_j=\frac{G_j}{\sum_kG_k},
\qquad G_j\stackrel{\rm iid}{\sim}{\rm Gamma}(2,1).
\tag{4.7}
\]

Then

\[
H_j=\frac{\sum_kG_k}{nG_j}.
\]

Since `(\sum_kG_k)/n=2+o(1)` with exponentially high probability and

\[
\Pr(G_j\le u)=1-e^{-u}(1+u)=\frac{u^2}{2}+O(u^3),
\tag{4.8}
\]

we obtain for fixed `h>0`

\[
\boxed{\Pr(H_j\ge n^h)=n^{-2h+o(1)}.}
\tag{4.9}
\]

Conversely `H_j\le n^{-h}` requires `G_j` of order at least `n^h` and therefore has super-polynomially small probability.

More generally, let `S_n` be any eigenvalue-measurable index set with

\[
|S_n|=n^{c+o(1)},
\]

so that `S_n` is independent of the endpoint Dirichlet vector conditional on the eigenvalues. Then for `0<h<c/2`,

\[
\#\{j\in S_n:H_j\ge n^h\}=n^{c-2h+o(1)}
\tag{4.10}
\]

with conditional probability tending to one at a stretched/polynomial rate strong enough for a geometric subsequence; for `h>c/2` there are no such sites with probability tending to one. This is just binomial concentration on the Gamma representation together with the exponentially concentrated common factor `\sum G/n`.

### Corollary 4.3 — spectrum-transfer rule for the endpoint layer

Suppose a derivative-only one-level exponent spectrum is known in the form

\[
\#\{j:\widetilde q_j=n^{-y+o(1)}\}=n^{c_{\rm der}(y)+o(1)}.
\tag{4.11}
\]

Then the beta-4 endpoint layer transforms the count exponent, wherever the right side is positive and the usual small windows are used, by

\[
\boxed{
c_q(x)=\sup_{h\ge0}\{c_{\rm der}(x+h)-2h\}.}
\tag{4.12}
\]

There is no competing polynomial-cost branch from `H_j<n^{-h}`.

In particular, if the missing derivative-only field has the target parabola

\[
c_{\rm der}(y)=\frac12-(y-\tfrac34)^2,
\tag{4.13}
\]

then

\[
\frac{d}{dh}\left[c_{\rm der}(x+h)-2h\right]
=-2(x+h+\tfrac14)<0
\]

for every `x>-1/4`. Therefore

\[
\boxed{c_q(x)=c_{\rm der}(x)\quad\text{for }x>-1/4.}
\tag{4.14}
\]

The desired level-3 window `alpha=2x in (1/2,1)` lies safely inside this range. Thus **the independent beta-4 endpoint Dirichlet/Gamma layer cannot alter the target exponent spectrum on the window R14 is trying to prove.** The remaining stochastic difficulty is the derivative-at-random-root field itself.

Equation (4.14) is conditional only on the derivative field having (4.13); the statement that the endpoint layer preserves any given exponent spectrum through the variational rule (4.12) is the proved reduction.

## 5. The actual residual field

After Theorem 4.1, it is natural to define the derivative-only normalized weights

\[
\boxed{
\widetilde q_{j,n}
:=
\frac{|D_n'(\xi_{j,n})|^{-2}}
{\sum_{\ell=1}^n|D_n'(\xi_{\ell,n})|^{-2}}.
}
\tag{5.1}
\]

For beta 4, proving level 3 on a nonzero-width interval is now reduced, up to the deterministic CMS-Moran conversion below, to establishing a quenched multiscale spectrum for (5.1). The previous Gamma/Dirichlet factor is no longer a plausible explanation for failure of the GMC parabola in the target window.

Call the narrowed stochastic target

`DERIV-GMC_4`.

A one-scale LDP for `D_n'(xi_j)` is not enough: root conditioning is a Palm-type operation, and the previous deterministic-energy Christoffel LDP does not automatically imply the root-count exponent. This distinction is important; the conditional count formula in the preceding report must not be silently promoted to a theorem.

## 6. A new exact route into current characteristic-polynomial GMC results: charge insertion at a root

There is an exact identity that converts moments of the derivative at an eigenvalue into ordinary **positive characteristic-polynomial moments** of one fewer particle.

Consider an `N`-particle beta-4 log gas with a common confining potential `V_N`, symmetric density

\[
\frac1{Z_N}
\prod_{1\le i<j\le N}|\lambda_i-\lambda_j|^4
\prod_{i=1}^Ne^{-V_N(\lambda_i)}.
\tag{6.1}
\]

Let

\[
D_N(z)=\prod_{i=1}^N(z-\lambda_i).
\]

Let `Z_{N-1}^{(N)}` denote the partition function of the `(N-1)`-particle beta-4 ensemble using the **same** potential `V_N`; this notation avoids silently changing the finite-N normalization to a standard rescaled `(N-1)` ensemble.

### Proposition 6.1 — marked-root / characteristic-polynomial identity

For every bounded/nonnegative test function `f` and every real `t` for which the displayed integrals are finite,

\[
\boxed{
\begin{aligned}
&\mathbb E_N\sum_{j=1}^N
 f(\lambda_j)|D_N'(\lambda_j)|^{-2t}\\
&\qquad=
N\frac{Z_{N-1}^{(N)}}{Z_N}
\int_{\mathbb R} f(x)e^{-V_N(x)}
\mathbb E_{N-1}^{(N)}
\left|D_{N-1}(x)\right|^{4-2t}\,dx.
\end{aligned}}
\tag{6.2}
\]

Here `E_{N-1}^{(N)}` is expectation in that same-potential `(N-1)` beta-4 ensemble.

#### Proof

By symmetry it is enough to mark `lambda_1=x` and multiply by `N`. Since

\[
D_N'(\lambda_1)=\prod_{k=2}^N(x-\lambda_k),
\]

the interaction factors involving the marked particle become

\[
\prod_{k=2}^N|x-\lambda_k|^{4}
\cdot
\prod_{k=2}^N|x-\lambda_k|^{-2t}
=
\prod_{k=2}^N|x-\lambda_k|^{4-2t}.
\]

The remaining-particle Vandermonde is unchanged at power four. Factoring its partition function gives exactly (6.2). ∎

At `t=0`, (6.2) is the usual one-point intensity identity. For `t<2`, the inserted characteristic-polynomial power `4-2t` is positive. This is the crucial connection to Kivimae's GSE characteristic-polynomial GMC/moment machinery and to Lambert--Paquette's microscopic/global factorization. Pair-collision integrability alone suggests the identity remains locally integrable somewhat beyond `t=2`, but I do not need or claim a sharp maximal `t` range here.

### Why this changes the route

The derivative field (5.1) had looked like a new object unrelated to the existing positive-characteristic-polynomial GMC literature. Equation (6.2) shows that its **Palm moments are exactly positive characteristic-polynomial insertion moments**. This is the correct bridge to test before trying to prove a new derivative theorem from scratch.

Kivimae proves GSE GMC for positive powers in a nonzero subcritical range and a broad GOE/GSE/GUE moment relation. Lambert--Paquette resolve the local Sine-beta factor and the macroscopic log-correlated field simultaneously. Fang's September 2026 Sine-beta fusion work supplies current local derivative/inverse-environment moment control. Together these results make the following program concrete:

1. use (6.2) and existing/extended GSE Fisher--Hartwig moment asymptotics for one marked root to obtain the one-level derivative-root exponent cost;
2. obtain two marked-root / merging-point analogues, which are the root-conditioned counterpart of the overlap law from the previous R14 report;
3. verify that the local Sine-beta derivative factor contributes only `n^{o(1)}` to the polynomial exponent, leaving the macroscopic log-correlated field as the source of the parabola;
4. feed those one- and two-scale estimates into the deterministic CMS-Moran algorithm below.

What is **not** currently on the page is the required uniform merging/root-conditioned moment theorem at the strength needed for a quenched Frostman construction. Therefore (6.2) is a certified route reduction, not level 3.

## 7. Method #19 — MAKE IT AN ALGORITHM: an explicit deterministic CMS-Moran criterion

The preceding reports referred generically to “nesting/Frostman control”. Here is an explicit deterministic algorithmic target, so the missing stochastic estimates are visible.

Choose a geometric sequence of polynomial degrees `n_k` and set the physical bulk scale

\[
r_k:=n_k^{-1/2}.
\]

At level `k`, form centered quadrature cells

\[
J_{j,k}:=(\xi_{j-1,n_k},\xi_{j+1,n_k}].
\tag{7.1}
\]

For a tolerance `epsilon_k downarrow0` and target `x`, call `J_{j,k}` **good** if:

1. `|J_{j,k}|=r_k^{1+o(1)}` quantitatively, e.g. `r_k^{1+epsilon_k} <= |J| <= r_k^{1-epsilon_k}`;
2. each of `q_{j-1,n_k},q_{j,n_k},q_{j+1,n_k}` lies in `n_k^{-x\pm epsilon_k}`;
3. a bounded enlargement of `J_{j,k}` has the same finite-neighbor weight exponent, so arbitrary balls centered in the retained cell are controlled by a bounded number of CMS cells.

By (2.2), every good cell obeys

\[
\mu_4(J_{j,k})=n_k^{-x+o(1)}=r_k^{2x+o(1)}.
\tag{7.2}
\]

Now retain a separated subfamily (for instance one residue class of indices modulo a fixed integer) and connect a fine good cell to the unique coarse retained cell whose fixed enlargement contains it. Delete children that meet coarse boundaries.

### Lemma 7.1 — deterministic CMS-Moran transfer

Suppose the resulting nested tree has the following properties for some `d>0`:

- cell diameters are `r_k^{1+o(1)}` and separated children are at distance comparable to their diameter;
- every retained parent has enough retained children that the cumulative branching number `M_1\cdots M_k` satisfies
  \[
  \frac{\log(M_1\cdots M_k)}{-\log r_k}\longrightarrow d;
  \tag{7.3}
  \]
- every retained cell and its bounded neighbors satisfy (7.2);
- the boundary deletions consume only `e^{o(|\log r_k|)}` of the available children.

Then the limit set `F_x` of infinite retained branches satisfies

\[
\boxed{\dim_HF_x\ge d,}
\tag{7.4}
\]

and every `E in F_x` has local spectral dimension

\[
\boxed{d_{\mu_4}(E)=2x.}
\tag{7.5}
\]

Conversely, if at every sufficiently large level all cells satisfying the same finite-neighbor mass criterion can be covered by at most `r_k^{-d+o(1)}` intervals of diameter `r_k^{1+o(1)}`, then the corresponding local-dimension level set has Hausdorff dimension at most `d`.

#### Proof

For the lower Hausdorff bound, put equal conditional mass on the retained children of each parent. The mass of a level-`k` cylinder is `(M_1\cdots M_k)^{-1+o(1)}=r_k^{d+o(1)}`. Separation implies a ball of radius comparable to `r_k` meets only a bounded/subexponential number of same-level retained cylinders. The mass-distribution principle then gives `dim_H F_x>=d`.

For (7.5), a point on an infinite branch lies in a retained cell at every scale. The cell is contained in a ball of comparable radius, while a slightly enlarged ball is covered by a bounded number of the cell and its controlled neighbors. Equation (7.2) therefore squeezes `mu_4(B(E,r_k))` between `r_k^{2x+o(1)}` factors. Geometric scale ratios and `epsilon_k->0` interpolate between successive levels, proving the full local-dimension limit. The upper Hausdorff bound is the standard Hausdorff-cover estimate from the assumed levelwise cover. ∎

This is deliberately deterministic. It specifies exactly what the stochastic root-field theorem must produce. No simulation or arbitrary mesh is needed.

If the derivative-root field has count exponent

\[
c_{\rm der}(x)=\frac12-(x-\tfrac34)^2
\tag{7.6}
\]

and enough two-scale child concentration to realize the tree, then because `r=n^{-1/2}` the branching dimension is

\[
d(x)=\frac{c_{\rm der}(x)}{1/2}
=1-2(x-\tfrac34)^2.
\tag{7.7}
\]

Putting `alpha=2x` gives

\[
\boxed{d(\alpha)=1-\frac12(\alpha-\tfrac32)^2,}
\tag{7.8}
\]

the beta-4 GMC parabola. Equations (7.6)--(7.8) remain conditional on `DERIV-GMC_4`; Lemma 7.1 itself is the proved deterministic transfer.

## 8. What happened to the three methods

- **#14 succeeded.** The endpoint-to-quadrature map is an exact reciprocal involution with an explicit pushed-forward Dirichlet density. This identifies a genuine `Z_2` action and removes opaque finite-dimensional dependence.
- **#4 succeeded on a complete restricted theorem.** The beta-4 endpoint normalization is uniformly polynomially neutral for every derivative field, and endpoint large multipliers have exact exponent cost `2h`. The endpoint layer has a rigorous spectrum-transfer rule and cannot change the target parabola on the desired `alpha in (1/2,1)` window if the derivative field has it.
- **#19 succeeded structurally.** The vague “need a Frostman argument” obligation is now an explicit quadrature-cell tree algorithm with a deterministic sufficient/necessary covering criterion. The only serious stochastic input left is root-field child counts/correlations.

The fixed metric nevertheless has **no movement** because the root-conditioned derivative field has not yet been proved to possess (7.6) on any nonzero-width exponent interval, let alone with the multiscale child estimates needed by Lemma 7.1.

## 9. Exact remaining obstruction after this run

The broad `QUAD-GMC_4` blocker from the preceding run can now be replaced by the narrower statement

\[
\boxed{
\texttt{DERIV-GMC\_4: prove a quenched multiscale parabola for }
\widetilde q_{j,n}\propto|D_n'(\xi_{j,n})|^{-2}
\texttt{ on one nonzero-width }x\texttt{-interval.}
}
\tag{9.1}
\]

The most promising concrete attack is not another EFGP cumulant expansion. It is the **marked-root charge insertion** (6.2) plus current GSE characteristic-polynomial moment/GMC machinery, upgraded to merging marked roots, followed by Lemma 7.1.

The nearest solved shape is now much closer than in the prior route: Kivimae proves a GSE positive-characteristic-polynomial GMC theorem, Junnila--Lambert--Webb show how exponential moment asymptotics generate thick-point chaos, Lambert--Paquette resolve the local/global Gaussian-beta characteristic-polynomial decomposition, and Fang supplies current Sine-beta fusion/derivative control. What these results still lack in exactly the required form is a **quenched, random-root, multi-scale merging estimate** for (5.1).

## 10. Stagnation trigger and next run

The own immutable D0039 metric history after the movement to level 2 is now:

1. `12-54-06Z`: `2 -> 2`;
2. `14-18-00Z`: `2 -> 2`;
3. this run: `2 -> 2`.

The root `RESULTS.md` authoritative numeric stagnation field for R14 remains stale/`UNKNOWN`, so I do not replace it by a guessed shared count. But the three consecutive own immutable no-movement reports satisfy the owner's Section-I trigger. Therefore the **next D0039 invocation must be a thinking-only stuck-recovery 1/2**, not another auxiliary lemma run.

The next report should use a new triple, provisionally **#6 DEFORM TO A POINT YOU CAN SOLVE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #22 READ THE FAILURES, NOT THE SUCCESSES**, and must contain the five required stuck items. The recovery choice should be: **port the nearest solved technique**—specifically, test whether the Kivimae/Junnila--Lambert--Webb characteristic-polynomial GMC moment machinery can be transported through the exact marked-root identity (6.2) to a genuine two-scale root-field estimate. If that fails, record the precise missing merging/Palm estimate rather than adding another fixed-energy lemma.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R14
  lane: HARD_OUTSIDE
  target: D0039
  source: "Balint Virag, Operator limits of random matrices, ICM 2014 / arXiv:1804.06953, Section 4, Question 1"
  status: PARTIAL
  metric:
    name: B_spectrum
    before: 2
    after: 2
    movement: false
  authoritative_shared_stagnation_count: UNKNOWN
  own_post_move_flat_sequence: 3
  section_I_next_run: STUCK_RECOVERY_1_OF_2
  methods_used: [4, 14, 19]
  proved_this_run:
    - "reciprocal simplex map T_a(r)_j proportional to a_j/r_j is an involution and permutation-equivariant"
    - "exact pushed-forward symmetric-Dirichlet density under the reciprocal involution"
    - "intrinsic beta-4 endpoint normalization Z_n is uniformly polynomially neutral; dyadic log Z_n/log n -> 0 a.s."
    - "endpoint multiplier H_j has polynomial upper-tail cost 2h and super-polynomial opposite tail"
    - "conditional exponent-spectrum transfer c_q(x)=sup_{h>=0}{c_der(x+h)-2h}; target parabola is unchanged for x>-1/4"
    - "exact marked-root charge-insertion identity converting moments of |D_N'(lambda_j)|^{-2t} to positive characteristic-polynomial moments of an (N-1)-particle same-potential beta-4 ensemble"
    - "deterministic CMS-Moran criterion reducing level-set Hausdorff dimensions to multiscale good-cell counts"
  conditional_not_counted:
    - "the derivative-only normalized root field has c_der(x)=1/2-(x-3/4)^2"
    - "marked-root one/two-scale asymptotics strong enough for a quenched Frostman tree"
    - "beta-4 local-dimension spectrum d(alpha)=1-(alpha-3/2)^2/2 on a nonzero-width interval"
  remaining_obligation:
    - "DERIV-GMC_4: quenched multiscale parabola for normalized |D_n'(xi_j)|^{-2} at beta 4 on one nonzero-width interval"
  literature_refresh_utc: "2026-09-18"
  relevant_newer_inputs:
    - "Kivimae, arXiv:2012.09969 / EJP 2024, GSE characteristic-polynomial GMC and moment relation"
    - "Lambert-Paquette, arXiv:2508.01458, Gaussian-beta bulk characteristic-polynomial asymptotics"
    - "Junnila-Lambert-Webb, arXiv:2209.06548, thick-point chaos from exponential moments"
    - "Fang, arXiv:2609.11543, 2026-09-10, Sine-beta fusion and derivative bounds"
  no_source_matching_full_solution_found_in_bounded_search: true
  next_methods: [6, 17, 22]
  shared_roots_edited: false
  peer_files_edited: false
  email: false
  drive: false
  public_posting: false
  scheduler_modified: false
```

## 12. Model / scheduler-control note

The exposed task-management surface still has prompt/title/schedule/timing/enabled controls but no binding model-family selector, reasoning-effort selector, guaranteed-runtime field, or authenticated completed-run model telemetry. Therefore GPT-6/maximum remains prompt-only in this environment and cannot truthfully be reported as applied. The repository policy likewise records that limitation. A task returning `You cannot modify this task` must be changed through its authorized owning/admin context or platform support; no permission bypass, duplicate schedule, scheduler mutation, email, Drive action, or public post was attempted in this run.