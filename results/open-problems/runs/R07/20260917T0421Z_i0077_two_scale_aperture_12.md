Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **METRIC MOVEMENT: 11 -> 12 genuinely distinct nonparabolic shape families; Section-B moves tried: #1 CHANGE THE CATEGORY, #24 FIND THE EXTREMAL OBJECT, #27 SWAP THE QUANTIFIERS.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the source's open-ended request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 12: two-scale parabolic-aperture tubes

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Fixed metric and continuity

The frozen metric remains

> the number of genuinely nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The previous authoritative report is

`runs/R07/20260917T0326Z_i0077_parabolic_tail_pinched_seam_11.md`,

which moved the metric `10 -> 11` for regions that are asymptotically parabolic in the remote past but are **super-parabolically pinched at the seam**, i.e. their normalized aperture tends to zero as `u downarrow 0`.

This run changes the local category. The new regions remain genuinely parabolic at **both** ends, but with two different positive normalized apertures. Their local tangent cone at the seam is nondegenerate, and its critical aperture competes with a different far-past aperture. This produces a two-threshold phase theorem and a direct counterexample to a tempting “tail aperture alone controls pointwise confinement” extension.

Therefore the fixed metric moves

\[
\boxed{11\longrightarrow 12.}
\]

`unchanged_count = 0`.

All 30 Section-B moves were already used once in I0077 runs 1–10. Run 11 began a second cycle with `5,18,30`. This run uses the different second-cycle triple `1,24,27`; it does not repeat the preceding triple.

The old R07 KPZ/FPP route remains retired exactly as preserved by the immutable handoff; no historical report is deleted or rewritten.

## 2. Admission / repository continuity / ownership

Before new mathematics I rechecked current `master` evidence including:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest R07 report plus the prior I0077 chain recovered by exact repository search;
- newest neighbouring Burdzy--Scheutzow report `runs/R15/20260917_0156Z_rotation_hold_scope_a22.md`;
- targeted intake/attempt searches for I0077, `1302.6958`, and Problem 7.8.

`INDEX.md` and `RANKING.md` settle Burdzy--Scheutzow Problem 7.5, not 7.8. `POSTED.md` contains no Problem-7.8 exclusion. `QUEUE.md` still lists I0077 as the distinct Problem-7.8 candidate. The canonical claim remains exclusive to R07, although its shared text still says `PENDING_ADMISSION, not READY`; the owner continues to assign this exact target to R07, and this worker does not edit the shared claim or ledgers.

The root compact `RESULTS.md` still contains an older R-series snapshot for R07 and explicitly instructs readers to recover a newer complete current-target report before replacing it. The immutable R07 reports are therefore the current mathematical state, not the stale old-FPP row.

R15's latest report preserves its six-run retirement from distinct Problem 7.2 / I0076 and does not claim I0077. No ownership collision was found.

