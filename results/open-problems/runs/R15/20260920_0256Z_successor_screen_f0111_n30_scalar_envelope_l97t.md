Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: for F0111 `k=2`, every dimension-30 full-support two-level Hessian-null scalar survivor is now confined to exactly four integer block branches with exact algebraic `z-1` cutoffs; globally `0<z-1<0.014404`. Methods #4 PROVE SOMETHING WEAKER COMPLETELY, #19 MAKE IT AN ALGORITHM, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R15 retained screen — exact scalar envelope for the remaining dimension-30 two-level branch

Date checked: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything about Talagrand/F0111 below remains **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. This report does not reopen Burdzy--Scheutzow Problem 7.2, does not promote F0111 to READY, does not solve Talagrand Problem 10.9, and does not satisfy the independent-audit closure rule.

Historical R15 work has already used all thirty Section-B move numbers at least once. Thus the literal globally-never-used-number condition is exhausted. The present triple differs from the immediately preceding `#8/#11/#24` and is applied to a new object: the exact two-variable scalar feasibility region left after the dimension-30 boundary analysis.

## 1. Continuity, source exactness, allocation and whole-repository readback

Before new mathematics I reread/recovered the current `master` state required by the owner policy:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- the controlling I0076 six-run handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- the newest own report `runs/R15/20260920_0209Z_successor_screen_f0111_n30_oneheavy_boundary_k96s.md`;
- the newest neighboring Burdzy report, R07's Problem-7.8 terminal handoff `runs/R07/20260919T093413Z_i0077_random_reroot_periodic_completion_59_handoff_rr59s3.md`;
- targeted searches for I0076/I0077, current queue/claim state, and F0111 work.

The root queue still records zero newly certified free READY candidates. I0077 remains separately owned/handoff-retired by R07; F0111 remains a retained screen, not a claimed successor. I did not steal another worker's source, promote a PENDING row to READY, edit a shared ledger, or create a successor claim.

### Exact Burdzy--Scheutzow source

I rechecked the primary PDF on 2026-09-20: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), 95--126.

Definition 2.1 says:

- FBM: there are random origins `S_n -> -infinity` a.s. whose complete centered **futures** are standard Brownian motions;
- BBM: the time-reversed process is an FBM;
- 2BM: there is one random time `S` such that the complete centered future and complete centered past at `S` are **independent standard Brownian motions**.

Problem 7.2 asks whether FBM + BBM plus existence of an arbitrary random time `T` at which the two complete centered half-processes are independent implies 2BM. The problem does **not** say `T` is a stopping time and does **not** separately assume either half at `T` is Brownian. Problem 7.5 is different and remains excluded.

The controlling six-run handoff remains correct. The source-Theorem-6.1 candidate has FBM, BBM and non-2BM but no source-valid independent seam; the later Brownian-prefix/BES candidate had an exact independent seam but was proved to be 2BM. Hence there is no surviving frozen counterexample candidate on which the requested four obligations can honestly be counted. The historical `2/4` is a retired positive-route metric, not a current counterexample score.

Fresh dated searches using the exact title/arXiv number/Problem-7.2 language recovered the source and later references but no accessible later primary paper explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only, not a worldwide-openness certificate.

## 2. Current F0111 literature scope

For the retained screen I rechecked current primary literature:

- Ruben Ascoli, Xiaoyu He, Jinyoung Park and Michel Talagrand, arXiv:2608.11183, 11 Aug 2026, reformulate the discrete Convexity Conjecture using `k`-thresholds and prove substantial classes;
- Jinyoung Park, arXiv:2609.14681, 13 Sep 2026, proves a dimension-free expectation/fractional-expectation comparison whose application is explicitly described as progress **toward** the conjecture.

These sources do not authorize calling the present `k=2` first-bifurcation work a full solution. I found no accessible source matching the scalar-envelope theorem below in this bounded search. **Novelty remains UNVERIFIED.**

## 3. Carried exact scalar subsystem

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
G=P-F,\qquad H=D^2G(q)\succeq0.
\tag{3.3}
\]

Assume `H` has a full-support two-level mixed null direction

\[
h=(1+\delta)\mathbf1_J-(1-\delta)\mathbf1_K,
\qquad 0<\delta<1,
\tag{3.4}
\]

