Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED by the runtime; GPT-6 maximum was requested, but the scheduler exposes no model/reasoning selector and I do not claim GPT-6 maximum. **NO MOVEMENT in the fixed metric.**
Problem/source: ordinary undirected Exp(1) first-passage variance on Z^2 — Kardar-Parisi-Zhang (1986); Auffinger-Damron-Hanson (2015), arXiv:1511.03262, Question 13.
Metric: before `b(n)=c_PP log n` for integers `n>=2`, one fixed non-explicit `c_PP>0`; after the same bound; status **OPEN / STUCK RECOVERY 1**; canonical unchanged-count = **3**.

# R07 HARD OUTSIDE — prescribed stuck/thinking report: the missing positive-noise persistence theorem

Run date: 2026-09-16.
Repository: `yspennstate/math-open-problems`, branch `master`.

This is the third consecutive canonical R07 run with no movement in the frozen metric. Per the owner's protocol, this run is a **thinking/stuck run**: I do not add another R07 lemma. I isolate the exact obstruction, catalogue the failed routes, identify the simplest still-unproved special case, compare with the nearest solved literature, and choose exactly one recovery route. The only new mathematical verification performed is an independent audit of neighboring R08-L003, as required by the R-series audit cycle.

## 1. Repository recovery and admission/status check

At run start I read the required control files:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- newest canonical own report `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md` (creation commit `e9420902b01dec21ffa7bc077777a58ac87ba5a5`);
- newest neighboring R08 report `runs/R08/20260916T1528Z_fpp_axis_transition_3b7c92.md`;
- the current intake/attempt inventory and targeted `probability_1000_intake_*` / attempt-ledger searches.

The large intake JSONL resources cannot all be materialized row-by-row in one GitHub connector response because oversized responses are truncated. I therefore record the intake/attempt reread as **PARTIAL / targeted due connector truncation**, not as fictitious complete ingestion of every row. The current R07 admission does not rely on a stale `admitted=true` field.

`POSTED.md`, `INDEX.md`, `RANKING.md`, current ownership searches and the newest fleet ledgers do not mark this exact ordinary Exp(1) point-to-point KPZ variance target as posted, settled, retired, or owned by another track. R08 owns the distinct strict-convexity/limit-shape question. P26 is the sole root-ledger writer, so R07 does not edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, or peer files.

No Gmail, Drive, email, public publication, purchase, permission, or schedule action occurred.

## 2. Current literature/status check — 2026-09-16

Dated bounded searches this run covered:

- `Pemantle Peres planar first-passage percolation times are not tight variance log n exponential`;
- `Auffinger Damron Hanson 50 years first passage percolation Question 13 Question 16`;
- `Ahlberg Deijfen Sfragara chaos concentration multiple valleys first passage percolation variance overlap`;
- `Dembin Elboim Peled coalescence first passage percolation extreme points overlap`;
- `Basu Sidoravicius Sly rotationally invariant first passage percolation variance 2026`;
- `Kardar Parisi Zhang Dynamic Scaling Growing Interfaces March 3 1986`;
- later/current FPP variance-lower-bound and overlap searches around these papers.

Scope retained:

1. **Kardar--Parisi--Zhang (1986).** `Dynamic Scaling of Growing Interfaces`, Phys. Rev. Lett. 56, 889, was published 3 March 1986. It is the universality prediction source, not a proof for ordinary undirected lattice FPP.
2. **Auffinger--Damron--Hanson (2015).** Question 13 asks for the planar fluctuation exponent `chi=1/3`; the survey's overlap question is a proposed route, not a solved theorem.
3. **Pemantle--Peres (2004).** For iid mean-one exponential passage times on Z^2, their theorem gives `Var T(0,n e1) >= C log n`. The theorem does not expose a numerical universal value of `C`; after shrinking the constant to absorb finitely many indices, R07 retains one fixed non-explicit `c_PP>0` on integers `n>=2`.
4. **Ahlberg--Deijfen--Sfragara (arXiv:2302.11367).** They rigorously relate fluctuations, noise/chaos and geodesic overlap, but the stability/chaos transition is located at a scale expressed through the unknown variance. Substituting `n^(2/3)` into that scale here would be circular.
5. **Dembin--Elboim--Peled (arXiv:2204.02332).** Quantitative coalescence/overlap is proved under the hypothesis that the limit shape has more than 32 extreme points. That is a conditional result for the present Exp(1) target because the needed shape geometry has not been proved here.
6. **Basu--Sidoravicius--Sly (arXiv:2604.01214, 1 April 2026).** Their polynomial variance improvement concerns a different rotationally invariant Riemannian FPP model, not ordinary nearest-neighbor lattice FPP.

