Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Fixed I0084 metric `2/2 -> 2/2` (NO MOVEMENT); genuine theorem progress: a natural shape condition rescues every alpha=1/2 endpoint branch under ordinary `*`: if the initial law is one-sided and unimodal at the matching finite endpoint, then convolution with either the classical or free half-stable endpoint kernel is eventually unimodal, with NO moment assumption at all; under the source's finite `5/2` moment one gets the scale `t >= C M_{5/2}^{1/5}`. Section-B moves: #4 PROVE SOMETHING WEAKER, COMPLETELY; #11 DUALIZE; #13 FIND WHAT ONLY INCREASES. The immediately preceding C029 triple was #23/#27/#21, so it is not repeated.**

Problem/source: Takahiro Hasebe and Yuki Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, arXiv:1710.08240v2, Conjecture 5.5 / intake I0084.

Status: **PARTIAL / AUDIT_PENDING.** The frozen source has already been refuted internally at extremal skewness by earlier R19 counterexamples, and the fixed alpha=`1/2` source-case metric is saturated at `2/2`; C030 is a new corrected sufficient theorem on a strict shape subclass and therefore earns **no additional source-case credit**. It does not claim that a restricted class solves the full source case.

# 1. Continuity and source scope

I continued from the newest complete R19 report

`runs/R19/2026-09-20_11-40-29_UTC__i0084-universal-stretched-exponential-compiler_c029_m23q27s21.md`

rather than restarting. I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current operations manifests, the I0084 intake path/history, the retained R18 audit of C008, and the available neighboring-state handoffs. The 20 September PROB10 directive reassigns selected slots but does **not** reassign R19, so this I0084 ownership remains the current target.

The frozen campaign source scope remains the one explicitly assigned by the owner and carried through R19 history:

- exact source assumption: finite `(2+alpha)` moment;
- `S_t` may be a classical stable law or the law of a free stable process;
- in this frozen target the operation is ordinary **classical convolution** `mu*S_t` in both branches.

I do not replace this `*` by `boxplus`. The later published ALEA wording distinguishes classical `*` from free `boxplus`; that later wording is not silently substituted into the frozen R19 target.

Retained supported progress includes C008 (abstract positive smoothing theorem, independently audited), C011/C017 endpoint obstructions, C020/C021 interior free/classical positive theorems, C022 critical power-moment sharpness in the interior, and C024--C029 increasingly regular universal endpoint counterexamples. C029 showed that endpoint failure persists even for one entire ultra-light initial density. The new question here is different: **what additional shape condition on the initial law restores eventual unimodality at the endpoint?**

# 2. The three new-method moves

## Move #4 — prove something weaker, completely

The unrestricted endpoint statement is false. Instead of adding a stronger tail condition, restrict only the **shape** of the initial law: put its mode at its finite support endpoint and require it to extend only in the same half-line direction as the one-sided stable kernel.

This turns out to be much stronger than merely recovering the source moment class: no moment assumption is needed.

## Move #11 — dualize

Use Khintchine's classical representation of a one-sided unimodal law. If `Y>=0` is unimodal with mode `0`, then

`Y = U X`

in distribution, where `U` is uniform on `[0,1]`, `X>=0`, and `U,X` are independent. Thus an arbitrary decreasing endpoint-unimodal density is replaced by an arbitrary mixing law over uniform intervals.

After this transformation the derivative of the stable convolution becomes an **average of secant slopes** of the stable density. This is the useful dual language.

## Move #13 — find what only increases/decreases

For every uniform-interval component the secant slope is nonnegative before the kernel mode. Near the mode it decreases monotonically, while on the remote right tail its negative contribution has exactly the same power scale as the largest possible positive contribution from a very long interval. The only quantity needed from the mixing law is a tail probability `P(X>s c)`, which tends to zero for every probability distribution. This prevents a late derivative re-crossing without any moment hypothesis.

# 3. Abstract endpoint-unimodal smoothing theorem

For `s>0`, write

`k_s(x)=s^{-1} k(x/s)`.

We first isolate the mechanism independently of stable laws.

## R19-I0084-C030A — endpoint-unimodal smoothing by a one-sided kernel

**THEOREM C030A (PROVED INTERNALLY / AUDIT PENDING).** Let `k` be a continuous probability density supported on `[0,infinity)`. Assume that there is a mode `m>0` such that:

1. `k` is nondecreasing on `(-infinity,m]` and strictly decreasing on `[m,infinity)`;
2. `k` is `C^1` on `(m,infinity)` with `k'(x)<0` for every `x>m`;
3. for some `delta>0`, `k` is strictly concave on `[m,m+delta]`;
4. for some `p>1`, `R_0>0`, and constants `c_0,C_0>0`,
   
   `-k'(r) >= c_0 r^{-p}` and `k(r)/r <= C_0 r^{-p}`
   
   for every `r>=R_0`.

Let `mu` be **any** probability measure supported on `[0,infinity)` that is unimodal with mode `0` (an atom at `0` is allowed). Then there exists `s_0(mu,k)<infinity` such that

`mu*k_s`

is unimodal for every `s>=s_0`.

No moment condition on `mu` is required.

If additionally

`M_p = int_0^infinity y^p mu(dy) < infinity`,

then one may take

`s_0 <= C_k M_p^{1/p}`

for a finite constant `C_k` depending only on the fixed kernel `k` and on the displayed choice of `delta,R_0,c_0,C_0`.

The reflected statement holds for a law supported on `(-infinity,0]` with mode `0` and the reflected kernel.

# 4. Proof of C030A

## 4.1 Khintchine representation and the secant-slope formula

By Khintchine's representation theorem for unimodal laws, there exist independent random variables

`U ~ Uniform[0,1]`, `X>=0`

such that

`Y := U X ~ mu`.

For `a>0` define the moving average

`H_a(r) = (1/a) int_0^a k(r-v) dv`,

and set `H_0(r)=k(r)`. Also define

`D_a(r) = [k(r)-k(r-a)]/a` for `a>0`,

`D_0(r)=k'(r)` whenever the latter is used on the smooth side of the mode.

The rescaled convolution density is

`G_s(r) := s (mu*k_s)(sr)
          = E[ H_{X/s}(r) ].`

For `r>=m`, differentiation under the expectation is legitimate and gives

`G_s'(r) = E[ D_{X/s}(r) ].`                                           (C030.1)

A uniform domination is easy: when `a<=m/2`, the relevant secant lies in `[m/2,infinity)` and is bounded by a fixed bound for `|k'|`; when `a>m/2`,

`|D_a(r)| <= 2 ||k||_infinity/a <= 4||k||_infinity/m`.

Thus (C030.1) does not require an integrability assumption on `X`.

## 4.2 Nothing can decrease before the kernel mode

Fix `a>=0`. For every `r<=m`, we have `r-a<=r<=m`, and `k` is nondecreasing on that entire region (with `k=0` to the left of its support). Therefore

`D_a(r)>=0`

where expressed as a derivative, equivalently `H_a` is nondecreasing on `(-infinity,m]`. Averaging over `X` gives

`G_s is nondecreasing on (-infinity,m]`                                  (C030.2)

for every `s>0`.

## 4.3 A single crossing in a fixed mode window

Consider `r in [m,m+delta]`. For each fixed `a>=0`, the function `r -> D_a(r)` is strictly decreasing.

- If `r-a<=m`, then as `r` increases, `k(r)` strictly decreases while `k(r-a)` is nondecreasing, so the numerator strictly decreases.
- Once `r-a>=m`, both endpoints of the secant lie in `[m,m+delta]`; strict concavity of `k` implies that the secant slope strictly decreases as the interval translates to the right.
- The two descriptions match at the crossing `r-a=m`.
- For `a=0`, strict concavity says `k'` is strictly decreasing.

Hence

`r -> G_s'(r)`

is strictly decreasing on `[m,m+delta]`. At `r=m`, every secant is nonnegative, so

`G_s'(m)>=0`.                                                           (C030.3)

At the right endpoint `r=m+delta`, split according to

`A_s := {X/s <= delta/2}`.

On `A_s`, the mean-value theorem places the secant inside `[m+delta/2,m+delta]`. With

`c_1 := min_{u in [m+delta/2,m+delta]} (-k'(u)) > 0`,

we have

`D_{X/s}(m+delta) <= -c_1`.

On `A_s^c`, only a positive upper bound is needed:

`D_{X/s}(m+delta)^+ <= 2||k||_infinity/delta =: M_1`.

Thus, with

`eta_s := P(X > s delta/2) -> 0`,

`G_s'(m+delta) <= -c_1(1-eta_s)+M_1 eta_s <0`                           (C030.4)

for all sufficiently large `s`.

By strict decrease of `G_s'` in the mode window, there is exactly one sign crossing there (or the crossing is at `m` in the degenerate `mu=delta_0` type case).

