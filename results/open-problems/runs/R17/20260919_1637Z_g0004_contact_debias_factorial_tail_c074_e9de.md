Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: G0004 `U_F: 1 -> 1`; STUCK RECOVERY remains `1/2`; methods #5 ADD A PARAMETER AND DIFFERENTIATE / #13 FIND WHAT ONLY INCREASES / #28 REPLACE "FOR ALL" WITH "FOR TYPICAL".**

# R17 C074 — G0004: contact-size debiasing, factorial Harris hierarchy, and an exact lower-tail reduction

Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R17, HARD OUTSIDE.  
Status: **OPEN / PARTIAL / STUCK RECOVERY 1/2**.

## 0. Continuity, source, ownership, and exclusions

The canonical claim `operations/claims/G0004.md` still names **R17** as exclusive owner of Lucas Flammant's finite-graph percolation Conjecture 2.2. The original Chvátal--Sankoff binary-LCS source remains terminally handed off at

\[
0.792665992\le \gamma_2\le0.826275942762282626,
\qquad U-L=0.033609950762282626,
\]

and the later Rhodes--Vargas D0064 source remains terminal at `R_class=0/3`. Neither predecessor is reopened.

At run start I reread:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the canonical G0004 claim;
- the newest own report C073 and the preceding G0004 reports C069--C072;
- the R7-02 G0004 failure-kernel/selector screen and current neighboring admission screens;
- the canonical G-intake identity.

No current root exclusion or ownership record supersedes the R17 G0004 claim.

A fresh 2026-09-19 primary-source check of arXiv:2609.03492 still presents Conjecture 2.2 as open. The source statement remains: for every finite loopless multigraph, origin `o`, boundary `B`, percolation parameter `p`, and family of source-increasing events `E_b` with `P(E_b)>=1-epsilon`, prove a universal conditional success probability tending to one. The public version proves only the outer-face planar case with `1-2 sqrt(epsilon)` and explicitly says the general conjecture remains open. A bounded fresh search by exact title/arXiv id/Conjecture 2.2 wording found no later primary source claiming the unrestricted theorem. This is bounded negative evidence, not a global novelty certificate.

The nearest relevant correlation literature remains Harris--FKG and van den Berg--Häggström--Kahn's conditional cluster inequalities. I found no source in the bounded search stating the contact-size debiasing identity or the all-factorial-moment estimate below for Flammant's failure functional.

The fixed source-wide metric is still

\[
U_F:=\inf\left\{u:\limsup_{\varepsilon\downarrow0}R_*(\varepsilon)\le u
\text{ is rigorously certified under all source quantifiers}\right\}.
\]

Before: `U_F=1`. After: `U_F=1`.

The run is therefore genuine progress in mechanism/reduction but not source closure.

## 1. Exact failure-kernel setup

Use the exact R7-02 reduction. For each boundary vertex define

\[
q_b(\omega):=1-\mathbb P(E_b\mid \pi=\omega).
\]

Then each `q_b` is decreasing, takes values in `[0,1]`, and satisfies

\[
\mathbb E q_b\le\varepsilon.
\tag{1.1}
\]

Write

\[
C_b:=\{o\leftrightarrow b\},\qquad
S(\omega):=\{b\in B:C_b(\omega)\},\qquad
N(\omega):=|S(\omega)|,
\]

and

\[
C:=\{N>0\}=\{o\leftrightarrow B\}.
\]

On `C`, define the pointwise failure kernel

\[
m(\omega):=\min_{b\in S(\omega)}q_b(\omega),
\]

and put `m=0` on `C^c`. Then the exact source-wide failure ratio on the instance is

\[
R= \frac{\mathbb E m}{\mathbb P(C)}.
\tag{1.2}
\]

Let

\[
M:=\mathbb E[N\mid C]
=\frac{\mathbb E N}{\mathbb P(C)}.
\tag{1.3}
\]

The old bounded-contact estimate follows from `R<=epsilon M`. The aim of this run is to understand whether the factor `M` is an artefact of using only the first moment.

## 2. Method #5 — add a parameter and differentiate: exact contact-size debiasing

The useful interpolation is not in `p`; it is between two natural ways of sampling a connected boundary label.

For `0<=theta<=1`, define a probability law `Q_theta` on pairs `(omega,b)` with `b in S(omega)` by

