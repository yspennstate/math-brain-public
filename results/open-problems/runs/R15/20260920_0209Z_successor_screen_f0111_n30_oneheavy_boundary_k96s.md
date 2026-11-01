Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: in the F0111 `k=2` first-bifurcation screen, no heterogeneous full-support two-level exact quadratic contact can approach the sharp `n=30`, `z downarrow 1` boundary; the previous one-heavy limiting escape is now impossible in dimension 30. Methods #8 DISCRETIZE, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT.**

# R15 retained screen — the one-heavy sharp boundary is impossible in dimension 30

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about Talagrand/F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand Problem 10.9, and does not satisfy the independent-audit closure rule.

Historical R15 work has already used every one of the thirty Section-B move numbers at least once, so the literal request for three globally never-used numbers is no longer satisfiable. The present triple is different from the immediately preceding #15/#18/#29 and is applied to a genuinely new object: the finite one-heavy limiting flow/PSD system.

## 1. Continuity, exact source and current allocation

Before new mathematics I reread/recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the controlling I0076 six-run handoff;
- the newest own report `runs/R15/20260920_0106Z_successor_screen_f0111_heterogeneous_oneheavy_j95r.md`;
- the newest same-source neighboring Burdzy report, R07's Problem 7.8 terminal handoff `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- targeted intake/claim searches for I0076/I0077 and current ownership.

The current root queue still records zero newly certified free READY candidates. I0077/Problem 7.8 is separately reserved/owned by R07 and is itself now at a terminal handoff. I did not create or overwrite a successor claim, steal another worker's source, or promote a PENDING row to READY.

### Exact Burdzy--Scheutzow source

The primary PDF was rechecked directly on 2026-09-20: K. Burdzy and M. Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM means there are random origins tending to `-infinity` from which the complete centered **future** is standard Brownian motion;
- BBM means the time-reversed process is FBM;
- 2BM means there is one random time `S` such that the complete centered future and complete centered past at `S` are **independent standard Brownian motions**.

Problem 7.2 asks: if `X` is FBM and BBM and there is an arbitrary random time `T` at which the two complete centered half-processes are independent, must `X` be 2BM? The source does **not** assume `T` is a stopping time and does **not** separately assume either half at `T` is Brownian. Problem 7.5 is distinct and remains excluded.

Fresh dated searches on 2026-09-20 used the exact title, arXiv number, `Problem 7.2`, and independent-past/future terms. They recovered the original source/publication and later references but no accessible later primary paper explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide-openness certificate.

The native I0076 handoff therefore remains controlling. The source-Theorem-6.1 candidate has FBM, BBM and non-2BM but fails the required independent random seam. The later Brownian-prefix/BES route has an exact independent seam but was proved actually to be 2BM. There is no surviving frozen counterexample candidate on which a fresh `0/4`, `2/4`, `3/4`, or `4/4` score would be honest. The historical `2/4` is only the retired positive-route handoff value.

## 2. Current F0111 literature scope

For the retained screen I also rechecked current primary literature. Ascoli--He--Park--Talagrand, arXiv:2608.11183 (11 Aug 2026), reformulates the discrete Convexity Conjecture through `k`-thresholds and proves substantial classes. Park, arXiv:2609.14681 (13 Sep 2026), proves a dimension-free comparison yielding a bound explicitly described as progress **toward** the conjecture. These sources do not authorize calling the present `k=2` first-bifurcation analysis a full solution. I found no accessible source matching the dimension-30 boundary theorem below, but novelty remains **UNVERIFIED**.

## 3. Carried one-heavy boundary system

For the cardinality-two hazard write

\[
F(q)=\sum_i q_i-\log S(q),\qquad
S(q)=\sum_i e^{q_i}-(n-1).
\tag{3.1}
\]

Let

\[
P(q)=\sum_i A_iq_i+\sum_{i<j}B_{ij}q_iq_j,
\qquad A_i,B_{ij}\ge0,
\tag{3.2}
\]

