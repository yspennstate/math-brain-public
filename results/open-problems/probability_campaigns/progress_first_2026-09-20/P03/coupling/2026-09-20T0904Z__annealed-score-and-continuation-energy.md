Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — exact annealed path score, posterior-continuation energy, and the earliest possible local reversal

**Status:** PROVED PARTIAL / NEW PROBABILISTIC REDUCTION / SOURCE-VALID OBSTRUCTION. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains unresolved. This run does not repeat a known high-bias range and does not claim a new full speed-monotonicity interval.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, regeneration/coupling and counterexample-search role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master immediately before write:** `7d99692a6de9713b8e745b288708570c51774f4c`.

**Previous own checkpoint:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0813Z__local-history-filter-and-dangerous-tail.md`, creation commit `a892fe1f5a9fe546e10d99b85abbf4652aecf126`.

**Complementary P03-A checkpoint consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0810Z__third-moment-contraction-correction-and-high-mean-theorem.md`. P03-A is pursuing recursive escape/speed identities. The present run stays on annealed path likelihoods, posterior degree information, and regeneration-compatible coupling quantities.

## 1. Minimal source continuity

Primary source: Gérard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865, https://arxiv.org/abs/1111.5865 . Their model is a Galton–Watson tree without leaves, i.e. `P(Z=0)=0`. At a non-root vertex with `k` children they use **outward child bias** `beta`:

\[
q_k(\beta):=P_\beta(\text{parent}\mid k)=\frac1{1+\beta k},
\qquad
P_\beta(\text{specified child}\mid k)=\frac\beta{1+\beta k}.
\tag{1.1}
\]

The source records transience for `beta>1/EZ` and the Lyons–Pemantle–Peres conjecture that `v(beta)` is increasing on the entire interval `(1/EZ,infinity)`. The old arXiv theorem says `beta>=717` (or `717/d` when the minimum offspring is `d`); the final 2014 CPAM abstract gives `1160`, so neither number is treated as the current frontier.

Bowditch–Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and give a Gaussian-covariance derivative representation; arXiv:2006.03433 proves analyticity in the ballistic regime. The strongest broad later primary monotonicity theorem retained in this campaign is He Song, Longmin Wang and Kainan Xiang, *J. Appl. Probab.* 62 (2025), 1044–1052, DOI `10.1017/jpr.2024.113`: in reciprocal parent bias `lambda=1/beta`, for minimum offspring `d>=2`, speed is strictly decreasing for

\[
0\le \lambda\le \frac{d}{1+\sqrt{1-1/d}}.
\tag{1.2}
\]

A bounded literature check on 20 September 2026 found no material primary-source change to the exact full conjecture. This search miss is not used as proof of worldwide openness.

The fixed full-source status is unchanged: **OPEN**.

For the quantitative bounded-support corollaries below I retain the source-valid restricted assumptions

\[
2\le d\le Z\le D<\infty,
\qquad \beta d>1,
\tag{1.3}
\]

and the post-root convention from the `0729Z` clarification, so no non-root formula is silently applied at the root.

## 2. Inherited local posterior identities and the missing bridge

The `0813Z` report proved that, at a non-root vertex with hidden offspring count `K`, after a canonical local departure history with

* `n` total departures,
* `o` child departures,
* `c` distinct child identities used,

one has the posterior

\[
\pi_{n,c}^{(\beta)}(k)
=
\frac{\pi(k)(k)_c(1+\beta k)^{-n}}
{\sum_j\pi(j)(j)_c(1+\beta j)^{-n}}.
\tag{2.1}
\]

Writing

\[
Q=q_K(\beta),\qquad M=EQ,\qquad V=\operatorname{Var}(Q),
\qquad \alpha_c=1+\beta c,
\tag{2.2}
\]

the next local departure falls into

* `R`: parent or one of the `c` already used children, with probability `alpha_c M`;
* `N`: a genuinely new child, with probability `1-alpha_c M`.

The posterior-mean jumps are exactly

