Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed automation/runtime surface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen metric: `S=5 -> 5`. Methods tried: B2, B6, B13.**

# HARD7-02 run 13 — complexified gauge stress test and the logarithmic-mean law on the full axis cone

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question remains OPEN in bounded current-status search.**

This run deliberately did not manufacture a sixth checker-style metric unit. Instead it attacked a natural strengthening of the run-4 relative-phase gauge theorem: whether the invisible opposite-coordinate `U(1)` action can be enlarged to the reciprocal complex scaling action `C^*`, `(z,w) -> (lambda z,lambda^{-1}w)`. The answer is **no**, already on the completely solved axis class. In fact the failure is exact and admits a closed formula in terms of the logarithmic mean. This identifies the run-4 unitary gauge as the maximal **universal** invisible subgroup inside that reciprocal `C^*` action on the axis family, modulo the already known discrete transpose symmetry.

The same calculation upgrades the preceding probability-axis formula to every finite C2 axis measure `A delta_(1,0)+B delta_(0,1)`, and it gives a strict one-dimensional monotone parameter along every positive reciprocal-amplitude orbit. The full source question is not closed: the next genuinely new class is an interior, swap-symmetric two-orbit quotient family recorded in Section 10.

## 1. Continuity, repository state, ownership, source, and neighboring work

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T08-18-00Z__complete-axis-support-classification.md`.

At run start I re-read the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the HARD7-02 report chain and canonical claim;
- the heavy-tail neighborhood in the `probability_1000_intake_*/problems.jsonl` material through repository search;
- the newest neighboring heavy-tail records, including the R7-06/C0032 explicit-density track and the C0031 ownership/history entries.

A fresh repository claim search still records Campbell–O'Rourke Question 1.8 as owned by HARD7-02. C0031 and C0032 are distinct Bordenave–Chafaï iid heavy-tail questions and are not aliases of this dependence-classification target. No release, collision, posted equivalent, Bernoulli-singularity reassignment, or excluded owner-manuscript collision was found.

The newest neighboring R7-06 record continues to study the explicit all-radius density of the iid Bordenave–Caputo–Chafaï law; it does not classify `theta_d`. The newest R7-05 record has already moved to a different outside target, P0336, so no theorem from that track is imported here.

### Primary source and current-status refresh

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3`.

Primary links:

- https://arxiv.org/abs/2010.01261
- https://arxiv.org/html/2010.01261v3
- https://doi.org/10.1214/22-EJP849

The live arXiv record checked on 2026-09-19 still lists v3, revised 2 February 2022, as the latest version. The source's Condition C1 uses a finite angular measure `theta_d` on the unit sphere of `C^2`; Condition C2 adds the no-complex-hyperplane support condition and the asymptotic normalization `a_n/n^(1/alpha) -> c>0`. Theorem 1.6 gives the deterministic limiting ESD `mu_{alpha,theta_d}`. Section 1.3 still asks exactly:

> **Question 1.8.** What properties of `theta_d` determine `mu_{alpha,theta_d}`?

A fresh bounded literature search dated 2026-09-19 used the exact title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, dependence measure, PWIT, classification, gauge, scaling, and 2023--2026 terms. It recovered the 2022 source and later Campbell–O'Rourke work on Lévy–Khintchine random Laplacian matrices, but no located paper claiming a full solution of Question 1.8 or the reciprocal-scaling calculation below. This is **bounded negative evidence only**, not a worldwide novelty certificate.

### Runtime/scheduler capability

The exposed automation interface still does not provide a binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. Therefore this worker cannot enforce GPT-6/maximum despite the prompt request; changing that would require a platform surface that actually exposes authenticated model/effort controls. The current root ledger also records that historical `You cannot modify this task` failures are context-specific: P26 was later editable in another authorized native context. For a task that still refuses modification, the compliant workaround remains the authorized owner/account/workspace interface or platform support/ownership transfer, not a permission bypass or duplicate schedule. No scheduler modification was attempted here.

## 2. Frozen metric and Section-I bookkeeping

The canonical claim freezes

`S = number of exact nontrivial full-source transformation laws theta_d -> mu_{alpha,theta_d}`

counted under the claim's established rule.

Before this run: `S=5`.

After this run: **`S=5` — no movement.**

The new formula below is source-level mathematics but is derived by combining the already verified run-6 mass homogeneity with the run-11/12 axis law. It is therefore not relabeled as a sixth independent metric unit.

