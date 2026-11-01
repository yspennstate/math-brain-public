Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated model selector or reasoning-effort selector, so I do not claim otherwise. **NO METRIC MOVEMENT: `6.48139658710 -> 6.48139658710`; unchanged count `0 -> 1`. Section-B moves: #2 ATTACK THE NEGATION FIRST, #19 MAKE IT AN ALGORITHM, #8 GO THE OTHER WAY AND DISCRETIZE.**

Problem/source: Elizabeth Gardner (1988), *The space of interactions in neural network models*, J. Phys. A 21, 257–270, DOI `10.1088/0305-4470/21/1/030`; modern source navigation through Stojnic arXiv:1306.3980, El Alaoui–Sellke arXiv:2010.15811, Montanari–Zhong–Zhou arXiv:2110.15824 / PTRF 188 (2024), and Stojnic arXiv:2312.16531. Frozen target: rigorous SAT/UNSAT threshold bracket at `kappa=-1` for the iid standard-Gaussian spherical model.

Status: **PARTIAL / source problem OPEN**. The bracket does not move this run. The substantive result is a rigorous route obstruction: the Montanari–Zhong–Zhou weighted second-moment lower bound `delta_lb(-1)` is forced below `3.714`, hence is strictly weaker at `kappa=-1` than their already-imported LP lower bound `delta_lin(-1)=1/Phi(-1)>4` (in fact `6.302974...`). This analytically eliminates a lower-side route before any global overlap numerics are attempted.

# 1. Repository continuity, exclusions, and access limits

Before new mathematics I reread/rechecked on current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own report `runs/R14/2026-09-16T19-54-46Z_r14-c185-mzz-linear-lower.md`;
- newest visible R15 package `runs/R15/20260916_1952Z_i0076_alternating_dual_candidate_a16.md`;
- current R14/R15 ownership and the Ising-perceptron exclusion.

The large intake JSONL corpus cannot be literally rendered row-by-row through the connector without truncation; this run therefore records that part of the requested whole-corpus read as **ACCESS-LIMITED / INCOMPLETE**, not as completed. Bounded repository searches did not reveal a conflicting R14 owner or a newer R14 report.

Recovered canonical R14 state before this run:

- rigorous SAT endpoint `alpha_L = 630297437506/10^11 = 6.30297437506` from C185, by MZZ Theorem 4.3 and exact normalization matching;
- rigorous UNSAT endpoint `alpha_U = 1278437096216/10^11 = 12.78437096216` from C184;
- bracket width `64813965871/10^10 = 6.48139658710`;
- C182/C183 already exhaust the corrected one-parameter 2013 partial-lift upper-bound family at `12.78437096209 < alpha_PL^* < 12.78437096216`.

# 2. Current primary-source scope — dated 2026-09-16

Gardner's 1988 paper is the historical neural-network locator; the publisher abstract explicitly says the order parameters at the saddle point are assumed replica symmetric. It is not a rigorous negative-margin capacity theorem.

El Alaoui–Sellke arXiv:2010.15811 study exactly the Gaussian spherical set

`{sigma: ||sigma||^2=N, <g_a,sigma> >= kappa sqrt(N) for all a}`

and identify the negative-margin FRSB geometry and capacity through a Parisi variational principle only conjecturally. Their algorithm outputs a feasible point at radius `sqrt(qbar N)` with `qbar<1`, not a target-sphere sample.

Stojnic arXiv:2312.16531 states a fully lifted RDT characterization, but also states that practical operation requires substantial numerical work and presents concrete capacities through stationarized finite-level numerical evaluation. Its 2-sfl table gives approximately `12.32` at `kappa=-1`; this remains numerical in R14, not a bracket endpoint.

Huang–Sellke–Sun arXiv:2608.29416 (submitted 2026-08-29) gives exact **algorithmic** thresholds for high-dimensional projection pursuit for general bounded continuous activations and explicitly says unrestricted non-algorithmic feasible projections remain a major outstanding challenge. This is not an unrestricted SAT threshold theorem.

No bounded primary-source search this run found a later theorem rigorously closing the unrestricted full-radius threshold at `kappa=-1` or all `kappa<0`. This is a dated bounded-search statement, not a worldwide novelty proof.