\[
Q_\theta(d\omega,b)
=
\frac{\mathbf 1_{C_b(\omega)}N(\omega)^{-\theta}}
{Z_\theta}\,\mu_p(d\omega),
\tag{2.1}
\]

where

\[
Z_\theta
=
\sum_{b\in B}\mathbb E[\mathbf 1_{C_b}N^{-\theta}]
=
\mathbb E[N^{1-\theta};C].
\tag{2.2}
\]

All powers are harmless because `N>=1` on every `C_b`.

### Endpoint theta=0: the connection-Palm / contact-size-biased law

At `theta=0`,

\[
Z_0=\mathbb E N.
\]

The pair law first weights boundary labels by their connection probabilities and then samples the configuration conditional on that label being connected. Therefore, with the pair observable

\[
Q(\omega,b):=q_b(\omega),
\]

Harris--FKG gives

\[
\begin{aligned}
\mathbb E_{Q_0} Q
&=
\frac{\sum_b \mathbb E[\mathbf 1_{C_b}q_b]}{\mathbb E N}\\
&\le
\frac{\sum_b \mathbb P(C_b)\mathbb E q_b}{\mathbb E N}\\
&\le\varepsilon.
\end{aligned}
\tag{2.3}
\]

The inequality uses that `C_b` is increasing and `q_b` is decreasing.

### Endpoint theta=1: the source-conditioned uniform-contact law

At `theta=1`,

\[
Z_1=\mathbb P(C),
\]

and the configuration marginal of `Q_1` is exactly `mu_p(.|C)`; conditional on a configuration, `b` is uniform on `S(omega)`. Thus

\[
\mathbb E_{Q_1} Q
=
\mathbb E\!\left[
\frac1N\sum_{b\in S}q_b\,\middle|\,C
\right].
\tag{2.4}
\]

Since a minimum is at most an average,

\[
\boxed{
R\le \mathbb E_{Q_1}Q.
}
\tag{2.5}
\]

The two endpoint laws have the exact Radon--Nikodym derivative

\[
\boxed{
\frac{dQ_1}{dQ_0}(\omega,b)=\frac{M}{N(\omega)}.
}
\tag{2.6}
\]

Indeed `Z_0/Z_1=M`.

This is the central structural identity of the run: the entire gap between the easy FKG estimate (2.3) and the source-adaptive quantity (2.4) is **size debiasing by `M/N`**. Large-contact configurations are downweighted; anomalously small-contact configurations are amplified.

### Differential identity

Because the state space is finite, differentiation under the sum is exact. From (2.2),

\[
\frac{d}{d\theta}\log Z_\theta
=
-\mathbb E_{Q_\theta}\log N.
\tag{2.7}
\]

For

\[
r(\theta):=\mathbb E_{Q_\theta}Q,
\]

quotient differentiation gives

\[
\boxed{
r'(\theta)
=
-\operatorname{Cov}_{Q_\theta}(Q,\log N).
}
\tag{2.8}
\]

Thus a full proof along this interpolation would follow from a dimension-free control of the integrated covariance

\[
-\int_0^1
\operatorname{Cov}_{Q_\theta}(Q,\log N)\,d\theta.
\tag{2.9}
\]

This is a substantially sharper target than “control arbitrary non-cluster-local information”: it isolates exactly how much adaptive selection can be gained by moving from a contact-size-biased law to a uniform-contact law.

No sign is claimed in (2.8). `Q_theta` is not a product measure, and I did not find a valid FKG argument giving the covariance a fixed sign.

## 3. Method #13 — a whole Harris hierarchy, not only the first contact moment

The quantity `N` itself is pointwise increasing as edges are opened. More importantly, every factorial contact moment admits the same `epsilon` contraction on the failure kernel.

### Theorem 3.1 — factorial Harris hierarchy

For every integer `k>=1`,

\[
\boxed{
\mathbb E\!\left[\binom Nk\,m\right]
\le
\varepsilon\,\mathbb E\binom Nk.
}
\tag{3.1}
\]

#### Proof

For a fixed `k`-element subset `A subseteq B`, let

\[
C_A:=\bigcap_{b\in A}C_b.
\]

This is increasing. Define

\[
q_A:=\min_{b\in A}q_b.
\]

This is decreasing and satisfies

