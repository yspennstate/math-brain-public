Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **No movement in the frozen source metric: `T_corr=0 -> 0`. Methods tried: B3, B7, B19. New rigorous progress: the previous `p<1` moment theorem extends uniformly to the full interior `vartheta_x` family, and the reciprocal-edge heuristic is upgraded to a positive-density exact tail-eigenvalue theorem for the tail-scale exceedance skeleton, with asymptotic coefficient `K_1(vartheta_x)=(x(1-x))^(1/4)`. The sole remaining source-level gap is nonnormal stability under reattaching the sub-threshold background.**

# HARD7-02 — Campbell–O'Rourke Question 1.9: uniform subcritical moments and an exact exceedance-skeleton tail law

Status: **PARTIAL / source Question 1.9 remains OPEN by bounded current-status search.**

Frozen metric: `T_corr=0 -> 0` (**no movement**). The preceding Q1.9 ordinary run was the first unchanged run after admission; this is the second, so the Q1.9 unchanged streak is now `2`. Section I is not yet triggered. If the next run also leaves `T_corr` unchanged, it must execute the Section-I stuck protocol rather than file another ordinary lemma.

## 1. Continuity, repository read, ownership, and capability honesty

I resumed the active exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

and the latest HARD7-02 checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T15-09-49Z__q19-subcritical-moments-reciprocal-order-parameter.md`

rather than restarting the released Question 1.8 target.

At run start I re-read the controlling HARD7 file, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the active Q1.9 claim, the newest own report, repository search results in the heavy-tail/intake neighborhood, and the newest neighboring heavy-tail terminal handoff

`research7_2026-09-17/R7-06/handoffs/2026-09-19T095800Z__C0032_terminal_handoff.md`.

That neighboring target is the distinct iid heavy-tailed circular-law density problem and is explicitly in terminal handoff. Q1.9 remains separately owned by HARD7-02. Repository searches again found no equivalent active claim under an alias, and no claim file was modified in this run.

The scheduler capability statement is still unchanged. The exposed automation surface provides task title, prompt, schedule/timing mode and enabled state; it exposes no binding model selector, no reasoning-effort selector, no authenticated effort telemetry and no guaranteed run duration. Thus `GPT-6 / maximum` remains a text request only and cannot be enforced or verified here. A real change requires a product/backend surface that exposes binding model/effort controls or an authorized workspace/account context in which those controls are available. Historical repository records show that P26/P01/P03 modification probes once returned `You cannot modify this task`; later evidence says P26 became editable in a different authorized context. The compliant workaround for a task that still refuses modification is to use the owning/authorized account or workspace context, or platform support/ownership transfer. It is **not** to create a duplicate schedule or bypass permissions. No scheduler mutation was attempted.

No email, Drive, public posting, paid compute, workflow execution, force push, neighboring-track edit, or shared-root ledger write was performed.

## 2. Exact source statement and fresh status check

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Section 1.3 asks exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The source's Theorem 1.6 gives the deterministic limiting ESD `mu_{alpha,theta_d}` under its C1/C2 heavy-tail hypotheses and emphasizes that the limit depends on the dependence measure `theta_d`. The source itself contrasts the much lighter iid/axis-supported tail with the Hermitian heavy-tail endpoint. Those endpoint facts are literature baselines, not HARD7-02 discoveries.

A fresh bounded 19 September 2026 search used the exact title/authors, `Question 1.9`, `theta_d`, `mu_{alpha,theta_d}`, `tail behavior`, `heavy-tailed elliptic`, `PWIT`, and 2023--2026 follow-up terms. It recovered the 2022 source, Campbell--O'Rourke's *Spectrum of Levy--Khintchine Random Laplacian Matrices* (JTP 2024), Carpenter--O'Rourke's 2025 sparse elliptic paper in a finite-variance/sparsity regime, and unrelated modern non-Hermitian universality papers. I did **not** locate a paper claiming a general solution of Question 1.9 or a tail classification for the frozen `alpha=1`, `vartheta_{1/4}` family. This is bounded negative evidence only, not a worldwide novelty certificate.

Primary source URL: `https://arxiv.org/abs/2010.01261`.

Relevant follow-up checks included:

