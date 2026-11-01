Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **NO MOVEMENT in the fixed upper envelope** `B_R13(86)=728143/100000=7.28143` (fixed-upper unchanged count `0 -> 1`), but the **explicit finite obstruction moved** `K_86^* >= 2259253/10^6 = 2.259253 -> K_86^* >= 225925611947/10^11 = 2.25925611947`; methods actually used: **#9 RANDOMIZE, #2 ATTACK THE NEGATION FIRST, #4 PROVE SOMETHING WEAKER COMPLETELY.**

# R13 — Boolean Komlós: a failed energy-only random-sign route and an almost closed 86-leaf balanced-tree obstruction

Run ID: `20260919T1129Z_balanced86-primaldual-91b4`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R13  
Lane: **HARD OUTSIDE**

## 1. Continuity, source status, ownership, and metric state

I continued from the newest immutable R13 report

`runs/R13/20260919T1100Z_mixed-bsb-coverdual-a83f.md`

rather than from the older 10:01 report or from the original source. The 11:00 report is the controlling predecessor: it moved the finite-dimensional upper anchor to

\[
\boxed{K_{86}^*\le \frac{728143}{100000}=7.28143}
\]

and retained the balanced-tree lower obstruction

\[
K_{86}^*\ge \frac{2259253}{10^6}=2.259253.
\]

Before new mathematics I reread/reconciled the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current I0091 source-resolution reconciliation, the newest R13 report/checker chain, and neighboring discrepancy work including the newest R02 report. I also checked the current intake/ownership surfaces rather than treating stale `open_per_source` metadata as current status. Boolean Komlós remains the R13 quantitative track and is not a free READY reserve target. I did not edit shared roots or peer-track files.

The qualitative source question is **KNOWN / RESOLVED_IN_2026_PREPRINT_LITERATURE**, not open. Current primary-source status checked for this run:

- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189, submitted 10 September 2026, prove the genuine real-sign dimension-free bound `3 sqrt(2 pi)`;
- Karingula--Lovett, ECCC TR26-188, 17 September 2026, give an independent elementary real-sign bound `36`;
- Akbas--Sra, arXiv:2609.20785, submitted 17 September 2026, obtain Boolean small-ball inequalities and recover Komlós;
- Bansal--Jiang, arXiv:2508.03961v2, remains the earlier real-Boolean `\widetilde O((log n)^{1/4})` comparison source;
- Kunisky, SIAM J. Discrete Math. 37 (2023), arXiv:2111.02974, gives the unsatisfiable-matrix / read-once-resolution lower-obstruction framework used by the finite construction below and already discusses optimizing fixed formulas by a convex program / dual certificate.

Accordingly this report makes **no qualitative solution claim** and does not claim the general convex duality below as new. R13's object remains the finite-dimensional real-Boolean constant

\[
K_n^*:=\sup_{m\ge1}\sup_{\substack{A\in\mathbb R^{m\times n}\\\|A_{\cdot j}\|_2\le1}}
\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty.
\]

The immediately preceding Section-B triple was `#23/#22/#26`. This run uses the distinct triple `#9/#2/#4`.

## 2. Method #9 — RANDOMIZE: an energy-only random-sign bound and why it fails here

I first tried to leave the directional-TV machinery completely and ask whether the Frobenius budget alone makes a uniform random signing competitive at the finite source dimension.

Let `A` be any real `m x n` unit-column matrix and write its rows as `r_i`, with

\[
a_i:=\|r_i\|_2,\qquad \sum_i a_i^2=\|A\|_F^2\le n.
\tag{2.1}
\]

For independent uniform signs `epsilon_j`, Hoeffding's inequality gives for every row with `a_i>0`

\[
\Pr\{|r_i\cdot\varepsilon|\ge h\}
\le 2\exp\left(-\frac{h^2}{2a_i^2}\right).
\tag{2.2}
\]

Put `c=h^2/2` and `x=a_i^2`. Since with `y=c/x`

\[
\frac{2e^{-c/x}}{x}
=\frac{2}{c}ye^{-y}
\le\frac{2}{ec}
=\frac{4}{e h^2},
\]

we have the useful rowwise linearization