# 3. Move #2 — ATTACK THE NEGATION FIRST: can MZZ's weighted second moment beat C185 at kappa=-1?

The answer is **no**, for a local-curvature reason that does not require solving MZZ's global overlap minimization.

MZZ Definition 1 (their equations (14)–(15)) fixes, for `kappa<0`, the unique positive `c_*=c_*(kappa)` satisfying

`c_* (1-Phi(kappa+c_*)) = phi(kappa+c_*)`,

and for correlated standard Gaussians `(G_1,G_2)` with correlation `q` defines

`Psi(q) = -log E_q[ exp(-c_*(G_1+G_2)) 1{G_1>=kappa,G_2>=kappa} ]
          -(1/(2 delta)) log(1-q^2)`.

Their second-moment lower endpoint `delta_lb(kappa)` is the supremum of `delta>0` for which `Psi` is uniquely minimized at zero **and** `Psi''(0)>0`.

## R14-C187 — exact curvature ceiling for the MZZ second-moment bound

**STATUS: PROVED.** For every fixed `kappa<0`,

`delta_lb(kappa) <= 1/(kappa^2 c_*(kappa)^2)`.

### Proof

Put

`f(x)=exp(-c_* x) 1{x>=kappa}`

and let `He_j` denote the probabilists' Hermite polynomial. Since `f` is square-integrable with all polynomial moments, Mehler's expansion is valid:

`e(q):=E_q[f(G_1)f(G_2)]
     = sum_{j>=0} (m_j^2/j!) q^j`,

where

`m_j=E[f(G) He_j(G)]`.

Hence

`e(0)=m_0^2`, `e'(0)=m_1^2`, `e''(0)=m_2^2`.

Write `c=c_*`, `a=kappa+c`, `Q=1-Phi(a)`. Completing the square,

`exp(-cx) phi(x)=exp(c^2/2) phi(x+c)`.

Therefore

`m_0 = exp(c^2/2) Q`,

and

`m_1 = exp(c^2/2)[phi(a)-cQ]=0`

by the defining equation for `c_*`.

For `He_2(x)=x^2-1`, use

`int_a^infty y phi(y)dy=phi(a)`,

`int_a^infty y^2 phi(y)dy=Q+a phi(a)`.

After the change of variables `y=x+c`,

`m_2
 = exp(c^2/2)[c^2 Q+(a-2c)phi(a)]
 = exp(c^2/2)Q[c^2+c(kappa-c)]
 = kappa c m_0`.

Thus `e'(0)=0` and

`e''(0)/e(0)=kappa^2 c^2`.

Since

`Psi(q)=-log e(q)-(1/(2delta))log(1-q^2)`,

we obtain exactly

`Psi''(0)=1/delta-kappa^2 c_*^2`.

MZZ's Definition 1 requires `Psi''(0)>0`, hence every `delta` in the defining admissible set satisfies

`delta < 1/(kappa^2 c_*^2)`.

Taking the supremum proves C187. □

This is a necessary local condition only; it does not replace MZZ's global requirement that zero be the unique minimizer. That is precisely why it is useful as a route obstruction.

# 4. R14-X41 — at kappa=-1 the MZZ second-moment route is strictly dominated by their LP route

**STATUS: PROVED.** At `kappa=-1`, the defining equation becomes

`c_* Phi(1-c_*) = phi(1-c_*)`.

MZZ Lemma 1(a) proves uniqueness of the positive root. The exact rational checker in this run certifies

`F(0.5189)<0<F(0.5190)`,

where

`F(c)=c Phi(1-c)-phi(1-c)`.

Therefore

`0.5189<c_*<0.5190`.

C187 then gives

`delta_lb(-1) <= 1/c_*^2 < 1/(0.5189)^2 < 3.714`.

The same exact checker proves

`Phi(-1)<1/4`.

MZZ Theorem 4.3 has the LP threshold

`delta_lin(kappa)=1/Phi(kappa)`,

so

`delta_lin(-1)>4`.

Consequently

**(X41)**

`delta_lb(-1) < 3.714 < 4 < delta_lin(-1)`.

Thus MZZ Theorem 4.1's weighted second-moment lower bound cannot improve C185 at `kappa=-1`, even before checking its global overlap condition. This rigorously explains, at this frozen margin, the qualitative source observation that the second-moment bound is inferior to LP for smaller `|kappa|`.

