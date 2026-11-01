Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **METRIC MOVEMENT: 9 -> 10 genuinely distinct nonparabolic shape families; Section-B moves tried: #10 DERANDOMIZE, #16 COMPUTE EVERY SMALL CASE, #22 READ THE FAILURES.**
Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Status: PARTIAL; the open-ended source problem is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 10: bounded-envelope nonmonotone gauges and a discrete-scale log-sawtooth family

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Fixed metric and continuity

The frozen metric remains

> the number of genuinely nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and parameter changes inside one structural family do not create new metric points.

The previous authoritative report is

`runs/R07/20260917T0122Z_i0077_sparse_drifting_pulses_09.md`,

which moved the metric from `8` to `9` by proving the weighted sparse-pulse obstruction and giving a zero-density drifting-pulse family. This run does not restart that route. It uses the earlier general gauge compiler from

`runs/R07/20260916T1822Z_i0077_log_cusp_gauge_02.md`

as a proved dependency and removes its monotonicity restriction by a deterministic envelope argument. The resulting class contains genuinely nonmonotone, discretely scale-invariant gauges that are not Brownian-rescaling-equivalent to any of the first nine counted structural families.

Therefore

\[
\boxed{9\longrightarrow10.}
\]

`unchanged_count` remains `0` because the fixed metric moved.

The old R07 KPZ/FPP route remains retired from this slot exactly as preserved by the run-1 handoff. No historical file was altered or deleted.

## 2. Required repository/source/ownership recovery

Before new mathematics I reread or directly rechecked current `master` state including:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest R07 report and the preceding I0077 chain recovered by exact repository search;
- newest neighboring R15 report `runs/R15/20260917_0156Z_rotation_hold_scope_a22.md`.

`INDEX.md` and `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` contains no Problem-7.8 exclusion. `QUEUE.md` still lists I0077 as the Burdzy–Scheutzow shape problem. The canonical claim remains exclusive to R07, although its shared text remains `PENDING_ADMISSION, not READY`; the full source/current-status/ownership admission was recovered in run 1 and this exact target remains the owner's direct R07 assignment. R15 has retired its distinct Problem 7.2 / I0076 after its six-run handoff and explicitly recognizes I0077 as R07-owned.

The large `probability_1000_intake_*/problems.jsonl` resources remain connector-truncated when rendered wholesale. I therefore record the whole-intake reread as **PARTIAL / targeted due connector limits**, rather than falsely claiming a byte-for-byte visual read. Exact I0077 source, ownership, exclusions, and prior attempts were recovered directly.

## 3. Source statement and current-status check

I rechecked the primary Burdzy–Scheutzow PDF rather than relying on the intake paraphrase.

Definition 2.1 gives the FBM witness-time definition. Definition 2.2 gives the decomposable concatenation construction. Theorem 4.3 treats the parabolic strip

\[
c_1\sqrt{|t|}\le x\le c_2\sqrt{|t|},\qquad t\le0,
\]

through the Ornstein–Uhlenbeck/Sturm–Liouville exponent `lambda_0(c_1,c_2)`:

1. `lambda_0>=1` gives a universal asymptotic obstruction for every FBM;
2. `lambda_0<=1` gives a decomposable FBM with the requested asymptotic parabolic confinement;
3. if `c_1<=0<=c_2` and `lambda_0<1`, there is a decomposable FBM confined pointwise in the parabolic strip for all `t<=0`.

Problem 7.8 is exactly the one-sentence question

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The following forward-Lévy text is separately Problem 7.9 and is not part of I0077.

### Dated literature/status pass — 2026-09-17

Fresh bounded searches covered the exact Problem-7.8 wording/title, later Burdzy/Scheutzow papers and citing papers, decomposable-FBM moving-boundary terms, Brownian slow points, and time-dependent/killed Ornstein–Uhlenbeck survival. I found no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the theorem below. This is **negative bounded evidence only; novelty remains UNVERIFIED**.

Relevant surrounding machinery is known. Perkins' Brownian slow-point theorem is the ingredient used by the source. Periodic and nonautonomous OU first-passage/survival problems also have an established literature. None of that by itself supplies the forward-Brownian concatenation theorem here, and the present argument deliberately treats all Brownian LIL/support/envelope ingredients as classical rather than claiming them as novel.

