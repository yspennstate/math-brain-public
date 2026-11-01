Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **NO MOVEMENT in the fixed metric: `R_unique=+infinity -> +infinity`; Section-B moves tried: #12 FIND WHAT IS CONSERVED, #25 COUNT THE SAME THING TWICE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**
Problem/source: Héctor Jardón-Sánchez, Sam Mellick, Antoine Poulin, Konrad Wróbel, *Exactness and the topology of the space of invariant random equivalence relations*, PLMS 132(5) (2026), e70158, arXiv:2502.11622v2, **Question 2**; intake **I0079**.

# R06 CLOSABLE OUTSIDE — run 5 on I0079: the global-label case is KNOWN; the source's pointwise-random refinement is phase-nonunique on `F_2 x F_2`

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity and why I0056 was not restarted

The scheduler prompt still names I0056 / Lyons--Peres Question 6.20, but repository continuity is authoritative. R06 already reached the six-unchanged-run rotation threshold on I0056 and created the canonical I0079 claim. I therefore did **not** restart I0056. Its `H_{5,5}` width-zero result and full-source `PARTIAL / audit-gated` handoff remain preserved in earlier immutable R06 reports.

I reread/rechecked current `master`, including `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0079.md`, the newest R06 report `runs/R06/20260917T0017Z_i0079_stuck_priorart_bridge_04.md`, and the newest neighboring R07 package. The canonical claim still assigns I0079 exclusively to R06. No posted exclusion or newer owner was found.

The fixed metric remains

`R_unique = largest radius on which all subsequential limits agree for the frozen global-iid-nucleus-label refinement on Gamma=F_2 x F_2`.

It was already `+infinity`; it remains `+infinity`. The previous I0079 unchanged count was 3, so this run records unchanged count 4. This run nevertheless resolves the prior-art status of that frozen refinement and then moves, as the previous stuck report required, to the simplest different source-admissible refinement.

## 2. Fresh source and literature check (2026-09-17)

The current accepted/arXiv-v2 source was opened and its relevant PDF pages visually rechecked. It fixes a left-invariant proper metric, notes that graph Voronoi cells may share boundary vertices, and explicitly says one may refine equivariantly by having **each boundary point pick one tied nucleus at random**; it then fixes a refinement. Its Question 2 remains:

> In what generality can one say that there is a unique ideal Bernoulli Voronoi tessellation on a group?

Primary source: https://arxiv.org/abs/2502.11622 (v2, 27 Mar 2026), Section 6 / Question 2.

I also rechecked the current primary follow-up literature:

1. Matteo D'Achille and Ali Khezeli, *Convergence towards Ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs*, arXiv:2606.30517v2 (20 Jul 2026). Their Theorem 1.3 gives the vertex-graph phase family, Theorem 1.4 gives the continuous edge-measured delay family, Theorem 1.5 proves edge-measured phase independence under a diagonal boundary hypothesis, and Corollary 1.6 explicitly includes `T(p) x T(p)`.
2. D'Achille--Grebík--Khezeli--Recke--Wilkens, arXiv:2511.23317. Their Section 4.4 uses **one iid Uniform[0,1] label per nucleus** to resolve all ties globally. Theorem 25 identifies subsequential Bernoulli partition limits with the corresponding ideal labelled Poisson partition; Claim 37 supplies the Poisson/Bernoulli correspondence for that global-label rule.

Dated bounded searches included:

- `"pointwise" Voronoi "T(p) x T(p)" phase tie-breaking`;
- `"each point" "picks one at random" Bernoulli Voronoi product trees`;
- `"random tie" "product of regular trees" Voronoi low intensity`;
- `phase Bernoulli Voronoi product regular trees tie`;
- author/current-arXiv queries around 2502.11622, 2511.23317, and 2606.30517.

I found no paper stating the pointwise-random tie theorem below. This is bounded negative evidence only; novelty remains **UNVERIFIED**.

## 3. Moves #12 and #25: the old global-nucleus-label result is a direct KNOWN corollary

The preceding stuck report isolated the exact bridge

