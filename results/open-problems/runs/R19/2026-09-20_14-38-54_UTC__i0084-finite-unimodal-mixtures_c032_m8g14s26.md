Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT); genuine theorem progress: C031 extends from one unimodal initial law to every finite mixture of unimodal initial laws, with arbitrary tails and no moment assumption. Section-B moves: #8 GO THE OTHER WAY AND DISCRETIZE; #14 FIND THE GROUP ACTING; #26 HUNT THE SPORADIC CASE. The immediately preceding C031 triple was #2/#5/#18, so it is not repeated. Every numbered move has appeared somewhere in the long R19 history; these three are reused here in a materially new mathematical role rather than falsely claimed globally unused.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **PARTIAL / AUDIT_PENDING.** The frozen source statement is already internally refuted at extremal skewness by earlier R19 counterexamples satisfying the source moment hypothesis, while the positive interior regions are internally proved by C020/C021 using C008. The fixed alpha=`1/2` two-branch case-count metric is saturated at `2/2`; C032 therefore earns no new source-case credit. It is a new source-relevant theorem for a strict class of inputs broader than C031, so it remains PARTIAL.

# 1. Recovery and exact source convention

I continued from the newest complete R19 checkpoint

`runs/R19/2026-09-20_13-40-27_UTC__i0084-all-unimodal-inputs-no-moment_c031_m2p5l18.md`

rather than restarting. I re-read/queried the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `QUEUE.md`, the 20 September progress-first owner directive and registry, the current I0084/R19 history, and the inherited R18 audit of C008. The later progress-first directive explicitly allows an unchanged headline metric to coexist with a genuine structural theorem and prioritizes mathematics over repeated admission/audit loops.

The frozen source convention is preserved exactly. In arXiv v2 Conjecture 5.5, `S_t` may be the law of a **classical or free** alpha-stable process, the hypothesis is

`int_R |x|^(2+alpha) mu(dx) < infinity`,

and the conclusion is that

`mu * S_t`

is unimodal for all sufficiently large `t`. The operation displayed in this frozen source is ordinary **classical convolution** `*`, including when `S_t` is the law of a free stable distribution. I do **not** replace it by free convolution. The later published wording is not silently substituted into this task.

Retained supported R19 progress includes C008 (independently audited abstract critical-tail smoothing theorem), endpoint counterexamples C011/C017, interior exact-moment theorems C020/C021, power-moment sharpness C022, regular endpoint counterexamples C024--C029, and the no-moment unimodal-input theorem C031. This run asks whether C031 survives a first genuinely multimodal enlargement of the input class.

# 2. New-method attacks before the theorem

## Move #26 — hunt the sporadic case: a two-component bimodal counterexample

I first tried to break C031 with the simplest possible nonunimodal input class:

`mu = theta mu_1 + (1-theta) mu_2`,

where both `mu_j` are unimodal but their modes are far apart and the component tails may be arbitrarily heavy. A priori the two smoothed components could have slightly displaced derivative zeroes, and their sum could in principle create a second crossing.

The attempted obstruction fails for a robust reason. At stable spatial scale `s`, the finite mode displacement is only `O(1/s)`. Khintchine's representation of each component reduces its remaining shape to a signed interval length `X_j/s`; for each fixed component the probability of a non-small normalized interval tends to zero. With only finitely many components, the **maximum** of those finitely many bad-tail probabilities also tends to zero. Thus every component eventually has the same derivative sign on a common left region, a common negative sign on a common right region, and a uniformly decreasing derivative through one common central window. Positive weights preserve all three facts. There is no two-component sporadic counterexample.

This failure suggested the finite-mixture theorem below.

## Move #8 — discretize modal complexity

Instead of asking immediately for arbitrary input measures, stratify by the finite number `N` of unimodal pieces. The class

`mu = sum_(j=1)^N w_j mu_j`

already includes multimodal, asymmetric, atomic and arbitrarily heavy-tailed laws. The key question becomes whether the C031 secant-slope proof can be made uniform over finitely many component-specific Khintchine variables. It can.