The large `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered byte-for-byte through the connector in one response. I therefore record the whole-intake reread honestly as **PARTIAL / targeted due connector truncation**. Exact I0077 source, ownership, exclusions, queue status, prior R07 work, and neighbouring ownership were recovered directly.

## 3. Source recovery and current-status pass

I reread the primary paper, not only the intake text.

Definition 2.1: an FBM `X` has random witness times `S_n -> -infinity` such that, for each witness,

\[
B^{(n)}_t=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion.

Definition 2.2: a decomposable FBM is obtained by concatenating independent Brownian pieces stopped at finite stopping times.

For finite `c_1<c_2`, Theorem 4.3 states:

1. if `lambda_0(c_1,c_2)>=1`, every FBM has the universal normalized far-past obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there is a decomposable FBM with the corresponding normalized asymptotic confinement;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there is a decomposable FBM lying pointwise in the exact parabolic strip for every `t<=0`.

Remark 4.1 identifies `lambda_0` with the principal killed-Ornstein--Uhlenbeck/Sturm--Liouville exponent and gives continuity plus strict domain monotonicity. Remark 4.2 records the symmetric critical pair

\[
\lambda_0(-1,1)=1.
\]

The proof of Theorem 4.3(i) invokes Perkins' Brownian slow-point theorem. In source notation, for a cone whose exponent exceeds one, the compact sets of Brownian times obeying the cone constraint on every sufficiently small scale have empty intersection almost surely. This is the local input used below.

Problem 7.8 is exactly the single sentence asking whether Theorem 4.3 can be generalized from parabolas to other space-time shapes. The following forward-Lévy sentence is separately Problem 7.9 and is not part of I0077.

### Dated literature search — 2026-09-17

Fresh bounded searches included:

- exact title + `Problem 7.8` + `other space-time shapes`;
- exact title + later/citing `forward Brownian motion` papers;
- Brownian slow points + time-dependent / square-root boundaries;
- Brownian first passage across asymptotically square-root boundaries.

The search again recovered the original paper and ordinary-Brownian square-root moving-boundary literature, including Denisov--Hinrichs--Sakhanenko--Wachtel (2022), but no later paper in this bounded pass explicitly resolving exact Problem 7.8 or stating the two-scale FBM theorem below. **This is bounded negative evidence only; publication novelty remains UNVERIFIED.** Brownian slow points, the principal OU exponent, and ordinary square-root first-passage theory are prior art; the claim here is the assembled Problem-7.8 consequence.

## 4. First attack: falsify a tail-only pointwise classification

A tempting extension of Theorem 4.3 is:

> If a nonparabolic tube has normalized width tending to a favorable parabolic width `b>1` as `u->infinity`, then pointwise confinement should be possible as well.

This is false. The failure is not a refutation of Problem 7.8; it identifies the extra datum a correct extension must retain.

The seam `u=0` has its own Brownian tangent cone. If the normalized aperture there is `a<1`, the Brownian slow-point obstruction is local and cannot be repaired by making the remote past arbitrarily wide. Conversely, if the entire moving tube contains a static cone of aperture `a>1`, the source's pointwise construction in that smaller cone works simultaneously for every larger profile.

The result is a genuine two-threshold phase diagram.

## 5. The new structural family

Fix

\[
0<a\le b<\infty
\]

and a continuous profile

\[
\rho:[0,\infty)\to[0,1]
\]

with

\[
\rho(0)=0,
\qquad
\rho(u)\longrightarrow1\quad(u\to\infty).
\]

Set

\[
w(u)=a+(b-a)\rho(u)
\tag{5.1}
\]

and define the symmetric moving tube

\[
\mathcal D_{a,b,\rho}
=
\left\{(-u,x):u\ge0,\ |x|\le w(u)\sqrt u\right\}.
\tag{5.2}
\]

When `a<b` and `rho` is nonconstant this is not a parabolic strip. It has two distinct parabolic tangent apertures:

\[
\frac{w(u)\sqrt u}{\sqrt u}\to a
\quad(u\downarrow0),
\qquad
\frac{w(u)\sqrt u}{\sqrt u}\to b
\quad(u\to\infty).
\tag{5.3}
\]

Brownian rescaling `u -> cu`, `x -> sqrt(c)x` only replaces `rho(u)` by a phase/scale change `rho(cu)` and leaves the endpoint apertures `(a,b)` unchanged. In particular it cannot turn `a<b` into a constant parabolic strip.

# 6. I0077-R07-T13 — two-scale parabolic-aperture phase theorem

**Status of theorem: PROVED on the page below. Overall source status remains PARTIAL.**

Let `D_{a,b,rho}` be as above.

### T13(i): the far-past obstruction is controlled exactly by `b`

If

\[
\lambda_0(-b,b)\ge1,
\]

then every FBM `X` satisfies

\[
\boxed{
\mathbb P\left(
\limsup_{u\to\infty}\frac{X_{-u}}{\sqrt u}\ge b
\ \text{or}\ 
\liminf_{u\to\infty}\frac{X_{-u}}{\sqrt u}\le-b
\right)=1.
}
\tag{T13.i}
\]

Equivalently, since `w(u)->b`, the same statement is the source obstruction written relative to the moving walls.

### T13(ii): the far-past existence phase is also controlled exactly by `b`

If

\[
\lambda_0(-b,b)\le1,
\]

then there exists a decomposable FBM `X` such that

\[
\boxed{
\mathbb P\left(
\limsup_{u\to\infty}\frac{X_{-u}}{\sqrt u}\le b,
\quad
\liminf_{u\to\infty}\frac{X_{-u}}{\sqrt u}\ge-b
\right)=1.
}
\tag{T13.ii}
\]

### T13(iii-a): a subcritical seam aperture kills pointwise confinement for every FBM

If

\[
0<a<1,
\]

then every FBM `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists\delta>0:
|X_{-u}|\le w(u)\sqrt u
\quad\forall\,0\le u\le\delta
\right)=0.
}
\tag{T13.iii-a}
\]

