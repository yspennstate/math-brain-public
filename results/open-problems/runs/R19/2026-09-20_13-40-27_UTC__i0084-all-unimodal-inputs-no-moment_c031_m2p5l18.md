Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT); genuine theorem progress: every unimodal initial probability law, with no moment assumption at all, is eventually made unimodal by ordinary convolution with either alpha=1/2 endpoint kernel (classical half-stable or the law of the free half-stable distribution), and likewise after reflection. Section-B moves: #2 ATTACK THE NEGATION FIRST; #5 ADD A PARAMETER AND DIFFERENTIATE IN IT; #18 SAY IT IN ANOTHER LANGUAGE. The immediately preceding C030 triple was #4/#11/#13, so it is not repeated.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **PARTIAL / AUDIT_PENDING.** The frozen source statement is already internally refuted at extremal skewness by earlier R19 counterexamples satisfying the source moment hypothesis, while the positive interior regions are internally proved by C020/C021 using C008. The fixed alpha=`1/2` two-branch case-count metric is already saturated at `2/2`, so C031 earns no new metric credit. C031 is a new source-relevant structural theorem for the strict subclass of **unimodal initial laws**, and therefore remains PARTIAL rather than a new complete source case.

# 1. Recovery, source scope, exclusions, and continuity

I continued from the newest complete R19 checkpoint

`runs/R19/2026-09-20_12-36-54_UTC__i0084-endpoint-unimodal-rescue_c030_m4d11i13.md`

rather than restarting. At run start I read or queried the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the operative new-methods owner directive, the current R-series implementation manifest, the I0084 history, and the retained independent R18 audit of C008. `QUEUE.md` continues to assign I0084 to R19, and the current R19 implementation registry still identifies the fixed quantity as the complete classical/free half-stable cases.

The posted additive Brownian / Hasebe-Ueda Problem 3.3 result is excluded and earns no credit here. No posted Brownian result is being repackaged as stable progress.

The source convention is frozen exactly as required by the owner and by the established R19 history:

- `S_t` may be a classical stable law or the law of a free stable process;
- the hypothesis in the frozen target is the exact finite `(2+alpha)` moment;
- in both branches the operation under study is ordinary **classical convolution** `mu*S_t`.

I do **not** replace the asterisk by free convolution. The later published ALEA wording separates classical `*` and free `boxplus`; that later wording is not silently substituted into this frozen arXiv target.

Retained supported R19 progress includes:

- C008: abstract critical-tail eventual-unimodality theorem, independently audited as `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF`;
- C011/C017: endpoint counterexamples under the source moment condition;
- C020/C021: the interior free/classical positive theorems under the exact `(2+alpha)` moment;
- C022: power-moment sharpness in the interior;
- C024--C029: increasingly regular endpoint counterexamples, culminating in universal analytic/entire ultra-light examples;
- C030: a no-moment positive result when the initial law is supported on the same half-line and has its mode at the support endpoint.

C031 asks whether C030's **one-sided support restriction on the initial law** is actually necessary. It is not.

# 2. Three new-method attacks

## Move #2 — attack the negation first

I first tried to build a counterexample with an initial law that is unimodal but has mass on both sides of its mode. The earlier C024--C029 constructions all rely on separated remote bumps, so they are strongly nonunimodal and do not address this shape class.

Khintchine's representation shows why the counterexample route fails. An arbitrary law unimodal at `0` can be written

`Y = U X`,

where `U` is uniform on `[0,1]`, `X` is an arbitrary real random variable, and `U,X` are independent. Thus the two-sided law is an average of **signed uniform intervals** with one endpoint at its mode. For large stable scale `s`, the only intervals whose normalized length `|X|/s` is not small form a set of mixing probability tending to zero. The stable kernel gives enough sign margin on the remaining small intervals to dominate that vanishing exceptional probability. This destroys the obvious route to a forever-nonunimodal unimodal input and points directly to a proof.

