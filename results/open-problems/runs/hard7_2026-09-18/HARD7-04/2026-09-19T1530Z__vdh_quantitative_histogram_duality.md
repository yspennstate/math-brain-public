Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen metric `lim Delta_dual,n`: `0 -> 0`; methods actually used: B9 RANDOMIZE, B23 DO WHAT THE PROPOSER DID NOT EXPECT, B27 SWAP THE QUANTIFIERS.**

# HARD7-04 bounded research iteration — quantitative post-giant degree-law duality

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / stronger source-level duality proof candidate / source still OPEN until the repository closure protocol is satisfied**.

## 1. Continuity, ownership, required reads, and capability honesty

I resumed the admitted canonical target

`operations/claims/VDH-8.3-DUALITY.md`,

owner `HARD7-04`, status `OPEN / ADMITTED`. I did not restart the old I0049 queue seed, mint an alias, overwrite another claim, edit another track, modify a shared root ledger, or create/modify/disable any schedule.

Before new mathematics I re-read or recovered the required control/continuity surfaces:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the active `VDH-8.3-DUALITY` claim;
- the latest complete own checkpoint `2026-09-19T1430Z__vdh_collared_lower_bound_recovery.md` and its proof/local-limit artifacts;
- the earlier post-giant stopping and random-time weighted-residual proofs on which the present route depends;
- the newest complete neighboring HARD7-03 and HARD7-05 reports available at run start;
- targeted intake/queue searches including `probability_1000_intake_I_20260914/problems.jsonl` references for I0049 and neighboring random-graph entries.

The intake history still records I0049 as **KNOWN / RESOLVED IN QUEUED SCOPE**, so it remains ineligible as a fresh assignment. No competing owner, release, posted equivalent, or closure marker surfaced for `VDH-8.3-DUALITY`.

The scheduler capability situation is unchanged. The exposed automation interface offers task identity/title/prompt, schedule/timing mode, enabled state and update fields; it exposes **no model selector and no reasoning-effort selector**, and no guaranteed execution duration. GPT-6/maximum therefore remains prompt-requested only. This runtime identifies as GPT-5.6 Sol and exposes no reasoning-effort telemetry, so the reasoning level is `UNVERIFIED`. Changing that requires a platform/scheduler capability, or another authorized interface, that actually exposes model and reasoning controls; no repository edit can create such a selector.

The root deployment ledger also reconciles the historical `You cannot modify this task` errors: task edit permission can differ by authorized native context, and P26 was later editable from another authorized context. The compliant workaround is to use the owning/authorized context or platform support. It is **not** to bypass permissions or duplicate the task. I did not probe or mutate P26 or any other schedule in this run.

## 2. Exact source and fresh literature/status check — 19 September 2026

The primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

I reopened the PDF and verified the relevant paragraph directly. In the finite-third-moment barely-supercritical configuration-model discussion, after noting that the 2019 work does not investigate the second-largest component in the supercritical regime and motivating an Erdős--Rényi-type picture, the source asks exactly:

> “Does the discrete duality principle still hold?”

The retained source regime is the deterministic-degree configuration model with

\[
\nu_n=1+\varepsilon_n,
\qquad
\varepsilon_n\downarrow0,
\qquad
\varepsilon_n n^{1/3}\to\infty,
\tag{2.1}
\]

positive limiting mean, convergent finite third degree moment, and the source's nondegenerate critical limiting degree law.

The fresh literature check recovered the same nearest structural results as before, plus one important prior-art detail that materially changes how the present theorem must be described.

1. R. van der Hofstad, S. Janson, M. J. Luczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms 55 (2019), DOI `10.1002/rsa.20837`, proves the barely-supercritical giant/exploration inputs used by this track. It does not give the source's requested sharp second-largest-component scaling.
2. **Important prior-art correction/clarification:** Remark 2.7 of that 2019 paper already gives a **fixed-degree** asymptotic for the degree composition of the giant. In the present notation its first-order content is
   \[
   v_k(C_1)=k\rho_n n_k(1+o_p(1))
   \]
   for each fixed `k`, where `rho_n=1-xi_n` is the survival probability. Therefore the extinction-tilt degree profile itself is **not** a new discovery of this track.
3. M. Coulson and G. Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), DOI `10.1214/23-EJP921`, gives general subcritical upper-bound technology and asymptotic tightness for certain sequences, not a theorem already closing the present 2026 source scope.
4. R. van der Hofstad, M. J. Luczak, J. Spencer, *The second largest component in the supercritical 2D Hamming graph*, Random Structures & Algorithms 36 (2010), proves a discrete-duality-type statement in a different model; it is evidence/analogy, not the present configuration-model theorem.

