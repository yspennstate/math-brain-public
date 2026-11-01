Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# P0220 — explicit extended-Bessel/Fredholm description of the stationary law

Status: **OPEN / PARTIAL under the campaign closure protocol**. This note gives a complete source-matching formula for all finite-dimensional stationary survival probabilities, but does not claim novelty, literature priority, or campaign closure. Independent P26 and distinct OTHER-track audits have not occurred.

## 1. Exact source target and inherited theorem

David Aldous's maintained problem page, *A one-dimensional drift-jump particle process* (posted February 2018), asks:

> Give some (fairly explicit) description of the stationary distribution.

Source URL: `https://www.stat.berkeley.edu/~aldous/Research/OP/left_Hamm.html`.

The historical Aldous--Diaconis notes *Patience Sorting, Longest Increasing Subsequences*, Section 4.1, equation (42), give

\[
(X_1,\ldots,X_k)\overset d=(\Gamma(B(1)),\ldots,\Gamma(B(k))),
\]

where `B(j)` are stabilized patience-sorting pile-top labels and `Gamma(m)` is the `m`th point of an independent rate-one Poisson process.

The previous R7-04 run proved, without changing the source assumptions, that if `Lambda(t)` is standard rate-one poissonized Plancherel growth and

\[
\tau_k:=\inf\{t\ge 0:\Lambda_1(t)\ge k\},
\]

then jointly for every finite `m`,

\[
(X_1,\ldots,X_m)\overset d=(\tau_1,\ldots,\tau_m). \tag{1}
\]

It also proved the exact Schur-process finite-dimensional weight: for
`0=t_0<t_1<\cdots<t_r` and nested diagrams
`\varnothing=\lambda^{(0)}\subset\lambda^{(1)}\subset\cdots\subset\lambda^{(r)}`,

\[
\begin{aligned}
&\Pr\{\Lambda(t_j)=\lambda^{(j)},\ 1\le j\le r\}\\
&\qquad=e^{-t_r}\frac{f^{\lambda^{(r)}}}{|\lambda^{(r)}|!}
\prod_{j=1}^r
\frac{f^{\lambda^{(j)}/\lambda^{(j-1)}}(t_j-t_{j-1})^{|\lambda^{(j)}|-|\lambda^{(j-1)}|}}
{(|\lambda^{(j)}|-|\lambda^{(j-1)}|)!}. \tag{2}
\end{aligned}
\]

This run specializes the standard Schur-process kernel exactly in the normalization of (1)--(2), and turns (1) into an explicit Fredholm determinant for the full stationary law.

---

## 2. B1 — change category: from stationary particles to a Schur-process gap field

For a partition `lambda`, use the standard Maya-particle encoding

\[
\mathcal S(\lambda)=\{\lambda_i-i+\tfrac12:i\ge1\}\subset\mathbb Z+\tfrac12.
\]

For `k>=1` define the right half-line

\[
H_k:=\{k-\tfrac12,k+\tfrac12,k+\tfrac32,\ldots\}.
\]

Because the largest Maya particle is `lambda_1-1/2`,

\[
\lambda_1<k
\quad\Longleftrightarrow\quad
\mathcal S(\lambda)\cap H_k=\varnothing. \tag{3}
\]

Combining (1) and (3), for every `t>=0`,

\[
\boxed{
\{X_k>t\}
=_{d}
\{\mathcal S(\Lambda(t))\cap H_k=\varnothing\}.
} \tag{4}
\]

Thus a joint survival event of the stationary coordinates is a multi-time gap event of a Schur-process determinantal point field.

### 2.1 Exact Schur specialization

Let `rho_a` be the Plancherel specialization of symmetric functions, characterized by

\[
H(\rho_a;u)=\sum_{n\ge0}h_n(\rho_a)u^n=e^{au},
\]

so that

\[
s_{\mu/\lambda}(\rho_a)
=
\frac{f^{\mu/\lambda}a^{|\mu|-|\lambda|}}
{(|\mu|-|\lambda|)!}.
\]

Then (2) is exactly

\[
e^{-t_r}s_{\lambda^{(1)}}(\rho_{t_1})
\prod_{j=2}^r s_{\lambda^{(j)}/\lambda^{(j-1)}}(\rho_{t_j-t_{j-1}})
\,s_{\lambda^{(r)}}(\rho_1). \tag{5}
\]

In Okounkov--Reshetikhin notation, every time increment contributes a `+` Wiener--Hopf factor

\[
\phi^+_{\Delta t}(z)=e^{\Delta t z},
\]

and the terminal specialization `rho_1` contributes the single `-` factor

\[
\phi^-(z)=e^{z^{-1}}.
\]

For a slice at physical time `t`, the product of all prior plus factors is `e^{tz}`, while the terminal minus factor remains after the slice. Therefore their kernel gauge function specializes to

\[
\boxed{\Phi(t,z)=\exp(z-t/z).} \tag{6}
\]

No asymptotic limit is being taken in (6); it is an exact specialization of the finite-dimensional Schur-process weight (5).

