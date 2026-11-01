Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the entire dimension-30, `N=|K|=11`, full-support two-level Hessian-null F0111 branch is eliminated, with arbitrary within-block heterogeneity; the surviving scalar branches shrink from `N in {11,12,13}` to `N in {12,13}`. Methods #5 ADD A PARAMETER AND DIFFERENTIATE, #13 FIND WHAT ONLY INCREASES, #18 SAY IT IN ANOTHER LANGUAGE.**

# R15 retained screen — complete elimination of the `n=30, N=11` two-level branch

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about Talagrand/F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand's discrete Convexity Conjecture, and does not satisfy the two-other-track audit closure rule.

The immediately preceding complete report used methods `#11/#15/#24`. The present `#5/#13/#18` triple is nonconsecutive. The originally assigned I0076 moves `#2/#12/#23` were already exhausted in the retired I0076 phase; they are not repeated here.

## 1. Whole-repository continuity, ownership, source and exclusions

Before new mathematics I reread or source-searched the required current state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the I0076 intake/history through repository-wide exact-identifier searches, including the controlling six-run handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the newest R15 report `runs/R15/20260920_0424Z_successor_screen_f0111_n14_fullcell_elimination_m98u.md` and its artifacts;
- the neighboring Burdzy--Scheutzow Problem 7.8 terminal handoff `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- current queue/gate reports. They still certify **zero newly free READY+CLOSABLE successors**. I did not steal another worker's source, promote a PENDING item, or edit a shared ledger.

`POSTED.md` was refreshed on 2026-09-20 and does not make the present restricted F0111 statement posted/closed. The R15 I0124 cap-set source has a historical claim file but its later six-run report explicitly retired it to handoff; it is not reopened by the stale claim header.

### Exact Burdzy--Scheutzow source rechecked

I rechecked the UW-hosted primary PDF, arXiv:1302.6958v4 / PTRF 160 (2014), especially Definition 2.1 and Problem 7.2.

Definition 2.1 says:

- FBM: there are random origins `S_n -> -infinity` a.s. whose complete centered futures are standard Brownian motions;
- BBM: the time-reversed process is an FBM;
- 2BM: there is one random time `S` such that the complete centered future and complete centered past at `S` are independent standard Brownian motions.

Problem 7.2 asks whether **FBM + BBM + existence of an arbitrary random time `T` at which the two complete centered half-processes are independent** implies 2BM. The source does **not** say that `T` is a stopping time and does **not** separately assume either half at `T` is Brownian. Problem 7.5 is different and remains excluded.

The controlling I0076 handoff remains unchanged. The source Theorem-6.1 candidate gives FBM, BBM and non-2BM but has no source-valid independent seam. The later Brownian-prefix/BES construction gives the source-valid independent seam but was proved to be 2BM. Hence there is no surviving frozen counterexample candidate on which the requested four obligations can honestly be counted. The old source-candidate `3/4`, BES diagnostic `3/4`, and positive-route `2/4` are historical diagnostics, not a current frozen-candidate score.

Dated searches on 2026-09-20 included exact-title/problem-number variants for `Forward Brownian Motion`, Burdzy--Scheutzow later/citing work, and the authors' current open-problem material. They recovered the primary source and related concatenated-Brownian questions but no accessible later primary paper explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

## 2. Carried F0111 state and idea-before-code receipt

The retained F0111 screen concerns the `k=2` quadratic-majorant hazard

\[
F(t)=\sum_i t_i-\log\!\left(\sum_i e^{t_i}-29\right)
\]

in dimension `n=30`. The preceding scalar-envelope and `N=14` reports proved that any remaining full-support two-level Hessian-null exact quadratic contact on the surviving `z=1+s>1` branch must have

\[
N=|K|\in\{11,12,13\}.
\]

The exact scalar cells include

\[
N=11:\qquad \frac{11}{25}<\delta<\frac5{11},\qquad
0<s<s_{11}<\frac{2323}{250000}=0.009292.
\tag{2.1}
\]

Before writing any checker I committed the new route in

`artifacts/R15/f0111_n111213_unified_entropy_idea_n99v.md`

at commit

`0832e1c1d0b2617b6645f5addfc506afb0985cf7`.

The initial ambition was one common inequality for `N=11,12,13`. The useful exact route that emerged is a complete theorem for `N=11`; this is real movement and leaves the two harder cells for future work.

## 3. Carried exact scalar and residual-Gram formulas

Put

\[
a=1+\delta,\qquad b=1-\delta,\qquad z=1+s,
\]

and carry the scalar cubic-null formulas

\[
k=\frac{2z(1-z^2)}{(1-\delta^2)(\delta+3z)},
\qquad
x=1-k-y,
\]

\[
y=\frac{(\delta+z)(1-z)(1-\delta-2z)}
{2(1-\delta)(\delta+3z)},
\]

\[
K_2=\frac{(\delta+z)(1-z^2)}{\delta+3z},
\quad
t_J=(1-z)^2-K_2,
\quad
t_K=(1+z)^2-K_2,
\]

\[
R=-\frac{2(\delta+z)(1-z^2)
(\delta^2z+3\delta z^2+\delta+3z^3)}{(\delta+3z)^2},
\]

\[
A_J=1+\frac{3t_J^2}{R},\quad
A_K=1+\frac{3t_K^2}{R},\quad
A_{JK}=1+\frac{3t_Jt_K}{R}.
\]

Let

\[
L_K=yA_K,\qquad Q_K=-kA_K,\qquad U_K=-\frac{29y}{k}.
\]

For a scalar `N=11` survivor,

\[
L_K\le11<U_K.
\tag{3.1}
\]

At an exact contact `q`, write

\[
r_i=\frac{e^{q_i}}{S(q)},\qquad
S(q)=\sum_i e^{q_i}-29,
\]

so that `sum r_i=1-k`. Let `H=D^2(P-F)(q)>=0`, let

\[
h=a\mathbf 1_J-b\mathbf 1_K
\]

be the null vector, and use the projective rank-one downdate

\[
K=H-\frac3R\beta\beta^T\succeq0,
\]

where `beta_i=r_i t_J` on `J` and `beta_j=r_j t_K` on `K`. Represent `K` by Gram vectors `w_i`. Then

\[
\|w_i\|^2=r_i(1-A_Jr_i),\qquad
\|w_j\|^2=r_j(1-A_Kr_j),
\]

and, for distinct indices,

\[
B_{ij}=\langle w_i,w_j\rangle+A_{\mathrm{block}(i),\mathrm{block}(j)}r_ir_j.
\]

If

\[
T=\Bigl\|\sum_{j\in K}w_j\Bigr\|^2,
\]

then the exact block compression is

\[
2U=\frac{b^2}{a^2}T-x+A_Jx^2,
\quad
2V=T-y+A_Ky^2,
\quad
W=\frac baT+A_{JK}xy,
\tag{3.2}
\]

and Cauchy on the eleven `K` vectors gives

\[
T\le T_{\rm cap}:=y(11-L_K).
\tag{3.3}
\]

No within-block symmetry is assumed.

## 4. Method #13 — exact finite slanted cell and monotone scalar bounds

The carried scalar theorem proves that `L_K` and `U_K` are increasing in `delta`. Define

\[
s_0=\frac{2323}{250000},
\]

\[
\delta_-(s)=\frac{1791}{4000}-\frac{11}{40}s,
\qquad
\delta_+(s)=\frac5{11}-s.
\tag{4.1}
\]

Exact Bernstein certificates prove

\[
U_K(\delta_-(s),s)<11,
\qquad
L_K(\delta_+(s),s)>11,
\quad 0<s\le s_0.
\tag{4.2}
\]

Hence every scalar survivor lies in the compact slanted band

\[
0<s<s_0,\qquad
\delta_-(s)<\delta<\delta_+(s).
\tag{4.3}
\]

On that whole band, exact rational Bernstein certificates give

\[
\frac{29}{20}<\kappa:=-\frac{k}{s}<\frac32,
\qquad
0<\frac{x-1}{s}<\frac{91}{100},
\tag{4.4}
\]

and, after putting `T=T_cap` in (3.2),

\[
U<\frac{91}{100}s,\qquad
V<3s,\qquad
W<3s.
\tag{4.5}
\]

They also give

\[
Q_K>\frac{14295}{500}=28.59,
\qquad
S(q)s=-\frac{29s}{k}<20,
\qquad A_J>1.
\tag{4.6}
\]

Residual positivity on `K` gives `r_j<=1/A_K`, hence

\[
S(q)r_j\le\frac{29}{Q_K}<\frac{14500}{14295}<e^{1/70},
\]

so

\[
q_j<\frac1{70},\qquad j\in K.
\tag{4.7}
\]

The last exponential comparison is certified by the exact rational lower bound `e^(1/70)>1+1/70+1/(2*70^2)`.

## 5. Method #18 — turn the projective subsystem into a flow/Gram obstruction

Let

\[
r_*:=\max_{i\in J}r_i.
\]

I prove

\[
\boxed{r_*<1-25s.}
\tag{5.1}
\]

Assume instead `r_*>=r_0:=1-25s`. Put

\[
\ell=x-r_0,\qquad e=r_0(1-A_Jr_0),
\]

and

\[
\Delta=
\frac{s(x-2\ell)}b-rac baT_{\rm cap}-A_{JK}\ell y.
\tag{5.2}
\]

The exact certificate proves throughout the whole slanted band

\[
e>0,\qquad 2A_Jr_0>1,\qquad
\Delta>0,\qquad
\Delta^2>eT_{\rm cap}.
\tag{5.3}
\]

Let `*=i_*` attain `r_*`, let `L=J\setminus\{*\}`, and put

\[
\ell_0=\sum_{i\in L}r_i=x-r_*\le\ell.
\]

The coordinate null equations on `J` are

\[
a\sum_{l\in J\setminus\{i\}}B_{il}
-b\sum_{j\in K}B_{ij}=sr_i.
\tag{5.4}
\]

Summing (5.4) over the light coordinates and combining with the heavy-coordinate equation, while using nonnegativity of the light-light coefficients, yields

\[
B_{L,K}\ge\frac{s(r_*-\ell_0)}b
=\frac{s(x-2\ell_0)}b
\ge\frac{s(x-2\ell)}b.
\tag{5.5}
\]

By the residual Gram representation,

\[
B_{L,K}=\langle W_L,W_K\rangle+A_{JK}\ell_0y,
\]

while `Kh=0` gives

\[
w_*+W_L=\frac baW_K.
\]

Using `T<=T_cap` and `ell_0<=ell` therefore gives

\[
\langle w_*,W_K\rangle\le-\Delta.
\tag{5.6}
\]

Residual positivity gives `r_*<=1/A_J`. Since `2A_Jr_0>1`, the function `u(1-A_Ju)` is decreasing on `[r_0,1/A_J]`, hence

\[
\|w_*\|^2=r_*(1-A_Jr_*)\le e.
\]

Cauchy then contradicts (5.3):

\[
\Delta^2
\le\langle w_*,W_K\rangle^2
\le eT
\le eT_{\rm cap}.
\]

This proves (5.1).

## 6. Method #5 — differentiate the entropy-energy gap

Exact value contact has the conserved identity

\[
E:=\sum_{i<j}B_{ij}q_iq_j
=k\log S(q)-\sum_i r_i\log r_i.
\tag{6.1}
\]

Write `L=log S(q)`. By (4.6),

\[
L<\log\frac{20}{s}.
\tag{6.2}
\]

I split according to the heaviest `J` mass.

### 6.1 Case A: `r_*>51/100`

Put

\[
c=\frac{1-r_*}{s}.
\]

By (5.1), `c>25`, while `r_*>51/100` gives

\[
cs<\frac{49}{100}.
\tag{6.3}
\]

The total light `J` mass is

\[
\ell_0=x-r_*<s(c+1).
\]

Thus every light `J` coordinate satisfies

\[
q_i< M(c):=\log(20(c+1)).
\tag{6.4}
\]

Moreover `M(c)<L`: indeed `20s(c+1)<20(49/100+s_0)<10`, whereas `S(q)s=29/kappa>58/3`. Hence every `J-J` pair contains a light coordinate and

\[
E_{JJ}<\frac{91}{100}sLM(c).
\]

Using (4.5) and (4.7),

\[
E_{JK}<\frac3{70}sL,
\qquad
E_{KK}<\frac3{4900}s.
\]

Therefore

\[
E<s\left[
\frac{91}{100}LM(c)+\frac3{70}L+\frac3{4900}
\right].
\tag{6.5}
\]

On the entropy side, the nonheavy total mass is

\[
\eta=(c+\kappa)s<1.
\]

The heavy contribution obeys, with `u=cs`,

\[
-(1-u)\log(1-u)
\ge u-\frac{u^2}{2}-\frac{u^3}{2},
\tag{6.6}
\]

using `-log(1-u)>=u+u^2/2`. The remaining coordinates have total mass `eta`, so concavity/extreme-point minimization gives

\[
-\sum_{i\ne *}r_i\log r_i\ge\eta\log(1/\eta)
\ge cs\log\frac1{s(c+3/2)}.
\tag{6.7}
\]

Since `k=-kappa s` and `kappa<3/2`, (6.1), (6.5)--(6.7) imply that any survivor must satisfy

\[
G(c,s)\le0,
\]

where

\[
\begin{aligned}
G(c,s):={}&c-\frac{c^2s}{2}-\frac{c^3s^2}{2}
+c\log\frac1{s(c+3/2)}\\
&-\log\frac{20}{s}\left[
\frac32+\frac{91}{100}\log(20(c+1))+\frac3{70}
\right]-\frac3{4900}.
\end{aligned}
\tag{6.8}
\]

I prove the opposite.

Let

\[
A(c)=\frac32+\frac{91}{100}\log(20(c+1))+\frac3{70}.
\]

For `c>=25`, `A(c)<c`: at `c=25`, `log 520<63/10` makes this immediate, and `A'(c)=91/[100(c+1)]<1`. Hence

