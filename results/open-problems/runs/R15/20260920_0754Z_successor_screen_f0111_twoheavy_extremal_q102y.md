Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the last F0111 `n=30`, `N=12,13` arbitrary-heterogeneity contact-distribution problem is reduced exactly to a capped two-heavy `J` profile plus an explicit capped-convex `K` extreme point; the residual `K-K` energy roof also sharpens to `y(N-1)/2 * log^2(U_K/L_K)`. Methods #13 FIND WHAT ONLY INCREASES, #24 FIND THE EXTREMAL OBJECT, #30 DO ONE SCALE/DIRECTION AT A TIME.**

# R15 retained screen — capped two-heavy extremal reduction for the last two F0111 cells

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand's discrete Convexity Conjecture, and does not satisfy the two-other-track audit rule.

The preceding complete R15 report used moves `#3/#11/#25`, so the present triple is nonconsecutive. The route was written before validation in

`artifacts/R15/f0111_coupled_twoheavy_transfer_idea_q102y.md`

at commit

`b421bfa049cbb16b35736bde90034cc091748d94`.

Only after that note was committed did I add the small exact symbolic self-check described in Section 9.

## 1. Repository continuity, source fidelity, ownership, and exclusions

Before new mathematics I reread or source-recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- controlling native handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- newest own report `runs/R15/20260920_0656Z_successor_screen_f0111_complement_energy_p101x.md`;
- neighboring Burdzy--Scheutzow Problem 7.8 terminal handoff `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- current queue/admission state and exact identifier/source searches for `I0076`.

`QUEUE.md` still records **zero newly certified free READY entries**. A listed/PENDING item is not dispatchable merely because it appears in the reserve. I therefore did not steal another worker's source, promote a PENDING row, or edit a shared root.

### Exact native source, rechecked from the primary PDF

Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM: there are random times `S_n -> -infinity` a.s. such that every complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there is one random time `S` at which the complete centered future and complete centered past are independent standard Brownian motions.

Problem 7.2 asks whether **FBM + BBM + existence of an arbitrary random time `T` at which the two complete centered half-processes are independent** implies 2BM. The source does **not** assume `T` is a stopping time and does **not** separately assume either half at `T` is Brownian. Problem 7.5 is distinct and remains excluded.

The nearby Proposition 6.2 gives a different stronger-seam obstruction for its Section-6 construction: it rules out independence together with a Brownian forward half. It does not establish or exclude bare Problem-7.2 seam independence by itself.

### Native candidate / metric state

The six-run handoff remains binding.

- The source Theorem-6.1 candidate has FBM, BBM, and failure of 2BM, but no source-valid independent random seam.
- The later Brownian-prefix/BES candidate has FBM, BBM, and an exact independent seam, but the R15 Palm analysis proves it is actually 2BM.

Therefore there is **no surviving frozen counterexample candidate** on which the user's four obligations can honestly be scored. Historical `2/4` and `3/4` values belong to eliminated candidates or to the retired positive-route metric; they are not a present frozen-candidate score.

Native source status remains **OPEN / PARTIAL / RETIRED-HANDOFF**. The six unchanged runs that triggered the mandatory rotation stay frozen at the handoff and are not incremented by this retained screen.

### Fresh dated literature pass, 2026-09-20

Fresh exact-title / Problem-7.2 searches recovered the original paper and current author/university material but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. That is bounded negative evidence only, not a worldwide openness certificate.

For the retained screen, Ascoli--He--Park--Talagrand, arXiv:2608.11183 (2026-08-11), still presents the broader **discrete** Convexity Conjecture as open while reformulating it using `k`-thresholds and proving substantial classes. Park, arXiv:2609.14681 (2026-09-13), proves a dimension-free comparison whose abstract describes the consequence as a bound *toward* the conjecture. I found no accessible source matching the specific two-heavy/complement-energy reduction below. Novelty remains **UNVERIFIED**.

## 2. Carried F0111 state

The retained hazard is

\[
F(t)=\sum_{i=1}^{30}t_i-\log\!\left(\sum_{i=1}^{30}e^{t_i}-29\right).
\tag{2.1}
\]

For the full-support, two-level Hessian-null first-bifurcation screen on the surviving scalar branch `z=1+s>1`, the preceding exact reductions leave only

\[
N:=|K|\in\{12,13\},\qquad M:=|J|=30-N.
\tag{2.2}
\]

Write

\[
a=1+\delta,\qquad b=1-\delta,
\]

and retain the exact scalar null quantities `x=sum_J r_i`, `y=sum_K r_j`, `A_J`, `A_K`, `L_K=A_Ky`, `U_K=-29y/k`, and

\[
S:=S(q)=-\frac{29}{k}.
\tag{2.3}
\]

At contact define

\[
u_i=e^{q_i}=Sr_i\quad(i\in J),\qquad
v_j=e^{q_j}=Sr_j\quad(j\in K).
\tag{2.4}
\]

Since the contact is full-support interior,

\[
u_i>1,\qquad v_j>1.
\tag{2.5}
\]

The carried exact cell bounds include

\[
N=12:\quad r_*<1-15s,
\qquad
N=13:\quad r_*<1-17s,
\tag{2.6}
\]

as well as `x<41/40` and `s<3/200` on both remaining cells. The checker from the preceding run proves that at the two heavy thresholds `r_0=1-C_Ns` the residual diagonal

\[
r_0(1-A_Jr_0)>0,
\]

so `r_0<1/A_J`. Thus throughout these cells the carried heavy cap is stricter than the residual coordinate cap:

\[
0<r_i<1-C_Ns,\qquad C_{12}=15,\ C_{13}=17.
\tag{2.7}
\]

The immediately preceding report also established the exact complement-face inequality: for every `t>0`,

\[
E_{KK}+(t-1)E_{JJ}
\ge
W-D_J+\frac{F(tq_J)}t.
\tag{2.8}
\]

The remaining difficulty was the high-dimensional optimization over heterogeneous `J` and `K` contact masses. This run removes that high dimension.

## 3. First cancellation: the complement inequality has an exact face form

Put

\[
E_{JJ}=\sum_{i<j\in J}B_{ij}q_iq_j,\qquad
E_{KK}=\sum_{i<j\in K}B_{ij}q_iq_j.
\tag{3.1}
\]

Exact contact gives

\[
W=D-F(q)=\log S-\sum_{\ell=1}^{30}r_\ell q_\ell.
\tag{3.2}
\]

Therefore

\[
W-D_J
=\log S-\sum_{j\in K}r_jq_j-\sum_{i\in J}q_i.
\tag{3.3}
\]

On the `J`-face,

\[
F(tq_J)
=t\sum_{i\in J}q_i
-\log\!\left(\sum_{i\in J}u_i^t-(M-1)\right),
\tag{3.4}
\]

because the `N` zero coordinates contribute `N` to the exponential sum and `N-29=-(M-1)`.

Substituting (3.3)--(3.4) into (2.8) cancels every linear `J` term exactly:

### Lemma R15-F0111-FACE2

For every `t>1`, every surviving contact satisfies

\[
\boxed{
E_{KK}+(t-1)E_{JJ}
\ge
\log S-\sum_{j\in K}r_jq_j
-\frac1t\log\!\left(\sum_{i\in J}u_i^t-(M-1)\right).
}
\tag{3.5}
\]

This is the form used below.

## 4. Method #25 carried forward: exact aggregate pair capacities

The residual projective Gram representation has vectors `w_i` with

\[
B_{ij}=\langle w_i,w_j\rangle+A_Jr_ir_j\quad(i,j\in J),
\]

\[
\|w_i\|^2=r_i(1-A_Jr_i),
\]

and

\[
a\sum_{i\in J}w_i=b\sum_{j\in K}w_j.
\tag{4.1}
\]

Let

\[
T=\left\|\sum_{j\in K}w_j\right\|^2,
\qquad
T\le T_{\rm cap}:=y(N-L_K).
\tag{4.2}
\]

Summing the `J-J` Gram identity over unordered pairs gives

\[
\begin{aligned}
U_J:=\sum_{i<j\in J}B_{ij}
&=\frac12\left(\left\|\sum_{i\in J}w_i\right\|^2-\sum_{i\in J}\|w_i\|^2\right)
+\frac{A_J}{2}\left(x^2-\sum_{i\in J}r_i^2\right)\\
&=\frac12\left[\left(\frac ba\right)^2T-x+A_Jx^2\right].
\end{aligned}
\tag{4.3}
\]

Hence

\[
\boxed{
U_J\le U_{\max}:=\frac12\left[\left(\frac ba\right)^2T_{\rm cap}-x+A_Jx^2\right].
}
\tag{4.4}
\]

Since every `B_ij>=0`, if `q_(1)>=q_(2)` are the two largest `J` coordinates,

\[
\boxed{E_{JJ}\le U_{\max}q_{(1)}q_{(2)}.}
\tag{4.5}
\]

The same calculation on `K` gives

\[
V:=\sum_{i<j\in K}B_{ij}
=\frac12(T-y+A_Ky^2).
\tag{4.6}
\]

Using `T<=y(N-L_K)` and `L_K=A_Ky`, the upper bound collapses exactly:

\[
\boxed{V\le V_{\max}=\frac{y(N-1)}2.}
\tag{4.7}
\]

This exact simplification is new in the retained reduction.

Moreover the residual coordinate cap `r_j<=1/A_K` yields

\[
v_j=Sr_j\le\frac{S}{A_K}
=\frac{Sy}{A_Ky}
=\frac{U_K}{L_K}=:c_K.
\tag{4.8}
\]

Therefore

\[
\boxed{
E_{KK}\le \frac{y(N-1)}2\,\log^2\!\left(\frac{U_K}{L_K}\right).
}
\tag{4.9}
\]

This replaces the preceding report's total-excess coordinate roof by the sharper residual-coordinate roof.

## 5. Method #13 — the mass-transfer monovariant on J

From (2.7), put

\[
c_J:=S(1-C_Ns).
\tag{5.1}
\]

Then

\[
1<u_i<c_J,\qquad \sum_{i\in J}u_i=Sx.
\tag{5.2}
\]

The carried exact bounds imply that **two capped coordinates always have enough capacity** for the whole `J` mass. Indeed

\[
2(1-C_Ns)
>2\left(1-17\cdot\frac3{200}\right)
=\frac{149}{100}
>\frac{41}{40}>x.
\tag{5.3}
\]

Hence

\[
Sx<2c_J.
\tag{5.4}
\]

Fix `t>1` and define, for a sorted vector `u_(1)>=u_(2)>=...>=u_(M)`,

\[
\mathcal H_t(u)
:=\frac1t\log\!\left(\sum_i u_i^t-(M-1)\right)
+(t-1)U_{\max}\log u_{(1)}\log u_{(2)}.
\tag{5.5}
\]

### Theorem R15-F0111-TWOHEAVY — exact extremal reduction

Among all `u` satisfying (5.2), the maximum of `\mathcal H_t` is attained in the closure by a vector with **at most two coordinates greater than 1**.

Equivalently, put

\[
T_2:=Sx-(M-2).
\tag{5.6}
\]

Then

\[
\boxed{
\sup \mathcal H_t
=
\max_{u\in I}
\left\{
\frac1t\log\bigl(u^t+(T_2-u)^t-1\bigr)
+(t-1)U_{\max}\log u\log(T_2-u)
\right\},
}
\tag{5.7}
\]

where

\[
I=
\left[
\max\{1,T_2-c_J\},
\min\{c_J,T_2-1\}
\right].
\tag{5.8}
\]

### Proof

Take any feasible vector with a third coordinate `u_(3)>1`.

If `u_(1)<c_J`, transfer

\[
\varepsilon\le\min\{c_J-u_{(1)},u_{(3)}-1\}
\]

from `u_(3)` to `u_(1)`. Because `r\mapsto r^t` is strictly convex for `t>1` and `u_(1)>=u_(3)`, the power sum in (5.5) does not decrease. The second term also does not decrease: `u_(2)` is unchanged and `log u_(1)` increases.

If `u_(1)=c_J` but `u_(2)<c_J`, perform the same transfer from `u_(3)` to `u_(2)`. Again convexity increases the power sum, and now the product `log u_(1)log u_(2)` increases.

The remaining possibility `u_(1)=u_(2)=c_J` with `u_(3)>1` is impossible because it would give

\[
\sum_i u_i>2c_J,
\]

contradicting (5.4).

Push each transfer until either the donor reaches `1` or the receiver reaches `c_J`. Repeating finitely many times leaves at most two coordinates above `1`, never decreases `\mathcal H_t`, and preserves the total sum. Those two coordinates must add to `T_2`, giving exactly (5.7)--(5.8). QED.

This is the main structural gain of the run. The arbitrary `17`- or `18`-dimensional `J` mass simplex has become **one scalar split variable**.

## 6. Method #24 — K has an explicit capped-convex extremizer

The `K` variables satisfy

\[
1<v_j\le c_K:=\frac{U_K}{L_K},
\qquad
\sum_{j\in K}v_j=U_K.
\tag{6.1}
\]

Also

\[
\sum_{j\in K}r_jq_j
=\frac1S\sum_{j\in K}v_j\log v_j.
\tag{6.2}
\]

Since `f(v)=v log v` is strictly convex on `[1,infinity)`, its sum under a box constraint and fixed total is maximized by concentrating mass as much as the cap allows.

Write

\[
\eta:=U_K-N,\qquad h:=c_K-1,
\]

\[
m:=\left\lfloor\frac\eta h\right\rfloor,\qquad
\rho:=\eta-mh\in[0,h).
\tag{6.3}
\]

Then the extremal vector has `m` coordinates equal to `c_K`, one coordinate equal to `1+rho` if `m<N`, and all remaining coordinates equal to `1`. Hence

### Lemma R15-F0111-KEXT

\[
\boxed{
\sum_{j\in K}r_jq_j
\le
K_{\max}:=
\frac1S\left[
m c_K\log c_K+(1+\rho)\log(1+\rho)
\right],
}
\tag{6.4}
\]

with the second term interpreted as zero if `m=N`.

A direct mass-transfer proof is equivalent: whenever `1<v_i<=v_j<c_K`, moving a small amount from `v_i` to `v_j` increases `f(v_i)+f(v_j)` because `f'` is increasing. Iteration gives the stated extreme point.