Bounded searches included the exact source phrase, `barely supercritical configuration model second largest component`, `configuration model discrete duality`, and the degree-composition language from the 2019 paper. I found no 2024--2026 theorem that closes the exact finite-third-moment shrinking-window configuration-model source statement. This is bounded negative evidence only, **not** a worldwide novelty certificate.

The correct novelty boundary for this run is therefore narrow and explicit: the fixed-`k` composition mechanism is known; the theorem below is a **simultaneous weighted-ell1 / total-variation uniformization over the whole triangular-array degree support at the natural `n epsilon_n` scale**, derived for the literal complement of the giant using the source-window stopping construction. Independent prior-art review is still required before any novelty claim.

## 3. Carry-in state and frozen metric

The admission metric remains

\[
\Delta_{\rm dual,n}
:=\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|.
\tag{3.1}
\]

Earlier HARD7-04 work already proved

\[
\Delta_{\rm dual,n}\to0.
\tag{3.2}
\]

Thus the metric is already at its mathematical floor, and this run necessarily records

`lim Delta_dual,n: 0 -> 0` — **NO MOVEMENT**.

The previous STUCK2 recovery nevertheless changed the source-level state substantially. It produced a full on-page proof candidate for

\[
|C_{2,n}|
=(1+o_p(1))
\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3),
\tag{3.3}
\]

conditional on the earlier HARD7-04 stopping-time/remainder reductions, with

\[
R_*=
\frac{\mathbb E[D(D-2)^2]}{\mathbb ED}>0.
\tag{3.4}
\]

The last report correctly did **not** label the source PROVED/CLOSED because “discrete duality principle” can be broader than the scalar size asymptotic (3.3), and because independent audits are still missing.

This run attacks that exact residual ambiguity rather than manufacturing another certificate around the already-zero scalar metric.

## 4. Idea-before-code checkpoint and method rotation