I found no current unconditional ordinary-lattice point-to-point variance lower-bound order that improves the Pemantle--Peres logarithm. This is a bounded current search, not a proof of literature absence.

Thus the frozen metric remains

\[
\boxed{b(n)=c_{\rm PP}\log n,\qquad n\ge2,\qquad c_{\rm PP}>0\text{ fixed and non-explicit}.}
\]

## 3. Retained R07 state; no re-derivation this run

The newest report retains the following supported claims/routes:

- `R07-GH-C01`: Pemantle--Peres logarithmic variance lower bound — **KNOWN**, fixed metric;
- `R07-GH-C02`: Doob martingale variance identity — **KNOWN / proof on page**;
- `R07-GH-C03`: exact one-edge exponential cavity representation — **PROVED elementary**;
- `R07-GH-X01`: Boolean geodesic membership is not uniformly comparable from below to weighted passage sensitivity — **REFUTED ROUTE**;
- `R07-GH-C04`: product-refresh/ANOVA integrated-sensitivity identity — **KNOWN / proof on page**;
- `R07-GH-C05`: exact refresh-cavity covariance derivative — **PROVED**;
- `R07-GH-C06`: explicit cavity-kernel lower bound — **PROVED**;
- `R07-GH-C07`: depth-weighted survived-common-geodesic overlap reduction — **PROVED REDUCTION**;
- `R07-GH-X02`: unweighted common-geodesic count alone does not control weighted sensitivity pointwise — **REFUTED ROUTE**;
- `R07-GH-C08`: a fixed positive cavity-depth threshold captures linearly many geodesic edges in expectation at zero noise — **PROVED auxiliary theorem**;
- `R07-GH-C09`: the initial refresh-covariance decay rate is at least linear in `n` — **PROVED auxiliary theorem**.

The previous report already states the key qualitative conclusion: the supply of deep geodesic edges at `t=0` is no longer the obstruction; **their survival under positive off-geodesic perturbation is**.

## 4. (a) Exact blocking statement

Let `X^t` be the stationary independent-coordinate refresh coupling, where each coordinate survives with probability `e^{-t}`. Let

\[
C_n(t)=\operatorname{Cov}(T_n(X),T_n(X^t)).
\]

For each edge `e`, let `R_e,R_e^t` be the retained off-coordinate cavity thresholds, `gamma_n,gamma_n^t` the unique geodesics, and `B_e(t)` the event that coordinate `e` survives the refresh.

The simplest variance-free positive-noise statement that is still missing is: find fixed constants `delta,c>0` such that, for all sufficiently large `n`,

\[
\boxed{
E\#\Bigl\{e:\ B_e(n^{-1/3}),\ e\in\gamma_n\cap\gamma_n^{n^{-1/3}},\
\min(R_e,R_e^{n^{-1/3}})\ge\delta\Bigr\}\ \ge\ c n.
}
\tag{BLOCK}
\]

This is the exact statement I regard as the current blocker. It does **not** use the unknown variance to define its noise scale.

Why it is sufficient follows from the already-retained C05--C07 identities, not from a new lemma this run. C07 lower-bounds `-C_n'(t)` by a fixed positive constant times this depth-truncated survived overlap. The ANOVA representation retained in C04 makes `-C_n'(t)` nonincreasing in `t`. Thus (BLOCK) at `t=n^{-1/3}` would keep `-C_n'(s)` of order `n` throughout `0<=s<=n^{-1/3}` and integration would give an order-`n^(2/3)` variance lower bound.

The same obstruction has an ANOVA/spectral restatement. If

