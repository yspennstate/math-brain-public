Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED by runtime metadata — GPT-6 maximum was requested, but the exposed scheduler/runtime surface has no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **METRIC MOVEMENT: 4 -> 5 genuinely distinct nonparabolic shape families; Section-B moves tried: #24 FIND THE EXTREMAL OBJECT, #11 DUALIZE, #27 SWAP THE QUANTIFIERS.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the open-ended source problem is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 5: positive-seam superdiffusive gauges

Run date: 2026-09-17 Asia/Jerusalem / 2026-09-16 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Fixed metric and continuity

The frozen metric is the number of genuinely nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

Previous authoritative report:

`runs/R07/20260916T2026Z_i0077_outward_corrugations_04.md`.

It records metric `4` from:

1. the two-power cusp `u^alpha+u^beta`, `0<alpha<1/2<beta`;
2. the logarithmic cusp with regular-variation index `1/2` at both ends;
3. the pure-power family `u^beta`, with its subcritical/critical/supercritical phase portrait around `beta=1/2`;
4. outward `o(sqrt u)` corrugations of a parabolic strip, with the exact source Theorem-4.3 asymptotic threshold retained and pointwise existence inherited by inclusion.

This run proves a complete amplitude theorem for **positive-seam superdiffusive gauges**. The canonical representative is

\[
f_*(u)=1+u^{3/4}.
\]

This is not a parameter change of any of the four preceding families. In particular, its far-past regular-variation exponent is `3/4`, whereas the parabolic/logarithmic/corrugation families have exponent `1/2`; and unlike the zero-seam pure-power/two-power families it has a positive cross-section at the terminal time. Even allowing affine Brownian time-space symmetries, `1+u^{3/4}` is not of the form `A(u+b)^{3/4}`: asymptotic exponent comparison forces the same exponent, while expansion of `A(u+b)^{3/4}` has first correction of order `u^{-1/4}` after the leading `u^{3/4}` term, not a nonzero constant correction. Thus this canonical representative is not a trivial translate/rescale of the previous pure-power family.

Therefore

\[
\boxed{4\longrightarrow5.}
\]

`unchanged_count` resets to `0`.

## 2. Required repository continuity / admission / neighboring work

Before new mathematics I reread/rechecked current `master`:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- newest own report `runs/R07/20260916T2026Z_i0077_outward_corrugations_04.md` and the three earlier I0077 reports;
- newest same-source neighboring report `runs/R15/20260916_2056Z_i0076_two_ray_smoothing_a17.md`; R15 owns distinct Problem 7.2 / I0076;
- R06's independent scoped audit of the earlier R07 super-LIL gauge compiler, `R06-AUDIT-R07-I0077-T2-20260916T1922Z: PASS_SCOPED / NOVELTY_UNVERIFIED`;
- the C29 duplicate-exclusion record for I0077;
- targeted intake/repository searches for I0077 / Problem 7.8 and previous attempts.

`INDEX.md` and `RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. `QUEUE.md` still distinguishes I0077 from R15's I0076. The canonical I0077 reservation remains exclusive to R07, although its shared-file status text still reads `PENDING_ADMISSION`; this worker does not mutate shared operational files. The direct owner assignment in the current task is the operative authorization for this run.

The large `probability_1000_intake_*/problems.jsonl` files cannot be rendered row-by-row through the connector without truncation. I therefore record the whole-intake reread honestly as **PARTIAL / targeted due connector limits**. Exact I0077/source/ownership, duplicate attempts, and neighboring Burdzy–Scheutzow scopes were rechecked. I did not use a stale `admitted=true` flag as permission.

No other track's file was edited.

## 3. Primary source recovered again

Primary PDF checked directly this run:

`https://math.washington.edu/sites/math/files/documents/research/1302.6958.pdf`.

Definition 2.1: an FBM is a continuous real-indexed process `X` with random witness times `S_n -> -infinity` a.s. such that, for every n,

\[
(X_{S_n+t}-X_{S_n})_{t\ge0}
\]

is standard Brownian motion.

Definition 2.2: a decomposable FBM is obtained by concatenating independent Brownian pieces stopped at a.s.-finite stopping times whose durations diverge in both index directions.