Before any verification work, I wrote and committed the new route:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1530Z__vdh_quantitative_histogram_duality_idea.md`

creation commit

`0fc56bc1a39cb4f1114bfb81eb31bb76253d59b7`.

It was read back at that commit before the theorem proof was written.

The immediately preceding run used B3/B11/B14. Repository search found no previous HARD7-04 `VDH-8.3-DUALITY` report using this exact new triple:

- **B9 — RANDOMIZE.** Realize the ideal dual degree law through the independent exponential half-edge clocks already built into the 2019 exploration.
- **B23 — DO WHAT THE PROPOSER DID NOT EXPECT.** Rather than prove another scalar second-component estimate, aim for quantitative duality of the **entire empirical degree law** after giant deletion.
- **B27 — SWAP THE QUANTIFIERS.** Replace fixed-degree asymptotics by one simultaneous weighted `ell^1` estimate over **all** degree classes allowed by the triangular array.

All three moves succeeded mathematically, subject to the inherited post-giant stopping inputs and independent audit.

## 5. Counterexample-first stress test: can a fragmented degree support break uniformity?

Let

\[
n_d:=\#\{i:d_i=d\},
\qquad
M_{n,d}(t):=\sum_{i:d_i=d}\mathbf1\{E_i>t\},
\qquad
m_{n,d}(t):=n_de^{-dt},
\tag{5.1}
\]

where `E_i~Exp(d_i)` independently and `E_i=infinity` for `d_i=0`.

The obvious attempt to refute a whole-histogram statement is to spread the empirical degree mass over as many occupied degree classes as the finite-third-moment constraint permits. The classwise half-line maximal inequality from the earlier HARD7-04 clock proof gives

\[
\mathbb E\sup_t|M_{n,d}(t)-m_{n,d}(t)|
\le4\sqrt{n_d}.
\tag{5.2}
\]

Naively summing (5.2) over all degrees could have lost the source scale. Instead Cauchy--Schwarz gives

\[
\begin{aligned}
\sum_{d:n_d>0}(1+d)\sqrt{n_d}
&\le
\sqrt{(d_{\max}+1)
\sum_d(1+d)^2n_d}.
\end{aligned}
\tag{5.3}
\]

Finite third-moment convergence implies

\[
d_{\max}=o(n^{1/3}),
\qquad
\sum_d(1+d)^2n_d=O(n),
\tag{5.4}
\]

so (5.3) is `o(n^{2/3})`. Since

\[
\varepsilon_n n^{1/3}\to\infty,
\tag{5.5}
\]

we have `n epsilon_n >> n^{2/3}`. Hence even the maximally fragmented support permitted by the source assumptions cannot make the simultaneous clock noise reach the natural duality scale.

**Counterexample-search outcome:** the strongest obvious triangular-array support adversary fails. This is useful structural information: the same `n^{-1/3}` window boundary that controlled the earlier weighted second-factorial moment also protects the entire empirical degree histogram.

## 6. B9 + B27 theorem: simultaneous weighted clock thinning

Summing (5.2) before taking expectation and applying (5.3)--(5.5) yields

\[
\mathbb E\sup_{t\ge0}
\sum_{d\ge0}(1+d)
|M_{n,d}(t)-m_{n,d}(t)|
=o(n^{2/3})
=o(n\varepsilon_n).
\tag{6.1}
\]

Therefore, by Markov,

\[
\boxed{
\sup_{t\ge0}
\sum_d(1+d)
|M_{n,d}(t)-n_de^{-dt}|
=o_p(n\varepsilon_n).
}
\tag{6.2}
\]

This is the quantifier swap: (6.2) is one simultaneous estimate over all degrees and all times. There is no “fix `d`, then let `n` grow” tail gap.

Let `xi_n` be the extinction probability of the size-biased excess branching process and

\[
t_n^*:=-\log\xi_n.
\tag{6.3}
\]

The previously proved lawful giant stopping boundary satisfies

\[
\tau_n-t_n^*=o_p(\varepsilon_n).
\tag{6.4}
\]

Since `t->e^{-dt}` is `d`-Lipschitz and the empirical second moment is bounded,

\[
\begin{aligned}
\sum_d(1+d)n_d
|e^{-d\tau_n}-e^{-dt_n^*}|
&\le
|\tau_n-t_n^*|\sum_dd(1+d)n_d\\
&=o_p(n\varepsilon_n).
\end{aligned}
\tag{6.5}
\]

Evaluating (6.2) at the dependent time `tau_n` and using (6.5) gives

\[
\boxed{
\sum_d(1+d)
|M_{n,d}(\tau_n)-n_d\xi_n^d|
=o_p(n\varepsilon_n).
}
\tag{6.6}
\]

No independence between `tau_n` and the clocks is required because (6.2) is uniform in time.

## 7. Transfer to the exact stopping remainder and then to the literal complement of the giant

Let `S_{n,d}` count degree-`d` vertices still sleeping at `tau_n`. The earlier graph-level stopping theorem proved the degree-square mismatch

\[
\sum_i d_i^2
\left|
\mathbf1\{i\text{ sleeping at }\tau_n\}
-\mathbf1\{E_i>\tau_n\}
\right|
=o_p(n\varepsilon_n).
\tag{7.1}
\]

Degree-zero vertices have no mismatch; for every `d>=1`,

\[
1+d\le2d^2.
\tag{7.2}
\]

Thus (7.1) and (6.6) imply

\[
\boxed{
\sum_d(1+d)|S_{n,d}-n_d\xi_n^d|
=o_p(n\varepsilon_n).
}
\tag{7.3}
\]

Conditional on the exploration history at `tau_n`, the unrevealed half-edges are a uniform perfect matching. Hence (7.3) describes the degree law of an **exact** conditional configuration-model remainder, not an iid approximation to the graph.

The literal complement of the giant differs from this stopping remainder only by components completed before the giant. The previously archived exploration input gives their total half-edge mass

\[
H_n^{pre}=o_p(n\varepsilon_n).
\tag{7.4}
\]

For every positive-degree vertex in those components, `1+d<=2d`; degree-zero vertices never enter such components. Therefore adding the pre-giant components back changes the weighted histogram by only `o_p(n epsilon_n)`.

Let

\[
N_{n,d}^{out}:=\#\{v\notin C_{1,n}:d_v=d\}.
\tag{7.5}
\]

The main theorem of this run is

\[
\boxed{
\sum_{d\ge0}(1+d)
\left|N_{n,d}^{out}-n_d\xi_n^d\right|
=o_p(n\varepsilon_n).
}
\tag{7.6}
\]

A complete on-page proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1530Z__vdh_quantitative_histogram_duality.md`

creation commit

`6b77fdfb3e77eaf9021ec42f8a4632c805b30871`.

That artifact was read back at its exact commit after creation.

## 8. B23 consequence: quantitative total-variation discrete duality

Define the deterministic extinction-tilted vertex degree law

