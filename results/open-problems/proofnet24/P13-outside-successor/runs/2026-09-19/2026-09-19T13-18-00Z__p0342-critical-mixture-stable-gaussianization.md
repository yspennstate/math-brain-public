Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `M_P0342 = 2/2 -> 2/2`. NEW MATHEMATICAL MOVEMENT: the finite local orientation statistic is asymptotically Gaussian and asymptotically independent of every bounded unoriented-scaffold observable; consequently the critical `alpha=1/2` perturbation has the explicit non-Gaussian limit `N(0,3/(2*pi^2)) + (1/2)Rademacher`, and the whole `Phi_alpha` family has a sharp three-regime limit theorem. Methods actually tried: B2, B7, B12.**

# P13 / P0342 — scaffold-stable Gaussianization and the exact critical two-Gaussian mixture

UTC run date: 2026-09-19.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`.  
Own root: `proofnet24/P13-outside-successor/`.

## 1. Continuity, ownership, exclusions, and recovered baseline

This invocation continues the current exclusive P13 successor `P0342`, governed by `operations/claims/P0342.md`. It does not reopen the retired I0051 clade-covariance target, the completed six-unchanged-run C0021 handoff, any posted/excluded source, or any peer-owned claim.

I reread the controlling owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the P0342 canonical claim, the newest P13 report, source-specific intake/attempt history hits, current P0342 audit searches, and the newest relevant neighboring I0054 report.

The mandatory I0054 screen was checked first. The newest recovered R11 report is

`runs/R11/2026-09-19T12-40-00Z_i0054-reed-solomon-oa-u047-c068-84c1.md`.

It moves R11's own author-side model-class metric `67 -> 68`, remains PARTIAL at source/campaign level, and explicitly continues exclusive I0054 work. P13 therefore did not touch I0054.

The latest P13 report before this invocation is

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T12-03-38Z__p0342-alpha-rate-barrier-scope-strengthening.md`.

It preserved the already-complete frozen source metric `M_P0342=2/2` and proved a one-sided phase barrier for the family `Theta_alpha=Psi+Phi_alpha`: non-tightness for `alpha<1/2`, failure of the fringe Gaussian at `alpha=1/2`, and deterministic negligibility of the perturbation for `alpha>1/2`. It did **not** identify the critical finite limit or prove that the finite local mark `Psi` itself has the matching Gaussian CLT. Those are the targets of this run.

Repository-wide source-specific searches still recover no P0342 end-to-end PASS from P26 and no end-to-end PASS from a distinct OTHER research track. P13's historical exact checker is a self-check only. Thus the campaign status remains

`CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`.

No claim file is created or modified in this run.

## 2. Source statement and current literature check — 2026-09-19

The source is David Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 12, Section 4.10. The current v3 HTML, revised 18 April 2025, states literally:

> If a CLT is known for the fringe-process sum of a given functional, must the same CLT hold for the corresponding `DTCS(n)` leaf sum?

The source's exact displayed statement is available at arXiv:2303.02529v3, Open Problem 12. This run used the accessible v3 HTML statement; it did not analyze the PDF, so no PDF screenshot claim is made.

Fresh dated searches on 2026-09-19 used combinations of

- `"Open Problem 12" "critical beta-splitting" fringe DTCS`,
- `critical beta-splitting fringe CLT finite tree 2026`,
- `beta-splitting fringe process finite DTCS CLT 2026`,
- the source arXiv id `2303.02529`,
- Brandenberger--Chin--Mossel arXiv `2505.24821`,
- Janson arXiv `2405.01239`, and
- the August/September 2026 beta-splitting papers.

The strongest directly useful later result is Anna Brandenberger, Byron Chin and Elchanan Mossel, *Asymptotics for the harmonic descent chain and applications to critical beta-splitting trees*, arXiv:2505.24821v2 (8 July 2025). Its introduction explicitly says it answers Open Problems 5 and 6 and partially Open Problem 8, not Open Problem 12. For the number `N_n(k)` of size-`k` clades it records the exact identity

`E[N_n(k)] = n a(n,k)/k`,

with `a(n,k)->a(k)=6 h_{k-1}/(pi^2(k-1))`; and Section 4 proves linear variance,