- Campbell--O'Rourke, *Spectrum of Levy--Khintchine Random Laplacian Matrices*, J. Theor. Probab. 37 (2024), 933--973;
- Carpenter--O'Rourke, *The Limiting Spectral Distribution for Sparse Elliptic Random Matrices*, arXiv:2508.04891 (2025).

Neither is the source's interior heavy-tail tail-classification problem.

## 3. Frozen family, metric, and exact Pareto representative

The active claim studies first

`alpha=1`,

`eta_x = Law(sqrt(x)e^{i phi}, sqrt(1-x)e^{-i phi})`,

`vartheta_x = (eta_x + tau#eta_x)/2`,

where `tau(w_1,w_2)=(w_2,w_1)`, with the canonical concrete point `x=1/4`.

The frozen metric is

`T_corr = number of explicit non-iid, non-Hermitian C2 dependence families for which the full asymptotic radial tail exponent/class of mu_{alpha,theta} is rigorously determined`.

Before: `T_corr=0`.

After: **`T_corr=0`**.

As in the preceding run, use the source-valid representative

- `P(R>r)=r^(-1)` for `r>=1`;
- `phi` uniform on `[0,2pi)`;
- independently choose `(sqrt(x)e^{i phi},sqrt(1-x)e^{-i phi})` or its coordinate swap with probability `1/2`;
- set `(xi_1,xi_2)=R W`;
- diagonal atom zero and normalization `a_n=n`.

For every `0<x<1`, the same support argument as in the preceding report verifies the nondegeneracy condition: if a complex linear form vanishes on the support curve for every `phi`, multiplying by `e^{i phi}` gives a constant plus a nonzero `e^{2i phi}` Fourier mode, so both coefficients must vanish. Thus the representative lies in the source class for every interior `x`.

Write

`kappa_x := (x(1-x))^(1/4)`.

For every angular support point,

`|w_1 w_2| = sqrt(x(1-x))`,

so an isolated reciprocal `2 x 2` block with radial mark `r` has both eigenvalues of modulus `kappa_x r`.

At the frozen point `x=1/4`,

`kappa = kappa_{1/4} = (3/16)^(1/4)=3^(1/4)/2`.

This is exactly the previous local order parameter `K_1(vartheta_{1/4})`.

## 4. B3 — prove something stronger: all `p<1` moments uniformly over the interior family

The preceding run proved all `p<1` moments only at `x=1/4`. The same argument actually yields a uniform family theorem.

### Theorem A — uniform subcritical radial moments

Let

`mu_x := mu_{1,vartheta_x}`, `0<x<1`,

and put

`m_x := (sqrt(x)+sqrt(1-x))/2`,

`C_x := 1+3 sqrt(2) m_x`.

Then for every `0<p<1`,

`int_C |z|^p mu_x(dz) <= 1 + p C_x/(1-p)`.

Since `m_x<=1/sqrt(2)`, this gives the uniform estimate

`sup_{0<x<1} int_C |z|^p mu_x(dz) <= 1 + 4p/(1-p)`.

Consequently, for every fixed interior `x`,

`liminf_{R->infinity} [-log mu_x({|z|>R})]/log R >= 1`.

#### Proof

For one coordinate of the exact Pareto representative, let

`Z=|xi_1|^2`.

The coordinate modulus is `sqrt(x)` or `sqrt(1-x)` with probability `1/2` each. Hence for every `y>=1`,

`P(Z>y)=m_x y^(-1/2)`.                                           (4.1)

For one row of `A_n=X_n/n`, dominate its squared Euclidean norm by

`S_n=n^(-2) sum_{j=1}^n Z_j`

with independent copies `Z_j`. For `t>=1`, split at `Z_j/n^2=t/2`:

`P(S_n>t)`
`<= P(max_j Z_j/n^2>t/2)`
` + P(sum_j (Z_j/n^2)1_{Z_j/n^2<=t/2}>t/2)`.                     (4.2)

By (4.1),

`P(max_j Z_j/n^2>t/2) <= sqrt(2)m_x t^(-1/2)`.                    (4.3)

For `T>=1`,

`E[Z 1_{Z<=T}] <= 1+2m_x sqrt(T)`.                                (4.4)

Taking `T=n^2t/2` in the truncated term of (4.2) and applying Markov gives, for `n>=2`,

