Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: both remaining F0111 dimension-30 cells `N=12,13` are now excluded throughout the full arbitrary-heterogeneity interior strip `0<s=z-1<=10^{-4}`, not merely on the lower scalar boundary. Methods #6 DEFORM TO A POINT YOU CAN SOLVE, #19 MAKE IT AN ALGORITHM, #25 COUNT THE SAME THING TWICE.**

# R15 retained screen — exact small-scale interior exclusion for N=12,13

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, and does not claim Talagrand's full discrete Convexity Conjecture is solved.

The preceding completed report is

`runs/R15/20260920_1316Z_successor_screen_f0111_boundary_curve_v107d.md`.

Its Section-B triple was `#7/#12/#29`; this run uses `#6/#19/#25`. All thirty move numbers already occur somewhere in older R15 history, so these are reused on the newly reduced object rather than represented as globally unused.

The mathematical route was written before any new checker code in

`artifacts/R15/f0111_smallscale_interior_idea_w108e.md`

at commit

`18616b9e8f741dc07bc3a218ee45dd63a5123b55`.

Only afterward was the exact finite arithmetic checker added and executed.

## 1. Whole-repository continuity, source fidelity, exclusions, and ownership

Before new mathematics I reread/recovered the current `master` state required by the owner policy:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the controlling native handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- newest own report `runs/R15/20260920_1316Z_successor_screen_f0111_boundary_curve_v107d.md`;
- neighboring Burdzy--Scheutzow Problem 7.8 terminal handoff `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- exact repository searches for `I0076`, `Problem 7.2`, and current queue/claim state.

The current queue still says newly certified free READY inventory is zero; a listed PENDING row is not automatically dispatchable. I therefore did not reopen a retired source, claim another worker's target, or edit shared roots.

### Exact Burdzy--Scheutzow source, rechecked 2026-09-20

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM: there are random times `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there exists one random time `S` such that the complete centered future and past at `S` are independent standard Brownian motions.

Problem 7.2 assumes FBM + BBM and existence of **an arbitrary random time** `T` for which the two complete centered half-processes are independent. It does not say that `T` is a stopping time and does not separately assume either seam half is Brownian. The nearby Proposition 6.2 excludes, for the Section-6 construction, the stronger combination of seam independence plus a Brownian forward half; it does not settle the bare Problem-7.2 hypothesis.

The native state is unchanged. The source Theorem-6.1 construction has FBM, BBM and failure of 2BM but no source-valid independent real seam. The later Brownian-prefix/BES construction has FBM, BBM and the exact independent seam but was proved by the existing R15 Palm argument to be 2BM. Hence there is **no surviving frozen counterexample candidate** on which the owner's four source obligations can honestly be scored. Historical `2/4` and `3/4` values belong to eliminated candidates or the retired positive-route diagnostic.

Native I0076 therefore remains **OPEN / PARTIAL / RETIRED-HANDOFF**, with the mandatory six-run handoff binding and the native unchanged count frozen at six. Retained-screen work below does not increment that streak.

Fresh dated public searches on 2026-09-20 used the exact title/arXiv number/Problem-7.2 language and later-author/citing-paper variants. They recovered the primary paper but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

For the retained F0111 context I also checked Ascoli--He--Park--Talagrand, arXiv:2608.11183 (submitted 2026-08-11), which reformulates Talagrand's discrete Convexity Conjecture via k-thresholds and proves broad classes, and Park, arXiv:2609.14681 (submitted 2026-09-13), which explicitly describes its dimension-independent consequence as a bound toward the conjecture. Novelty of the restricted R15 theorem below remains **UNVERIFIED**.

## 2. Carried final two-cell reduction

The retained hazard is

\[
F(q)=\sum_{i=1}^{30}q_i-\log\left(\sum_{i=1}^{30}e^{q_i}-29\right).
\]

For the full-support, two-level Hessian-null first-bifurcation screen on

\[
z=1+s>1,
\]
all earlier exact reductions leave only

\[
N:=|K|\in\{12,13\},\qquad M=30-N.
\]

Put `d=delta`, `a=1+d`, `b=1-d`. The carried exact scalar functions are

\[
k=\frac{2z(1-z^2)}{(1-d^2)(d+3z)},
\]

\[
y=\frac{(d+z)(1-z)(1-d-2z)}{2(1-d)(d+3z)},
\qquad x=1-k-y,
\]

