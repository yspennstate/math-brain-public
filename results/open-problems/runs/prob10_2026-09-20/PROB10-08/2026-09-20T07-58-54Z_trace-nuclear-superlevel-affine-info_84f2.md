Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 maximum was requested, but no authenticated runtime metadata available to this run establishes that setting. **NO SOURCE-METRIC MOVEMENT:** Salez Problem 2.3 remains OPEN/PARTIAL and `W_exp=1/2 provisional -> 1/2 provisional`. **MECHANISM MOVEMENT:** a new trace/nuclear argument removes the predecessor's moderate-localization restriction for every exponent, yields a universal heat-kernel information-tail/varentropy envelope, and converts the affine mutual-information bottleneck into one exact monotone conditional-information functional.

# PROB10-08 — trace/nuclear superlevel obstruction and affine conditional-information monovariant

Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL / substantive obstruction and reduction theorems proved / no new source-level cutoff class this run / independent validation pending / worldwide novelty UNVERIFIED**.

## 0. Required continuity and consumed state

Before research I read/recovered the required state and did not reset prior failures:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- current root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`, preserving the exclusion of the already-written Abelian Cayley/product-condition target;
- canonical `operations/claims/I0112.md`, blob `707af6a4ca81d0d6bcf52225c6f69c266ae981e9`;
- preserved R16 pre-refocus successor handoff `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`;
- historical I0112 stuck report `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md`, preserving the failed product-varentropy, synchronous-tensor, moving-weight/local-Poincare, Hecke/information-curvature, ordinary-curvature, local-limit/AEP and time-zero subcommutation routes;
- newest own predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T06-57-55Z_relation-block-persistence-affine-quotient_b631.md`, blob `271d6ee62c6bcb17357aa900f636c9eac08aa80a`;
- newest neighboring P26 T08 report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_10-10-50__biregular-halved-green-transfer.md`, blob `fd122a821741be5930402d33bed302d43a6f9544`; P26 owns Green/spherical and biregular-halving transfer;
- newest neighboring NM13 T08 report `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T07-22-00Z__reversal-arc-orbit-likelihood.md`, blob `1c033f20afeaee2d9e1e5b1028afc45e3bd9a01c`; NM13 owns arc-cover/Hodge/reversal/orbit routes.

Accordingly this run does not duplicate P26's spherical/halved-graph work, NM13's arc/reversal work, or the old R16 tensor and moving-Poincare routes.

## 1. Primary-source refresh

The frozen source remains Justin Salez, `https://arxiv.org/abs/2508.21055`, Problem 2.3: prove cutoff for all bounded-degree vertex-transitive expander sequences. The exact source convention is rate-one continuous time,

\[
H_t=e^{t(P-I)}.
\]

Dylan J. Altschuler, `https://arxiv.org/abs/2609.14945`, remains the primary new positive lead. The bounded 20 September 2026 check still exposed only v1, submitted 14 September 2026; no correction/erratum or v2 surfaced. I reread the full proof. Its long-range-expansion premise is used exactly to:

1. transfer maximal-rate growth to the oriented-edge NBRW state space (Lemma 3.2);
2. turn this growth into near-maximal Shannon entropy by the forest/restart argument (Lemma 3.3);
3. obtain endpoint entropy `log n-O(log log n)` (Proposition 3.1);
4. after that, ordinary spectral expansion only performs the short entropy-to-TV cleanup.

Thus the full-source missing input is still an entropy/Green replacement for LRE that follows from transitivity plus spectral expansion alone.

Pedrotti--Salez, `https://arxiv.org/abs/2607.05345v2`, was also rechecked. Their local-product theorem remains a relevant baseline, but the historical R16 moving-weight/local-Poincare route already targeted it and is not restarted here.

## 2. New idea before calculations

The preceding report converted non-cutoff into a symmetric automorphism-invariant high-likelihood relation

\[
R(x)=\{y:nH_t(x,y)\ge n^a\}
\]

at the **early** threshold `t=t_mix(1-epsilon)`, with fixed positive heat mass `b` and degree at most `n^(1-a)`. Its block-concatenation theorem needed powers of that degree to stay sublinear, so it did not control the moderate regime `a<=1/2`.

The new idea was to stop composing the relation. Normalize its adjacency matrix and pair it directly with the heat kernel in trace duality. Vertex transitivity makes the trace exactly the relation's heat mass, while the ordinary gap controls the heat operator and regularity controls the relation's nuclear norm. This produces the formal `k->infinity` endpoint of the old block bound in one step, with no support-size restriction.

## 3. Main theorem — all-exponent invariant-relation bound

Let `G` be any finite connected regular vertex-transitive graph on `n` vertices, let `gamma=1-lambda_2(P)`, and define for `u>0`

