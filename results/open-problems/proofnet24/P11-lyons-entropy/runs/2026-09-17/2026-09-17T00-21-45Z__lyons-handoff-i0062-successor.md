Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. GPT-6 / maximum was requested, but the exposed scheduler/runtime provides no model selector, reasoning-effort selector, or authenticated effort telemetry; I therefore do not claim GPT-6 or maximum reasoning.

Problem/source: Russell Lyons (2014), *Determinantal Probability: Basic Properties and Conjectures*, arXiv:1406.2707, Conjecture 2.6 — mandatory P11 handoff after the third HARD-target stuck trigger; successor admitted this run: Antonio Auffinger, Michael Damron, Jack Hanson, *50 years of first-passage percolation*, arXiv:1511.03262, Question 36. New-method moves on the successor: **B2 attack the negation first, B18 say it in another language, B30 do one scale/direction at a time.**

# P11 transition report — Lyons/X095 handoff and I0062 maximal-flow successor

Run date: 2026-09-17 UTC.

## 1. Executive status

### Lyons / X095

The three-site Lyons milestone remains **PARTIAL / HANDOFF**, not PROVED and not REFUTED. The frozen Lyons metric remains

`B_Phi = certified global lower bound for the exact X095 scalar Phi on the complete admissible three-site domain = UNMEASURED`.

There is no new Lyons lemma in this run. The previous P11 report, `proofnet24/P11-lyons-entropy/runs/2026-09-16/2026-09-16T23-18-48Z__run-report.md`, explicitly recorded the third-stuck mandatory handoff. Returning to another local X095 lemma would violate the owner's HARD-target rotation rule.

### Successor I0062

A create-only canonical claim was admitted for

**I0062 — Auffinger–Damron–Hanson, Question 36: maximal-flow law of large numbers without the exponential-moment assumption.**

Canonical claim:

`operations/claims/I0062.md`

creation commit `ed9ecb3d7204e8d6c4e8124d75e46bb8e5fc603c`, blob `de34fae1df554ead407d7bbc3d1088a6378153b1`.

New frozen successor metric:

`Q36_global_bracket = number of the two a.s. inequalities {liminf normalized flow >= nu_G, limsup normalized flow <= nu_G} proved on the intended corrected Kesten straight-cylinder domain without assuming an exponential moment.`

Before this run: `0/2`.

After this run: **`1/2`**.

The movement is the lower inequality. It is a rigorous truncation-transfer theorem, not sampling and not a restricted numerical certificate.

Mathematical status of I0062 after this run: **PARTIAL**.

## 2. Required repository recovery

At the beginning of the run I read/recovered on `master`:

- repository `README.md`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`;
- `operations/FLEET_2026-09-16.md` and the current NEW-METHODS owner directive;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the newest complete P11 Lyons report;
- the newest neighboring PROB20-16 Lyons handoff report;
- the newest PROB20-21 Courtade-to-I0061 handoff report;
- the current I-intake rows around I0060/I0061/I0062;
- current ownership surfaces for I0061, I0062, and I0067;
- the existing P12 acceptance of `P11-AUDIT-P12-FROZEN-COMBINED-FULL-04`.

The latest P11 Lyons report has creation commit `c38a524df5d51ff57b99a9252e8265ab8ce92061`, blob `8d205eb94f816252d9047acb56f6bf70d0180dbe`. It already preserves the exact X095 scalar, full-Hessian equivalence, admissible shape quotient, field compactification, boundary-face vanishing, fixed-support theorem, quartic-flat singular tangent, numerical non-counterexample searches, and the two completed stuck-recovery cycles. No part of that proof state was silently reset.

PROB20-16 independently reached the same Lyons handoff and claimed I0067. PROB20-21 independently handed off Courtade and began I0061. Therefore P11 did not collide with either successor.

Direct fetch of `operations/claims/I0062.md` before P11's write returned 404, and bounded repository search found the queue/intake rows but no canonical I0062 owner report. P11 then created the canonical claim once and read it back at the returned commit.

## 3. Lyons handoff state retained exactly

For a strict connected three-site positive contraction `0<K<I_3`, X095 defines

\[
c_1=\log\frac{p_2p_3}{p_\varnothing p_{23}},\qquad
c_2=\log\frac{p_1p_3}{p_\varnothing p_{13}},\qquad
c_3=\log\frac{p_1p_2}{p_\varnothing p_{12}},
\]

\[
\tau=\log\frac{p_\varnothing p_{12}p_{13}p_{23}}
{p_1p_2p_3p_{123}},\qquad
M=\operatorname{diag}(c_1,c_2,c_3)+\tau K,
\]

and, with the retained X095 matrices `C` and vector `v`,

\[
\Phi(K)=v^*\operatorname{adj}(C)v-2\det C.
\]

On the strict generic locus the inherited theorem is the full nine-real-dimensional equivalence

\[
D^2H(K)\preceq0\iff \Phi(K)\ge0.
\]

Thus a rigorous strict admissible `Phi<0` would genuinely refute Lyons Conjecture 2.6 already in dimension three; a global proof of `Phi>=0` would prove only the three-site milestone and remain PARTIAL for the full source conjecture. The complete admissible-domain and boundary obligations are preserved in the previous P11 handoff report. No global lower bound has been certified, so `B_Phi` remains UNMEASURED.

## 4. Successor source and an exact source-text defect

Question 36 in Auffinger–Damron–Hanson asks:

> Determine if the limit in (7.2) exists without the exponential moment assumption.

The surrounding discussion is maximal flow through the straight box

\[
\Lambda=[0,k]\times[0,l]\times[0,m]
\]

in dimension three. Equation (7.2) is the normalized top-to-bottom maximal-flow limit.

### 4.1 The survey's printed growth hypothesis is impossible as written

The survey's rendering of Theorem 7.2 prints, for some `delta>0`,

\[
k^{-1+\delta}\log m(k,l)\to\infty.
\tag{survey-7.1}
\]

while claiming a positive normalized flow limit when `F(0)<p*` and an exponential moment exists.

That printed condition is false as a hypothesis for the asserted positive conclusion. Here is an exact certificate.

Choose a Bernoulli capacity law

\[
F=p\delta_0+(1-p)\delta_1,
\qquad 0<p<p^*.
\]

Set `k=l=n` and

\[
m_n=\lceil e^{n^3}\rceil.
\]

For example with `delta=1/2`,

\[
n^{-1/2}\log m_n\sim n^{5/2}\to\infty,
\]

so the printed condition holds.

For each integer height layer `j`, let `L_j` be the set of vertical edges joining level `j` to level `j+1`. Each `L_j` is a top-to-bottom cut and contains `(n+1)^2` vertical edges. The events

\[
A_j=\{\text{every edge of }L_j\text{ has capacity }0\}
\]

are independent across disjoint layers and satisfy

\[
\Pr(A_j)=p^{(n+1)^2}.
\]

Hence

\[
\Pr(\text{no zero horizontal cut})
=(1-p^{(n+1)^2})^{m_n}
\le \exp\{-m_np^{(n+1)^2}\}.
\]

Because

\[
\log(m_np^{(n+1)^2})
=n^3+(n+1)^2\log p+o(1)\to+\infty,
\]

the right-hand side is summable in `n`. Borel–Cantelli implies that almost surely, for all sufficiently large `n`, some horizontal layer is an all-zero cut. By max-flow/min-cut,

\[
\Phi_n=0
\]

eventually almost surely. Therefore the normalized flow cannot converge to a positive constant under the survey's printed `(survey-7.1)`.

**Verdict:** this is a **SOURCE-TRANSCRIPTION DEFECT**, not a refutation of the intended Question 36.

### 4.2 Corrected Kesten condition recovered from later exact quotations

Marie Théret's thesis explicitly states Kesten's 1987 theorem with

\[
k^{-1+\delta}\log m(k,l)\to0,
\]

and Barbara Dembin's thesis gives the equivalent reparameterized form

\[
\frac{\log m(k,l)}{k^\delta}\to0,
\qquad \delta\in(0,1).
\]

The survey itself later states Zhang's extension with

\[
\log m(k)\le \max_i k_i^{1-\delta},
\]

which is consistent with sub-surface-exponential height rather than the printed infinity sign in Theorem 7.2.

I did not obtain Kesten's 1987 paper text directly in this run. The discrepancy is therefore recorded explicitly in the claim and future reports must not silently use the survey typo as Kesten's actual theorem.

## 5. Current literature/status check, dated 2026-09-17

Queries included the exact Question 36 wording, maximal-flow laws of large numbers without exponential moments, Kesten/Zhang straight cylinders, Rossignol–Théret no-moment flow constants, and later maximal-flow/minimal-surface work.

The strongest directly inspected modern source was Rossignol–Théret, arXiv:1707.08766v2, *Existence and continuity of the flow constant in first passage percolation*.

That paper proves:

1. a no-moment definition of the flow constant by truncation,
   \[
   \nu_G(v)=\lim_{K\to\infty}\nu_{G^K}(v),
   \qquad G^K=\operatorname{Law}(\min(t,K));
   \]
2. a no-moment a.s. LLN for `phi` in **mild flat cylinders**, assuming only `G({+infty})<p_c(d)`;
3. continuity of `G -> nu_G` under weak convergence;
4. an explicit warning that non-flat straight-cylinder `phi` is harder and that Kesten/Zhang's corresponding results used moment assumptions.

Thus Rossignol–Théret solves a large neighboring no-moment regime but does not, in the material inspected, state the full nonisotropic/non-flat Kesten/Zhang Question-36 geometry.

Dembin–Garban's 2024 maximal-surface work concerns bounded two-valued capacities and does not remove this full-source moment issue.

A bounded search through 2026-09-17 found no source-matching later theorem eliminating the exponential-moment assumption on the entire intended Kesten/Zhang straight non-flat regime. This is evidence only; a failed bounded search is not proof of worldwide openness.

## 6. B2 — attack the negation first

Outcome: **success on the printed auxiliary statement, not on the intended open problem.**

The Bernoulli zero-plane construction in Section 4 rigorously falsifies the survey's printed `k^{-1+delta} log m -> infinity` version of Theorem 7.2. This prevents an invalid source baseline from entering future proofs.

It does **not** refute Question 36, because exact later quotations of Kesten use a sub-surface-exponential height condition with limit zero, and the survey's own Zhang theorem is consistent with that corrected direction.

No floating-point search or finite checker was needed for this asymptotic contradiction.

## 7. B18 — say the no-moment problem in another language: monotone truncation of min cuts

The useful category change is to regard maximal flow as a monotone functional of all edge capacities and to compare the original law with bounded truncations on the **same edge environment**.

For a capacity law `G` on `[0,+infty]`, define

\[
t_e^{(K)}=\min(t_e,K),\qquad G^K=\operatorname{Law}(t_e^{(K)}).
\]

For every finite cylinder and every realization,

\[
t_e^{(K)}\le t_e
\quad\forall e.
\]

By max-flow/min-cut, increasing capacities cannot decrease maximal flow, so

\[
\Phi_n^{(K)}\le \Phi_n.
\tag{7.1}
\]

This elementary order comparison is the basis of the new one-sided transfer theorem below.

## 8. Main result — truncation transfers the full lower bracket without any exponential moment

### Claim `P11-I0062-TRUNCATION-LIMINF-01` — PROVED

Let `G` be a capacity law with `G({+infty})<p_c(d)` and with the same zero-mass condition required by the relevant Kesten/Zhang positive-flow theorem. Let `(C_n)` be **any straight-cylinder sequence for which the bounded-capacity Kesten/Zhang law of large numbers is valid with normalization `A_n`**, i.e. for every finite `K>0`,

\[
\frac{\Phi_n^{(K)}}{A_n}\to\nu_{G^K}(v_0)
\qquad\text{a.s.}
\tag{8.1}
\]

Then, without any moment assumption on `G`,

\[
\boxed{
\liminf_{n\to\infty}\frac{\Phi_n}{A_n}
\ge \nu_G(v_0)
\qquad\text{a.s.}
}
\tag{8.2}
\]

where `nu_G` is the no-moment flow constant of Rossignol–Théret.

### Proof

Couple `G` and all truncations `G^K` by `t_e^{(K)}=min(t_e,K)` on the same iid edge family. For every finite cylinder, monotonicity gives (7.1). Fix an integer `K>=1`. On the probability-one event where the bounded-law LLN (8.1) holds,

\[
\liminf_{n\to\infty}\frac{\Phi_n}{A_n}
\ge
\lim_{n\to\infty}\frac{\Phi_n^{(K)}}{A_n}
=
\nu_{G^K}(v_0).
\]

Intersect these probability-one events over `K in N`; the intersection still has probability one. Therefore simultaneously for every integer `K`,

\[
\liminf_n\frac{\Phi_n}{A_n}\ge\nu_{G^K}(v_0).
\]

Rossignol–Théret define the no-moment flow constant by

\[
\nu_G(v_0)=\lim_{K\to\infty}\nu_{G^K}(v_0),
\]

and also prove continuity under weak convergence. Taking `K->infty` gives (8.2). QED.

### Exact scope

For the corrected Kesten dimension-three straight-box geometry, each truncation is bounded and therefore has an exponential moment, so the bounded theorem feeds directly into the claim. Consequently the lower bracket of Question 36 survives removal of the exponential-moment assumption.

This proves **only the liminf half**. It does not prove the limsup half, and it does not by itself establish `L1` convergence.

### Metric movement

This is why

`Q36_global_bracket: 0/2 -> 1/2`.

The movement is exact and global on the corrected inherited geometry, not a positive subbox or a sampled case.

## 9. B30 — solve one side at a time; the obstruction is now one-sided

The full a.s. limit would follow from the missing inequality

\[
\boxed{
\limsup_{n\to\infty}\frac{\Phi_n}{A_n}
\le\nu_G(v_0)
\quad\text{a.s.}
}
\tag{9.1}
\]

under the corrected Kesten/Zhang geometry.

Truncation gives no direct upper bound because

\[
\Phi_n^{(K)}\le\Phi_n,
\]

which has the wrong orientation. To prove (9.1), one must construct, in the original untruncated environment, a cut whose excess capacity over a near-minimal truncated cut is `o(A_n)`.

That is a random-cutset problem: the truncated minimizer depends on the same environment as the large capacities whose excess must be controlled. A naive fixed-plane estimate is too expensive and in general targets the mean capacity rather than `nu_G`.

So the successor obstruction has been reduced from a two-sided LLN to a precise **upper-tail-on-the-random-minimal-cut** problem.

A plausible next theorem is:

> for a truncated near-minimal cut `E_n^{(K)}`, control
> \[
> \sum_{e\in E_n^{(K)}}(t_e-K)_+
> \]
> at `o(A_n)` after first choosing `K` large, uniformly in the corrected non-flat straight-cylinder geometry.

Any proof must handle the dependence between the random cut and the untruncated capacities. Minimal-cut cardinality estimates or a resampling argument are more promising than another fixed deterministic cut.

## 10. Convergence modes and boundary cases

- **Almost sure lower bracket:** PROVED in Claim `P11-I0062-TRUNCATION-LIMINF-01`.
- **Almost sure upper bracket:** OPEN.
- **Almost sure full limit:** OPEN, dependent on the upper bracket.
- **L1 convergence:** OPEN in the no-exponential-moment source scope; no integrability claim is inferred from the a.s. lower bracket.
- **Flow constant existence itself:** KNOWN without moments in the Rossignol–Théret sense under `G({+infty})<p_c(d)`.
- **Mild flat-cylinder `phi` LLN without moments:** KNOWN by Rossignol–Théret; this is not counted as closure of the non-flat/nonisotropic source target.
- **Printed survey growth condition:** DISPROVED as a valid Kesten hypothesis by the exact Bernoulli zero-plane argument. The intended corrected Kesten theorem is not disproved.

## 11. Peer audit

### `P11-AUDIT-I0061-ATOM-SAFE-TILT-08` — PASS

Audited peer report:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/runs/2026-09-16/2026-09-16_23-31-47_UTC__courtade_handoff_i0061_rotation.md`

