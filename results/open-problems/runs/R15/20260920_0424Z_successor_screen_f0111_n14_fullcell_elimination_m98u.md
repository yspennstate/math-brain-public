Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the entire dimension-30, `N=|K|=14`, full-support two-level Hessian-null F0111 branch is eliminated, with arbitrary within-block heterogeneity; the scalar survivors shrink from `N in {11,12,13,14}` to `N in {11,12,13}`. Methods #11 DUALIZE, #15 BREAK THE SYMMETRY ON PURPOSE, #24 FIND THE EXTREMAL OBJECT.**

# R15 retained screen — complete elimination of the `n=30, N=14` two-level branch

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about Talagrand/F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand Problem 10.9, and does not satisfy the independent-audit closure rule.

The immediately preceding complete report used methods `#4/#19/#30`. The present `#11/#15/#24` triple is nonconsecutive and is applied to a new object: the complete finite `N=14` cell after the exact scalar-envelope reduction.

## 1. Source continuity, allocation and exclusions

I reread the current repository state required by the owner policy: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest R15 reports/artifacts, and the current operations implementation material. The queue still records zero newly certified free READY candidates. I did not steal another worker's source, promote a PENDING row to READY, edit any shared root ledger, or create a successor claim.

### Exact Burdzy--Scheutzow source

I rechecked Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126, including Definition 2.1 and the exact text of Problem 7.2.

Definition 2.1 says:

- FBM: there are random origins `S_n -> -infinity` a.s. whose complete centered futures are standard Brownian motions;
- BBM: the time-reversed process is an FBM;
- 2BM: there is one random time `S` such that the complete centered future and complete centered past at `S` are independent standard Brownian motions.

Problem 7.2 asks whether **FBM + BBM + existence of an arbitrary random time `T` at which the two complete centered half-processes are independent** implies 2BM. The source does not say that `T` is a stopping time and does not separately assume either half at `T` is Brownian. Problem 7.5 is different and remains excluded.

The controlling I0076 six-run handoff remains unchanged. The source-Theorem-6.1 candidate gives FBM, BBM and non-2BM but does not give the Problem-7.2 independent seam. The later Brownian-prefix/BES candidate gives the independent seam but was proved to be 2BM. Hence there is no surviving frozen counterexample candidate on which the requested four obligations can honestly be rescored. The historical `2/4` is a retired positive-route value, not a current candidate score.

A dated exact-title/arXiv/problem-language search again recovered the primary source and did not recover an accessible later primary paper explicitly announcing a resolution of exact Problem 7.2. This is only bounded negative evidence; it is not a worldwide-openness certificate.

## 2. Retained F0111 screen: carried exact scalar cell

The preceding report

`runs/R15/20260920_0256Z_successor_screen_f0111_n30_scalar_envelope_l97t.md`

proved that any remaining dimension-30, full-support, two-level Hessian-null exact quadratic contact on the surviving `z>1` branch must have

`N=|K| in {11,12,13,14}`,

with the `N=14` cell contained in

\[
0<s:=z-1<s_{14}<\frac{217}{50000},
\qquad
\frac{14}{25}<\delta<\frac47.
\tag{2.1}
\]

The present run eliminates this entire `N=14` cell.

Put

\[
a=1+\delta,\qquad b=1-\delta,
\tag{2.2}
\]

and use the carried cubic-null scalar functions

\[
k=\frac{2z(1-z^2)}{(1-\delta^2)(\delta+3z)},
\qquad
x=1-k-y,
\tag{2.3}
\]

\[
y=\frac{(\delta+z)(1-z)(1-\delta-2z)}
{2(1-\delta)(\delta+3z)},
\tag{2.4}
\]

\[
K_2=\frac{(\delta+z)(1-z^2)}{\delta+3z},
\quad
t_J=(1-z)^2-K_2,
\quad
t_K=(1+z)^2-K_2,
\tag{2.5}
\]

\[
R=-\frac{2(\delta+z)(1-z^2)
(\delta^2z+3\delta z^2+\delta+3z^3)}{(\delta+3z)^2},
\tag{2.6}
\]

and

\[
A_J=1+\frac{3t_J^2}{R},\qquad
A_K=1+\frac{3t_K^2}{R},\qquad
A_{JK}=1+\frac{3t_Jt_K}{R}.
\tag{2.7}
\]