`Var[N_n(k)]/n -> sigma(k)^2`,

with an error estimate. These published facts will be used below only to obtain the law of large numbers for `N_n(3)`.

Svante Janson's revised arXiv:2405.01239v3 (2 February 2026), *Fringe trees of Patricia tries, compressed binary search trees, and three other random full binary trees*, gives quenched fringe-count convergence for the critical beta-splitting model. Its HTML presentation uses both vertex-fringe and leaf-Palm normalizations; because the displayed normalizations around equations (6.2), (6.4), and (6.8) require care, the proof below deliberately does **not** depend on converting those formulas. The Brandenberger--Chin--Mossel mean/variance statements give the needed size-three density directly.

The 18 August 2026 paper of Chorbadzhiyska--Minchev--Savov, arXiv:2608.18320, treats beta-splitting via fragmentation and resolves a different critical-beta height problem. Heng Ma's 13 September 2026 arXiv:2609.14325 studies extremal separation times and clade-count dynamics in fragmentation trees. I found no checked primary source in this bounded search explicitly resolving Aldous--Janson Open Problem 12 or stating the critical mixture theorem proved below. This is dated bounded negative evidence only, not a global openness, novelty, or priority certificate.

## 3. Frozen witness and family

The frozen P0342 witness is a single bounded continuous functional

`Theta = Psi + Phi`,

where `Psi` is the size-three orientation mark and `Phi` is the global finite-tree root-split perturbation. The historical witness is the `alpha=1/4` member of the family

\[
\Phi_\alpha(T)=
\begin{cases}
 n^{-\alpha}(B_n(T)-p_n),&T\text{ finite with }n\ge9\text{ leaves},\\
 0,&T\text{ infinite or }n<9,
\end{cases}
\qquad
\Theta_\alpha=\Psi+\Phi_\alpha.
\tag{3.1}
\]

Here `B_n` is the indicator that the smaller root-clade size is at most

\[
r_n=\lfloor\sqrt n\rfloor,
\tag{3.2}
\]

and `p_n=E B_n`.

The source metric is frozen to the original `Theta=Theta_{1/4}` and is already `2/2`: the positive-variance fringe CLT and the finite failure were both proved in the preceding P13 reports. Studying `Theta_alpha` is a strengthening only; it cannot increase the denominator-two source metric.

The preceding run established that every `Phi_alpha` vanishes on the infinite fringe tree, so every `Theta_alpha` has the same stationary fringe-process CLT as `Psi`:

\[
\frac1{\sqrt m}\sum_{i=0}^{m-1}\Theta_\alpha(\mathcal T_i)
\Rightarrow N(0,\lambda_3),
\qquad
\lambda_3:=\frac{3}{2\pi^2}.
\tag{3.3}
\]

This run determines the **finite** limit for every `alpha>0`.

## 4. Idea-before-proof receipt and the three methods