\[
R_u(x)=\{y:nH_t(x,y)\ge u\},
\quad
m_u=|R_u(x)|,
\quad
M_u=H_t(x,R_u(x)).
\]

Then the matching artifact proves the exact finite-graph inequality

\[
\boxed{
M_u\le \frac{m_u}{n}+e^{-\gamma t}\sqrt{m_u}.
}
\tag{3.1}
\]

Since `m_u<=n/u`,

\[
\boxed{
M_u\le u^{-1}+e^{-\gamma t}\sqrt{n/u}.
}
\tag{3.2}
\]

The proof is short but complete. If `Q_u` is normalized adjacency of the invariant relation, then

\[
\operatorname{tr}(H_tQ_u)=\frac{nM_u}{m_u}.
\]

Writing `H_t=Pi+E_t`, one has `||E_t||op<=e^{-gamma t}`, `tr(Pi Q_u)=1`, and because `Q_u` has `nm_u` entries equal to `1/m_u`,

\[
\|Q_u\|_*\le\sqrt n\|Q_u\|_F=\frac n{\sqrt{m_u}}.
\]

Trace duality gives (3.1).

### Consequence for a hypothetical non-cutoff sequence

For the predecessor's relation with threshold `u=n^a`, mass at least fixed `b>0`, and degree at most `n^(1-a)`, (3.1) yields

\[
b\le n^{-a}+e^{-\gamma t}n^{(1-a)/2}.
\]

Hence every source counterexample must satisfy

\[
\boxed{
\frac{\gamma t_{mix}(1-\varepsilon)}{\log n}
\le\frac{1-a}{2}+o(1),
}
\tag{3.3}
\]

or equivalently

\[
\boxed{
a\le1-2\gamma t_{mix}(1-\varepsilon)/\log n+o(1).}
\tag{3.4}
\]

Unlike the previous block theorem, this is valid for **every** `a>0`, including the moderate regime `a<=1/2`. Thus the prior technical hole is removed. It does not close Salez 2.3 because the surviving right-hand side can still be a positive constant on bounded-degree spectral expanders.

## 4. Two further exact outputs

### 4.1 Schatten interpolation

For

\[
R_p(t)=\sum_{i=2}^n e^{-p(1-\lambda_i)t},
\]

the artifact proves, by Schatten duality, the full interpolation

\[
M_u\le \frac{m_u}{n}+
\begin{cases}
(R_p(t)m_u/n)^{1/p},&1\le p\le2,\\
R_p(t)^{1/p}n^{-1/p}\sqrt{m_u},&2\le p\le\infty.
\end{cases}
\tag{4.1}
\]

This diagnoses the obstruction cleanly. The `p=2` endpoint is Green/chi-square and is known from the affine Haiman stress family to be polynomially bad at the plausible TV scale; the `p=infinity` endpoint is (3.1) and is universal but loses a constant exponent. A full proof needs genuinely new information between these endpoints, not another formal interpolation.

### 4.2 Universal transitive varentropy envelope

For

\[
Z_t=\log(nH_t(x,X_t)),\qquad X_t\sim H_t(x,\cdot),
\]
(3.2) gives

\[
\Pr(Z_t\ge z)
\le e^{-z}+e^{(A_t-z)/2},
\qquad
A_t=\log n-2\gamma t.
\]

The negative second moment is at most `4/e^2`, and exact tail integration gives

\[
\boxed{
\operatorname{Varent}(H_t(x,\cdot))
\le (A_t)_+^2+4(A_t)_++11.
}
\tag{4.2}
\]

Applying Salez Theorem 5.1 at the correct early threshold `t_-=t_mix(1-epsilon)` yields the valid auxiliary estimate

\[
\boxed{
 w_{mix}(\varepsilon)
\le \frac{2}{\gamma\varepsilon^2}
\left[1+\sqrt{(A_-)_+^2+4(A_-)_++11}\right],
\quad A_-=\log n-2\gamma t_-.
}
\tag{4.3}
\]

This is labeled auxiliary rather than source movement: `A_-` can still be `Theta(log n)` in the full source class.

## 5. Third materially different route — affine information defect

The previous affine analysis used relative coordinates `(M,Y)` with `Y=M^{-1}x`, where `Y` is autonomous and the joint entropy deficit splits into subgroup deficit, quotient deficit and mutual information. This run found a cleaner exact object:

\[
\boxed{
J_t=D(\mathcal L(M_t,Y_t)\|U_{\Pi}\otimes\mathcal L(Y_t))
=D(\mathcal L(M_t)\|U_{\Pi})+I(M_t;Y_t).
}
\tag{5.1}
\]