be a global quadratic majorant exact at an interior point `q>0`. Put

\[
G=P-F,\qquad H=D^2G(q)\succeq0,
\qquad r_i=\frac{e^{q_i}}{S(q)}.
\tag{3.3}
\]

Suppose `H` has a full-support two-level mixed null direction

\[
h=a\mathbf1_J-b\mathbf1_K,
\qquad a=1+\delta,\quad b=1-\delta,
\quad 0<\delta<1.
\tag{3.4}
\]

On the only dimension-30 branch allowed by the earlier scalar barrier, write

\[
z=1+\varepsilon,\qquad \varepsilon\downarrow0.
\tag{3.5}
\]

The exact cubic-null formulas give, with `D=delta+3`,

\[
\kappa=\frac4{abD},\qquad
\nu=\frac{a^2}{2bD},\qquad
\xi=\frac{\delta^2+4\delta+7}{2aD},
\tag{3.6}
\]

and

\[
k=-\kappa\varepsilon+O(\varepsilon^2),\qquad
x=1+\xi\varepsilon+O(\varepsilon^2),\qquad
y=\nu\varepsilon+O(\varepsilon^2).
\tag{3.7}
\]

The previous report proved the heterogeneous one-heavy theorem. Thus after passing to a subsequence there is a distinguished `* in J` such that

\[
r_*=1-c\varepsilon+o(\varepsilon),
\tag{3.8}
\]

\[
r_i=\varepsilon u_i+o(\varepsilon)\quad(i\in J\setminus\{*\}),
\qquad
r_j=\varepsilon v_j+o(\varepsilon)\quad(j\in K),
\tag{3.9}
\]

with

\[
\sum_{j\in K}v_j=\nu,
\qquad
\sum_{i\in J\setminus\{*\}}u_i=c+\xi.
\tag{3.10}
\]

Full support `q_i>0` gives the limiting lower bounds

\[
u_i,v_j\ge \frac{\kappa}{n-1}
\tag{3.11}
\]

(with equality allowed only in the limit).

## 4. Method #11 — dualize the projective condition to a residual Gram system

The exact projective theorem from the preceding R15 chain says that the fourth-order condition is equivalent to a rank-one PSD downdate. On the `z=1+epsilon` boundary its scaled limit has a particularly simple form.

Set

\[
\rho=\frac3D,\qquad
\gamma=\frac{12D}{a^2},\qquad
\theta=\frac6a.
\tag{4.1}
\]

After dividing the residual PSD matrix by `epsilon` there are Gram vectors

\[
w_0,\quad w_i\ (i\in J\setminus\{*\}),\quad y_j\ (j\in K)
\tag{4.2}
\]

such that

\[
\|w_0\|^2=c-\rho,
\qquad
\|w_i\|^2=u_i,
\qquad
\|y_j\|^2=v_j(1-\gamma v_j),
\tag{4.3}
\]

and the residual null relation is

\[
a\left(w_0+\sum_iw_i\right)=b\sum_j y_j.
\tag{4.4}
\]

In particular

\[
0\le v_j\le\frac1\gamma.
\tag{4.5}
\]

Write the leading scaled pair coefficients as

\[
p_i=b_{*i},\quad s_{i\ell}=b_{i\ell},\quad
t_{ij}=b_{ij},\quad q_j=b_{*j}.
\tag{4.6}
\]

The Gram decomposition gives exactly

\[
p_i=u_i+\langle w_0,w_i\rangle,
\tag{4.7}
\]

\[
s_{i\ell}=\langle w_i,w_\ell\rangle,
\qquad
t_{ij}=\langle w_i,y_j\rangle,
\tag{4.8}
\]

\[
q_j=(1+\theta)v_j+\langle w_0,y_j\rangle.
\tag{4.9}
\]

All of these are nonnegative because the original quadratic coefficients are nonnegative.

The limiting null-flow equations from the previous report are

\[
a\sum_i p_i-b\sum_jq_j=1,
\tag{4.10}
\]