`P(truncated term>t/2)`
`<= 2/(nt) + 2sqrt(2)m_x t^(-1/2)`
`<= t^(-1)+2sqrt(2)m_x t^(-1/2)`.                                (4.5)

Therefore

`P(S_n>t) <= C_x t^(-1/2)`, `t>=1`.                              (4.6)

Let `q=p/2<1/2`. Tail integration yields

`E S_n^q <= 1 + p C_x/(1-p)`.                                    (4.7)

The finite-matrix Weyl/Schatten inequalities used in the source give

`sum_k |lambda_k(A_n)|^p <= sum_i ||Row_i(A_n)||_2^p`.

Divide by `n`, take expectations, apply (4.7), then pass to the deterministic weak limit using the bounded continuous truncations `min(|z|^p,M)` and monotone convergence exactly as in the preceding run. This proves the moment bound. Markov and then `p upward 1` give the tail-exponent lower endpoint. Finally,

`m_x=(sqrt(x)+sqrt(1-x))/2 <= 1/sqrt(2)`

by Cauchy--Schwarz, so `C_x<=4`. `QED`

**B3 outcome:** successful. The one-sided tail-exponent lower endpoint `>=1` is not peculiar to `x=1/4`; it holds uniformly throughout this entire interior dependence family. This still does not classify the tail, since stretched-exponential tails also have all such moments.

## 5. B7 — take the limit after isolating the tail-scale exceedance skeleton

The previous run's reciprocal-edge mechanism was local. Here it becomes an exact positive-density spectral statement for a canonical tail-scale skeleton.

For fixed `t>=1`, define the **`t`-exceedance skeleton** `A_n^{>t}(x)` by keeping both directed entries of an unordered pair `e={i,j}` iff its radial mark satisfies

`R_e>tn`,

and setting all other off-diagonal pairs to zero. The retained undirected edge graph is exactly

`G(n,1/(tn))`.                                                    (5.1)

For `s>=t`, let `J_n(s,t)` be the number of unordered pairs `e={i,j}` such that

1. `R_e>sn`, and
2. every other radial mark incident to `i` or `j` is at most `tn`.

Call these **strong-isolated edges**.

### Theorem B — exact strong-isolated edge density

For every fixed `t>=1` and `s>=t`,

`2 J_n(s,t)/n -> e^(-2/t)/s` in `L^2` and hence in probability.   (5.2)

#### Proof

Put

`q_n=1-1/(tn)`.

A fixed candidate edge must exceed `sn`, probability `1/(sn)`, and the `2(n-2)` other edges incident to its endpoints must fail the `tn` threshold. Thus

`p_n:=P(I_e=1)=(sn)^(-1) q_n^(2(n-2))`.                           (5.3)

Hence

`(2/n)E J_n(s,t)`
`= ((n-1)/(sn)) q_n^(2(n-2))`
`-> e^(-2/t)/s`.                                                   (5.4)

It remains to prove concentration.

If two candidate edges overlap in one vertex, their strong-isolated events are mutually exclusive: each event requires the other edge to be below the `tn` threshold while the other event requires it to exceed `sn>=tn`. Their covariance is therefore nonpositive and can be discarded in an upper bound for the variance.

If two candidate edges are vertex-disjoint, the union of the two isolation neighborhoods contains exactly `4n-12` other unordered edges. Thus

`P(I_e=I_f=1)=(sn)^(-2) q_n^(4n-12)`.                             (5.5)

Subtracting `p_n^2` gives the exact covariance

`Cov(I_e,I_f)`
`=(sn)^(-2) q_n^(4n-12)(1-q_n^4)`.                               (5.6)

Since

`1-q_n^4 <= 4/(tn)`,

(5.6) is at most

`4/(t s^2 n^3)`.                                                  (5.7)

There are at most `n^4/8` unordered pairs of disjoint candidate edges. Also

`sum_e Var(I_e) <= binom(n,2)/(sn) <= n/(2s)`.

Therefore, including the factor `2` in the covariance sum and discarding the negative overlapping covariances,

`Var J_n(s,t) <= n/(2s) + n/(t s^2) = O(n)`.                      (5.8)

Consequently

`Var(2J_n/n)=O(1/n)->0`,

and (5.2) follows from (5.4). `QED`