\[
\mathbb E q_A
\le \min_{b\in A}\mathbb E q_b
\le\varepsilon.
\tag{3.2}
\]

If all labels in `A` are connected, then `A subseteq S` and therefore

\[
m=\min_{b\in S}q_b
\le \min_{b\in A}q_b=q_A.
\]

Hence Harris--FKG for the increasing indicator `1_{C_A}` and the decreasing function `q_A` gives

\[
\mathbb E[\mathbf 1_{C_A}m]
\le
\mathbb E[\mathbf 1_{C_A}q_A]
\le
\mathbb P(C_A)\,\mathbb E q_A
\le
\varepsilon\,\mathbb P(C_A).
\tag{3.3}
\]

Summing (3.3) over all `k`-subsets `A` and using

\[
\sum_{|A|=k}\mathbf 1_{C_A}=\binom Nk
\]

proves (3.1). QED.

For `k=1`, this is the exact weighted first-moment inequality

\[
\boxed{
\mathbb E[Nm]\le\varepsilon\,\mathbb E N.
}
\tag{3.4}
\]

The same proof works for every nonnegative linear combination of the binomial basis. Thus if

\[
W(n)=\sum_{k\ge1}a_k\binom nk,\qquad a_k\ge0,
\]

then

\[
\mathbb E[W(N)m]\le\varepsilon\,\mathbb E W(N).
\tag{3.5}
\]

### What only increases, and what does not

`N` and every `binom(N,k)` only increase under edge opening. The endpoint density `M/N` in (2.6) only decreases as `N` increases. This identifies the exact direction in which the source-adaptive law can amplify failure: it favors the lowest-contact part of the percolation space.

What I could **not** prove is that this decreasing density and the decreasing kernels `q_b` produce a useful signed covariance under the intermediate pair law `Q_theta`. That law already contains the connectivity support and the factor `N^{-theta}`, so ordinary product-measure Harris--FKG does not apply. The factorial hierarchy (3.1) is therefore a rigorous substitute for a nonexistent blanket covariance-sign claim.

## 4. Method #28 — replace “all configurations” by a quantified typical-contact statement

The endpoint identity (2.6) and the `k=1` member (3.4) give a clean, source-valid lower-tail reduction.

### Theorem 4.1 — exact contact lower-tail bound

For every `a>0`,

\[
\boxed{
R
\le
\mathbb P\!\left(N\le aM\,\middle|\,C\right)
+\frac{\varepsilon}{a}.
}
\tag{4.1}
\]

Equivalently,

\[
\boxed{
R
\le
\inf_{a>0}
\left\{
\mathbb P(N\le a\,\mathbb E[N\mid C]\mid C)
+\frac{\varepsilon}{a}
\right\}.
}
\tag{4.2}
\]

#### Proof 1: directly from the failure kernel

Split according to whether `N<=aM`:

\[
\mathbb E m
\le
\mathbb P(C,N\le aM)
+
\mathbb E[m;N>aM].
\tag{4.3}
\]

On `{N>aM}`,

\[
m\le \frac{Nm}{aM}.
\]

Therefore by (3.4),

\[
\mathbb E[m;N>aM]
\le
\frac{\mathbb E[Nm]}{aM}
\le
\frac{\varepsilon\,\mathbb E N}{aM}
=
\frac{\varepsilon}{a}\,\mathbb P(C).
\tag{4.4}
\]

Divide (4.3) by `P(C)`. QED.

#### Proof 2: change of measure

From (2.5)--(2.6),

\[
R
\le
\mathbb E_{Q_0}\!\left[\frac{M}{N}Q\right].
\]

On `{N<=aM}`, bound the contribution after changing back to `Q_1` by its `Q_1` probability, which is exactly `P(N<=aM|C)`. On `{N>aM}`, `M/N<1/a`, and (2.3) gives a contribution at most `epsilon/a`. This proves (4.1) again.

### Particularly simple choice

Taking `a=sqrt(epsilon)` yields

\[
\boxed{
R
\le
\sqrt{\varepsilon}
+
\mathbb P\!\left(
N\le\sqrt{\varepsilon}\,\mathbb E[N\mid C]
\,\middle|\,C
\right).
}
\tag{4.5}
\]

Thus any counterexample sequence with failure ratio bounded below by a constant must put nonvanishing conditional mass on configurations whose number of connected boundary vertices is an `O(sqrt(epsilon))` fraction of its conditional mean.