## 4. Method #22 — READ THE FAILURES: what the source proof says breaks

The source proof of Theorem 4.3 uses a monotone/convex aggregation mechanism when stopped Brownian pieces are pasted backward. In its discussion of the harder case the authors explicitly note that the previous reasoning fails when the parabolic region is nonconvex and the argument becomes more complicated. That is the exact failure relevant here: the run-2 gauge theorem assumed a nondecreasing gauge precisely so that every earlier stopped endpoint and the current reversed partial piece could be bounded by the single present-time gauge value.

So I did **not** try another probabilistic stopping-time lemma. The question is whether the monotonicity needed by the concatenation proof can be supplied deterministically at controlled multiplicative cost.

This leads to a clean envelope criterion.

## 5. Method #10 — DERANDOMIZE: bounded running-envelope compiler

The earlier R07 theorem `I0077-R07-T2` proved:

> If `F:[0,infinity)->[0,infinity)` is continuous and nondecreasing, `F(0)=0<F(u)` for `u>0`, and
> \[
> \frac{F(u)}{\sqrt{u\log\log(1/u)}}\to\infty\quad(u\downarrow0),
> \qquad
> \frac{F(u)}{\sqrt{u\log\log u}}\to\infty\quad(u\to\infty),
> \]
> then for every `A>0` there exists a decomposable FBM `X`, `X_0=0`, satisfying `|X_t|<=A F(|t|)` for every `t<=0` almost surely.

The new point is to remove monotonicity from the target gauge.

### Theorem I0077-R07-T11 — bounded-envelope nonmonotone super-LIL gauges

Let

\[
f:[0,\infty)\to[0,\infty)
\]

be continuous with `f(0)=0`, `f(u)>0` for `u>0`, and assume

\[
\tag{G0}
\frac{f(u)}{\sqrt{u\log\log(1/u)}}\longrightarrow\infty
\qquad(u\downarrow0),
\]

\[
\tag{G∞}
\frac{f(u)}{\sqrt{u\log\log u}}\longrightarrow\infty
\qquad(u\to\infty).
\]

Define its backward running-envelope distortion

\[
Q_f
:=
\sup_{u>0}
\frac{\sup_{0<s\le u}f(s)}{f(u)}.
\tag{5.1}
\]

If

\[
\boxed{Q_f<\infty,}
\tag{5.2}
\]

then for every `C>0` there exists a decomposable FBM `X`, normalized by `X_0=0`, such that

\[
\boxed{|X_t|\le C f(|t|)\qquad\forall t\le0\quad a.s.}
\tag{T11}
\]

#### Proof

Set

\[
F(u):=\max_{0\le s\le u}f(s).
\tag{5.3}
\]

Because `f` is continuous, the maximum exists on every compact interval. The running maximum `F` is continuous and nondecreasing, with `F(0)=0` and `F(u)>0` for `u>0`. (For continuity: on any compact `[0,R]`, uniform continuity of `f` shows that changing the right endpoint by at most `delta` can change the new running maximum only through values of `f` within `delta` of that endpoint; left continuity follows by approximating a maximizer from below, and right continuity from uniform continuity.)

Since `F>=f`, conditions (G0) and (G∞) pass immediately from `f` to `F`. By (5.1), for every `u>0`,

\[
F(u)\le Q_f f(u).
\tag{5.4}
\]

Apply the proved monotone-gauge theorem T2 to `F` with amplitude

\[
A=C/Q_f.
\]

It gives a decomposable FBM `X` with

\[
|X_t|
\le \frac{C}{Q_f}F(|t|)
\le C f(|t|)
\qquad(t\le0)
\]

almost surely. This proves T11. `square`

The important feature is that the stochastic construction is **not** rerun. The nonmonotone geometry is deterministically compiled into a monotone majorant with a finite loss and then fed into the already proved stopping-time construction.

## 6. Method #16 — COMPUTE EVERY SMALL CASE: a canonical log-sawtooth family

The simplest genuinely nonmonotone test is a bounded oscillation in logarithmic scale.

Let

\[
g(u)=u^{1/4}+u^{3/4},\qquad u\ge0,
\tag{6.1}
\]