As before,

\[
L_K=yA_K,\qquad Q_K=-kA_K,\qquad U_K=-\frac{29y}{k}.
\tag{2.8}
\]

For `N=14`, scalar feasibility requires

\[
L_K\le14<U_K.
\tag{2.9}
\]

## 3. Method #11: dualize the projective condition to a residual Gram system

Let `P` be a putative nonnegative-coefficient quadratic global majorant exact at an interior contact `q>0`, let

\[
G=P-F,\qquad H=D^2G(q)\succeq0,
\tag{3.1}
\]

and let

\[
h=a\mathbf1_J-b\mathbf1_K
\tag{3.2}
\]

be the full-support two-level null vector. Write

\[
r_i=\frac{e^{q_i}}{S(q)},\qquad S(q)=\sum_i e^{q_i}-29.
\tag{3.3}
\]

The projective fourth-order necessary condition is equivalent to the rank-one downdate

\[
K:=H-\frac3R\,\beta\beta^T\succeq0,
\tag{3.4}
\]

where

\[
\beta_i=r_it_J\quad(i\in J),\qquad
\beta_j=r_jt_K\quad(j\in K).
\tag{3.5}
\]

Cubic nullity gives `beta.h=0`, so `Kh=0`. Represent `K` as a Gram matrix of vectors `w_i`. Then

\[
\|w_i\|^2=r_i(1-A_Jr_i),\quad i\in J,
\qquad
\|w_j\|^2=r_j(1-A_Kr_j),\quad j\in K,
\tag{3.6}
\]

and, for distinct indices,

\[
B_{ij}=\langle w_i,w_j\rangle+A_{\mathrm{block}(i),\mathrm{block}(j)}r_ir_j.
\tag{3.7}
\]

Let

\[
W_J=\sum_{i\in J}w_i,\qquad W_K=\sum_{j\in K}w_j,
\qquad T=\|W_K\|^2.
\tag{3.8}
\]

Since `Kh=0`,

\[
aW_J=bW_K.
\tag{3.9}
\]

If `U,V,W` denote the aggregate pair-coefficient masses on `J-J`, `K-K`, and `J-K`, respectively, then, **without any within-block symmetry assumption**,

\[
2U=\frac{b^2}{a^2}T-x+A_Jx^2,
\tag{3.10}
\]

\[
2V=T-y+A_Ky^2,
\tag{3.11}
\]

\[
W=\frac baT+A_{JK}xy.
\tag{3.12}
\]

Cauchy on the fourteen `K`-vectors gives the sharp block-capacity upper bound

\[
T\le T_{\rm cap}:=y(14-L_K).
\tag{3.13}
\]

Thus every aggregate coefficient-energy term is controlled by one scalar `T`.

## 4. Exact localization of the complete `N=14` cell

Set

\[
s_0=\frac{217}{50000},\qquad
\delta_{\rm hi}=\frac47,
\qquad
\delta_{\rm line}(s)=\frac{5689}{10000}-\frac{11}{50}s.
\tag{4.1}
\]

The exact Bernstein checker proves

\[
U_K(\delta_{\rm line}(s),s)<14
\quad(0\le s\le s_0).
\tag{4.2}
\]

Since `U_K` is increasing in `delta`, (2.9) forces every `N=14` scalar survivor into the slanted compact cell

\[
0<s<s_0,\qquad
\delta_{\rm line}(s)<\delta<\frac47.
\tag{4.3}
\]

On this entire cell, exact Bernstein-sign certificates give

\[
\frac32<\kappa:=-\frac{k}{s}<\frac{167}{100},
\tag{4.4}
\]

\[
0<\frac{x-1}{s}<\frac78,
\qquad
0<\frac{y}{s}<\frac{13}{16},
\tag{4.5}
\]

\[
0<\frac{A_J-1}{s}<\frac78,
\qquad
0<A_{JK}<5,
\tag{4.6}
\]

and, after putting `T=T_cap` in (3.10)--(3.12),

\[
U<s,\qquad
V<\frac{11}{2}s,\qquad
W<\frac{17}{4}s.
\tag{4.7}
\]

The same exact certificate gives

\[
Q_K>\frac{144}{5},
\qquad
S(q)s<18.
\tag{4.8}
\]

These are uniform over the **whole** scalar cell, not point samples.