and orient it on the only branch still possible in dimension 30,

\[
z=1+s,\qquad s>0.
\tag{3.5}
\]

Write `N=|K|`. The exact cubic-null formulas carried from the preceding reports are

\[
k=\frac{2z(1-z^2)}{(1-\delta^2)(\delta+3z)},
\tag{3.6}
\]

\[
y=\frac{(\delta+z)(1-z)(1-\delta-2z)}
{2(1-\delta)(\delta+3z)},
\tag{3.7}
\]

\[
K_2=\frac{(\delta+z)(1-z^2)}{\delta+3z},
\qquad
t_K=(1+z)^2-K_2,
\tag{3.8}
\]

and

\[
R=-\frac{2(\delta+z)(1-z^2)
(\delta^2z+3\delta z^2+\delta+3z^3)}
{(\delta+3z)^2}.
\tag{3.9}
\]

The projective fourth-order/block-capacity theorem gives

\[
N\ge L_K(\delta,s):=y\left(1+\frac{3t_K^2}{R}\right),
\tag{3.10}
\]

while full-support positivity `q_i>0` gives, for `n=30`,

\[
N<U_K(\delta,s):=-\frac{29y}{k}.
\tag{3.11}
\]

Finally define the pure scalar projective quantity

\[
Q_K(\delta,s):=-k\left(1+\frac{3t_K^2}{R}\right).
\tag{3.12}
\]

The three quantities satisfy the exact identity

\[
\boxed{\frac{L_K}{U_K}=\frac{Q_K}{29}.}
\tag{3.13}
\]

Thus every dimension-30 full-support two-level scalar survivor must satisfy

\[
L_K\le N<U_K,
\qquad Q_K<29.
\tag{3.14}
\]

The previous report excluded an actual **full contact sequence** with `s->0`, using the heterogeneous one-heavy limiting system and exact value contact. The present run does something different: it solves the entire **scalar necessary region** (3.14) exactly.

## 4. Method #30 — localize one scale at a time

For compactness write `d=delta`. Direct simplification gives

\[
U_K(d,s)=
\frac{29(d+1)(d+s+1)(d+2s+1)}{4(s+1)(s+2)}.
\tag{4.1}
\]

The formulas for `L_K,Q_K` are rational with the same positive core polynomial

\[
T=d^2s+d^2+3ds^2+6ds+4d+3s^3+9s^2+9s+3>0.
\tag{4.2}
\]

Their continuous `s=0` boundary values are

\[
L_K(d,0)=\frac6{1-d},
\qquad
U_K(d,0)=\frac{29(1+d)^3}{8},
\tag{4.3}
\]

\[
Q_K(d,0)=\frac{48}{(1-d)(1+d)^3}.
\tag{4.4}
\]

### 4.1 `Q_K` is strictly increasing in `s`

Exact differentiation gives

\[
\partial_s Q_K=
\frac{-2\,P_Q(d,s)}
{(d-1)(d+1)(d+s+1)^2T(d,s)^2},
\tag{4.5}
\]

where `P_Q` is a polynomial whose every coefficient in `(d,s)` is strictly positive. On `0<d<1`, `s>0`, the denominator has exactly one negative factor, `d-1`. Therefore

\[
\boxed{\partial_sQ_K>0.}
\tag{4.6}
\]

Also

\[
\partial_dQ_K(d,0)
=\frac{96(2d-1)}{(d-1)^2(d+1)^4}.
\tag{4.7}
\]

Hence the boundary function decreases up to `d=1/2` and then increases. At the two rational test points,

\[
Q_K(2/5,0)-29=\frac{53}{343}>0,
\qquad
Q_K(3/5,0)-29=\frac{19}{64}>0.
\tag{4.8}
\]

Since a survivor has `Q_K(d,s)<29<Q_K(d,s')` nowhere with smaller `s`, (4.6)--(4.8) imply

\[
\boxed{\frac25<d<\frac35.}
\tag{4.9}
\]

### 4.2 An explicit global upper scale: `s<3/200`

Because `Q_K` increases in `s`, it is enough to show

\[
Q_K(d,3/200)>29
\qquad(2/5\le d\le3/5).
\tag{4.10}
\]

Exact simplification gives