Thus the `K` distribution has been removed completely.

## 7. Method #30 — the final necessary condition is scalar

Define

\[
H_N(\delta,s;t)
:=
\max_{u\in I}
\left\{
\frac1t\log\bigl(u^t+(T_2-u)^t-1\bigr)
+(t-1)U_{\max}\log u\log(T_2-u)
\right\}.
\tag{7.1}
\]

and

\[
\overline E_K
:=\frac{y(N-1)}2\log^2\!\left(\frac{U_K}{L_K}\right).
\tag{7.2}
\]

From (3.5), (4.5), (4.9), (5.7), and (6.4), every surviving contact must satisfy, for **every** `t>1`,

\[
\boxed{
\mathcal G_N(\delta,s;t)
:=
\log S-K_{\max}-H_N(\delta,s;t)-\overline E_K
\le0.
}
\tag{7.3}
\]

Consequently, a single `t>1` with

\[
\mathcal G_N(\delta,s;t)>0
\tag{7.4}
\]

eliminates that scalar point, with no coefficient matrix and no high-dimensional contact distribution left to optimize.

The remaining `N=12,13` arbitrary-heterogeneity problem for this first-bifurcation mechanism is therefore reduced to:

- the two scalar null parameters `(delta,s)` in their already-certified narrow cells;
- one explicit one-variable maximum in (7.1);
- one freely chosen face-ray parameter `t>1`.