\[
\partial_sG=-\frac{c^2}{2}-c^3s+\frac{A(c)-c}{s}<0.
\tag{6.9}
\]

Set

\[
c_0=\frac{49/100}{s_0}=\frac{122500}{2323}.
\]

For `25<=c<=c_0`, the worst allowed `s` is `s_0`. On this interval `G(c,s_0)` is strictly concave. Indeed its second derivative is bounded above by

\[
-\frac2{109}+\frac{91}{100}\frac{31/4}{26^2}
=-\frac{17947}{2267200}<0.
\tag{6.10}
\]

Exact rational Taylor enclosures of the logarithms give the endpoint margins

\[
G(25,s_0)>
\frac{13015879}{392000000}>0,
\tag{6.11}
\]

\[
G(c_0,s_0)>
\frac{14600281}{1821232}>0.
\tag{6.12}
\]

A concave function on an interval has its minimum at an endpoint, so this disposes of `25<=c<=c_0`.

For `c>=c_0`, (6.3) gives `s<beta/c` with `beta=49/100`. By (6.9), it suffices to set

\[
\Psi(c)=G(c,\beta/c).
\]

Differentiating gives

\[
\begin{aligned}
\Psi'(c)={}&1-\frac\beta2-\frac{\beta^2}{2}
+\log\frac{c}{\beta(c+3/2)}+\frac{3/2}{c+3/2}\\
&-\frac{A(c)}c
-\frac{91}{100}\frac{\log(20c/\beta)}{c+1}.
\end{aligned}
\tag{6.13}
\]