\[
2e^{-h^2/(2a_i^2)}
\le \frac{4a_i^2}{e h^2}.
\tag{2.3}
\]

Summing (2.3) and using (2.1),

\[
\Pr\left\{\max_i|r_i\cdot\varepsilon|\ge h\right\}
\le\frac{4n}{e h^2}.
\tag{2.4}
\]

Therefore for every `h>2 sqrt(n/e)` the right side is strictly below one, so some Boolean signing has infinity norm below `h`. Taking the infimum over such `h` gives the valid universal finite-dimensional bound

\[
\boxed{K_n^*\le2\sqrt{n/e}.}
\tag{2.5}
\]

This is a complete theorem, but it is useless for the current metric: at `n=86`, even the crude inequality `e<3` gives

\[
2\sqrt{86/e}>2\sqrt{86/3}>10,
\]

far above `7.28143`. I also examined the exact Rademacher mgf rather than Hoeffding as route scouting; the same energy-only union-bound strategy still did not approach the retained finite-dimensional certificate, so I stopped rather than build a checker for a noncompetitive constant.

**Outcome #9:** a clean alternative universal bound, but a substantive failure for R13's fixed envelope. It identifies the obstruction precisely: controlling rows only through `sum_i ||r_i||_2^2` and then union-bounding loses too much at `n=86`.

## 3. Methods #2 and #4 — attack the balanced-tree obstruction's claimed improvability, then solve that fixed mechanism almost completely

The strongest same-dimension finite lower construction in R13 is the balanced 86-leaf read-once tree from

`runs/R13/20260919T0833Z_balanced86-rational-e21c.md`.

Its combinatorics are fixed:

- recursively split a node with `s` leaves into `floor(s/2)` and `ceil(s/2)` leaves;
- there are 86 leaves, 85 internal nodes, and one CNF-to-NAE dummy column, hence 86 columns;
- exactly 42 leaves have depth 6 and 44 leaves have depth 7;
- each leaf gives one signed row support consisting of the dummy plus the internal vertices on its root-to-leaf path.

Distinct leaves diverge at an internal vertex, hence their projective full-alignment cylinders are disjoint. Their total projective mass is

\[
42\,2^{-6}+44\,2^{-7}=1.
\tag{3.1}
\]

Thus they partition the projective Boolean cube: every signing aligns, up to global sign, with exactly one row template. This means that once every row is given common `l1` mass `q` under the unit-column constraints, the resulting matrix proves `K_86^*>=q`.

### 3.1 The fixed-support minimax problem

Normalize every row to `l1` mass one. For row supports `S_i`, define

\[
L_*:=
\min_{\substack{\alpha_{ij}\ge0\\
\sum_{j\in S_i}\alpha_{ij}\ge1}}
\max_{1\le j\le86}
\sum_{i:j\in S_i}\alpha_{ij}^2.
\tag{3.2}
\]

The largest common row mass achievable by this **fixed support family** is

\[
q_{\rm tree}^*=L_*^{-1/2}.
\tag{3.3}
\]

For any positive simplex point `mu_j>0`, `sum_j mu_j=1`, Cauchy--Schwarz gives rowwise

\[
\min_{\substack{\alpha_j\ge0\\\sum_{j\in S}\alpha_j=1}}
\sum_{j\in S}\mu_j\alpha_j^2
=
\left(\sum_{j\in S}\mu_j^{-1}\right)^{-1},
\tag{3.4}
\]

with equality at `alpha_j proportional to 1/mu_j`. Consequently the dual functional

\[
D(\mu):=
\sum_i
\left(\sum_{j\in S_i}\mu_j^{-1}\right)^{-1}
\tag{3.5}
\]

satisfies

\[
D(\mu)\le L_*.
\tag{3.6}
\]

The epigraph primal is convex and has a strict feasible point, so the familiar SOCP/convex-duality argument actually gives equality after maximizing (3.5); for the present theorem I need only the certified weak-dual direction (3.6). This is an instance of the fixed-formula scaling optimization already present in Kunisky's framework, not a novelty claim about convex duality.

### 3.2 #2 ATTACK THE NEGATION FIRST — refute a stronger target for this mechanism

