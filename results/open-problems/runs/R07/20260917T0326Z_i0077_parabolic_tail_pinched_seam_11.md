Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **METRIC MOVEMENT: 10 -> 11 genuinely distinct nonparabolic shape families; Section-B moves tried: #5 ADD A PARAMETER, #18 SAY IT IN ANOTHER LANGUAGE, #30 ONE SCALE/DIRECTION AT A TIME.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the source problem is open-ended and is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 11: parabolic tails with a supercritical pinched seam

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Fixed metric and continuity

The frozen metric remains

> the number of genuinely nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and parameter changes inside one structural family do not create new metric points.

The previous authoritative report is

`runs/R07/20260917T0230Z_i0077_log_sawtooth_envelope_10.md`,

which moved the metric from `9` to `10` with the bounded-envelope nonmonotone gauge compiler and its discrete-scale log-sawtooth family. This run does not repeat that route.

Across I0077 runs 1–10, every Section-B number 1–30 has now been used at least once. There is therefore no unused number left. This run begins a second cycle with a different triple from the immediately preceding `10,16,22`: `5,18,30`. The implementations below are new uses of those moves, not reruns of the earlier arguments.

The new family has a parabolic far-past tail but collapses *strictly faster than parabolically* at the seam `t=0`. It preserves the exact Theorem-4.3 asymptotic `lambda_0` phase while destroying pointwise confinement for every FBM. This is structurally opposite to run 4's outward asymptotically parabolic corrugations, which preserved the parabolic core pointwise.

Therefore the metric moves

\[
\boxed{10\longrightarrow 11.}
\]

`unchanged_count = 0`.

The old R07 KPZ/FPP route remains retired exactly as preserved in the run-1 handoff. No historical file was altered or deleted.

## 2. Admission / repository continuity / ownership

Before new mathematics I rechecked current `master` evidence including:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the complete visible `runs/R07/` directory listing, including the four preserved KPZ/FPP reports, the immutable rotation/handoff, and I0077 runs 1–10;
- newest neighboring R15 report located at `runs/R15/20260917_0156Z_rotation_hold_scope_a22.md`.