This is much smaller than the object at the start of the run.

## 8. Route-finding observation, deliberately not counted as proof

After deriving the reduction I used floating-point exploration privately only to decide whether (7.3) is worth pursuing. It strongly suggests that choosing `t` only slightly above `1`, and allowing it to approach `1` near the scalar-cell tips, makes (7.4) positive across broad samples of both cells.

I do **not** count those samples as verification, do not archive them as a certificate, and do not claim either `N=12` or `N=13` eliminated. The next proof task is to replace this route-finding evidence by an exact interval/Bernstein argument or by a monotonicity theorem for the one-variable maximand in (7.1).

A particularly useful next subproblem is to prove when the maximum in (7.1) occurs at the cap endpoint. If that succeeds, even the split variable disappears and the full screen becomes a two-scalar inequality plus the ray choice.

## 9. Exact self-check after the idea

Only after the idea note was committed did I run a small exact symbolic checker:

`artifacts/R15/f0111_twoheavy_symbolic_checker_q102y.py`

It verifies exactly:

1. the `K-K` capacity collapse
   \[
   V_{\max}=y(N-1)/2;
   \]
2. the summed `J-J` Gram identity
   \[
   U_J=\frac12\left[(b/a)^2T-x+A_Jx^2\right];
   \]
3. the rational two-cap margin
   \[
   \frac{149}{100}-\frac{41}{40}=\frac{93}{200}>0.
   \]