The functions `A(c)/c` and `log(20c/beta)/(c+1)` are decreasing for `c>=50`. Exact rational exponential bounds give

\[
\log(100/49)>7/10,
\quad
\log(1020)<7,
\quad
\log(100000/49)<8.
\]

Together with `log(1+3/(2c))<3/(2c)<=3/100`, these imply

\[
\Psi'(c)>
\frac{1783211}{1785000}>0,
\qquad c\ge c_0.
\tag{6.14}
\]

Since `Psi(c_0)=G(c_0,s_0)>0`, Case A is impossible.

### 6.2 Case B: `r_*<=51/100`

Every `J` mass is at most `51/100`. On `K`, residual positivity gives

\[
r_j\le\frac1{A_K}=\frac{-k}{Q_K}
<\frac{2323}{4765000}<\frac1{1000},
\]

so every coordinate mass is at most `51/100`. Since `sum r_i=1-k>1`,

\[
-\sum_i r_i\log r_i
>\log\frac{100}{51}>\frac23.
\tag{6.15}
\]

Consequently

\[
E>\frac23-\frac32sL.
\]

The function `s log(20/s)` is increasing on the present interval, and exact Taylor bounds give `log(20/s_0)<31/4`. Hence

\[
E>
\frac23-\frac32s_0\frac{31}{4}.
\tag{6.16}
\]