\[
S=-\frac{29}{k},
\qquad
U_K=-\frac{29y}{k},
\qquad
L_K=yA_K,
\]
with `A_K` and the corresponding `A_J` from the carried projective Gram reduction. Scalar feasibility is

\[
L_K\le N<U_K.
\tag{2.1}
\]

The previous arbitrary-heterogeneity theorem provides

\[
U_{\max}<\frac98s,
\qquad
\frac{29}{20}<\frac{-k}{s}<\frac{13}{8},
\tag{2.2}
\]
through both remaining cells, and the heavy-coordinate caps

\[
r_*<1-C_Ns,
\qquad C_{12}=15,\quad C_{13}=17.
\tag{2.3}
\]

For the adaptive face ray, every `0<c<=7/100` is allowed by the earlier monotonicity proof. This run fixes

\[
c=\frac3{100},\qquad
\varepsilon=\frac{c}{\log S},\qquad t=1+\varepsilon.
\tag{2.4}
\]

The arbitrary `J` distribution is then maximized in the closure at

\[
u_1=S(1-C_Ns),
\qquad
u_2=S(x-1+C_Ns)-(M-2).
\tag{2.5}
\]

The preceding K-excess theorem gives

\[
\eta:=U_K-N,
\qquad D:=S^{-1}=-k/29,
\qquad c_K:=U_K/L_K,
\]

\[
K_{\rm sec}=\eta D\frac{c_K\log c_K}{c_K-1},
\tag{2.6}
\]
and every survivor must satisfy

\[
\widehat\Gamma_N
:=\log S-\left(1+\frac\eta2\right)K_{\rm sec}-H_J^*\le0.
\tag{2.7}
\]

The preceding v107d report proves the full lower scalar boundary `U_K=N` already violates (2.7). The present run moves from that one-dimensional boundary into the complete two-dimensional small-scale interiors.

## 3. Method #25 — a mass-defect identity and a coarser gate

For `c_K>=1`,

\[
\log c_K\le c_K-1,
\]
so

\[
K_{\rm sec}\le \eta D c_K.
\tag{3.1}
\]

Define

\[
\boxed{
\overline\Gamma_N
:=\log S-H_J^*-\left(1+\frac\eta2\right)\eta D c_K.
}
\tag{3.2}
\]

Then

\[
\overline\Gamma_N\le\widehat\Gamma_N.
\tag{3.3}
\]

Thus every survivor must also satisfy `overlineGamma_N<=0`; proving the coarser gap positive is enough to contradict (2.7).

Now scale the two-heavy extremizer by `S`:

\[
A=1-C_Ns,
\qquad
B=x-1+C_Ns-(M-2)D.
\tag{3.4}
\]

Then `u_1=SA`, `u_2=SB`. Using exactly

\[
x=1-k-y,\qquad y=U_KD,\qquad -k=29D,\qquad M-1=29-N,
\]
we obtain

\[
\begin{aligned}
A+B-D
&=x-(M-1)D\\
&=1+29D-U_KD-(29-N)D\\
&=1-(U_K-N)D.
\end{aligned}
\]
Hence the new conserved defect identity is

\[
\boxed{A+B-D=1-\eta D.}
\tag{3.5}
\]

Put

\[
\mathcal F=A^t+B^t-D^t,
\qquad q_1=\log(SA),
\qquad q_2=\log(SB).
\tag{3.6}
\]

Because

\[
u_1^t+u_2^t-1=S^t\mathcal F,
\]
the large `log S` terms cancel exactly and (3.2) becomes

\[
\boxed{
\overline\Gamma_N
=-\frac1t\log\mathcal F
-\varepsilon U_{\max}q_1q_2
-\left(1+\frac\eta2\right)\eta Dc_K.
}
\tag{3.7}
\]

This is the useful invariant of the run: the K excess appears both as the missing scaled mass in (3.5) and as the only complementary energy budget in (3.7).

## 4. Method #6 — deform the whole interior to the exact small-scale regime

We prove that no survivor can have

\[
0<s\le10^{-4}.
\tag{4.1}
\]

The carried outer scalar strips are

\[
N=12:\quad
\frac{49}{100}-\frac{s}{4}<d<\frac12-\frac9{10}s,
\tag{4.2}
\]

