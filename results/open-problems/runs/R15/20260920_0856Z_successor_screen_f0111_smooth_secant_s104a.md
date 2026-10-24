Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the remaining F0111 `n=30`, `N=12,13` scalar gate is made floor-free by a sharp secant envelope on the K block, and the resulting smooth gate is proved uniformly positive to first order at the entire `s=z-1 -> 0+` boundary. Methods #6 DEFORM TO A POINT YOU CAN SOLVE, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT.**

# R15 retained screen — floor-free K secant and uniform boundary positivity

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand's discrete Convexity Conjecture, and does not satisfy the two-other-track audit rule.

The immediately preceding R15 report is

`runs/R15/20260920_0822Z_successor_screen_f0111_adaptive_ray_r103z.md`.

Its Section-B triple was `#5/#13/#30`; the present `#6/#11/#24` triple is nonconsecutive. All thirty move numbers have appeared somewhere in the older R15 history, so this is a reuse on a new reduced object, not a claim that these numbers are globally new.

The route was written before repository validation code in

`artifacts/R15/f0111_smooth_k_secant_idea_s104a.md`

at commit

`3e1bc9ddb84bb5047f4a278bd11662aa9fd20be5`.

Only after that note was committed did I add the small exact-arithmetic checker used in Section 8. Private scratch numerics used only for route finding are not evidence and are not counted as verification.

## 1. Whole-repository continuity, exclusions, and ownership

Before new mathematics I recovered or reread the current `master` state required by the owner directive:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- newest own report `runs/R15/20260920_0822Z_successor_screen_f0111_adaptive_ray_r103z.md`;
- neighboring Burdzy--Scheutzow Problem 7.8 terminal handoff `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- targeted repository searches for `I0076`, current queue ownership, and retained F0111 work.

`QUEUE.md` still distinguishes PENDING reserve entries from READY inventory and still records zero newly certified free READY entries. I therefore did not claim another worker's source, promote a PENDING row, or edit a shared root. Problem 7.5 and every exact scope already settled/posted in the campaign remain excluded.

## 2. Exact native I0076 source rechecked

Primary source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM: there are random origins `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there exists one random time `S` such that the complete centered future and complete centered past at `S` are independent standard Brownian motions.

Problem 7.2 asks whether **FBM + BBM + existence of an arbitrary random time `T` at which the two complete centered half-processes are independent** implies 2BM. The source does **not** assume `T` is a stopping time and does **not** separately assume either half at `T` is Brownian.

The nearby Proposition 6.2 proves a different stronger-seam obstruction for the Section-6 construction: it rules out a random seam having independence together with a Brownian forward half. It neither supplies nor rules out bare Problem-7.2 seam independence by itself.

### Native candidate / metric state

The six-run handoff remains binding.

- The source Theorem-6.1 construction has FBM, BBM and failure of 2BM but no source-valid independent random seam.
- The later Brownian-prefix/BES candidate has FBM, BBM and an exact independent seam, but R15's Palm analysis proves that candidate is actually 2BM.

Therefore there is **no surviving frozen counterexample candidate** on which the user's four obligations can honestly be counted. Historical `2/4` and `3/4` values belong to eliminated candidates or a retired positive-route diagnostic, not to a current frozen candidate.

Native status remains **OPEN / PARTIAL / RETIRED-HANDOFF**. The native unchanged count stays frozen at the mandatory six-run handoff; retained-screen work does not increment it.

A fresh dated public-source pass on 2026-09-20 recovered the original paper and current author/university records but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

## 3. Current retained-screen literature scope

The retained screen concerns Talagrand's **discrete** Convexity Conjecture, not the distinct continuous Gaussian convexity problem. Current primary literature checked this run includes:

- Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), which reformulates the discrete conjecture via `k`-thresholds and proves substantial classes;
- Jinyoung Park, arXiv:2609.14681 (2026-09-13), whose abstract gives a dimension-free comparison and explicitly describes its application as a bound *toward* the conjecture.