## 5. Method #15: a heavy-coordinate alternative

Let

\[
r_*:=\max_{i\in J}r_i.
\tag{5.1}
\]

I first prove that no survivor can satisfy

\[
r_*\ge1-50s.
\tag{5.2}
\]

Set

\[
r=1-50s,\qquad \ell=x-r,\qquad e=r(1-A_Jr).
\tag{5.3}
\]

The exact checker proves on the whole cell that

\[
\Delta:=\frac{s(x-2\ell)}{b}
-\frac baT_{\rm cap}-A_{JK}\ell y>0,
\tag{5.4}
\]

and

\[
\Delta^2>eT_{\rm cap}.
\tag{5.5}
\]

Assume (5.2), and write `L=J\setminus{*}` and

\[
\ell_0=\sum_{i\in L}r_i=x-r_*\le\ell.
\tag{5.6}
\]

The coordinate null equations are

\[
a\sum_{l\in J\setminus\{i\}}B_{il}
-b\sum_{j\in K}B_{ij}=sr_i,
\qquad i\in J.
\tag{5.7}
\]

Summing (5.7) over the light set and using nonnegativity of the light-light coefficients plus the heavy-coordinate equation yields

\[
B_{L,K}\ge\frac{s(r_*-\ell_0)}b
=\frac{s(x-2\ell_0)}b
\ge\frac{s(x-2\ell)}b.
\tag{5.8}
\]

By (3.7),

\[
B_{L,K}=\langle W_L,W_K\rangle+A_{JK}\ell_0y.
\tag{5.9}
\]

Also `w_*+W_L=(b/a)W_K`. Therefore, using `T\le T_cap`,

\[
\langle w_*,W_K\rangle
\le-\Delta.
\tag{5.10}
\]

On the cell, `A_J>1` and `r\ge1-50s_0>0.78`, so `u\mapsto u(1-A_Ju)` is decreasing on `[r,1/A_J]`. Thus

\[
\|w_*\|^2=r_*(1-A_Jr_*)\le e.
\tag{5.11}
\]

Cauchy now gives

\[
\Delta^2
\le\langle w_*,W_K\rangle^2
\le eT
\le eT_{\rm cap},
\tag{5.12}
\]

contradicting (5.5). Hence

\[
\boxed{r_*<1-50s.}
\tag{5.13}
\]

This is the first half of the full-cell contradiction.

## 6. Method #24: extremize entropy against coefficient energy

Put

\[
c=\frac{1-r_*}{s}>50,
\qquad
\alpha=\frac{167}{100}.
\tag{6.1}
\]

At an exact interior contact, `q_i=\log(Sr_i)>0`, and exact value contact can be written in the two equivalent forms

\[
E:=\sum_{i<j}B_{ij}q_iq_j
=k\log S-\sum_i r_i\log r_i.
\tag{6.2}
\]

This is the conserved quantity that couples coefficient energy to entropy.

### 6.1 Uniform coefficient-energy upper bounds

From residual positivity, `r_j\le1/A_K` on `K`. By (4.8),

\[
Sr_j\le\frac{S}{A_K}=\frac{29}{Q_K}<\frac{145}{144},
\tag{6.3}
\]

so

\[
q_j<\log(145/144)<\frac1{144},\qquad j\in K.
\tag{6.4}
\]

Let

\[
L=\log S<\log\frac{18}{s}.
\tag{6.5}
\]

If `r_*>201/400`, it is the unique coordinate above `1/2`, because `x<1+(7/8)s_0`. Every other `J`-mass is at most

\[
\ell_0=x-r_*<s(c+1),
\tag{6.6}
\]

and therefore its contact coordinate is bounded by

\[
q_i<\log(18(c+1))=:M(c).
\tag{6.7}
\]

Every `J-J` pair contains at least one light coordinate. Using (4.7),

\[
E_{JJ}<sL M(c).
\tag{6.8}
\]

Similarly,

\[
E_{JK}<\frac{17}{576}sL,
\qquad
E_{KK}<\frac{11}{41472}s.
\tag{6.9}
\]

Writing

\[
b_0=\frac{17}{576},\qquad d_0=\frac{11}{41472},
\tag{6.10}
\]

we have

\[
E<s\left[L(M(c)+b_0)+d_0\right].
\tag{6.11}
\]

### 6.2 Case A: `r_*>201/400`