The executed checker uses exact `fractions.Fraction` arithmetic, a Machin-series enclosure of `pi`, and alternating rational Taylor bounds for the Gaussian integrals. Its archived output ends `ALL_EXACT_CHECKS_PASS`.

# 5. Move #19 — MAKE IT AN ALGORITHM: test the 2026 exact algorithmic-threshold theory

I checked whether Huang–Sellke–Sun's 2026 exact projection-pursuit threshold could immediately replace MZZ's LP lower endpoint.

It cannot be imported as stated. Their theorem gives exact algorithmic thresholds for Hamiltonians with **bounded continuous activation**. Exact hard-margin satisfiability is the simultaneous condition

`min_a <g_a,x>/sqrt(N) >= kappa`,

whose zero-violation indicator is discontinuous. A continuous bounded penalty can certify a small empirical violation mass, but that alone does not yield **zero** violating constraints at finite `N`, and therefore does not supply a full-radius SAT witness for R14 without an additional repair theorem or a uniform positive margin buffer.

No such repair theorem was verified in this run. Hence the HSS result remains a promising algorithmic framework, not a rigorous new R14 endpoint.

Concrete next question from this route: prove a smoothing/repair lemma converting an algorithmically attainable empirical law with a strict gap below `kappa` into an exact all-constraints solution while preserving unit norm. Without that extra step, importing the algorithmic Hamiltonian threshold would conflate approximate optimization with satisfiability.

# 6. Move #8 — DISCRETIZE: attempt to turn the 2-sfl numerical table into a finite interval certificate

I re-read the r=2 full-lifting source formula rather than using its table as a theorem.

Stojnic 2023 Theorem 2 assumes the complete sfl-RDT setup and requires the non-fixed lifting parameters `(p_2,q_2,c_2,gamma_sq,gamma_sq^(p))` to solve the full stationarity system before the equality formula is invoked. The source then says the theorem becomes operational through numerical evaluation. At `kappa=-1`, Table 2 reports approximately

`gamma_sq=0.1500`, `gamma_sq^(p)=1.6660`, `p_2=0.6649`, `q_2=0.2780`, `c_2=3.7194`, `alpha=12.32`.

The modulo-m theorem later gives a one-sided inequality but still uses stationarized parameters, and the source discusses tightness through numerical evaluation. Therefore a box around the displayed decimal parameters is not by itself a rigorous UNSAT certificate.

The exact finite obligation is now clear: derive a source-faithful sufficient one-sided r=2 full-lift inequality; compactify its parameter domain; use interval Newton/Krawczyk to prove existence and uniqueness (or at least a validated admissible stationary box) for the nested Gaussian-expectation system; then evaluate the correct comparison direction on that entire box. Until this is done, `12.32` remains numerical and is excluded from the bracket.

This discretization route did not move the metric this run, but it identifies the finite validated-numerics target that could materially lower `alpha_U`.

# 7. Independent R15 audit

Newest package read:

`runs/R15/20260916_1952Z_i0076_alternating_dual_candidate_a16.md`.

I independently audited its Lemma A16.2 and record

`R14-AUDIT-R15-I0076-A16.2-06 = PASS`.

Let `Q` be the law of Brownian motion from zero stopped at its first exit from `(-1,1)`, retaining the whole stopped path. Let `check Q` be time reversal followed by recentering at the exit endpoint.

If the original path exits at `+1` at time `tau`, then for every `0<t<tau`, `B_{tau-t}<1`; hence the reversed/recentered path

`Y_t=B_{tau-t}-B_tau`

is strictly negative for all `0<t<tau` and ends at `-1`. If the original path exits at `-1`, the reversed/recentered path is strictly positive and ends at `+1`. Thus under `check Q` the event

`A = {the stopped path has one fixed sign on every positive time before its endpoint}`

has probability one.

Under `Q`, standard Brownian motion started from zero visits both positive and negative values arbitrarily close to time zero almost surely (equivalently by the Brownian LIL / regularity of both half-lines at zero). Hence `Q(A)=0`.

Therefore `Q` and `check Q` are mutually singular. The R15 lemma is correct. This audit covers A16.2 only; it does not audit the alternating construction as a whole and does not close Burdzy–Scheutzow Problem 7.2.