and, after summing the light-`J` equations,

\[
b\sum_{i,j}t_{ij}
=a\left(\sum_i p_i+2\sum_{i<\ell}s_{i\ell}\right).
\tag{4.11}
\]

Put

\[
P_*=\sum_i p_i,\quad Q_*=\sum_jq_j,
\quad T_*=\sum_{i,j}t_{ij}.
\tag{4.12}
\]

Then nonnegativity gives

\[
P_*\ge\frac1a,
\qquad
T_*\ge\frac1b.
\tag{4.13}
\]

This is the dual quantity that will collide with the residual Gram capacity.

## 5. Method #24 — extremize the residual cross-flow capacity

Let

\[
Y=\sum_{j\in K}y_j,
\qquad
W=\sum_{i\in J\setminus\{*\}}w_i.
\tag{5.1}
\]

From (4.4),

\[
W=\frac baY-w_0,
\tag{5.2}
\]

while (4.8) gives

\[
T_*=\langle W,Y\rangle.
\tag{5.3}
\]

Let `N=|K|`. Since `sum v_j=nu`, Cauchy and (4.3) yield

\[
\begin{aligned}
\|Y\|^2
&\le N\sum_j\|y_j\|^2\\
&=N\left(\nu-\gamma\sum_jv_j^2\right)\\
&\le N\left(\nu-\gamma\frac{\nu^2}{N}\right)
=\nu(N-L),
\end{aligned}
\tag{5.4}
\]

where

\[
L:=\gamma\nu=\frac6b.
\tag{5.5}
\]

Put

\[
E^2:=\nu(N-L).
\tag{5.6}
\]

If `E=0`, then `Y=0` and (5.3) contradicts `T_*>=1/b`. Hence every survivor has `E>0`.

Using (5.2), (5.3), (4.13), and `||w_0||=sqrt(c-rho)`,

\[
\frac1b
\le T_*
\le \left(\sqrt{c-\rho}+\frac baE\right)E.
\tag{5.7}
\]

Therefore

\[
\boxed{
 c\ge C_N(\delta)
 :=\rho+
 \frac{\left(\frac1b-\frac baE^2\right)^2}{E^2}.
}
\tag{5.8}
\]

This is the first half of the contradiction.

## 6. Method #8 — dimension 30 makes the remaining scalar problem finite

The residual coordinate cap (4.5) and `sum v_j=nu` imply

\[
N\ge L=\frac6b.
\tag{6.1}
\]

Full-support positivity (3.11) gives

\[
N\frac\kappa{29}\le\nu,
\qquad\text{hence}\qquad
N\le U:=\frac{29a^3}{8}.
\tag{6.2}
\]

Thus a dimension-30 boundary survivor must satisfy

\[
\frac6{1-\delta}\le N\le\frac{29(1+\delta)^3}{8}.
\tag{6.3}
\]

In particular `L<=U` gives

\[
29(1-\delta)(1+\delta)^3\ge48.
\tag{6.4}
\]

The function `(1-delta)(1+delta)^3` increases up to `delta=1/2` and decreases afterwards. At `delta=2/5` and `3/5`, the left side of (6.4) minus 48 equals respectively

\[
-\frac{159}{625},\qquad -\frac{304}{625}.
\tag{6.5}
\]

Therefore

\[
\frac25<\delta<\frac35.
\tag{6.6}
\]

Then `L>10` and `U<1856/125<15`, so

\[
\boxed{N\in\{11,12,13,14\}.}
\tag{6.7}
\]

The continuous part of the lower bound is now four exact one-variable rational inequalities.

### Lemma 6.1: `C_N(delta)>26` throughout every feasible interval

Differentiating (5.8) gives

\[
C_N'(d)=
-\frac{2P_N(d)}{(1+d)^3(d+3)^2(Nd-N+6)^2},
\tag{6.8}
\]

where

\[
P_N(d)=\sum_{r=0}^5p_r(N)d^r
\tag{6.9}
\]