The first Section-I recovery episode has already been used (`STUCK1`, followed by its axis-family recovery execution). The preceding run was the first ordinary post-recovery no-movement run. This is the **second ordinary post-recovery no-movement run**. Thus no STUCK2 report is written prematurely here; if the ordinary unchanged streak reaches the controlling threshold on a later execution, the next run must obey Section I rather than append another auxiliary lemma.

All thirty Section-B numbers have already appeared somewhere in the HARD7-02 chain, so literal globally never-before-used numbering is exhausted. I rotate to a triple different from the immediately preceding B14/B24/B29 and apply it to a genuinely new deformation:

**B2 / B6 / B13.**

## 3. Idea before code: can the unitary tree gauge be complexified?

Run 4 proved that

`g_phi(z,w)=(e^(i phi) z, e^(-i phi) w)`

is invisible to the limiting ESD. On the corrected local tree this is an exact diagonal **unitary** gauge. A tempting stronger guess is that acyclicity might allow the whole reciprocal complex group

`G_lambda(z,w)=(lambda z, lambda^(-1) w)`, `lambda in C^*`,

to be invisible as well, because a finite tree can absorb reciprocal edge factors by diagonal similarity even when the diagonal gauge is nonunitary.

That stronger guess is dangerous: Hermitization is invariant under unitary conjugacy, not arbitrary nonunitary similarity. Rather than trying to prove the stronger statement, this run attacks it first on the exact axis class where the output law is already known.

The result is decisive. The phase part of `lambda` is invisible, exactly as run 4 says, but its modulus changes the heavy-tail angular masses and generally changes the limiting ESD. The failure can be measured exactly.

No code was written until this deformation and its closed formula had been derived. The archived script is only the final exact-algebra self-check.

## 4. Raw axis measures: the logarithmic-mean formula

For `A,B>0`, define the finite axis measure

`Theta_(A,B) = A delta_(1,0) + B delta_(0,1)`.

Its support contains both coordinate axes, so the C2 hyperplane obstruction is absent. Put

`m=A+B`, `p=A/m`, `q=B/m`.

Then

`Theta_(A,B) = m theta_p`,

where `theta_p=p delta_(1,0)+q delta_(0,1)` is the probability-axis measure from runs 11--12.

Run 6 proved mass homogeneity:

`mu_(alpha, m theta) = D_(m^(1/alpha)) # mu_(alpha,theta)`.

Runs 11--12 proved for the probability-axis family

`mu_(alpha,theta_p)=D_(k_(alpha,p)) # mu_alpha`,

with

`k_(alpha,p)^alpha = 2(p-q)/log(p/q)`,

understood continuously at `p=q=1/2`.

Combining the two statements gives a cleaner formula that had not been isolated in the preceding reports.

### Theorem 1 — full finite axis cone

For every `A,B>0`,

\[
\boxed{
\mu_{\alpha,\Theta_{A,B}}
=(D_{\kappa_\alpha(A,B)})_\#\mu_\alpha,
\qquad
\kappa_\alpha(A,B)^\alpha
=\frac{2(A-B)}{\log A-\log B}.
}
\]

At `A=B` the continuous value is

\[
\kappa_\alpha(A,A)^\alpha=2A.
\]

Equivalently, with the logarithmic mean

\[
L(A,B):=\frac{A-B}{\log A-\log B},\qquad L(A,A)=A,
\]

we have the compact identity

\[
\boxed{\kappa_\alpha(A,B)^\alpha=2L(A,B).}
\]

#### Proof

By mass homogeneity and the probability-axis law,

\[
\kappa_\alpha(A,B)^\alpha
=m k_{\alpha,p}^\alpha
=(A+B)\frac{2(2p-1)}{\log(p/(1-p))}.
\]

Since

`2p-1=(A-B)/(A+B)`

and

`p/(1-p)=A/B`,

the displayed expression reduces exactly to

`2(A-B)/log(A/B)`.

The equal-mass value follows by continuity. `QED`

This theorem is not counted as new metric movement because its two ingredients were already established. Its value is that it puts the complete axis cone in a standard scalar mean and makes the next deformation transparent.

## 5. B2 — attack the negation: an exact failure of `C^*` gauge invariance

Let `r>0` and transform the off-diagonal atom pair by the invertible linear map

\[
L_r(z,w)=(rz,r^{-1}w).
\]