`INDEX.md` and `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no Problem-7.8 exclusion. `QUEUE.md` still lists I0077 separately from R15's former I0076 / Problem 7.2. The canonical I0077 claim remains exclusive to R07, although its shared status text remains `PENDING_ADMISSION, not READY`; the source/current-status/ownership admission was completed in the first I0077 run and the owner continues to assign this exact target to R07.

The large intake JSONLs cannot be rendered byte-for-byte in one connector response. I therefore record the whole-intake reread honestly as **PARTIAL / targeted due connector truncation**. Exact I0077 source, ownership, posted exclusions, run history, and neighboring ownership were recovered directly.

## 3. Source recovery and dated literature pass

I reread the primary PDF, not only the intake summary.

Definition 2.1: an FBM `X` has witness times `S_n -> -infinity` such that each process

\[
B^{(n)}_t=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

is standard Brownian motion.

Definition 2.2: decomposable FBM means concatenation of independent Brownian pieces stopped at finite stopping times.

Theorem 4.3 treats the parabolic strip

\[
c_1\sqrt{|t|}\le X_t\le c_2\sqrt{|t|},\qquad t\le0,
\]

through the Sturm–Liouville / killed-OU exponent `lambda_0(c_1,c_2)`:

1. `lambda_0 >= 1`: every FBM hits the normalized upper/lower asymptotic obstruction;
2. `lambda_0 <= 1`: there exists a decomposable FBM with the corresponding normalized asymptotic confinement;
3. `c_1 <= 0 <= c_2` and `lambda_0 < 1`: there exists a decomposable FBM satisfying the pointwise parabolic inequalities for every `t<=0`.

Remark 4.1 records continuity and strict domain monotonicity of `lambda_0`; Remark 4.2 records `lambda_0(-1,1)=1`. In the proof of Theorem 4.3(i), Burdzy–Scheutzow invoke Perkins (1983), Theorem 2(a), to rule out Brownian slow points inside a fixed parabolic cone when the corresponding exponent exceeds one.

Problem 7.8 is exactly the one sentence asking whether Theorem 4.3 can be generalized from parabolas to other space-time shapes. The following forward-Lévy sentence is Problem 7.9 and is not part of I0077.

### Current-status search, 2026-09-17

Fresh bounded searches covered:

- exact title + `Problem 7.8` + `space-time shapes`;
- Burdzy/Scheutzow + forward Brownian motion + moving/nonparabolic boundary;
- later/citing forward-Brownian papers and Brownian path decompositions;
- Perkins slow points / parabolic cone points / pointwise Brownian regularity;
- first-passage work for nonparabolic moving Brownian boundaries.

The search recovered the original paper, the UW publication page, Burdzy's decomposable-FBM slides, Perkins' slow-point paper, and later work citing forward Brownian motion, but no later paper in this bounded pass explicitly resolving exact Problem 7.8 or stating the theorem below. **This is negative bounded evidence only; novelty remains UNVERIFIED.** The slow-point input and Brownian time reversal are classical, and I do not claim those ingredients as new.

## 4. New route: separate the two ends of the shape

Runs 6–9 concentrated on critical parabolic-scale oscillations in the remote past. Run 10 returned to super-LIL existence gauges. This run instead asks whether the two logically different pieces of Theorem 4.3 — the `t -> -infinity` spectral phase and the pointwise requirement through `t=0` — can be forced to disagree.

That gives the new structural class.

Let

\[
\ell,r:[0,\infty)\to\mathbb R
\]

be continuous, with

\[
\ell(0)=r(0)=0,\qquad \ell(u)<r(u)\quad(u>0).
\]

Assume there are finite `c_1<c_2` such that

\[
\tag{A∞}
\frac{\ell(u)}{\sqrt u}\longrightarrow c_1,
\qquad
\frac{r(u)}{\sqrt u}\longrightarrow c_2
\qquad(u\to\infty),
\]

but at the seam

\[
\tag{A0}
\frac{\max\{|\ell(u)|,|r(u)|\}}{\sqrt u}
\longrightarrow0
\qquad(u\downarrow0).
\]

Define the nonparabolic region

\[
\mathcal D_{\ell,r}
=
\{(-u,x):u\ge0,\ \ell(u)\le x\le r(u)\}.
\]

Condition (A∞) says that the remote past looks exactly parabolic after Brownian normalization. Condition (A0) says that the seam is pinched more tightly than every fixed parabolic cone.

## 5. Theorem I0077-R07-T12 — parabolic-tail / pinched-seam phase theorem

Under (A∞) and (A0):

### (i) The source asymptotic obstruction is unchanged

If

\[
\lambda_0(c_1,c_2)\ge1,
\]

then every FBM `X` satisfies

\[
\boxed{
\mathbb P\left(
\left\{\limsup_{u\to\infty}\frac{X_{-u}-r(u)}{\sqrt u}\ge0\right\}
\cup
\left\{\liminf_{u\to\infty}\frac{X_{-u}-\ell(u)}{\sqrt u}\le0\right\}
\right)=1.
}
\tag{T12.i}
\]

### (ii) The source asymptotic existence phase is unchanged

If

\[
\lambda_0(c_1,c_2)\le1,
\]

then there exists a decomposable FBM `X` such that

\[
\boxed{
\mathbb P\left(
\left\{\limsup_{u\to\infty}\frac{X_{-u}-r(u)}{\sqrt u}\le0\right\}
\cap
\left\{\liminf_{u\to\infty}\frac{X_{-u}-\ell(u)}{\sqrt u}\ge0\right\}
\right)=1.
}
\tag{T12.ii}
\]

### (iii) Pointwise confinement through the seam is impossible for every FBM

For every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists\delta>0:\ 
\ell(u)\le X_{-u}\le r(u)\quad\forall\,0\le u\le\delta
\right)=0.
}
\tag{T12.iii}
\]

In particular,

\[
\boxed{
\mathbb P\left(
(-u,X_{-u})\in\mathcal D_{\ell,r}
\quad\forall u\ge0
\right)=0
}
\tag{T12.pointwise}
\]

for every FBM, even when `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`.

### Proof of (i) and (ii)

By (A∞),

\[
\frac{r(u)}{\sqrt u}\to c_2,
\qquad
\frac{\ell(u)}{\sqrt u}\to c_1.
\]

Therefore, pathwise in the extended real sense,

\[
\limsup_{u\to\infty}
\frac{X_{-u}-r(u)}{\sqrt u}
=
\limsup_{u\to\infty}
\frac{X_{-u}}{\sqrt u}-c_2,
\]

and

\[
\liminf_{u\to\infty}
\frac{X_{-u}-\ell(u)}{\sqrt u}
=
\liminf_{u\to\infty}
\frac{X_{-u}}{\sqrt u}-c_1.
\]

Thus (T12.i) is exactly Theorem 4.3(i), rewritten in the moving-boundary language, and (T12.ii) is exactly Theorem 4.3(ii), with the same decomposable process. No new asymptotic estimate is needed.

### Proof of (iii)

Fix any `epsilon` with

\[
0<\varepsilon<1.
\]

By (A0), there is deterministic `delta_0>0` such that

\[
[\ell(u),r(u)]
\subset
[-\varepsilon\sqrt u,\varepsilon\sqrt u]
\qquad(0<u\le\delta_0).
\tag{5.1}
\]

Suppose the event in (T12.iii) had positive probability. On that event, after reducing the random `delta` if necessary to `delta_0`, we have `X_0=0` and

\[
|X_{-u}|\le\varepsilon\sqrt u
\qquad(0<u\le\delta)
\tag{5.2}
\]

for some `delta>0`.

Let `S_n` be any FBM witness sequence from Definition 2.1. Since `S_n->-infinity`, for every path in the event there is some witness index with

\[
T_n:=-S_n>\delta.
\]

For that fixed witness process

\[
B^{(n)}_t=X_{S_n+t}-X_{S_n},\qquad t\ge0,
\]

which is standard Brownian motion, (5.2) gives for every `0<h<=delta`,

\[
B^{(n)}_{T_n-h}-B^{(n)}_{T_n}
=X_{-h}-X_0
\in[-\varepsilon\sqrt h,\varepsilon\sqrt h].
\tag{5.3}
\]

Thus `T_n` is a left Brownian slow point lying inside the symmetric parabolic cone of aperture `epsilon` at every sufficiently small scale.

But Remark 4.2 of the source gives

\[
\lambda_0(-1,1)=1,
\]

and strict domain monotonicity from Remark 4.1 gives

\[
\lambda_0(-\varepsilon,\varepsilon)>1
\qquad(0<\varepsilon<1).
\tag{5.4}
\]

Perkins (1983), Theorem 2(a), in exactly the local slow-point form used in the proof of Theorem 4.3(i), rules out a Brownian point that stays in such a cone through all sufficiently small scales. The source states this as emptiness of the intersection of its compact slow-point sets `Lambda(b_1,b_2)` when `b_1 downarrow 0`. Applying the same statement to a time-reversed Brownian path on each finite deterministic horizon rules out **left** slow points as in (5.3). Taking the countable union over deterministic horizons rules them out anywhere at positive time almost surely.

Hence a standard Brownian witness almost surely cannot have a terminal time satisfying (5.3). This contradicts the existence of the witness forced by the confinement event. Therefore (T12.iii) holds. `square`

## 6. Canonical family — rounded/shifted parabola with a linear seam

Method #5 adds a geometric seam parameter `a>0` to the parabola:

\[
h_a(u):=\sqrt{u+a}-\sqrt a
=
\frac{u}{\sqrt{u+a}+\sqrt a}.
\tag{6.1}
\]

Fix finite

\[
c_1<0<c_2
\]

and define

\[
\ell_a(u)=c_1h_a(u),
\qquad
r_a(u)=c_2h_a(u).
\tag{6.2}
\]

Then

\[
\frac{h_a(u)}{\sqrt u}	o1
\qquad(u\to\infty),
\tag{6.3}
\]

while

\[
0\le h_a(u)
\le\frac{u}{2\sqrt a},
\qquad
\frac{h_a(u)}{\sqrt u}\to0
\qquad(u\downarrow0).
\tag{6.4}
\]

So T12 applies.

A canonical representative is `a=1`, `c_1=-2`, `c_2=2`:

\[
\boxed{
|x|\le2\bigl(\sqrt{1+|t|}-1\bigr),
\qquad t\le0.
}
\tag{6.5}
\]

By strict domain monotonicity and `lambda_0(-1,1)=1`,

\[
\lambda_0(-2,2)<1.
\]

Therefore there exists a decomposable FBM with the *same asymptotic normalized phase* as the wide parabolic strip, namely

\[
\limsup_{u\to\infty}
\frac{X_{-u}-2h_1(u)}{\sqrt u}\le0,
\qquad
\liminf_{u\to\infty}
\frac{X_{-u}+2h_1(u)}{\sqrt u}\ge0,
\]

almost surely.

Nevertheless **no FBM at all** can satisfy

\[
|X_{-u}|\le2(\sqrt{1+u}-1)
\qquad\forall u\ge0.
\tag{6.6}
\]

For the exact parabola `|x|<=2 sqrt(u)`, Theorem 4.3(iii) gives pointwise decomposable-FBM existence because `lambda_0(-2,2)<1`. Thus the rounded cap (6.5), although asymptotically indistinguishable after Brownian normalization, reverses the pointwise answer solely through its local seam geometry.

This is the cleanest result of the run.

## 7. The three methods and what each did

### #5 ADD A PARAMETER AND DIFFERENTIATE / MOVE IT

Instead of perturbing the far-past OU exponent, insert a seam-rounding parameter `a` into

\[
\sqrt u\rightsquigarrow \sqrt{u+a}-\sqrt a.
\]

The parameter leaves the `u->infinity` Brownian normalization unchanged but changes the local exponent at the seam from `1/2` to `1`. That immediately suggests a phase split between asymptotic and pointwise confinement.

### #18 SAY IT IN ANOTHER LANGUAGE

The theorem is not best viewed as a special formula. It is a **two-end boundary-regularity theorem**:

- the far-past normalized limits `(c_1,c_2)` determine the Theorem-4.3 spectral phase;
- the seam ratios `ell(u)/sqrt(u), r(u)/sqrt(u)` determine whether a Brownian witness can terminate there.

In this language, the same shape can be parabolic in one end and supercritical/narrow in the other. The source's three clauses need not travel together once exact self-similarity is lost.

### #30 ONE SCALE / ONE DIRECTION AT A TIME

The proof deliberately separates `u->infinity` from `u->0` instead of trying to control the whole shape by one global comparison. The remote-past theorem is inherited exactly from Theorem 4.3. The seam theorem is local and uses only the narrow-cone slow-point obstruction. The failure to glue those two favorable statements into a pointwise construction is itself the structural result.

## 8. Why this is a new metric family

All shapes satisfying (A∞) and (A0) are counted here as **one** structural family. Changing `a`, `c_1,c_2`, or lower-order smooth terms does not create another metric point.

It is distinct from the previous ten counted classes:

- unlike the pure-power `beta>1/2` family, its far-past width is parabolic, not superdiffusive;
- unlike the mixed-power and logarithmic super-LIL cusp families, its remote normalized boundary converges to finite nonzero constants and inherits the nontrivial `lambda_0` phase;
- unlike run 4 outward `o(sqrt u)` corrugations, it is *inside* every fixed parabolic cone near the seam rather than containing a parabolic core;
- unlike the positive-seam family, its time-zero cross-section is a single point;
- unlike runs 6–9, its normalized far-past profile does not oscillate, pulse, drift, or accumulate spectral mass;
- unlike run 10's log-sawtooth gauges, its decisive obstruction is local at `u=0`, not bounded-envelope global aggregation.

Brownian scaling sends `a` to another positive `a` but cannot turn the local seam exponent `1` into the parabolic exponent `1/2`. Thus it cannot map this family to an exact parabola or to the previously counted asymptotic classes.

The fixed metric therefore moves

\[
\boxed{10\to11}.
\]

## 9. What was falsified / what is not claimed

A natural but false proposed extension was:

> if a nonparabolic tube is asymptotically parabolic and its limiting pair `(c_1,c_2)` has `lambda_0<1`, then the pointwise existence clause of Theorem 4.3(iii) should survive.

T12 + (6.5) disproves that proposed extension. This is **not** a refutation of Problem 7.8, which is open-ended.

I do **not** claim:

- eventual pointwise inclusion from the asymptotic clause (ii);
- a complete classification of arbitrary moving boundaries;
- novelty from the bounded negative literature search;
- that Perkins' slow-point theorem, Brownian time reversal, or the Sturm–Liouville facts are new;
- source closure or publication readiness.

## 10. Closure / audit state

T12 is a theorem-sized analytic claim and its full proof is on this page. There is no finite combinatorial core, so no checker was manufactured merely to certify elementary limits.

There is no independent T12 audit yet, including no P26 audit and no second OTHER-track audit. Therefore the source remains **PARTIAL** under the owner's closure protocol and no `paper_<name>/` folder is created.

This run spends its validation budget only on source/current-status/ownership recovery and the proof itself; it does not generate receipt-only or checker-only commits.

## 11. Model / scheduler control status

Still true: the exposed scheduler control surface provides prompt/title, schedule, enablement and timing-mode controls, but no authenticated model-family or reasoning-effort field. GPT-6/maximum therefore remains prompt-only from this surface. A real change requires those selectors to be exposed by the product or an authorized owning/admin/platform-support context.

Repository `RESULTS.md` now records an important permission nuance: historical P26/P01/P03 probes returned `You cannot modify this task`, while a later P26 full update succeeded from another authorized context. The legitimate workaround is therefore the task's authorized owning context (or platform support), not a worker-level permission bypass and not creation of a duplicate schedule.

No scheduler change was attempted in this run, per the owner restriction.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  run_id: 20260917T0326Z_i0077_parabolic_tail_pinched_seam_11
  source: "Burdzy-Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  target: "generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shape families"
  metric:
    name: "number of distinct nonparabolic shape families with a complete source-appropriate theorem, modulo frozen no-trivial-rescaling convention"
    before: 10
    after: 11
    movement: true
  status: PARTIAL
  unchanged_count: 0
  methods: [5, 18, 30]
  theorem: I0077-R07-T12
  new_family: "parabolic-at-infinity tubes pinched to o(sqrt(u)) at the seam; canonical h_a(u)=sqrt(u+a)-sqrt(a)"
  source_closure: false
  audits:
    p26: missing_for_T12
    second_other_track: missing_for_T12
  finite_core: none
  prior_art: "bounded dated search; exact Problem 7.8 resolution not located; novelty UNVERIFIED"
  ownership: "R07 exclusive provisional reservation; shared claim text still says PENDING_ADMISSION"
  old_kpz_route: "retired; immutable handoff preserved"
  delivery: "private GitHub only"
```

## 13. Next high-value direction

Do **not** add another easy formula next. T12 identifies the sharp conceptual split to attack: classify local seam profiles that *do* admit a Brownian terminal slow point while the remote tail lies in a fixed `lambda_0<1` phase. The first unresolved boundary is the critical seam

\[
\ell(u),r(u)\asymp \sqrt u
\]

with nonconstant slowly varying or oscillatory coefficients as `u downarrow0`.

A useful next run should try a second-cycle triple different from this one, for example `#11 DUALIZE`, `#20 FIND WHY THE ALGORITHM FAILS`, and `#24 FIND THE EXTREMAL OBJECT`, and seek a seam-capacity criterion rather than a twelfth easy family.