The preceding rational certificate had common mass `2.259253`, leaving open the possibility that repeated amplitude tuning might produce a noticeably larger number on exactly the same balanced-tree supports.

I attacked that stronger possibility directly. Define

\[
q_+:=\frac{225925612084}{10^{11}}
=2.25925612084.
\tag{3.7}
\]

The exact checker supplies positive rational dual weights `mu_j` from the 25 orbit weights listed in Section 3.4 below and proves

\[
D(\mu)>\frac1{q_+^2}.
\tag{3.8}
\]

Combining (3.6) and (3.8),

\[
L_*>\frac1{q_+^2},
\qquad
\boxed{q_{\rm tree}^*<q_+=2.25925612084.}
\tag{3.9}
\]

So the explicit stronger claim “the same 86-leaf balanced-tree support pattern can be scaled to common row mass at least `2.25925612084`” is **refuted exactly**. This does **not** upper-bound the true `K_86^*`; it upper-bounds only this fixed support/common-row-mass mechanism.

**Outcome #2:** success as an obstruction-to-the-obstruction theorem. Merely adding more digits to the old weights cannot cross (3.7).

### 3.3 #4 PROVE SOMETHING WEAKER, COMPLETELY — a near-optimal fixed-support certificate and a stronger global lower obstruction

Now define

\[
q_-:=\frac{225925611947}{10^{11}}
=2.25925611947.
\tag{3.10}
\]

For the positive integer orbit weights `W_j` in Section 3.4, set on every row support `S_i`

\[
\alpha_{ij}
=
\frac{W_j^{-1}}{\sum_{k\in S_i}W_k^{-1}}.
\tag{3.11}
\]

Every row has normalized `l1` mass exactly one. Let

\[
L_{\rm pr}:=\max_j\sum_i\alpha_{ij}^2.
\tag{3.12}
\]

The exact checker proves

\[
q_-^2L_{\rm pr}<1,
\tag{3.13}
\]

with scaled worst-column squared norm

\[
0.9999999999918195311023173509699792879\ldots<1.
\tag{3.14}
\]

Therefore scaling every entry by `q_-` gives an admissible real 86-column matrix with every row `l1` mass exactly `q_-`. By the exact projective partition (3.1), every Boolean signing fully aligns with one row, hence

\[
\boxed{K_{86}^*\ge q_-
=\frac{225925611947}{10^{11}}
=2.25925611947.}
\tag{3.15}
\]

Relative to the preceding certificate this is exact movement

\[
\frac{225925611947}{10^{11}}-
\frac{2259253}{10^6}
=\boxed{0.00000311947}.
\tag{3.16}
\]

Combining the primal and dual certificates gives an almost complete solution of the **fixed support scaling problem**:

\[
\boxed{
2.25925611947
\le q_{\rm tree}^*
<2.25925612084,}
\tag{3.17}
\]

an interval of width

\[
\boxed{1.37\times10^{-9}}.
\tag{3.18}
\]

This is the reason to stop scalar retuning of this particular support pattern. A materially stronger lower obstruction must change the projective cover / support combinatorics, not only the orbit magnitudes.

**Outcome #4:** success. The weaker fixed-support problem is essentially closed numerically with rigorous rational endpoints, and its lower endpoint moves the genuine global finite obstruction.

### 3.4 Exact 25-orbit rational certificate

Columns in each orbit below receive the displayed positive integer `W_j`:

```text
(0,1):4857310000
(2,44):3434636839
(3,45):2440008214
(4,46):1735452915
(5,9,47,51):1227150525
(6,10,48,52):876677743
(7,11,49,53):858681865
(8,12,50,54):598368377
(13,55):1715180242
(14,56):1222221961
(15,57):873156772
(16,58):855233170
(17,59):595965170
(18,60):1203335672
(19,21,61,63):850886814
(20,22,62,64):592936433
(23,65):2417248464
(24,34,66,76):1709252781
(25,35,67,77):1217998106
(26,36,68,78):870139244
(27,37,69,79):852277584
(28,38,70,80):593905585
(29,39,71,81):1199177086
(30,32,40,42,72,74,82,84):847946249
(31,33,41,43,73,75,83,85):590887314
```