## Move #5 — add a parameter and differentiate in it

The signed normalized interval length

`a = X/s`

is the deformation parameter. For fixed `a`, differentiation of the moving average produces the secant slope

`D_a(r) = [k(r)-k(r-a)]/a`.

As `s` grows, the mixing distribution of `a` contracts toward `0`; the derivative of the whole convolution is the expectation of these signed secant slopes. The proof becomes a quantitative stability statement for the sign pattern of `D_a` as `a -> 0`, plus a tail-probability estimate for large `|a|`.

## Move #18 — say it in another language

The original question is about modes of convolutions of probability measures. In the Khintchine language it is a statement about averages of chord slopes of one fixed kernel. The hard global issue — ruling out a late derivative recrossing — becomes a comparison between:

1. a definite negative derivative from short chords on the right tail, and
2. the largest possible positive chord from a long interval crossing back over the mode.

For the half-stable kernels those two contributions have the same `r^(-5/2)` scale, leaving only a mixing **probability**, not a moment, to control.

# 3. Abstract theorem for arbitrary unimodal input laws

For `s>0` write

`k_s(x)=s^(-1) k(x/s)`.

Translations of either the initial law or the kernel do not affect unimodality, so the formulation below places the mode of the initial law at `0` without loss.

## R19-I0084-C031A — arbitrary-unimodal eventual smoothing by a one-sided kernel

**THEOREM C031A (PROVED INTERNALLY / AUDIT PENDING).** Let `k` be a continuous probability density supported on `[e,infinity)` for some finite `e`, with a unique mode `m>e`. Assume:

1. `k` is strictly increasing on `(e,m)` and strictly decreasing on `(m,infinity)`;
2. there are `eta>0` and `kappa>0`, with `e<m-2 eta`, such that `k` is `C^2` on `[m-2 eta,m+2 eta]` and

   `k''(x) <= -kappa` on `[m-2 eta,m+2 eta]`;

3. the left logarithmic slope has a positive compact lower bound

   `lambda := inf_{e<x<=m-eta/2} k'(x)/k(x) > 0`;

4. for some `p>1`, `R_0>0`, and `c_0,C_0>0`,

   `-k'(r) >= c_0 r^(-p)` and `k(r)/r <= C_0 r^(-p)`

   for every `r>=R_0`.

Let `mu` be **any unimodal probability measure on R** with mode `0`; atoms are allowed. Then there is `s_0(mu,k)<infinity` such that

`mu*k_s`

is unimodal for every `s>=s_0`.

No moment assumption on `mu` is needed.

If additionally

`M_p = int_R |y|^p mu(dy) < infinity`,

then one may take

`s_0 <= C_k M_p^(1/p)`

for a finite constant `C_k` depending only on the fixed kernel and the displayed quantitative choices. The reflected statement holds for the reflected kernel.

# 4. Proof of C031A

## 4.1 Khintchine representation with signed mixing variable

A classical theorem of Khintchine says that a real law is unimodal with mode `0` if and only if it can be represented as

`Y = U X`,

where

`U ~ Uniform[0,1]`

and `X` is an arbitrary real random variable independent of `U`. The possibility `X<0` is exactly what removes C030's one-sided restriction.

For `a != 0` define the signed moving average

`H_a(r) = (1/a) int_0^a k(r-v) dv`,

and set `H_0(r)=k(r)`. This definition is positive also for `a<0`, because numerator and denominator reverse orientation together. Define

`D_a(r) = [k(r)-k(r-a)]/a`,   `a != 0`,

and `D_0(r)=k'(r)` wherever `k'` exists.

The rescaled convolution is

`G_s(r) := s (mu*k_s)(sr)
          = E[H_{X/s}(r)].`                                             (C031.1)

On the regions used below, differentiation under the expectation is justified by the same split used in the estimates: for `|a|` bounded away from zero, `|D_a|` is bounded by a constant times `1/|a|`; for small `|a|`, the secant lies in a fixed compact smooth interval or in a monotone tail where the explicit derivative bounds apply. Consequently