### 2.2 Explicit extended kernel

For `t,s>0` and `x,y in Z+1/2`, define

\[
\boxed{
K((t,x),(s,y))
=
\frac{1}{(2\pi i)^2}
\oint_{C_z}\oint_{C_w}
\frac{e^{z-t/z-w+s/w}}{z-w}
\,z^{-x-1/2}w^{y-1/2}\,dw\,dz .
} \tag{7}
\]

Here both contours are positively oriented circles around zero. Choose

- `|z|>|w|` when `t>=s`;
- `|z|<|w|` when `t<s`.

Since `x,y` are half-integers, the powers in (7) are ordinary integer powers. The two contour nestings encode the two Laurent expansions of `1/(z-w)` and are part of the definition.

#### Proof of (7)

Okounkov--Reshetikhin's Schur-process correlation theorem gives the generating series

\[
\sum_{x,y\in\mathbb Z+1/2}
 z^x w^{-y}K((t,x),(s,y))
=
\frac{\sqrt{zw}}{z-w}\frac{\Phi(t,z)}{\Phi(s,w)}, \tag{8}
\]

with the `|z|>|w|` expansion for `t>=s` and the `|z|<|w|` expansion for `t<s`.
Substitute (6):

\[
\frac{\sqrt{zw}}{z-w}
 e^{z-t/z-w+s/w}. \tag{9}
\]

Double coefficient extraction of `z^x w^{-y}` in (9) gives exactly (7). QED.

At equal time `t=s=u`, the scaling `z=sqrt(u) zeta`, `w=sqrt(u) omega` transforms the exponent into

\[
\sqrt u(\zeta-\zeta^{-1}-\omega+\omega^{-1}),
\]

which is the standard discrete-Bessel form. Thus (7) is the extended discrete-Bessel/Plancherel kernel in the present rate-one time normalization.

---

## 3. B7 — take the limit: an honest half-line Fredholm gap formula

A technical point is that every `H_k` is infinite. We avoid silently assuming an operator theorem by taking the gap determinant through finite truncations.

For `M>=k-1`, put

\[
H_{k,M}:=\{k-\tfrac12,k+\tfrac12,\ldots,M+\tfrac12\}.
\]

Take any finite list of constraints `(k_a,t_a)`, `a=1,...,m`, with `t_a>0`. If several constraints use the same time, replace them by the strongest one, i.e. the smallest `k`. Let

\[
A_M:=\bigsqcup_a \{t_a\}\times H_{k_a,M}.
\]

The Schur-process point field is determinantal with kernel (7), so the standard finite DPP gap identity gives

\[
\Pr\{\mathcal S(\Lambda(t_a))\cap H_{k_a,M}=\varnothing\ \forall a\}
=
\det(I-K|_{A_M}). \tag{10}
\]

As `M` increases, the events on the left decrease to

\[
\{\mathcal S(\Lambda(t_a))\cap H_{k_a}=\varnothing\ \forall a\}.
\]

Probability continuity from above therefore yields the limit

\[
\boxed{
\Pr\{\mathcal S(\Lambda(t_a))\cap H_{k_a}=\varnothing\ \forall a\}
=
\lim_{M\to\infty}\det(I-K|_{A_M}).
} \tag{11}
\]

We may take the right-hand side of (11) as the Fredholm gap determinant

\[
\det(I-K)_{\bigsqcup_a\{t_a\}\times H_{k_a}}.
\]

This definition is sufficient here and makes the infinite-half-line passage noncircular: existence of the limit follows from the underlying probability measure, not from an unproved trace-class assertion.

Constraints with `t_a=0` are vacuous because every stationary coordinate is strictly positive, and can simply be omitted before applying (11).

---

## 4. Full source-level stationary-law formula

### Theorem 4.1 — explicit finite-dimensional stationary survival law

Let `(X_1,X_2,...)` have the unique stationary law of Aldous's drift-jump process. For any positive integers `k_1,...,k_m` and thresholds `t_1,...,t_m>=0`, define

\[
A=\bigsqcup_{a:t_a>0}\{t_a\}\times H_{k_a},
\]

merging duplicate times by retaining the smallest `k`. Then

\[
\boxed{
\Pr(X_{k_a}>t_a\ \text{for all }a)
=
\det(I-K)_A,
} \tag{12}
\]

where `K` is the explicit double-contour kernel (7), and the determinant is the finite-truncation limit (11).

#### Proof

By the previously proved stationary representation (1),

\[
\Pr(X_{k_a}>t_a\ \forall a)
=
\Pr(\tau_{k_a}>t_a\ \forall a).
\]

By definition of `tau_k`,

\[
\tau_k>t\iff\Lambda_1(t)<k.
\]

By (3), this is exactly the gap event

\[
\mathcal S(\Lambda(t))\cap H_k=\varnothing.
\]

Apply the Schur-process correlation theorem in the exact specialization (5)--(7), then the finite-to-infinite gap limit (10)--(11). QED.

### Corollary 4.2 — the entire stationary distribution is determined explicitly