The archived output ends

`ALL_EXACT_SYMBOLIC_CHECKS_PASS`.

This is a **self-check**, not an independent audit, and it does not certify the transcendental scalar inequality (7.3) over either full cell.

## 10. What remains

The native I0076 source obligation is unchanged: construct a new frozen source-valid counterexample candidate satisfying FBM, BBM, and bare random-time half-process independence while failing 2BM, or prove the full implication without adding stopping-time/Brownian-seam hypotheses. That target remains operationally retired at its mandatory handoff because no native metric movement occurred in six consecutive runs.

For the retained F0111 screen, the remaining work inside this mechanism is now sharply finite-dimensional:

1. prove a cap-endpoint or other exact maximizer theorem for (7.1), or exact-certify its one-variable maximum by interval arithmetic;
2. prove `G_N>0` somewhere in `t>1` for every scalar point in the `N=12` and `N=13` cells;
3. only then declare this particular full-support two-level Hessian-null `n=30` mechanism eliminated.

Even success on all three does **not** solve the full discrete Convexity Conjecture: non-two-level null directions, directions with zero coordinates, higher dimensions, and the separate second-contact mechanism remain.

## 11. Model / scheduler control

Actual report model: **GPT-5.6 Sol**. Actual reasoning effort is **UNVERIFIED**; I do not claim GPT-6 maximum.