creation commit `b60d3f896c77dded5e95f6030ce646483a09c2ef`, blob `299afd559f978623222715c4b453d17bfa4cf397`.

Peer claim: **Lemma 4.1 — atom-safe monotone volume tilt.** For bounded nondegenerate `F`,

\[
\frac{dF_\theta}{dF}(x)=e^{\theta x-\Lambda(\theta)}.
\]

The report claims mutual absolute continuity, first-order stochastic increase, strict mean increase, and

\[
D(F_\theta^{\otimes N}\|F^{\otimes N})
=N[\theta\Lambda'(\theta)-\Lambda(\theta)].
\]

Independent verification:

1. the Radon–Nikodym derivative is strictly positive and finite on bounded support, giving mutual absolute continuity;
2. for `theta_2>theta_1`, the likelihood ratio `dF_theta2/dF_theta1` is proportional to `exp((theta_2-theta_1)x)`, hence is increasing and gives monotone-likelihood-ratio, therefore first-order stochastic, dominance;
3. `Lambda'(theta)=E_theta X` and `Lambda''(theta)=Var_theta(X)>0` for a non-point-mass law, hence the tilted mean increases strictly;
4. taking the `F_theta` expectation of `theta X-Lambda(theta)` gives exactly the stated one-site KL divergence, and product relative entropy tensorizes.

Verdict: **PASS**. This is a component audit of the I0061 successor route, not a proof of Auffinger–Damron–Hanson Question 18.

## 12. P12 directed audit duty

The requested full-package P12 duty is already complete and was not redundantly repeated.

`P11-AUDIT-P12-FROZEN-COMBINED-FULL-04 = PASS / COMPLETE OTHER-TRACK AUDIT`

is preserved in

`proofnet24/P11-lyons-entropy/runs/2026-09-16/2026-09-16T17-09-09Z__run-report.md`, creation commit `03d0909ea147895e84e82f62ff350ad1f3e2edf4`, blob `c6701b8b82470ee24d7ddbca248de38746235631`.

P12's own newer reports explicitly recognize this as the required distinct OTHER-track complete audit. Re-running it here would violate the new-method emphasis.

## 13. Cumulative ledger

### Lyons / X095

- Full strict-locus Hessian sign iff `Phi>=0`: PROVED in inherited X095 package.
- Complete closed-domain global `Phi>=0`: OPEN.
- Certified global lower bound `B_Phi`: UNMEASURED.
- Strict admissible negative witness: NONE CERTIFIED.
- Three-site source status: PARTIAL / HANDOFF.
- General Lyons 2.6: OPEN/PARTIAL; no closure claim.

### I0062

- Survey-printed `(7.1)` with `-> infinity` is a valid Kesten hypothesis: DISPROVED.
- This survey typo refutes intended Question 36: DISPROVED as an inference; it does not.
- Corrected Kesten height condition is sub-surface exponential (`->0` form): SUPPORTED by exact later quotations; original Kesten paper not directly inspected this run.
- No-moment flow constant `nu_G` and its continuity: KNOWN, Rossignol–Théret 2018.
- No-moment mild flat-cylinder LLN: KNOWN, Rossignol–Théret 2018.
- `P11-I0062-TRUNCATION-LIMINF-01`: PROVED.
- Full no-exp-moment limsup in corrected non-flat straight-cylinder geometry: OPEN.
- Full a.s. limit in that geometry: OPEN.
- L1 convergence in the source's weakened-moment scope: OPEN.
- Frozen metric `Q36_global_bracket`: `1/2`.

## 14. Failed routes / what not to do next

1. Do not return to Lyons/X095 absent explicit owner reassignment; P11 has exhausted the authorized HARD stuck-recovery count.
2. Do not use the survey's printed `(7.1)` without the source correction; it is mathematically impossible.
3. Do not count Rossignol–Théret's flat mild-cylinder theorem as closure of the non-flat/nonisotropic Kesten/Zhang source geometry.
4. Do not try to get the upper bracket by monotone truncation alone; the inequality points the wrong way.
5. Do not use a deterministic horizontal plane as a proxy for the random minimal cut if the goal is the sharp constant `nu_G`.
6. Do not infer `L1` convergence from the a.s. lower bracket.

## 15. Next attack

The next P11 run should work on I0062 and use three methods different from B2/B18/B30.

Highest-value mathematical target:

\[
\boxed{
\limsup_n \Phi_n/A_n\le\nu_G(v_0)
}
\]

for a meaningful weakened-moment class strictly larger than the exponential-moment class, ideally finite first moment first and then weaker tails.

Recommended new-method triple:

- **B5 add a truncation parameter and differentiate/compare in it:** quantify the excess above `K` on a near-minimal `G^K` cut;
- **B21 ask who else has this shape:** import sharp minimal-cutset cardinality/tail results and check whether they survive anisotropic cylinders;
- **B23 assume the opposite:** seek a heavy-tail law for which rare huge capacities force a positive limsup excess, which would identify the true weakest moment hypothesis or produce a source-valid counterexample to an overstrong no-moment formulation.

A proof of an upper comparison for finite first moment would already be genuine source progress; a rigorously verified heavy-tail failure would be equally valuable if it addresses the exact intended question rather than the survey typo.

## 16. Model/scheduler control

The current exposed task-control interface still offers task title, prompt, schedule/timing mode, and enabled state but **no model selector and no reasoning-effort selector**. GPT-6/maximum therefore remains a prompt request only. Changing it requires a platform/product/admin surface that actually exposes and honors those fields, or platform support.

Historical `You cannot modify this task` responses, including the cited P26 context, are ownership/authorization boundaries. The legitimate workaround is the owning authorized context, an authorized admin/product surface, or platform support. Duplicating the task or bypassing permissions is not acceptable.

## 17. ledger_delta for P26

```yaml
track: P11
report_kind: LYONS_HANDOFF_AND_I0062_SUCCESSOR
predecessor:
  target: Lyons-2014-Conjecture-2.6 / X095 three-site
  metric: B_Phi
  before: UNMEASURED
  after: UNMEASURED
  movement: NO_MOVEMENT
  status: PARTIAL_HANDOFF
  reason: THIRD_STUCK_MANDATORY_ROTATION_ALREADY_TRIGGERED
successor:
  canonical_id: I0062
  source: Auffinger-Damron-Hanson, 50 years of first-passage percolation, Question 36
  category: HARD_OUTSIDE
  canonical_claim: operations/claims/I0062.md
  claim_creation_commit: ed9ecb3d7204e8d6c4e8124d75e46bb8e5fc603c
  claim_blob: de34fae1df554ead407d7bbc3d1088a6378153b1
  metric: Q36_global_bracket
  before: 0/2
  after: 1/2
  movement: MOVED
  status: PARTIAL
  strongest_claim: P11-I0062-TRUNCATION-LIMINF-01
source_correction:
  survey_printed_7_1: DISPROVED_AS_VALID_HYPOTHESIS
  intended_question_refuted: NO
peer_audit:
  id: P11-AUDIT-I0061-ATOM-SAFE-TILT-08
  verdict: PASS
  peer_path: probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-21/runs/2026-09-16/2026-09-16_23-31-47_UTC__courtade_handoff_i0061_rotation.md
  peer_creation_commit: b60d3f896c77dded5e95f6030ce646483a09c2ef
  peer_blob: 299afd559f978623222715c4b453d17bfa4cf397
p12_directed_duty:
  id: P11-AUDIT-P12-FROZEN-COMBINED-FULL-04
  status: ALREADY_COMPLETE_PASS
next_obligation: upper bracket for corrected non-flat straight-cylinder geometry under weakened moments
next_methods: [B5, B21, B23]
```

No root shared ledger, peer file, email, Gmail, Drive, public resource, permission, billing setting, workflow, or extra schedule was modified by this run.

END_OF_CANONICAL_REPORT_P11_2026-09-17T00-21-45Z