In particular no FBM can lie pointwise in `D_{a,b,rho}` on the whole negative half-line, no matter how large `b` is.

### T13(iii-b): a supercritical seam aperture gives pointwise existence uniformly over every profile

If

\[
a>1,
\]

then there exists a decomposable FBM `X^{(a)}` such that **for every** `b>=a` and every admissible `rho`,

\[
\boxed{
|X^{(a)}_{-u}|
\le a\sqrt u
\le w(u)\sqrt u
\qquad\forall u\ge0
}
\tag{T13.iii-b}
\]

almost surely.

The critical local aperture `a=1` is deliberately not claimed: source Theorem 4.3(iii) itself requires the strict condition `lambda_0<1`. T13 therefore preserves rather than conceals the source's critical boundary.

## 7. Complete proof

### Proof of T13(i) and T13(ii)

By construction,

\[
w(u)\to b\qquad(u\to\infty).
\]

Hence pathwise, in the extended-real sense,

\[
\limsup_{u\to\infty}
\frac{X_{-u}-w(u)\sqrt u}{\sqrt u}
=
\limsup_{u\to\infty}
\frac{X_{-u}}{\sqrt u}-b,
\tag{7.1}
\]

and

\[
\liminf_{u\to\infty}
\frac{X_{-u}+w(u)\sqrt u}{\sqrt u}
=
\liminf_{u\to\infty}
\frac{X_{-u}}{\sqrt u}+b.
\tag{7.2}
\]

T13(i) is therefore source Theorem 4.3(i) with `(c_1,c_2)=(-b,b)`, and T13(ii) is source Theorem 4.3(ii) with the same pair. No moving-boundary first-passage assertion is smuggled into these asymptotic clauses.

### Proof of T13(iii-a)

Assume `0<a<1`. Choose `epsilon>0` so small that

\[
c:=a+\varepsilon<1.
\tag{7.3}
\]

Because `rho` is continuous and `rho(0)=0`, `w(u)->a` as `u downarrow0`. Hence there exists deterministic `delta_0>0` such that

\[
w(u)\le c
\qquad(0\le u\le\delta_0).
\tag{7.4}
\]

Remark 4.2 gives

\[
\lambda_0(-1,1)=1.
\]

Strict domain monotonicity from Remark 4.1 therefore gives

\[
\lambda_0(-c,c)>1
\qquad(c<1).
\tag{7.5}
\]

Perkins' Theorem 2(a), in the exact slow-point form quoted and used in the source proof of Theorem 4.3(i), implies that a standard Brownian path almost surely has no point at which its increments remain in the cone `[-c sqrt(h),c sqrt(h)]` for every sufficiently small positive `h`. The source states this as emptiness of the intersection of the compact slow-point sets `Lambda(b_1,b_2)` as `b_1 downarrow0`.

The same is true for **left** increments. Indeed, on each fixed deterministic horizon `[0,H]`, the reversed-increment process

\[
\widetilde B_s=B_H-B_{H-s},\qquad0\le s\le H,
\]

is standard Brownian motion. A left cone point of `B` at time `t<=H` becomes a right cone point of `tilde B` at time `H-t`. Taking the countable union over integer `H` shows that, almost surely, a standard Brownian path has no positive time `t` satisfying

\[
|B_{t-h}-B_t|\le c\sqrt h
\qquad\text{for all sufficiently small }h>0.
\tag{7.6}
\]

Now suppose the event in T13(iii-a) had positive probability. On that event, after shrinking the random `delta` if necessary,

\[
|X_{-h}|\le c\sqrt h
\qquad(0<h\le\delta)
\tag{7.7}
\]

for some `delta<=delta_0`, and `X_0=0` because the tube collapses to the origin at `u=0`.

Let `S_n` be any FBM witness sequence from Definition 2.1. Since `S_n->-infinity`, on every path in the confinement event there is a witness with

\[
T_n:=-S_n>\delta.
\]

For its standard Brownian witness

\[
B^{(n)}_t=X_{S_n+t}-X_{S_n},
\]

we have, for every `0<h<=delta`,

\[
B^{(n)}_{T_n-h}-B^{(n)}_{T_n}
=X_{-h}-X_0,
\]

and therefore by (7.7)

\[
|B^{(n)}_{T_n-h}-B^{(n)}_{T_n}|\le c\sqrt h.
\tag{7.8}
\]

But (7.8) makes `T_n` a forbidden left Brownian slow point. Each fixed witness process is standard Brownian motion and almost surely has no such time anywhere; the witness family is countable. Hence the confinement event has probability zero. This proves T13(iii-a).