For the parabolic strip

\[
c_1\sqrt{|t|}\le x\le c_2\sqrt{|t|},
\qquad t\le0,
\]

source Theorem 4.3 states:

1. if `lambda_0(c1,c2)>=1`, every FBM has the universal normalized-growth obstruction;
2. if `lambda_0(c1,c2)<=1`, a decomposable FBM exists with the corresponding asymptotic normalized confinement;
3. if `c1<=0<=c2` and `lambda_0(c1,c2)<1`, a decomposable FBM exists pointwise inside the strip for every `t<=0`.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

Problem 7.9 is the distinct forward-Lévy question. The intake trailing text from 7.9 is not part of I0077.

## 4. Current-status / prior-art pass — dated 2026-09-17 Asia/Jerusalem

Fresh bounded queries this run included:

- exact title + `Problem 7.8`;
- `decomposable forward Brownian` + `moving boundary`;
- `forward Brownian motion` + `space-time shapes`;
- Burdzy / Scheutzow later-author and citing-paper searches;
- ordinary Brownian `superdiffusive boundary`, `t^beta`, `1+t^beta`, and moving-boundary integral-test searches.

I found no later paper explicitly resolving Burdzy–Scheutzow Problem 7.8 or stating the decomposable-FBM positive-seam gauge theorem below. This is **bounded negative evidence only, not a novelty certificate**.

Relevant ordinary-Brownian prior art includes Aurzada–Kramm, *First exit of Brownian motion from a one-sided moving boundary* (arXiv:1203.4691), revisiting Uchiyama's moving-boundary integral test. Brownian LIL, compact-interval small-ball positivity, ergodicity of integer shifts of two-sided Wiener increments, and stopping-time concatenation are all classical ingredients. I do **not** claim those ingredients are new. The source-specific content here is their use to produce an all-time decomposable-FBM confinement theorem for a new class of nonparabolic shapes.

## 5. Move #24 — FIND THE EXTREMAL OBJECT: the apparent parabolic bottleneck is not the real threshold

Take the canonical rounded power

\[
f_*(u)=1+u^{3/4}.
\]

The normalized width `f_*(u)/sqrt(u)` tends to `infinity` both as `u downarrow 0` and `u->infinity`, so it has a finite positive bottleneck at some intermediate scale. A first attempt was to use the narrowest inscribed parabolic strip as the extremal object. That would give only a **positive sufficient amplitude threshold** inherited from source Theorem 4.3(iii).

I attacked that threshold as a possible necessity before proving anything new. It is not necessary. The terminal-time construction below works for **every** positive amplitude, however small. Thus the extremal finite-time bottleneck seen by a static inscribed parabola is not the correct invariant for decomposable FBMs.

This is not a refutation of the source problem; it falsifies only a proposed spectral-extension route.

## 6. Move #11 — DUALIZE: replace tube geometry by recurrence of good terminal times

Instead of asking whether a Brownian path started at the seam survives the whole tube, look at the dual object:

> terminal times `n` at which the **reversed Brownian past ending at n** lies in the tube.

For a two-sided Brownian path, integer re-rooting is an ergodic Bernoulli shift. Therefore any positive-probability whole-past tube event recurs with positive density. The first recurrent terminal time that also has a small endpoint displacement is an a.s.-finite stopping time for a one-sided Brownian motion. Independent copies of those stopping rules can then be concatenated backward.

For zero-seam gauges the previous R07-T2 theorem needed a local-LIL widening hypothesis. A positive seam changes the dual recurrence problem qualitatively: local Brownian roughness no longer creates any obstruction at the terminal time.

## 7. Move #27 — SWAP THE QUANTIFIERS: every positive amplitude, not merely sufficiently large amplitudes

The static-parabolic comparison naturally asks:

> for a fixed gauge, is there a sufficiently large `C` for which a confined decomposable FBM exists?

The dual terminal-time view proves the stronger quantifier order:

\[
\boxed{
\text{for every }C>0,
\text{ there exists a decomposable FBM confined in the }C\text{-tube.}
}
\]