For the primal use (3.11). For the dual use

\[
\mu_j=\frac{W_j}{\sum_{k=1}^{86}W_k}.
\tag{3.19}
\]

The exact output records

\[
L_{\rm pr}
=0.1959156211349754493787525574629690399\ldots,
\]

\[
D(\mu)
=0.1959156208993490119260770002750741490\ldots,
\]

and verifies the acceptance inequalities (3.8) and (3.13) with rational arithmetic. The displayed decimals are diagnostics only.

## 4. Complete fixed upper envelope — unchanged

The fixed upper metric does **not** move in this run. It remains exactly the predecessor's complete rigorously certified real-Boolean envelope. Define

\[
T_5=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\tag{4.1}
\]

The oldest retained Guo--Fang--Lu row-pruning branch is

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\qquad
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]

\[
\delta_D=2[1-(1-p_D)^D],
\qquad
G_0(n)=\max\left\{\frac{7507}{1000},
3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\}.
\tag{4.2}
\]

The retained one-threshold refinement is

\[
D_*(n)=\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]

\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]

\[
H(n)=\max\left\{\frac{148709}{20000},
3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\tag{4.3}
\]

For the retained three-threshold upper-tail branch, with `c_{ell,D}^{(3)}` the exact coefficients of the three-threshold occupancy polynomial defined in the immutable predecessor chain,

\[
\beta_D^{\uparrow,3}
=\frac12\sum_{\ell=1}^Dc_{\ell,D}^{(3)}
\left[
\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}
\right],
\tag{4.4}
\]

\[
D_9(n)=\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1,
\]

\[
J(n)=\max\left\{\frac{740179}{100000},
\frac{27\sqrt{10\pi}}{20}
(1-\beta_{D_9(n)}^{\uparrow,3})\right\}.
\tag{4.5}
\]

The four retained lower-tail refinements have, for integer `D>=135`,

\[
C_D^-=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,-}),
\quad
L_-(n)=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\},
\tag{4.6}
\]

and for `r=2,3,4`,

\[
C_D^{(r)}=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,r}),
\quad
L_r(n)=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{C_D^{(r)},\frac n{\sqrt{D+1}}\right\}.
\tag{4.7}
\]

Here every `beta^{downarrow,*}` is exactly the certified conditional lower-tail functional, including its failed-threshold `0` convention, from the immutable reports that introduced `L_-`, `L_2`, `L_3`, and `L_4`; none is changed or weakened here.

For the five-threshold occupancy/Cantelli branch, for `k=1,...,5`,

\[
A_{k,D}=
\frac{5}{7(4437/5000)}
\left(1-\frac{2k}{5D}\right)
\left(\frac{2k}{5}\right)^{7/5}D^{-2/5},
\quad a_k=A_{k,D}/D,
\]

`a_0=0`, `d_k=a_k-a_{k-1}`, and

\[
F_{1,0}=1,
\qquad
F_{k,r}=\sum_{s=0}^rF_{k-1,r-s}\frac{d_k^s}{s!}
\quad(k=2,\ldots,5;\ 0\le r\le k-1).
\tag{4.8}
\]

The complement polynomial and upper-tail coefficients are

\[
C_{D,5}(x)=
\sum_{r=0}^4\frac{D!}{(D-r)!}F_{5,r}x^r(1-a_5x)^{D-r},
\]

\[
1-C_{D,5}(x)=\sum_{\ell=1}^Dc_{\ell,D}^{(5)}x^\ell,
\]

\[
\beta_{D,5}^{\uparrow}
=\frac12\sum_{\ell=1}^Dc_{\ell,D}^{(5)}
\left[
\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}
\right].
\tag{4.9}
\]

Let `beta_{D,5}^{downarrow}` be the exact truncated-`U=157/20`, four-shell, two-moment Cantelli functional from the immutable report `runs/R13/20260918T2334Z_cantelli-cascade-c4a7.md`, with zero contribution when its certified residual threshold does not exceed the certified conditional-mean upper bound. Then

\[
C_D^{(5)}=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_{D,5}^{\uparrow}-\beta_{D,5}^{\downarrow}),
\]

