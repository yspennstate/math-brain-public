Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on H0008: `I_mf = a_hi-a_lo -> same`. STUCK-RECOVERY-1/2, THINKING-ONLY; no new theorem claims. Methods actually used: #7 TAKE THE LIMIT, #22 READ THE FAILURES, #30 DO ONE SCALE, ONE DIRECTION AT A TIME.**

# R14 HARD OUTSIDE — H0008 stuck recovery 1/2: port the one-type exit-time regeneration mechanism

## 0. Continuity, ownership, and mandatory stuck state

This run obeys the mandatory Section-I recovery triggered by the preceding R14 report `runs/R14/2026-09-19T07-51-25Z_h0008_palm_transfer_pipe_jacobian_83c1.md`. I do **not** reopen the original negative-margin spherical-perceptron target, H0017, D0036, D0039, or D0034. The active exclusive R14 HARD OUTSIDE claim remains `operations/claims/H0008.md`.

The canonical source remains Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3, open problem (6), **Boundary fluctuations**. The source asks for the multifractal spectrum of transmission-weighted flows and for harmonic measure of the failed cluster, where dimension drop is expected. The later Kumar--Duddala companion arXiv:2608.21125 concerns front propagation and continuous-type limit questions, not a resolution of this harmonic-measure clause.

The frozen metric is already maximal for the finite-type multifractal clause,

\[
I_{\rm mf}=a_{\rm hi}-a_{\rm lo}.
\]

It cannot honestly increase in this thinking-only harmonic-measure recovery. Therefore the metric is unchanged. Counting this mandated recovery, this is the fourth consecutive H0008 run without a further change to `I_mf`; the hard-task recovery counter, not the raw unchanged streak, is the controlling state: **STUCK-RECOVERY-1/2**.

Status remains **PARTIAL / SOURCE OPEN**. No new theorem, lemma, numerical endpoint, or finite certificate is claimed in this report.

## 1. Required repository/source read

