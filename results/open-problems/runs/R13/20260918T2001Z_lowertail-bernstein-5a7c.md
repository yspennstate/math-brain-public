Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** `B_R13(86)` improves from `740179/100000 = 7.40179` to `<= 185022/25000 = 7.40088`, an exact certified decrease of at least `91/100000 = 0.00091`; the complete pointwise envelope is strengthened by the new lower-tail branch `L_-(n)` defined below. Methods actually used: **#8 GO THE OTHER WAY AND DISCRETIZE, #20 FIND WHY THE ALGORITHM FAILS, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R13 — lower-tail Bernstein correction to the finite-dimensional DTV Komlós bound

Run ID: `20260918T2001Z_lowertail-bernstein-5a7c`  
Repository/branch: private `yspennstate/math-open-problems` / `master`.

R13 remains the HARD OUTSIDE owner of the real Boolean Komlós target `E0042`.  For a real `m x n` matrix `A` with every column of Euclidean norm at most one, write

\[
\operatorname{disc}(A)
=\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty,
\qquad
K_n^*=\sup_A\operatorname{disc}(A).
\]

The fixed metric is the **complete rigorously certified pointwise upper envelope**
`B_R13(n)`.  Complex phases, vector/rank-two colorings, and average-case
statements are not substitutes.

Before new mathematics I reread/recovered the required campaign state:
`probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`,
root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`,
the `E0042` intake record, the newest complete R13 report
`runs/R13/20260918T1834Z_cospower-3threshold-c9e4.md`, and current neighboring
sign-matrix-discrepancy ownership/status.  The 18 September R02 reconciliation
still treats `I0095` as a distinct sign-matrix source and does not reopen it as
a competing Komlós assignment.  No shared root, claim, peer file, scheduler,
email, Drive item, public page, permission, or workflow was changed.

All thirty Section-B labels had already appeared somewhere in R13 history by
the 17 September six-column report, so the literal requirement to choose three
labels never before used on this problem is no longer satisfiable.  I therefore
follow the stronger operational requirement that matters now: do not repeat the
preceding triple (`#6,#15,#25`) and use three genuinely different attacks.  The
three used here are `#8,#20,#23`.

## 1. Fresh source and prior-art check — 18 September 2026

The original source remains Bandeira's Open Problem 0.1 / intake `E0042`.

* N. Bansal and H. Jiang, arXiv:2508.03961 (current repository navigation v2),
  give the earlier real-Boolean \(\widetilde O((\log n)^{1/4})\) Komlós bound.
  Their 2026 exposition is arXiv:2608.28452.
* S. Guo, E. X. Fang and J. Lu, arXiv:2609.11189v1, submitted
  **10 September 2026**, state the genuine real-Boolean theorem
  \[
  K_n^*<3\sqrt{2\pi}
  \]
  uniformly in `m,n`.  Their Proposition 2.2 / Corollary 2.3 is the
  directional-total-variation signing criterion and Lemma 2.4 supplies the
  product `cos^2` cube density.  Their Remark 2.5 says only that the
  \(\sqrt{2\pi}\) coefficient is asymptotically sharp for that **fixed**
  product family; it does not assert optimality among all cube densities.
* The complex-phase/rank-two results remain outside the Boolean target.

Current links:
- https://arxiv.org/abs/2508.03961
- https://arxiv.org/abs/2608.28452
- https://arxiv.org/abs/2609.11189

I also checked the standard continuous gamma bounds used below.  The
Encyclopedia of Mathematics records both the continuous Stirling form and
Sonin's sharper form
\[
\Gamma(1+x)=\sqrt{2\pi}\,x^{x+1/2}
\exp\!\left(-x+\frac1{12(x+\theta)}\right),
\qquad 0<\theta<\frac12.
\]
Source:
https://encyclopediaofmath.org/wiki/Gamma-function