\[
N=13:\quad
\frac{53}{100}-\frac{s}{5}<d<\frac7{13}-\frac45s.
\tag{4.3}
\]

### 4.1 A uniform slope roof for x

Direct simplification of the exact formula for `x` gives

\[
\boxed{
\frac{x-1}{s}
=
\frac{d^2+3ds+4d+2s^2+9s+7}
{2(d+1)(d+3s+3)}.
}
\tag{4.4}
\]

The difference from `9/10` has the sign of

\[
P(d,s)=2d^2+6ds+8d-5s^2-9s-4.
\tag{4.5}
\]

On the relevant rectangle, `P` increases in `d` and decreases in `s`. The worst possible lower wall is the N=12 wall at `s=10^{-4}`:

\[
d\ge\frac{19599}{40000}.
\]
The exact margin is

\[
P\left(\frac{19599}{40000},\frac1{10000}\right)
=
\frac{319475949}{800000000}>0.
\tag{4.6}
\]
Therefore, throughout both cells in (4.1),

\[
\boxed{\frac{x-1}{s}<\frac9{10}.}
\tag{4.7}
\]

### 4.2 The K excess and cap are uniformly tiny

The exact scalar function

\[
U_K(d,s)=
\frac{29(d+1)(d+s+1)(d+2s+1)}{4(s+1)(s+2)}
\tag{4.8}
\]
is increasing in both `d` and `s` on the retained region. In particular,

\[
\frac{49}{4}-U_K\left(\frac12,10^{-4}\right)
=rac{2002077}{133353334}>0,
\tag{4.9}
\]

\[
\frac{53}{4}-U_K\left(\frac7{13},10^{-4}\right)
=rac{29056383467}{585954549596}>0.
\tag{4.10}
\]
Hence

\[
\boxed{0<\eta<1/4}
\tag{4.11}
\]
for both cells.

The carried scalar theorem also proves that `L_K` is increasing in `d,s` and

\[
L_K(d,0)=\frac6{1-d}.
\tag{4.12}
\]
The lower d-walls satisfy

\[
\frac{19599}{40000}>\frac{19}{39},
\qquad
\frac{26499}{50000}>\frac{67}{127},
\]
so

\[
N=12:\quad L_K>117/10,
\qquad
N=13:\quad L_K>127/10.
\tag{4.13}
\]
Combining (4.9)--(4.13),

\[
\boxed{c_K=U_K/L_K<21/20.}
\tag{4.14}
\]

### 4.3 Exact logarithmic roofs

From (2.2),

\[
S<20/s,
\qquad
S>\frac{232}{13s}.
\tag{4.15}
\]
For `s<=10^{-4}`, the exact exponential certificate from v107d gives

\[
\log S>12,
\]
so

\[
\boxed{\varepsilon<1/400,\qquad t<401/400.}
\tag{4.16}
\]

By (4.7),

\[
u_2<S(x-1+C_Ns)<20(C_N+9/10).
\tag{4.17}
\]
Exact Taylor lower sums give

\[
e^{29/5}>318,
\qquad e^{59/10}>358,
\]
with positive rational margins archived by the checker. Therefore

\[
\boxed{
q_2<29/5\quad(N=12),
\qquad
q_2<59/10\quad(N=13).
}
\tag{4.18}
\]
Also `0<q_1<log S` by the carried two-heavy profile.

Finally, from (2.2),

\[
D=-k/29<\frac{13}{232}s,
\]
and hence by (4.11)

\[
\boxed{\eta D<\frac{13}{928}s.}
\tag{4.19}
\]

## 5. Entropy-versus-energy contradiction on the complete small-scale cells

Since `A,B,D` lie in `(0,1)` on the retained two-heavy profile and

\[
D^t=De^{-c}
\]
exactly, use

\[
e^u\le1+u+u^2/2\qquad(u\le0).
\]
Define

\[
\mathcal E=-A\log A-B\log B+D\log D,
\qquad
\mathcal V=A\log^2A+B\log^2B.
\tag{5.1}
\]
Using (3.5),

\[
1-\mathcal F
\ge
\eta D+\varepsilon\mathcal E
-\frac{\varepsilon^2}{2}\mathcal V
+D(c-1+e^{-c}).
\tag{5.2}
\]
The last term is nonnegative. Moreover, because `log D=-log S` and `q_2=log(SB)`, (3.5) yields the stable entropy identity