## Move #14 — quotient the translation action

Translation is the only new geometric parameter introduced by multiple component modes. Choose one reference location `a_*` and write each component mode as

`a_j = a_* + A_j`.

After evaluating the convolution at `a_* + s r`, the `j`-th component sees the kernel at the shifted normalized coordinate

`r - A_j/s`.

Because there are finitely many `A_j`,

`max_j |A_j|/s -> 0`.

Thus the translation group is asymptotically quotiented out: all component mode centers enter the **same** strict-concavity window for large `s`. This is the gluing mechanism absent from the infinite sparse-bump counterexamples C024--C029.

# 3. Abstract finite-mixture theorem

For `s>0` write

`k_s(x)=s^(-1) k(x/s)`.

I use the same kernel class as C031, with a little spare room obtained by shrinking its local parameter `eta` once.

## R19-I0084-C032A — finite mixtures of arbitrary unimodal laws

**THEOREM C032A (PROVED INTERNALLY / AUDIT PENDING).** Let `k` be a continuous probability density supported on `[e,infinity)` for a finite `e`, with a unique mode `m>e`. Assume:

1. `k` is strictly increasing on `(e,m)` and strictly decreasing on `(m,infinity)`;
2. for some `eta>0`, `kappa>0`, with `e<m-4eta`, `k` is `C^2` on `[m-4eta,m+4eta]` and

   `k''(x) <= -kappa` on `[m-4eta,m+4eta]`;

3. the left logarithmic slope has a positive compact lower bound

   `lambda := inf_(e<x<=m-eta) k'(x)/k(x) > 0`;

4. for some `p>1`, `R_0>0`, `c_0,C_0>0`,

   `-k'(r) >= c_0 r^(-p)` and `k(r)/r <= C_0 r^(-p)`

   for every `r>=R_0`.

Let

`mu = sum_(j=1)^N w_j mu_j`,

where `N<infinity`, `w_j>0`, `sum_j w_j=1`, and every `mu_j` is an arbitrary unimodal probability measure on `R`, with mode `a_j`. Atoms, asymmetry and infinite moments are allowed.

Then there exists `s_0<infinity` such that

`mu*k_s`

is unimodal for every `s>=s_0`.

The reflected statement holds for the reflected kernel.

If additionally each component has finite centered `p`-th moment

`M_(p,j) = int |x-a_j|^p mu_j(dx) < infinity`,

then after fixing any reference mode `a_*` one may take

`s_0 <= C_k [ 1 + D + max_j M_(p,j)^(1/p) ]`,                 (C032.1)

where

`D=max_j |a_j-a_*|`

and `C_k<infinity` depends only on the fixed kernel and the displayed quantitative choices. No dependence on a lower bound for the mixture weights is required.

# 4. Proof of C032A

## 4.1 Componentwise Khintchine representation

For each `j`, translate `mu_j` to its mode. Khintchine's representation gives

`Y_j = a_j + U_j X_j`,

where `U_j ~ Uniform[0,1]`, independent of an arbitrary real random variable `X_j`. We may use separate `U_j,X_j` on separate auxiliary spaces; only their one-dimensional laws matter.

Choose a reference mode `a_*` and put

`A_j=a_j-a_*`,

`delta_j=A_j/s`,

`a=X_j/s`.

For `a != 0` define

`D_a(r)=[k(r)-k(r-a)]/a`,

and set `D_0(r)=k'(r)` at smooth points. Evaluating the rescaled convolution at `a_*+sr` gives

`G_s(r):=s (mu*k_s)(a_*+sr)`

and, on the smooth regions used below,

`G_s'(r)
 = sum_(j=1)^N w_j E D_(X_j/s)(r-delta_j).`                (C032.2)

This is the same signed-secant representation as C031, except for the small deterministic shifts `delta_j`.

Since `N<infinity`,

`Delta_s:=max_j |delta_j| -> 0`,                              (C032.3)

and for every fixed `c>0`,

`q_s(c):=max_j P(|X_j|>cs) -> 0`.                            (C032.4)