This produces a complete amplitude phase portrait: critical infimum amplitude zero, but zero itself is unattainable.

# 8. I0077-R07-T6 — positive-seam superdiffusive gauge theorem

**Status: PROVED.**

Let

\[
f:[0,\infty)\to(0,\infty)
\]

be continuous and nondecreasing. Assume

\[
f(0)=a>0
\tag{T6.1}
\]

and

\[
\frac{f(u)}{\sqrt{u\log\log u}}
\longrightarrow\infty
\qquad(u\to\infty),
\tag{T6.2}
\]

with the logarithm interpreted in the usual large-`u` LIL range.

Then for every `C>0` there exists a decomposable forward Brownian motion `X`, normalized by `X_0=0`, such that

\[
\boxed{
|X_t|\le C f(|t|)
\qquad\forall t\le0,
\quad\text{a.s.}
}
\tag{T6.3}
\]

Moreover, ordinary two-sided Brownian motion already satisfies the corresponding asymptotic statement

\[
\boxed{
\frac{|W_{-u}|}{f(u)}\longrightarrow0
\qquad(u\to\infty)
\quad\text{a.s.}
}
\tag{T6.4}
\]

while amplitude `C=0` is impossible for any FBM on the whole negative half-line.

Thus this shape family has exact source-appropriate amplitude phase:

\[
\boxed{
C>0:\ \text{pointwise decomposable-FBM existence};
\qquad
C=0:\ \text{impossible}.
}
\tag{T6.5}
\]

## 9. Complete proof of T6

### Step 1. A Brownian path has positive probability to stay in the whole positive-seam tube

Fix `c>0` and let `B` be standard Brownian motion. We prove

\[
p_c:=
\mathbb P\{|B_s|\le c f(s)\ \forall s\ge0\}>0.
\tag{9.1}
\]

Let `Z` be another standard Brownian motion. For `R>0`, define

\[
H_R=
\sup_{u\ge0}
\frac{|Z_u|}{f(R+u)}.
\tag{9.2}
\]

We claim

\[
H_R\to0
\quad\text{in probability as }R\to\infty.
\tag{9.3}
\]

For `0<=u<=R`, monotonicity gives `f(R+u)>=f(R)`, so by the reflection principle,

\[
\mathbb P\left(
\sup_{0\le u\le R}
\frac{|Z_u|}{f(R)}>\varepsilon
\right)
\le
4\exp\left(-\frac{\varepsilon^2 f(R)^2}{2R}\right)
\longrightarrow0,
\tag{9.4}
\]

because (T6.2) implies `f(R)^2/R -> infinity`.

For `u>=R`, monotonicity gives `f(R+u)>=f(u)`. Brownian LIL plus (T6.2) yields

\[
\frac{|Z_u|}{f(u)}\to0
\quad\text{a.s.},
\]

hence, pathwise,

\[
\sup_{u\ge R}\frac{|Z_u|}{f(u)}\to0.
\tag{9.5}
\]

Combining (9.4) and (9.5) proves (9.3).

Choose deterministic `R` so large that

\[
\mathbb P(H_R\le c/2)>0.
\tag{9.6}
\]

The compact-interval Brownian small-ball event

\[
A_R=
\left\{
\sup_{0\le s\le R}|B_s|
\le \frac{c a}{2}
\right\}
\tag{9.7}
\]

has strictly positive probability. Conditional on `B_R`, the future increment process

\[
Z_u:=B_{R+u}-B_R
\]

is an independent standard Brownian motion. On `A_R` and `{H_R<=c/2}`, for `0<=s<=R`,

\[
|B_s|\le ca/2\le c f(s),
\]

and for `s=R+u`,

\[
|B_{R+u}|
\le |B_R|+|Z_u|
\le \frac{ca}{2}+rac c2 f(R+u)
\le c f(R+u),
\]

because `a=f(0)<=f(R+u)`.

The two events in the last paragraph depend respectively on the Brownian path through time `R` and on the independent future increments, so their intersection has positive probability. This proves (9.1).

### Step 2. Good reversed terminal times recur almost surely

Let `W` be two-sided Brownian motion and let the integer re-rooting map be