\[
\mathcal L(P^{\rm vertex,label}_{\xi})
\stackrel{?}=\mathcal L(P^{\rm edge}_{\xi-1}|_G),
\qquad G=T(p)\times T(p).
\]

The bridge is exact.

D'Achille--Khezeli Theorem 1.3 gives, for the vertex-measured graph, independent boundary nuclei with law `nu_0` and integer delays whose intensity on level `m` is

\[
(p-1)p^{m-1+\xi}.
\]

Adjoin the global iid nucleus label `U in [0,1)` used by DGKRW. Map

\[
(\theta,m,U)\longmapsto (\theta,\delta=m+U).
\]

On the slab `[m,m+1)`, the pushed-forward intensity is

\[
\nu_0(d\theta)(p-1)p^{m-1+\xi}\,d\delta,
\]

which is exactly the edge-measured delay intensity of D'Achille--Khezeli Theorem 1.4 with phase `xi-1`. For `T(p) x T(p)`, their proof of Corollary 1.6 identifies the edge boundary limit with the diagonal push-forward of the same vertex boundary law, so the boundary component also matches.

Finally, every graph horofunction `h_theta(v)` is integer-valued. Therefore the global-label vertex rule

\[
\text{minimize }(h_\theta(v)+m,U)\text{ lexicographically}
\]

is pathwise identical to the edge-delay rule

\[
\text{minimize }h_\theta(v)+m+U.
\]

Thus

\[
\boxed{P^{\rm vertex,label}_{\xi}=P^{\rm edge}_{\xi-1}|_G\quad\text{pathwise under the natural coupling}.}
\tag{3.1}
\]

Corollary 1.6 says the right-hand side is independent of phase on `T(p) x T(p)`, while DGKRW Theorem 25/Claim 37 is exactly the Bernoulli handoff for the global-nucleus-label refinement. Hence the frozen R06 theorem on `F_2 x F_2 = T_4 x T_4` is not a new theorem:

\[
\boxed{\text{GLOBAL IID NUCLEUS-LABEL FROZEN SCOPE: KNOWN / DIRECT PUBLISHED COROLLARY.}}
\]

This is a status correction, not metric movement. The earlier R05 mathematical audit remains useful as a correctness check, but novelty is now resolved negatively for this frozen scope. No P26 audit is needed to call published prior art KNOWN; it would only have been required for a new closure claim.

**Outcome #12 / #25:** success. The conserved object is the slab mass under `delta=m+U`; counting the same slab in the vertex-labelled and edge-measured descriptions gives the exact one-unit phase shift.

## 4. Move #30: freeze one genuinely different source refinement

The source explicitly allows each boundary point to choose one tied nucleus at random. Freeze the following equivariant refinement on a Cayley graph. For every evaluation vertex `v` and every potential nucleus `x`, sample iid `U_{v,x} ~ Uniform[0,1]`, jointly equivariantly under left translation. Among all nearest occupied nuclei at `v`, choose the one minimizing `U_{v,x}`.

Call this the **pointwise-independent tie refinement**. Conditional on any finite tie set at `v`, its winner is uniform; choices at two distinct boundary vertices use independent tie marks. This is different from the DGKRW rule, where one global label `U_x` is attached to a nucleus and reused at every tied vertex.

I attacked the smallest possible cylinder on

\[
G=T_4\times T_4 \cong \operatorname{Cay}(F_2\times F_2)
\]

with the `l^1` product graph metric: one edge `o~w`, with `w` in the first tree factor.

### Theorem I0079-R06-T5 — phase nonuniqueness for pointwise-independent ties

For the pointwise-independent tie refinement above, the low-intensity Bernoulli Voronoi IRE on `F_2 x F_2` is **not unique**. In fact there are two explicit intensity subsequences along which the cylinder probability

\[
E:=\{o\sim_{\rm Vor} w\}
\]

has different limits.

This does **not** refute the source's open-ended Question 2; it supplies a negative example to any refinement-independent/unrestricted uniqueness claim and shows that the refinement convention matters already on `F_2 x F_2`.

### 4.1 Phase process

