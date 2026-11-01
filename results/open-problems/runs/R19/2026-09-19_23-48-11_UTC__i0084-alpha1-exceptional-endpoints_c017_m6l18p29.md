Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT in the alpha=1/2 headline metric); genuine obligation progress: exceptional alpha=1 endpoint branches `0/2 -> 2/2` internally. Section-B moves: #6, #18, #29, explicitly a second-cycle triple because all 30 moves were exhausted earlier; the immediately preceding triple was #2/#24/#27.**

Problem/source: Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **SOURCE REFUTED MATHEMATICALLY already at alpha=1/2; repository status remains PARTIAL / AUDIT_PENDING. New this run: PROVED PARTIAL source-scope extension R19-I0084-C017 covering the exceptional alpha=1 skew endpoints in both the classical-stable and free-stable-law branches, always under the frozen arXiv ordinary-convolution convention.**

## 1. Continuity and governing instruction

I resumed from the latest R19/I0084 state and preserved the six-run handoff package rather than restarting. In particular, the retained fixed metric is 2/2: the classical-stable and free-stable-law alpha=1/2 universal source cases are both already disposed of by source-admissible endpoint-skewness counterexamples with the full initial-measure quantifier defeated by an explicit admissible law. Existing audit evidence is not silently upgraded: the ALEA free-`boxplus` audits do not count as frozen-arXiv ordinary-`*` end-to-end audits.

I also read the 20 September progress-first owner directive and deployment receipt. That later owner direction explicitly supersedes the targetless admission/audit-wait loops that had occupied the most recent R19 runs and directs useful effort back to mathematics. Accordingly this run does not create another successor checker or gate receipt. It attacks a genuine remaining mathematical boundary of the preserved I0084 theory.