### Corollary B.1 — positive density of exact tail eigenvalues in the skeleton

Every strong-isolated edge is an actual isolated connected component of the skeleton graph. After permuting coordinates, it is therefore an exact `2 x 2` diagonal block

`[[0,(R_e/n)w_1],[(R_e/n)w_2,0]]`.

Its two eigenvalues satisfy

`|lambda|=(R_e/n)|w_1w_2|^(1/2)=kappa_x R_e/n > kappa_x s`.

Thus the empirical spectral measure `nu_{n,t,x}` of `A_n^{>t}(x)` satisfies the deterministic finite-`n` inequality

`nu_{n,t,x}({|z|>kappa_x s}) >= 2J_n(s,t)/n`.                     (5.9)

Combining (5.2) and (5.9), for every `epsilon>0`,

`P( nu_{n,t,x}(|z|>kappa_x s) < e^(-2/t)/s - epsilon ) -> 0`.    (5.10)

In particular, setting `s=t`, the skeleton has the tail-scale lower bound

`nu_{n,t,x}(|z|>kappa_x t) >= e^(-2/t)/t - o_P(1)`.              (5.11)

If `R=kappa_x t`, the right side is

`kappa_x e^(-2/t)/R`.

As `t->infinity`, the coefficient tends to `kappa_x`, exactly matching

`K_1(vartheta_x)=int |w_1w_2|^(1/2) vartheta_x(dw)=kappa_x`,

the PWIT reciprocal-edge order parameter isolated in the preceding run.

**B7 outcome:** successful. The previously heuristic `R^(-1)` reciprocal-edge channel is now an exact positive-density spectral theorem after tail-scale truncation. The coefficient agrees with the local Poisson order parameter, with no simulation and no finite-size fit.

## 6. B19 — make the tail mechanism an algorithm, then identify exactly where it fails for the full matrix

The theorem above has a constructive certificate.

Given the radial marks and thresholds `t<=s`:

1. build the threshold graph `H_t` with edge set `{e:R_e>tn}`;
2. compute the degree of every vertex in `H_t`;
3. output every edge `e` with `R_e>sn` whose two endpoints both have degree one.

The output is exactly the strong-isolated edge set counted by `J_n(s,t)`. Each returned edge carries two explicit skeleton eigenvalues, and no eigenvalue solver is needed to certify their moduli: the characteristic equation is `lambda^2=(R_e/n)^2 w_1w_2`.

This algorithmic reformulation exposes the only missing bridge to `T_corr=1`.

Write the full normalized matrix as

`A_n = A_n^{>t} + A_n^{<=t}`.                                    (6.1)

Theorem B certifies order `n/t` exact skeleton eigenvalues at radial scale order `t`. To turn (5.11) into a lower tail for the source limit `mu_x`, one needs a theorem saying that reattaching `A_n^{<=t}` cannot destroy an asymptotically comparable number of those eigenvalues when first `n->infinity` and then `t->infinity`.

For a normal or uniformly well-conditioned block-diagonal matrix, this would resemble a standard perturbation problem. Here it does not: the full matrix is nonnormal, and operator-norm control alone does not supply eigenvalue-count stability. A large reciprocal pair can be spectrally rearranged by dense couplings through a badly conditioned complement. This is precisely why the local two-cycle calculation in the preceding run was insufficient.

The new reduction is therefore:

> **Reattachment stability obligation.** Find `c_x>0` and a tail-scale sequence of deterministic inequalities strong enough to imply, for all sufficiently large fixed `t`,
> 
> `liminf_{n->infinity} mu_{A_n}({|z|>c_x t}) >= c_x/t`
> 
> in probability, using the strong-isolated skeleton certificates above and controlling the sub-threshold Schur complement or Hermitization.

A proof of this obligation, combined with Theorem A, would pin the frozen family's radial power exponent to exactly `1` and increment `T_corr` from `0` to `1`.

**B19 outcome:** successful as a reduction, not as source closure. It converts the vague phrase “large reciprocal edges should create tail eigenvalues” into a concrete linear-size certificate and isolates one specific missing nonnormal reattachment theorem.

## 7. Counterexample-oriented interpretation

The source contrasts an iid axis-supported endpoint with a Hermitian heavy-tail endpoint. A tempting interpolation heuristic is that tails might gradually change with the angular dependence measure.