The total non-heavy mass is

\[
\eta=(1-k)-r_*=(c+\kappa)s<s(c+\alpha)<1.
\tag{6.12}
\]

Every non-heavy mass is at most `eta`, hence

\[
-\sum_{i\ne *}r_i\log r_i
\ge cs\log\frac1{s(c+\alpha)}.
\tag{6.13}
\]

Since `k=-\kappa s` and `\kappa<\alpha`, (6.2) gives

\[
E\ge cs\log\frac1{s(c+\alpha)}-\alpha sL.
\tag{6.14}
\]

Combining (6.11), (6.14), and `L<\log(18/s)`, every survivor would have to satisfy

\[
\Phi(c,s):=
 c\log\frac1{s(c+\alpha)}
-\log\frac{18}{s}\left[\alpha+\log(18(c+1))+b_0\right]
-d_0\le0.
\tag{6.15}
\]

I prove the opposite.

For `c\ge50`, the coefficient of `\log(1/s)` in `\Phi` is positive, so `\Phi` increases as `s` decreases. Put

\[
c_0=\frac{25000}{217}=\frac1{2s_0}.
\tag{6.16}
\]

On `50\le c\le c_0`, the worst case is `s=s_0`. As a function of `c`, `\Phi(c,s_0)` is strictly concave: its second derivative is

\[
-\frac1{c+\alpha}-\frac{\alpha}{(c+\alpha)^2}
+\frac{\log(18/s_0)}{(c+1)^2}<0,
\tag{6.17}
\]

since `c\ge50` and `\log(18/s_0)<8.331`. Hence the minimum is at an endpoint. Exact rational Taylor enclosures of the logarithms give

\[
\Phi(50,s_0)>
\frac{131160679}{64800000}>0,
\tag{6.18}
\]

\[
\Phi(c_0,s_0)>
\frac{23447914307}{70308000000}>0.
\tag{6.19}
\]

For `c\ge c_0`, the assumption `r_*>201/400` gives `cs<199/400<1/2`, hence `s<1/(2c)`. Therefore it suffices to bound

\[
\Psi(c):=\Phi\left(c,\frac1{2c}\right).
\tag{6.20}
\]

Again `\Psi(c_0)>0`, and the exact logarithmic bounds used in the checker yield the uniform derivative lower bound

\[
\Psi'(c)>
\frac{23870468789947}{45390600000000}>0,
\qquad c\ge c_0.
\tag{6.21}
\]

Thus `\Phi(c,s)>0` for every case-A point, contradicting (6.15).

### 6.3 Case B: `r_*\le201/400`

Now every coordinate mass is at most `201/400`. Since

\[
\sum_i r_i=1-k>1,
\tag{6.22}
\]

entropy satisfies

\[
-\sum_i r_i\log r_i
>\log\frac{400}{201}>rac23.
\tag{6.23}
\]

The last logarithmic inequality is certified by a rational Taylor enclosure.

All `J` coordinates satisfy

\[
q_i<\log\frac{10}{s}.
\tag{6.24}
\]

Hence, by (4.7),

\[
E<s\left[\log^2\frac{10}{s}+b_0\log\frac{10}{s}+d_0\right].
\tag{6.25}
\]

On `0<s\le s_0`, the functions `s\log(10/s)` and `s\log^2(10/s)` are increasing. Exact Taylor bounds give

\[
\log(10/s_0)<\frac{31}{4},
\qquad
\log(18/s_0)<\frac{8331}{1000}.
\tag{6.26}
\]

Using (6.2), (6.23), and `\kappa<\alpha`, we obtain the lower bound

\[
E>rac23-\alpha s_0\frac{8331}{1000}.
\tag{6.27}
\]

while (6.25)--(6.26) give

\[
E<s_0\left[\left(\frac{31}{4}\right)^2
+b_0\frac{31}{4}+d_0\right].
\tag{6.28}
\]

The exact gap between the lower side of (6.27) and upper side of (6.28) is

\[
\frac{2233138533611}{6480000000000}>0,
\tag{6.29}
\]

again a contradiction.

Cases A and B exhaust all possibilities after (5.13). Therefore:

\[
\boxed{
\text{There is no dimension-30, full-support, two-level, Hessian-null exact quadratic contact}
\atop
\text{on the }z>1\text{ branch with }|K|=14,
}
\tag{6.30}
\]