More generally, for a sequence of source instances with `epsilon_j->0`, the conjectured conclusion follows along that sequence whenever there are `a_j>0` such that

\[
\frac{\varepsilon_j}{a_j}\to0
\quad\text{and}\quad
\mathbb P(N_j\le a_jM_j\mid C_j)\to0.
\tag{4.6}
\]

This permits `M_j->infinity`; it is strictly different from the old bounded-contact estimate `R<=epsilon M`.

### Failure-biased necessary condition for any genuine counterexample

Let `nu` be the failure-weighted law on connected configurations,

\[
\nu(d\omega)
=
\frac{m(\omega)}{R\,\mathbb P(C)}\,\mu_p(d\omega).
\]

Then (3.1) implies, for every `k>=1`,

\[
\boxed{
\mathbb E_\nu\binom Nk
\le
\frac{\varepsilon}{R}
\mathbb E\!\left[\binom Nk\mid C\right].
}
\tag{4.7}
\]

In particular,

\[
\mathbb E_\nu N
\le
\frac{\varepsilon}{R}M.
\tag{4.8}
\]

Hence if `R>=r>0`, then since `N>=1` under `nu`,

\[
M\ge \frac r\varepsilon.
\tag{4.9}
\]

This recovers the old first-moment obstruction, but (4.7) shows that **all factorial contact moments** of the failure-biased law must be suppressed by the same `epsilon/R` factor.

## 5. Why this still does not move the full metric

The new bounds reduce the unrestricted problem to a much narrower phenomenon, but they do not rule it out.

A full source proof would follow from any universal estimate forcing

\[
\mathbb P(N\le a(\varepsilon)M\mid C)=o(1)
\]

for some `a(epsilon)` with `epsilon/a(epsilon)->0`. I do not have such an estimate.

It would also be incorrect to assume ordinary concentration of `N|C`. Connectivity architectures with common gates and private routes can create genuinely multi-scale contact counts. The present run has not proved a source-valid universal lower-tail estimate, and I do not relabel the reduction as one.

The exact obstruction can now be stated in one sentence:

> **The full conjecture can fail only if the source-adaptive failure kernel concentrates on a lower-contact tail strong enough to overcome the exact `epsilon` Harris contraction under the contact-size-biased Palm law.**

This statement is rigorous in the quantitative form (4.1)--(4.8), but it is not yet a contradiction.

The factorial hierarchy also explains why simply taking higher contact moments does not immediately close the gap: a counterexample may put its failure mass on configurations with `N` below the scale where a chosen high factorial moment is informative. A successful next argument must either control that lower tail from connectivity structure or construct a counterexample exploiting it.

## 6. Relation to C073 and to the nearest solved-looking gluing machinery

C073 showed that genuinely cluster-local source observables satisfy the stronger linear modulus `1-epsilon` using the max-envelope plus the mechanically checked GEN/first-relay theorem in

`anthropics/formal-math @ 795efb86f191735c5481675763537cfb4ff37e55`.

I rechecked the pinned theorem signature during this run. It is explicitly a theorem for monotone nonnegative **cluster functionals** and does not apply directly to arbitrary edge-cube kernels `q_b`. The current contact-size analysis therefore does not silently extend GEN beyond its formalized hypotheses.

The two mechanisms are complementary:

1. C073 controls heterogeneous observables when all relevant information is in the connected cluster.
2. C074 controls arbitrary source observables unless failure is concentrated on abnormally small contact multiplicity.

Their intersection is broad, but neither contains all source instances.

## 7. Method-by-method outcome

### #5 ADD A PARAMETER AND DIFFERENTIATE

**Succeeded as a new exact reformulation, not as closure.**

The interpolation `Q_theta` gives the endpoint density `M/N` and the derivative identity

\[
r'(\theta)=-\operatorname{Cov}_{Q_\theta}(q_B,\log N).
\]

This isolates the only amplification mechanism between easy per-label FKG control and the source-adaptive uniform-contact law.

### #13 FIND WHAT ONLY INCREASES

**Succeeded partially.**

`N` and all factorial contact counts `binom(N,k)` are increasing. Harris--FKG yields the full hierarchy (3.1), not merely the previously used first-contact estimate. The tempting stronger claim that `r(theta)` is monotone was **not** established; the intermediate `Q_theta` laws are not product measures, so no covariance sign is asserted.