Fresh bounded searches for combinations of `Komlos`, `directional total
variation`, `cos^p`, `inverse chi-square`, `Bernstein`, and `lower tail`
returned Guo--Fang--Lu and unrelated inverse-chi-square/statistics material,
but no matching finite-dimensional lower-tail correction of the form proved
below.  This is only bounded negative evidence: **novelty remains UNVERIFIED**.

## 2. Baseline from the preceding R13 run

The exact finite history is retained:

\[
T_5=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13},
\qquad
K_5^*=T_5,
\]

\[
K_6^*\ge1.84535465,\qquad
K_{11}^*\ge1.99488049,\qquad
K_{12}^*\ge2.013108.
\]

The preceding run deformed the Guo--Fang--Lu product density to exponent
\(p=9/5\).  In dimension \(D\), with

\[
S_i\sim\chi^2_{14/5},\qquad
Y_i=\frac4{5S_i},\qquad
X_D=\frac1D\sum_{i=1}^D Y_i,
\]

the worst directional-variation direction is the balanced direction, and

\[
a_D:=\mathbb E\sqrt{X_D}
\]

controls a Boolean signing cube of half-side

\[
C_D=\frac{27\sqrt{10\pi}}{20}\,a_D.
\tag{2.1}
\]

The balanced direction is worst because
\[
w\longmapsto
\mathbb E\sqrt{\sum_i w_iY_i}
\]
is concave and permutation-invariant on the simplex; averaging all coordinate
permutations of `w` gives the uniform vector.

Since \(\mathbb E X_D=1\),

\[
2(1-a_D)=
\mathbb E\bigl(\sqrt{X_D}-1\bigr)^2.
\tag{2.2}
\]

The previous run used only the `X_D>=1` part of (2.2), through the exact
three-threshold event
(one coordinate at least `Dt`, or two at least `Dt/2`, or three at least
`Dt/3`).  Its retained lower bound on the Jensen defect will be denoted
\(\beta_D^\uparrow\).  At `D=135`, the exact rationalized certificate below
gives

\[
\beta_{135}^\uparrow
>0.021737695196183224.
\tag{2.3}
\]

The preceding full metric had

\[
B_{\rm old}(86)=\frac{740179}{100000}=7.40179.
\]

## 3. #23 — use the opposite half of the Jensen defect

The point missed by the previous route is that (2.2) has a **second,
disjoint** source of defect.  Rather than asking only for a large coordinate
which makes \(X_D\ge1\), force a bounded conditional average to fall
strictly below one.

Fix

\[
U=\frac{157}{20}=7.85,\qquad
t=\frac{8183}{10000}=0.8183.
\tag{3.1}
\]

For one inverse-chi-square variable \(Y=4/(5S)\), `Y>U` is exactly

\[
S<\frac{16}{157}.
\]

The \(\chi^2_{14/5}\) density is

\[
f(s)=
\frac{s^{2/5}e^{-s/2}}
     {2^{7/5}\Gamma(7/5)}
\qquad(s>0).
\tag{3.2}
\]

We first need two one-dimensional estimates, one on the truncation
probability and one on the mass removed from the mean.

### 3.1 A rigorous lower bound for the retained probability

From \(e^{-s/2}\le1\),

\[
\Pr(Y>U)
\le
\frac{(8/157)^{7/5}}{\Gamma(12/5)}.
\tag{3.3}
\]

Sonin's formula at \(x=7/5\) gives a correction \(>5/114\).  The exact
rational checks

\[
\left(\frac{207}{200}\right)^{10}>\frac75,
\qquad
e^{773/570}<\frac{1941}{500},
\qquad
\sqrt{2\pi}>\frac{1253}{500}
\]

imply

\[
\Gamma(12/5)>
\frac{491176}{401787}.
\tag{3.4}
\]

The Taylor/geometric-tail proof of the exponential comparison is in the
checker.  Raising (3.3) to the fifth power eliminates all fractional powers;
the checker verifies exactly that