No independence between the random witness time and its Brownian witness was assumed or needed: the Brownian statement rules out the existence of **any** such terminal time on the whole path.

### Proof of T13(iii-b)

Assume `a>1`. Since `(-a,a)` strictly contains the critical interval `(-1,1)`, strict domain monotonicity and `lambda_0(-1,1)=1` give

\[
\lambda_0(-a,a)<1.
\tag{7.9}
\]

Source Theorem 4.3(iii) therefore provides a decomposable FBM `X^{(a)}` with

\[
|X^{(a)}_{-u}|\le a\sqrt u
\qquad\forall u\ge0
\tag{7.10}
\]

almost surely.

For every `b>=a` and every admissible `rho`, (5.1) gives `w(u)>=a` for all `u`. Thus (7.10) immediately implies

\[
|X^{(a)}_{-u}|\le w(u)\sqrt u
\qquad\forall u\ge0.
\]

The same single source process works for the entire profile class. This proves T13(iii-b). `square`

## 8. Canonical counterexample to the tail-only extension

Take

\[
a=\frac12,
\qquad
b=2,
\qquad
\rho(u)=\frac{u}{1+u}.
\]

Then

\[
w(u)=\frac12+\frac32\frac{u}{1+u},
\]

and the region is

\[
\boxed{
|x|\le
\left(
\frac12+\frac32\frac{|t|}{1+|t|}
\right)\sqrt{|t|},
\qquad t\le0.
}
\tag{8.1}
\]

At the seam its normalized tangent aperture is `1/2`; in the remote past it tends to aperture `2`.

Since `(-2,2)` strictly contains `(-1,1)`,

\[
\lambda_0(-2,2)<1.
\]

Thus T13(ii) gives a decomposable FBM with the favorable **far-past asymptotic** normalized behavior associated with the aperture-2 parabola.

But the seam aperture `1/2<1`, so T13(iii-a) says that **no FBM whatsoever** can stay pointwise in (8.1) even on a random nontrivial neighborhood of `t=0`.

This falsifies the proposed tail-only pointwise classification while leaving the source's open-ended Problem 7.8 untouched.

For the opposite side, take `a=3/2`, `b=2` and the same `rho`. Source Theorem 4.3(iii) gives one decomposable FBM inside the static aperture-`3/2` cone; by T13(iii-b), that same process is pointwise confined in the whole two-scale moving tube.

## 9. Why this is a genuinely new family under the frozen convention

This is not a trivial rescaling of a preceding metric point.

1. **Versus run 11 (pinched seam):** run 11 has normalized seam aperture tending to `0`, so the boundary is `o(sqrt(u))` at the seam. Here the seam has a **nonzero parabolic tangent aperture `a`**. The local regular-variation exponent remains exactly `1/2`, and the coefficient crosses a genuine Brownian slow-point threshold at `a=1`. Brownian scaling cannot turn zero normalized aperture into positive normalized aperture.

2. **Versus run 4 (outward `o(sqrt(u))` corrugations):** run 4 enlarges a single asymptotic parabolic core by lower-order terms that vanish under remote-past normalization. Here the normalized width itself changes by an order-one amount from `a` to `b`; relative to the far-past cone it is an **inward order-`sqrt(u)` narrowing** near the seam. No `o(sqrt(u))` outward corrugation produces this.

3. **Versus the pulse families:** runs 6–9 have persistent or sparse critical-scale pulses in logarithmic time. Here the normalized profile has two deterministic endpoint limits and no recurring pulse mechanism.

4. **Versus pure/mixed powers and logarithmic cusps:** those families change regular-variation behavior at one or both ends. T13 stays at the exact Brownian exponent `1/2` at both ends and changes only the positive tangent aperture.

The invariant pair `(a,b)` is preserved by Brownian rescaling. The structural feature is not a mere value of one old parameter: it is the coexistence of **two nondegenerate parabolic tangent cones with different critical roles**, a regime absent from the preceding 11 families.

Therefore this run counts exactly one new family, not one family per choice of `a`, `b`, or `rho`.

## 10. Section-B methods and outcomes

### #1 CHANGE THE CATEGORY — success

I stopped treating the shape only as a remote-past moving-boundary problem and moved the seam question into the category of Brownian exceptional points. The local tangent cone is governed by Perkins slow-point theory, while the far past is governed by source Theorem 4.3. This split is what exposes the independent threshold `a=1`.

