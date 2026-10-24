Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — common regeneration, unavoidable reverse mismatches, and a one-dimensional negative-debt criterion

**Status:** PROVED PARTIAL. This report proves new coupling/reduction lemmas in this repository. It does **not** prove the full Lyons–Pemantle–Peres monotonicity conjecture, and no external-novelty claim is made.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, probabilistic regeneration/coupling role under `operations/progress_first_2026-09-20/REGISTRY.md`.

**Captured master immediately before write:** `ceba9c0d1b57518afe08c674353a1ae43ee86f39`.

**Complementary peer checkpoint read before doing the main derivation:** P03-A, `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0004Z__two-point-near-regular-extension.md`, creation commit `b72d74a7bb76b5580301ead846bd47902fdc74e4`. P03-A proved a restricted analytic theorem for `{2,3}` offspring with sufficiently small mass at 3: strict monotonicity in the inward-bias parameter through `lambda=3/2`. I do not duplicate its Aïdékon-formula analysis below; the point here is to isolate what a regeneration coupling must pay probabilistically beyond that range.

## 1. Exact source convention and current primary results

The primary high-bias paper is Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases* (2011 preprint; published in CPAM 2014 under the title *Lyons-Pemantle-Peres Monotonicity Problem for High Biases*).

For a Galton–Watson tree without leaves, the offspring variable `Z` is positive integer-valued with

`P(Z=0)=0`.

Their **outward-bias** parameter is `beta>0`. At a non-root vertex with `k` children,

\[
P_\beta(\hbox{parent})=q_k(\beta):=\frac1{1+\beta k},\qquad
P_\beta(\hbox{a specified child})=\frac{\beta}{1+\beta k}.
\tag{1.1}
\]

Thus increasing `beta` means stronger bias away from the root. The walk is transient for

\[
\beta>1/EZ,
\]

and the Lyons–Pemantle–Peres conjecture asks whether the speed `v(beta)` is increasing throughout that transient interval. The arXiv v1 theorem states monotonicity for `beta>=717` (and `beta>=717/d` when the minimum offspring is `d`), whereas the final 2014 CPAM abstract states `beta>=1160`; neither old numerical threshold is used below as a current frontier.

The reciprocal convention used in much later work is

\[
\lambda=\beta^{-1},
\]

so at a `k`-child vertex

\[
P_\lambda(\hbox{parent})=\frac{\lambda}{\lambda+k},\qquad
P_\lambda(\hbox{a specified child})=\frac1{\lambda+k}.
\tag{1.2}
\]

Consequently a theorem saying speed is **decreasing** in `lambda` is consistent with the conjectured **increase** in outward `beta`; it is not a contradiction.

Strong later primary results checked on 20 September 2026:

* Aïdékon, arXiv:1111.4313 / PTRF 2014, gives an exact speed representation; the later monotonicity literature credits this with improving the no-leaf low-`lambda` monotonicity interval to `lambda<=1/2`, i.e. outward `beta>=2`.
* He–Wang–Xiang, arXiv:1610.08151, published online 5 March 2025 in *Journal of Applied Probability*, proves for minimum offspring `m_1>=2` that the speed is strictly decreasing in the inward parameter for
  \[
  0\le\lambda\le \frac{m_1}{1+\sqrt{1-1/m_1}}.
  \tag{1.3}
  \]
  Equivalently, in outward bias this is monotonicity for
  \[
  \beta\ge \frac{1+\sqrt{1-1/d}}{d},\qquad d=m_1\ge2.
  \tag{1.4}
  \]
* Bowditch–Tokushige, arXiv:1906.07913, proves differentiability of the speed in the ballistic/CLT regime and represents the derivative through a two-dimensional Gaussian covariance. Their proof is built on the Lyons–Pemantle–Peres regeneration structure. Differentiability by itself does not determine the derivative's sign. In the no-leaf exponential-moment setting their regeneration moments are uniformly controlled on compact subintervals of the ballistic regime.