These two finite maxima are the entire new input needed to glue the C031 estimates.

## 4.2 Common left-flank positivity

Take `s` so large that

`Delta_s <= eta/4`.

Consider first

`r <= m-2eta`.

For the `j`-th component set

`q_j=r-delta_j`.

Then

`q_j <= m-7eta/4`.

If `q_j<=e`, the same support-edge calculation as in C031 shows that every short signed secant is nonnegative, and any negative contribution can only come from a negative interval long enough to reach past the kernel mode.

If `e<q_j<=m-7eta/4`, then on the good event

`|X_j|/s <= eta/2`,

the entire signed secant remains on the increasing flank and the logarithmic-slope lower bound gives

`D_(X_j/s)(q_j) >= c_L k(q_j)`                              (C032.5)

with one constant `c_L>0` independent of `j`, `r`, and large `s`. Exactly as in C031, a harmful long negative interval is bounded below by

`-(2/eta)k(q_j)`.                                            (C032.6)

Therefore

`E D_(X_j/s)(q_j)
 >= k(q_j)[c_L(1-q_s(eta/2))-(2/eta)q_s(eta/2)]`.             (C032.7)

The bracket is positive for all sufficiently large `s` by (C032.4). Thus **every component contribution is nonnegative on the common left region**, and strictly positive wherever its shifted kernel value is positive. Summing with positive weights gives

`G_s'(r)>=0` for `r<=m-2eta`,                                (C032.8)

with strict positivity once the convolution density has entered its positive flank. In particular no mode can occur before the common central zone.

## 4.3 A common central window with strictly decreasing derivative

Take the common window

`I=[m-eta,m+eta]`.

For large `s`, `|delta_j|<=eta/4`. On the good event

`|X_j|/s<=eta/2`,

if `r in I`, every point of the chord

`r-delta_j-theta X_j/s`,  0<=theta<=1,

lies in `[m-2eta,m+2eta]`, hence in the strict-concavity region. Therefore for `r_2>r_1` in `I`,

`D_(X_j/s)(r_2-delta_j)-D_(X_j/s)(r_1-delta_j)
 <= -kappa (r_2-r_1)`                                       (C032.9)

on the good event.

For bad intervals `|X_j|/s>eta/2`, compactness and monotonicity give a crude universal upper Lipschitz bound

`D_(X_j/s)(r_2-delta_j)-D_(X_j/s)(r_1-delta_j)
 <= C_I (r_2-r_1)`                                          (C032.10)

for a fixed `C_I<infinity`, uniformly in `j` and large `s`. (As in C031, when the far endpoint remains on the same monotone side its increment is favorable; otherwise one drops that favorable term and uses the bounded derivative on the compact central interval together with `|X_j|/s>=eta/2`.)

Hence for each `j`,

`E D_(X_j/s)(r_2-delta_j)-E D_(X_j/s)(r_1-delta_j)
 <= [-kappa(1-q_s(eta/2))+C_I q_s(eta/2)](r_2-r_1).`         (C032.11)

For large `s` the bracket is negative. Multiplying by `w_j` and summing, we obtain

`G_s'(r_2)<G_s'(r_1)` for `r_2>r_1` in `I`.                 (C032.12)

Thus the derivative of the **whole finite mixture** is strictly decreasing through one common central window.

We next show that it enters this window positive and exits negative.

## 4.4 Common moderate-right negativity

Fix `R>m+2eta`, later enlarged for the tail estimate. Consider

`r in [m+2eta,R]`.

For large `s`, `|delta_j|<=eta/4`, and on

`|X_j|/s<=eta/2`

every chord lies in a fixed compact decreasing interval to the right of the mode. Hence there exists `c_R>0`, independent of `j`, such that

`D_(X_j/s)(r-delta_j) <= -c_R`.                              (C032.13)

A negative signed interval points farther to the right and can never contribute positively. A positive long interval has positive part bounded by a fixed constant `M_R`, so

`E D_(X_j/s)(r-delta_j)
 <= -c_R(1-q_s(eta/2))+M_R q_s(eta/2).`                     (C032.14)