\[
\boxed{
\mathcal E
=-A\log A+(C_Ns-\eta D)\log S-Bq_2.
}
\tag{5.3}
\]

Whenever the resulting lower bound makes `mathcal F<1`, the inequality `-log mathcal F>=1-mathcal F` together with (3.7) gives

\[
\begin{aligned}
t\overline\Gamma_N
\ge{}&
\varepsilon\left(
\mathcal E-\frac\varepsilon2\mathcal V
-tU_{\max}q_1q_2
\right)\\
&+\eta D\left[
1-t\left(1+\frac\eta2\right)c_K
\right].
\end{aligned}
\tag{5.4}
\]

We now bound every negative contribution in (5.4) by a rational multiple of `s`.

First, the positive term `-A log A` in (5.3) may be discarded. Since `epsilon log S=c`, (4.19) gives the entropy-excess loss

\[
c\eta D<\frac{39}{92800}s.
\tag{5.5}
\]
Put

\[
\beta_N=C_N+9/10.
\]
Then `B<beta_N s`, so by (4.16), (4.18),

\[
\varepsilon Bq_2
<\frac1{400}\beta_N q_{2,N}s.
\tag{5.6}
\]

For the variance, `|log B|=log S-q_2<log S`, hence

\[
\frac{\varepsilon^2}{2}B\log^2B
<\frac{c^2}{2}\beta_Ns
=\frac9{20000}\beta_Ns.
\tag{5.7}
\]
Also, with `p=C_Ns`,

\[
-\log(1-p)\le\frac{p}{1-p},
\]
so

\[
A\log^2A\le\frac{p^2}{A}.
\]
Using `epsilon<1/400` and `s<=10^{-4}` gives the additional coefficient

\[
\frac{C_N^2}{3200000000(1-C_N/10000)}s.
\tag{5.8}
\]

For the J-pair energy, `epsilon q_1<c`, `U_max<(9/8)s`, so

\[
t\varepsilon U_{\max}q_1q_2
<
\frac{401}{400}\frac3{100}\frac98 q_{2,N}s.
\tag{5.9}
\]

Finally, (4.11), (4.14), (4.16) imply

\[
t\left(1+\frac\eta2\right)c_K
<
\frac{401}{400}\frac98\frac{21}{20}
=rac{75789}{64000}.
\]
Thus the possible negative part of the second line of (5.4) is at most

\[
\left(\frac{75789}{64000}-1\right)\frac{13}{928}s
=rac{153257}{59392000}s.
\tag{5.10}
\]

Collecting (5.5)--(5.10) against the positive main contribution `c C_N s`, the checker obtains the exact strict margins

\[
\boxed{
N=12:\quad
\frac{t\overline\Gamma_{12}}s
>
\frac{38709573299}{2965145600000}
>0,
}
\tag{5.11}
\]

\[
\boxed{
N=13:\quad
\frac{t\overline\Gamma_{13}}s
>
\frac{523190108977}{14822758400000}
>0.
}
\tag{5.12}
\]

These positive bounds also force `mathcal F<1`, so the invocation of `-log mathcal F>=1-mathcal F` in (5.4) is self-consistent. Since `t>0`, (5.11)--(5.12) prove

\[
\boxed{
overline\Gamma_N(d,s)>0
\quad
\text{for every scalar-feasible point with }
N\in\{12,13\},\ 0<s\le10^{-4}.
}
\tag{5.13}
\]
But every survivor requires `overlineGamma_N<=0`. Contradiction.

### New restricted theorem

\[
\boxed{
\begin{minipage}{0.86\linewidth}
There is no dimension-30, full-support, two-level Hessian-null exact nonnegative quadratic contact in either remaining branch `N=12` or `N=13` with `0<z-1<=10^{-4}`. The statement permits arbitrary heterogeneity inside both sign blocks.
\end{minipage}
}
\tag{5.14}
\]

This is genuine movement beyond v107d: that report excluded only the one-dimensional lower scalar closure `U_K=N`; (5.14) removes the **entire two-dimensional small-scale interior** of both final cells.

## 6. Method #19 — algorithmic full-cell route, and why it did not close this run