with **no within-block symmetry assumption**.

Equivalently, the scalar survivor list shrinks from

\[
\boxed{N\in\{11,12,13,14\}}
\quad\text{to}\quad
\boxed{N\in\{11,12,13\}}.
\tag{6.31}
\]

The previous global numerical localization `0<z-1<0.014404` remains controlled by the `N=12` scalar branch and is not improved by this run.

## 7. Exact validation and prior-art scope

The research route was written before the checker at commit

`6f2c9d0291b10c3f708723690e50f2b0bc1d18af`

in

`artifacts/R15/f0111_n14_finite_residual_idea_m98u.md`.

Only after that route existed, the exact checker was added at

`e8dabe17b1ac85e472af2bd9d59756c56e2ebd6a`

as

`artifacts/R15/f0111_n14_fullcell_checker_m98u.py`.

Its archived exact output is

`artifacts/R15/f0111_n14_fullcell_checker_m98u.out`

at commit

`ea720af2efc71b759d74dbffdd09b593ef8db0df`.

It certifies the slanted-cell reduction, all rational-function sign bounds, the heavy-coordinate Cauchy contradiction, and every logarithm inequality by exact rational Taylor enclosures. The final line is

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit.

For current literature, I rechecked the August 11, 2026 Ascoli--He--Park--Talagrand `k`-threshold reformulation (arXiv:2608.11183) and the September 13, 2026 Park dimension-free comparison (arXiv:2609.14681), whose abstract explicitly says the result gives a dimension-independent bound **toward** Talagrand's discrete Convexity Conjecture. Nothing in this bounded search authorizes calling the present restricted `k=2` first-bifurcation theorem a solution of the full conjecture. I found no accessible source matching the exact `N=14` residual-Gram/entropy exclusion above, but **novelty remains UNVERIFIED**.

The next useful target is not another checker on `N=14`; that branch is finished at this level. Attack `N=11,12,13`, starting with whichever admits the strongest residual-capacity pinch, or find a compression that eliminates all three at once. The broader unsolved mechanisms remain: non-two-level null directions, null directions with zero coordinates, and the distinct second-contact mechanism.

## 8. Model/scheduler control status

The repository's current implementation record remains unchanged: the exposed scheduler/task surface has prompt/title, schedule/timing and enabled-state controls, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort attestation, and no guaranteed full-hour execution field. Thus `GPT-6 / maximum` remains prompt text only in this environment.

The historical P26 `You cannot modify this task` event was authorization-context-specific; `RESULTS.md` records that a later full P26 update succeeded from an authorized P/C context. The compliant workaround is the owning/authorized workspace/account/API/admin context or platform support, not a permission bypass or duplicate task. I made no scheduler mutation in this run.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: R15
  native_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2 / intake I0076"
  native_metric: "number of the four source-matching obligations proved for one frozen counterexample candidate"
  native_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE; historical retired positive-route value 2/4"
  native_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE; historical retired positive-route value 2/4"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "6_FROZEN_AT_HANDOFF"
  tried_moves: [11, 15, 24]
  remaining_native_obligation: "Future reassignment requires a new source-valid frozen candidate satisfying the exact arbitrary-random-time independence hypothesis, or a proof of the implication under the source's complete hypotheses."
  retained_screen: "Talagrand F0111 k=2; PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_screen_metric_before: "n=30 full-support two-level z>1 scalar survivors N in {11,12,13,14}"
  retained_screen_metric_after: "n=30 full-support two-level z>1 scalar survivors N in {11,12,13}"
  retained_screen_status: "PARTIAL / SELF_CHECK_ONLY"
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260920_0256Z_successor_screen_f0111_n30_scalar_envelope_l97t.md"
    - "artifacts/R15/f0111_n14_finite_residual_idea_m98u.md @ 6f2c9d0291b10c3f708723690e50f2b0bc1d18af"
    - "artifacts/R15/f0111_n14_fullcell_checker_m98u.py @ e8dabe17b1ac85e472af2bd9d59756c56e2ebd6a"
    - "artifacts/R15/f0111_n14_fullcell_checker_m98u.out @ ea720af2efc71b759d74dbffdd09b593ef8db0df"
  audit_ids: []
  audit_note: "No independent audit; exact checker is SELF_CHECK_ONLY."
```