# 8. Metric and ledger

No bracket endpoint moves this run:

`alpha_L = 630297437506/10^11 = 6.30297437506`,

`alpha_U = 1278437096216/10^11 = 12.78437096216`,

`alpha_U-alpha_L = 64813965871/10^10 = 6.48139658710`.

This is **one unchanged run after the large C185 movement**, not a stuck episode.

```yaml
ledger_delta:
  worker: "R14 HARD OUTSIDE"
  source:
    original: "Gardner 1988, The space of interactions in neural network models, DOI 10.1088/0305-4470/21/1/030"
    navigation:
      - "arXiv:1306.3980"
      - "arXiv:2010.15811"
      - "arXiv:2110.15824 / PTRF 188 (2024)"
      - "arXiv:2312.16531"
      - "arXiv:2608.29416"
  target: "negative-margin spherical Gaussian perceptron capacity at kappa=-1"
  metric: "rigorously certified whp threshold-bracket width alpha_U-alpha_L"
  before:
    alpha_L: "630297437506/10^11 = 6.30297437506"
    alpha_U: "1278437096216/10^11 = 12.78437096216"
    width: "64813965871/10^10 = 6.48139658710"
  after:
    alpha_L: "630297437506/10^11 = 6.30297437506"
    alpha_U: "1278437096216/10^11 = 12.78437096216"
    width: "64813965871/10^10 = 6.48139658710"
  status: "PARTIAL"
  metric_movement: "NO MOVEMENT"
  unchanged_count_before: 0
  unchanged_count_after: 1
  methods: [2, 19, 8]
  exact_evidence:
    - "R14-C187: delta_lb(kappa) <= 1/(kappa^2 c_*(kappa)^2)"
    - "R14-X41: at kappa=-1, delta_lb<3.714<4<delta_lin"
    - "artifacts/R14/2026-09-16T20-53-04Z_r14-c187-mzz-curvature_checker.py"
    - "artifacts/R14/2026-09-16T20-53-04Z_r14-c187-mzz-curvature_checker_output.txt"
    - "checker-output SHA256 9ee37f8b448653e4117655f421c1b0157f80324bf937a2086473c16d68031cb6"
  audit_ids:
    - "R14-AUDIT-R15-I0076-A16.2-06=PASS"
  remaining_obligation: "materially improve alpha_U via a rigorously validated 2-sfl sufficient UNSAT certificate, or produce an exact smoothing/repair theorem that lets a stronger 2026 algorithmic threshold imply hard satisfiability"
```

# 9. Artifacts and limitations

Checker:

`artifacts/R14/2026-09-16T20-53-04Z_r14-c187-mzz-curvature_checker.py`.

Corrected archived output:

`artifacts/R14/2026-09-16T20-53-04Z_r14-c187-mzz-curvature_checker_output.txt`.

Output SHA-256:

`9ee37f8b448653e4117655f421c1b0157f80324bf937a2086473c16d68031cb6`.

An earlier same-run output path ending `_checker.out` contains the same numerical calculation but retained an obsolete `C186` label in its first line. It is preserved immutably and is **not** the canonical output referenced above; no mathematical value differs.

# 10. Next attack

Do not spend the next run globally optimizing MZZ `delta_lb(-1)`: C187/X41 prove that route cannot beat the existing LP lower endpoint.

The next materially capable attacks are:

1. **Upper side:** rigorously instantiate the r=2 full-lift/Stojnic 2023 sufficient comparison at a conservative density such as `12.5` or `12.4`, with interval-certified nested Gaussian expectations and correct optimization direction. A successful `12.5` certificate would move the fixed metric by about `0.284` immediately.
2. **Algorithmic lower side:** investigate whether the HSS 2026 stochastic-control optimum can be combined with a strict-margin smoothing/repair lemma; do not equate bounded-continuous Hamiltonian optimization with zero violations without that proof.
3. **Polytope side:** search post-MZZ Gaussian random-polytope inradius/covering results specifically at constant aspect ratio near `alpha=6–13`; generic asymptotic inradius bounds are not enough.

The exact all-negative-margin threshold and rigorous full-RSB identification remain OPEN.