`G_s'(r)=E[D_{X/s}(r)]`                                                  (C031.2)

at every point in the smooth regions relevant to the sign analysis. Equivalently, the same inequalities can be read in terms of difference quotients if one prefers to avoid differentiation at the support edge.

Put

`a = X/s`.

All estimates below are uniform once `s` is sufficiently large.

## 4.2 To the left of the kernel support, nothing can decrease

If `r<=e`, then for `a>0` both `r` and `r-a` lie at or to the left of the support, so `D_a(r)=0` except for the harmless boundary convention. For `a=-b<0`,

`D_-b(r) = [k(r+b)-k(r)]/b >= 0`

because `k(r)=0` and `k(r+b)>=0`.

Thus

`G_s'(r)>=0` for `r<=e`.                                                 (C031.3)

## 4.3 Uniform positivity on the whole left flank

Now fix

`e<r<=m-eta`.

Let the good event be

`A_s={|X|/s <= eta/2}`.

We show that on `A_s` every signed secant has a uniform positive lower bound proportional to `k(r)`.

### Positive `a`

Take `0<a<=eta/2`.

If `r-a<=e`, then

`D_a(r)=k(r)/a >= (2/eta) k(r)`.

If `r-a>e`, the definition of `lambda` implies

`log k(r)-log k(r-a) >= lambda a`,

so

`k(r-a) <= e^(-lambda a) k(r)`

and hence

`D_a(r)
 >= [(1-e^(-lambda a))/a] k(r)
 >= c_+ k(r)`,                                                          (C031.4)

where

`c_+ := min_{0<=u<=eta/2} (1-e^(-lambda u))/u >0`

with the value at `u=0` understood as `lambda`.

### Negative `a`

Write `a=-b`, `0<b<=eta/2`. Then `r+b<=m-eta/2`, still on the increasing side. Again the log-slope lower bound gives

`k(r+b) >= e^(lambda b) k(r)`,

so

`D_-b(r)
 = [k(r+b)-k(r)]/b
 >= lambda k(r)`.                                                       (C031.5)

Thus on `A_s`,

`D_{X/s}(r) >= c_L k(r)`,                                               (C031.6)

where `c_L=min(c_+,lambda)>0`.

What can happen off `A_s`? A positive `a>eta/2` cannot create a negative secant here, because `r-a<r<=m` and `k` is nondecreasing up to the mode. A negative `a=-b<-eta/2` can overshoot the mode and become harmful, but universally

`D_-b(r)
 = [k(r+b)-k(r)]/b
 >= -k(r)/b
 >= -(2/eta) k(r)`.                                                     (C031.7)

Averaging (C031.6)--(C031.7),

`G_s'(r)
 >= k(r) [ c_L P(A_s) - (2/eta) P(X<-s eta/2) ].`                       (C031.8)

Since `X` is a finite real random variable,

`P(|X|>s eta/2) -> 0`.

Therefore the bracket in (C031.8) is positive for all sufficiently large `s`, uniformly in

`e<r<=m-eta`.

Combined with (C031.3), the density cannot have a mode before `m-eta`.

## 4.4 The central window: the derivative becomes strictly decreasing

Consider

`r in I=[m-eta,m+eta]`.

For `|a|<=eta`, the whole segment joining `r` and `r-a` lies inside

`[m-2eta,m+2eta]`.

The identity

`D_a(r)=int_0^1 k'(r-theta a) dtheta`                                  (C031.9)

holds also for negative `a`. Hence if `r_2>r_1` are in `I`, then by `k''<=-kappa`,

`D_a(r_2)-D_a(r_1)
 = int_0^1 [k'(r_2-theta a)-k'(r_1-theta a)] dtheta
 <= -kappa (r_2-r_1)`                                                   (C031.10)

for every `|a|<=eta`.

We next control the exceptional long intervals. Let

