Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the final `n=30` F0111 scalar branches `N=|K|=12,13` are eliminated for all `s=z-1>0` and arbitrary within-block heterogeneity; combined with the earlier exact `N=11,14` eliminations, the full-support two-level Hessian-null `z>1` mechanism now has `2 -> 0` surviving integer branches. Methods #8 GO THE OTHER WAY AND DISCRETIZE, #20 FIND WHY THE ALGORITHM FAILS, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R15 retained screen — complete elimination of the dimension-30 full-support two-level Hessian-null branch

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand's full discrete Convexity Conjecture, and does not satisfy the two-other-track audit rule.

The immediately preceding complete R15 report is

`runs/R15/20260920_1354Z_successor_screen_f0111_smallscale_interiors_w108e.md`.

The new route was written **before checker code** in

`artifacts/R15/f0111_corridor_fixedray_idea_x109f.md`

at commit

`8c87e505f2bf2a837343b3aabea74c28a86f5d1f`.

All thirty Section-B move numbers have appeared in older R15 history, so the present `#8/#20/#30` triple is a nonconsecutive reuse on a new reduced object, not a claim that these numbers were globally unused.

## 1. Continuity, source, ownership, whole-repository readback

Before new mathematics I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the exact I0076 intake row in `probability_1000_intake_I_20260914/problems.jsonl`;
- the controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- newest own report `runs/R15/20260920_1354Z_successor_screen_f0111_smallscale_interiors_w108e.md`;
- neighboring Burdzy--Scheutzow Problem-7.8 terminal handoff `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- the prior scalar-envelope, `N=14`, `N=11`, adaptive-ray, boundary-curve, and small-scale exact R15 reports needed below.

The intake row is source-exact: I0076 is Burdzy--Scheutzow, *Forward Brownian Motion*, Problem 7.2, asking whether FBM + BBM + independence of the complete centered future/past at **some random time** implies 2BM. `QUEUE.md` continues to distinguish PENDING reserve entries from READY assignments and still has zero newly certified free READY entries. I therefore did not steal another track, promote a PENDING row, edit shared roots, or fabricate a new claim.

Problem 7.5 and already-posted/settled work remain excluded.

## 2. Exact native I0076 source and metric state

Primary source rechecked today: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM: there are random origins `S_n -> -infinity` a.s. whose complete centered futures are standard Brownian motions;
- BBM: the time-reversed process is FBM;
- 2BM: there exists one random time `S` at which the complete centered future and past are **independent standard Brownian motions**.

Problem 7.2 says only that `X` is FBM and BBM and that there exists a random time `T` for which the two complete centered half-processes are independent. It does **not** say that `T` is deterministic, does **not** make `T` a stopping time, and does **not** separately assume that either seam half is Brownian.

The nearby Proposition 6.2 proves a different stronger-seam obstruction for the paper's Section-6 construction: it excludes independence **plus** a Brownian forward half. That does not by itself answer bare Problem 7.2.

The controlling six-run handoff remains binding:

- the source Theorem-6.1 construction has FBM, BBM and failure of 2BM, but no source-valid independent seam;
- the later Brownian-prefix/BES candidate has FBM, BBM and an exact independent seam, but R15's Palm analysis proves that candidate is actually 2BM.

Hence there is still **no surviving frozen counterexample candidate** on which the requested four obligations can honestly be scored. Historical `2/4` and `3/4` values belong to retired candidates/diagnostics. Native status remains **OPEN / PARTIAL / RETIRED-HANDOFF** and the native unchanged count remains frozen at six.

Fresh dated public searches on 2026-09-20 included exact-title / exact-Problem-7.2 variants, the arXiv identifier, later-author/citing variants, and the current University of Washington publication record. They recovered the primary article but no accessible later primary paper explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

## 3. Current F0111 literature scope

For the retained screen I also rechecked current 2026 primary literature:

- Ascoli--He--Park--Talagrand, arXiv:2608.11183 (submitted 11 Aug 2026), reformulates the discrete Convexity Conjecture by `k`-thresholds and proves substantial graph-property classes;
- Park, arXiv:2609.14681 (13 Sep 2026), proves a dimension-free comparison and explicitly describes its application as a bound **toward** the discrete Convexity Conjecture.

I found no accessible source matching the restricted dimension-30 theorem below in this bounded search. **Novelty remains UNVERIFIED.** The theorem below is not being promoted to a full solution.

## 4. Carried exact scalar reduction

For the cardinality-two hazard in dimension 30,

\[
F(q)=\sum_iq_i-\log\!\left(\sum_i e^{q_i}-29\right),
\]

consider an interior exact quadratic contact whose contact Hessian has a full-support two-level mixed null vector. On the only remaining orientation write

\[
z=1+s>1,\qquad d=\delta\in(0,1),\qquad N=|K|.
\]

The exact cubic-null / projective reduction gives

\[
U_K(d,s)=
\frac{29(d+1)(d+s+1)(d+2s+1)}{4(s+1)(s+2)},
\]

and

\[
L_K(d,s)=
-\frac{(d+2s+1)P(d,s)}{2(d-1)Q(d,s)},
\]

where

\[
\begin{aligned}
P={}&d^2s^2+d^2s+7ds^3+26ds^2+32ds+12d\\
&+9s^4+51s^3+109s^2+103s+36,
\end{aligned}
\]

\[
Q=d^2s+d^2+3ds^2+6ds+4d+3s^3+9s^2+9s+3.
\]

Every scalar survivor satisfies

\[
L_K(d,s)\le N<U_K(d,s).
\tag{4.1}
\]

The scalar-envelope theorem already proves `L_K,U_K` strictly increase in both `d` and `s`, and reduces the integer possibilities to

\[
N\in\{11,12,13,14\}.
\]

Earlier exact runs completely eliminate `N=14` and `N=11`, with arbitrary within-block heterogeneity. Thus before this run only

\[
N\in\{12,13\}
\]

remain. Their exact outer scalar cells satisfy

\[
N=12:\quad
0<s<\frac{3601}{250000},\quad
\frac{49}{100}-\frac{s}{4}<d<\frac12-\frac9{10}s,
\tag{4.2}
\]

\[
N=13:\quad
0<s<\frac{12637}{10^6},\quad
\frac{53}{100}-\frac{s}{5}<d<\frac7{13}-\frac45s.
\tag{4.3}
\]

The heavy-coordinate theorem gives

\[
r_*<1-15s\quad(N=12),\qquad r_*<1-17s\quad(N=13).
\tag{4.4}
\]

The preceding run already proves **both entire cells are impossible for**

\[
0<s\le10^{-4}.
\tag{4.5}
\]

It remains only to treat `s>=10^-4`.

## 5. Method #20 — diagnose the failed full-cell interval algorithm

The preceding direct two-dimensional exact interval attempt boxed the complete outer strips (4.2)--(4.3). It over-refined because it ignored the much thinner true feasible corridor (4.1).

For each fixed `s`, monotonicity in `d` gives unique roots

\[
U_K(d_U(s),s)=N,\qquad L_K(d_L(s),s)=N,
\]

and every survivor obeys

\[
d_U(s)<d\le d_L(s).
\tag{5.1}
\]

Since both `L_K` and `U_K` increase with `s` as well, both roots decrease with `s`. Therefore, on any rational slab `[s_0,s_1]`, the **entire feasible set** lies in

\[
\boxed{
[d_U(s_1),d_L(s_0)]\times[s_0,s_1].
}
\tag{5.2}
\]

This converts the two-dimensional search into a one-dimensional sequence of thin exact corridor boxes. That is the essential algorithmic change.

## 6. Method #30 — a fixed ray valid throughout the post-small-scale corridor

Let

\[
\varepsilon=\frac1{400},\qquad t=1+\varepsilon=\frac{401}{400}.
\tag{6.1}
\]

The carried scalar bound `S<20/s`, together with `s>=10^-4`, gives

\[
S<200000.
\]

The exact Taylor lower sum used by the checker proves

\[
e^{28}>200000
\]

with rational margin

\[
\frac{149380673}{45}>0.
\]

Hence

\[
\varepsilon\log S<\frac{28}{400}=\frac7{100}.
\tag{6.2}
\]

The earlier adaptive-ray theorem was proved for every effective parameter `0<c<=7/100`. Applying it pointwise with

\[
c_{\rm eff}=\varepsilon\log S
\]

shows that the arbitrary `J`-block distribution is still maximized at the heavy-cap two-coordinate profile for this **fixed** ray.

Put

\[
C_{12}=15,\qquad C_{13}=17,
\]

\[
D=S^{-1}=-\frac{k}{29},\qquad
\eta=U_K-N,
\]

and scale the two heavy coordinates by `S`:

\[
A=1-C_Ns.
\]

The second coordinate has the exact simplification

\[
\boxed{
B=C_Ns+(1-\eta)D.
}
\tag{6.3}
\]

Indeed, the carried formula is

\[
B=x-1+C_Ns-(M-2)D,
\]

while `x=1-k-y`, `-k=29D`, `y=U_KD=(N+\eta)D` and `M=30-N`. Therefore

\[
\boxed{A+B-D=1-\eta D.}
\tag{6.4}
\]

This mass-defect identity is what makes the fixed-ray bound stable.

## 7. A short global bound for the K-block factor

The last negative K-block term uses

\[
c_K=\frac{U_K}{L_K}.
\]

We need only the simple uniform roof

\[
\boxed{c_K<\frac{21}{20}.}
\tag{7.1}
\]

For `N=12`, the upper wall in (4.2), monotonicity of `U_K`, and direct simplification give

\[
\eta<\eta_{12}^+(s)
=-\frac{3(957s^3+30065s^2+41475s-625)}
{4000(1+s)(2+s)}.
\]

Its derivative is

\[
-\frac{87(33s^4+198s^3+1878s^2+4190s+2925)}
{4000(1+s)^2(2+s)^2}<0,
\]

so

\[
\eta<\eta_{12}^+(0)=\frac{15}{64}<\frac14.
\tag{7.2}
\]

Similarly for `N=13`,

\[
\eta<\eta_{13}^+(s)
=-\frac{382278s^3+6265675s^2+7882875s-109750}
{274625(1+s)(2+s)},
\]

with derivative

\[
-\frac{174(2197s^4+13182s^3+75907s^2+145300s+92500)}
{274625(1+s)^2(2+s)^2}<0,
\]

and hence

\[
\eta<\eta_{13}^+(0)=\frac{439}{2197}<\frac14.
\tag{7.3}
\]

For `N=12`, the lower wall and the scalar `s` roof give

\[
d>\frac{486399}{10^6}>\frac{17}{35}.
\]

Since `L_K` increases in `d,s` and `L_K(d,0)=6/(1-d)`, this implies

\[
L_K>\frac{35}{3}.
\]

Together with `U_K=N+\eta<49/4`,

\[
\frac{U_K}{L_K}<\frac{49/4}{35/3}=\frac{21}{20}.
\]

For `N=13`, analogously

\[
d>\frac{2637363}{5\cdot10^6}>\frac{139}{265},
\]

so

\[
L_K>\frac{265}{21},\qquad U_K<\frac{53}{4},
\]

and again

\[
\frac{U_K}{L_K}<\frac{53/4}{265/21}=\frac{21}{20}.
\]

This proves (7.1) without any within-block symmetry assumption.

## 8. Method #8 — remove fractional powers and certify thin rational corridors

The carried K-excess theorem and secant bound imply that every survivor satisfies the coarse necessary inequality

\[
\overline\Gamma_N\le0,
\tag{8.1}
\]

where, after scaling by (6.3),

\[
\overline\Gamma_N
=-\frac1t\log(A^t+B^t-D^t)
-\varepsilon U_{\max}q_1q_2
-\left(1+\frac\eta2\right)\eta D c_K,
\tag{8.2}
\]

\[
q_1=\log(A/D),\qquad q_2=\log(B/D).
\]

Now `0<A,B,D<1` throughout both cells. For `u<=0`,

\[
e^u\le1+u+\frac{u^2}{2},
\]

and for every real `u`,

\[
e^u\ge1+u.
\]

Define

\[
E=-A\log A-B\log B+D\log D,
\]

\[
V=A\log^2A+B\log^2B.
\]

Applying the quadratic upper bound to `A^t,B^t` and the tangent lower bound to `D^t`, then using (6.4), gives

\[
A^t+B^t-D^t
\le
1-\eta D-\varepsilon E+\frac{\varepsilon^2}{2}V.
\]

Since `-log x>=1-x` for `x>0`,

\[
\boxed{
 t\overline\Gamma_N
\ge
\eta D+\varepsilon E-\frac{\varepsilon^2}{2}V
-t\varepsilon U_{\max}q_1q_2
-t\left(1+\frac\eta2\right)\eta Dc_K.
}
\tag{8.3}
\]

For the exact certificate I even **drop** the positive term `eta D` and bound `c_K` by `21/20`. Thus any positive certified lower bound for the remaining expression is sufficient.

The checker uses only:

- exact `Fraction` arithmetic;
- 32-step exact dyadic brackets of `d_U(s)` and `d_L(s)`;
- the corridor enclosure (5.2);
- exact rational interval arithmetic for every rational expression;
- exact logarithm enclosures obtained from

\[
\log y=2\sum_{j\ge0}\frac{w^{2j+1}}{2j+1},
\qquad w=\frac{y-1}{y+1},\quad 1\le y\le2,
\]

with an explicit rational geometric tail after 18 terms and powers-of-two rescaling.

The exact simplified formulas used for `U_max/s` are

\[
\frac{U_{\max}}s
=\frac{(d+s+1)(-11d^2-20ds+4d+4s^2+34s+19)}
{4(d+1)^2(d+3s+3)}
\quad(N=12),
\tag{8.4}
\]

and

\[
\frac{U_{\max}}s
=\frac{(d+s+1)(-6d^2-11ds+2d+2s^2+18s+10)}
{2(d+1)^2(d+3s+3)}
\quad(N=13).
\tag{8.5}
\]

No sampled path and no floating-point sign decision enters the proof.

## 9. Executed exact certificate

Checker:

`artifacts/R15/f0111_corridor_fixedray_checker_x109f.py`

committed at

`d6a513252025a675068d41929fadd9cce729c368`.

Executed output:

`artifacts/R15/f0111_corridor_fixedray_checker_x109f.out`

committed at

`5ed4ada7b7eb6b6f6be953d121155a414f74146d`.

Both were read back at those exact commits.

Starting from 64 rational `s` slabs and refining only failed enclosures, the exact result is:

- `N=12`: 83 terminal slabs, maximum extra depth 3; the worst exact rational lower bound is positive. Its float rendering is only a summary, `1.261996947169277e-06`; the exact positive numerator has 36294 bits and denominator 36314 bits.
- `N=13`: 67 terminal slabs, maximum extra depth 2; the worst exact rational lower bound is positive. Float summary `2.6857603845101985e-06`; exact numerator 36989 bits, denominator 37008 bits.

The archived output ends

`FULL_REMAINING_N12_N13_CORRIDORS_EXCLUDED_FOR_S_GE_1E_MINUS_4`

and

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit.

## 10. New restricted theorem

From (8.3) and the exact certificate,

\[
\boxed{
\overline\Gamma_N(d,s)>0
}
\]

for every scalar-feasible point in either `N=12` or `N=13` cell with

\[
s\ge10^{-4}.
\]

But every survivor would require `overlineGamma_N<=0`; hence none exists. Combining with the preceding exact small-scale theorem (4.5),

\[
\boxed{
\text{there is no full-support two-level Hessian-null exact quadratic contact}
}
\]

in either `N=12` or `N=13` branch for **any** `s>0`.

Earlier exact runs already eliminate `N=11` and `N=14`. Since the scalar-envelope theorem proves those four integers exhaust the dimension-30 `z>1` possibilities, we obtain the stronger combined restricted conclusion

\[
\boxed{
\text{the dimension-30 full-support two-level Hessian-null }z>1
\text{ branch has no survivors.}
}
\tag{10.1}
\]

No within-block symmetry was used.

This is a genuine completion of the **restricted first-bifurcation mechanism**, not of F0111 or Talagrand's conjecture. The broader problem can still involve null directions not of the full-support two-level form, zeros in the null vector/contact support, multiple-null configurations, or a different/global contact mechanism. Those possibilities are outside (10.1).

## 11. Why the three moves helped

**#20 FIND WHY THE ALGORITHM FAILS.** The old exact interval algorithm failed because it boxed the outer two-dimensional strips rather than the true root-defined feasible corridor. Identifying that dependency loss was the key step.

**#30 ONE SCALE / ONE DIRECTION AT A TIME.** Exact monotonicity turns each `s` slab into one thin `d` corridor, and the constant ray `t=401/400` avoids an extra adaptive logarithmic parameter.

**#8 DISCRETIZE.** The remaining analytic problem becomes finitely many rational slabs with exact root brackets and exact log tails. The discretization certifies a theorem rather than sampling trajectories.

## 12. Native ledger state and remaining obligations

The native Burdzy--Scheutzow target does not move. There is no surviving frozen counterexample candidate, so its four-obligation metric is still not scoreable. The six-run I0076 handoff remains the controlling state and is not incremented by retained-screen work.

The retained F0111 secondary branch count does move:

\[
\{12,13\}\longrightarrow\varnothing,
\]

and, together with the previous `11,14` eliminations, the restricted dimension-30 two-level branch is exhausted.

No independent audit was requested or simulated. No shared ledger/root was edited. No email, Drive, public posting, permission change, purchase, or scheduler change was performed.

```yaml
ledger_delta:
  worker: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958v4, Problem 7.2 / I0076"
  target: "decide whether FBM + BBM + independent centered halves at an arbitrary random time imply 2BM"
  native_metric:
    name: "number of four source-matching obligations proved for one surviving frozen counterexample candidate"
    before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
    after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
    movement: "none"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "6, frozen by mandatory handoff"
  tried_moves: [8, 20, 30]
  retained_screen:
    target: "F0111 k=2, n=30, full-support two-level Hessian-null z>1 mechanism"
    status: "PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
    secondary_metric_before: "remaining scalar integer branches {12,13}"
    secondary_metric_after: "empty set"
    new_result: "N=12 and N=13 excluded for all s>0; with earlier N=11,N=14 exclusions, no branch survives"
  remaining_obligation_native: "A genuinely new source-valid I0076 route/candidate after reassignment, or a proof covering the complete source hypotheses; current route is retired."
  remaining_obligation_retained: "The broader F0111 problem outside the full-support two-level Hessian-null mechanism remains untouched by this restricted theorem."
  evidence:
    idea_commit: "8c87e505f2bf2a837343b3aabea74c28a86f5d1f"
    checker_commit: "d6a513252025a675068d41929fadd9cce729c368"
    output_commit: "5ed4ada7b7eb6b6f6be953d121155a414f74146d"
    checker_result: "ALL_EXACT_CHECKS_PASS"
  audits: []
```

## 13. Model / scheduler control limitation

This actual run again executed as **GPT-5.6 Sol**, with reasoning level **UNVERIFIED**. The exposed scheduler/update surface still has prompt/title, schedule/timing, timing mode, enabled-state and ordinary update controls, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution control. Therefore GPT-6 / maximum remains a prompt request, not an attested runtime setting.

The operations manifest still records the historical P26 response `You cannot modify this task.` for one authorization context; repository continuity also records later successful P26 editing from an authorized context. The compliant workaround is to modify the same task from its owning/authorized workspace/account/API/admin surface or through platform support. A real GPT-6/maximum fix requires a scheduler/backend surface that exposes and persists those routing controls and returns authenticated runtime telemetry. No permission bypass or duplicate task was attempted here.