\[
M^R-M=\frac VM,
\qquad
M^N-M=-\frac{\alpha_cV}{1-\alpha_cM}.
\tag{2.3}
\]

Thus `M` is a Bayes martingale in the local `R/N` observation filtration.

The same report isolated the continuation-weighted selection term

\[
\alpha_cV(H_R-H_N),
\tag{2.4}
\]

but did not control it in a way that survives many visits and many newly discovered vertices. This is the first target of the present run.

## 3. Exact annealed finite-path score after integrating out all offspring degrees

The local posterior calculus can be pushed one step further: it gives a closed score formula for an entire annealed finite path.

Consider a finite path segment that stays at non-root vertices. Canonically label children at each vertex by their order of first use. For each visited vertex `v`, let

\[
n_v=\#\{\text{departures from }v\},
\quad
o_v=\#\{\text{child departures from }v\},
\quad
p_v=n_v-o_v,
\tag{3.1}
\]

and let `c_v` be the number of distinct child identities used from `v`.

Define

\[
Z_{n,c}(\beta)
:=E\left[(K)_c(1+\beta K)^{-n}\right],
\qquad
M_{n,c}(\beta)=\frac{Z_{n+1,c}(\beta)}{Z_{n,c}(\beta)}.
\tag{3.2}
\]

### Theorem 3.1 — exact annealed path-likelihood factorization and score

For every fixed canonical non-root path pattern `gamma`,

\[
\boxed{
P_\beta(\gamma)
=C_\gamma
\prod_{v\in V(\gamma)}
\beta^{o_v}Z_{n_v,c_v}(\beta),
}
\tag{3.3}
\]

where `C_gamma` is independent of `beta`. Consequently

\[
\boxed{
\partial_\beta\log P_\beta(\gamma)
=\frac1\beta
\sum_{v\in V(\gamma)}
\bigl(n_vM_{n_v,c_v}(\beta)-p_v\bigr).
}
\tag{3.4}
\]

In particular, after annealing over all hidden offspring degrees, the entire path score depends on the random environment only through the **effective posterior parent thresholds** `M_{n_v,c_v}`.

#### Proof

Conditional on `K_v=k`, the local canonical record at `v` has likelihood

\[
(k)_{c_v}\beta^{o_v}q_k(\beta)^{n_v}
=(k)_{c_v}\beta^{o_v}(1+\beta k)^{-n_v},
\tag{3.5}
\]

up to a path-pattern factor independent of `k` and `beta`. Galton–Watson offspring counts are independent across vertices, so integrating `K_v` vertex by vertex gives (3.3).

Now