\[
(\theta_nW)(t)=W(n+t)-W(n).
\]

Under two-sided Wiener measure, `theta_1` is ergodic: the path can be encoded by its i.i.d. Brownian unit-increment segments, so integer re-rooting is a Bernoulli shift.

Define the whole-past good event

\[
\mathcal A_c=
\left\{
|W_0-W_{-s}|
\le c f(s)
\quad\forall s\ge0
\right\}.
\tag{9.8}
\]

The reversed past of two-sided Brownian motion is standard Brownian motion, so Step 1 gives

\[
\mathbb P(\mathcal A_c)=p_c>0.
\]

By Birkhoff's ergodic theorem, almost surely a positive density of positive integers `n` satisfy `theta_nW in A_c`. In particular, infinitely many `n` satisfy

\[
|W_n-W_{n-s}|
\le c f(s)
\qquad\forall 0\le s\le n.
\tag{9.9}
\]

The restriction `B_t=W_t-W_0`, `t>=0`, is ordinary one-sided Brownian motion, so (9.9) is an almost-sure statement for standard Brownian motion.

Also, by Brownian LIL and (T6.2),

\[
\frac{|B_n|}{f(n)}\to0
\qquad(n\to\infty)
\quad\text{a.s.}
\tag{9.10}
\]

Hence, for every `delta>0` and every `a_0>=1`, the integer-valued time

\[
T(a_0,\delta,c)
=
\inf\left\{
 n\in\mathbb N:n\ge a_0,
\ |B_n-B_{n-s}|\le c f(s)\ \forall 0\le s\le n,
\ |B_n|\le\delta f(n)
\right\}
\tag{9.11}
\]

is finite almost surely.

It is a stopping time for the Brownian filtration: for each integer `n`, the qualifying event in braces is measurable from `(B_s)_{0<=s<=n}`; the first qualifying integer therefore has `{T<=n}` in `F_n`.

### Step 3. Concatenate independent good pieces

Fix the desired amplitude `C>0` and set

\[
c=C/2,
\qquad
\delta_m=C2^{-m-1},
\quad m\ge1.
\tag{9.12}
\]

Then

\[
\sum_{m\ge1}\delta_m=C/2.
\tag{9.13}
\]

Take independent standard Brownian motions `B^{-m}`, `m>=1`, and for each define

\[
T_{-m}=T(1,\delta_m,c).
\]

Every `T_{-m}` is an a.s.-finite stopping time and `T_{-m}>=1`. Let

\[
S_0=0,
\qquad
S_{-m}=-\sum_{j=1}^mT_{-j}.
\tag{9.14}
\]

Thus `S_{-m}->-infinity`. Concatenate the stopped pieces according to Definition 2.2; on nonnegative indices use arbitrary independent unit Brownian pieces. The resulting whole-line process `X` is decomposable, hence FBM.

Fix `m>=1` and a time

\[
t\in[S_{-m},S_{-m+1}].
\]

Set

\[
r=S_{-m+1}-t\in[0,T_{-m}],
\qquad
u=-t
=r+\sum_{j=1}^{m-1}T_{-j}.
\tag{9.15}
\]

Express the current point from the right endpoint of its Brownian piece:

\[
X_t
=
X_{S_{-m+1}}
+
B^{-m}_{T_{-m}-r}-B^{-m}_{T_{-m}}.
\tag{9.16}
\]

The good-terminal condition gives

\[
|B^{-m}_{T_{-m}-r}-B^{-m}_{T_{-m}}|
\le c f(r).
\tag{9.17}
\]

The right-endpoint displacement is the accumulated displacement of the later pieces. Therefore

\[
|X_{S_{-m+1}}|
\le
\sum_{j=1}^{m-1}
|B^{-j}_{T_{-j}}|
\le
\sum_{j=1}^{m-1}
\delta_j f(T_{-j}).
\tag{9.18}
\]

By (9.15), every `T_{-j}` occurring in (9.18) and the partial time `r` are at most `u`. Since `f` is nondecreasing,