The correct transformation of a regular-variation angular measure is not just naive pushforward on the unit sphere, because `L_r` changes radial size. If

\[
\nu_\theta(dt,d\omega)=\alpha t^{-1-\alpha}dt\,\theta(d\omega)
\]

is the tail measure, then the mapping theorem gives `L_r#nu_theta`. Re-polarizing gives the angular measure

\[
\boxed{
(\mathcal T_r\theta)(E)
=\int \|L_r\omega\|^\alpha
\mathbf 1\!\left\{\frac{L_r\omega}{\|L_r\omega\|}\in E\right\}
\theta(d\omega).
}
\]

Indeed, for `s=t ||L_r omega||`, the radial density picks up the factor `||L_r omega||^alpha`. Because `L_r` is invertible, C2(i) is preserved; the same `a_n` keeps C2(ii), and leaving the diagonal atom unchanged preserves the diagonal-tail hypothesis.

For the probability-axis family this becomes especially simple:

\[
\mathcal T_r\theta_p
= p r^\alpha\,\delta_{(1,0)}
 +(1-p)r^{-\alpha}\,\delta_{(0,1)}.
\]

Thus Theorem 1 gives immediately

\[
\boxed{
\mu_{\alpha,\mathcal T_r\theta_p}
=(D_{\kappa_{p}(r)})_\#\mu_\alpha,
\quad
\kappa_p(r)^\alpha
=2L\bigl(p r^\alpha,(1-p)r^{-\alpha}\bigr).
}
\tag{5.1}
\]

This already disproves the tempting stronger gauge statement.

### Exact interior counterexample

Take

`alpha=1`, `p=1/4`, `r=2`.

Before deformation,

\[
\kappa_{1/4}(1)=\frac1{\log 3}.
\]

After deformation the raw axis masses are

`A=1/2`, `B=3/8`,

so

\[
\kappa_{1/4}(2)=\frac{1}{4\log(4/3)}.
\]

These are **exactly unequal**. Equality would imply

\[
\log 3=4\log(4/3)=\log((4/3)^4),
\]

hence

`3=256/81`, i.e. `243=256`, a contradiction.

Numerically only for orientation,

`1/log 3 = 0.9102392266...`,

while

`1/(4 log(4/3)) = 0.8690148742...`.

This is not a finite-size simulation and does not refute Question 1.8, which is a question. It refutes only the stronger candidate principle that the run-4 reciprocal phase gauge extends from `U(1)` to all positive reciprocal amplitudes.

**B2 outcome: succeeded.** The nonunitary extension fails on a fully source-valid interior C2 family, with an exact output-level witness.

## 6. B6 — deform through the entire reciprocal-amplitude orbit

The preceding witness is more informative when `r` remains symbolic.

Write `q=1-p`. Because

\[
A(r)=p r^\alpha,\qquad B(r)=q r^{-\alpha},
\]

the product is conserved:

\[
A(r)B(r)=pq.
\]

Equation (5.1) therefore solves the entire positive reciprocal-amplitude deformation at the source-output level.

For a complex `lambda != 0`, write `lambda=r e^{i phi}`. Its opposite phases are invisible by run 4, so the same formula depends only on `r=|lambda|`. Thus on the axis class the full reciprocal `C^*` action is explicitly decomposed into

1. an invisible `U(1)` phase gauge;
2. a positive-amplitude motion along the fixed-product hyperbola `(A,B)=(p r^alpha,q r^(-alpha))`.

The second motion is not invisible in general.

A useful exceptional point is

\[
r^\alpha=q/p.
\]

Then

\[
A=q,\qquad B=p,
\]

so the transformation simply exchanges the two axis masses. The output is therefore equal to the original law by transpose symmetry. This is not a new continuous gauge freedom; it is exactly the already counted discrete coordinate swap appearing at one modulus depending on `p`.

For the test point `p=1/4`, `alpha=1`, the swap modulus is `r=3`. Thus the same deformation that genuinely changes the law at `r=2` returns to the original output at `r=3` by reaching the swapped input.

**B6 outcome: succeeded.** The entire deformation is solved exactly on the axis cone, not just sampled at one parameter.

## 7. B13 — find what only increases: strict monotonicity on the fixed-product hyperbola

Set

\[
g=\sqrt{pq},
\qquad
s(r)=\frac12\log\frac{p}{q}+\alpha\log r.
\]