\[
\pi_{n,d}^{\dagger}
:=\frac{n_d\xi_n^d}{\sum_jn_j\xi_n^j}
\tag{8.1}
\]

and the actual empirical degree law outside the giant

\[
\widehat\pi_{n,d}^{out}
:=\frac{N_{n,d}^{out}}{\sum_jN_{n,j}^{out}}.
\tag{8.2}
\]

Because `1-xi_n=O(epsilon_n)` and the mean degree is bounded,

\[
\sum_jn_j\xi_n^j=\Theta(n).
\tag{8.3}
\]

The elementary normalization inequality

\[
\sum_j\left|\frac{a_j}{A}-\frac{b_j}{B}\right|
\le\frac{2\sum_j|a_j-b_j|}{A}
\tag{8.4}
\]

for nonnegative vectors and (7.6) imply

\[
\boxed{
\|\widehat\pi_n^{out}-\pi_n^{\dagger}\|_{TV}
=o_p(\varepsilon_n).
}
\tag{8.5}
\]

The same weighted estimate gives the size-biased/half-edge law. Define

\[
\widehat q_{n,d}^{out}
:=\frac{dN_{n,d}^{out}}{\sum_jjN_{n,j}^{out}},
\qquad
q_{n,d}^{\dagger}
:=\frac{dn_d\xi_n^d}{\sum_jjn_j\xi_n^j}.
\tag{8.6}
\]

Then

\[
\boxed{
\|\widehat q_n^{out}-q_n^{\dagger}\|_{TV}
=o_p(\varepsilon_n).
}
\tag{8.7}
\]

This is stronger than the scalar reflected-drift prerequisite but does not replace it: total variation controls bounded observables, while the excess-degree test `d-1` is unbounded. The earlier degree-square theorem separately supplies

\[
\nu_n^{post}=1-\varepsilon_n+o_p(\varepsilon_n).
\tag{8.8}
\]

Together, (8.5), (8.7), (8.8), and the source-size candidate (3.3) give a substantially more literal discrete-duality picture: the exact post-giant remainder is conditionally a configuration model, its empirical degree law is the extinction tilt to `o_p(epsilon_n)` total variation, its criticality is reflected at first order, and its largest component gives the original second-largest component w.h.p.

## 9. Prior-art reconciliation with the 2019 fixed-degree theorem