\[
L_5(n)=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{C_D^{(5)},\frac n{\sqrt{D+1}}\right\}.
\tag{4.10}
\]

The retained continuous Laplace branch is

\[
L_{\rm LT}(n)=
\max\left\{\frac{739097}{100000},\frac n{\sqrt{136}}\right\}.
\tag{4.11}
\]

Finally the current finite-`D`, `p=33/20` tilted-transform branch is

\[
L_{33/20}^{\rm tight}(n)=
\max\left\{\frac{728143}{100000},\frac n{\sqrt{140}}\right\}.
\tag{4.12}
\]

With all coefficient definitions, conditional threshold conventions, integer restrictions and predecessor constants in (4.2)--(4.12) retained exactly, the complete current upper envelope is

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{\rm LT}(n),L_{33/20}^{\rm tight}(n)\},&5\le n\le85,\\[2mm]
\min\{G_0(n),H(n),J(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{\rm LT}(n),L_{33/20}^{\rm tight}(n)\},&n\ge86.
\end{cases}}
\tag{4.13}
\]

In particular

\[
\boxed{B_{R13}(86)=\frac{728143}{100000}=7.28143}
\]

is unchanged, so the fixed-upper unchanged count is `1`. The continuation condition is nevertheless satisfied because the explicit finite obstruction (3.15) moved.

## 5. Current same-dimension interval and propagated lower branch

Combining (3.15) with the unchanged upper theorem,

\[
\boxed{
2.25925611947
\le K_{86}^*
\le 7.28143.}
\tag{5.1}
\]

Kunisky's doubling construction still propagates the improved lower endpoint. Put

\[
q_0=\frac{225925611947}{10^{11}},
\qquad
q_{r+1}=\frac{1+q_r}{\sqrt2}.
\tag{5.2}
\]

Then for every integer `r>=0`,

\[
K_{86\cdot2^r}^*\ge q_r,
\]

and zero-padding gives the same lower bound for every larger `n`. Equivalently

\[
q_r=(1+\sqrt2)+2^{-r/2}
\left(q_0-(1+\sqrt2)\right).
\tag{5.3}
\]

No claim is made that this propagated branch is globally optimal.

## 6. Prior-art / novelty check

The relevant prior lower-bound mechanism is not folklore accidentally rediscovered: Kunisky's published 2023 paper explicitly develops unsatisfiable matrices from resolution constructions, proves power-of-two lower bounds approaching `1+sqrt(2)`, and discusses optimizing a fixed unsatisfiable support pattern through convex optimization / duality. That is why this report claims neither the tree mechanism nor the primal/dual scaling formalism as new.

A bounded fresh search for the exact decimal `2.259256...`, the 86-leaf balanced support, and the particular rational orbit certificate above did not locate a matching published finite-86 certificate. This is only negative search evidence. **Novelty of the finite-86 sharpening remains UNVERIFIED.**

The qualitative current-source status remains external-literature KNOWN; the new claim here is only the finite quantitative obstruction (3.15) and the fixed-support interval (3.17).

## 7. Exact self-check and immutable artifacts

The exact checker is

`artifacts/R13/20260919T1129Z_balanced86-primaldual-91b4_checker.py`

created at commit

`a17e477813943eb5dac26569fbc96c6ec674da9c`

and read back at that exact commit.

The archived checker output is

`artifacts/R13/20260919T1129Z_balanced86-primaldual-91b4.out`

created at commit

`4b28727fa5ee28f68fe89c4f20ac3c25b2bea9c3`

and read back at that exact commit. It ends with the PASS sentinel

`R13_BALANCED86_PRIMAL_DUAL_EXACT_PASS`.

The checker uses only exact integer / `Fraction` arithmetic for all acceptance decisions. It verifies:

- 86 rows and 86 columns;
- depth distribution `{6:42,7:44}`;
- pairwise projective incompatibility and Kraft sum exactly one;
- exact normalized row masses;
- `q_-^2 L_pr<1` for every column;
- the movement `q_->2.259253`;
- the exact dual identity for the supplied `mu`;
- `D(mu)>1/q_+^2`;
- hence the fixed-support bracket (3.17).