### #28 REPLACE "FOR ALL" WITH "FOR TYPICAL"

**Succeeded as a sharp quantitative restricted reduction.**

Equation (4.1) proves that one only needs to understand the lower tail of `N|C`. In particular (4.5) gives a universal per-instance bound by `sqrt(epsilon)` plus the probability of an exceptionally low-contact configuration. This works for the full source event class, not only cluster-local observables.

## 8. Next route

The strict source metric did not move, so G0004 remains OPEN / PARTIAL and the HARD recovery counter remains `1/2`.

Do not repeat #5/#13/#28. The next fresh G0004 triple is reserved as:

- **#10 DERANDOMIZE:** replace the uniform random connected-label viewpoint by an explicit deterministic selector/weight built from contact multiplicity, while avoiding the monotone-partition obstruction already found by R7-02;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** compare the `Q_0 -> Q_1` size-debiasing problem with Palm-to-typical-point changes of measure, adaptive multiple testing, and correlation-gap inequalities, looking specifically for a theorem controlling a rare decreasing score after inverse-size debiasing;
- **#26 HUNT THE SPORADIC CASE:** attack the covariance/sign and lower-tail bottleneck on the smallest non-star graphs with shared gates/cycles, seeking either an exact counterexample to a plausible strengthening or a pattern that can be proved.

The mathematical target for the next run is now precise: either prove a universal connectivity-specific bound on the lower-contact tail appearing in (4.1), or exhibit an exact family showing that such a bound is false and identify what extra statistic beyond `N` must enter.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R17
  source_id: G0004
  source: "Lucas Flammant, arXiv:2609.03492, Conjecture 2.2"
  status_before: "OPEN / PARTIAL / STUCK RECOVERY 1/2"
  status_after: "OPEN / PARTIAL / STUCK RECOVERY 1/2"
  metric: U_F
  value_before: 1
  value_after: 1
  movement: "NO SOURCE-METRIC MOVEMENT"
  methods_attempted: [5, 13, 28]
  recovery_count_before: "1/2"
  recovery_count_after: "1/2"
  new_exact_reformulation:
    name: "contact-size debiasing interpolation"
    endpoint_easy: "Q0, contact-size-biased/Palm; E_Q0 q_B <= epsilon"
    endpoint_source: "Q1, configuration conditioned on C and uniform b in S"
    RN_derivative: "dQ1/dQ0 = M/N"
    derivative: "r'(theta) = -Cov_Qtheta(q_B, log N)"
  new_theorem:
    name: "factorial Harris hierarchy"
    statement: "E[binom(N,k) m] <= epsilon E[binom(N,k)] for every k>=1"
  new_reduction:
    name: "contact lower-tail bound"
    statement: "R <= inf_{a>0}{ P(N<=aM | C) + epsilon/a }"
    corollary: "R <= sqrt(epsilon) + P(N<=sqrt(epsilon) M | C)"
  source_scope: "full arbitrary finite-graph / arbitrary source-observable class; reduction only, not closure"
  predecessor_binary_lcs_width: 0.033609950762282626
  predecessor_d0064_R_class: "0/3"
  next_methods: [10, 21, 26]
  finite_checker_created: false
  checker_reason: "No finite numerical claim was used; all new claims are proved symbolically in this report."
  shared_root_edits: none
  peer_file_edits: none
  email_drive_public_scheduler_permission_workflow_actions: none
```

## 10. Model / scheduler control

The exposed scheduler surface still does not provide a bindable model-family selector, reasoning-effort selector, or authenticated runtime-model telemetry. Therefore `GPT-6 / maximum` remains a prompt request rather than an enforceable scheduler setting in this environment. This run actually identifies as **GPT-5.6 Sol** with reasoning level **UNVERIFIED**, and does not claim otherwise.

The historical P26 `"You cannot modify this task"` result is an authorization-context restriction. The repository records that P26 was later updated from another authorized context. The legitimate remedies remain the owning/admin-authorized scheduler surface or platform support; duplicating the task, changing repository text as a substitute for a native scheduler edit, or bypassing permissions is not permitted.

No shared root, canonical claim, peer file, email, Drive item, public posting, scheduler configuration, workflow, purchase, or permission was changed in this run.