For every `J` coordinate,

\[
q_i\le\log\frac{(51/5)}s=:Q(s),
\]

and `Q(s)>2`, so both `sQ(s)` and `sQ(s)^2` increase with `s`. Exact Taylor bounds give

\[
Q(s_0)<\frac{71}{10}.
\]

Using (4.5) and (4.7),

\[
E<
 s_0\left[
 \frac{91}{100}\left(\frac{71}{10}\right)^2
 +\frac3{70}\frac{71}{10}
 +\frac3{4900}
 \right].
\tag{6.17}
\]

The exact gap between the lower side of (6.16) and upper side of (6.17) is

\[
\frac{47613744539}{367500000000}>0,
\tag{6.18}
\]

again impossible.

Combining Cases A and B proves the new restricted theorem:

\[
\boxed{
\text{No }n=30,\ |K|=11,\ \text{full-support two-level Hessian-null exact quadratic contact exists on }z>1.
}
\tag{6.19}
\]

Thus the retained scalar survivor set moves

\[
\boxed{\{11,12,13\}\longrightarrow\{12,13\}.}
\]

This theorem permits arbitrary heterogeneity inside both sign blocks.

## 7. Validation, literature and what remains

Only after the route above was fixed did I write and execute

`artifacts/R15/f0111_n11_fullcell_checker_n99v.py`