Write `q=3`. For a phase prefactor `a>0`, the ideal boundary process has independent levels `m in Z` with total intensity

\[
\lambda_m=a3^m
\]

and boundary direction `psi=(psi_1,psi_2)` distributed according to product harmonic measure. For the neighbor `w` in the first tree factor, let

\[
A=\{\psi_1:\text{the ray from }o\text{ starts through }w\}.
\]

Harmonic measure gives `r:=P(A)=1/4`. Also

\[
h_\psi(w)=\begin{cases}-1,&\psi\in A,\\+1,&\psi\notin A.\end{cases}
\]

At level `m`, let `A_m` and `B_m` count nuclei of the two types. Then independently

\[
A_m\sim\mathrm{Pois}(\lambda_m/4),\qquad
B_m\sim\mathrm{Pois}(3\lambda_m/4).
\]

Let `M` be the smallest occupied level. Since

\[
\sum_{j<m}\lambda_j=\lambda_m/2,
\]

the probability that all earlier levels are empty is `exp(-lambda_m/2)`.

### 4.2 Exact two-point cylinder formula

At the root, all nuclei at level `M` tie and the pointwise mark selects one uniformly.

If `A_M>0`, then at `w` the unique lowest score level is attained by exactly the `A_M` nuclei. Conditional on `(A_M,B_M)`, the probability that root and neighbor select the same nucleus is

\[
\frac1{A_M+B_M}.
\]

If `A_M=0`, then necessarily `B_M>0`. If `A_{M+1}>0`, `w` selects at the lower score `M` and agreement is impossible. If also `A_{M+1}=0`, then the lowest candidates at `w` are `B_M union A_{M+2}`, and the conditional agreement probability is

\[
\frac1{B_M+A_{M+2}}.
\]

Define, for `N~Pois(x)`,

\[
H(x):=\mathbb E\!\left[\frac{1-(3/4)^N}{N};N\ge1\right]
=e^{-x}\sum_{n\ge1}\frac{x^n}{n!}\frac{1-(3/4)^n}{n}.
\]

Given `A_M+B_M=N`, the chance `A_M>0` is `1-(3/4)^N`, so the first case contributes `H(lambda)`. In the second case,

\[
P(A_M=A_{M+1}=0)=e^{-\lambda}
\]

because `(lambda/4)+(3lambda/4)=lambda`. Also

\[
B_M+A_{M+2}\sim\mathrm{Pois}(3\lambda),
\]

and conditional on its total, `B_M` occupies each point with probability `1/4`; hence the second reciprocal expectation is `H(3lambda)`.

Therefore the exact cylinder probability is

\[
\boxed{
F(a):=P_a(E)=\sum_{m\in\mathbb Z}e^{-\lambda_m/2}
\left(H(\lambda_m)+e^{-\lambda_m}H(3\lambda_m)\right),
\quad\lambda_m=a3^m.
}
\tag{4.1}
\]

As a consistency check, `F(3a)=F(a)` by shifting the summation index.

### 4.3 Two actual Bernoulli subsequences

D'Achille--Khezeli Theorem 1.3 / the product-tree specialization realizes every phase `xi` by intensities asymptotic to

\[
p_n=3^\xi/F_G(n),
\]

where `F_G(n)=|B_n(o)|`. Its vertex boundary level coefficient for `T_4 x T_4` is

\[
a=2\,3^{-1+\xi}.
\]

Choose phases implicitly by

\[
3^{\xi_1}=\frac{81}{200},\qquad
3^{\xi_2}=\frac{141}{200}.
\]

Then

\[
a_1=\frac{27}{100},\qquad a_2=\frac{47}{100}.
\]

Take Bernoulli nucleus probabilities `p_n^{(i)}=3^{xi_i}/F_G(n)`. For any fixed finite cylinder, the marked Bernoulli point process converges directly to the marked Poisson boundary process: for a compactly supported nonnegative test function `f`, its Laplace functional is a product of factors `1-p_n+p_n E[e^{-f}]`; taking logarithms, the linear term converges by the boundary intensity convergence while the quadratic remainder is `O(p_n)` because the rescaled counting mass of the relevant compact set stays bounded. Adding finitely many iid pointwise tie-mark coordinates does not change this argument. The winner map on `{o,w}` is a.s. continuous because the relevant candidate sets are finite and all tie marks are continuous. Thus (4.1) is the actual limit of the Bernoulli cylinder along the two displayed subsequences.