Before writing the proof I recorded the route in

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T13-05-20Z__p0342_b2_b7_b12_idea.md`.

Creation/read-back commit: `53713638fdf6893179f7c3f6e70e081c1c22e1c5`; verified blob `f9e02e7b8e7670ba9eb73635bf173ec0cabe9a76`.

The methods are genuinely different from the previous run's B5/B23/B27 triple.

**B2 — ATTACK THE NEGATION FIRST.** At the critical exponent `alpha=1/2`, test the possibility that the bounded root-split shift is nevertheless swallowed by the local orientation noise so that the same Gaussian survives. Instead of another moment obstruction, compute the exact joint characteristic-function limit. The negation fails: the limit is an explicit two-Gaussian mixture.

**B7 — TAKE THE LIMIT.** The local finite statistic has an exact conditional characteristic function depending only on the size-three clade count. Take that random characteristic function all the way to its deterministic Gaussian limit using a published `N_3(n)/n` law of large numbers.

**B12 — FIND WHAT IS CONSERVED.** Conditional on the entire unoriented clade scaffold, the left/right orientations of size-three `1|2` splits remain independent fair signs. This exact symmetry survives conditioning and forces asymptotic factorization against **every bounded scaffold observable**, not merely the chosen root-split event.

No code is needed: all new claims are analytic and are proved below. No finite enumeration claim is introduced.

## 5. Size-three clade density from published finite-tree estimates

Let `N_3(n)` be the number of size-three clades in `DTCS(n)`.

### Lemma 1 — exact limiting density

\[
\boxed{
\frac{N_3(n)}{n}\longrightarrow\lambda_3:=\frac3{2\pi^2}
\quad\text{in }L^2\text{ and hence in probability}.}
\tag{5.1}
\]

#### Proof

Brandenberger--Chin--Mossel record, for fixed `k`,

\[
E[N_n(k)]=\frac{n\,a(n,k)}{k},
\tag{5.2}
\]

where

\[
a(n,k)\longrightarrow a(k)
=\frac{6h_{k-1}}{\pi^2(k-1)}.
\tag{5.3}
\]

At `k=3`, `h_2=3/2`, so

\[
a(3)=\frac{6(3/2)}{2\pi^2}=\frac9{2\pi^2},
\qquad
\frac{E N_3(n)}n\longrightarrow\frac{a(3)}3
=\frac3{2\pi^2}=\lambda_3.
\tag{5.4}
\]

Their Lemma 4.2 proves that for every fixed `k`,

\[
\frac1n\operatorname{Var}(N_n(k))
=\sigma(k)^2+O(n^{-1/6}),
\tag{5.5}
\]

so in particular `Var(N_3(n))=O(n)`. Therefore

\[
E\left[\left(\frac{N_3(n)}n-\lambda_3\right)^2\right]
=
\frac{\operatorname{Var}(N_3(n))}{n^2}
+
\left(\frac{E N_3(n)}n-\lambda_3\right)^2
\longrightarrow0.
\tag{5.6}
\]

This is (5.1). `square`

The only external input in Lemma 1 is the published fixed-`k` mean/variance theory. In particular, no P13 ergodicity claim is used here.

## 6. Exact conditional orientation symmetry

Define

\[
Z_n:=\sum_{i=1}^n\Psi(\mathcal T_i^{(n)}),
\qquad
X_n:=\frac{Z_n}{\sqrt n}.
\tag{6.1}
\]

Let `G_n` be the sigma-field exposing the entire **unoriented** recursive split scaffold: all clades, all split sizes, and all randomness except the left/right ordering of each size-three `1|2` split. In particular, the root-split event `B_n` is `G_n`-measurable.

Distinct size-three clades are disjoint: clades in a rooted tree are nested or disjoint, and two distinct clades of equal size cannot be strictly nested. Each size-three clade has split sizes `1|2` or `2|1`; from

\[
q(3,1)=q(3,2)=\frac12,
\tag{6.2}
\]

and the independent recursive construction, its left/right orientation is a fair sign independent of the orientations of all other size-three clades after conditioning on `G_n`.

By the definition of `Psi`, each size-three clade contributes exactly one such sign to `Z_n`. Therefore, conditional on `G_n`,

\[
Z_n=\sum_{r=1}^{N_3(n)}\varepsilon_r,
\tag{6.3}
\]

where the `epsilon_r` are conditionally independent Rademacher variables. In particular, for every real `t`,

\[
\boxed{
E\left[e^{itX_n}\mid G_n\right]
=\cos\left(\frac{t}{\sqrt n}\right)^{N_3(n)}.}
\tag{6.4}
\]

This identity is exact at every `n`.

## 7. B7/B12 theorem — scaffold-stable Gaussianization

### Theorem 2 — conditional characteristic function becomes deterministic

For every fixed `t in R`,

\[
C_n(t):=
E\left[e^{itX_n}\mid G_n\right]
\longrightarrow
\exp\left(-\frac{\lambda_3t^2}{2}\right)
\quad\text{in }L^1.
\tag{7.1}
\]

Consequently, for every sequence of complex `G_n`-measurable random variables `U_n` with `|U_n|<=1`,

\[
\boxed{
E[U_n e^{itX_n}]
-
 e^{-\lambda_3t^2/2}E[U_n]
\longrightarrow0.}
\tag{7.2}
\]

In particular,

\[
X_n\Rightarrow G,
\qquad
G\sim N(0,\lambda_3),
\tag{7.3}
\]

and `X_n` is asymptotically independent, in the factorization sense (7.2), of every bounded observable of the unoriented scaffold.

#### Proof

For fixed `t`, for all sufficiently large `n`, `|t|/sqrt(n)` lies in a neighborhood of zero on which

\[
\log\cos x=-\frac{x^2}{2}+O(x^4).
\tag{7.4}
\]

Also `N_3(n)<=n/3` because the size-three clades are pairwise disjoint. Therefore from (6.4), for all sufficiently large `n`,

\[
\log C_n(t)
=-\frac{t^2}{2}\frac{N_3(n)}n+R_n(t),
\qquad
|R_n(t)|\le \frac{K_t}{n}
\tag{7.5}
\]

for a deterministic finite `K_t`: the `O(n^{-2})` error from one logarithm is multiplied by at most `n/3` clades.

By Lemma 1,

\[
\frac{N_3(n)}n\to\lambda_3
\quad\text{in probability},
\tag{7.6}
\]

hence (7.5) gives

\[
C_n(t)\to e^{-\lambda_3t^2/2}
\quad\text{in probability}.
\tag{7.7}
\]

Because `|C_n(t)|<=1`, bounded convergence in probability implies convergence in `L^1`, proving (7.1).

For any `G_n`-measurable `U_n` with `|U_n|<=1`, the tower property gives

\[
E[U_ne^{itX_n}]=E[U_nC_n(t)].
\tag{7.8}
\]

Therefore

\[
\left|
E[U_ne^{itX_n}]
-e^{-\lambda_3t^2/2}E[U_n]
\right|
\le
E\left|C_n(t)-e^{-\lambda_3t^2/2}\right|
\to0,
\tag{7.9}
\]

which is (7.2). Taking `U_n=1` gives convergence of characteristic functions to that of `N(0,lambda_3)`, proving (7.3) by Levy's theorem. `square`

### Interpretation

The Gaussian limit here is generated by the **orientation signs**, while the entire random clade scaffold survives as conditioning information. The random conditional variance `N_3(n)/n` self-averages to `lambda_3`, so the conditional characteristic function loses all scaffold dependence asymptotically. This is strictly stronger than an unconditional CLT for `X_n`.

This theorem is the B12 conservation/symmetry payoff: any bounded statistic measurable before the left/right orientation coins are tossed asymptotically factors from `X_n`.

## 8. Root-split threshold law, rederived source-faithfully

Let `S_n=min(G_n,R_n)` be the smaller size in the original root split, and let

\[
B_n=1_{\{S_n\le r_n\}},
\qquad r_n=\lfloor\sqrt n\rfloor.
\tag{8.1}
\]

For all sufficiently large `n`, `r_n<n/2`. Since the source split law is

\[
q(n,i)=\frac{n}{2H_{n-1}}\frac1{i(n-i)},
\qquad1\le i\le n-1,
\tag{8.2}
\]

symmetry gives

\[
p_n:=P(B_n=1)
=2\sum_{i=1}^{r_n}q(n,i).
\tag{8.3}
\]

Using

\[
\frac{n}{i(n-i)}=\frac1i+\frac1{n-i},
\tag{8.4}
\]

we get the exact formula

\[
\boxed{
p_n=
\frac{H_{r_n}+\sum_{i=1}^{r_n}(n-i)^{-1}}{H_{n-1}}.}
\tag{8.5}
\]

Now `H_{r_n}/H_{n-1}->1/2` because `log r_n/log n->1/2`, while

\[
0\le\sum_{i=1}^{r_n}\frac1{n-i}
\le\frac{r_n}{n-r_n}=O(n^{-1/2}),
\tag{8.6}
\]

so

\[
\boxed{p_n\to\frac12.}
\tag{8.7}
\]

Since `B_n` is Bernoulli(`p_n`),

\[
Y_n:=B_n-p_n
\Rightarrow \frac{S}{2},
\tag{8.8}
\]

where `S` is a symmetric Rademacher variable.

## 9. B2 theorem — the critical perturbation has an explicit non-Gaussian limit

### Theorem 3 — joint limit at `alpha=1/2`

Let `G~N(0,lambda_3)` and let `S` be an independent symmetric Rademacher variable. Then

\[
\boxed{
(X_n,B_n-p_n)\Rightarrow(G,S/2),
\quad G\perp S.}
\tag{9.1}
\]

Consequently, for the critical member `Theta_{1/2}`,

\[
\boxed{
W_n^{(1/2)}
:=\frac1{\sqrt n}\sum_{i=1}^n
\Theta_{1/2}(\mathcal T_i^{(n)})
\Rightarrow G+\frac S2.}
\tag{9.2}
\]

Its limiting characteristic function is

\[
\boxed{
\varphi_{1/2}(t)
=\exp\left(-\frac{\lambda_3t^2}{2}\right)
\cos\left(\frac t2\right).}
\tag{9.3}
\]

This law is a symmetric equal mixture of two Gaussians,

\[
\frac12N\left(-\frac12,\lambda_3\right)
+
\frac12N\left(\frac12,\lambda_3\right),
\tag{9.4}
\]

and is not Gaussian.

#### Proof

Because `B_n` is `G_n`-measurable, so is `Y_n=B_n-p_n`. For real `t,u`, use (6.4):

\[
E[e^{itX_n+iuY_n}]
=E\left[e^{iuY_n}C_n(t)\right].
\tag{9.5}
\]

By Theorem 2, `C_n(t)->c(t):=e^{-lambda_3t^2/2}` in `L^1`; since `|e^{iuY_n}|=1`,

\[
E[e^{itX_n+iuY_n}]
-c(t)E[e^{iuY_n}]
\longrightarrow0.
\tag{9.6}
\]

On the other hand,

\[
E[e^{iuY_n}]
=p_ne^{iu(1-p_n)}+(1-p_n)e^{-iup_n}
\longrightarrow
\frac12e^{iu/2}+\frac12e^{-iu/2}
=\cos(u/2).
\tag{9.7}
\]

Hence the joint characteristic function converges to

\[
e^{-\lambda_3t^2/2}\cos(u/2),
\tag{9.8}
\]

the product of the characteristic functions of `G` and `S/2`. Levy's continuity theorem proves the joint convergence and independence in (9.1).

For `alpha=1/2`, summing the global perturbation over all `n` leaf rerootings and dividing by `sqrt(n)` gives exactly

\[
\frac1{\sqrt n}\sum_{i=1}^n\Phi_{1/2}(\mathcal T_i^{(n)})
=B_n-p_n=Y_n.
\tag{9.9}
\]

Thus `W_n^(1/2)=X_n+Y_n`, and the continuous mapping theorem gives (9.2). Formula (9.3) follows by evaluating the characteristic function of the independent sum.

Finally,

\[
\varphi_{1/2}(\pi)=0,
\tag{9.10}
\]

whereas a Gaussian characteristic function `exp(i mu t-sigma^2 t^2/2)` is never zero. Therefore the limiting law is not Gaussian. `square`

This is stronger than the preceding report's second-moment contradiction: the critical finite sequence is tight and convergent, but converges to a specific non-Gaussian two-component mixture.

## 10. Exact three-regime phase diagram

### Theorem 4 — sharp `sqrt(n)` phase transition for the explicit family

For every `alpha>0`, let

\[
W_n^{(\alpha)}
:=\frac1{\sqrt n}\sum_{i=1}^n
\Theta_\alpha(\mathcal T_i^{(n)}).
\tag{10.1}
\]

Then, with `G~N(0,lambda_3)` and independent symmetric Rademacher `S`, exactly the following three regimes hold.

#### (i) Subcritical decay: `0<alpha<1/2`

\[
\boxed{|W_n^{(\alpha)}|\xrightarrow{p}\infty.}
\tag{10.2}
\]

#### (ii) Critical decay: `alpha=1/2`

\[
\boxed{W_n^{(1/2)}\Rightarrow G+S/2,}
\tag{10.3}
\]

an explicit non-Gaussian two-Gaussian mixture.

#### (iii) Supercritical decay: `alpha>1/2`

\[
\boxed{W_n^{(\alpha)}\Rightarrow G.}
\tag{10.4}
\]

Thus in this explicit family, `o(n^{-1/2})` pointwise global perturbations are harmless at the finite `sqrt(n)` scale, exact `Theta(n^{-1/2})` perturbations can change the limit to a non-Gaussian mixture, and slower decay destroys tightness.

#### Proof

For every `alpha`, summing the common global value over the `n` leaf rerootings gives the exact decomposition

\[
W_n^{(\alpha)}
=X_n+n^{1/2-\alpha}(B_n-p_n).
\tag{10.5}
\]

Theorem 2 gives

\[
X_n\Rightarrow G.
\tag{10.6}
\]

For `alpha>1/2`,

\[
\left|n^{1/2-\alpha}(B_n-p_n)\right|
\le n^{1/2-\alpha}\to0
\tag{10.7}
\]

deterministically, so (10.4) follows from Slutsky's theorem.

For `alpha=1/2`, Theorem 3 gives (10.3).

For `0<alpha<1/2`, by `p_n->1/2`, eventually both `p_n` and `1-p_n` are at least `1/3`; hence

\[
\left|n^{1/2-\alpha}(B_n-p_n)\right|
\ge\frac13n^{1/2-\alpha}
\quad\text{a.s.}
\tag{10.8}
\]

Also, conditional on `G_n`, `Z_n` is a Rademacher sum of length `N_3(n)<=n/3`, so

\[
E[X_n^2]=E\left[\frac{N_3(n)}n\right]\le\frac13.
\tag{10.9}
\]

For fixed `M`, the event `|W_n^(alpha)|<=M` therefore implies

\[
|X_n|\ge\frac13n^{1/2-\alpha}-M.
\tag{10.10}
\]

Chebyshev gives

\[
P(|W_n^{(\alpha)}|\le M)
\le
\frac{1/3}{(n^{1/2-\alpha}/3-M)^2}
\longrightarrow0,
\tag{10.11}
\]

which is (10.2). `square`

### Corollary 5 — exact transfer threshold for this mechanism

For the explicit family `Theta_alpha`, the fringe process always has the same Gaussian limit `N(0,lambda_3)`. The finite `DTCS(n)` sum has that same limit **if and only if `alpha>1/2`**. At equality the limit exists but is non-Gaussian; below equality the normalized sums are non-tight.

This is a theorem about this root-split perturbation family only. It does **not** claim that arbitrary functionals satisfying a pointwise `o(n^{-1/2})` condition automatically obey a general fringe-to-finite transfer theorem; locality, stabilization, cancellation, or aggregate coupling conditions may still be needed in a valid general repair.

## 11. What this changes mathematically, and what it does not

The frozen source metric does not move: it was already complete at `2/2`, and the owner forbids metric renaming or denominator inflation. The genuine new mathematical movement is instead:

1. a finite-tree CLT for the local orientation mark itself,
   \[
   X_n\Rightarrow N(0,3/(2\pi^2));
   \]
2. the stronger scaffold factorization (7.2), which makes the Gaussian orientation noise asymptotically independent of any bounded statistic determined before the size-three orientation coins;
3. an exact critical law at `alpha=1/2`, rather than merely a proof that the fringe Gaussian fails; and
4. a complete three-regime phase theorem showing that `1/sqrt(n)` is the exact transition scale for this explicit global mechanism.

This materially clarifies the source-level counterexample. The failure is not caused by a defective local statistic: `Psi` has the same Gaussian limit in the finite and fringe settings. The failure is caused by a global continuous perturbation which is invisible on every infinite fringe tree yet accumulates over `n` finite rerootings. At critical strength it survives as an independent Bernoulli shift; above critical strength it disappears; below critical strength it dominates.

This also sharpens the likely shape of any repaired theorem. A restriction merely saying that the functional's discrepancy from its infinite-fringe value goes to zero is far too weak. Even `O(n^{-1/2})` pointwise decay can alter the CLT. Any universal positive result must impose enough structure to rule out such coherent global accumulation, for example true locality/stabilization, a quantitative aggregate finite/infinite coupling, or cancellation/mixing assumptions.

The source itself says “for a given functional” in Open Problem 12, while surrounding prose discusses “suitable functionals.” P0342 therefore remains a candidate refutation of the **literal universal implication**. It does not claim to refute every stronger intended formulation restricted to local or stabilizing functionals.

## 12. Prior-art limitations and closure gate

The new finite `Psi` CLT uses published Brandenberger--Chin--Mossel input only at the level of `N_3(n)` mean/variance. Their paper proves scalar CLTs for fixed clade counts and fixed clade shapes, but the conditional-orientation factorization (7.2), the asymptotic independence from arbitrary bounded unoriented-scaffold observables, and the root-split critical mixture above are not statements I located there. I make no novelty claim: a bounded literature search cannot establish absence from the literature.

The original source v3 still lists Open Problem 12. The checked later beta-splitting papers found in the 2026-09-19 search resolve or advance other listed problems. No checked primary source found in this bounded search announces a resolution of the exact universal fringe-to-finite CLT implication.

Campaign closure is **not** claimed. The owner's closure rule still requires:

- an end-to-end source/prior-art gate with limitations preserved;
- one P26 end-to-end independent audit of the complete P0342 argument; and
- one end-to-end audit by a distinct OTHER track.

Fresh repository searches in this invocation recover neither required P0342 PASS. Historical P12/P13 clade audits concern retired I0051 and do not transfer to this successor. The existing P13 checker/output remains a self-check only.

No `paper_*` package is created before those gates are satisfied.

## 13. Delivery receipts

### Idea artifact

Path:

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T13-05-20Z__p0342_b2_b7_b12_idea.md`