\[
Q_K(d,3/200)-29
=
\frac{-29P(d)}
{20000(d-1)(d+1)(200d+203)(8120000d^2+32725400d+25096281)},
\tag{4.11}
\]

where

\[
\begin{aligned}
P(d)={}&32480000000000d^5+163868800000000d^4
+200770248000000d^3\\
&-61909179580000d^2-176894008806200d
+67683686139909.
\end{aligned}
\tag{4.12}
\]

The denominator in (4.11) is negative on the interval, so it remains to prove `P(d)>0`. Put

\[
d=\frac12+u,\qquad |u|\le\frac1{10}.
\tag{4.13}
\]

Then

\[
\begin{aligned}
P(1/2+u)={}&112467841809+3858897613800u
+525649392420000u^2\\
&+609707848000000u^3+245068800000000u^4
+32480000000000u^5.
\end{aligned}
\tag{4.14}
\]

For `u>=0` positivity is immediate. For `u=-v`, `0\le v\le1/10`, split (4.14) as

\[
\left(c_0-c_1v+\frac{c_2}{10}v^2\right)
+
\left(\frac{9c_2}{10}v^2-c_3v^3\right)
+
\left(c_4v^4-c_5v^5\right).
\tag{4.15}
\]

The first bracket is positive for every real `v`, because its discriminant is

\[
c_1^2-4c_0(c_2/10)
=-8756370291684475524672000<0.
\tag{4.16}
\]

The other two are positive because

\[
\frac9{10}c_2-\frac1{10}c_3
=412113668378000>0,
\tag{4.17}
\]

\[
c_4-\frac1{10}c_5
=241820800000000>0.
\tag{4.18}
\]

Thus `P>0` throughout the interval, proving (4.10), hence

\[
\boxed{0<s<\frac3{200}=0.015.}
\tag{4.19}
\]

This is the first **effective** global upper localization of the remaining dimension-30 scalar branch. It is logically different from the preceding theorem, which gave a qualitative positive distance of any full-system survivor from `s=0` but did not compute that distance.

## 5. Method #4 — a complete finite integer classification

Exact differentiation gives

\[
\partial_d U_K=
\frac{29(3d^2+6ds+6d+2s^2+6s+3)}{4(s+1)(s+2)}>0,
\tag{5.1}
\]

\[
\partial_s U_K=
-\frac{29(d-1)(d+1)(2ds+3d+3s^2+6s+3)}
{4(s+1)^2(s+2)^2}>0.
\tag{5.2}
\]

Similarly

\[
\partial_dL_K=
\frac{(s+1)(s+2)P_d(d,s)}{(d-1)^2T(d,s)^2}>0,
\tag{5.3}
\]

and

\[
\partial_sL_K=
-\frac{P_s(d,s)}{2(d-1)T(d,s)^2}>0,
\tag{5.4}
\]

where every coefficient of `P_d` and `P_s` is positive. The exact coefficient check is archived, but the sign argument is fully displayed here: `(d-1)^2>0`, while in (5.4) the numerator and `d-1` are both negative after the displayed minus sign.

Now (4.9), (4.19), and monotonicity immediately make the integer block size finite. Since `s>0`,

\[
L_K(d,s)>L_K(d,0)>L_K(2/5,0)=10,
\tag{5.5}
\]

so `N>=11`. On the other side,

\[
U_K(d,s)<U_K(3/5,3/200)
=\frac{210596}{14105}<15,
\tag{5.6}
\]

because the gap to `15` is exactly `979/14105`. Since `N<U_K`,

\[
\boxed{N\in\{11,12,13,14\}.}
\tag{5.7}
\]

We can also trap `d` separately on each branch. From `N>=L_K>L_K(d,0)`,

\[
\boxed{d<1-\frac6N.}
\tag{5.8}
\]

For the lower endpoint, monotonicity gives

\[
U_K(d,s)\le U_K(N/25,3/200)<N
\quad\text{whenever }d\le N/25,
\tag{5.9}
\]

with exact gaps

\[
\begin{array}{c|c}
N & U_K(N/25,3/200)-N\\ \hline
11 & -827/10075\\
12 & -1699/10850\\
13 & -82/455\\
14 & -47/310.
\end{array}
\tag{5.10}
\]