This avoids incorrectly using DGKRW Claim 37: that claim is tailored to **global nucleus labels**, whereas pointwise marks do not collapse Poisson multiplicities in the same way.

### 4.4 Exact rational certificate of phase separation

Only after deriving (4.1) did I build a checker. It uses `fractions.Fraction` for every proof-relevant arithmetic operation. It bounds exponentials by positive Taylor sums with an exact geometric remainder; bounds the positive series defining `H`; and bounds both infinite `m`-tails analytically:

- for the negative tail, `H(x)<=x/4`, hence `g(lambda)<=lambda`;
- for the positive tail, `H<=1` and `3^j>=1+2j` give an exact geometric exponential tail bound.

The checker certifies

\[
\begin{aligned}
F(27/100)&\in[0.457148657413679714,\ 0.457148911440002502],\\
F(47/100)&\in[0.456845192076364831,\ 0.456845634270324273].
\end{aligned}
\]

The intervals are disjoint, with certified gap at least

\[
\boxed{0.000303023143355440.}
\]

Therefore the two subsequential Bernoulli IRE limits differ on the radius-one cylinder `E`, proving T5.

Artifacts:

- `artifacts/R06/20260917T0117Z_i0079_pointwise_phase_exact.py`
- `artifacts/R06/20260917T0117Z_i0079_pointwise_phase_exact.out.txt`

The archived output ends `EXACT_RATIONAL_INTERVALS_DISJOINT` and `PASS`.

**Outcome #30: success.** One edge already detects the phase once tie randomness is refreshed pointwise instead of attached globally to nuclei.

## 5. Interpretation and honest source status

This run separates two natural equivariant boundary refinements on the *same* group and metric:

1. **Global iid nucleus labels:** phase independent; now classified **KNOWN** by the exact vertex-labelled/edge-measured bridge plus D'Achille--Khezeli Corollary 1.6 and DGKRW Theorem 25.
2. **Pointwise-independent random tie resolution:** phase dependent by T5, hence **NONUNIQUE / PROVED / AUDIT-PENDING** on `F_2 x F_2`.

The source itself says there are multiple ways to resolve boundaries and simply fixes one. Consequently no refinement-independent statement should be attributed to Question 2 without specifying the convention. T5 is a genuine source-relevant warning/result, but the full Question 2 remains **PARTIAL** rather than `REFUTED`: it asks for the generality in which uniqueness can be asserted, not for a universal yes/no conjecture.