\[
\Pr(Y>U)<\frac{317}{25000}.
\]

Hence

\[
\boxed{
\Pr(Y\le U)>
p_0:=\frac{24683}{25000}=0.98732.
}
\tag{3.5}
\]

### 3.2 The truncation removes a definite part of the mean

On \(0\le s\le16/157\), use \(e^{-s/2}\ge1-s/2\).
A direct integration of \(Y f_S(s)\) gives

\[
\mathbb E[Y;Y>U]
\ge
\frac{1083}{1099\,\Gamma(7/5)}
\left(\frac{64}{24649}\right)^{1/5}.
\tag{3.6}
\]

For the opposite gamma direction, the continuous Stirling upper bound,
together with the already retained exact tenth-root and Taylor comparisons,
gives

\[
\Gamma(7/5)<\frac{88869}{100000}.
\tag{3.7}
\]

The exact fifth-power check then yields

\[
\boxed{
\mathbb E[Y;Y>U]>
\frac{337097}{10^6}.
}
\tag{3.8}
\]

Since \(\mathbb E Y=1\), (3.5)--(3.8) imply

\[
\mathbb E[Y\mid Y\le U]
<
\mu:=
\frac{662903}{987320}
=
0.671416562006\ldots .
\tag{3.9}
\]

## 4. #8 — replace the unbounded law by a bounded conditional core

Let

\[
E_0=\bigcap_{i=1}^D\{Y_i\le U\}.
\]

Because the original variables are independent and `E_0` is a product event,
conditioning on `E_0` leaves the coordinates independent.  Let
\(Z_i\) denote the conditional variables.  Then

\[
0\le Z_i\le U,\qquad
\mathbb E Z_i<\mu.
\]

Also \(Z_i^2\le UZ_i\), so

\[
\operatorname{Var}(Z_i)
\le\mathbb E Z_i^2
\le U\mu.
\tag{4.1}
\]

Put

\[
\Delta=t-\mu>0.
\]

The one-sided Bernstein inequality gives

\[
\Pr\!\left(
\frac1D\sum_{i=1}^D Z_i>t
\right)
\le
\exp(-E_D),
\tag{4.2}
\]

where

\[
E_D=
\frac{D\Delta^2}
     {2U\mu+\frac23U\Delta}.
\tag{4.3}
\]

Therefore

\[
\Pr(X_D\le t)
\ge
p_0^D\bigl(1-e^{-E_D}\bigr).
\tag{4.4}
\]

For a completely rational lower certificate, use

\[
e^{E_D}\ge
1+E_D+\frac{E_D^2}{2}+\frac{E_D^3}{6}.
\]

Define

\[
R_D:=
1-
\frac1{
1+E_D+E_D^2/2+E_D^3/6
}.
\tag{4.5}
\]

Then

\[
\Pr(X_D\le t)\ge p_0^D R_D.
\tag{4.6}
\]

Finally set

\[
q=\frac{477}{5000}=0.0954.
\]

The checker verifies

\[
(1-q)^2-t=\frac{29}{25\,000\,000}>0,
\]

so \(q<1-\sqrt t\).  On \(\{X_D\le t\}\),

\[
(\sqrt{X_D}-1)^2>q^2.
\]

The lower-tail contribution to (2.2) is therefore

\[
\boxed{
\beta_D^\downarrow
:=
\frac{q^2}{2}\,p_0^D R_D.
}
\tag{4.7}
\]

This event lies in `X_D<1`; the old upper-tail integral lies in `X_D>=1`.
They are disjoint, so their contributions **add**:

\[
a_D
\le
1-\beta_D^\uparrow-\beta_D^\downarrow.
\tag{4.8}
\]

This is the conceptual movement of the run.

## 5. General strengthened density branch

For completeness, retain the preceding exact three-threshold definition of
\(\beta_D^\uparrow\).  Put

