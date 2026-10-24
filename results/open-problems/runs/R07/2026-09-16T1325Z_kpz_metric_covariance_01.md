Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED by the runtime; GPT-6 maximum was requested, but the scheduler exposed no model or reasoning selector and I do not claim GPT-6 maximum.
Problem: ordinary undirected Exp(1) first-passage variance on Z^2 — Auffinger–Damron–Hanson (2015), Question 13; Kardar–Parisi–Zhang (1986).
Metric movement: UNMEASURED -> b(n)=c_PP log n for all integers n>=2 after fixing a positive theorem constant c_PP for the e1 direction; status OPEN; unchanged-count UNKNOWN because no prior canonical R07 run was found.

# R07 canonical GitHub run — variance lower-bound baseline and exact sensitivity identities

Run date: 2026-09-16.
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Admission, source, exact target, and current status

Outside source locator: Auffinger–Damron–Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 13. The survey asks, under suitable conditions on the passage-time law, to prove the fluctuation exponent chi is <1/2 in d>=2 and, in d=2, chi=1/3. For iid Exp(1) nearest-neighbor edge weights on Z^2, the variance formulation tracked here is

\[
T_n:=T(0,ne_1),\qquad \operatorname{Var}(T_n)=n^{2/3+o(1)}.
\]

This run tracks only the fixed metric requested by the fleet protocol:

> **metric** = strongest rigorously proved uniform lower-bound function b(n) such that Var(T_n) >= b(n), retaining hypotheses, constants, and n-domain.

The transversal exponent and limiting law are separate and remain OPEN.

Current-status search performed 2026-09-16 against the original survey, current arXiv search, later lower-bound papers, and the 2026 variance literature. I found no unconditional ordinary-lattice result improving the uniform point-to-point lower-bound order beyond logarithmic variance. In particular:

- Pemantle–Peres, arXiv:math/0404050, Theorem 1: iid mean-one exponential nearest-neighbor FPP on Z^2, any fixed unit direction v, Var(T(0,v^(n))) >= C log n. Taking v=e1 gives the present target direction. The theorem states an unspecified positive constant C; no numerical value is supplied. For the fixed e1 direction I denote one valid constant by c_PP>0. Since decreasing c_PP if necessary absorbs finitely many n, I record the uniform comparison as `b(n)=c_PP log n` for integers n>=2.
- Bates–Chatterjee, arXiv:1810.03656, gives sqrt(log n)-order fluctuation lower bounds in broad planar growth settings; this does not improve the present variance order beyond log n.
- Damron–Houdre–Ozdemir, arXiv:2204.06592, notes the known point-to-point sqrt(log |x-y|) fluctuation lower bound and obtains polynomial lower bounds for a different square-crossing variable under curvature; it does not improve the unconditional point-to-point metric here.
- Dembin–Elboim, arXiv:2505.03211, concerns minimal left-right square crossings, with stronger lower bounds under curvature assumptions; it is not an unconditional improvement for T(0,ne1).
- Damron–Hanson–Sosoe, arXiv:1306.1197, proves the point-to-point upper bound C n/log n under assumptions covering Exp(1).
- Ahlberg–Deijfen–Sfragara, arXiv:2302.11367, proves a rigorous fluctuations/chaos/geodesic-overlap connection, but identifies the chaos transition in terms of the unknown variance scale itself.
- Basu–Sidoravicius–Sly, arXiv:2604.01214 (2026-04-01), gives a polynomial improvement of n/log n only for a different rotationally invariant Riemannian FPP model and explicitly describes O(n/log n) as the standing upper bound in nontrivial ordinary FPP variants.

Therefore the fixed metric after this run is

\[
\boxed{b(n)=c_{\rm PP}\log n,\qquad n\ge 2,\qquad c_{\rm PP}>0,}
\]

with c_PP non-explicit and depending at worst on the fixed direction/model. Status remains OPEN.

Historical source check: Kardar–Parisi–Zhang, *Dynamic Scaling of Growing Interfaces*, Phys. Rev. Lett. 56 (1986), 889–892, was published 3 March 1986. Directed integrable last-passage models are not being substituted for this undirected FPP problem.

## 2. Repository recovery / protocol compliance