A bounded current search did not locate a full-source solution after the 2025 theorem. This search miss is **not** treated as proof of worldwide openness.

## 2. Previous repository result and fixed full-source metric

The older repository row `P0066` only recorded the local observation that for fixed offspring `D`, radial drift changes monotonically with bias, while explicitly noting that this does not control the changing environment/measure seen by the walk. No sign bound for that measure-change term or globally ordered speed coupling had been established there.

The progress-first metric remains:

`R_full = 1` = full monotonicity for every no-leaf supercritical offspring law on every source-admissible transient bias has **not** been proved here.

This run leaves `R_full` unchanged. The mathematical progress is a new intermediate obligation: all negative contribution in a common-regeneration coupling can be bounded by a scalar one-dimensional regeneration debt, and a naive pathwise ordering mechanism is ruled out sharply.

## 3. Common-uniform coupling for bounded-support offspring

Assume for this section that

\[
d\le Z\le D\quad\hbox{a.s.},\qquad 1\le d\le D<\infty,
\tag{3.1}
\]

and fix outward biases `beta` and `beta+eps`, with `eps>0` and

\[
\beta d>1.
\tag{3.2}
\]

Write `X^-` for the `beta` walk and `X^+` for the `beta+eps` walk, and let

\[
H_n^-:=|X_n^-|,\qquad H_n^+:=|X_n^+|.
\]

Use one iid sequence `U_n~Unif[0,1]` to make the radial decision for both walks. If the current offspring counts are `j` for `X^-` and `i` for `X^+`, set

\[
X^-\hbox{ moves to its parent}\iff U_n\le q_j(\beta),
\]

\[
X^+\hbox{ moves to its parent}\iff U_n\le q_i(\beta+\varepsilon).
\tag{3.3}
\]

Whenever both walks are at the same vertex and both move outward, choose the same child. Away from one another choose child labels in any marginally uniform way. Each marginal is exactly the required biased random walk.

Define a one-dimensional auxiliary walk by

\[
\Delta Y_n=
\begin{cases}
-1,&U_n\le q_d(\beta),\\
+1,&U_n>q_d(\beta).
\end{cases}
\tag{3.4}
\]

Because every current degree is at least `d`,

\[
q_j(\beta)\le q_d(\beta),\qquad q_i(\beta+\varepsilon)\le q_d(\beta),
\]

so pathwise

\[
\Delta H_n^-\ge \Delta Y_n,\qquad \Delta H_n^+\ge\Delta Y_n.
\tag{3.5}
\]

Therefore both processes

\[
H_n^- -Y_n,\qquad H_n^+-Y_n
\]

are nondecreasing.

### Lemma 3.1 — common-regeneration domination

Let `tau` be a regeneration time of `Y`: `Y_tau` is a strict record relative to the past and the future never falls below the regeneration level in the standard one-dimensional regeneration sense. Then `tau` is simultaneously a radial regeneration time for both `X^-` and `X^+`.

**Proof.** For `s<tau`,

\[
H_\tau^\pm-H_s^\pm=(Y_\tau-Y_s)+[(H_\tau^\pm-Y_\tau)-(H_s^\pm-Y_s)]>0,
\]

because the first term is positive and the bracket is nonnegative. For `s>tau`, the regeneration property gives `Y_s>=Y_tau` and monotonicity of `H^\pm-Y` gives

\[
H_s^\pm-H_\tau^\pm\ge0.
\]

Thus neither tree walk can cross back through the parent edge below its regeneration level. The usual on-the-fly Galton–Watson exploration then gives the standard iid regeneration-block argument. `beta d>1` is exactly what makes `Y` transient to `+infinity`. QED.

This is the minimum-degree analogue of the common super-regeneration device in Ben Arous–Fribergh–Sidoravicius, but it is phrased to expose a later scalar debt bound.

Let `tilde P` denote the one-dimensional super-regeneration conditioning at time 0, let `tau` be the first nonzero common regeneration time, and let

\[
B:=\#\{n<\tau:\Delta Y_n=-1\}
\tag{3.6}
\]