\[
\bar\Gamma=\frac{88869}{100000},
\]

\[
A_{k,D}=
\frac{5}{7\bar\Gamma}
\left(\frac{2k}{5}\right)^{7/5}
\left(1-\frac{2k}{5D}\right)D^{-2/5},
\qquad k=1,2,3,
\tag{5.1}
\]

and \(a_{k,D}=A_{k,D}/D\).  Define

\[
\begin{aligned}
Q_D(x)=1
&-(1-a_{3,D}x)^D\\
&-D(a_{3,D}-a_{1,D})x(1-a_{3,D}x)^{D-1}\\
&-\binom D2
\Big[(a_{3,D}-a_{2,D})^2
+2(a_{2,D}-a_{1,D})(a_{3,D}-a_{2,D})\Big]
x^2(1-a_{3,D}x)^{D-2}.
\end{aligned}
\tag{5.2}
\]

Write \(Q_D(x)=\sum_{\ell=1}^D c_{\ell,D}x^\ell\).  For \(D\ge135\),

\[
\beta_D^\uparrow
=
\frac12\sum_{\ell=1}^D c_{\ell,D}
\left[
\frac1{7\ell/5-1}
-
\frac1{7\ell/5-1/2}
\right].
\tag{5.3}
\]

Combining (4.7)--(5.3), define

\[
\boxed{
C_D^-=
\frac{27\sqrt{10\pi}}{20}
\left(
1-\beta_D^\uparrow-\beta_D^\downarrow
\right),
\qquad D\ge135.
}
\tag{5.4}
\]

The Guo--Fang--Lu finite-step criterion then gives genuine Boolean signs into
the cube of half-side \(C_D^-\).

There is a useful row-pruning formulation which avoids fixing a threshold in
advance.  For any `n` and integer \(D\ge135\), set

\[
h_D(n)=
\max\left\{
C_D^-,
\frac{n}{\sqrt{D+1}}
\right\}.
\tag{5.5}
\]

Call a row active when its Euclidean norm is \(>h_D(n)/\sqrt n\).  The
Frobenius budget gives

\[
d\,\frac{h_D(n)^2}{n}
<
\sum_i\|r_i\|_2^2
\le n,
\]

hence

\[
d<\frac{n^2}{h_D(n)^2}\le D+1,
\]

and therefore \(d\le D\).  Pad the active-row submatrix by zero rows to
dimension `D` and apply (5.4).  Every inactive row is bounded by
Cauchy--Schwarz.  Thus

\[
\boxed{
K_n^*
\le
L_-(n):=
\inf_{D\in\mathbb Z,\ D\ge135}
\max\left\{
C_D^-,
\frac{n}{\sqrt{D+1}}
\right\}.
}
\tag{5.6}
\]

This is a new source-matching real-Boolean branch; no complex signs appear.

## 6. Exact specialization: \(n=86,D=135\)

The exact checker uses conservative rational lower values

\[
A_{1,135}=\frac{78077}{2500000},\qquad
A_{2,135}=\frac{821737}{10^7},\qquad
A_{3,135}=\frac{36133}{250000}.
\]

It evaluates the entire degree-135 polynomial in exact rational arithmetic and
obtains

\[
\beta_{135}^\uparrow
>0.021737695196183224\ldots .
\]

For the lower-tail part,

\[
E_{135}
=
\frac{106469830750716801}{413434823555991800}
=
0.2575250672765293\ldots ,
\]

\[
R_{135}>0.22692234986849888\ldots ,
\]

\[
p_0^{135}R_{135}
>0.040522705718697684\ldots ,
\]

and consequently

\[
\beta_{135}^\downarrow
>
0.00018440181418939128\ldots .
\]

Thus

\[
\beta_{135}^\uparrow+\beta_{135}^\downarrow
>
0.021922097010372614\ldots .
\]

Using only the rational square-root certificate