### #24 FIND THE EXTREMAL OBJECT — success

The moving profile is trapped between two extremal static cones:

\[
a\sqrt u\le w(u)\sqrt u\le b\sqrt u.
\]

The smallest cone is the exact pointwise-existence extremal object for `a>1`; the limiting outer cone is the exact far-past asymptotic object. This avoids inventing a moving-boundary spectral theory where none is needed.

### #27 SWAP THE QUANTIFIERS — success

The obvious statement would be

\[
\forall\rho\ \exists X_\rho\text{ confined in }D_{a,b,\rho}.
\]

For `a>1` the source gives the stronger statement

\[
\boxed{
\exists X^{(a)}\ \forall b\ge a\ \forall\rho:
X^{(a)}\subset D_{a,b,\rho}.
}
\]

The stronger quantifier order makes the construction immediate and identifies the minimum aperture, not the moving profile, as the pointwise control parameter.

## 11. Checker / artifact decision

There is no finite combinatorial or arithmetic core in T13. The only numerical comparisons in the canonical example are the exact rational inequalities `1/2<1<2`, and the spectral inequalities follow symbolically from the source's exact identity `lambda_0(-1,1)=1` plus strict domain monotonicity. Creating a checker for those inequalities would violate the 90/10 instruction by manufacturing evidence instead of testing a substantive finite claim.

The theorem-sized argument is therefore written in full on this page. No checker-only artifact is created.

## 12. Closure / audit status

This run proves a new source-appropriate theorem for one nonparabolic family and advances the fixed metric, but **Problem 7.8 is not called closed**.

For T13 specifically:

- full written argument: **YES, this report**;
- finite exact certificate: **NOT APPLICABLE; no finite core**;
- dated prior-art search: **YES, bounded / novelty UNVERIFIED**;
- P26 independent audit: **NO**;
- second independent OTHER-track audit: **NO**.

Therefore no paper folder is created and source status remains `PARTIAL`.

## 13. Model / scheduler interface and protected-task status

The model-control limitation remains unchanged. The exposed task-management schema allows title/prompt, schedule, enabled state and timing mode, but has **no model-family field and no reasoning-effort field**. GPT-6 / maximum remains a request in prompt text only; it is not authenticated runtime telemetry and no hour-long execution is guaranteed.

Actually enforcing and verifying GPT-6 / maximum would require the product to expose explicit model/reasoning controls with run telemetry, or an authorized owner/admin/platform-support context that can change those settings. There is no worker-side selector available here.

The repository records that historical probes for protected tasks, including P26 in one context, returned `You cannot modify this task`, while a later full P26 prompt update succeeded from another authorized context. The legitimate interpretation is context/ownership scoping. The workaround is the authorized owning/admin context or platform support — **not** a worker-level permission bypass and not a duplicate schedule. No scheduler modification is attempted in this run.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  track: R07
  run_id: 20260917T0421Z_i0077_two_scale_aperture_12
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  target: "generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shape families"
  metric:
    name: "number of distinct nonparabolic shape families with a complete source-appropriate theorem, modulo frozen no-trivial-rescaling convention"
    before: 11
    after: 12
    movement: "+1"
    unchanged_count_before: 0
    unchanged_count_after: 0
  methods_this_run: [1, 24, 27]
  theorem:
    id: I0077-R07-T13
    family: "two-scale parabolic-aperture tubes"
    far_past_parameter: b
    seam_parameter: a
    far_phase: "exact source lambda_0(-b,b) obstruction/existence"
    pointwise_phase:
      a_lt_1: "universal local impossibility for every FBM"
      a_gt_1: "one decomposable FBM works for every b>=a and every admissible profile"
      a_eq_1: "not claimed / critical"
    canonical_profile: "rho(u)=u/(1+u)"
    canonical_mismatch: "a=1/2, b=2: favorable far-past asymptotic phase but pointwise local impossibility"
  status: PARTIAL
  audits:
    P26: MISSING
    second_other_track: MISSING
  prior_art: "bounded dated search completed; no explicit Problem-7.8 resolution located; novelty UNVERIFIED"
  intake_read: "PARTIAL_TARGETED_DUE_CONNECTOR_TRUNCATION"
  next_research_direction: "critical seam a=1 and asymmetric two-tangent intervals; do not count parameter-only variants"
  proposed_next_methods: [3, 14, 20]
```

No shared root, peer file, email, Drive resource, public resource, purchase, permission, workflow, or scheduler setting was modified in this run.