and define the continuous 1-periodic triangular factor

\[
q(r)=1+\frac23\,\operatorname{dist}(r,\mathbb Z),
\qquad 1\le q(r)\le\frac43.
\tag{6.2}
\]

For `u>0`, put

\[
f_{\rm saw}(u)=g(u)q(\log_2u),
\qquad
f_{\rm saw}(0)=0.
\tag{6.3}
\]

This is a centered, symmetric, discrete-scale log-sawtooth tube

\[
\mathcal S_C
=
\{(t,x):t\le0,\ |x|\le C f_{\rm saw}(|t|)\}.
\]

### 6.1 The super-LIL hypotheses

Because `q>=1`,

\[
f_{\rm saw}(u)\ge u^{1/4}+u^{3/4}.
\]

Hence as `u downarrow 0`,

\[
\frac{f_{\rm saw}(u)}{\sqrt{u\log\log(1/u)}}
\ge
\frac{u^{-1/4}}{\sqrt{\log\log(1/u)}}\to\infty,
\]

and as `u to infinity`,

\[
\frac{f_{\rm saw}(u)}{\sqrt{u\log\log u}}
\ge
\frac{u^{1/4}}{\sqrt{\log\log u}}\to\infty.
\]

So (G0) and (G∞) hold.

### 6.2 Exact envelope distortion

For `0<s<=u`, monotonicity of `g` and the bounds on `q` give

\[
f_{\rm saw}(s)
\le\frac43 g(s)
\le\frac43 g(u)
\le\frac43 f_{\rm saw}(u).
\]

Therefore

\[
\boxed{Q_{f_{\rm saw}}\le\frac43.}
\tag{6.4}
\]

T11 now gives, for every `C>0`, a decomposable FBM `X` with

\[
\boxed{|X_t|\le C\bigl(|t|^{1/4}+|t|^{3/4}\bigr)
q(\log_2|t|)\qquad\forall t\le0.}
\tag{C11.1}
\]

### 6.3 It is truly nonmonotone on every dyadic scale

Let

\[
u_k=2^{k+1/2},
\qquad
v_k=2^{k+1}=\sqrt2\,u_k.
\]

Then `q(log_2 u_k)=4/3` and `q(log_2 v_k)=1`. Moreover

\[
\frac{g(v_k)}{g(u_k)}
\]

is a positive weighted average of

\[
(\sqrt2)^{1/4}=2^{1/8}
\quad\text{and}\quad
(\sqrt2)^{3/4}=2^{3/8},
\]

so

\[
\frac{g(v_k)}{g(u_k)}\le2^{3/8}.
\]

The exact inequality

\[
\frac43>2^{3/8}
\]

is equivalent, after raising to the eighth power, to

\[
4^8>8\,3^8,
\]

i.e.

\[
65536>52488.
\]

Therefore

\[
f_{\rm saw}(v_k)<f_{\rm saw}(u_k)
\qquad\text{for every }k\in\mathbb Z.
\tag{6.5}
\]

So this is not a monotone gauge disguised by notation: it has an actual down-step in every dyadic annulus.

The finite route-discovery check tested the rational heights `5/4,4/3,3/2,2` against the exact condition `H^8>8`; `4/3` is the first passing candidate in that scan. The source and archived output are

- `artifacts/R07/20260917T0230Z_sawtooth_height_checker.py` @ `4dd6732ae09e62bfeb02248aa76c47977e803a9d`;
- `artifacts/R07/20260917T0230Z_sawtooth_height_checker.out` @ `8f5b1644a4324ddbf6f0bb9995b15a751d1c8dc3`, ending `PASS`.

The checker certifies only the finite rational-height comparison; the theorem itself is proved analytically above.

## 7. Why this is a new metric family rather than a parameter change

All bounded-envelope nonmonotone super-LIL gauges are counted here as **one** structural family. Changing the sawtooth height, period, phase, or the two harmless power exponents inside the allowed regime does not create further metric points.

The canonical family is nevertheless distinct from the previous counted families under the frozen equivalence convention.

The strongest invariant is persistent log-periodicity. For the scale factor `lambda=sqrt(2)`, the ratio

\[
\frac{f_{\rm saw}(\lambda u)}{f_{\rm saw}(u)}
\]