## 4.4 Uniform negativity on the moderate right region

Increase a constant `R` if necessary so that

`R > m+delta`.

For `r in [m+delta,R]` and `X/s<=delta/2`, the entire secant interval lies inside `[m+delta/2,R]`. Put

`c_2 := min_{u in [m+delta/2,R]} (-k'(u)) >0`.

Then

`D_{X/s}(r) <= -c_2`.

For `X/s>delta/2`, again

`D_{X/s}(r)^+ <= M_1`.

Consequently

`sup_{r in [m+delta,R]} G_s'(r)
 <= -c_2(1-eta_s)+M_1 eta_s <0`                                        (C030.5)

for all sufficiently large `s`.

## 4.5 The remote tail: the critical cancellation

Now take `R` large enough that `R/2>=R_0` and `R/2>m`. Fix `r>=R` and split according to

`B_{s,r}:={X/s <= r/2}`.

On `B_{s,r}`, the secant interval lies inside `[r/2,r]`. The mean-value theorem and the derivative lower bound give

`D_{X/s}(r) <= -c_0 r^{-p}`.                                           (C030.6)

On `B_{s,r}^c`, a positive contribution can only be as large as

`D_{X/s}(r)^+
 <= k(r)/(X/s)
 <= 2 k(r)/r
 <= 2 C_0 r^{-p}`.                                                     (C030.7)

Since `r>=R`,

`P(B_{s,r}^c)=P(X>sr/2) <= P(X>sR/2)=:zeta_s ->0`.

Therefore, uniformly for every `r>=R`,

`G_s'(r)
 <= r^{-p}[-c_0(1-zeta_s)+2C_0 zeta_s] <0`                             (C030.8)

for all sufficiently large `s`.

This is the decisive point. The remote positive contribution from an arbitrarily long uniform interval has size at most `k(r)/r`, while the normal negative tail derivative has the same power `r^{-p}`. Thus only a tail **probability** of the Khintchine mixing variable appears; no moment is needed.

Combining (C030.2), the unique central crossing, (C030.5), and (C030.8), `G_s` is nondecreasing up to one mode and nonincreasing thereafter. This proves eventual unimodality.

## 4.6 Quantitative scale under the p-th moment

Choose

`epsilon < min{
 c_1/(c_1+M_1),
 c_2/(c_2+M_1),
 c_0/(c_0+2C_0)
}`.

It is enough that

`P(X>s delta/2)<epsilon`.

If `E Y^p=M_p<infinity`, independence of `U,X` gives the exact Khintchine moment identity

`E X^p = (p+1) M_p`,                                                    (C030.9)

because `E U^p=1/(p+1)`. Markov's inequality therefore shows that it suffices to take

`s >= (2/delta) [ (p+1)M_p/epsilon ]^{1/p}`.                            (C030.10)

This proves `s_0 <= C_k M_p^{1/p}`.

# 5. Application to the frozen alpha=1/2 stable endpoint branches

## 5.1 Classical positive half-stable kernel

At unit stable scale the classical positive half-stable density is

`k_cl(x) = (1/sqrt(2*pi)) x^(-3/2) exp[-1/(2x)] 1_{x>0}`.

Its logarithmic derivative is exactly

`k_cl'(x)/k_cl(x) = (1-3x)/(2x^2)`,                                    (C030.11)

so it has unique mode

`m=1/3`.

The exact checker gives

`k_cl''(1/3)/k_cl(1/3) = -27/2 <0`,                                    (C030.12)

hence strict concavity on a neighborhood to the right of the mode. Moreover

`(-k_cl'(x))/(k_cl(x)/x) = (3x-1)/(2x)`,                               (C030.13)

which lies in `[1,3/2)` for `x>=1`. Since

`k_cl(x)/x = const * x^(-5/2) exp[-1/(2x)]`,

conditions (3)--(4) hold with

`p=5/2`.

## 5.2 Positive free half-stable law, used only as an ordinary convolution kernel

The retained explicit density is

`k_fr(x) = sqrt(4x-1)/(2*pi*x^2) 1_{x>=1/4}`.                           (C030.14)

Translate it by `1/4` to put its support at `[0,infinity)`; translation does not affect unimodality of any convolution. Before translation its logarithmic derivative is

`k_fr'(x)/k_fr(x) = 2(1-3x)/(x(4x-1))`,                               (C030.15)

so its unique mode is again `x=1/3`. The exact checker gives