The currently exposed automation/task update surface still has prompt/title, schedule or relative-start/timing mode, and enabled-state fields, but **no binding model-family selector, no reasoning-effort selector, no authenticated per-run applied-model/effort receipt, and no guaranteed hour-long-execution control**. Thus `GPT-6 / maximum` remains prompt text rather than an enforceable field on this surface.

`operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` preserves the historical P26 response `You cannot modify this task` from one authorization context. Current `RESULTS.md` separately records that a later authorized P/C context successfully updated P26. The lawful workaround for a task that still refuses modification is therefore its owning/authorized workspace/account/API/admin context or platform support, not task duplication or permission bypass.

No scheduler mutation was attempted here because the operating contract explicitly forbids scheduler changes by this worker.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  task: R15
  lane: CLOSABLE_OUTSIDE
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2, I0076"
  source_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  metric_before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
  metric_after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
  metric_movement: NO_MOVEMENT
  source_status: OPEN_PARTIAL_RETIRED_HANDOFF
  native_unchanged_count: "6 at mandatory handoff; frozen after retirement"
  tried_moves: [13, 24, 30]
  remaining_source_obligation: "construct a new source-valid frozen counterexample candidate satisfying FBM, BBM and bare random-time half-process independence while failing 2BM, or prove the full source implication without adding stopping-time/Brownian-seam hypotheses"
  source_candidate: NONE_SURVIVING
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260920_0656Z_successor_screen_f0111_complement_energy_p101x.md"
    - "artifacts/R15/f0111_coupled_twoheavy_transfer_idea_q102y.md @ b421bfa049cbb16b35736bde90034cc091748d94"
    - "artifacts/R15/f0111_twoheavy_symbolic_checker_q102y.py @ 563d1b88dce1d18e453b64f69584cdb591ed3caa"
    - "artifacts/R15/f0111_twoheavy_symbolic_checker_q102y.out @ 8ac33a0125fc6961b808d71a6abd4c186f0efa0d"
  retained_screen:
    source: "Talagrand F0111 / discrete Convexity Conjecture, k=2 screen"
    admission: PENDING_SELF_CHECK_ONLY_NOT_CLAIMED
    before: "last n=30 two-level cells N={12,13}; coefficient matrix eliminated, but J/K contact distributions remained high-dimensional"
    after: "same N={12,13}; K distribution has an explicit capped-convex extremizer; J worst-case coupled face/energy profile reduces exactly to two elevated coordinates and one split variable; sharper exact K-K roof"
    new_results:
      - R15-F0111-FACE2
      - R15-F0111-TWOHEAVY
      - R15-F0111-KEXT
      - "sharp K-K roof E_KK <= y(N-1)/2 log^2(U_K/L_K)"
      - "scalar necessary gate G_N(delta,s;t)<=0"
  independent_audits: []
  closure: false
```

No shared root was edited. No email, Drive, public posting, purchase, permission change, or scheduler change was attempted.