I found no accessible source matching the floor-free secant/boundary calculation below in this bounded search. **Novelty remains UNVERIFIED.**

## 4. Carried two-scalar gate

The retained hazard is

\[
F(q)=\sum_{i=1}^{30}q_i-\log\!\left(\sum_{i=1}^{30}e^{q_i}-29\right).
\]

For the full-support two-level Hessian-null first-bifurcation screen on the surviving branch

\[
z=1+s>1,
\]

all earlier exact reductions leave only

\[
N:=|K|\in\{12,13\},\qquad M=30-N.
\]

Put

\[
a=1+\delta,\qquad b=1-\delta,
\]

and carry the exact scalar quantities

\[
k=\frac{2z(1-z^2)}{(1-\delta^2)(\delta+3z)},
\]

\[
y=\frac{(\delta+z)(1-z)(1-\delta-2z)}{2(1-\delta)(\delta+3z)},
\qquad x=1-k-y,
\]

\[
K_2=\frac{(\delta+z)(1-z^2)}{\delta+3z},
\quad t_J=(1-z)^2-K_2,
\quad t_K=(1+z)^2-K_2,
\]

\[
R=-\frac{2(\delta+z)(1-z^2)(\delta^2z+3\delta z^2+\delta+3z^3)}{(\delta+3z)^2},
\]

\[
A_J=1+\frac{3t_J^2}{R},\qquad
A_K=1+\frac{3t_K^2}{R},
\]

\[
L_K=yA_K,\qquad U_K=-\frac{29y}{k},\qquad S=-\frac{29}{k}.
\]

Scalar feasibility requires

\[
L_K\le N<U_K.
\tag{4.1}
\]

The carried projective Gram bound is

\[
T_{\rm cap}=y(N-L_K),
\]

\[
U_{\max}=\frac12\left[\left(\frac ba\right)^2T_{\rm cap}-x+A_Jx^2\right],
\tag{4.2}
\]

and the `K-K` coefficient-energy roof is

\[
\overline E_K=rac{y(N-1)}2\log^2 c_K,
\qquad c_K:=\frac{U_K}{L_K}.
\tag{4.3}
\]

The preceding adaptive-ray theorem sets

\[
L=\log S,\qquad c=\frac7{100},\qquad
\varepsilon=\frac cL,\qquad t=1+\varepsilon,
\tag{4.4}
\]

and proves that the arbitrary heterogeneous `J` optimization is attained in the closure at

\[
u_1^*=S(1-C_Ns),
\]

\[
u_2^*=S(x-1+C_Ns)-(M-2),
\tag{4.5}
\]

with

\[
C_{12}=15,\qquad C_{13}=17.
\]

Thus

\[
H_J^*=
\frac1t\log\left((u_1^*)^t+(u_2^*)^t-1\right)
+(t-1)U_{\max}\log u_1^*\log u_2^*.
\tag{4.6}
\]

The only remaining non-smoothness in the prior two-scalar gate was the floor appearing in the exact capped-convex `K` extremizer.

## 5. Method #11 — dualize the K cap by its secant

At exact contact put

\[
v_j=e^{q_j}=Sr_j\qquad(j\in K).
\]

The residual coordinate cap gives

\[
1<v_j\le c_K,
\]

and the exact K-excess identity gives

\[
\sum_{j\in K}v_j=U_K=N+\eta_K,
\qquad \eta_K:=U_K-N>0.
\tag{5.1}
\]

The function

\[
f(v)=v\log v
\]

is convex. Hence for every `1<=v<=c_K`, its graph lies below the secant joining `(1,0)` and `(c_K,c_K log c_K)`:

\[
\boxed{
 v\log v
\le
\frac{v-1}{c_K-1}\,c_K\log c_K.
}
\tag{5.2}
\]

Summing (5.2) and using (5.1) yields the floor-free theorem

### Lemma R15-F0111-KSEC