with coefficient vector, in increasing powers of `d`,

\[
\begin{aligned}
(&N^3-21N^2+162N-594,\\
 &N^3-21N^2+120N-774,\\
 &-2N^3+14N^2-52N-318,\\
 &-2N^3+22N^2-56N-42,\\
 &N^3+7N^2-14N,\\
 &N^3-N^2).
\end{aligned}
\tag{6.10}
\]

Put `d=(2+t)/5`, `0<=t<=1`, and express `P_N` in the degree-five Bernstein basis. The exact Bernstein coefficients are:

| N | beta_0 | beta_1 | beta_2 | beta_3 | beta_4 | beta_5 |
|---|---:|---:|---:|---:|---:|---:|
| 11 | `-351742/625` | `-1982862/3125` | `-2206141/3125` | `-2417256/3125` | `-2600472/3125` | `-109376/125` |
| 12 | `-1754022/3125` | `-2023572/3125` | `-2294439/3125` | `-510504/625` | `-2777976/3125` | `-2943648/3125` |
| 13 | `-1686964/3125` | `-402378/625` | `-2341681/3125` | `-2659048/3125` | `-2939448/3125` | `-3149056/3125` |
| 14 | `-1539014/3125` | `-1930176/3125` | `-2331319/3125` | `-2721576/3125` | `-3071064/3125` | `-3338336/3125` |

Every Bernstein basis function is nonnegative on `[0,1]`, so `P_N<0` on `[2/5,3/5]` and hence

\[
C_N'(d)>0.
\tag{6.11}
\]

For each `N`, the lower feasible endpoint `d_N` is determined by

\[
29(1+d_N)^3=8N.
\tag{6.12}
\]

Choose the following exact rational point `dhat_N<d_N`:

| N | `dhat_N` | `8N-29(1+dhat_N)^3` | `C_N(dhat_N)-26` |
|---|---:|---:|---:|
| 11 | `447/1000` | `137492933/1000000000` | `15778300411333/1198081697418` |
| 12 | `2451/5000` | `3855509321/125000000000` | `85052778256/322944721617` |
| 13 | `53/100` | `134267/1000000` | `177400645/181794294` |
| 14 | `71/125` | `393456/1953125` | `437412109/12850152` |

All entries in the last two columns are positive. Since `C_N` is increasing and every feasible `d` satisfies `d>=d_N`,

\[
\boxed{C_N(d)>26}
\tag{6.13}
\]

for every dimension-30 boundary survivor.

Thus (5.8) forces

\[
\boxed{c>26.}
\tag{6.14}
\]

## 7. Exact value contact gives the opposite inequality

The same residual Gram representation also controls the heavy incident coefficient sums. From (4.7), (4.9), (5.2), and (3.10),

\[
P_*=\xi+\rho+\frac ba\langle w_0,Y\rangle,
\tag{7.1}
\]

\[
Q_*=(1+6/a)\nu+\langle w_0,Y\rangle.
\tag{7.2}
\]

The exact leading value-contact identity derived in the previous report is

\[
c=
\sum_{i\in J\setminus\{*\}}p_i\log(Au_i)
+\sum_{j\in K}q_j\log(Av_j),
\qquad
A:=\frac{29}{\kappa}.
\tag{7.3}
\]

All logarithms here are nonnegative limits of the positive contact coordinates. Since

\[
u_i\le c+\xi,
\qquad
v_j\le\frac1\gamma,
\tag{7.4}
\]

we have

\[
c\le
P_*\log(A(c+\xi))
+Q_*\log(A/\gamma).
\tag{7.5}
\]

Now use only coarse uniform consequences of (6.6)--(6.7):

1. `xi<1` and `rho<1`.
2. The function `b a^3` is maximized at `delta=1/2` with value `27/16`. Hence
   \[
   U-L=\frac{29ba^3-48}{8b}<\frac{75}{256}.
   \tag{7.6}
   \]