Read before working:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`;
- root `RESULTS.md`;
- root `QUEUE.md`;
- `operations/FLEET_2026-09-16.md`;
- `operations/RFLEET_2026-09-16.md`;
- newest canonical neighboring report located for R01: `runs/R01/2026-09-16T1258Z_i0024_flow_duality_01.md`.

`RESULTS.md` supplied the R07 baseline `UNMEASURED | OPEN` for this metric. No canonical `runs/R07/` report existed on branch master when this run began, so I do not invent a stagnation count: it remains UNKNOWN.

A canonical R08 package was not available under `runs/R08/` in the authorized GitHub repository this run, so no R08 lemma is imported or audited. This is nonblocking and is recorded under `audit_ids` below.

Intake ledgers discovered at repository root and read-attempted: `probability_1000_intake_claude_20260907/problems.jsonl` and D, E, F, G, H, I dated 2026-09-08 through 2026-09-14. The connector returned these large JSONL resources with model-visible truncation. I therefore record intake ingestion as **PARTIAL due connector truncation**, not falsely as a complete row-by-row read. I did not use any old `admitted=true` field as current verification. The current R07 admission rests instead on the outside source plus the fresh 2026-09-16 literature check above.

No Gmail or Drive read/write occurred.

## 3. R07-GH-C01 — metric baseline

**Label: KNOWN.**

For iid Exp(1) nearest-neighbor FPP on Z^2, there exists c_PP>0 such that, for the fixed direction e1,

\[
\operatorname{Var}(T(0,ne_1))\ge c_{\rm PP}\log n\qquad(n\ge2).
\]

Primary evidence: Pemantle–Peres, Theorem 1. The theorem proves the result for every fixed unit direction, with the lattice endpoint obtained by coordinatewise integer parts of nv; for v=e1 the endpoint is exactly ne1.

No stronger unconditional point-to-point lower-bound order was verified in the current search.

## 4. R07-GH-C02 — exact Doob martingale variance identity

**Label: KNOWN; proof included.**

Enumerate the lattice edges `e_1,e_2,...` and let

\[
\mathcal F_k=\sigma(\tau_{e_1},\ldots,\tau_{e_k}),\qquad
M_k=E[T_n\mid\mathcal F_k].
\]

Since the straight coordinate path from 0 to ne1 has passage time

\[
S_n=\sum_{j=1}^n X_j,\qquad X_j\stackrel{iid}{\sim}\mathrm{Exp}(1),
\]

we have `0<=T_n<=S_n`, hence `T_n in L^2`. Therefore `M_k -> T_n` in L^2. Martingale differences

\[
D_k=M_k-M_{k-1}
\]

are pairwise orthogonal in L^2: for j<k,

\[
E[D_jD_k]=E[D_jE(D_k\mid\mathcal F_{k-1})]=0.
\]

Thus

\[
E[(M_m-M_0)^2]=\sum_{k=1}^mE[D_k^2].
\]

Passing m->infinity by L^2 convergence gives the exact identity

\[
\boxed{\operatorname{Var}(T_n)=\sum_{k\ge1}E[(M_k-M_{k-1})^2].}
\]

This identity by itself contains no KPZ exponent; the hard issue is estimating the energy distribution over coordinates/scales.

## 5. R07-GH-C03 — exact one-edge exponential cavity sensitivity

**Label: PROVED (elementary product-space identity; no novelty claim).**

Freeze all edge weights except one edge e with weight X_e. Positive weights imply that a minimizing path may be chosen simple, hence uses e at most once. Let

- A_e = best path cost from 0 to ne1 among paths avoiding e, possibly infinity;
- B_e = best cost of all other edges among simple paths from 0 to ne1 using e, possibly infinity.

Then

\[
T_n=\min\{A_e,B_e+X_e\}.
\]

Therefore there are off-e-measurable C_e and R_e in [0,infinity] such that

\[
\boxed{T_n=C_e+\min\{X_e,R_e\}.}
\]

Off the null tie event,

\[
\boxed{e\in\gamma_n\iff X_e<R_e.}
\]

For X~Exp(1), finite r,

\[
E\min(X,r)=1-e^{-r},
\]

\[
E\min(X,r)^2=2-2(r+1)e^{-r},
\]

and hence

\[
\boxed{q(r):=\operatorname{Var}(\min(X,r))=1-2re^{-r}-e^{-2r}.}
\]

Set q(infinity)=1. The corresponding geodesic-membership probability is

\[
p(r)=P(X<r)=1-e^{-r}.
\]

On finite exhaustions Efron–Stein gives

\[
\operatorname{Var}(T_n)\le\sum_e E\,q(R_e),
\]

and monotone/finite-exhaustion passage yields the usual infinite-product formulation when justified. This is an **upper sensitivity relation**, not a lower-bound proof.

## 6. R07-GH-X01 — refutation of Boolean-influence equivalence

**Label: REFUTED ROUTE, not a refutation of the open problem.**

A tempting Shmalo-style influence transfer would require a uniform comparison of weighted cavity variance `q(r)` to Boolean membership probability `p(r)`. The exact checker gives

\[
p(r)=r-\frac12r^2+\frac16r^3+O(r^4),
\]

\[
q(r)=\frac13r^3-\frac13r^4+O(r^5),
\]

so

\[
\boxed{\frac{q(r)}{p(r)}=\frac13r^2+O(r^3)\longrightarrow0.}
\]

Therefore no constant c>0 can satisfy

\[
q(r)\ge c\,p(r)\qquad\text{for all }r>0.
\]

This is an exact counterexample to identifying Boolean geodesic membership influence with the weighted passage-time sensitivity that appears in the variance decomposition. It directly enforces the user requirement not to confuse the two notions.

## 7. R07-GH-C04 — exact product-refresh / ANOVA covariance identity

**Label: KNOWN PRODUCT-SPACE IDENTITY; proof included.**

Let `f` be centered and square-integrable on a countable product probability space and write its orthogonal ANOVA decomposition

\[
f=\sum_{\emptyset\ne S}f_S.
\]

Let `P_t` be the continuous-time coordinate-refresh semigroup in which every coordinate independently survives without refresh to time t with probability e^{-t}. Then

\[
P_tf_S=e^{-|S|t}f_S.
\]

Hence for X stationary and X^t its refreshed copy,

\[
\boxed{
\operatorname{Cov}(f(X),f(X^t))
=\|P_{t/2}f\|_2^2
=\sum_{S\ne\emptyset}e^{-|S|t}\|f_S\|_2^2.
}
\]

For the one-coordinate conditional variance operator,

\[
\sum_eE[\operatorname{Var}_e(P_tf)]
=\sum_{S\ne\emptyset}|S|e^{-2|S|t}\|f_S\|_2^2.
\]

Since for every integer k>=1,

\[
2\int_0^\infty k e^{-2kt}\,dt=1,
\]

Tonelli gives the exact integrated identity

\[
\boxed{
\operatorname{Var}(f)
=2\int_0^\infty
\sum_eE[\operatorname{Var}_e(P_tf)]\,dt.
}
\]

The exact-arithmetic checker verifies the finite-cube version, including Doob, ANOVA, a survival probability a=1/2 refresh kernel, and the integrated coefficient identity.

## 8. What overlap estimate is actually needed, and why current chaos theorems do not close it

**Label: PARTIAL REDUCTION.**

For `f=T_n-E T_n`, C04 says a proof can be organized around the scale-integrated weighted sensitivity

\[
\mathcal I_n(t):=
\sum_eE[\operatorname{Var}_e(P_tT_n)],
\qquad
\operatorname{Var}(T_n)=2\int_0^\infty\mathcal I_n(t)\,dt.
\]

This is the exact quantity that a multiscale noise/overlap argument has to estimate. C03/X01 show why a theorem stated only in terms of unweighted geodesic membership probabilities is not automatically enough: shallow cavity edges can have membership probability of order r but variance sensitivity only order r^3.

Ahlberg–Deijfen–Sfragara rigorously establish a fluctuations/chaos/geodesic-overlap correspondence under random resampling, and identify the stability-to-chaos transition in terms of the variance of the FPP system. This is highly relevant, but it does **not** supply the missing KPZ scale independently: inserting Var(T_n)~n^(2/3) into the transition scale would be circular. The open obligation is therefore a non-circular bound on the weighted, scale-integrated overlap/sensitivity above, derived from geometry or resampling without assuming the target variance exponent.

No curvature assumption is used here. The conditional polynomial lower bounds mentioned by Pemantle–Peres/Newman–Piza under nonflat/curvature hypotheses remain PARTIAL and do not change the fixed unconditional metric.

## 9. Exact checker / certificates

Executed exact-arithmetic checker:

- `artifacts/R07/20260916T1325Z_metric_covariance_checker.py`
- `artifacts/R07/20260916T1325Z_metric_covariance_checker.out`

Local SHA-256 before GitHub upload:

- checker source: `ebcebe305b922c3bf7c1b469f0a32d032872af8c1d25a0c9b91b3254f6775d3a`
- checker output: `8a1bd8b20fbb25763d422d31fb0622e3d9acda13d6a4a0dc04cdf335b1234ba4`

Exact output begins `PASS` and verifies:

1. the cavity mean, second moment, variance formula, and series;
2. `q(r)/p(r)->0` with leading ratio `r^2/3`;
3. an exact 3-bit rational Doob decomposition;
4. exact ANOVA variance reconstruction;
5. exact refresh covariance at survival probability 1/2;
6. the integrated coefficient `2k int_0^infinity exp(-2kt)dt=1` for k=1,2,3.

Self-checks are explicitly self-checks; no independent audit is fabricated.

## 10. Ledger / failed routes / next attack

Current ledger:

- R07-GH-C01: `b(n)=c_PP log n` lower bound — **KNOWN**.
- R07-GH-C02: Doob variance identity — **KNOWN / PROVED ON PAGE**.
- R07-GH-C03: exact Exp(1) one-edge cavity variance — **PROVED elementary**.
- R07-GH-X01: uniform Boolean-membership-to-weighted-sensitivity lower comparison — **REFUTED as a route**.
- R07-GH-C04: product-refresh/ANOVA integrated sensitivity identity — **KNOWN / PROVED ON PAGE**.
- KPZ variance target — **OPEN**.
- transversal exponent — **OPEN**.
- limiting law — **OPEN**.

Preserved failed/forbidden routes:

- substituting integrable directed last-passage percolation;
- silently assuming strict or uniform limit-shape curvature;
- equating Boolean geodesic influence with weighted passage sensitivity;
- using a chaos transition normalized by the unknown variance as if it determined that variance;
- numerical KPZ exponents as a theorem.

The next mathematical attack should keep the fixed metric and attempt to improve it, not reset it. Two precise options are admissible:

1. re-open the Pemantle–Peres growth-order conditioning and ask whether the exact conditional variance can be strengthened beyond `log n` by a new unconditional lower bound on the Eden boundary sequence `Y_k`; or
2. derive a **lower** counterpart to the exact weighted refresh identity at selected noise times by proving a non-circular lower bound on the weighted overlap of the original and refreshed geodesic, with the shallow-cavity suppression from X01 explicitly retained.

A failure of both should trigger the fleet stuck protocol rather than another cosmetic lemma.

## 11. Dated current-status queries

Queries run 2026-09-16 included:

- `Auffinger Damron Hanson 50 years first passage percolation Question 13 fluctuation exponent chi 1/3 arXiv 1511.03262`;
- `Pemantle Peres Planar first-passage percolation times are not tight exponential variance log n theorem`;
- `Damron Hanson Sosoe sublinear variance first passage percolation general distributions n log n exponential`;
- `Ahlberg Deijfen Sfragara chaos concentration multiple valleys first passage percolation variance overlap noise`;
- `Basu Sidoravicius Sly rotationally invariant first passage percolation breaking n log n variance barrier`;
- later lower-bound searches covering Bates–Chatterjee, Damron–Houdre–Ozdemir, and Dembin–Elboim.

No searched source produced an unconditional ordinary-lattice point-to-point variance lower-bound order stronger than `log n` for iid Exp(1).

Primary URLs:

- https://arxiv.org/abs/1511.03262
- https://arxiv.org/abs/math/0404050
- https://arxiv.org/abs/1306.1197
- https://arxiv.org/abs/2302.11367
- https://arxiv.org/abs/2604.01214
- https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.56.889

```yaml
ledger_delta:
  source: "Auffinger–Damron–Hanson (2015), arXiv:1511.03262, Question 13; Kardar–Parisi–Zhang (1986)"
  target: "Var(T(0,n e1)) = n^(2/3+o(1)) for iid Exp(1) undirected nearest-neighbor FPP on Z^2"
  metric: "strongest rigorously proved uniform lower-bound function b(n)"
  before: "UNMEASURED"
  after: "b(n)=c_PP log n for integers n>=2, with c_PP>0 non-explicit, from Pemantle–Peres Theorem 1 in the e1 direction"
  status: "OPEN"
  unchanged_count: "UNKNOWN"
  exact_evidence:
    - "Pemantle–Peres, arXiv:math/0404050, Theorem 1"
    - "artifacts/R07/20260916T1325Z_metric_covariance_checker.py"
    - "artifacts/R07/20260916T1325Z_metric_covariance_checker.out"
  audit_ids:
    - "R08: NOT AVAILABLE as a canonical GitHub package this run"
    - "R01 neighbor read: runs/R01/2026-09-16T1258Z_i0024_flow_duality_01.md (not imported into FPP)"
  repository_read_status:
    intake_ledgers: "PARTIAL: all discovered root intake ledgers were read-attempted, but GitHub connector truncated large JSONL responses; no old admitted=true flag was treated as current verification"
```