This is negative for every component simultaneously once `s` is large. Therefore

`G_s'(r)<0` uniformly on `[m+2eta,R]`.                       (C032.15)

Similarly, the left-flank estimate can be run up to `m-eta` after shrinking the spare local parameter once, so

`G_s'(m-eta)>0`.                                             (C032.16)

By (C032.12), `G_s'` has exactly one zero in the central window and changes sign there from positive to negative.

## 4.5 Remote right tail: finite gluing of the critical-scale estimate

Enlarge `R` so that all shifted short chords with `r>=R` remain in the region of the tail assumptions, and so that

`r-delta_j-m >= r/3`                                        (C032.17)

for every `j` and all large `s`.

On `|X_j|/s<=eta/2`, the tail derivative lower bound and the mean-value theorem give

`D_(X_j/s)(r-delta_j) <= -c_3 r^(-p)`                       (C032.18)

for one `c_3>0` independent of `j`.

As before, every negative signed interval contributes nonpositively on the decreasing tail. Suppose a positive interval `a=X_j/s>eta/2` contributes positively. Then its backward endpoint must cross back past the mode; otherwise monotonicity gives a nonpositive secant. Thus

`a >= r-delta_j-m >= r/3`.                                  (C032.19)

Therefore its positive part satisfies

`D_a(r-delta_j)^+
 <= k(r-delta_j)/a
 <= 3 k(r-delta_j)/r
 <= C_4 r^(-p)`                                              (C032.20)

for a fixed `C_4`, using `k(u)/u<=C_0u^(-p)` and `u=r-delta_j` comparable with `r`.

Consequently

`E D_(X_j/s)(r-delta_j)
 <= r^(-p)[-c_3(1-q_s(eta/2))
            +C_4 P(X_j >= s(r/3))].`                        (C032.21)

For `r>=R`,

`P(X_j>=sr/3) <= q_s(R/3)`.                                 (C032.22)

Both `q_s(eta/2)` and `q_s(R/3)` tend to zero. Hence the bracket in (C032.21) is negative simultaneously for every `j`, uniformly for every `r>=R`. Positive weights preserve negativity, so

`G_s'(r)<0` for every `r>=R`                                 (C032.23)

when `s` is large.

Combining (C032.8), (C032.12), (C032.15), (C032.16), and (C032.23), the whole finite-mixture convolution has one global increase-to-decrease transition and is unimodal. This proves the qualitative assertion.

## 4.6 Quantitative scale under componentwise p-th moments

If

`M_(p,j)=E|Y_j-a_j|^p<infinity`,

then Khintchine's representation gives the exact identity

`E|X_j|^p=(p+1)M_(p,j)`.                                    (C032.24)

All qualitative uses of (C032.3)--(C032.4) are satisfied once, for fixed kernel-dependent positive thresholds,

`D/s <= c_k`

and

`max_j P(|X_j|>c_k s) <= epsilon_k`.

Markov's inequality yields

`max_j P(|X_j|>c_k s)
 <= (p+1) max_j M_(p,j)/(c_k s)^p`.                          (C032.25)

Thus

`s_0 <= C_k[1+D+max_j M_(p,j)^(1/p)]`,                      (C032.26)

which is (C032.1). This completes C032A.

# 5. Alpha=1/2 stable consequence

## R19-I0084-C032B — finite mixtures for both frozen endpoint kernels

**COROLLARY C032B (PROVED INTERNALLY / AUDIT PENDING).** Let

`mu=sum_(j=1)^N w_j mu_j`

be any finite mixture of unimodal probability laws on `R`, with arbitrary component modes, atoms, asymmetry and tails. No moment assumption is required. Let `L_t` be the positive classical alpha=`1/2` stable law and `F_t` the positive free alpha=`1/2` stable **law regarded as an ordinary classical convolution kernel**, exactly as required by the frozen arXiv target. Then there is `t_0<infinity` such that for all `t>=t_0`,

`mu*L_t` and `mu*F_t`