Before thinking, I read or scoped the current repository state required for continuity:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/claims/H0008.md`;
- the newest R14 H0008 report, `runs/R14/2026-09-19T07-51-25Z_h0008_palm_transfer_pipe_jacobian_83c1.md`;
- repository-wide H0008/ownership/neighbor searches, including the neighboring R19 source-recheck record;
- the H-intake `probability_1000_intake_H_20260914/problems.jsonl`, containing the source-checked H0008 wording; and the broader intake family was scoped for ownership/rotation conflicts, though no rotation is authorized in this first recovery.

Fresh literature check on 19 September 2026 retained the same source state and rechecked the nearest solved mechanisms:

- Pierre Rousselin, arXiv:1708.06965, *Invariant Measures, Hausdorff Dimension and Dimension Drop of some Harmonic Measures on Galton-Watson Trees*;
- Pierre Rousselin, arXiv:1711.07920, *Dimension Drop for Transient Random Walks on Galton-Watson Trees in Random Environments*;
- Sebastian Altok, arXiv:1307.5962, *Unimodularity for multi-type Galton-Watson trees*;
- Amir Dembo and Nike Sun, arXiv:1011.4056, *Central limit theorem for biased random walk on multi-type Galton-Watson trees*.

The bounded search again found no theorem that can simply be cited to provide the exact transient multitype harmonic-descendant stationary law required here. This is bounded negative evidence, not a novelty certificate.

## 2. (a) Exact blocking statement

The preceding run reduced the remaining harmonic-stationarity problem to the following scalar conductance transfer equation. For a finite type set `D`, source laws `P_i`, root escape conductance `B`, size-biased potential offspring count `\widehat\nu`, and sibling conductance sum `R_i`, define

\[
\boxed{
(\mathcal Lh)_j(b)
=
 m_*q_j b\sum_i p_{ij}\,
 \mathbb E\!\left[
 \frac{
 h_i\!\left(\dfrac{b+R_i}{1+b+R_i}\right)
 }{b+R_i}
 \right],
\qquad b>0.
}
\tag{2.1}
\]

The precise remaining obligation is to construct a vector function `h=(h_i)` such that

\[
\boxed{
\mathcal Lh=h,
\qquad
h_i(b)>0\ \ P_i\text{-a.e. on }\{b>0\},
\qquad
\sum_i\mathbb E_i[h_i(B)]=1,
}
\tag{2.2}
\]

and then verify the logarithmic integrability hypotheses needed by the previously proved PF--KL reduction.

The `R_i=0` / sole-infinite-child part has already been isolated and shown spectrally subcritical through the extinction Jacobian. Hence the exact blocker is not (2.1) indiscriminately but the **branch-producing channel**

\[
\boxed{R_i>0,}
\tag{2.3}
\]

i.e. the transition at a genuine branching point where at least one infinite sibling competes with the harmonic descendant.

## 3. (b) Routes already tried, and the exact reason each fails to finish H0008

This recovery deliberately does not add another lemma. The useful output is a consolidated failure map.

1. **Pressure / branching-random-walk route.** The shifted pressure `\psi(q)=\phi(1+q)` and its finite/zero-temperature analysis solve the finite-type multifractal clause under the recorded hypotheses. **Failure for harmonic measure:** harmonic child selection contains a random sibling normalization through escape conductances, so the Perron pressure does not encode the harmonic environment.

2. **Pressure-only harmonic formula.** An explicit pair of one-type Galton--Watson examples with the same complete pressure curve but different harmonic dimensions already killed this idea. **Failure:** even all of `\phi(\beta)` omits offspring/conductance-law information needed by harmonic flow.

3. **Electrical recursion.** The exact recursion `B=S/(1+S)` and local harmonic weights `B_u/S` translate the problem into conductances. **Failure:** recursion alone supplies neither a stationary environment along the harmonic ray nor the ergodic theorem needed for dimension.

4. **One-type / Bethe / exact lumpability slices.** The one-type theorem and exact type-lumpability reduce substantial subclasses to ordinary Galton--Watson trees and give dimension drop there. **Failure:** generic source matrices have parent-type-dependent block offspring vectors and do not collapse to one type.

5. **PF--KL identity.** Conditional on an equivalent stationary ergodic harmonic-descendant environment, harmonic dimension is `log rho` minus a mean KL divergence from the PF flow. **Failure:** this is a reduction, not a construction of the needed stationary law.

6. **Equality rigidity.** The zero-KL source equality case was reduced to the deterministic regular no-thinning model. **Failure:** strictness remains conditional on the stationary environment existing with the required equivalence/integrability.

7. **Palm scalar transfer operator.** The tree-space stationarity problem was compressed exactly to (2.1)--(2.2). **Failure:** positivity and mass preservation of a Perron/Markov operator do not by themselves imply an absolutely continuous invariant density. A density sequence can concentrate near the boundary of conductance space.

8. **Sole-infinite-lineage / pipe decomposition.** The `R_i=0` channel is governed by the extinction Jacobian, whose spectral radius is below one; long one-child pipes therefore have exponential tails. **Failure:** this removes one source of noncompactness but leaves the branch-producing `R_i>0` operator untouched.

9. **Direct import of existing invariant-measure results.** Rousselin supplies explicit/invariant forward environments for one-type Galton--Watson flow rules and, in the random-environment paper, uses exit-time regeneration plus ergodic theory; Altok and Dembo--Sun construct multitype reversible/reversing laws for different rerooting or biased-walk kernels. **Failure:** none of these papers, as checked, directly identifies the exact invariant law of the present transient *harmonic descendant* kernel with type-dependent thinning and sibling-conductance competition.

The recurring error to avoid is now clear: another positivity estimate on `\mathcal L`, or another finite-type moment identity, will not finish the problem unless it produces a genuine positive-recurrence / mean-compactness mechanism for the `R_i>0` channel.

## 4. (c) What a successful proof must contain that no existing route contains

A complete route needs a **recurrence mechanism at genuine branch points**, not another local identity. Concretely it must furnish at least one of the following, in a form strong enough to imply (2.2) and PF--KL integrability:

- a regeneration construction for the harmonic ray in which regeneration blocks include the entrance type, exit type and sibling-conductance marks, together with a finite mean regeneration length and an absolutely continuous Palm/Rokhlin stationary law;
- a Foster--Lyapunov estimate for the conductance/type chain that prevents mass of Cesaro iterates of `\mathcal L` from escaping toward `b=0`, yielding uniform integrability and hence a positive fixed density;
- or an explicit multitype invariant-density formula that generalizes the one-type harmonic-flow law and is provably positive/equivalent on every surviving type component.

The **new ingredient has to control the branch-producing conductance normalization uniformly across types**. The previous results control finite-type Perron growth, one-child pipes, and the equality case, but none controls recurrence of the actual branch-point environment.

## 5. (d) Simplest special case still unproved

The cleanest first non-lumpable test case is a two-type source with deterministic potential degree

\[
\nu\equiv2,
\qquad q=(1/2,1/2),
\qquad
P=\begin{pmatrix}
3/4&3/4\\
1/2&1/4
\end{pmatrix}.
\tag{5.1}
\]

All transmission entries are strictly between zero and one and the mean matrix is irreducible. The two `q`-weighted row averages are unequal (`3/4` versus `3/8`), so the earlier one-block lumpability theorem does not collapse this to a one-type Galton--Watson tree. This case is intentionally recorded only as the **simplest unproved special case for the regeneration port**, not as a new result and not as a finite certificate.

The immediate special-case question is therefore:

\[
\boxed{
\text{Can Rousselin's exit-time/Palm construction be written explicitly for (5.1),}
\text{ producing a positive fixed density for (2.1)?}
}
\tag{5.2}
\]

If the answer is no, the obstruction in this two-type case should reveal exactly which multitype renewal quantity is missing.

## 6. (e) Nearest solved problem and the ingredient it has that H0008 lacks

The nearest solved mechanism is Rousselin's one-type Galton--Watson harmonic/random-environment work.

- In arXiv:1708.06965, Rousselin builds invariant measures for a class of flow rules on marked one-type Galton--Watson trees under algebraic assumptions and applies them to harmonic dimensions.
- In arXiv:1711.07920, he uses **regeneration times and ergodic theory** to construct explicitly an invariant measure for the forward environment seen at exit times, absolutely continuous with respect to the joint tree/path law.

That is much closer to the present obstruction than ordinary compactness. What the source problem lacks is not regeneration in principle, but a verified **finite-type marked renewal theorem for the harmonic branch-point chain**. At a regeneration step here the block law depends on entry type, exit type, transmission thinning and the random sibling conductances that normalize harmonic choice. The one-type scalar exchangeability that makes the existing constructions tractable no longer collapses those marks automatically.

Altok and Dembo--Sun show that finite-type Galton--Watson trees can support useful reversible/reversing environment laws, but their kernels are not the transient harmonic-exit descendant kernel (2.1). They are evidence that a matrix/Palm renewal formalism is plausible, not a substitute for proving it.

## 7. Three actual Section-B moves in this thinking run

### #7 TAKE THE LIMIT

I conceptually collapsed the harmonic ray by skipping the already-controlled sole-infinite-child pipes and looking only at successive **genuine branching points**. This is the natural limiting/embedded chain after the `rho(J)<1` pipe result. Outcome: the right state appears to be a marked branch-point environment `(entry type, descendant conductance configuration, chosen exit type)`, but no invariant law is claimed here.

### #22 READ THE FAILURES, NOT THE SUCCESSES

I re-read the mechanism in Rousselin's one-type papers and compared it with the multitype reversible constructions of Altok and Dembo--Sun. Outcome: the missing object is not another spectral estimate; it is a finite-type extension of the **exit-time regeneration/Rokhlin-tower invariant law** adapted to conductance-biased child choice. This is the most concrete literature port found in the recovery.

### #30 DO ONE SCALE, ONE DIRECTION AT A TIME

I isolated the first non-lumpable two-type deterministic-degree model (5.1) and the branch-producing channel `R_i>0` as the sole port target. Outcome: the next mathematical run should not attempt arbitrary offspring laws and arbitrary types simultaneously; it should derive the regeneration kernel in this smallest genuinely multitype setting and identify which estimate survives abstraction.

No method above is promoted to a theorem in this recovery.

## 8. Section-I choice: PORT THE TECHNIQUE FROM (e)

I choose exactly one permitted recovery action:

\[
\boxed{\textbf{PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.}}
\]

The next R14 mathematical attempt on H0008, if still authorized, is therefore constrained to port Rousselin's exit-time regeneration/Palm/Rokhlin construction first to the two-type test (5.1), then only after that to the general finite-type source law. It should not return to pressure calculations, another PF lemma, a checker, or a generic fixed-point existence slogan.

The next nonrepeating Section-B moves to use for that attempt are:

- **#10 DERANDOMIZE** — turn the regeneration/Palm existence picture into an explicit density/renewal equation;
- **#13 FIND WHAT ONLY INCREASES** — search for a Lyapunov/renewal quantity that forces return away from `b=0` at genuine branch points;
- **#24 FIND THE EXTREMAL OBJECT** — identify the type/conductance configuration that maximizes regeneration delay or density concentration and prove it is still controlled.

This is **recovery 1 of at most 2** on H0008. If the next permitted recovery again leaves the same blocker, the second recovery must either produce the missing positive-recurrence input or prepare terminal handoff; a third recovery on H0008 is not authorized.

## 9. Model/scheduler capability statement

The current exposed automation-control surface still provides prompt text, schedule, timing mode, enabled state, notification/email flags, timezone and run metadata, but **no binding model-family selector and no reasoning-effort selector**. Thus `GPT-6 / maximum` remains a request inside the prompt, not an enforceable setting from this scheduler surface. This run actually identifies itself as GPT-5.6 Sol with reasoning level UNVERIFIED.

A task returning `You cannot modify this task` is an authorization-context problem. The lawful workaround is an owning/admin-authorized context or platform support; it is not a permission bypass or duplicate-task workaround. No scheduler, permission, email, Drive, public-posting or workflow state was changed in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R14
  source: "Kumar 2026 arXiv:2608.15987v1, Section 12.3 open problem (6), Boundary fluctuations"
  canonical_claim: "operations/claims/H0008.md"
  target_status: "PARTIAL / SOURCE OPEN"
  metric: "I_mf = a_hi - a_lo"
  metric_before: "a_hi - a_lo (exact finite-type multifractal interval already certified)"
  metric_after: "same"
  movement: "NO MOVEMENT"
  unchanged_metric_runs_since_last_certification_including_this_recovery: 4
  stuck_recovery: "1/2"
  thinking_only: true
  methods_used: [7, 22, 30]
  new_theorem_claims: []
  blocker: "Positive normalized fixed density Lh=h for the multitype harmonic conductance transfer operator, with equivalence and PF-KL logarithmic integrability; only R_i>0 branch-producing channel unresolved."
  chosen_section_I_action: "PORT THE TECHNIQUE FROM NEAREST SOLVED PROBLEM"
  port_source: "Rousselin exit-time regeneration / invariant forward-environment construction on one-type Galton-Watson trees"
  simplest_unproved_special_case: "two types, nu=2, q=(1/2,1/2), P=[[3/4,3/4],[1/2,1/4]]"
  next_methods: [10, 13, 24]
  checker: "none; mandated thinking-only recovery"
  audit_ids: []
  remaining_obligation: "Build and control the branch-point regeneration/Palm kernel, first in the two-type non-lumpable test and then generally, yielding a positive equivalent stationary density and PF-KL integrability."
```