After the analytic theorem was fixed, I tried the natural exact full-cell algorithm suggested by (5.4): rational interval arithmetic on `(d,s)`, discard boxes with `L_K>N` or `U_K<=N`, enclose all logarithms by the exact atanh series, and recursively subdivide only boxes whose lower bound for the right side of (5.4) is not positive.

This route is promising but did **not** produce a completed exact certificate in this run. The direct two-dimensional `Fraction` implementation suffers severe denominator growth and interval dependency in the three coupled logarithms; it over-refines before a global certificate is obtained. No partial numerical scan is counted as proof and no unexecuted full-cell certificate is archived.

The better next route is structural. Private route finding suggests the coarse gap is concave in `d` for fixed `s`. If exact concavity can be proved, its minimum is at a scalar-cell endpoint. The lower endpoint `U_K=N` is already excluded by v107d. It would then suffice to certify the opposite boundary `L_K=N` and concavity on `s>=10^{-4}`. This is the next attack, not a theorem claimed here.

## 7. Validation

The idea-before-code note was committed first at

`18616b9e8f741dc07bc3a218ee45dd63a5123b55`.

Only afterward I added

`artifacts/R15/f0111_smallscale_interior_checker_w108e.py`

at commit

`73da9cb6d09d04d02f9aa90818029b7c9fb8312d`.

The checker was executed with exact Python `Fraction` arithmetic. Its output was archived as

`artifacts/R15/f0111_smallscale_interior_checker_w108e.out`

at commit

`0a0179f30d86ace9931ad26177d3d5b5b68640d0`.

The output ends

`SMALLS_INTERIORS_N12_N13_EXCLUDED`

and

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit. No finite or numerical path sample is used to verify any Brownian law.

## 8. Model / scheduler / denied-task boundary

The requested GPT-6/maximum setting is still not binding in the exposed scheduler interface. This invocation actually ran GPT-5.6 Sol; the reasoning-effort route is not authenticated by the interface and is therefore reported as UNVERIFIED.

The exposed scheduling/update schema offers title, prompt, schedule or relative start, timing mode, enabled state and ordinary task update fields. It exposes no model-family field, no reasoning-effort field, no authenticated completed-run model/effort receipt and no guaranteed hour-long execution control. A genuine fix therefore requires an owner/admin/product/API scheduler surface that actually persists model and effort fields and returns runtime telemetry; prompt text cannot enforce this by itself.

The historical P26 response `You cannot modify this task` was authorization-context-specific. The current repository also records a later successful P26 update from a different authorized P/C context. The compliant workaround for any edit-denied task is therefore to modify that same task from its owning/authorized workspace/account/API/admin context or use platform support. It is not to duplicate the task or bypass permissions. This worker made no scheduler changes.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.2; intake I0076"
  native_target: "Decide whether FBM + BBM + source-exact independent centered half-processes at an arbitrary random time implies 2BM."
  native_metric_before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
  native_metric_after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
  native_status: OPEN / PARTIAL / RETIRED-HANDOFF
  native_unchanged_count: 6_FROZEN_AT_MANDATORY_HANDOFF
  tried_moves:
    - 6_DEFORM_TO_A_POINT_YOU_CAN_SOLVE
    - 19_MAKE_IT_AN_ALGORITHM
    - 25_COUNT_THE_SAME_THING_TWICE
  native_remaining_obligation: "Future reassignment only: prove or refute equality with 2BM on the full common-re-rooting invariant sigma-field; equivalently construct or exclude a nontrivial relative phase/common eigen-cocycle at infinity compatible with FBM, BBM and seam independence."
  native_evidence:
    - runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md
  retained_screen: F0111 / PENDING / SELF_CHECK_ONLY / NOT_CLAIMED
  retained_before: "N=12,13 remain; complete lower boundary U_K=N excluded, interiors still possible."
  retained_after: "Additionally, every scalar-feasible point in both N=12,13 cells with 0<s=z-1<=10^-4 is excluded, with arbitrary within-block heterogeneity."
  retained_evidence:
    - artifacts/R15/f0111_smallscale_interior_idea_w108e.md
    - artifacts/R15/f0111_smallscale_interior_checker_w108e.py
    - artifacts/R15/f0111_smallscale_interior_checker_w108e.out
  audits: []
  closure_claim: false
  next_obligation: "For s>=10^-4, prove an exact concavity/endpoint reduction for overlineGamma_N or find a different global interior obstruction; lower endpoint U_K=N is already certified."
```