are unimodal. The same holds for the reflected negative endpoint laws.

The verification of the kernel hypotheses is inherited from C031:

- classical half-stable density

  `k_cl(x)=(1/sqrt(2*pi))x^(-3/2)exp[-1/(2x)]1_(x>0)`,

  with mode `1/3`, strict negative curvature there and critical tail exponent `p=5/2`;

- positive free-half-stable density

  `k_fr(x)=sqrt(4x-1)/(2*pi*x^2)1_(x>=1/4)`,

  again with mode `1/3`, strict negative curvature and the same `p=5/2` tail scale.

If every component has finite centered `5/2` moment and `D=max_j|a_j-a_*|`, then the stable spatial scale is proportional to `s=t^2`, so (C032.26) gives

`t_0 <= C [1+D+max_j M_(5/2,j)^(2/5)]^(1/2).`               (C032.27)

Equivalently, apart from the finite inter-mode separation term, the component moment contribution scales as `M_(5/2,j)^(1/5)` in time, agreeing with C031 when `N=1`.

This is a **strict enlargement** of C031: the initial law itself need not be unimodal. It may have any fixed finite number of separated modal components, and those components may individually have infinite moments.

# 6. Conceptual consequence and exact remaining boundary

The endpoint counterexamples C024--C029 use infinitely many remote oscillatory pieces. C032 proves that this is not incidental to that construction:

> For the half-stable endpoint kernels, no fixed finite mixture of unimodal laws can remain nonunimodal forever under dilation.

Therefore any counterexample mechanism that survives all times must escape **finite unimodal-mixture complexity**. The already constructed sparse counterexamples do exactly that by using an unbounded hierarchy of increasingly remote pieces.

This does **not** prove a theorem for countable mixtures. The proof uses finiteness twice in an essential way:

`max_j |a_j-a_*|/s -> 0`

and

`max_j P(|X_j|>cs) -> 0`.

Neither is available for a general countable mixture with unbounded component modes or nonuniform tails. Indeed the existing infinite sparse-bump counterexamples show that a naive countable extension is false. This sharply identifies the gluing obstruction: not the number of local modes at one fixed scale by itself, but the absence of a uniform tail/translation modulus across infinitely many components.

This is the main mathematical gain of the run.

# 7. Current primary-literature and prior-art check — 20 September 2026

I rechecked the original arXiv source and ran bounded current searches before treating C032 as new campaign progress. The frozen arXiv v2 source is still the 14 September 2018 revision and visibly states Conjecture 5.5 with ordinary `mu*S_t` for a law `S_t` of a classical or free alpha-stable process.

Dated search themes included:

- `"Conjecture 5.5" Hasebe Ueda stable unimodality`;
- `eventual unimodality stable convolution unimodal distribution`;
- `finite mixture of unimodal distributions convolution theorem`;
- `mixture of two unimodal distributions convolution stable`;
- later Hasebe/Ueda work and papers citing the 2018 article.

The search recovered the original Hasebe--Ueda article, later Hasebe/Ueda-related additive/multiplicative/Boolean-unimodality work, and general literature on mixtures of unimodal densities (including work on conditions for bimodality or multimodality of two-component mixtures). I did **not** locate a primary theorem asserting C032A or C032B, nor a later primary theorem resolving the exact frozen arXiv ordinary-`*` Conjecture 5.5 formulation.

This is bounded negative search evidence only, **not** a novelty or priority certificate. General facts about Khintchine representations and mixtures of unimodal laws are classical inputs; the claimed internal contribution is the finite-component gluing of the large-scale signed-secant argument.

# 8. Validation posture and audits

C032 is an infinite analytic theorem, not a finite arithmetic claim, so no cosmetic exact checker was created. The proof is written on the page. The explicit half-stable identities used in the specialization were already checked in C030/C031; those retained checks are self-checks, not independent audits of C032.

The inherited independent audit remains

`R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF`