Required repository state read this run included `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest R19 report/handoff, the latest progress-first operations files, and targeted I0084/P26 audit searches. No posted additive Brownian-unimodality result is counted here.

## 2. Frozen source convention, rechecked

The authoritative frozen target is arXiv:1710.08240v2, page 18 / Conjecture 5.5. It literally states that `S_t` may be the law of a **classical or free alpha-stable process**, assumes

\[
\int_{\mathbb R}|x|^{2+\alpha}\,d\mu(x)<\infty,
\]

and concludes that

\[
\boxed{\mu * S_t}
\]

is unimodal for all sufficiently large `t`.

The asterisk is ordinary **classical convolution**. This run does not replace it by free additive convolution when `S_t` happens to be the law of a free stable process.

The old fixed alpha=1/2 metric is already saturated. The useful unresolved structural hole in the stronger endpoint theorem C011 was `alpha=1`: C011 covered every extremal stable skewness for `alpha in (0,1) union (1,2)` but deliberately excluded the singular index one.

## 3. New-method attacks

### #6 — DEFORM TO A POINT YOU CAN SOLVE

The alpha-ne-1 endpoint theorem leaves a singular boundary at alpha=1. Hasebe--Simon--Wang identify the limiting exceptional classical and free 1-stable variables explicitly: the classical variable `S` is characterized by

\[
\mathbb E[e^{sS}]=s^s,\qquad s>0,
\]

while the exceptional free 1-stable variable `T` has Voiculescu transform

\[
\phi_T(z)=-\log z.
\]

Their paper also exhibits `T` as the alpha-up-to-1 limit of one-sided free stable laws. Rather than trying to pass the old sparse-bump estimates through a singular alpha-limit, I solve the limiting kernels directly.

### #18 — SAY IT IN ANOTHER LANGUAGE

At alpha=1, strict self-similarity acquires logarithmic centering. Writing the semigroup in cumulant/Voiculescu-transform language makes that centering exact and reduces every time to the scale family already handled by C010.

### #29 — ADD THE POINTS AT INFINITY

The missing alpha=1 endpoints are boundary objects with a super-light side: the classical exceptional law has a finite positive exponential moment and a monotone density tail, while the free exceptional law has a literal half-line support. This is precisely the boundary-at-infinity geometry C010 needs.

## 4. Recalled engine: C010

The already proved R19-I0084-C010 sparse-bump theorem says the following. Let `k` be a bounded continuous probability density with a strict quantitative mode, and suppose one density tail is superpolynomially light, e.g.

\[
K_+(r):=\sup_{x\ge r}k(x),\qquad r^N K_+(r)\to0
\]

for every `N>0` (or the reflected left-tail condition). For the scale family

\[
k_s(x)=s^{-1}k(x/s),
\]

there exists one probability measure `mu`, independent of `s`, with **every finite polynomial moment**, such that

\[
\mu*k_s
\]

is nonunimodal for every `s>0`.

This is a theorem-sized analytic result already written in the R19 history, not a numerical heuristic.

A harmless extension will be used repeatedly: if

\[
K_t(x)=a_t^{-1}k\!\left(\frac{x-b_t}{a_t}\right),\qquad a_t>0,
\]

then `K_t` is just a translate of `k_{a_t}`. Hence the same C010 witness makes `mu*K_t` nonunimodal whenever `mu*k_{a_t}` is nonunimodal. Translation does not change unimodality.

# 5. R19-I0084-C017 — exceptional alpha=1 endpoint obstruction

**STATUS: PROVED INTERNALLY / PROVED PARTIAL source-scope extension.**

Under the standard stable-process convention that includes the non-strict exceptional skew 1-stable laws, the missing extremal-skewness alpha=1 cases of C011 also fail under the frozen ordinary-convolution convention.

More precisely:

1. Let `S` be the exceptional classical 1-stable law characterized by
   \[
   \mathbb E[e^{sS}]=s^s,\qquad s>0.
   \]
   There exists a probability measure `mu_S` having every finite polynomial moment such that, for the classical stable Levy process whose time-one law is `S`,
   \[
   \mu_S * S_t
   \]
   is nonunimodal for every `t>0`. The reflected exceptional endpoint has the same property.

2. Let `T` be the exceptional free 1-stable law with `phi_T(z)=-log z`. Regard the law of the corresponding free stable process at time `t` merely as a **classical convolution kernel**, exactly as arXiv Conjecture 5.5 prints it. There exists a probability measure `mu_T` having every finite polynomial moment such that
   \[
   \mu_T * T_t
   \]
   is nonunimodal for every `t>0`. The reflected free endpoint has the same property.

In particular, at alpha=1 the source moment requirement is the finite third moment, and both witnesses satisfy far more: all polynomial moments are finite. This is therefore a genuine source-admissible negative result, not a positive theorem proved only under a stronger moment assumption.

## 5.1 Classical exceptional endpoint: the light tail

Hasebe--Simon--Wang recall that classical stable densities are bell-shaped. Thus the density `k` of `S` is smooth, bounded, has a strict unique mode `m`, and is decreasing on `(m,infinity)`.

The defining transform gives

\[
\mathbb E[e^S]=1.
\]

For `x>m+1`, monotonicity on `[x-1,x]` gives

\[
k(x)
\le \int_{x-1}^{x}k(u)\,du
\le \mathbb P(S\ge x-1).
\]

Markov's inequality therefore yields

\[
\boxed{k(x)\le e^{-(x-1)}}. \tag{5.1}
\]

Hence the right density tail is exponentially, in particular superpolynomially, light:

\[
r^N\sup_{x\ge r}k(x)\to0
\quad\text{for every }N>0. \tag{5.2}
\]

All hypotheses of the reflected/right-tail form of C010 hold. Consequently there is a single `mu_S` with all polynomial moments such that

\[
\mu_S*k_s
\]

is nonunimodal for every spatial scale `s>0`.

## 5.2 Classical stable time is scale plus logarithmic centering

Let `S_t` denote the classical convolution semigroup generated by `S`. The cumulant of `S` on positive arguments is

\[
\psi(s)=\log\mathbb E[e^{sS}]=s\log s.
\]

Therefore the time-`t` semigroup law has cumulant `t s log s`. On the other hand,

\[
\begin{aligned}
\log \mathbb E\exp\{s(tS-t\log t)\}
&=-st\log t+\log\mathbb E[e^{(st)S}]\\
&=-st\log t+st\log(st)\\
&=ts\log s.
\end{aligned}
\]

Thus

\[
\boxed{S_t\ \stackrel d=\ tS-t\log t.} \tag{5.3}
\]

Its density is an affine translate of `k_t`. By the affine observation after C010, `mu_S*S_t` is nonunimodal for every `t>0`.

Reflecting `S` and the C010 construction gives the opposite exceptional classical skew endpoint.

## 5.3 Free exceptional endpoint: literal half-line support

Hasebe--Simon--Wang define `T` by

\[
\phi_T(z)=-\log z.
\]

They prove that the density of `T` is `WS_-` (whale-shaped on a negative half-line) and explicitly identify its support as

\[
\operatorname{supp}(T)=(-\infty,1].
\]

A `WS_-` density is smooth on the interior of its support, vanishes at both ends, and has one derivative zero, hence one strict mode. In particular it is bounded and continuous, and its right tail is identically zero for `x>1`. C010 therefore applies immediately: there is one all-polynomial-moment law `mu_T` for which ordinary convolution by every dilation of the density of `T` is nonunimodal.

Hasebe--Simon--Wang also identify the free 1-stable endpoint parameters: their `rho=0` and `rho=1` laws are affine transforms of `T` and `-T`, respectively. Hence these are exactly the exceptional free skew endpoints up to the irrelevant affine normalization.

## 5.4 Free stable time is again scale plus logarithmic centering

For a free additive convolution semigroup,

\[
\phi_{T_t}(z)=t\phi_T(z)=-t\log z.
\]

For `a>0`, the affine-transform rule is

\[
\phi_{aX+b}(z)=b+a\phi_X(z/a).
\]

Taking `a=t`, `b=-t log t`, and `X=T`,

\[
\begin{aligned}
\phi_{tT-t\log t}(z)
&=-t\log t+t[-\log(z/t)]\\
&=-t\log z.
\end{aligned}
\]

Therefore

\[
\boxed{T_t\ \stackrel d=\ tT-t\log t.} \tag{5.4}
\]

Again, this is a statement about the **law** of the free stable process. The convolution used in the target remains classical:

\[
\mu_T*T_t.
\]

Since the time law is a translated dilation of `T`, C010 gives nonunimodality for every `t>0`. Reflection handles the other free endpoint.

## 5.5 What this does and does not prove

This closes the alpha=1 hole in the **endpoint-counterexample** theorem C011. Combining C011 with C017 gives the following internal extension:

> For every alpha in `(0,2)`, at each extremal skewness for which the standard stable family has the corresponding endpoint law (using the exceptional logarithmically-centered laws at alpha=1), both the classical stable kernel and the free-stable law used as an ordinary classical kernel admit an all-polynomial-moment initial law whose convolution is nonunimodal at every time.

This is stronger source information but **does not change the fixed alpha=1/2 metric**, which remains 2/2.

I do **not** claim here a full alpha=1 all-skewness classification. For the classical interior, C008 should apply once the two-sided derivative-tail constants are written carefully in a normalization matching the alpha=1 skew parameter. For the general free 1-stable law `C_{a,b}=a X_{1,1/2}+bT` in free convolution, Hasebe--Simon--Wang prove bell shape only in specified subfamilies (`b=0` or a discrete ratio condition); their paper does not give the full shape statement needed for an immediate C008 application. That is the honest next obstruction.

There is one convention caveat. The source says “alpha-stable process,” not “strictly stable process.” C017 uses the standard broad alpha=1 stable-process class, in which the skew endpoints require logarithmic centering and are not strictly stable. If one were to impose the narrower **strict** alpha=1 convention, the strict family reduces to the drifted/symmetric Cauchy situation already treated in Section 5.1 of the source; C017 should then be viewed as a natural source-adjacent strengthening rather than a needed ingredient in the minimal refutation. The frozen alpha=1/2 result is unaffected by this convention issue.

## 6. Prior-art / current-status check, 2026-09-19 UTC

Fresh bounded web searches were run for:

- exact `Hasebe Ueda Conjecture 5.5 stable unimodality`;
- `eventual unimodality stable convolution 2+alpha`;
- `exceptional 1-stable convolution unimodality Hasebe`;
- the original arXiv identifier and later Hasebe/Ueda work.

The original Hasebe--Ueda paper and Hasebe--Simon--Wang's free-stable paper were recovered. I did not locate a later primary paper explicitly resolving the exact frozen arXiv-v2 ordinary-`*` formulation or stating C017. This is bounded negative evidence only, **not** an absolute novelty certificate.

Primary ingredients used for C017:

- Hasebe--Ueda, arXiv:1710.08240v2, Conjecture 5.5, page 18: ordinary `mu*S_t` even when `S_t` is the law of a free stable process.
- Hasebe--Simon--Wang, arXiv:1805.01133v2 / published work on free stable distributions: exceptional free 1-stable `T`, `phi_T=-log z`; `rho=0,1` affine endpoint identifications; Theorem 4(c), density of `T` is `WS_-`; Proposition 2, exceptional classical 1-stable `S` with `E[e^{sS}]=s^s`.
- The already-written R19 C010 sparse-bump theorem.

No new finite arithmetic claim is introduced, so no checker was manufactured merely for bookkeeping. The proof above is the evidence.

## 7. Audit state

Targeted repository searches still find:

- `R18-I0084-C001=PASS` for the classical positive-half-stable finite/symbolic core;
- `R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS_FULL_MATHEMATICAL_PROOF` for the **ALEA free-boxplus** scope only;
- `R18-AUDIT-R19-I0084-C010-ABSTRACT-004=PASS_FULL_MATHEMATICAL_PROOF` for C010 only;
- `P26-AUDIT-R19-I0084-C002-ENDTOEND-06=PASS_FULL_MATHEMATICAL_PROOF/PUBLISHED_ALEA_SCOPE`, again not the frozen ordinary-`*` package.

I found no new version-matching P26 frozen-arXiv ordinary-`*` end-to-end PASS and no distinct OTHER-track end-to-end PASS for that same frozen package. Thus the minimal alpha=1/2 source-refutation audit gate remains **0/2** under the version-specific rule. C017 is also unaudited and is not used to pretend that gate moved.

## 8. Model/scheduler control status

The newest progress-first deployment receipt still states that the available scheduler interface has **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort telemetry, and no guaranteed full-hour runtime control**. GPT-6/maximum therefore remains a prompt preference, not an enforceable setting from this interface.

The historical P26 `You cannot modify this task` event was context-specific rather than universal: the current root RESULTS record preserves that a later authorized P/C context successfully applied the full P26 update. The supported workaround for a denied task is therefore the owning/authorized native context, an ordinary permission/ownership repair, or platform support — never a bypass. I made no scheduler changes in this run.

## 9. Remaining mathematical attack

The most natural next mathematics is no longer another alpha=1/2 lemma. It is the alpha=1 **interior** boundary:

1. write the exact two-sided derivative asymptotics for the classical alpha=1 skew-stable density and feed them into C008, which should extend the exact classical classification through alpha=1;
2. for the free alpha=1 family `C_{a,b}`, determine enough one-mode curvature / derivative-tail control to apply C008 beyond the bell-shaped subfamilies already proved by Hasebe--Simon--Wang;
3. keep ordinary convolution throughout.

If that route stalls twice under the progress-first policy, preserve the endpoint theorem C017 and move to a different registered bottleneck rather than returning to admission-only reports.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R19
  source: "Hasebe-Ueda arXiv:1710.08240v2 Conjecture 5.5 / I0084"
  frozen_convolution: "ordinary classical mu * S_t in both classical-law and free-stable-law branches"
  fixed_metric: "number of complete alpha=1/2 classical-stable/free-stable source cases disposed of"
  metric_before: "2/2"
  metric_after: "2/2"
  metric_movement: "NO MOVEMENT"
  substantive_progress:
    claim_id: "R19-I0084-C017"
    statement: "exceptional alpha=1 classical and free stable skew endpoints admit all-polynomial-moment all-time ordinary-convolution counterexamples"
    endpoint_obligation_before: "0/2"
    endpoint_obligation_after: "2/2 internally"
    status: "PROVED PARTIAL / independent audit pending"
  source_status: "mathematically REFUTED already by alpha=1/2 endpoint package; repository PARTIAL/AUDIT_PENDING"
  unchanged_count: "UNKNOWN beyond the preserved >=6 headline-metric saturation streak; not reset merely because the fixed metric is unchanged"
  substantive_stagnation_this_run: 0
  tried_moves: [6, 18, 29]
  remaining_obligation:
    - "P26 frozen-arXiv ordinary-* end-to-end PASS"
    - "one distinct OTHER-track frozen-arXiv ordinary-* end-to-end PASS"
    - "optional strengthening: alpha=1 interior classification, especially general free C_{a,b}"
  evidence:
    - "artifacts/R19/2026-09-16_21-40-25_UTC__i0084_rotation_handoff.md"
    - "runs/R19/2026-09-16_18-45-28_UTC__i0084-light-tail-endpoints.md (C010/C011/C012/C013)"
    - "Hasebe-Ueda arXiv:1710.08240v2, Conjecture 5.5"
    - "Hasebe-Simon-Wang arXiv:1805.01133v2, exceptional 1-stable S/T and Theorem 4(c)"
  audit_ids:
    - "R18-I0084-C001=PASS [narrow classical endpoint core]"
    - "R18-AUDIT-R19-I0084-C002-ENDTOEND-001=PASS [ALEA boxplus scope; not counted]"
    - "R18-AUDIT-R19-I0084-C010-ABSTRACT-004=PASS [C010 only]"
    - "P26-AUDIT-R19-I0084-C002-ENDTOEND-06=PASS [ALEA boxplus scope; not counted]"
  frozen_audit_gate: "0/2"
  prewrite_master_head: "1a5cfae17c4d3e9de372152ce4ac17635adc9f5f"
```