\[
\frac{Z'_{n,c}}{Z_{n,c}}
=-n\,E_{\pi_{n,c}^{(\beta)}}\frac{K}{1+\beta K}.
\tag{3.6}
\]

Since

\[
\frac{K}{1+\beta K}=\frac{1-q_K(\beta)}\beta,
\tag{3.7}
\]

we have

\[
\frac{Z'_{n,c}}{Z_{n,c}}
=-\frac n\beta(1-M_{n,c}).
\tag{3.8}
\]

The logarithmic derivative of the local factor is therefore

\[
\frac{o_v}\beta-\frac{n_v}\beta(1-M_{n_v,c_v})
=\frac1\beta(n_vM_{n_v,c_v}-p_v),
\]

and summing over vertices proves (3.4). QED.

### Corollary 3.2 — exact finite-horizon derivative representation

For any bounded path functional `F` with no explicit `beta` dependence and supported on such finite non-root path segments,

\[
\boxed{
\frac d{d\beta}E_\beta F
=
\frac1\beta E_\beta\left[
F\sum_v(n_vM_{n_v,c_v}-p_v)
\right].
}
\tag{3.9}
\]

For stopping-time functionals, (3.9) extends whenever the usual differentiation/dominating-integrability step is justified. I do **not** use (3.9) here to claim the infinite-regeneration limit without that step.

### Why this matters

Let

\[
\bar q(\beta):=E q_Z(\beta).
\tag{3.10}
\]

Then the score splits exactly as

\[
\sum_v(n_vM_v-p_v)
=
\sum_v(n_v\bar q-p_v)
+
\sum_v n_v(M_v-\bar q).
\tag{3.11}
\]

The second sum is the complete annealed **history/heterogeneity score debt** relative to a fresh-degree baseline. Thus the local Bayes filter from the previous run is not merely diagnostic: it is the exact hidden-environment state variable in the finite-path derivative.

## 4. Posterior-continuation energy identity

The continuation term (2.4) has a Hilbert-space structure that removes the need to bound `H_R-H_N` pointwise.

Fix one vertex and work at fixed `beta`. Let `F` be any square-integrable terminal reward. Let `F_j` be the local filtration generated by successive `R/N` observations at this vertex (together with whatever past information is fixed before the next category is revealed). Define

\[
G_j:=E[F\mid\mathcal F_j].
\tag{4.1}
\]

At a local state `(M,V,c)`, put

\[
a:=\alpha_cM,
\qquad
H_R:=E[F\mid\mathcal F_j,R],
\qquad
H_N:=E[F\mid\mathcal F_j,N].
\tag{4.2}
\]

### Lemma 4.1 — exact one-step covariance factorization

The posterior-mean increment `Delta M` and continuation-martingale increment `Delta G` satisfy

\[
\boxed{
E[\Delta M\,\Delta G\mid\mathcal F_j]
=\alpha_cV(H_R-H_N).
}
\tag{4.3}
\]

Moreover, with

\[
I_j:=E[(\Delta M)^2\mid\mathcal F_j]
=\frac{\alpha_cV^2}{M(1-\alpha_cM)},
\tag{4.4}
\]

and

\[
C_j:=E[(\Delta G)^2\mid\mathcal F_j]
=\alpha_cM(1-\alpha_cM)(H_R-H_N)^2,
\tag{4.5}
\]

we have the exact identity

\[
\boxed{
|\alpha_cV(H_R-H_N)|=\sqrt{I_jC_j}.
}
\tag{4.6}
\]

#### Proof

Equation (2.3) gives the two values of `Delta M`. The two values of `Delta G` are `H_R-G_j` and `H_N-G_j`. Since `P(R|F_j)=alpha_cM`, direct multiplication gives

\[
E[\Delta M\Delta G\mid\mathcal F_j]
=\alpha_cV[(H_R-G_j)-(H_N-G_j)],
\]

which is (4.3). Equations (4.4) and (4.5) are the conditional variances of the two two-point martingale increments, and their product is the square of the right-hand side of (4.3). QED.

### Theorem 4.2 — stopped continuation-energy bound at one vertex

For every almost surely finite local stopping time `N`,

\[
\boxed{
E\sum_{j<N}
|\alpha_{c_j}V_j(H_{R,j}-H_{N,j})|
\le
\sqrt{\operatorname{Var}(Q_0)\operatorname{Var}(F)}.
}
\tag{4.7}
\]

#### Proof

By Cauchy–Schwarz over time and probability and (4.6),

\[
E\sum_{j<N}\sqrt{I_jC_j}
\le
\left(E\sum_{j<N}I_j\right)^{1/2}
\left(E\sum_{j<N}C_j\right)^{1/2}.
\tag{4.8}
\]

The first factor is the predictable quadratic variation of the posterior-mean martingale and was computed in the previous run:

\[
E\sum_{j<N}I_j
=E[M_N^2]-M_0^2
\le \operatorname{Var}(Q_0).
\tag{4.9}
\]

The second factor is the quadratic variation of the Doob martingale `G_j`, hence

\[
E\sum_{j<N}C_j
=E[(G_N-G_0)^2]
\le \operatorname{Var}(F).
\tag{4.10}
\]

Combining (4.8)–(4.10) proves (4.7). QED.

This is the missing continuation-value control promised in the previous report: `H_R-H_N` need not have a sign and need not be bounded pointwise. Its entire contribution is controlled by the product of an **environment-information energy** and a **continuation-value energy**.

## 5. Globalization across all newly discovered post-split vertices

The preceding estimate can be interleaved across vertices.

Let `V_new` be the random set of newly discovered post-split non-root vertices whose local `R/N` histories are observed before a finite stopping time. In a Galton–Watson tree, the event that a child vertex is first reached is independent of that child's own offspring count, so each newly discovered vertex begins with the raw offspring prior. Put

\[
\sigma_q^2:=\operatorname{Var}(q_Z(\beta)).
\tag{5.1}
\]

Interleave all local `R/N` reveals in chronological order. At each reveal `i`, let `I_i,C_i` be the quantities in (4.4)–(4.5) for the currently active vertex.

### Theorem 5.1 — global posterior-selection energy bound

For every square-integrable terminal reward `F`,

\[
\boxed{
E\sum_i
|\alpha_iV_i(H_i^R-H_i^N)|
\le
\sigma_q\sqrt{E|V_{\rm new}|\,\operatorname{Var}(F)}.
}
\tag{5.2}
\]

#### Proof

For each discovered vertex separately, the expected total posterior quadratic variation is at most `sigma_q^2`. Summing the coordinate quadratic variations and then averaging over the random number of discovered vertices gives

\[
E\sum_i I_i\le \sigma_q^2 E|V_{\rm new}|.
\tag{5.3}
\]

The continuation martingale is one scalar Doob martingale for `F`; the `R/N` reveals are only a subset of its information increments, hence

\[
E\sum_i C_i\le \operatorname{Var}(F).
\tag{5.4}
\]

Apply Cauchy–Schwarz to `sum_i sqrt(I_iC_i)` exactly as in (4.8). QED.

This improves substantially on summing a worst-case continuation oscillation vertex by vertex: all post-split Bayesian selection is aggregated in **one square root**.

### Bounded-support corollary

The sharp support coefficient from the previous run is

\[
\rho_{d,D}(\beta)
=
\frac{\beta(\sqrt D-\sqrt d)^2}
{(1+\beta d)(1+\beta D)},
\tag{5.5}
\]

and gives

\[
\sigma_q^2\le \rho_{d,D}(\beta)\,\bar q(1-\bar q)
\le \frac14\rho_{d,D}(\beta).
\tag{5.6}
\]

Therefore

\[
\boxed{
E\sum_i|\alpha_iV_i(H_i^R-H_i^N)|
\le
\frac12\sqrt{
\rho_{d,D}(\beta)\,E|V_{\rm new}|\,\operatorname{Var}(F)}.
}
\tag{5.7}
\]

## 6. Explicit regeneration-block envelope

The earlier P03-B runs gave the exact auxiliary one-dimensional backstep law. Put

\[
q=\frac1{1+\beta d},\qquad p=1-q,
\qquad c=p-q=\frac{\beta d-1}{\beta d+1},
\qquad r=\frac qp=\frac1{\beta d},
\tag{6.1}
\]

and

\[
\mathcal L(r)=\sum_{m\ge1}\frac{r^m}{1-r^m},
\qquad
A=1+3p+c\mathcal L(r).
\tag{6.2}
\]

For the positive auxiliary super-regeneration block, the previous exact formulas are

\[
\widetilde E\tau=c^{-2},
\qquad
\widetilde EB=\frac q{c^2},
\qquad
\widetilde E[B(B-1)]=\frac{2q^2}{c^4}A,
\tag{6.3}
\]

and the corrected deterministic bound is `tau<=4B+1`. Therefore

\[
\boxed{
\widetilde E\tau^2
\le
T_2:=1+\frac{24q}{c^2}+\frac{32q^2}{c^4}A.
}
\tag{6.4}
\]

Indeed

\[
E(4B+1)^2
=16E[B(B-1)]+24EB+1.
\]

Now let `H` be the radial gain of one regeneration block and set

\[
F:=H-v\tau.
\tag{6.5}
\]

Since `0<=H<=tau` and `0<=v<=1`, `|F|<=tau`, so `Var(F)<=E tau^2`. Also a block can discover at most `tau+1` relevant non-root vertices. Hence the entire unweighted post-split Bayesian continuation-selection energy obeys

\[
\boxed{
\mathcal E_{\rm sel}
\le
\frac12\sqrt{
\rho_{d,D}(\beta)
(1+c^{-2})
T_2}.
}
\tag{6.6}
\]

Dividing by the exact block mean gives the normalized envelope

\[
\boxed{
\frac{\mathcal E_{\rm sel}}{\widetilde E\tau}
\le
\frac{c^2}{2}
\sqrt{
\rho_{d,D}(\beta)
(1+c^{-2})
T_2}.
}
\tag{6.7}
\]

This is **not yet a lower bound on `v'(beta)`**. The exact annealed score (3.4) weights the terminal posterior displacement at a vertex by its local departure count `n_v`. Passing from the unweighted predictable-covariation control (5.2) to that visit-count-weighted score without losing the gain is the remaining bridge. Equation (6.7) is therefore recorded as a rigorous component bound, not a monotonicity theorem.

## 7. A sharp local obstruction: wrong-sign posterior derivatives cannot occur before two departures, but can occur at exactly two

The `0813Z` report proved, for a fixed canonical local record `(n,c)`,

\[
\boxed{
M'_{n,c}(\beta)
=\frac1\beta\left((n+1)V-M(1-M)\right).
}
\tag{7.1}
\]

Thus a wrong-sign local threshold derivative requires

\[
(n+1)\frac{V}{M(1-M)}>1.
\tag{7.2}
\]

The support coefficient (5.5) is the sharp uniform upper envelope of `V/[M(1-M)]` for `d<=K<=D`.

### Proposition 7.1 — two departures are the earliest possible reversal time under `beta d>1`

For every finite `D>=d` and every `beta d>1`,

\[
\boxed{\rho_{d,D}(\beta)<\frac12.}
\tag{7.3}
\]

Consequently every source-valid bounded-support local history with `n=0` or `n=1` satisfies

\[
\boxed{M'_{n,c}(\beta)<0}
\tag{7.4}
\]

unless the offspring law is degenerate, in which case the inequality is still nonpositive and the history-selection variance vanishes.

#### Proof

Because `(sqrt(D)-sqrt(d))^2<D` and `1+beta D>beta D`,

\[
\rho_{d,D}(\beta)
<\frac{\beta D}{(1+\beta d)\beta D}
=\frac1{1+\beta d}
<\frac12.
\tag{7.5}
\]

For `n<=1`, `(n+1)rho<1`, so (7.1) has the favorable sign. QED.

The statement is sharp in `n`: a reversal can already occur at `n=2`.

### Exact source-valid `n=2` certificate

Take

\[
\beta=\frac{51}{100},
\qquad
P(K=2)=\frac{10201}{551001},
\qquad
P(K=100)=\frac{540800}{551001}.
\tag{7.6}
\]

This is a bounded-support Galton–Watson law without leaves, with

\[
E K=\frac{54100402}{551001}\approx98.1857,
\qquad
\frac1{EK}\approx0.0101848<\beta,
\qquad
\beta d=\frac{102}{100}>1.
\tag{7.7}
\]

Consider any positive-probability canonical local record with exactly two departures and one distinct child, for example: depart to one child, return to the vertex, then depart again through that same child. Excursion behavior away from the vertex is independent of its own offspring count, so the local degree likelihood is exactly the `(n,c)=(2,1)` likelihood in (2.1).

The two degree likelihood factors are

\[
L_2=\frac{2}{(1+2\beta)^2}=\frac{5000}{10201},
\qquad
L_{100}=\frac{100}{(1+100\beta)^2}=\frac{25}{676}.
\tag{7.8}
\]

The prior odds were chosen so that

\[
\frac{P(K=2)}{P(K=100)}\frac{L_2}{L_{100}}
=\frac14,
\tag{7.9}
\]

hence the posterior is exactly

\[
P(K=2\mid n=2,c=1)=\frac15,
\qquad
P(K=100\mid n=2,c=1)=\frac45.
\tag{7.10}
\]

The two threshold values are

\[
q_2=\frac{50}{101},
\qquad
q_{100}=\frac1{52}.
\tag{7.11}
\]

Therefore

\[
M=\frac{751}{6565},
\qquad
V=\frac{6245001}{172396900},
\tag{7.12}
\]

and

\[
3V-M(1-M)=\frac{1269747}{172396900}>0.
\tag{7.13}
\]

Using (7.1),

\[
\boxed{
M'_{2,1}\!\left(\frac{51}{100}\right)
=\frac{24897}{1723969}>0.
}
\tag{7.14}
\]

Thus **two previous departures are exactly the earliest time at which a history-conditioned parent threshold can move in the wrong direction** in the bounded-support `beta d>1` regime.

This is not a counterexample to speed monotonicity. It is a sharp obstruction to any proof that tries to make the conditioned local threshold monotone after only one or two observations.

## 8. What changed mathematically

The previous run knew that local degree posteriors form a reuse/discovery martingale and that sufficiently long histories can reverse the local threshold derivative. This run adds three nontrivial pieces:

1. **Exact annealed score:** after integrating out the Galton–Watson degrees, every finite non-root path has the exact score (3.4). The hidden environment enters only through `M_{n,c}`.
2. **Continuation-energy control:** the previously uncontrolled term `alpha V(H_R-H_N)` is exactly a covariance of two martingale increments and its total contribution is bounded by posterior information times continuation variance, first at one vertex and then simultaneously over every newly discovered post-split vertex.
3. **Sharp reversal latency:** under `beta d>1`, a wrong-sign local posterior derivative is impossible for `n<=1`, while the exact law (7.6) produces one at `n=2`. The earlier four-departure obstruction was therefore not minimal.

The full-source metric remains unchanged because none of these statements yet proves the sign of the complete visit-count-weighted regeneration score.

## 9. Remaining obstruction and next attack

Equation (3.4) identifies the precise unresolved bridge. For each vertex, the heterogeneity part of the annealed score is

\[
\frac{n_v}{\beta}(M_{n_v,c_v}-\bar q).
\tag{9.1}
\]

The energy theorem controls posterior increments with no `n_v` weight. The next attack should therefore **not** return to worst-degree mismatch estimates. It should perform a discrete summation-by-parts/Doob decomposition of

\[
n_v(M_{n_v,c_v}-\bar q)
\tag{9.2}
\]

into posterior increments weighted by the number of future returns to `v`. The single-vertex return probability is uniformly at most `r=1/(beta d)`, so the future-return multiplicity has a geometric envelope. Combining that predictable return weight with the information energy (4.9) is the natural route to a square-integrable weighted version of (4.7). If that weighted estimate still cannot beat the direct score term, the exact `n=2` certificate above provides a concrete finite-depth family on which to test whether the coupling architecture itself is too weak, at which point a clean pivot to the Bowditch–Tokushige covariance/spine representation is justified.

## 10. Obligation ledger / ledger_delta

- `R_full` (full source conjecture): **OPEN -> OPEN**.
- Exact source convention / inverse-bias hazard: **unchanged and controlled**.
- Post-split local Bayes filter: **previously proved -> now embedded in the exact annealed path score**.
- Continuation-value gap `H_R-H_N`: **uncontrolled pointwise -> controlled in aggregate by the energy inequalities (4.7) and (5.2)**.
- Multi-vertex post-split selection: **vertexwise/worst-case -> one global square-root information bound (5.2)**.
- Earliest wrong-sign local posterior derivative: **known example at `n=4` -> exact minimum `n=2`**.
- Full derivative sign: **still blocked by the visit-count weight `n_v` in (3.4)**.
- No peer or historical report overwritten. No shared RESULTS/QUEUE/POSTED ledger edited. No email, Drive, public posting, task creation, schedule modification, credential operation, or force-push performed.