For each `m`, set `k_a=a` in (12). Then for arbitrary `t_1,...,t_m>=0`,

\[
\boxed{
\Pr(X_1>t_1,\ldots,X_m>t_m)
=
\det(I-K)_{\bigsqcup_{a=1}^m\{t_a\}\times H_a}.
} \tag{13}
\]

These joint survival functions determine the law of `(X_1,...,X_m)` for every `m`. The consistent family of all finite-dimensional laws determines the stationary law on the infinite coordinate sequence.

Thus (7) and (13) constitute a fairly explicit stationary-law description in standard integrable-probability language: a completely specified extended discrete-Bessel kernel and Fredholm half-line gap determinants.

### Corollary 4.3 — recovery of the previous one-coordinate result

For one constraint `(k,t)`, (12) reduces to the one-time discrete-Bessel gap probability

\[
\Pr(X_k>t)=\Pr(\Lambda_1(t)<k).
\]

By the previous run's Gessel/Toeplitz calculation this equals

\[
\boxed{
\Pr(X_k>t)=e^{-t}\det[I_{i-j}(2\sqrt t)]_{i,j=1}^{k-1}.
} \tag{14}
\]

Hence the extended kernel normalization is consistent with the already exact-checked scalar marginals.

For `k=1`, (13) gives `Pr(X_1>t)=Pr(Lambda(t)=empty)=e^{-t}`, recovering the source's exponential first coordinate.

---

## 5. B21 — who else has this shape? Prior-art reconciliation

The decisive machinery is not new and substantially predates the February 2018 problem page.

1. **Okounkov--Reshetikhin (2001/2003)**, *Correlation function of Schur process with application to local geometry of a random 3-dimensional Young diagram*, arXiv `math/0107056`, prove that Schur-process correlations are determinantal and give the explicit contour-kernel formalism. They also explain that a continuous-time formulation is available.

2. **Borodin--Olshanski (2004/2007)**, *Stochastic dynamics related to Plancherel measure on partitions*, arXiv `math-ph/0402064`, compute dynamical correlations for poissonized-Plancherel dynamics and identify discrete-Bessel structure.

3. **Mihai Nica (2014 arXiv; SPA 2017)**, *Decorated Young Tableaux and the Poissonized Robinson-Schensted Process*, arXiv `1404.4015`, explicitly identifies the continuous-time poissonized Robinson--Schensted Young-diagram trajectory as a Schur process and as a nonintersecting Poisson-walker ensemble.

4. The **Aldous--Diaconis 1993 notes** already contain the stationary patience-sorting representation (42).

Therefore neither the Schur determinantal theorem nor the extended discrete-Bessel kernel should be presented as novel. The source-specific content of this route is the explicit composition

`Aldous stationary drift-jump vector -> stabilized pile tops -> RSK P/Q symmetry -> Plancherel first-row hitting times -> Schur gap event -> specialized Fredholm determinant`.

A bounded literature search on 2026-09-19 did **not** find a paper explicitly identifying Aldous's 2018 stationary-law problem with formula (13). That search miss is not evidence of novelty, worldwide openness, or priority. Indeed, because all major ingredients predate the source page, the prior-art risk is high: the final classification could become KNOWN if an explicit source connection is located.

The maintained Aldous page was crawled within the current week and still displays the problem, so the present evidence remains `CURRENT-OPEN-LOOKING`, not a certified openness theorem.

---

## 6. What this does and does not establish

Mathematically, (13) supplies the requested object: every finite-dimensional stationary survival function is an explicit Fredholm determinant of the fully specified kernel (7). No missing probabilistic limit is left inside that formula.

Under the repository's stricter closure protocol, however, P0220 remains **PARTIAL** because:

- a source-specific prior-art search is bounded and has not certified novelty or the absence of this exact connection;
- no independent P26 full-proof audit has occurred;
- no distinct OTHER-track full-proof audit has occurred;
- a self-contained paper package has not yet passed those audits.

The frozen metric is already saturated from the preceding run:

`K_Bessel = infinity -> infinity` (**NO MOVEMENT**).

This is the first ordinary unchanged P0220 run after the metric moved, so the target-specific unchanged count becomes `1`.

The metric's saturation should not be mistaken for absence of mathematical progress: this run upgrades all one-coordinate determinant marginals to an explicit full-joint stationary-law determinant.

## 7. Next nonrepeating methods

If P0220 remains active after review, the next methods should be **B4 / B17 / B22**:

- **B4 (prove something weaker, completely):** extract an explicit closed two-coordinate formula or a rapidly convergent finite determinant/series from (13), useful for checking the normalization and making the source answer readable without Schur-process machinery.
- **B17 (look for the numbers somewhere else):** match low-dimensional joint coefficients/densities against published extended-Bessel/PNG/LIS formulas to locate exact prior art.
- **B22 (read the failures):** inspect the Aldous--Diaconis remarks and later citations around the leftmost-pile process for evidence why this Schur-process composition was not recorded as the answer.

No source-level PROVED/KNOWN label, publication claim, or novelty claim is made in this artifact.