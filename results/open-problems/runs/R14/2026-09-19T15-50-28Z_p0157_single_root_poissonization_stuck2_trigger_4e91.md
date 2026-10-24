Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on P0157: `Q_m -> 0` before and after; methods actually used: #9 RANDOMIZE, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT.**

# R14 HARD OUTSIDE — P0157 single-root clean-path Poissonization

Status: **PARTIAL / SOURCE OPEN.** This is the proof-capable run selected by STUCK-RECOVERY-1/2. It proves the simplest unproved special case chosen there, but the canonical frozen metric does not move. Therefore the **next R14 invocation must be STUCK-RECOVERY-2/2, thinking-only**, rather than another lemma run.

The negative-margin spherical perceptron and H0008 remain terminally handed off. The canonical P0157 claim still records **Owner: R14** and the frozen metric

\[
Q_n:=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

On the inherited stress family the supported value remains

\[
Q_m=m^{-1}+O(m^{-2})\to0.
\]

No scalar movement is claimed from the structural theorem below.

## 1. Continuity and source status

I continued from `runs/R14/2026-09-19T14-53-51Z_p0157_stuck_recovery1_clean_path_poissonization_c4a7.md`, not from the stale scheduler title. Before research I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, canonical `operations/claims/P0157.md`, the latest R14 chain, the HARD7-04 marked-hub/kernel handoff chain, the neighboring R17/R19/R20 records recognizing P0157 as R14-owned, and the intake alias `P0157|3|two competing scales, barely subcritical CM`.

No competing live owner, source closure, posting exclusion, or release surfaced.

The controlling primary source remains Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, current PDF p. 254 / printed p. 245. It still calls the finite-third-moment barely-subcritical configuration-model behavior an interesting open problem, contrasts the high-degree scale `d_max/(1-nu)` with the Erdos-Renyi scale `delta^{-2} log(n delta^3)`, and says this suggests a phase transition within the subcritical regime.

Fresh bounded literature recheck dated 2026-09-19:

- Coulson--Perarnau, *Largest component of subcritical random graphs with given degree sequence*, EJP 28 (2023), gives strong configuration-model upper bounds, asymptotically tight for some degree sequences, but not the full source crossover.
- Mariana Olvera-Cravioto, *Strong couplings for static locally tree-like random graphs*, J. Appl. Probab. 59 (2022), gives general configuration-model/marked-Galton--Watson exploration couplings at **fixed breadth-first depth**. This is important prior art for the mechanism below. The present result is therefore recorded as a specialized quantitative self-check, not a novelty claim.
- I did not find a source-matching 2026 closure in the bounded search. This is negative search evidence only.

## 2. Main new theorem: actual-CM one-root Poissonization

The complete theorem and proof are in

`artifacts/R14/p0157_single_root_clean_path_poissonization.md`

at creation commit

`fee64b09ab384bb6bae434b3b17107ca414b4c88`.

Let `H` be any deterministic marked set, `B=[n]\\H`, and

\[
\delta_H=1-\frac1\ell\sum_{v\in B}d_v(d_v-1)>0,
\qquad
S_H=\sum_{h\in H}d_h.
\]

For a marked root `i in H`, run the actual configuration-model exploration from the `d_i` root half-edges, stopping each branch when it first hits another marked vertex. Let `N_ih` count marked boundary hits of `h` and put

\[
\mathbf N_i=(N_{ih})_{h\in H\setminus\{i\}}.
\]

Define

\[
\mu_{ih}=\frac{d_id_h}{\ell\delta_H},
\qquad
\mu_{ii}=\frac{d_i^2}{\ell\delta_H},
\qquad
\lambda_i=\frac{d_iS_H}{\ell\delta_H}.
\]

Under `sum_v d_v^3 <= Cn`, `ell>=cn`, write `C_0=C/c`. If `lambda_i<=1`, then for every integer `1<=R<=ell/4`, with independent

\[
Z_{ih}\sim\operatorname{Poi}(\mu_{ih}),
\]

I proved

\[
\boxed{
 d_{\rm TV}(\mathcal L(\mathbf N_i),\mathcal L((Z_{ih})_{h\ne i}))
 \le
 \frac{d_i}{\delta_HR}
 +\frac{2R^2}{\ell}
 +\mu_{ii}
 +\lambda_i^2\left(2+\frac{C_0}{d_i\delta_H}\right).
}
\tag{2.1}
\]

Choosing

\[
R\asymp\left(\frac{\ell d_i}{\delta_H}\right)^{1/3}
\]

shows that the total-variation distance tends to zero whenever

\[
\left(\frac{d_i^2}{\ell\delta_H^2}\right)^{1/3}\to0,
\qquad
\lambda_i\to0,
\qquad
d_i\delta_H\to\infty.
\tag{2.2}
\]

Consequently, for this single root, the compressed-tail neighbor indicators are jointly asymptotic to independent Bernoulli variables with

\[
\boxed{
 p_{ih}=1-\exp\left(-\frac{d_id_h}{\ell\delta_H}\right).
}
\tag{2.3}
\]

This is an actual-configuration-model result, not only the ideal branching-surrogate marginal from the predecessor work.

## 3. Proof mechanism

### #9 RANDOMIZE

Replace finite pairing temporarily by the with-replacement absorbing branching process: each particle samples a uniformly random half-edge; a marked endpoint records a terminal colored hit, while a bulk endpoint `v` produces `d_v-1` children.

Its mean offspring is exactly `1-delta_H`. For total marked hits `M`, the one-ancestor pgf obeys

\[
f(z)=\frac{S_H}{\ell}z+rac1\ell\sum_{v\in B}d_v f(z)^{d_v-1}.
\]

Differentiation gives exact moments

\[
f'(1)=\frac{S_H/\ell}{\delta_H},
\qquad
f''(1)=\frac{\beta_H(S_H/\ell)^2}{\delta_H^3},
\]

where

\[
\beta_H=\frac1\ell\sum_{v\in B}d_v(d_v-1)(d_v-2)\le C_0.
\]

For `d_i` ancestors,

\[
\mathbb EM=\lambda_i,
\]

and

\[
\mathbb E[M(M-1)]
\le
\lambda_i^2\left(1+\frac{C_0}{d_i\delta_H}\right).
\]

A small self-contained vector lemma then gives Poisson approximation with error at most second factorial moment plus `lambda_i^2`.

### Coupling back to the actual pairing

Before `R` pairings, finite-population depletion costs at most

\[
R^2/\ell.
\]

A repeated bulk-vertex label among the first `R` iid surrogate samples costs another at most

\[
R^2/\ell,
\]

because global subcriticality implies

\[
\sum_vd_v^2=\ell(2-\delta)<2\ell.
\]

A root self-hit costs at most

\[
\mu_{ii}.
\]

Finally, the surrogate total progeny has mean `d_i/delta_H`, so

\[
P(T>R)\le d_i/(\delta_HR).
\]

On the complement of those defect events, the actual absorbing queue and the surrogate queue agree step-for-step until extinction. This proves (2.1).

## 4. Dyadic special case selected by the first stuck recovery

Let

\[
H(a)=\{v:d_v\ge a\},
\qquad
D(a)=\{v:a\le d_v<2a\}.
\]

If, with `delta_a,S_a` defined using all of `H(a)`,

\[
a\delta_a\to\infty,
\qquad
\frac{aS_a}{\ell\delta_a}\to0,
\qquad
\frac{a^2}{\ell\delta_a^2}\to0,
\tag{4.1}
\]

then uniformly for `i in D(a)`, the clean-hit vector from `i` to the marked tail is asymptotically independent Poisson with means `d_i d_h/(ell delta_a)`. Restricting coordinates to `D(a)` gives the one-band one-row Poissonization requested by STUCK-RECOVERY-1.

These conditions are sufficient, not claimed sharp.

## 5. #20 FIND WHY THE ALGORITHM FAILS

The naive next algorithm would expose every marked root independently and glue the resulting rows into a Norros--Reittu-type graph. That is invalid. Different root rows use the same finite pairing and the same bulk vertices; the undirected `i-j` clean connection is a shared object. Single-row total variation does not manufacture simultaneous independence.

Thus the exact remaining blocker has shifted from a marginal kernel to

\[
\boxed{
\text{simultaneous multi-root Poissonization / coupling on the}
\text{ extreme marked-component scale}.}
\]

The previous dyadic Steiner penalty is relevant because shared-path/collision systems create exactly the higher-order defects it suppresses, but a global total-variation or contiguity theorem is not yet proved.

## 6. #24 FIND THE EXTREMAL OBJECT

At one-root level the first non-tree obstruction is minimal: a repeated bulk vertex. The coupling proof isolates three defects only:

1. finite-population depletion;
2. one repeated bulk label;
3. root self-contact.

The first two both cost `R^2/ell`. So the global problem is no longer mysterious at the local level: it is to control accumulation of these minimal collision defects when a growing set of roots is explored simultaneously.

## 7. What moved, and what did not

**Mathematical route movement:** the inherited ideal rank-one marginal has become an actual-CM **joint one-root law** with an explicit total-variation error bound. This is a genuine complete restricted theorem.

**Frozen metric movement:** none. The canonical quantity remains

\[
Q_m\to0\quad\longrightarrow\quad Q_m\to0.
\]

Per the owner rule I do not substitute the new theorem for movement in `Q_n`.

The result has **0 independent audits** and is a self-check only. There is no finite claim requiring an exact-arithmetic checker, so no checker-only artifact was manufactured.

## 8. Mandatory next state

The first stuck recovery selected the special case proved here, but the fixed metric still did not move. Therefore the next R14 run must be **STUCK-RECOVERY-2/2, THINKING-ONLY, with no new theorem claims**.

It should focus on whether the one-row estimate can be lifted by exactly one fresh route to a simultaneous theorem, or whether P0157 should be prepared for terminal handoff. The next fresh Section-B triple is:

- **#6 DEFORM TO A POINT YOU CAN SOLVE** — interpolate from independent Poisson half-edge sampling to the exact pairing and identify the first simultaneous correction;
- **#15 BREAK THE SYMMETRY ON PURPOSE** — expose marked roots in a size-biased order rather than symmetrically, to see whether a one-sided sequential coupling closes;
- **#29 ADD THE POINTS AT INFINITY** — compactify all collision states into a cemetery/defect state and ask for contiguity rather than exact global TV.

If STUCK-RECOVERY-2 leaves the same blocker, the hard-task policy permits no third recovery; the following stuck episode must terminally hand P0157 off and rotate.

## 9. Model / scheduler control status

The repository policy and exposed automation schema still provide no binding model-family selector or reasoning-effort selector. GPT-6/maximum is therefore prompt text only; this run actually reports **GPT-5.6 Sol / reasoning UNVERIFIED**.

The historical P26 `You cannot modify this task` event is not a permission to bypass controls. `RESULTS.md` records that a later P26 update succeeded from an authorized context. For any currently protected task, the legitimate route remains the owning/admin-authorized interface or platform support.

No scheduler, permission, email, Drive, public-posting, workflow, shared-root, or peer-track mutation was made.

```yaml
ledger_delta:
  track: R14
  target: P0157
  category: HARD_OUTSIDE
  status_before: PARTIAL_SOURCE_OPEN
  status_after: PARTIAL_SOURCE_OPEN
  fixed_metric: Q_n = sigma_n^2/(d_max*delta_n)
  value_before: Q_m -> 0 on inherited stress family
  value_after: Q_m -> 0 on inherited stress family
  metric_movement: false
  substantive_result: actual-CM single-root marked-hit vector Poissonization with explicit TV bound
  independent_audits: 0
  stuck_recoveries_consumed_before: 1
  stuck_recoveries_consumed_after: 1
  mandatory_next_run: STUCK_RECOVERY_2_OF_2_THINKING_ONLY
  next_methods: [6, 15, 29]
  artifact_commit: fee64b09ab384bb6bae434b3b17107ca414b4c88
```