Creation/read-back commit:

`53713638fdf6893179f7c3f6e70e081c1c22e1c5`

Verified blob:

`f9e02e7b8e7670ba9eb73635bf173ec0cabe9a76`

### This immutable run report

Path:

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T13-18-00Z__p0342-critical-mixture-stable-gaussianization.md`

The creation commit and read-back blob are recorded after the write in the user-facing completion; the report is not called delivered until that read-back succeeds.

No shared root ledger, historical report, peer file, canonical claim, schedule, email/Gmail, Drive resource, public posting, workflow, permission, credential, paid-compute setting, or external contact is modified.

## 14. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  target: P0342
  source: "Aldous--Janson arXiv:2303.02529v3 Open Problem 12"
  source_scope: "literal universal fringe-process CLT -> finite DTCS(n) CLT implication for a given functional"
  ownership: "exclusive P13 claim operations/claims/P0342.md"
  prior_target_I0051: "RETIRED; not reopened"
  mandatory_I0054_screen: "peer-owned by R11; newest recovered metric 67->68; not touched"
  frozen_metric:
    name: M_P0342
    domain: "single fixed positive-variance witness Theta=Psi+Phi_{1/4}"
    denominator: 2
    obligations:
      - FRINGE
      - FINITE-FAILURE
    before: "2/2"
    after: "2/2"
    movement: false
  mathematical_movement: true
  new_results:
    - "N_3(n)/n -> 3/(2*pi^2) in L2 from published fixed-k mean/variance estimates"
    - "conditional characteristic function of X_n becomes deterministic Gaussian"
    - "asymptotic factorization against every bounded unoriented-scaffold observable"
    - "(X_n,B_n-p_n) => independent (Gaussian,Rademacher/2)"
    - "alpha=1/2 finite limit is exact two-Gaussian mixture"
    - "alpha>1/2 finite limit matches fringe Gaussian"
    - "alpha<1/2 remains divergent in absolute value in probability"
    - "sharp three-regime phase boundary at alpha=1/2 for this explicit family"
  methods_actually_tried:
    - "B2 ATTACK THE NEGATION FIRST"
    - "B7 TAKE THE LIMIT"
    - "B12 FIND WHAT IS CONSERVED"
  previous_triple: [B5, B23, B27]
  theorem_proofs_on_page: true
  new_finite_checker_required: false
  self_check_promoted_to_audit: false
  current_literature_check_date: 2026-09-19
  current_literature_result: "bounded search found no checked primary-source resolution of exact Open Problem 12; not a global openness/novelty certificate"
  source_access_failure: "none for v3 HTML; no PDF analysis performed"
  audit_gate:
    p26_end_to_end: "NOT RECOVERED"
    distinct_other_end_to_end: "NOT RECOVERED"
  campaign_status: "CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING"
  closure_claimed: false
  paper_package_created: false
  claim_modified: false
  shared_root_modified: false
  next_decisive_action:
    - "independent P26 end-to-end audit of full P0342 source-matching counterexample"
    - "distinct OTHER-track end-to-end audit"
    - "final source-specific prior-art reconciliation before any closure/package"
```