\[
T_n-ET_n=\sum_{\emptyset\ne S}(T_n)_S,
\qquad
a_S=\|(T_n)_S\|_2^2,
\]

then the retained product-refresh identity gives

\[
-C_n'(t)=\sum_{S\ne\emptyset}|S|e^{-|S|t}a_S.
\]

C09 gives a linear lower bound on the value at `t=0`, but this does not control the degrees `|S|` carrying that mass. The desired positive-noise persistence is precisely a low-enough-degree localization problem, rather than merely an initial-derivative problem.

## 5. (b) Routes tried and the precise reason each failed

### Route 1 — Boolean influence / geodesic membership

**Failure:** shallow cavities. For a one-edge cavity threshold `r`, geodesic membership has conditional probability

\[
1-e^{-r}=r+O(r^2),
\]

whereas the weighted coordinate variance behaves as

\[
\operatorname{Var}(\min\{X,r\})=\frac13r^3+O(r^4).
\]

Hence no uniform positive lower comparison can replace weighted passage sensitivity by Boolean edge membership. This is retained `X01`.

### Route 2 — raw common-geodesic overlap

**Failure:** common edges can all be shallow. The retained planar ladder obstruction `X02` has many common geodesic edges while their cavity thresholds vanish with system size, so the total weighted sensitivity tends to zero. Any usable overlap estimate must retain cavity depth or an equivalent passage-sensitivity weight.

### Route 3 — exact resampling/covariance identity alone

**What succeeded:** C04--C07 identify the correct weighted quantity exactly.

**Failure:** identity is not an estimate. It does not prevent the initial weighted sensitivity from disappearing on a very short positive-noise scale.

### Route 4 — zero-noise deep-edge abundance and linear initial covariance derivative

**What succeeded:** C08 supplies linearly many fixed-depth geodesic edges in expectation at `t=0`; C09 gives `-C_n'(0+) >= c_0 n` for an explicit `c_0>0`.

**Failure:** an initial derivative has no useful area without a persistence width. In the ANOVA language, the same linear initial derivative could in principle be carried at very high degrees, allowing rapid decay and leaving variance only logarithmic. C08/C09 therefore do not move the frozen lower-bound metric.

### Route 5 — Ahlberg--Deijfen--Sfragara chaos/overlap transition

**Failure for the present lower-bound task:** their natural transition scale is expressed through `Var(T_n)/n`. Using a conjectural `Var(T_n)~n^(2/3)` to choose the scale would assume the desired conclusion. Their machinery is highly relevant, but its variance-dependent normalization cannot be imported unchanged.

### Route 6 — Dembin--Elboim--Peled quantitative coalescence

**Failure for unconditional R07:** their strong quantitative overlap theorem assumes more than 32 extreme points of the limit shape. That geometry is not proved for ordinary Exp(1) FPP here. Importing it would make R07 depend circularly on an unresolved shape hypothesis/R08.

### Route 7 — Newman--Piza / Pemantle--Peres power improvement in nonflat/curved directions

**What the solved analogue has:** a curvature/nonflatness hypothesis localizes the geodesic in a sublinear strip and turns a count of relevant fluctuations into a polynomial variance lower bound.

**Failure for the present fixed unconditional metric:** the needed curvature/nonflatness is not proved for Exp(1) in the fixed `e1` direction. Such a statement is only **PARTIAL / CONDITIONAL** and cannot move the unconditional R07 metric.

### Route 8 — directed integrable LPP or numerical KPZ exponents

**Failure:** wrong model / non-proof. Integrable directed last-passage results and simulations do not settle ordinary undirected nearest-neighbor FPP.

## 6. (c) What a proof must contain that none of the routes contains

A successful unconditional variance lower-bound proof now needs a **variance-free stability mechanism at positive noise**. Concretely, it must prove that a macroscopic amount of the fixed-depth weighted geodesic sensitivity from C08 survives after refreshing a deterministic fraction of coordinates of order at least `n^{-1/3+o(1)}` (for the full KPZ lower exponent), or at least a scale large enough to improve the logarithmic metric.

It must control all of the following simultaneously:

1. off-geodesic shortcut creation after refresh;
2. dependence between the original and refreshed cavity thresholds `R_e,R_e^t`;
3. survival of the **same physical edge** on both minimizing paths, not merely existence of nearby alternative geodesics;
4. cavity depth bounded away from zero on the surviving overlap;
5. the above without assuming strict convexity, finite curvature, a transversal exponent, or a noise scale defined using the unknown variance.

No route tried so far contains all five ingredients.

## 7. (d) Simplest special case still unproved

The simplest source-relevant special case I cannot prove is exactly (BLOCK): fixed `delta,c>0` and deterministic noise `t_n=n^{-1/3}` with a linear expected number of survived, common, depth-`delta` geodesic edges.

A weaker theorem would already move the metric. For example, if for some deterministic `t_n` satisfying

\[
\frac{n t_n}{\log n}\longrightarrow\infty
\]

one could retain a linear depth-weighted common overlap at `t_n`, then integration of the retained covariance derivative would beat `c_PP log n` asymptotically. Even that variance-free statement is currently unproved.

## 8. (e) Nearest solved problem and the missing ingredient

The nearest dynamic analogue is Ahlberg--Deijfen--Sfragara, `Chaos, concentration and multiple valleys in first-passage percolation` (arXiv:2302.11367). Their proof develops precisely the covariance/co-influence/noise framework needed to relate fluctuations to geodesic instability.

What their theorem has that the present lower-bound problem cannot use is a **transition scale parametrized by the unknown variance itself**. For an analysis of chaos that is natural; for proving a new lower bound on that same variance it is circular unless the scale can be replaced by an independent deterministic one.

The nearest geometric analogue is the Newman--Piza/Pemantle--Peres polynomial lower-bound route under nonflat/curvature information. That proof gains a sublinear strip/localization theorem; unconditional Exp(1) in the fixed direction lacks exactly that geometry.

## 9. Exactly one recovery chosen

**Chosen recovery: port the Ahlberg--Deijfen--Sfragara continuous-noise covariance method to the deterministic scale `t_n=n^{-1/3}`, retaining the R07 cavity-depth truncation.**

The next R07 recovery run should not invent another overlap conjecture. It should read the ADS continuous-distribution proof line by line, identify every step where `Var(T_n)/n` is used, and attempt to replace that input by the retained C08 fixed-depth abundance plus a deterministic `n^{-1/3}` refresh scale. The success criterion is a source-matching estimate toward (BLOCK); the failure certificate should name the first precise ADS inequality whose proof genuinely requires the variance-defined scale.

This is one recovery choice only. I do not simultaneously launch a curvature route, a finite-computation route, or a queue switch in this stuck episode.

## 10. Independent audit of neighboring R08-L003

**Audit ID: `R07-AUDIT-R08-L003-03 = PASS` for the exact theorem/certificate; novelty remains UNVERIFIED.**

R08-L003 claims the auxiliary axis-time-constant lower bound

\[
\mu(e_1)\ge\frac{3753}{12500}=0.30024.
\]

R08's proof uses a `K=5` local-self-avoidance automaton, horizontal exponential tilt `z=22/7`, an exact positive Collatz vector with

\[
MV\le\frac{2407}{500}V,
\]

and an exact exponential-Chernoff summation with `lambda=38141/10000`.

I did not merely rerun R08's archived integer vector. The independent R07 checker reconstructs the 284-state / 780-transition automaton from the definition and uses a **separately regenerated hard-coded integer certificate at scale `10^10`**, rather than R08's archived `10^8` vector. All PASS decisions are exact `Fraction`/integer comparisons. It verifies

\[
\max_i\frac{(MV)_i}{V_i}
=
\frac{638973201626}{132732295445}
<\frac{2407}{500},
\]

\[
\rho=rac{\Lambda}{1+\lambda}=\frac{48140}{48141}<1,
\]

and an exact rational Taylor-plus-geometric-tail bound proving the final geometric base is strictly below one. It also exhaustively checks, for every direction word of lengths 1 through 9 (349,524 cases), that every globally simple word is accepted by the finite-memory automaton, as a sanity check of the language inclusion used in the proof.