The affine transition kernel maps every product law `U_Pi tensor nu` to `U_Pi tensor (nu Q_Y)`. Therefore data processing proves

\[
\boxed{J_t\text{ is nonincreasing in }t.}
\tag{5.2}
\]

Moreover

\[
D(\mathcal L(M_t,Y_t)\|U_\Pi\otimes U_V)
=J_t+D(\mathcal L(Y_t)\|U_V).
\tag{5.3}
\]

This turns the predecessor's two-term mutual-information obstruction into one exact Lyapunov functional plus an autonomous quotient term. The missing step is quantitative: an individual subgroup move can encode the selected generator into `Y`, so subgroup spectral expansion alone does not force one-step decay of `J_t`. Any successful estimate must be genuinely multi-step/hypocoercive and use interlacing with translations. No affine cutoff theorem is claimed.

## 6. Three nonexhausted approaches compared

**A. Trace/nuclear invariant-superlevel duality — RETAINED.** It proves (3.1)--(3.4) and removes the prior moderate-localization restriction without composing relations.

**B. Schatten interpolation — RETAINED AS DIAGNOSTIC, NOT CLOSED.** It proves (4.1), but the affine stress family rules out the naive Green endpoint and the ordinary gap leaves a constant-exponent loss at the operator-norm endpoint.

**C. Affine conditional-information monovariant — RETAINED AS STRUCTURAL ROUTE, DECAY OPEN.** It proves (5.1)--(5.3), but identifies a precise hypocoercive obstruction to using subgroup mixing in one step.

These are materially different from the immediately preceding block-composition argument and from the historical moving-weight Poincare and tensor routes.

## 7. Current literature/prior-art check

A bounded search on 20 September 2026 for combinations of `vertex-transitive heat kernel superlevel relation trace norm`, `Schatten heat kernel cutoff`, and `vertex-transitive varentropy` surfaced Salez's varentropy work and general Schatten/small-set literature, but no exact match to (3.1) or (4.2). This is negative evidence only; worldwide novelty remains **UNVERIFIED**.

Altschuler's arXiv record remains v1 in the bounded current check. His theorem is not counted as new fleet progress, and LRE is not assumed to follow from transitive spectral expansion.

## 8. Tests actually run

No finite simulation, mixing plot, numerical optimization or brute-force checker was used. There is no finite computational core.

Analytic self-checks performed:

- exact trace identity for invariant relations;
- Frobenius/nuclear norm calculation;
- both Schatten-duality regimes and the common `p=2` endpoint;
- explicit integration producing the constants in the varentropy envelope;
- invariance of the affine product manifold and data-processing monotonicity of `J_t`.

These are self-checks only. Independent audit count remains `0`.

## 9. Source before/after and ledger delta

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  exact_walk: "rate-one continuous-time simple random walk"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  new_graph_class_with_TV_cutoff: false
  mechanism_before:
    - "non-cutoff forces early-threshold polynomial invariant localization"
    - "multi-block relation persistence only while relation powers remain sublinear"
    - "affine joint deficit split into subgroup, quotient, and mutual-information terms"
  mechanism_after:
    - "all-exponent relation mass bound M <= m/n + exp(-gamma t) sqrt(m)"
    - "moderate-localization restriction removed without relation composition"
    - "Schatten-p interpolation hierarchy"
    - "universal transitive varentropy envelope in terms of log n - 2 gamma t"
    - "one monotone affine conditional-information defect J_t"
  finite_checker: "not applicable"
  independent_audits: 0
  publication_novelty: "UNVERIFIED"
  status_label: "OPEN/PARTIAL"
```

## 10. Matching artifact, readback and remaining full-scope gap

The complete proof is stored in the create-only artifact

`artifacts/prob10_2026-09-20/PROB10-08/2026-09-20T07-58-54Z_trace-nuclear-superlevel-affine-info_84f2.md`,

created at commit

`31febf16d428fb400d2ea3b59a3c4a18741f77e0`,

blob `3369ada9838cbcd4d27027efed2a89eab80bdebb`, and read back at that exact commit before this report write.

The remaining source-level gap is now a constant-exponent one rather than the predecessor's relation-composition gap. A full proof needs either:

1. a transitivity-specific improvement of the nuclear estimate for the **particular heat-kernel superlevel relation**, strong enough to turn the positive-information tail from polynomial to subpolynomial at the early mixing threshold; or
2. a quantitative multi-step decay theorem for an affine/general hypocoercive conditional-information defect that survives the source-admissible non-LRE stress families; or
3. an admissible counterexample realizing the surviving low-exponent localization and a genuinely broad TV window.

No scheduler state, cadence, enabled state, email, Drive object, public post, permission, workflow, shared root, peer file or force push is changed by this run.