3. On `(2/5,3/5)`, `nu<16/17<1`, hence
   \[
   E^2<\frac{75}{256},\qquad E<\frac9{16}.
   \tag{7.7}
   \]
4. Also `b/a<3/7`, so
   \[
   \frac baE<\frac{27}{112}<\frac14.
   \tag{7.8}
   \]
5. Since `N<=14` and `L<=N`, `delta<=4/7`. Direct algebra then gives
   \[
   (1+6/a)\nu<4.
   \tag{7.9}
   \]
6. `A=29abD/4` decreases for `delta>2/5`, and
   \[
   A(2/5)=\frac{10353}{500}<21.
   \tag{7.10}
   \]
7. Finally
   \[
   \frac A\gamma=\frac{29ba^3}{48}
   \le\frac{261}{256}<\frac{51}{50},
   \tag{7.11}
   \]
   so `log(A/gamma)<1/50`.

Since `||Y||<=E` and `||w_0||=sqrt(c-rho)<sqrt(c)`, (7.1)--(7.11) imply the necessary scalar inequality

\[
\boxed{
 c<\Psi(c):=
 \left(2+\frac{\sqrt c}{4}\right)\log(21(c+1))
 +\frac{4+\sqrt c}{50}.
}
\tag{7.12}
\]

But (7.12) is impossible for every `c>=26`. Indeed, for `c>=26`,

\[
\log(21(c+1))<2\sqrt c.
\tag{7.13}
\]

At `c=26`, this follows from `sqrt(26)>5` and

\[
e^7>\sum_{r=0}^{7}\frac{7^r}{r!}
=\frac{47273}{72}>567,
\tag{7.14}
\]

so `log 567<7<2sqrt(26)`. The difference in (7.13) then increases because

\[
\frac{d}{dc}\left(2\sqrt c-\log(21(c+1))\right)
=\frac1{\sqrt c}-\frac1{c+1}>0.
\tag{7.15}
\]

Moreover

\[
\Psi(26)
<\left(2+\frac64\right)7+\frac{4+6}{50}
=\frac{247}{10}<26,
\tag{7.16}
\]

and for every `c>=26`, using (7.13) and `sqrt(c)>5`,

\[
\Psi'(c)
<\frac14+\frac2{27}+\frac1{20}+\frac1{500}
=\frac{5077}{13500}<1.
\tag{7.17}
\]

Hence `Psi(c)-c` is strictly decreasing on `[26,infinity)` and is already negative at 26. Thus

\[
\boxed{c<\Psi(c)\ \text{cannot hold when }c\ge26.}
\tag{7.18}
\]

This contradicts (6.14).

## 8. New theorem

### Theorem R15-F0111-N30-BOUNDARY-EXCLUSION

There is no sequence of full-support interior exact nonnegative-coefficient quadratic certificates for the `k=2` F0111 hazard in dimension `n=30` whose contact Hessian has a two-level mixed-sign null direction and whose cubic-null scalar parameter satisfies

\[
z\downarrow1.
\]

The statement allows arbitrary within-block heterogeneity of the contact point and of the quadratic coefficients.

Equivalently, within this full-support two-level Hessian-null first-bifurcation mechanism, if any dimension-30 candidate exists at all then its scalar parameter is separated from the compactified sharp boundary:

\[
z\ge1+\eta
\]

for some positive `eta` (not made effective here).

This strictly strengthens the preceding results:

- the scalar/projective calculation only proved `n>=30` on the `z>1` branch, with the constant `256/9` sharp solely at `z downarrow1, delta->1/2`;
- the block-constant repulsion theorem excluded only symmetric contacts near that boundary;
- the preceding heterogeneous theorem reduced every possible boundary escape to a one-heavy finite flow system;
- the present theorem eliminates that final one-heavy boundary system for **all** admissible `delta` and every possible `K`-block size in dimension 30.

It does **not** rule out a dimension-30 candidate at a scalar point bounded away from `z=1`, does not address `n>=31`, non-two-level null directions, null directions with zero coordinates, the separate second-contact mechanism, or the full Talagrand quantifiers.