\[
|X_t|
\le
\left(
\sum_{j=1}^{m-1}\delta_j+c
\right)f(u)
\le
\left(
\frac C2+rac C2
\right)f(u)
=Cf(|t|).
\tag{9.19}
\]

This holds simultaneously for every negative-time piece, proving (T6.3).

### Step 4. Asymptotic statement and sharp amplitude endpoint

For ordinary two-sided Brownian motion `W`, Brownian LIL and (T6.2) give

\[
|W_{-u}|/f(u)\to0
\qquad(u\to\infty),
\]

which is (T6.4).

If `C=0` and an FBM satisfied `|X_t|<=0` for every `t<=0`, then `X_t=0` on the whole negative half-line. Choose any FBM witness time `S_n<0`. On the nontrivial interval `0<=s<=-S_n`,

\[
X_{S_n+s}-X_{S_n}=0,
\]

contradicting the requirement that this process be standard Brownian motion. Thus `C=0` is impossible.

This proves T6 completely. `QED`

# 10. I0077-R07-T7 — rounded superdiffusive power tubes

**Status: PROVED as a direct corollary of T6.**

For every `beta>1/2`, every `A>0`, and every `C>0`, define

\[
\mathcal R_{A,\beta,C}
=
\{(t,x):t\le0,\ |x|\le C(A+|t|^\beta)\}.
\tag{10.1}
\]

The gauge

\[
f(u)=A+u^\beta
\]

is continuous, nondecreasing, has positive seam `f(0)=A`, and satisfies

\[
\frac{f(u)}{\sqrt{u\log\log u}}
\sim
\frac{u^{\beta-1/2}}{\sqrt{\log\log u}}
\to\infty.
\]

Therefore for every positive amplitude `C` there exists a decomposable FBM pointwise confined in `R_{A,beta,C}` for all `t<=0`.

All choices of `A,beta,C` are counted as **one** positive-seam rounded-power/gauge family, not separate metric points. The canonical representative is `A=1,beta=3/4`.

# 11. Why this is not a fifth copy of an earlier family

The new theorem is not being counted because a parameter changed.

- R07-T2 required a **zero seam**, `f(0)=0`, and a local super-LIL widening condition. The new family has a **strictly positive seam** and needs no local-LIL condition at all.
- Pure-power and mixed-power cusps collapse to a point at their terminal tip. The canonical rounded boundary `1+u^{3/4}` does not.
- The previous parabolic/logarithmic/outward-corrugation families have far-past regular-variation exponent `1/2`; the canonical rounded family has exponent `3/4`.
- The canonical `1+u^{3/4}` is not an affine Brownian time translate/rescale of `u^{3/4}`, as noted in Section 1.

So the metric movement `4->5` respects the frozen no-trivial-rescaling convention.

# 12. Route ledger / failures preserved

New failed or insufficient routes this run:

1. **Static inscribed-parabola threshold as a necessary condition — FALSE AS A ROUTE.** It gives a positive sufficient amplitude, but T6 proves every `C>0` works.
2. **A universal lambda_0-type positive critical width for all parabolic-tail-like shapes — FALSE AS A HEURISTIC.** Positive seam + superdiffusive tail can have critical amplitude infimum zero.
3. **Periodic/log-periodic moving-OU Floquet route — still OPEN.** No principal Floquet/terminal-point theorem was proved here, so no claim is made for oscillatory normalized boundaries of order `sqrt u`.
4. **Negative search as novelty proof — invalid.** The bounded literature search is recorded only as evidence, not certification.

Retained prior route limitations remain in the earlier immutable R07 reports and are not rewritten here.

# 13. Independent-audit status

The prior general zero-seam gauge compiler `I0077-R07-T2` has one distinct other-track scoped audit:

`R06-AUDIT-R07-I0077-T2-20260916T1922Z: PASS_SCOPED / NOVELTY_UNVERIFIED`.

That audit validates the earlier local-LIL / recurrence / stopping-time concatenation compiler at its stated scope. It does **not** automatically count as an audit of the new positive-seam theorem T6, whose Step 1 is different and simpler. No P26 audit of T6 exists in evidence available this run, and no second independent T6 audit exists. Therefore Problem 7.8 is not called closed and no paper folder is created.