Then

\[
A(r)=g e^{s(r)},\qquad B(r)=g e^{-s(r)}.
\]

The logarithmic mean becomes

\[
L(A(r),B(r))
=g\frac{\sinh s(r)}{s(r)},
\]

so

\[
\boxed{
\kappa_p(r)^\alpha
=2\sqrt{pq}\,\frac{\sinh s(r)}{s(r)}.
}
\tag{7.1}
\]

The function

\[
F(s)=\frac{\sinh s}{s},\qquad F(0)=1,
\]

is even and strictly increasing in `|s|`. For `s>0`,

\[
F'(s)=\frac{s\cosh s-\sinh s}{s^2},
\]

and if `h(s)=s cosh s-sinh s`, then

\[
h(0)=0,\qquad h'(s)=s\sinh s>0.
\]

Therefore `h(s)>0` and `F'(s)>0` for every `s>0`.

This gives three exact consequences.

### Corollary 2 — complete equality classification along the reciprocal orbit

Let

`s_0=(1/2) log(p/q)`.

Then

\[
\mu_{\alpha,\mathcal T_r\theta_p}
=\mu_{\alpha,\theta_p}
\]

if and only if

\[
|s_0+\alpha\log r|=|s_0|.
\]

Hence the only possibilities are

\[
\boxed{r=1\quad\text{or}\quad r^\alpha=q/p.}
\]

The first is the identity modulus; the second is exactly the transpose/swap point. No other positive reciprocal amplitude is spectrally invisible on this axis family.

The implication from unequal scale to unequal output uses only that the Bordenave–Caputo–Chafaï law `mu_alpha` is a nondegenerate probability measure. A nondegenerate probability measure cannot be invariant under a fixed nontrivial dilation: the standard disjoint-annulus argument would otherwise force all mass outside zero to vanish.

### Corollary 3 — unique balance point and exact minimum

The unique minimum occurs at `s(r)=0`, equivalently

\[
\boxed{r_{\rm bal}^\alpha=\sqrt{q/p}.}
\]

At this point the transformed raw masses are equal:

\[
A=B=\sqrt{pq},
\]

and

\[
\boxed{\min_{r>0}\kappa_p(r)^\alpha=2\sqrt{pq}.}
\]

For `alpha=1,p=1/4`, this gives `r_bal=sqrt(3)` and minimum scale `sqrt(3)/2`.

There is no contradiction with run 12's statement that the balanced **probability** axis law maximizes radial scale at fixed total mass. The present reciprocal deformation fixes the product `AB=pq`, not the sum `A+B`. The logarithmic mean satisfies

\[
\sqrt{AB}\le L(A,B)\le \frac{A+B}{2},
\]

so balance is the minimum under fixed product and the maximum under fixed sum.

### Corollary 4 — maximal universal reciprocal gauge on the axis class

Consider the reciprocal complex action

`G_lambda(z,w)=(lambda z,lambda^(-1)w)`.

For `|lambda|=1`, run 4 proves invisibility for every C2 dependence measure, hence in particular for every axis law. Conversely, if `|lambda|=r != 1`, Corollary 2 shows that invisibility on `theta_p` would require `r^alpha=(1-p)/p`, which cannot hold for every `p in (0,1)`. Therefore:

\[
\boxed{\text{within the reciprocal }C^*\text{ action, the universal invisible subgroup on the axis family is exactly }U(1).}
\]

The only extra equality for a fixed `p` is the already known discrete transpose point.

**B13 outcome: succeeded.** The deformation has a strict scalar monovariant `|s|` through `sinh(s)/s`; there are no hidden additional equality points.

## 8. Exact self-check, after the mathematics

Only after deriving the formulas above I ran a small exact symbolic self-check. It verifies:

1. the algebra combining mass homogeneity with the probability-axis law;
2. the hyperbolic reparameterization of the logarithmic mean;
3. the exact `243 != 256` counterexample certificate at `alpha=1,p=1/4,r=2`;
4. the exact swap point `r^alpha=3` for that test case;
5. the exact balance point `r^alpha=sqrt(3)`.

Artifacts:

- code: `artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T09-12-00Z__axis-cstar-logmean-check.py` at commit `efa696a9af26f7d918f0f73bb252ed6b18a4cbfe`;
- output: `artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T09-12-00Z__axis-cstar-logmean-check.out` at commit `51efea421777b69de07190d596bc0d51ffbc159c`.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit and not a closure certificate.