## 9. Exact validation, after the idea

The route was written before code in

`artifacts/R15/f0111_n30_oneheavy_boundary_idea_k96s.md`

at commit

`184027608c2ef8d78a6a1a713d7cd76670be65ea`.

Only after the analytic route was fixed did I add the exact `Fraction` checker

`artifacts/R15/f0111_n30_oneheavy_boundary_checker_k96s.py`

and execute/archive

`artifacts/R15/f0111_n30_oneheavy_boundary_checker_k96s.out`.

The checker uses no floating point arithmetic. It verifies:

- every Bernstein coefficient in Lemma 6.1 is strictly negative;
- the four rational lower-endpoint comparisons and the exact positive margins over 26;
- all coarse rational constants in Section 7;
- the Taylor lower bound `e^7>567`;
- the exact `Psi(26)` and derivative margins.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent audit.

## 10. What moved and the next mathematical cursor

### Native I0076

No movement. Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`. There is still no surviving frozen counterexample candidate and no source-level proof of the implication. No deterministic-time independence, stopping-time hypothesis, or Problem 7.5 argument was substituted.

### Retained F0111 screen

Real movement. Before this run the only surviving `z downarrow1` escape in dimension 30 was the finite one-heavy heterogeneous flow/PSD system. That escape is now impossible.

The next useful attack is no longer the compactified boundary itself. There are two genuinely different routes:

1. make the separation `eta>0` effective and combine it with the exact scalar condition `Q_K<29` to see whether the entire dimension-30 `z>1` interval collapses; or
2. leave dimension 30 and derive an `n`-dependent version of the residual-flow/value-contact contradiction for `n>=31`, looking for a strengthened uniform dimension barrier.

A third route, structurally more important for the full problem, is a compression theorem reducing arbitrary mixed-sign null directions to the two-level case. None of these is claimed here.

## 11. Scheduler/model-control status

The exposed task-management interface in this environment still provides prompt/title, schedule/timing, enabled state and ordinary update controls, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution field. Therefore GPT-6/maximum remains a prompt request rather than an enforceable setting here.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in one authorization context. Repository reconciliation later records a successful full P26 update from an authorized P/C context. The compliant workaround is the owning/authorized workspace/account/API/admin context or platform support, not a duplicate task or permission bypass. No scheduler mutation was attempted in this run.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  native_source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2, intake I0076"
  native_metric_name: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "RETIRED_HANDOFF; do not restart or fabricate a fresh streak"
  free_ready_closable_before: 0
  free_ready_closable_after: 0
  retained_screen: "Talagrand F0111 k=2, PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_screen_before: "all z->1+ heterogeneous contacts reduced to a one-heavy finite flow/PSD system"
  retained_screen_after: "dimension n=30 one-heavy boundary system impossible for every admissible delta and N; no full-support two-level exact contact sequence can have z downarrow 1"
  tried_moves:
    - "8 GO THE OTHER WAY AND DISCRETIZE"
    - "11 DUALIZE"
    - "24 FIND THE EXTREMAL OBJECT"
  remaining_obligation: "native I0076 has no surviving frozen candidate; retained screen must handle the compact interior n=30 z>1 region or higher dimensions, and still does not address non-two-level/null-with-zero/second-contact mechanisms"
  evidence:
    - "runs/R15/20260920_0106Z_successor_screen_f0111_heterogeneous_oneheavy_j95r.md"
    - "artifacts/R15/f0111_n30_oneheavy_boundary_idea_k96s.md @ 184027608c2ef8d78a6a1a713d7cd76670be65ea"
    - "artifacts/R15/f0111_n30_oneheavy_boundary_checker_k96s.py"
    - "artifacts/R15/f0111_n30_oneheavy_boundary_checker_k96s.out"
    - "this report"
  audit_ids: []
  validation_label: "SELF_CHECK_ONLY; proof on page plus exact rational checker; no independent audit"
```