No finite computational core occurs in T6/T7, so there is no exact-arithmetic checker to manufacture. The theorem-sized claim has its full proof on this page.

# 14. Model / scheduler / permission escalation

The model-control limitation is still real in this run.

The exposed scheduler update interface offers fields for task title, prompt, schedule, enablement and timing mode. It exposes **no model-family field and no reasoning-effort field**. Therefore `GPT-6 / maximum` can only be requested in prompt text from this surface; it cannot be verified or forced here. Actual runtime evidence for this report is GPT-5.6 Sol with reasoning level UNVERIFIED.

To change this for real, one of the following is required:

1. the product exposes an authenticated model and reasoning selector on scheduled tasks; or
2. an authorized owner/admin context that controls the task's runtime policy changes those settings; or
3. platform support repairs the owning-context permission/model configuration.

There is no legitimate worker-level bypass.

The repository now records an important nuance about prior `You cannot modify this task` errors. Earlier modification probes for P26/P01/P03 failed in one context, but `RESULTS.md` records that a later full P26 prompt update succeeded from a different authorized context. Therefore such an error is context/ownership scoped, not proof that the task is globally immutable. The correct workaround is to use the task's authorized owning context or platform support. Creating a duplicate scheduled task is not an authorized workaround.

No scheduler modification was attempted in this research run.

# 15. Status / next attack

**Source status:** PARTIAL / open-ended.  
**Metric:** `4 -> 5`.  
**Unchanged count:** `0`.  
**Closure:** NO.

The new theorem shows a sharp qualitative boundary phenomenon:

- zero-seam gauges can be blocked by local Brownian roughness and require local widening;
- positive-seam gauges remove that obstruction completely, and under a super-LIL tail every positive amplitude is attainable.

The next high-value frontier remains the normalized critical class

\[
f(u)=\sqrt u\,L(u),
\]

especially bounded nonconvergent or periodic `L(log u)`. Under logarithmic time this becomes Brownian/OU motion in a genuinely moving bounded interval. A new theorem there would extend the source's spectral `lambda_0` mechanism rather than only exploit supercritical tail growth.

Unused-method candidates for the next run: **#12 FIND WHAT IS CONSERVED**, **#14 FIND THE GROUP ACTING**, **#25 COUNT THE SAME THING TWICE**. The concrete target should be the period map of killed OU evolution over one log-time cycle and whether its spectral radius can replace `exp(-lambda_0 P)` in the source proof.

## Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  source:
    authors: [Krzysztof Burdzy, Michael Scheutzow]
    work: Forward Brownian Motion
    year: 2014
    arxiv: 1302.6958
    locator: Problem 7.8
    intake: I0077
  target: "Generalize Theorem 4.3 from parabolas to genuinely distinct nonparabolic space-time shape families."
  metric: "number of distinct nonparabolic shape families with a complete source-appropriate theorem, modulo frozen trivial-equivalence convention"
  before: 4
  after: 5
  movement: "YES: positive-seam superdiffusive gauge family"
  status: PARTIAL
  unchanged_count: 0
  methods_this_run: [24, 11, 27]
  exact_evidence:
    - "I0077-R07-T6: positive-seam superdiffusive gauge theorem; full proof in this report"
    - "I0077-R07-T7: rounded superdiffusive power-tube corollary"
  canonical_representative: "|x| <= C(1+|t|^(3/4)), t<=0"
  finite_checker: NOT_APPLICABLE_NO_FINITE_CORE
  independent_audits_new_theorem: []
  prior_related_audit:
    - "R06-AUDIT-R07-I0077-T2-20260916T1922Z: PASS_SCOPED / NOVELTY_UNVERIFIED"
  prior_art_status: "bounded negative search only; classical Brownian moving-boundary/LIL ingredients acknowledged; publication novelty UNVERIFIED"
  ownership:
    canonical_claim: operations/claims/I0077.md
    owner: R07
    shared_status_text: PENDING_ADMISSION
    conflict_found: false
  closure: false
  next_target: "moving killed-OU period map / Floquet exponent for log-periodic normalized boundaries"
```