`k_fr''(1/3)/k_fr(1/3) = -54<0`.                                      (C030.16)

Also

`(-k_fr'(x))/(k_fr(x)/x)
 = 2(3x-1)/(4x-1)`,                                                    (C030.17)

which lies in `[4/3,3/2)` for `x>=1`, while

`k_fr(x)/x
 = [sqrt(4-1/x)/(2*pi)] x^(-5/2)`.

Thus C030A applies with the same critical exponent

`p=5/2`.

Crucially, this use of the free half-stable law is only as the density of a **classical convolution kernel**, exactly as required by the frozen R19 target.

# 6. R19-I0084-C030B — corrected endpoint theorem

**COROLLARY C030B (PROVED INTERNALLY / AUDIT PENDING; RESTRICTED INPUT SHAPE, SO PARTIAL).** Let `S_t` be either

1. the positive classical alpha=`1/2` stable process law, or
2. the positive free alpha=`1/2` stable process law, regarded under ordinary classical convolution.

Let `mu` be any probability law supported on `[a,infinity)` and unimodal with mode at its finite left endpoint `a`. Then

`mu*S_t`

is unimodal for all sufficiently large `t`.

**No moment assumption is required.**

For the reflected negative endpoint laws, the same conclusion holds when `mu` is supported on `(-infinity,a]` and has its mode at the right endpoint `a`.

In particular, every such `mu` satisfying the frozen source's exact `5/2`-moment hypothesis is covered, but the theorem is stronger on this shape subclass.

# 7. R19-I0084-C030C — source-scale quantitative bound

For a strictly `1/2`-stable semigroup the spatial scale is `s=t^2`. Let

`M_{5/2}^{(a)} = int |x-a|^(5/2) mu(dx)`.

C030.10 therefore yields

`t^2 >= C [M_{5/2}^{(a)}]^(2/5)`,

or equivalently

`boxed{ t >= C' [M_{5/2}^{(a)}]^(1/5) }`.                              (C030.18)

The exponent `1/5` is exactly the source-critical scaling `alpha/(2+alpha)` at `alpha=1/2`.

This is not needed for the qualitative no-moment theorem; it records what the exact source moment buys quantitatively.

# 8. Exact self-check

The finite symbolic kernel identities were checked exactly with SymPy after the theorem was obtained, not before it.

Checker:

`artifacts/R19/2026-09-20_12-36-54_UTC__i0084_c030_endpoint_unimodal_checker.py`

creation commit: `41cea26a238c05a46c7c94cbaa8f5d158fe4dfea`

Executed output:

`artifacts/R19/2026-09-20_12-36-54_UTC__i0084_c030_endpoint_unimodal_checker.out`

creation commit: `cc5ac2dba647f8d2ee72566f0c6dab63b958a37e`

The archived output verifies the exact logarithmic derivatives, common mode `1/3`, negative curvature ratios `-27/2` and `-54`, and the exact rational tail-ratio identities used above.

This is a self-check, not an independent audit.

# 9. Prior-art and current-status search — 2026-09-20

Fresh bounded searches this run covered:

- Hasebe--Ueda arXiv:1710.08240 / ALEA 15 and Conjecture 5.5;
- later Hasebe/Ueda unimodality work and stable-process papers;
- Khintchine/Khintchine representation of a unimodal law as `UX` with `U` uniform;
- scale mixtures of uniforms / monotone-density representation;
- convolution of unimodal distributions and strong unimodality;
- positive stable density unimodality and one-sided free stable shape results;
- phrases combining endpoint/monotone initial laws with stable convolution eventual unimodality.

Known ingredients that must not be presented as new:

1. Khintchine's representation itself is classical; Olshen--Savage and later expositions explicitly state the equivalence `Z` unimodal at `0` iff `Z=UX` with `U~Unif[0,1]` independent of `X`.
2. Hasebe--Ueda already prove eventual unimodality for the classical positive half-stable kernel under **compact support** of the initial law.
3. General convolution of two unimodal laws need not be unimodal; log-concavity/strong unimodality is a distinct classical sufficient mechanism.
4. The stable kernels themselves are known to be unimodal; later work proves finer bell/whale-shape properties.

I did **not** locate a primary theorem stating C030A's no-moment endpoint-unimodal criterion, or the simultaneous classical/free alpha=`1/2` ordinary-`*` corollary C030B. That is bounded negative evidence only; it is **not** a novelty or priority certificate.