`L = sup_{x in I} |k'(x)| < infinity`.

If `a>eta`, then for `r in I` the second endpoint `r-a` lies to the left of `r`. Whenever it remains on the increasing side, its increment works in the favorable direction; otherwise discarding that favorable term gives the crude bound

`D_a(r_2)-D_a(r_1) <= (L/eta)(r_2-r_1)`.                               (C031.11)

The same bound holds for `a=-b<-eta`: the far endpoint is to the right, where monotonicity again makes its increment favorable whenever it stays beyond the mode, and dropping it yields

`D_-b(r_2)-D_-b(r_1) <= (L/eta)(r_2-r_1)`.                             (C031.12)

Averaging (C031.10)--(C031.12),

`G_s'(r_2)-G_s'(r_1)
 <= [ -kappa P(|X|<=s eta)
      +(L/eta) P(|X|>s eta) ] (r_2-r_1).`                              (C031.13)

For sufficiently large `s` the coefficient is strictly negative. Thus

`r -> G_s'(r)`

is strictly decreasing throughout `I`.

By the left-flank result,

`G_s'(m-eta)>0`                                                        (C031.14)

for large `s`. We will show next that

`G_s'(m+eta)<0`.                                                       (C031.15)

Consequently there is exactly one derivative sign crossing in the central window.

## 4.5 Uniform negativity on a moderate right interval

Choose `R>m+eta`, later enlarged for the tail estimates. On the compact interval

`[m+eta,R]`,

consider again the good event

`B_s={|X|/s<=eta/2}`.

If `|a|<=eta/2`, then every secant endpoint relevant to `r in [m+eta,R]` stays in the compact decreasing interval

`[m+eta/2,R+eta/2]`.

Set

`c_2 := min_{u in [m+eta/2,R+eta/2]} (-k'(u)) >0`.

The mean-value theorem then gives

`D_a(r) <= -c_2`                                                       (C031.16)

for every `r in [m+eta,R]` and every `|a|<=eta/2`.

A bad **negative** `a=-b` cannot contribute positively on the right of the mode: it compares `k(r+b)` with `k(r)` and `k(r+b)<=k(r)`, so

`D_-b(r)<=0`.                                                          (C031.17)

For a bad positive `a>eta/2`,

`D_a(r)^+ <= k(r)/a <= 2 ||k||_infinity/eta =: M_2`.                  (C031.18)

Therefore

`G_s'(r)
 <= -c_2 P(B_s) + M_2 P(X>s eta/2)`                                   (C031.19)

uniformly for `r in [m+eta,R]`. The second probability tends to zero while `P(B_s)->1`, proving

`sup_{r in [m+eta,R]} G_s'(r)<0`                                      (C031.20)

for all sufficiently large `s`. In particular this proves (C031.15).

## 4.6 The remote right tail: long intervals cannot create a late recrossing

Enlarge `R` so that

`R>=2R_0`, `R>=2m+2eta`,

and so that all points occurring in the good short secants lie in the region where the tail derivative bound is valid.

Fix `r>=R`.

On the good event `B_s={|a|<=eta/2}`, the entire secant lies in a bounded-width neighborhood of `r`. Since `r-eta/2>=r/2>=R_0`, the mean-value theorem and the derivative lower bound give

`D_a(r) <= -c_3 r^(-p)`                                                (C031.21)

for some `c_3>0` depending only on `c_0,p,eta` and the harmless factor comparing `(r+eta/2)^(-p)` to `r^(-p)`.

As above, every negative `a` contributes nonpositively because its far endpoint lies farther to the right on the decreasing tail.

Suppose now that `a>eta/2` and `D_a(r)>0`. Then necessarily the backward endpoint crosses sufficiently far toward the mode; in particular it cannot remain in `[m,r]`, where monotonicity would give `k(r-a)>=k(r)` and hence `D_a(r)<=0`. Thus

`a > r-m >= r/2`.