This contradicts `N<U_K`. Therefore the scalar region is already contained in the four disjoint strips

\[
\boxed{
\begin{array}{c|c}
N & \text{necessary }d\text{-interval}\\ \hline
11 & 11/25<d<5/11\\
12 & 12/25<d<1/2\\
13 & 13/25<d<7/13\\
14 & 14/25<d<4/7.
\end{array}}
\tag{5.11}
\]

## 6. Method #19 — turn the scalar region into an exact decision algorithm

Fix `N in {11,12,13,14}` and `0\le s\le3/200`. Since `L_K,U_K` are strictly increasing in `d`, define the unique roots

\[
L_K(d_L(s),s)=N,
\qquad
U_K(d_U(s),s)=N.
\tag{6.1}
\]

These roots exist for the whole interval. Indeed,

\[
L_K(0,3/200)=\frac{10166643943}{1648360000}<11,
\tag{6.2}
\]

while `L_K(d,s)->infinity` as `d->1-`; and

\[
U_K(0,3/200)=\frac{2987}{806}<11,
\qquad
U_K(1,s)=29.
\tag{6.3}
\]

Thus scalar feasibility for fixed `(N,s)` is exactly

\[
\boxed{d_U(s)<d_L(s).}
\tag{6.4}
\]

At `s=0`, the inequality is strict. Explicit witnesses `d` satisfying `L_K(d,0)<N<U_K(d,0)` are

\[
\begin{array}{c|c|c|c}
N&d&L_K(d,0)-N&U_K(d,0)-N\\ \hline
11&9/20&-1/11&3281/64000\\
12&99/200&-12/101&7196071/64000000\\
13&267/500&-29/233&85312227/1000000000\\
14&57/100&-2/43&226897/8000000.
\end{array}
\tag{6.5}
\]

At `s=3/200`, Section 4 gives `Q_K>29`, hence by (3.13) `L_K>U_K` for every `d`, so `d_L<d_U`. Therefore the continuous difference

\[
D_N(s):=d_L(s)-d_U(s)
\tag{6.6}
\]

starts positive and ends negative.

A collision `D_N(s)=0` satisfies simultaneously

\[
U_K=N,\qquad L_K=N.
\tag{6.7}
\]

By (3.13), this is equivalent to

\[
U_K=N,\qquad Q_K=29.
\tag{6.8}
\]

Eliminating `d` between the two numerator equations gives

\[
\operatorname{Res}_d(U_K-N,Q_K-29)
=-585336(s+1)^4(s+2)^5p_N(s),
\tag{6.9}
\]

where

\[
\begin{aligned}
p_{11}(s)={}&446571s^9-2080576s^8-23192680s^7-30122272s^6
+24917048s^5\\
&+81222240s^4+28249216s^3-45477248s^2-37603456s+353280,
\end{aligned}
\tag{6.10}
\]

\[
\begin{aligned}
p_{12}(s)={}&446571s^9-2549390s^8-25754740s^7-29216592s^6
+38403072s^5\\
&+97455168s^4+23071200s^3-65155968s^2-48254400s+708480,
\end{aligned}
\tag{6.11}
\]

\[
\begin{aligned}
p_{13}(s)={}&446571s^9-3018204s^8-28265848s^7-27711296s^6
+53330920s^5\\
&+113982272s^4+14796384s^3-89174592s^2-61129984s+786688,
\end{aligned}
\tag{6.12}
\]

\[
\begin{aligned}
p_{14}(s)={}&446571s^9-3487018s^8-30726004s^7-25644160s^6
+69666704s^5\\
&+130731424s^4+3096384s^3-118209920s^2-76857152s+335744.
\end{aligned}
\tag{6.13}
\]

### 6.1 Each `p_N` has exactly one root on `[0,3/200]`

Every `p_N(0)>0`, while exact rational evaluation gives `p_N(3/200)<0` for all four values. To prove uniqueness, differentiate. If all negative nonconstant terms of `p_N'` are discarded and each positive monomial is maximized at `s=3/200`, we obtain the following rigorous upper bounds:

\[
\begin{array}{c|c|c}
N & \text{constant term of }p_N' & \text{all positive higher terms at }3/200\\ \hline
11&-37603456&<20172\\
12&-48254400&<16899\\
13&-61129984&<11540\\
14&-76857152&<3873.
\end{array}
\tag{6.14}
\]