\[
\sqrt{10\pi}<\frac{1121}{200},
\]

the checker proves

\[
C_{135}^-
<
7.400870972446763\ldots
<
\boxed{\frac{185022}{25000}=7.40088}.
\tag{6.1}
\]

Now take

\[
h=\frac{185022}{25000}.
\]

For `n=86` the checker proves exactly

\[
135<
\frac{86^2}{h^2}
<
136.
\tag{6.2}
\]

Hence any `86`-column unit-column matrix has at most `135` active rows under
the threshold \(h/\sqrt{86}\).  The active rows are signed using (6.1), and
every inactive row obeys

\[
|r_i\cdot\varepsilon|
\le
\|r_i\|_2\sqrt{86}
\le h.
\]

Therefore

\[
\boxed{
K_{86}^*
\le
\frac{185022}{25000}
=
7.40088.
}
\tag{6.3}
\]

Compared with the preceding certified value,

\[
\frac{740179}{100000}
-
\frac{185022}{25000}
=
\boxed{\frac{91}{100000}}
=
0.00091.
\]

So the fixed metric moved and its stagnation count resets to **0**.

## 7. #20 — exact failure of the obvious continuation

The natural next attempt is "allow one more active row and run the same
certificate at `D=136`."  I tested that exact continuation rather than
assuming it helps.

With rational lower tail coefficients

\[
A_{1,136}=\frac{155697}{5000000},\qquad
A_{2,136}=\frac{16387}{200000},\qquad
A_{3,136}=\frac{288231}{2000000},
\]

the exact same proof gives the certified upper number

\[
C_{136}^{\rm cert}
=
7.4013621701598575\ldots ,
\]

which is **larger** than `7.40088`.  Thus the present
truncation/three-threshold/Bernstein certificate becomes weaker at `D=136`.
This is not an impossibility theorem for a better `D=136` density or sharper
tail analysis; it precisely identifies why simply increasing the active
dimension does not continue the present `n=86` improvement.

## 8. Complete retained pointwise metric

I retain every older valid branch and add \(L_-(n)\); nothing is discarded.

Define

\[
D_0(n)=
\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\qquad
p_D=
\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]

\[
\delta_D=2[1-(1-p_D)^D],
\qquad
G_0(n)=
\max\left\{
\frac{7507}{1000},
3\sqrt{2\pi}(1-\delta_{D_0(n)})
\right\}.
\]

Define

\[
D_*(n)=
\left\lceil
\frac{400000000n^2}{22114366681}
\right\rceil-1,
\]

\[
\alpha_D=
\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=
\frac{\alpha_D}{2(1+\alpha_D)},
\]

\[
H(n)=
\max\left\{
\frac{148709}{20000},
3\sqrt{2\pi}(1-\beta_{D_*(n)})
\right\}.
\]

For the preceding three-threshold cosine-power branch, define

\[
D_9(n)=
\left\lceil
\frac{10^{10}n^2}{547864952041}
\right\rceil-1,
\]

\[
J(n)=
\max\left\{
\frac{740179}{100000},
\frac{27\sqrt{10\pi}}{20}
\left(1-\beta_{D_9(n)}^\uparrow\right)
\right\}.
\]

Then the complete rigorously certified pointwise envelope after this run is

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\min\!\left\{
\sqrt{3n/4},
T_5\sqrt{\lceil n/5\rceil},
G_0(n),
L_-(n)
\right\},
&5\le n\le85,\\[2mm]
\min\!\left\{
G_0(n),H(n),J(n),L_-(n)
\right\},
&n\ge86.
\end{cases}
}
\tag{8.1}
\]

The explicit movement certified in this run is (6.3).  I have **not** claimed
that \(L_-(n)\) beats all old branches in every other dimension; (8.1) takes
the pointwise minimum precisely to preserve that distinction.

## 9. Checker, artifacts, audits, and status

The exact self-check is