Consequently any positive contribution obeys

`D_a(r)^+
 <= k(r)/a
 <= 2 k(r)/r
 <= 2 C_0 r^(-p)`.                                                     (C031.22)

Averaging (C031.21)--(C031.22),

`G_s'(r)
 <= r^(-p) [ -c_3 P(B_s)
              +2C_0 P(X>s(r-m)) ].`                                   (C031.23)

For `r>=R`,

`P(X>s(r-m)) <= P(X>s(R-m)) <= P(|X|>s eta/2)`

once `R-m>=eta/2`. Therefore the bracket in (C031.23) is strictly negative for all sufficiently large `s`, uniformly for all `r>=R`.

Hence

`G_s'(r)<0` for every `r>=R`                                           (C031.24)

when `s` is large.

## 4.7 Conclusion

For sufficiently large `s` we have established the global sign geometry:

- no decrease before the support edge;
- strict increase on the entire left flank through `m-eta`;
- strict decrease of `G_s'` across `[m-eta,m+eta]`, with exactly one crossing;
- strict negativity on `[m+eta,R]`;
- strict negativity for every `r>=R`.

Therefore `G_s`, hence `mu*k_s`, is unimodal. This proves the qualitative no-moment assertion of C031A.

## 4.8 Quantitative scale under the p-th moment

If

`M_p=E|Y|^p<infinity`,

then from `Y=UX`, independence gives the exact identity

`E|X|^p = (p+1) M_p`,                                                  (C031.25)

because `E U^p=1/(p+1)`.

The preceding proof only requires finitely many conditions of the form

`P(|X|>s eta/2) < epsilon_k`

for fixed positive thresholds `epsilon_k` determined by `k`. Let `epsilon` be the minimum of those thresholds. Markov's inequality yields

`P(|X|>s eta/2)
 <= (p+1)M_p /(s eta/2)^p`.                                            (C031.26)

Thus it is enough that

`s >= (2/eta) [(p+1)M_p/epsilon]^(1/p)`,                              (C031.27)

proving

`s_0 <= C_k M_p^(1/p)`.

This completes C031A.

# 5. The alpha=1/2 endpoint kernels satisfy C031A

## R19-I0084-C031B — all unimodal inputs for both half-stable endpoint laws

**COROLLARY C031B (PROVED INTERNALLY / AUDIT PENDING).** Let `mu` be any unimodal probability measure on `R`, with arbitrary mode and with no moment assumption. Let `L_t` be the positive classical alpha=`1/2` stable law, and let `F_t` be the positive free alpha=`1/2` stable **law regarded as an ordinary classical convolution kernel**, as required by the frozen arXiv target. Then there is `t_0(mu)<infinity` such that, for every `t>=t_0(mu)`,

`mu*L_t` and `mu*F_t`

are unimodal.

The same statement holds for the two reflected negative endpoint laws.

If the centered `5/2` moment

`M_(5/2)=int |x-a|^(5/2) mu(dx)`

is finite, where `a` is any mode used to translate `mu` to mode `0`, then

`t_0 <= C M_(5/2)^(1/5)`                                               (C031.28)

with a kernel-dependent finite constant `C`.

### Classical half-stable kernel

At unit spatial stable scale,

`k_cl(x) = (1/sqrt(2*pi)) x^(-3/2) exp[-1/(2x)] 1_{x>0}`.

Its logarithmic derivative is

`k_cl'(x)/k_cl(x) = (1-3x)/(2x^2)`.                                   (C031.29)

Hence its unique mode is `m=1/3`. On every compact interval inside `(0,1/3)`, the logarithmic derivative is positive and has a positive minimum, establishing condition 3 after choosing a small `eta`. The exact retained kernel computation gives

`k_cl''(1/3)/k_cl(1/3) = -27/2<0`,                                    (C031.30)

so strict concavity holds on a neighborhood of the mode. Finally