Thus

\[
\boxed{p_N'(s)<0\quad(0\le s\le3/200)}
\tag{6.15}
\]

for every `N=11,12,13,14`. Each polynomial has exactly one root `s_N` in the interval.

Because `D_N` is continuous, is positive at zero and negative at `3/200`, it has a zero. Every zero of `D_N` is a root of `p_N` by (6.9). Since `p_N` has only one root, `D_N` has exactly that one zero. Therefore its sign is positive before the root and negative after it. Combining with (6.4) proves the exact scalar classification

\[
\boxed{\text{fixed-}N\text{ scalar feasibility}\iff0<s<s_N.}
\tag{6.16}
\]

### 6.2 Exact root isolation

Exact rational signs at millionth endpoints give

\[
\boxed{
\begin{array}{c|c}
N&\text{unique }s_N\text{ lies in}\\ \hline
11&(9291/10^6,\ 9292/10^6)\\
12&(14403/10^6,\ 14404/10^6)\\
13&(12636/10^6,\ 12637/10^6)\\
14&(4339/10^6,\ 4340/10^6).
\end{array}}
\tag{6.17}
\]

For orientation only, the numerical roots are approximately

\[
0.0092910998,\quad0.0144035718,\quad0.0126366931,\quad0.0043394569,
\tag{6.18}
\]

but the proof is the exact isolation (6.17), not decimal root finding.

## 7. New restricted theorem

Combining Sections 4--6 gives:

**R15-F0111-N30-SCALAR-ENVELOPE.** Suppose a nonnegative-coefficient quadratic global certificate for the F0111 `k=2` hazard is exact at an interior point in dimension `n=30`, and its contact Hessian has a full-support two-level mixed-sign null direction on the `z>1` cubic-null branch. Orient the direction as in (3.4), put `N=|K|`, `d=delta`, and `s=z-1`. Then necessarily

\[
N\in\{11,12,13,14\},
\tag{7.1}
\]

with the corresponding `d` strip in (5.11), and

\[
0<s<s_N,
\tag{7.2}
\]

where `s_N` is the unique algebraic root in (6.17). In particular every such scalar survivor satisfies

\[
\boxed{0<z-1<\frac{14404}{10^6}=0.014404.}
\tag{7.3}
\]

This theorem is **only a necessary scalar classification**. It does not assert that any point in these four strips is realized by a valid contact. Such a point still has to satisfy the full coefficient nonnegativity, exact value/gradient contact, PSD/projective Gram constraints, and global all-ray majorant inequalities.

The previous run adds a complementary fact: an actual full-system dimension-30 contact sequence cannot have `s->0`. Therefore, if a full-support two-level dimension-30 first bifurcation exists at all, it lies in one of four compact algebraic strips and is separated from both endpoints: qualitatively `eta<=s<s_N` for some positive but still non-effective full-system `eta`. The upper endpoint is now explicit and exact; the lower endpoint is not.

## 8. Validation after the idea, not before it

The analytic route above was recorded **before** any checker in

`artifacts/R15/f0111_n30_scalar_envelope_idea_l97t.md`

at creation commit

`d073a7b3b9e89b8836064f4ffbadc1214946da3c`.

Only then I ran an exact SymPy/rational checker:

- `artifacts/R15/f0111_n30_scalar_envelope_l97t.py`, creation commit `c93ce45dc9e1c11d283661458cc45f4a1ce374a9`;
- archived execution `artifacts/R15/f0111_n30_scalar_envelope_l97t.out`, creation commit `8279a325eb2635a76188976f79c8099f181176b8`.

The executed output ends

`ALL_EXACT_CHECKS_PASS`.

It verifies the scalar identities, all monotonicity reductions, the exact `3/200` positivity certificate, the four integer strips, all four resultants, monotonicity of the degree-nine polynomials, the exact rational root-sign brackets, and the global `0.014404` upper bound. This is a **self-check**, not an independent audit.

No Brownian-law statement is inferred from numerical paths, and no finite grid is used as proof of the F0111 theorem.

## 9. What moved, what did not, and the next mathematical cursor

### Native I0076

No movement. Burdzy--Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`. There is no surviving frozen counterexample candidate and no proof of the full source implication. No deterministic-time substitute, stopping-time strengthening, or Problem-7.5 result was used.

### Retained F0111 screen

Real movement. Before this run, the dimension-30 two-level branch was known to satisfy the coarse scalar condition `Q_K<29`, and the **full system** was known not to accumulate at `z=1`. The remaining scalar region was still two-dimensional and non-explicit.

After this run:

- `N` is exactly one of `11,12,13,14`;
- each `N` has an explicit rational `delta` strip;
- for each `N`, scalar feasibility is exactly `0<s<s_N`, where `s_N` is the unique root of an explicit degree-nine integer polynomial;
- all roots are isolated by exact millionth brackets;
- globally, `z<1.014404`.

The next high-value attack is therefore no longer an unrestricted `(delta,z)` search. There are four narrow semialgebraic/algebraic cells. The best next move is to take each cell separately and add **one genuinely non-scalar constraint**—preferably exact value contact plus the residual Gram/projective inequalities, or the exact all-ray majorant cone—and prove that its feasible set is empty. Because the `N=14` scalar interval already ends below `0.004340`, it is the natural first cell for an effective full-system exclusion.

A second route is to derive an `n`-dependent version of the same collision algorithm for `n>=31`, looking for a stronger uniform dimension barrier.

This remains far from Talagrand Problem 10.9: non-two-level null directions, null directions with zero coordinates, the second-contact mechanism, higher `k`, and the full universal quantifiers remain untouched.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  actual_model: "GPT-5.6 Sol"
  reasoning_level: "UNVERIFIED; not GPT-6 maximum"
  native_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
  native_metric_name: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "RETIRED_HANDOFF; do not restart or fabricate a fresh streak"
  native_remaining_obligation: "a future reassignment needs either a new frozen candidate satisfying all four exact source obligations or a proof of the full source implication, with no stopping-time strengthening"
  free_ready_closable_before: 0
  free_ready_closable_after: 0
  retained_screen: "Talagrand F0111 k=2; PENDING / SELF_CHECK_ONLY / NOT CLAIMED"
  retained_aux_metric: "exact scalar feasibility envelope for n=30 full-support two-level Hessian-null branch"
  retained_aux_before: "Q_K<29 plus qualitative full-system exclusion of z->1; no exact branchwise scalar cutoff"
  retained_aux_after: "N in {11,12,13,14}; four exact delta strips; fixed-N feasibility iff 0<s<s_N with explicit degree-nine p_N; global s<0.014404"
  tried_moves:
    - "4 PROVE SOMETHING WEAKER, COMPLETELY"
    - "19 MAKE IT AN ALGORITHM"
    - "30 DO ONE PRIME, ONE SCALE, ONE DIRECTION AT A TIME"
  remaining_obligation: "eliminate or realize the four n=30 scalar cells using a non-scalar full-contact/global constraint; then extend beyond full-support two-level Hessian-null directions and separately handle second-contact mechanisms"
  evidence:
    idea_commit: "d073a7b3b9e89b8836064f4ffbadc1214946da3c"
    checker_commit: "c93ce45dc9e1c11d283661458cc45f4a1ce374a9"
    checker_output_commit: "8279a325eb2635a76188976f79c8099f181176b8"
  audit_ids: []
  audit_status: "SELF_CHECK_ONLY; no independent audit requested or counted"
```

## 11. Model / scheduler / denied-task boundary

The platform limitation remains unchanged in the exposed task surface and in the operative implementation record. The available task controls cover prompt/title, schedule/timing, enabled state and ordinary updates. They do **not** expose a binding model-family selector, a reasoning-effort selector, an authenticated applied-model/effort receipt, or a guaranteed hour-long execution field. GPT-6 / maximum therefore remains prompt-only here.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in one authorization context. Root `RESULTS.md` and `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` record that a later full P26 update succeeded from an authorized P/C context. The compliant workaround for an edit-denied task is therefore the owning/authorized workspace/account/API/admin context or platform support—not a permission bypass or a duplicate schedule. A real GPT-6/maximum guarantee requires a supported scheduler/product/backend/API surface that exposes, persists and attests those routing controls.