be the number of one-dimensional backsteps in the block. The elementary path counting used in the source gives

\[
\tau\le 3B+1.
\tag{3.7}
\]

The law of `(B,tau)` depends only on the effective one-dimensional bias `beta d`, not on the rest of the offspring distribution.

## 4. Exact gap identity and a sharp obstruction to pathwise monotonicity

Set

\[
G_n:=H_n^+-H_n^-.
\]

At a time when the higher-bias walk is at a vertex with `i` children and the lower-bias walk is at a vertex with `j` children, (3.3) gives the exact one-step identity

\[
E[\Delta G_n\mid i,j,\mathcal F_n]
=2\{q_j(\beta)-q_i(\beta+\varepsilon)\}.
\tag{4.1}
\]

In particular, while they are at the same vertex of degree `k`,

\[
E[\Delta G_n\mid k,\ X_n^+=X_n^-]
=2\delta_k,
\qquad
\delta_k:=q_k(\beta)-q_k(\beta+\varepsilon)>0.
\tag{4.2}
\]

The difficulty starts only after spatial separation, when `i` and `j` need not agree.

### Lemma 4.1 — unavoidable reverse mismatch

For **any** coupling of the radial Bernoulli decisions at current degrees `(i,j)`, the probability that the higher-bias walk moves inward while the lower-bias walk moves outward is at least

\[
\bigl[q_i(\beta+\varepsilon)-q_j(\beta)\bigr]_+.
\tag{4.3}
\]

Hence a pathwise radial domination valid simultaneously for every reachable pair `i,j in [d,D]` is possible only if

\[
q_d(\beta+\varepsilon)\le q_D(\beta),
\]

i.e.

\[
(\beta+\varepsilon)d\ge \beta D.
\tag{4.4}
\]

For a nondegenerate support `d<D`, condition (4.4) fails for every sufficiently small `eps>0`. Therefore an infinitesimal-bias proof cannot be based on a universal assertion that the more outward-biased walk always stays radially ahead.

**Proof.** If `I_+` and `I_-` are Bernoulli indicators of inward moves with means `q_i(beta+eps)` and `q_j(beta)`, then for every coupling

\[
P(I_+=1,I_-=0)\ge [E I_+-E I_-]_+,
\]

which is (4.3). Taking the worst pair `i=d,j=D` yields (4.4). QED.

For the concrete `{1,2}` family, if `0<eps<beta`, the state pair `(i,j)=(1,2)` has unavoidable reverse-mismatch mass

\[
r_{12}(\beta,\varepsilon)
=\frac1{1+\beta+\varepsilon}-\frac1{1+2\beta}
=\frac{\beta-\varepsilon}{(1+\beta+\varepsilon)(1+2\beta)}>0.
\tag{4.5}
\]

Under the common-uniform coupling this obstruction is visible in an explicit finite motif: at a degree-1 vertex `x` whose parent has two children, a favorable first split sends `X^+` to the unique child and `X^-` to the parent; at the next `(1,2)` reverse mismatch the lower-bias walk can take the sibling branch; a second `(1,2)` reverse mismatch then puts the higher-bias walk two radial levels behind. Conditional on the required local degrees, this particular three-step inversion has positive probability

\[
\frac12\,\delta_1\,r_{12}(\beta,\varepsilon)^2.
\tag{4.6}
\]

This is not a counterexample to speed monotonicity. It is a rigorous counterexample to the **mechanism** “larger outward bias preserves pathwise radial order.”

## 5. Fresh separated states are not the source of negative drift

There is nevertheless a useful positive fact. Suppose the two walks are at distinct first-visit vertices and, just before revealing the two current offspring variables, those offspring variables remain independent copies of `Z` under the exploration filtration. Averaging (4.1) over those two fresh degrees gives

\[
E[\Delta G_n\mid \hbox{fresh separated pair}]
=2A_\varepsilon(\beta),
\tag{5.1}
\]

where