`[-k_cl'(x)]/[k_cl(x)/x] = (3x-1)/(2x)`                               (C031.31)

for `x>1/3`, and `k_cl(x)/x` is a positive constant times

`x^(-5/2) exp[-1/(2x)]`.

Thus the tail assumptions hold with

`p=5/2`.

### Free half-stable law used under ordinary classical convolution

The retained explicit positive free half-stable density is

`k_fr(x) = sqrt(4x-1)/(2*pi*x^2) 1_{x>=1/4}`.                          (C031.32)

Its logarithmic derivative is

`k_fr'(x)/k_fr(x) = 2(1-3x)/[x(4x-1)]`.                               (C031.33)

Again the unique mode is `m=1/3`. On every compact interval `(1/4,1/3-eta/2]` the logarithmic derivative is positive with a positive minimum, and it diverges positively at the support edge. The retained exact calculation gives

`k_fr''(1/3)/k_fr(1/3)=-54<0`,                                        (C031.34)

hence strict concavity near the mode. Moreover

`[-k_fr'(x)]/[k_fr(x)/x]
 = 2(3x-1)/(4x-1)`,                                                    (C031.35)

which stays bounded above and bounded away from zero on a sufficiently remote right tail, while `k_fr(x)/x` is asymptotic to a positive constant times `x^(-5/2)`. Therefore C031A again applies with

`p=5/2`.

The alpha=`1/2` stable semigroup spatial scale is proportional to `s=t^2` under the retained normalization. Combining `s_0<=C M_(5/2)^(2/5)` from C031A with `s=t^2` gives

`t_0 <= C' M_(5/2)^(1/5)`,

which is (C031.28).

Reflection gives the two negative-skew endpoint statements.

# 6. What C031 changes conceptually

C024--C029 show that endpoint failure persists for remarkably light and regular **nonunimodal** initial densities: smooth, analytic, entire, strictly positive, and with extremely strong tail decay. C031 shows that the missing hypothesis is not another tail condition. A broad shape property suffices:

> **Every unimodal initial law is eventually smoothed to a unimodal law by each alpha=1/2 endpoint kernel under ordinary classical convolution.**

No moment is needed for this restricted-class theorem.

This is stronger than C030, which required the initial law to be supported on the same half-line and to have its mode at the finite endpoint. C031 permits arbitrary two-sided tails, atoms, asymmetry, and infinite moments.

It is also different from classical **strong unimodality**. Ibragimov's strong-unimodality theorem characterizes kernels whose convolution with every unimodal law is unimodal at **every fixed scale** by log-concavity of the kernel density. The half-stable kernels are not globally log-concave and need not preserve unimodality at small scales. C031 is an eventual large-scale theorem, so there is no contradiction.

# 7. Prior-art and current-source search, 20 September 2026

I checked the original arXiv source and current search results before treating C031 as new campaign progress. The arXiv source remains version 2, last revised 14 September 2018. The frozen owner-assigned source convention remains the historical arXiv ordinary-`*` target; the later published ALEA free branch uses different `boxplus` wording and is not substituted here.

Dated search themes included:

- `"Conjecture 5.5" Hasebe Ueda stable unimodality`;
- `"stable process" "unimodal distribution" convolution eventual unimodality`;
- `Khintchine representation unimodal distribution U X`;
- `Ibragimov strong unimodality convolution unimodal log concave`;
- later Hasebe/Ueda work and papers citing the 2018 article.

The search recovered:

1. Hasebe--Ueda's original arXiv/published paper;
2. the classical Khintchine representation of unimodal laws as `UX` with `U` uniform;
3. Ibragimov's 1956 strong-unimodality characterization;
4. background examples in the unimodality literature showing that convolution does not preserve unimodality in general;
5. later Hasebe/Ueda-related multiplicative/free-unimodality work, which does not state the frozen ordinary-`*` C031 theorem.