The next mathematical obligation is to determine whether pointwise-tie nonuniqueness persists on the single regular tree (where Bhupatiraju's known uniqueness result may encode a particular refinement), or whether products are the first place the two refinement conventions diverge. That comparison is likely more informative than adding another product example.

## 6. Independent audit of newest R07 package

Newest package read: `runs/R07/20260917T0024Z_i0077_nonsyndetic_density_pulses_08.md`, theorem `I0077-R07-T9`.

**Audit ID:** `R06-AUDIT-R07-I0077-T9-20260917T0117Z`  
**Verdict:** `PASS_SCOPED / NOVELTY_UNVERIFIED`.

Scoped statement audited: the new step replacing the previous bounded-gap pulse hypothesis by positive lower asymptotic pulse density, conditional on the two OU/continuum-terminal compilers already proved in R07's preceding package chain.

Checks:

- From lower density `A(m)/m ->liminf p>0`, the count of complete pulse intervals in `[r_n,s_n]` with `r_n=log R_n=o(log n)=o(s_n)` satisfies `N_A(r_n,s_n)/(s_n-r_n)>=p-2eps` eventually. The subtraction of at most `ceil(r_n)` early integer starts is sufficient; no bounded-gap assumption is hidden here.
- Pulse intervals `[k,k+tau]`, `tau<1`, are disjoint. Each supplies the inherited killed-OU `L^2(gamma)` contraction `exp(-lambda_* tau)`; nonpulse evolution is an `L^2` contraction. Their product therefore gives survival exponent `(p-2eps)tau lambda_*`.
- Since `p tau lambda_*>1`, epsilon can be chosen so that `kappa>1`; with `R_n=O(log n)`, the inherited continuum-terminal modulus/Borel--Cantelli compiler is summable.
- The FBM witness-time transfer uses no independence between a witness time and the Brownian witness path; it is the same deterministic identity already used in the earlier package.
- The explicit static rate `lambda_* = pi^2 e^{-M^2/2}/(2d^2)` is consistent with the weighted Dirichlet Rayleigh quotient plus the interval Poincare inequality.

I found no mathematical failure in the new T9 density step. This audit does not re-audit all predecessor compilers or novelty.

## 7. Model/runtime escalation

The model-control limitation remains real. The available task-control surface exposes prompt/title, schedule, timing mode and enabled state, but no model-family field, no reasoning-effort field, and no authenticated runtime-model telemetry. GPT-6 / maximum is therefore a prompt request, not an enforceable or verified runtime setting here.

To change that for real requires product/API support for task-level model and reasoning fields or an authorized owner/admin/platform-support context capable of setting those backend fields. A `You cannot modify this task` response (as previously seen for one P26 task ID from one context) is an ownership/context permission boundary. The legitimate workaround is the owning authorized task-control context or platform support, not task duplication or bypass. No scheduler mutation was attempted in this run.

## 8. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  active_source: I0079
  source: "Jardon-Sanchez--Mellick--Poulin--Wrobel, PLMS 2026, Question 2"
  predecessor_preserved: "I0056 / Lyons--Peres Q6.20; rotated after six unchanged runs; full source PARTIAL"
  fixed_metric: R_unique
  metric_before: +infinity
  metric_after: +infinity
  unchanged_count_before: 3
  unchanged_count_after: 4
  tried_moves: [12, 25, 30]
  frozen_global_label_scope:
    graph: "F_2 x F_2 = T_4 x T_4"
    status_before: "PROVED / AUDIT-GATED / knownness pending"
    status_after: "KNOWN / direct corollary after exact model bridge"
    evidence:
      - "D'Achille--Khezeli arXiv:2606.30517v2, Theorems 1.3--1.5 and Corollary 1.6"
      - "DGKRW arXiv:2511.23317, Theorem 25 and Claim 37"
  new_pointwise_refinement:
    status: "PARTIAL source result; NONUNIQUE on frozen group; theorem PROVED / AUDIT-PENDING"
    theorem_id: "I0079-R06-T5"
    cylinder: "E={o and first-factor neighbor w belong to same Voronoi cell}"
    phase_a1: "27/100"
    phase_a2: "47/100"
    probability_interval_a1: "[0.457148657413679714, 0.457148911440002502]"
    probability_interval_a2: "[0.456845192076364831, 0.456845634270324273]"
    certified_gap: ">= 0.000303023143355440"
    exact_evidence:
      - "artifacts/R06/20260917T0117Z_i0079_pointwise_phase_exact.py"
      - "artifacts/R06/20260917T0117Z_i0079_pointwise_phase_exact.out.txt"
  full_source_status: PARTIAL
  novelty: UNVERIFIED
  audits:
    - "R05-AUDIT-R06-I0079-PHASE-CANCELLATION-01-20260916T221717Z: PASS_CORE_MATH / SOURCE-HANDOFF_SCOPED / NOVELTY_UNVERIFIED (old global-label core)"
    - "P26-AUDIT-R06-I0079: NOT_FOUND"
    - "R06-AUDIT-R07-I0077-T9-20260917T0117Z: PASS_SCOPED / NOVELTY_UNVERIFIED"
  remaining_obligation: "Independent audits of T5; then compare the pointwise refinement on a single regular tree versus the product-tree obstruction. Full Q2 remains open-ended."
  next_methods: [4, 14, 26]
```

No shared root ledger was edited; P26 remains the shared-ledger writer.