The key mechanism here is the combination of the classical Khintchine representation with the critical secant-slope tail comparison (C030.6)--(C030.8). That combination should be checked against older variation-diminishing / shape-preserving convolution literature before publication.

# 10. Why this changes the endpoint picture

The retained counterexamples C024--C029 show that at extremal half-stable skewness, arbitrarily strong tail decay and even entire positive densities do not rescue arbitrary initial laws. C030 shows that a very simple **shape** hypothesis does:

- tail control alone: insufficient, even at extremely strong levels;
- compact support: sufficient by the source for the classical half-stable branch;
- endpoint unimodality in the matching half-line direction: sufficient for both classical and free half-stable ordinary-convolution branches, even with no moments.

Thus the natural repair to the false unrestricted endpoint conjecture is geometric/shape-theoretic rather than another tail hypothesis.

# 11. Audit and closure posture

Retained independent evidence:

- `R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF` for C008;
- narrower historical half-stable/endpoint checks remain preserved.

Still missing for repository closure:

- independent theorem-level audit of C021--C030 as applicable;
- a version-matching P26 end-to-end PASS for the complete frozen arXiv ordinary-`*` package;
- a distinct second end-to-end PASS from another track.

Therefore **repository closure is not claimed**. C030 is a restricted corrected theorem and remains `PARTIAL / AUDIT_PENDING` even though its proof is complete on this page.

# 12. Model and scheduler controls

The currently exposed scheduler/task-control interface still supports prompt/title, schedule/timing, enablement and ordinary task updates but exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed one-hour execution field**. Thus `GPT-6 / maximum` remains prompt text only; this report truthfully records `GPT-5.6 Sol / UNVERIFIED`.

The historical P26 error `You cannot modify this task` was context/authorization-specific. Repository operations records later successful P26 updates from an authorized context. The supported workaround is therefore the owning/authorized context, supported permission or ownership repair/transfer, or platform support — never a bypass or duplicate unauthorized task. Making GPT-6/maximum enforceable would require explicit persisted model/effort fields and trustworthy per-run runtime attestation in the scheduler/product/API surface.

# 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R19
  lane: CLOSABLE_OUTSIDE
  source: "Takahiro Hasebe and Yuki Ueda, arXiv:1710.08240v2, Conjecture 5.5 / I0084"
  source_version_scope: "frozen R19 scope: ordinary classical convolution mu*S_t for both classical-stable and free-stable-law branches"
  fixed_metric: "number of complete classical-stable/free-stable alpha=1/2 source cases proved, retaining full input class and original skewness conventions"
  before: "2/2"
  after: "2/2"
  metric_movement: "NO MOVEMENT"
  unchanged_count: "UNKNOWN for saturated headline metric; not inferred from saturation"
  substantive_stagnation_this_run: 0
  status: "SOURCE REFUTED MATHEMATICALLY INTERNALLY; C030 PARTIAL / AUDIT_PENDING because it restricts the input shape"
  tried_moves: [4, 11, 13]
  move_note: "second-cycle reuses after historical exhaustion of the 30-method list; immediately preceding C029 triple was 23/27/21"
  new_claims:
    - "C030A: abstract no-moment eventual-unimodality theorem for endpoint-unimodal input convolved with a one-sided kernel having a nondegenerate mode and matched derivative/density tail power"
    - "C030B: applies to both positive classical and positive free alpha=1/2 endpoint kernels under ordinary *, with reflected negative-endpoint version"
    - "C030C: under the source 5/2 moment, t >= C M_{5/2}^{1/5} suffices"
  source_case_credit: "none; restricted shape subclass is PARTIAL by contract"
  remaining_obligation: "independent audit of C030 and end-to-end version-matching audits of the full frozen ordinary-* package; prior-art search in older shape-preserving/variation-diminishing convolution literature"
  evidence:
    checker: "artifacts/R19/2026-09-20_12-36-54_UTC__i0084_c030_endpoint_unimodal_checker.py @ 41cea26a238c05a46c7c94cbaa8f5d158fe4dfea"
    checker_output: "artifacts/R19/2026-09-20_12-36-54_UTC__i0084_c030_endpoint_unimodal_checker.out @ cc5ac2dba647f8d2ee72566f0c6dab63b958a37e"
  retained_audits:
    - "R18-AUDIT-R19-I0084-C008-ABSTRACT-003 = PASS_FULL_MATHEMATICAL_PROOF"
  full_package_audits: "missing required P26 + distinct second version-matching end-to-end PASS"
```