The smallest reported scaled primal slack is approximately `8.18e-12`; the dual margin over `1/q_+^2` is approximately `3.75e-13`. Those decimals are diagnostic only; the assertions are rational.

## 8. What this run rules out and what remains

The balanced-tree amplitude route is now effectively saturated: its rigorously certified fixed-support interval is only `1.37e-9` wide. The next useful lower-bound attack must alter the support/cylinder cover, rather than re-optimize these 25 orbit weights.

The upper side did not move. The random-sign / energy-only route in Section 2 explains why one very different probabilistic approach is too weak. A future upper movement needs information beyond the total Frobenius budget — for example a genuinely better nonproduct DTV density, an explicit finite-constant extraction from Boolean small-ball machinery, or a new small-column theorem strong enough to improve a compiler branch. Since the fixed-upper unchanged count is only `1`, the Section-I stuck protocol is not yet triggered.

## 9. Model / scheduler control truthfulness

The exposed task-control surface still provides task title/prompt, schedule/timing, enabled state, and update/list controls, but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry**. Therefore `GPT-6 / maximum` remains prompt text only on this surface. This run is GPT-5.6 Sol with reasoning level UNVERIFIED, and I do not claim otherwise.

To make the owner request enforceable, the product/backend or an authorized workspace/admin surface would have to expose persisted model-family and reasoning-effort fields and return authenticated applied-runtime metadata for each completed run. That control is not exposed here.

The historical P26 `You cannot modify this task` result is authorization-context dependent; repository history records a later successful in-place P26 update from an authorized context. The lawful workaround is therefore the owning/authorized task surface or platform support, not duplicating the task or bypassing permissions. No scheduler, permission, workflow, email, Drive, purchase, or public-posting action was made in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R13
  lane: HARD_OUTSIDE
  canonical_intake_alias: I0091
  source_target: real Boolean Komlos signing
  source_qualitative_status: KNOWN_IN_2026_PREPRINT_LITERATURE
  quantitative_track_status: PARTIAL
  fixed_metric: complete universal real-Boolean upper envelope B_R13(n)
  fixed_anchor_n: 86
  fixed_upper_before: "728143/100000 = 7.28143"
  fixed_upper_after: "728143/100000 = 7.28143"
  fixed_upper_movement: false
  fixed_upper_unchanged_count_before: 0
  fixed_upper_unchanged_count_after: 1
  explicit_finite_obstruction_n86_before: "2259253/1000000 = 2.259253"
  explicit_finite_obstruction_n86_after: "225925611947/100000000000 = 2.25925611947"
  explicit_finite_obstruction_movement: "0.00000311947"
  fixed_balanced_tree_scaling_interval:
    lower: "225925611947/100000000000 = 2.25925611947"
    upper_strict: "225925612084/100000000000 = 2.25925612084"
    width: "1.37e-9"
    global_K86_upper_bound: false
  same_dimension_interval_K86:
    lower: "2.25925611947"
    upper: "7.28143"
  methods: [9, 2, 4]
  method_outcomes:
    9: "universal K_n^* <= 2 sqrt(n/e), complete but noncompetitive"
    2: "exactly refuted q_tree >= 2.25925612084 for the fixed balanced-tree support mechanism"
    4: "certified near-optimal fixed-support scaling and moved global K86 lower obstruction"
  checker: "artifacts/R13/20260919T1129Z_balanced86-primaldual-91b4_checker.py"
  checker_commit: "a17e477813943eb5dac26569fbc96c6ec674da9c"
  output: "artifacts/R13/20260919T1129Z_balanced86-primaldual-91b4.out"
  output_commit: "4b28727fa5ee28f68fe89c4f20ac3c25b2bea9c3"
  self_check: PASS
  outside_audits_of_new_sharpening: "0/2"
  novelty: UNVERIFIED
  shared_root_edits: false
  peer_file_edits: false
  scheduler_changes: false
  remaining_obligation: "Move B_R13(n) with a genuinely different upper route, or change the finite lower support/cylinder combinatorics; do not continue scalar tuning of the saturated 86-leaf balanced support."
```