I did **not** locate a primary source stating C031A or C031B, nor a later primary theorem resolving the exact frozen arXiv ordinary-`*` Conjecture 5.5 formulation. This is bounded negative search evidence only, **not** a novelty or priority certificate.

The Khintchine and Ibragimov ingredients are classical/folklore-level inputs and must be cited as such in any paper. The contribution claimed internally here is the large-scale secant-slope argument and its stable-kernel application, not those classical representation theorems.

# 8. Validation posture and audits

C031 is an infinite analytic theorem, not a finite combinatorial claim, so no cosmetic exact-arithmetic checker was manufactured. The complete proof is written above. The already archived exact kernel identities from C030 support the explicit half-stable specialization, but they are self-checks/retained checks, not an independent audit of C031.

The retained independent audit is:

`R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF`

for the abstract C008 positive smoothing engine.

That audit does **not** automatically certify C031. I did not locate a version-matching P26 end-to-end PASS for the full frozen arXiv ordinary-`*` package, nor a distinct second full-package PASS from another track. C031 itself also needs independent theorem-level review. Therefore no closure label is upgraded.

# 9. Model/scheduler control status

The requested GPT-6/maximum setting is still **not enforceable from the exposed scheduler surface**. The available task controls expose title/prompt, schedule or relative start, timing mode, enabled state, and ordinary update fields; they do not expose a binding model-family selector, a binding reasoning-effort selector, authenticated applied-model/effort telemetry, or a guaranteed hour-long execution field. Consequently GPT-6/maximum remains prompt text only and this run honestly reports GPT-5.6 Sol / UNVERIFIED.

To make the requested setting enforceable, the scheduler/product/API layer would need persistent model-family and reasoning-effort routing fields plus per-run attestation of what actually ran. R19 is not authorized to change scheduler configuration in this run.

The historical P26 scheduler ID `6aa7b43682948191b697d72fec69d539` did return `You cannot modify this task` in one recorded authorization context. Current repository reconciliation also records that a different authorized context later succeeded in updating P26. The supported workaround is therefore to use the owning/authorized context, supported permission/ownership repair or transfer, or platform support. There is no permission bypass.

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
  movement: "NO MOVEMENT"
  status: "PARTIAL / AUDIT_PENDING"
  unchanged_count: "UNKNOWN at shared-ledger level; fixed metric already saturated"
  tried_moves: [2, 5, 18]
  new_claims:
    - "R19-I0084-C031A: any unimodal initial probability law is eventually unimodal after convolution with a one-sided kernel satisfying the stated mode/log-slope/critical-tail hypotheses; no moment assumption"
    - "R19-I0084-C031B: applies to both classical and free alpha=1/2 endpoint stable laws under ordinary *, plus reflections; centered 5/2 moment gives t0 <= C M_(5/2)^(1/5)"
  evidence:
    - "full proof in this immutable report"
    - "retained C030 exact half-stable kernel identities"
    - "R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF for C008 only"
  audit_ids:
    - "R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF (inherited C008, not C031)"
    - "full-package P26 version-matching audit: NOT LOCATED"
    - "distinct second full-package audit: NOT LOCATED"
  remaining_obligation: "independent theorem-level audit of C031 and two version-matching end-to-end audits of the frozen ordinary-* source package before closure"
  posted_exclusions: "additive Brownian-unimodality and already-known stable special cases earn no new credit"
  prior_art_posture: "Khintchine/Ibragimov inputs classical; no exact C031 match located in bounded 2026-09-20 search; negative search is not a novelty certificate"
```

# 11. Next useful direction

The fixed source-case metric cannot exceed `2/2`. If R19 is kept on I0084 despite the saturated case count, the most useful remaining mathematical direction is no longer another tail strengthening. The next structural question is to identify the weakest shape condition between arbitrary input and unimodal input that rules out the sparse oscillatory obstruction — for example a finite bound on the number of modes or a quantitative variation-diminishing condition — while preserving the exact source moment class. Any such result remains PARTIAL unless it covers the source's full input class.