and archive its exact output as

`artifacts/R15/f0111_n11_fullcell_checker_n99v.out`.

The checker uses exact SymPy rationals / Python `Fraction`, exact Bernstein coefficients, one exact `2x2` Bernstein subdivision for the only harder quartic gap, and rational Taylor bounds for every logarithm. The output ends

`ALL_EXACT_CHECKS_PASS`.

This is a **SELF_CHECK**, not an independent audit.

Fresh 2026-09-20 literature checks distinguish the continuous and discrete Talagrand problems. The continuous Gaussian convexity problem was resolved in Hua--Song--Tudose, arXiv:2605.10908. The separate **discrete Convexity Conjecture** relevant to this retained screen is still treated as a conjecture by Ascoli--He--Park--Talagrand, arXiv:2608.11183 (August 11, 2026), who reformulate it via `k`-thresholds and prove substantial classes; Park, arXiv:2609.14681 (September 13, 2026), explicitly describes her dimension-free comparison as a bound **toward** the discrete conjecture. I found no accessible source matching the exact `N=11` residual-Gram/entropy exclusion above. **Novelty remains UNVERIFIED.**

This does **not** solve the full discrete conjecture. Even inside the present `k=2` first-bifurcation screen, the `n=30` cells `N=12,13` remain. Beyond them remain higher dimensions, non-two-level null directions, null directions with zero coordinates, and the separate second-contact mechanism.

The next high-value move is to reuse the present differentiated entropy gap on `N=12,13`, but not by blindly changing constants. The bottleneck is the heavy-coordinate threshold: the `N=11` projective Gram cell admits the sharp uniform `r_*<1-25s`, whereas the larger residual capacities in `N=12,13` weaken that step. A useful next route is to optimize the heavy threshold as a function of the normalized scalar cell and feed that function directly into `G`, rather than insist on a constant `C`.

## 8. Model and scheduler-control status

The limitation remains unchanged. The exposed scheduling/update interface available to this runtime supports prompt/title, schedule/timing, enabled state and ordinary task updates, but exposes **no binding model-family selector, no reasoning-effort selector, no authenticated per-run applied-model/effort receipt, and no guaranteed full-hour execution control**. Therefore GPT-6/maximum remains prompt text only; this run is honestly labeled GPT-5.6 Sol / UNVERIFIED.

`operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` records the historical P26 attempt that returned `You cannot modify this task`. Later repository reconciliation records successful P26 updates from an authorized P/C context. The compliant workaround for an edit-denied task is therefore its owning/authorized workspace/account/API/admin context or platform support, not a duplicate task or permission bypass. This R15 run made no scheduler change, as required.

## 9. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  source: "I0076 — Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2"
  native_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "RETIRED-HANDOFF; do not increment a new active count"
  tried_moves: [5, 13, 18]
  retained_screen: "Talagrand discrete Convexity Conjecture / F0111 k=2; PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_screen_metric_before: "n=30 full-support two-level z>1 scalar survivors N in {11,12,13}"
  retained_screen_metric_after: "n=30 full-support two-level z>1 scalar survivors N in {12,13}"
  retained_screen_status: "PARTIAL / SELF_CHECK_ONLY"
  remaining_obligation: "Native I0076 remains retired pending a fresh lawful reassignment; retained F0111 screen still has N=12,13 plus non-two-level/zero-coordinate/second-contact mechanisms."
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260920_0424Z_successor_screen_f0111_n14_fullcell_elimination_m98u.md"
    - "artifacts/R15/f0111_n111213_unified_entropy_idea_n99v.md @ 0832e1c1d0b2617b6645f5addfc506afb0985cf7"
    - "artifacts/R15/f0111_n11_fullcell_checker_n99v.py @ d57d721e134e27a91ef38c143affed5f73a0582d"
    - "artifacts/R15/f0111_n11_fullcell_checker_n99v.out @ 3f3bd39353d02d15f702bcd3df773e11d4190fb5"
  audit_ids: []
  audit_note: "No independent OTHER-track audit; exact checker is SELF_CHECK_ONLY."
```