## 9. What this changes about Question 1.8

The axis class is now understood at three compatible levels:

1. run 4: arbitrary phase statistics along an axis are invisible after the `q(z,w)=(|z|^2,zw)` quotient;
2. runs 11--12: for probability axis measures, the unordered axis masses determine the full limiting ESD through one dilation factor;
3. this run: for arbitrary finite axis masses, the exact output scale is twice the logarithmic mean at the `alpha`-power level, and reciprocal amplitude changes this scale strictly except at identity or transpose.

So the first coordinate of the `q` quotient is not merely a bookkeeping artifact: even after keeping the edge product fixed at zero, redistributing radial tail mass between the two coordinate directions changes the full source-level ESD. The unitary phase gauge can be removed; the corresponding nonunitary amplitude degree of freedom cannot.

This still does **not** prove that the run-4 `q#theta` statistic is minimal for general dependence measures. It proves only that one tempting further quotient—complexifying the relative-phase gauge—fails exactly on the simplest fully solved class.

No claim is made that the logarithmic-mean mechanism is independently publication-novel. It is derived from the preceding HARD7-02 theorems plus standard regular-variation mapping and classical logarithmic-mean algebra. The source itself and Bordenave–Caputo–Chafaï remain the cited prior art for the underlying heavy-tail limits.

## 10. The next genuinely new source class

The axis class should now be left rather than polished again. A minimal interior family survives all the reductions already proved and avoids the asymmetric-rank complication.

For `0<x<=1/2`, let `eta_x` be the Haar relative-phase orbit law of

\[
\left(\sqrt{x}e^{i\phi},\sqrt{1-x}e^{-i\phi}\right),
\qquad \phi\sim\mathrm{Unif}[0,2\pi),
\]

and define the swap-symmetric probability measure

\[
\vartheta_x=\frac12\bigl(\eta_x+\tau_\#\eta_x\bigr).
\]

Its run-4 quotient is exactly the two-point interior law

\[
q_\#\vartheta_x
=\frac12\delta_{(x,\sqrt{x(1-x)})}
 +\frac12\delta_{(1-x,\sqrt{x(1-x)})}.
\]

For `x=1/2` this is the complex-Hermitian orbit. As `x` tends toward the axis boundary, the dependence measure approaches the balanced-axis geometry at the level of angular support. No continuity of the output law is asserted here; that would require proof.

This is the smallest next family with all of the following advantages:

- it lies genuinely off the axes for `0<x<1/2`;
- it is swap symmetric, so the asymmetric rank-marked obstruction from runs 2--3 disappears and the source's homogeneous PWIT route is available;
- relative phases have already been quotiented exactly;
- its `q` statistic has only two atoms and one scalar parameter;
- its endpoints connect the two canonical source geometries: Hermitian and iid-axis.

The next ordinary research run should attack an **output-level** statistic for `vartheta_x`, preferably the regularized Hermitized root resolvent or logarithmic potential at `z=0`, and try first to show that it is nonconstant in `x`. A finite-tree eigenvalue identity, simulation, or product-only argument is not enough.

If the frozen metric remains unchanged through the controlling Section-I threshold, the next required run is STUCK2 rather than another axis calculation.

## 11. Closure / audit state

Question 1.8 is **not closed**. No paper folder is created. No independent audit is requested because the source question remains partial and the new result is an internal structural step, not a claimed closure.

No shared root ledger was edited. The coordinator/P26 shared-ledger ownership rule is preserved.

```yaml
ledger_delta:
  track: HARD7-02
  source: Campbell-O'Rourke 2022 Question 1.8
  metric: S
  before: 5
  after: 5
  movement: false
  status: PARTIAL
  source_status: OPEN_IN_BOUNDED_2026-09-19_SEARCH
  methods: [B2, B6, B13]
  post_STUCK1_ordinary_unchanged_count_before: 1
  post_STUCK1_ordinary_unchanged_count_after: 2
  hard_stuck_recoveries_used: 1
  hard_stuck_recoveries_allowed: 2
  new_result: "Raw axis scale is kappa^alpha=2 L(A,B); reciprocal C* amplitude is non-invariant except identity/swap; universal invisible reciprocal subgroup on axis family is U(1)."
  next_object: "swap-symmetric two-orbit interior quotient family vartheta_x"
  closure: false
```