for C008 only. It does **not** certify C032. I still do not locate a version-matching P26 end-to-end PASS for the complete frozen ordinary-`*` package or a distinct second end-to-end PASS from another track. C032 itself also needs independent theorem-level review. No closure label is upgraded.

# 9. Model and scheduler-control status

The requested GPT-6/maximum setting remains **not enforceable through the exposed scheduler controls**. The current 20 September owner directive records that the scheduler interface has no binding model-family selector, no reasoning-effort selector and no guaranteed full-hour execution field; applied model/effort telemetry is likewise not authenticated in this run. Therefore the report says GPT-5.6 Sol / UNVERIFIED rather than pretending the prompt preference was enforced.

Changing this would require the scheduler/product/API layer to expose and persist model-family and reasoning-effort routing fields and to return per-run attestation of what actually ran. R19 is not authorized to change scheduler configuration here, and I made no scheduler changes.

The historical P26 scheduler ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in one authorization context. Repository reconciliation records later successful modification from another authorized context. The supported workaround is therefore the owning/authorized context, ordinary supported permission/ownership repair or transfer, or platform support. There is no permission bypass.

# 10. Structured ledger delta

```yaml
ledger_delta:
  track: R19
  lane: CLOSABLE_OUTSIDE
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084"
  frozen_operation: "ordinary classical convolution mu*S_t in both classical-stable and free-stable-law branches"
  target: "eventual unimodality under exact finite (2+alpha)-moment assumption, beginning alpha=1/2"
  metric: "number of complete classical-stable/free-stable alpha=1/2 source cases proved, full input class and original skewness conventions"
  before: "2/2"
  after: "2/2"
  movement: "NO MOVEMENT in fixed metric; YES substantive structural progress"
  status: "PARTIAL / AUDIT_PENDING"
  unchanged_count: "UNKNOWN at shared-ledger level; fixed metric already saturated"
  tried_moves: [8, 14, 26]
  new_claims:
    - "R19-I0084-C032A: every finite mixture of arbitrary unimodal initial laws is eventually unimodal after convolution with any one-sided kernel satisfying the C031 mode/log-slope/critical-tail hypotheses; no moment assumption"
    - "R19-I0084-C032B: applies to both classical and free alpha=1/2 endpoint stable laws under ordinary *, plus reflections"
    - "componentwise p-th moments give s0 <= C_k[1+D+max_j M_(p,j)^(1/p)]; for alpha=1/2, t0 <= C[1+D+max_j M_(5/2,j)^(2/5)]^(1/2)"
  evidence:
    - "complete proof in this immutable report"
    - "retained C031 half-stable kernel verification"
    - "R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF for C008 only"
  audit_ids:
    - "R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF (inherited C008, not C032)"
    - "full-package P26 version-matching audit: NOT LOCATED"
    - "distinct second full-package audit: NOT LOCATED"
  remaining_obligation: "independent theorem-level audit of C032 and two version-matching end-to-end audits of the frozen ordinary-* package before closure"
  exact_new_boundary: "finite unimodal mixtures are rescued; a general countable-mixture extension is false without uniform translation/tail control, as the existing sparse endpoint counterexamples demonstrate"
  posted_exclusions: "additive Brownian-unimodality and known stable special cases earn no new credit"
  prior_art_posture: "Khintchine and general finite-mixture literature are classical; no exact C032 match located in bounded 2026-09-20 search; negative search is not a novelty certificate"
```

# 11. Next concrete attack

C032 identifies the next nontrivial boundary cleanly. The useful question is no longer `finite N`: that is solved by the theorem above. The next attack should seek a **uniform countable-mixture criterion** sharp enough to include genuinely infinite mixtures but weak enough to exclude C024--C029, for example conditions of the form

`sup_j |a_j| < infinity`

and

`sup_j P(|X_j|>R) -> 0 as R->infinity`,

possibly with no moment assumptions. Under exactly those two uniformity conditions the C032 proof appears to extend verbatim from finite maxima to suprema over countably many components. The sparse counterexamples violate the bounded-mode condition. Proving that countable extension, and then weakening bounded modes to a weighted tightness condition, is the strongest immediate route.