`artifacts/R13/20260918T2001Z_lowertail-bernstein-5a7c_checker.py`

created at commit

`9978c70ebab213e5f79ddcd4637f62f28bea02b3`

and read back at that exact commit.

The executed output is

`artifacts/R13/20260918T2001Z_lowertail-bernstein-5a7c_checker.out`

created at commit

`1a8d928ed0b61eb4918e2c80500004f4df9ed68a`

and read back at that exact commit.  It ends

`R13_LOWERTAIL_BERNSTEIN_EXACT_PASS`.

The checker is a **self-check**, not an independent audit.  The new
lower-tail sharpening has **0/2** required outside audits.  The existing
audits of the underlying Guo--Fang--Lu theorem do not count as audits of this
new finite-dimensional branch.

Status:
**PARTIAL QUANTITATIVE / FIXED METRIC MOVED / full written proof /
exact self-check PASS / outside audits 0/2 / novelty UNVERIFIED**.

The next useful route should not be a decimal retuning of `U,t,p`, because the
`D=136` diagnostic already shows diminishing returns in this certificate.
A materially different next attack would either:
1. replace scalar truncation + Bernstein by a two-band or empirical-Bernstein
   lower-tail decomposition;
2. abandon the product family for a symmetric nonproduct cube density; or
3. couple the exact five-column theorem \(K_5^*=T_5\) to the DTV active-row
   reduction through a row-energy decomposition.

## 10. Model / scheduler control status

The exposed scheduler/task-control surface still has no binding model-family
selector and no reasoning-effort selector.  The runtime therefore cannot
authenticate the requested `GPT-6 / maximum`; this run reports the actual
available model label `GPT-5.6 Sol` and reasoning `UNVERIFIED`.

The current repository ledger also records that a historical P26
`You cannot modify this task` error was context-dependent and that a later
full P26 update succeeded from an authorized P/C context.  The legitimate
resolution for any task that still rejects modification is the owning
account/workspace task surface or platform support exposing the control.
Repository edits, duplicate schedules, and permission bypass are not valid
workarounds.  No scheduler modification was attempted in this run.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  run_id: "20260918T2001Z_lowertail-bernstein-5a7c"
  source_id: "E0042"
  source: "Boolean Komlos; Bandeira Open Problem 0.1; Bansal-Jiang arXiv:2508.03961; Guo-Fang-Lu arXiv:2609.11189v1"
  fixed_metric: "complete rigorously certified real-Boolean pointwise upper envelope B_R13(n)"
  before:
    B_R13_86: "740179/100000 = 7.40179"
    stagnation_count: 0
  after:
    B_R13_86: "<=185022/25000 = 7.40088"
    exact_decrease_at_least: "91/100000 = 0.00091"
    new_general_branch: "L_-(n), eq. (5.6)"
    stagnation_count: 0
  movement: "FIXED_METRIC_MOVED"
  methods_actual: [8, 20, 23]
  preceding_methods: [6, 15, 25]
  all_30_methods_historically_represented: true
  status: "PARTIAL QUANTITATIVE"
  boolean_scope: "real signs {-1,+1}; arbitrary row count; column l2 norm <=1"
  self_check: "PASS"
  checker_commit: "9978c70ebab213e5f79ddcd4637f62f28bea02b3"
  output_commit: "1a8d928ed0b61eb4918e2c80500004f4df9ed68a"
  outside_audits_new_claim: "0/2"
  prior_art: "fresh bounded search; no matching lower-tail correction found; novelty UNVERIFIED"
  scheduler_model_selector: "NOT EXPOSED"
  scheduler_reasoning_selector: "NOT EXPOSED"
  actual_model_reported: "GPT-5.6 Sol"
  reasoning: "UNVERIFIED"
  next_route: "two-band lower-tail / symmetric nonproduct density / K5-DTV energy hybrid; no scalar retuning-only run"
```