\[
A_\varepsilon(\beta)
:=E[q_Z(\beta)-q_Z(\beta+\varepsilon)]>0.
\tag{5.2}
\]

Thus a negative expected gap increment requires history/selection information that makes the current degree pair differ from two fresh iid samples. This identifies revisits / already explored geometry as the only place where a negative derivative contribution can survive after annealed averaging.

The remainder of the proof below deliberately throws away this extra positivity and charges **every separated time** as potentially bad. The resulting criterion is weaker but fully one-dimensional.

## 6. A one-dimensional negative-debt criterion

Define

\[
\delta_{\min}:=\min_{d\le k\le D}\delta_k,
\qquad
\delta_{\max}:=\max_{d\le k\le D}\delta_k,
\tag{6.1}
\]

and

\[
R_\varepsilon(\beta;d,D)
:=\max_{d\le i,j\le D}
[q_i(\beta+\varepsilon)-q_j(\beta)]_+
=[q_d(\beta+\varepsilon)-q_D(\beta)]_+.
\tag{6.2}
\]

Let `S` be the event that the two walks separate at least once before `tau`, and let `N_sep` be the number of decision times before `tau` at which they are at distinct vertices.

### Lemma 6.1 — first-separation hazard bounds

Under `tilde P`,

\[
\frac{\delta_{\min}}{q_d(\beta)}\,\widetilde P(B\ge1)
\le \widetilde P(S),
\tag{6.3}
\]

while, conditional on the entire one-dimensional sign path,

\[
\widetilde P(S\mid Y)\le
B\,\frac{\delta_{\max}}{q_d(\beta)}.
\tag{6.4}
\]

**Proof.** Before the first separation the walks are at the same vertex. Separation can occur only on a `Y`-backstep, because the separation interval `(q_k(beta+eps),q_k(beta)]` lies inside `[0,q_d(beta)]`. Conditional on a fixed `Y`-backstep and on the pre-step history, `U_n` is uniform on `[0,q_d(beta)]`; the current degree `k` is pre-`U_n` measurable. Therefore the separation hazard on that backstep is exactly `delta_k/q_d(beta)`, between the two bounds in (6.1). If `B>=1`, applying the lower bound to the first `Y`-backstep gives (6.3). A union bound over the `B` backsteps gives (6.4). Conditioning on the super-regeneration event does not alter the within-sign-interval uniformity because that event is measurable with respect to the one-dimensional sign path. QED.

### Lemma 6.2 — separated occupation is `O(eps)`

\[
\widetilde E[N_{\rm sep}]
\le
\frac{\delta_{\max}}{q_d(\beta)}
\widetilde E[B(3B+1)].
\tag{6.5}
\]

**Proof.** If no separation occurs then `N_sep=0`; always `N_sep<=tau 1_S`. By (3.7),

\[
N_{\rm sep}\le (3B+1)1_S.
\]

Condition on the `Y` sign path, use (6.4), and average:

\[
\widetilde E[N_{\rm sep}]
\le \widetilde E[(3B+1)\widetilde P(S\mid Y)]
\le \frac{\delta_{\max}}{q_d(\beta)}
\widetilde E[B(3B+1)].
\]

QED.

Since `delta_max=O(eps)`, this proves that the entire potentially adverse separated occupation in one common regeneration block is itself only first order in the bias increment.

### Theorem 6.3 — regeneration-debt lower bound

For the common-uniform coupling,

\[
\boxed{
\widetilde E[G_\tau]
\ge
2\frac{\delta_{\min}}{q_d(\beta)}\widetilde P(B\ge1)
-
2R_\varepsilon(\beta;d,D)
\frac{\delta_{\max}}{q_d(\beta)}
\widetilde E[B(3B+1)].
}
\tag{6.6}
\]

Consequently, the explicit scalar inequality

\[
\boxed{
\delta_{\min}\,\widetilde P(B\ge1)
>
R_\varepsilon(\beta;d,D)\,
\delta_{\max}\,\widetilde E[B(3B+1)]
}
\tag{6.7}
\]

is sufficient for