\[
\boxed{
\frac1S\sum_{j\in K}v_j\log v_j
\le
K_{\rm sec}:=
\frac{U_K-N}{S}\,
\frac{c_K\log c_K}{c_K-1}.
}
\tag{5.3}
\]

The definition at `c_K=1` is by continuity. On the actual feasible cells `c_K>1`.

This bound is slightly weaker than the exact floor extremizer from the preceding report, but it removes **all floor subcells** and is sharp to first order as `U_K-N -> 0`.

Combining (5.3), (4.3), and (4.6) with the exact complement-face inequality from the preceding reports gives a single smooth necessary condition:

### Corollary R15-F0111-GAMMASEC

Every surviving `N=12` or `N=13` contact must satisfy

\[
\boxed{
\Gamma_N^{\rm sec}(\delta,s)
:=
\log S-\overline E_K-K_{\rm sec}-H_J^*
\le0.
}
\tag{5.4}
\]

Thus the remaining verification is no longer piecewise in the artificial integer `m_K=floor(eta_K/(c_K-1))`; it is one smooth two-variable sign problem for each `N`.

## 6. Method #6 — deform the smooth gate to `s=0`

The scalar quantities have the following uniform limits as `s->0+` with `d:=delta` in a compact subinterval of `(0,1)`:

\[
k=-\kappa(d)s+O(s^2),
\qquad
\kappa(d)=\frac4{(d+3)(1-d^2)},
\tag{6.1}
\]

\[
y=\nu(d)s+O(s^2),
\qquad
\nu(d)=\frac{(d+1)^2}{2(1-d)(d+3)},
\tag{6.2}
\]

\[
x=1+\xi(d)s+O(s^2),
\qquad
\xi(d)=\frac{d^2+4d+7}{2(d+1)(d+3)},
\tag{6.3}
\]

\[
S\,s\to\frac{29}{\kappa(d)},
\tag{6.4}
\]

\[
L_K\to L_0(d)=\frac6{1-d},
\qquad
U_K\to U_0(d)=\frac{29(1+d)^3}{8},
\tag{6.5}
\]

\[
c_K\to c_0(d)=\frac{29(1-d)(1+d)^3}{48},
\qquad
\eta_K\to\eta_0(d)=U_0(d)-N.
\tag{6.6}
\]

Also

\[
\frac{U_{\max}}s\to
\mu_N(d)
:=
\frac{N(1-d^2)+d^2+4d+7}{4(d+1)(d+3)}.
\tag{6.7}
\]

The smaller heavy coordinate converges to

\[
V_N(d)
:=
\frac{29}{\kappa(d)}\bigl(\xi(d)+C_N\bigr)-(28-N).
\tag{6.8}
\]

The limiting scalar-feasible closures satisfy

\[
U_0(d)\ge N,\qquad L_0(d)\le N,
\]

so

\[
\left(\frac{8N}{29}\right)^{1/3}-1\le d\le1-\frac6N.
\tag{6.9}
\]

For `N=12` this interval lies in `[49/100,1/2]`; for `N=13` it lies in `[53/100,27/50]`.

Now use the adaptive normalization

\[
S^{t-1}=e^c.
\]

Since `u_1^*=S(1-C_Ns)` and `u_2^*->V_N(d)`, uniformly on the limiting compact interval,

\[
\frac1s\left[
\log S-rac1t\log\left((u_1^*)^t+(u_2^*)^t-1\right)
\right]
\to
C_N-\frac{\kappa(d)(V_N(d)-1)}{29e^c}.
\tag{6.10}
\]

Further,

\[
\frac{\overline E_K}{s}
\to
\frac{\nu(d)(N-1)}2\log^2 c_0(d),
\tag{6.11}
\]

\[
\frac{K_{\rm sec}}s
\to
\frac{\kappa(d)}{29}\eta_0(d)
\frac{c_0(d)\log c_0(d)}{c_0(d)-1},
\tag{6.12}
\]

and