The combined B3/B7 result makes that heuristic harder to sustain for this family:

- every interior `x` has the same certified upper tail exponent endpoint `>=1`;
- every interior `x` has `K_1(vartheta_x)=kappa_x>0`;
- after keeping only the tail-scale edges, every interior `x` has a rigorously certified `R^(-1)` eigenvalue channel with asymptotic coefficient `kappa_x`;
- the channel disappears at the axis endpoint because `kappa_x->0`.

Thus the mathematically plausible picture is a singular tail-class transition at the axis-supported endpoint rather than a smooth interpolation of power exponents. This is still a **conjectural interpretation for the full limiting law**. The present run does not call it a refutation or theorem about `mu_x` until reattachment stability is proved.

## 8. Exact finite self-check

Only after the analytic route produced Theorem B did I add a small exact checker for its finite combinatorial core:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T16-12-44Z__exceedance-skeleton-count-check.py`

creation commit `3499264d6c1e379a95e00819a7413b8153df5576`.

It exactly enumerates complete-graph incidences for `n=4,...,10` and verifies:

- one edge has `2(n-2)` other incident edges;
- two disjoint candidate edges have `4n-12` distinct other edges in the union of their isolation neighborhoods;
- overlapping strong-isolated events are incompatible;
- the disjoint covariance formula is exact over rational arithmetic.

Archived output:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T16-12-44Z__exceedance-skeleton-count-check.out`

creation commit `d3b1c3a9765495de96f381adb1a253a32475ab15`, ending

`ALL_EXACT_CHECKS_PASS = True`.

This is explicitly a **SELF-CHECK**. The asymptotic theorem is proved on the page above; the script is not being used as a substitute for the proof.

## 9. What moved mathematically and what did not

Frozen source metric:

`T_corr: 0 -> 0`.

So there is **no metric movement** and the source question remains open.

What did move:

1. the all-`p<1` moment theorem now holds uniformly for the entire interior `vartheta_x` family, not only `x=1/4`;
2. the reciprocal-edge tail mechanism is no longer just a finite block or PWIT count: the tail-scale exceedance skeleton contains a deterministic asymptotic density `e^(-2/t)/s` of exact strong-isolated blocks;
3. their exact spectral tail coefficient tends to `K_1(vartheta_x)=kappa_x`;
4. the remaining proof obligation has been reduced to a single nonnormal reattachment-stability problem.

No claim of `PROVED`, `REFUTED`, `KNOWN`, or closure is made.

## 10. Next run

Because this is unchanged run 2 for Q1.9, one more unchanged run triggers Section I. The next run should **not** replay B3/B7/B19 or B2/B24/B30.

The best new triple is:

- **B11 DUALIZE:** express reattachment through Hermitization/resolvent or logarithmic-potential inequalities, where eigenvalue counts can be controlled through singular values rather than direct nonnormal perturbation;
- **B15 BREAK THE SYMMETRY:** condition on a strong isolated pair and explicitly retain the two different left/right couplings to the complement instead of replacing them by a symmetric proxy;
- **B29 ADD THE POINTS AT INFINITY:** rescale `z=t omega` and analyze the large-`t` Schur-complement boundary problem, with the goal of proving a uniform exclusion annulus around the two reciprocal-edge roots.

If those moves fail to increment `T_corr`, the report must be the full five-part Section-I stuck report and choose exactly one allowed recovery action.

## 11. Ledger delta for the designated shared-root maintainer

```yaml
ledger_delta:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.9
  claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md
  category: HARD OUTSIDE
  status: PARTIAL
  metric: T_corr
  before: 0
  after: 0
  movement: no movement
  unchanged_streak_q19: 2
  methods: [B3, B7, B19]
  new_results:
    - all p<1 moments uniformly bounded over the full interior vartheta_x family
    - exact strong-isolated edge density 2 J_n(s,t)/n -> exp(-2/t)/s in L2 for the exceedance skeleton
    - skeleton tail lower coefficient tends to K_1(vartheta_x)=(x(1-x))^(1/4)
  remaining_obligation: prove nonnormal reattachment stability from the tail-scale skeleton to the full limiting ESD
  exact_self_check: PASS
  closure: false
```