Because the 2019 Remark 2.7 fixed-degree composition result is prior art, I wrote a separate reconciliation rather than leaving an ambiguous novelty claim:

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1535Z__vdh_remark27_uniformization.md`

creation commit

`3aa907728f0268861ef18c9a49dfb151b3ee1792`.

It was read back at the exact commit.

Write

\[
\rho_n:=1-\xi_n.
\tag{9.1}
\]

The earlier branching-process expansion gives `rho_n=Theta(epsilon_n)`. For every integer `d>=0`,

\[
0\le d\rho_n-igl(1-(1-\rho_n)^d\bigr)
\le\frac{d(d-1)}2\rho_n^2.
\tag{9.2}
\]

Since

\[
(1+d)d(d-1)=d^3-d\le d^3,
\tag{9.3}
\]

the source third-moment assumption gives

\[
\sum_d(1+d)n_d
|1-\xi_n^d-d\rho_n|
=O(n\varepsilon_n^2)
=o(n\varepsilon_n).
\tag{9.4}
\]

Subtracting (7.6) from the full degree counts therefore yields the simultaneous giant-composition statement

\[
\boxed{
\sum_d(1+d)
\left|N_{n,d}^{G}-d\rho_n n_d\right|
=o_p(n\varepsilon_n).
}
\tag{9.5}
\]

For each fixed degree this is consistent with the known 2019 Remark 2.7 formula. What the present route adds is the single weighted estimate over the full moving support and the associated total-variation consequences. I make **no claim** that the fixed-degree profile itself is new.

As further corollaries, (9.5) gives total-variation convergence of the giant's empirical vertex-degree law to the original size-biased law and of the giant's half-edge-seen degree law to the corresponding twice-size-biased law, under the same source moment assumptions. Again these are presented as uniformizations/corollaries, not as a claim that the underlying composition mechanism was unknown.

## 10. Verification budget

This run introduces no finite exhaustive claim. The mathematical content is analytic: maximal inequalities, deterministic moment bounds, the already-proved stopping/remainder theorem, and elementary normalization/Taylor estimates. In accordance with the 90% rule, I therefore **did not manufacture a new finite checker** merely to prove that the run occurred.

The evidence budget was instead spent on:

1. idea-before-proof persistence (`0fc56bc...`);
2. a complete theorem proof (`6b77fdf...`);
3. an explicit prior-art reconciliation (`3aa9077...`);
4. readback of all three exact commits.

These are self-checks only. They are not independent audits.

## 11. Honest source status and Section-I boundary

I do **not** label `VDH-8.3-DUALITY` PROVED or CLOSED.

The state after this run is stronger than after the previous recovery:

- the second-largest-component size has a complete track-local proof candidate;
- the literal outside-giant empirical degree law is `o_p(epsilon_n)` in total variation from the extinction tilt;
- the corresponding half-edge law has the same quantitative total-variation control;
- the exact stopping remainder is conditionally an exact configuration model;
- the reflected subcritical drift was already proved;
- the known 2019 fixed-degree composition theorem has been explicitly reconciled, not silently rediscovered.

Three obligations remain before closure can even be considered.

1. **Source-scope boundary.** The source phrase “discrete duality principle” could mean full residual graph-law asymptotics, not only exact conditional CM structure plus its degree law, criticality, and second-largest-component consequence. This interpretation must be reconciled against the surrounding source prose rather than silently choosing the narrowest reading.
2. **Independent audits.** The theorem-sized chain has no two genuinely independent OTHER-track proof audits. Repository closure requires both.
3. **Prior art / novelty boundary.** The 2019 fixed-degree theorem is known. A wider literature audit must determine whether the simultaneous shrinking-window weighted-`ell1` version (7.6) is also already implicit or explicit elsewhere.

The frozen metric remains `0 -> 0`, but the **remaining mathematical obligation changed**, so this is not another failed unchanged-obligation stuck run. The previous STUCK2 recovery succeeded, and this execution then proved a genuinely new source-scope strengthening. If a subsequent execution finds no additional source-mathematical obligation beyond audit/polish, `CONTROL.md` says this hard research worker should preserve a handoff and rotate to a fresh admissible hard random-graph target rather than spend further runs producing checker receipts around a quantity already at its floor.

No root shared ledger was edited. No email or Drive action was taken. No schedule was modified.

### ledger_delta

```yaml
track: HARD7-04
target: VDH-8.3-DUALITY
owner: HARD7-04
source_status: OPEN
research_status: PARTIAL_STRONGER_DUALITY_PROOF_CANDIDATE
runtime_model: GPT-5.6 Sol
reasoning_level: UNVERIFIED
requested_model_only: GPT-6 maximum
metric:
  name: lim Delta_dual_n
  before: 0
  after: 0
  movement: NO_MOVEMENT_AT_MATHEMATICAL_FLOOR
methods: [B9, B23, B27]
counterexample_first:
  family: maximally_fragmented_degree_support_under_finite_third_moment
  outcome: FAILED_TO_REFUTE
  reason: simultaneous_clock_noise_o_n_2_3_while_n_epsilon_dominates_n_2_3
new_result:
  type: theorem_sized_partial
  statement: "sum_d (1+d) |N_out(d)-n_d xi_n^d| = o_p(n epsilon_n)"
  vertex_TV: "||pi_out-pi_extinction_tilt||_TV = o_p(epsilon_n)"
  halfedge_TV: "||q_out-q_extinction_tilt||_TV = o_p(epsilon_n)"
idea_checkpoint:
  commit: 0fc56bc1a39cb4f1114bfb81eb31bb76253d59b7
  path: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1530Z__vdh_quantitative_histogram_duality_idea.md
proof_artifact:
  commit: 6b77fdfb3e77eaf9021ec42f8a4632c805b30871
  path: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1530Z__vdh_quantitative_histogram_duality.md
prior_art_reconciliation:
  known_input: "van der Hofstad-Janson-Luczak 2019 Remark 2.7 fixed-degree giant composition"
  new_boundary: simultaneous_weighted_ell1_uniformization_only
  commit: 3aa907728f0268861ef18c9a49dfb151b3ee1792
  path: artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T1535Z__vdh_remark27_uniformization.md
finite_checker: NONE_NOT_APPLICABLE
independent_audits: 0
closure: false
section_I:
  previous: RECOVERY2_SUCCESS_ON_BOXED_LOWER_OBLIGATION
  this_run: NEW_SOURCE_SCOPE_THEOREM_OBLIGATION_CHANGED
next_boundary: source-scope reconciliation / prior-art audit / independent proof audit; rotate if no genuinely new source mathematics remains
```