\[
v(\beta+\varepsilon)>v(\beta).
\]

**Proof.** Before first separation, a separating step gives gap `+2`; hence the contribution of first separation is exactly `2 P(S)`. All additional coupled contributions are nonnegative by (4.2). At a separated state, (4.1) and (6.2) bound the conditional expected gap increment below by `-2R_eps`. Therefore

\[
\widetilde E[G_\tau]
\ge 2\widetilde P(S)-2R_\varepsilon\widetilde E[N_{\rm sep}].
\]

Insert (6.3) and (6.5) to obtain (6.6). If (6.7) holds, the common-regeneration numerator is positive. Both walks use the same regeneration-clock law, so the standard regeneration ratio comparison yields the strict speed inequality. QED.

**Interpretation.** The multidimensional random-tree difficulty has been compressed into two pieces:

1. an explicit local degree penalty `R_eps`, and
2. the one-dimensional regeneration statistic `P(B>=1) / E[B(3B+1)]` for the auxiliary biased walk.

No recursive escape-probability identity is used, so this is complementary to P03-A rather than a duplicate.

## 7. Infinitesimal form and the `{2,3}` bridge to P03-A

Because

\[
\frac{\delta_k}{\varepsilon}
\longrightarrow
\frac{k}{(1+\beta k)^2}
\qquad(\varepsilon\downarrow0),
\tag{7.1}
\]

Theorem 6.3 yields an explicit right-derivative sufficient condition whenever the regeneration moment is finite.

The most relevant complementary family after the current P03-A checkpoint is

\[
P(Z=2)=1-p,\qquad P(Z=3)=p.
\tag{7.2}
\]

P03-A has already established a new restricted result up to inward `lambda=3/2`, i.e. outward

\[
\beta\ge2/3,
\]

for an explicit small-`p` regime. The coupling above works as soon as

\[
2\beta>1,
\]

so its natural unresolved testing strip is

\[
1/2<\beta<2/3
\qquad\left(3/2<\lambda<2\right).
\tag{7.3}
\]

For `d=2,D=3` and sufficiently small `eps` (in particular `2eps<beta`),

\[
\delta_{\max}=\delta_2,\qquad
\delta_{\min}=\delta_3,
\]

\[
\frac{\delta_2}{q_2(\beta)}
=\frac{2\varepsilon}{1+2\beta+2\varepsilon},
\tag{7.4}
\]

\[
\frac{\delta_3}{q_2(\beta)}
=\frac{3\varepsilon(1+2\beta)}{(1+3\beta)(1+3\beta+3\varepsilon)},
\tag{7.5}
\]

and

\[
R_\varepsilon
=\frac{\beta-2\varepsilon}
{(1+2\beta+2\varepsilon)(1+3\beta)}.
\tag{7.6}
\]

Let `B_beta` denote the backstep count for the auxiliary one-dimensional walk with forward/backward odds `2beta`; its law is independent of `p`. Dividing (6.7) by `eps` and taking `eps downarrow 0` gives the clean scalar sufficient condition

\[
\boxed{
\frac{\widetilde P(B_\beta\ge1)}
{\widetilde E[B_\beta(3B_\beta+1)]}
>
\frac{2\beta(1+3\beta)}{3(1+2\beta)^3}.
}
\tag{7.7}
\]

If (7.7) holds at a given `beta>1/2`, the common-regeneration bound has strictly positive first-order gap there. Under the known differentiability framework this supplies a source-valid route to positive outward derivative at that bias. Importantly, (7.7) is **independent of the mixing parameter `p`**: the entire `{2,3}` family has been reduced to the same one-dimensional inequality.

I have **not** proved (7.7) throughout `(1/2,2/3)`. That is the exact next bottleneck, not a hidden claim of an extension beyond P03-A.

For comparison, the analogous `{1,2}` criterion (valid for `beta>1`) has right-hand side

\[
\frac{\beta(1+2\beta)}{2(1+\beta)^3}.
\tag{7.8}
\]