Artifacts:

- `artifacts/R07/20260916T1624Z_r08_l003_independent_audit.py` @ creation commit `231d60428be29c6dbbd749e17e169e82f683a085`;
- `artifacts/R07/20260916T1624Z_r08_l003_independent_audit.out` @ creation commit `f4b72299ae7301df2712cce197e932a6d78fede5`;
- archived output begins `PASS`.

Audit scope: the exact certificate and written path-count/Chernoff argument support R08-L003. I do **not** certify novelty: R08 itself notes Janson (1981) and Alm--Parviainen (2002) transition-matrix work and did not have the latter's full numerical table. I also do not certify R08's strict-convexity source target; its frozen strict-gap metric remains zero and the source problem remains OPEN.

## 11. Stuck status and next-run rule

This is **STUCK RECOVERY 1** for the current R07 target. The metric has failed to move for three consecutive canonical runs after the baseline. The obstruction is no longer vague: it is positive-noise persistence of fixed-depth common geodesic edges, equivalently sufficiently low-degree localization of the retained weighted sensitivity.

A later successful recovery that moves the fixed metric resets the immediate stagnation sequence by actual metric movement only. A new lemma, renamed obligation, or different auxiliary quantity does not count as movement. If this hard target later reaches the owner's third stuck episode after at most two recoveries, it must hand off and rotate according to the fleet protocol.

## ledger_delta

```yaml
ledger_delta:
  task: "R07 HARD OUTSIDE"
  source: "Kardar-Parisi-Zhang (1986); Auffinger-Damron-Hanson, arXiv:1511.03262, Question 13"
  target: "For iid Exp(1) undirected nearest-neighbor FPP on Z^2, prove Var(T(0,n e1)) = n^(2/3+o(1))"
  metric: "strongest rigorously proved uniform lower-bound function b(n) for Var(T(0,n e1)), constants and n-domain retained"
  domain: "integers n>=2, fixed direction e1, iid mean-one Exp(1) edge weights"
  before: "b(n)=c_PP log n, c_PP>0 fixed non-explicit"
  after: "b(n)=c_PP log n, c_PP>0 fixed non-explicit — NO MOVEMENT"
  status: "OPEN / STUCK RECOVERY 1"
  unchanged_count: 3
  exact_evidence:
    - "runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md @ e9420902b01dec21ffa7bc077777a58ac87ba5a5 (retained C01-C09)"
    - "artifacts/R07/20260916T1624Z_r08_l003_independent_audit.py @ 231d60428be29c6dbbd749e17e169e82f683a085"
    - "artifacts/R07/20260916T1624Z_r08_l003_independent_audit.out @ f4b72299ae7301df2712cce197e932a6d78fede5"
  audit_ids:
    - "R07-AUDIT-R08-L003-03=PASS"
  selected_recovery: "Port the Ahlberg-Deijfen-Sfragara continuous-noise covariance method to deterministic t_n=n^(-1/3), retaining fixed-depth cavity weights; do not use a variance-defined scale."
  root_ledger_action: "none; P26 is sole RESULTS/QUEUE/POSTED writer"
```

## Primary references

- M. Kardar, G. Parisi, Y.-C. Zhang, `Dynamic Scaling of Growing Interfaces`, Phys. Rev. Lett. 56 (1986), 889--892; published 3 March 1986.
- R. Pemantle, Y. Peres, `Planar first-passage percolation times are not tight`, arXiv:math/0404050.
- A. Auffinger, M. Damron, J. Hanson, `50 years of first-passage percolation`, arXiv:1511.03262.
- D. Ahlberg, M. Deijfen, M. Sfragara, `Chaos, concentration and multiple valleys in first-passage percolation`, arXiv:2302.11367.
- B. Dembin, D. Elboim, R. Peled, `Coalescence of geodesics and the BKS midpoint problem in planar first-passage percolation`, arXiv:2204.02332.
- R. Basu, V. Sidoravicius, A. Sly, `Rotationally invariant first passage percolation: Breaking the n/log n variance barrier`, arXiv:2604.01214 (different model).