has different subsequential limits depending on the phase of `log_2 u`. At integer phases the periodic factor contributes `4/3`; at half-integer phases it contributes `3/4`. Thus the gauge is not regularly varying at either end. Brownian rescaling `u mapsto a u` merely translates the phase of `q`; it cannot make a nonconstant periodic factor constant.

This separates family 10 from the earlier regularly varying mixed-power and pure-power cusps, from the index-1/2 logarithmic cusp, from the `o(sqrt u)` outward-corrugation class whose normalized perturbation vanishes, from the positive-seam class, and from the parabolic-scale pulse families whose normalized width remains bounded or whose obstruction is generated by isolated drifting pulses. In the present family the tube stays centered, its width diverges relative to the parabolic scale at both ends, and its nonmonotonicity persists at every multiplicative scale.

Accordingly the frozen metric moves only once:

\[
\boxed{9\to10.}
\]

## 8. Honest status and closure

This is a complete theorem for one new structural family, but Problem 7.8 is open-ended and is **not** called solved. The current label remains **PARTIAL**.

No independent OTHER-track audit of T11/C11.1 exists yet, including no P26 audit, so the owner's closure protocol is not met and no `paper_*` folder is created. The exact finite comparison has a checker, while the theorem-sized claim has its written proof on this page.

The next scientifically stronger direction is not another easy example. The remaining frontier is a genuinely critical moving tube whose width is of parabolic order `sqrt(u)` and for which one can prove both an obstruction and a matching phase-aware decomposable-FBM existence theorem, rather than only a sufficient construction or a sufficient obstruction.

## 9. Model / scheduler / protected-task limitation

The implementation limitation is unchanged. The exposed task-management schema provides prompt/title, schedule, enablement and timing-mode controls, but no authenticated model-family selector, reasoning-effort selector, or completed-run model telemetry. GPT-6 / maximum therefore remains a prompt request only from this surface.

Actually changing and verifying the model requires a product scheduler surface exposing explicit model/reasoning fields plus authenticated run metadata, or action from the authorized owning/admin context/platform support. Historical `You cannot modify this task` errors, including the earlier P26 probe, are authorization/context scoped; later repository evidence records successful P26 edits from another authorized context. There is no legitimate R07-level bypass, and duplicating the task is not an authorized workaround.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R07
  run_id: 20260917T0230Z_i0077_log_sawtooth_envelope_10
  source:
    authors: [Krzysztof Burdzy, Michael Scheutzow]
    work: Forward Brownian Motion
    year: 2014
    arxiv: 1302.6958
    locator: Problem 7.8
    intake: I0077
  target: "generalize Theorem 4.3 from parabolic regions to genuinely distinct nonparabolic space-time shape families"
  metric:
    name: "number of distinct nonparabolic shape families with a complete source-appropriate theorem, modulo the frozen no-trivial-rescaling convention"
    before: 9
    after: 10
    movement: MOVED
  status: PARTIAL
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods_this_run: [10, 16, 22]
  claims:
    - "I0077-R07-T11 bounded-envelope nonmonotone super-LIL gauge confinement theorem"
    - "I0077-R07-C11.1 discrete-scale log-sawtooth canonical family"
  exact_evidence:
    - "runs/R07/20260917T0230Z_i0077_log_sawtooth_envelope_10.md"
    - "artifacts/R07/20260917T0230Z_sawtooth_height_checker.py @ 4dd6732ae09e62bfeb02248aa76c47977e803a9d"
    - "artifacts/R07/20260917T0230Z_sawtooth_height_checker.out @ 8f5b1644a4324ddbf6f0bb9995b15a751d1c8dc3"
  audits: []
  prior_art: "bounded dated search performed 2026-09-17; source theorem, Perkins slow points and nonautonomous OU survival literature checked; exact Problem 7.8 resolution not found; novelty UNVERIFIED"
  access_limits: "large intake JSONL resources connector-truncated; intake reread targeted to exact I0077/source/ownership rather than falsely claimed byte-for-byte complete"
  remaining_obligation: "develop a genuinely critical parabolic-order moving-shape theorem with a matching existence/obstruction phase criterion, then obtain P26 plus a distinct OTHER-track audit before any closure claim"
```