This family is also useful for stress-testing mechanisms because the reverse mismatch (4.5) is especially transparent.

## 8. Why this is genuine progress but not closure

**New proved items in this run:**

1. A minimum-degree common-uniform regeneration domination valid for bounded offspring support whenever `beta d>1`.
2. The exact gap drift identity (4.1) used as a coupling ledger.
3. A sharp Fréchet obstruction (4.3)–(4.4) showing universal pathwise radial order is impossible for infinitesimal bias changes on every nondegenerate bounded support.
4. Fresh separated iid degree pairs have strictly positive annealed gap drift, so negative contributions must come from history/selection.
5. The separated occupation before common regeneration is `O(eps)` with the explicit bound (6.5).
6. The fully explicit regeneration-debt criterion (6.7), reducing speed monotonicity to one-dimensional regeneration moments plus local degree constants.
7. For `{2,3}`, the first-order criterion collapses to the scalar inequality (7.7), directly targeting the `beta in (1/2,2/3)` strip beyond the present P03-A restricted theorem.

**What remains:** the ratio

\[
\rho(\beta):=
\frac{\widetilde P(B_\beta\ge1)}
{\widetilde E[B_\beta(3B_\beta+1)]}
\tag{8.1}
\]

must be bounded sharply enough, preferably exactly, under the one-dimensional super-regeneration law. Coarse high-bias tail estimates merely reproduce already-known regimes and are not the goal. The next useful proof should derive a generating function or a renewal equation for `B_beta`, then compare it to the explicit threshold in (7.7). A finite simulation may guide that derivation but will not be counted as proof.

There is also deliberate slack in (6.6): every separated step is charged at the worst local penalty `R_eps`, even though Section 5 proves that a fresh iid separated pair has positive expected drift. If the one-dimensional scalar criterion fails near `beta=1/2`, the next pivot is to refine `N_sep` into fresh versus history-contaminated occupation and charge only the latter.

## 9. Obligation ledger and next attack

* `O1` recover source assumptions and outward/inward convention without inversion error: **DONE**.
* `O2` incorporate the strongest located 2025 minimum-degree monotonicity interval and 2019/2020 differentiability framework: **DONE for bounded current check; no worldwide-resolution claim**.
* `O3` avoid duplication with P03-A and reuse its `{2,3}` checkpoint: **DONE**.
* `O4` produce a rigorous obstruction to global pathwise monotone coupling: **DONE**, Lemma 4.1 and motif (4.6).
* `O5` control negative regeneration-block contributions by a new lemma: **DONE**, Theorem 6.3.
* `O6` convert the `{2,3}` continuation into a scalar one-dimensional inequality: **DONE**, (7.7).
* `O7` prove (7.7) on a new nonempty interval inside `(1/2,2/3)`, or prove that this coarse debt criterion cannot do so: **OPEN**.

**Next attack:** derive an exact or rigorously bounded probability generating function for the number `B_beta` of one-dimensional backsteps before the first nonzero super-regeneration under `tilde P`. The immediate target is a certified lower bound on `rho(beta)` in (8.1) for `beta in (1/2,2/3)`. If that fails, keep the same regeneration construction but split separated occupation into fresh-positive versus revisit/selection-contaminated states, rather than reverting to the old high-bias union bound.

## 10. Literature URLs checked 20 September 2026

* Ben Arous–Fribergh–Sidoravicius, arXiv:1111.5865: https://arxiv.org/abs/1111.5865
* Final CPAM paper / DOI: https://doi.org/10.1002/cpa.21505
* Aïdékon, arXiv:1111.4313: https://arxiv.org/abs/1111.4313
* Bowditch–Tokushige, arXiv:1906.07913: https://arxiv.org/abs/1906.07913
* He–Wang–Xiang, arXiv:1610.08151: https://arxiv.org/abs/1610.08151
* 2025 J. Applied Probability article: https://doi.org/10.1017/jpr.2024.113

No simulation, email, Drive write, public posting, canonical-claim overwrite, peer-report modification, or force-push was performed.