\[
\frac1s(t-1)U_{\max}\log u_1^*\log u_2^*
\to
c\,\mu_N(d)\log V_N(d).
\tag{6.13}
\]

Therefore

\[
\boxed{
\frac{\Gamma_N^{\rm sec}(d,s)}s\to G_N(d)
}
\tag{6.14}
\]

uniformly on the limiting feasible closure, where

\[
\begin{aligned}
G_N(d)={}&C_N
-\frac{\kappa(V_N-1)}{29e^c}
-\frac{\nu(N-1)}2\log^2c_0\\
&-\frac\kappa{29}\eta_0\frac{c_0\log c_0}{c_0-1}
-c\mu_N\log V_N.
\end{aligned}
\tag{6.15}
\]

The expression in (6.12) is interpreted continuously when `eta_0=0`; feasibility has `eta_0>=0`.

## 7. Method #24 — the boundary extremal is uniformly separated from zero

The point of (6.15) is that a very coarse **exact** envelope already leaves a large positive margin.

The derivative identities are elementary:

\[
\kappa'(d)=
\frac{4(3d^2+6d-1)}{(d-1)^2(d+1)^2(d+3)^2}>0,
\]

\[
\nu'(d)=\frac{4(d+1)}{(d-1)^2(d+3)^2}>0,
\]

\[
(c_0)'(d)=-\frac{29}{24}(d+1)^2(2d-1),
\qquad
\eta_0'(d)=\frac{87}{8}(d+1)^2>0.
\tag{7.1}
\]

For `N=12`,

\[
V_{12}'(d)=-\frac{87}{8}(31d^2+62d-9)<0,
\]

\[
\mu_{12}'(d)=
-\frac{2(6d^2+13d+8)}{(d+1)^2(d+3)^2}<0.
\tag{7.2}
\]

For `N=13`,

\[
V_{13}'(d)=-\frac{29}{8}(105d^2+210d-31)<0,
\]

\[
\mu_{13}'(d)=
-\frac{13d^2+28d+17}{(d+1)^2(d+3)^2}<0.
\tag{7.3}
\]

Hence endpoint evaluation gives the following rigorous roofs on the broad rational containing intervals.

### `N=12`

For `49/100<=d<=1/2`,

\[
\kappa<\frac{153}{100},\quad
\nu<\frac{65}{100},\quad
V_{12}<290,\quad
\mu_{12}<\frac{89}{100},
\]

\[
c_0<\frac{102}{100},\qquad
0\le\eta_0<\frac{24}{100}.
\tag{7.4}
\]

Use `e^c>1+c=107/100`, `log c_0<c_0-1<2/100`, and `log V_{12}<6`. The last inequality follows from `V_{12}<290<315<e^6`; the exact Taylor partial sum through degree eight is

\[
\sum_{j=0}^8\frac{6^j}{j!}=\frac{1709}{5}>315.
\]

The four subtractions after `C_12=15` in (6.15) are then bounded respectively by

\[
\frac{57}{4},\qquad
\frac2{1000},\qquad
\frac{13}{1000},\qquad
\frac{374}{1000}.
\]

Consequently

\[
\boxed{G_{12}(d)>15-14.639=0.361.}
\tag{7.5}
\]

### `N=13`

For `53/100<=d<=27/50`,

\[
\kappa<\frac85,\quad
\nu<\frac{73}{100},\quad
V_{13}<315,\quad
\mu_{13}<\frac{88}{100},
\]

\[
c_0<\frac{509}{500},\qquad
0\le\eta_0<\frac{24}{100}.
\tag{7.6}
\]

The same elementary logarithmic inequalities bound the four subtractions after `C_13=17` by

\[
\frac{162}{10},\qquad
\frac2{1000},\qquad
\frac{14}{1000},\qquad
\frac{370}{1000}.
\]

Therefore

\[
\boxed{G_{13}(d)>17-16.586=0.414.}
\tag{7.7}
\]

Because the convergence in (6.14) is uniform, (7.5)--(7.7) imply:

### Theorem R15-F0111-SMOOTH-BOUNDARY

There exists `s_0>0` such that **no** scalar-feasible `N=12` or `N=13` contact can satisfy the floor-free necessary condition (5.4) for `0<s<s_0`.

Equivalently, the smooth complement-face gate itself repels both remaining branches from the compactified boundary `z=1`, without using the earlier one-heavy limiting-flow contradiction.

This theorem is qualitative in `s_0`; I am not claiming an effective value in this run.

## 8. Exact finite self-check

After the idea note was committed, I wrote

`artifacts/R15/f0111_smooth_k_secant_check_s104a.py`

and executed the same exact `fractions.Fraction` calculation locally. Its archived output is

`artifacts/R15/f0111_smooth_k_secant_check_s104a.out`.

The checker verifies every rational endpoint roof used in Section 7, the Taylor certificate `1709/5>315`, and the final aggregate inequalities. It ends

`ALL_EXACT_CHECKS_PASS`.

Checker commit: `2f68f3912b801338cb54b56ac1e4c444c23e58b4`.  
Archived output commit: `d977f7f23b6e4df08412d4e74ead39a884adc56f`.

This is a **self-check**, not an independent audit.

## 9. What changed and what remains

The native I0076 research target did not move and remains retired at its source-faithful six-run handoff.

The retained F0111 screen did move structurally:

1. the exact K-block floor decomposition is no longer needed for a necessary condition;
2. the surviving gate is one smooth two-variable function per `N`;
3. this smooth gate is uniformly positive to first order on the entire `s=0` feasible boundary, so any possible survivor lies in a compact strip separated from `s=0`;
4. the only remaining task for this particular `n=30`, full-support, two-level first-bifurcation mechanism is to prove `Gamma_N^sec>0` on that interior compact strip, or find an exact scalar point where it fails.

A useful next route is now clear: differentiate `Gamma_N^sec` in `delta` on the scalar-feasible strip. Exploratory scratch calculations suggest the minimum may lie on the boundary `U_K=N`, but that observation is **not proved, not archived as evidence, and not counted**. If one can prove the monotonicity, the remaining two-dimensional sign problem collapses to one algebraic boundary curve and the K-sec term vanishes there.

## 10. Scheduler/model-control status

The current exposed scheduling/update surface still provides prompt/title, schedule/timing, enabled state, and timing mode, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution control. Thus GPT-6/maximum remains prompt-only; this run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED.

`RESULTS.md` and `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` preserve the historical P26 response `You cannot modify this task.` They also record that another authorized context later succeeded on P26. The compliant remedy is an owning/authorized workspace/account/API/admin scheduler surface or platform support, not a duplicate task or a permission bypass. This run made no scheduler changes.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), arXiv:1302.6958, Problem 7.2; intake I0076"
  target: "decide whether FBM + BBM + source-exact independent centered halves at an arbitrary random time imply 2BM"
  native_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "FROZEN_AT_SIX_RUN_HANDOFF"
  tried_moves: [6, 11, 24]
  retained_screen: "F0111 / Talagrand discrete k=2 first-bifurcation screen; PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_screen_delta: "removed K-floor subcells via secant; proved smooth gate uniformly positive to first order on full s=0 feasible boundary for N=12,13"
  remaining_obligation: "native I0076 has no surviving frozen candidate; retained screen still needs interior compact-strip sign proof for Gamma_sec or an exact failing scalar point"
  evidence:
    - "artifacts/R15/f0111_smooth_k_secant_idea_s104a.md @ 3e1bc9ddb84bb5047f4a278bd11662aa9fd20be5"
    - "artifacts/R15/f0111_smooth_k_secant_check_s104a.py @ 2f68f3912b801338cb54b56ac1e4c444c23e58b4"
    - "artifacts/R15/f0111_smooth_k_secant_check_s104a.out @ d977f7f23b6e4df08412d4e74ead39a884adc56f"
  audits: []
  novelty: "UNVERIFIED"
```
