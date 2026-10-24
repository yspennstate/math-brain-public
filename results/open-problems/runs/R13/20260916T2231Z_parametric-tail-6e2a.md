Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED**, not verified GPT-6 maximum. **Metric moved on 53 entries:** `B_R13(8): 349/125 -> 27919/10000`, every `B_R13(n)` for `10<=n<=56` improves below `sqrt(n)`, and every `B_R13(n)` for `57<=n<=61` improves below `3 sqrt(2 pi)`. Methods used: **#6 DEFORM TO A POINT YOU CAN SOLVE, #7 TAKE THE LIMIT, #19 MAKE IT AN ALGORITHM**.

# R13 run 11 — parametric Rademacher-tail compiler for finite-column Komlos bounds

Run ID: `20260916T2231Z_parametric-tail-6e2a`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Target and continuity

Target remains the full **real Boolean** Komlós problem: for every deterministic real `m x n` matrix `A` with
`||A_{.j}||_2<=1`, find `epsilon in {-1,+1}^n` with bounded `||A epsilon||_infinity`.

The tracked metric is the complete pointwise rigorously certified upper-bound function `B_R13(n)`, not only an exponent and not a complex/rank-two relaxation.

I continued from

`runs/R13/20260916T2134Z_n8-tailmix-c4d9.md`,

which had
`B_R13(8)=349/125=2.792`, retained exact values through `n=4`, finite upper bounds through `n=8`, the elementary `sqrt(n)` envelope through `n=56`, and the Guo--Fang--Lu constant thereafter. No prior theorem, obstruction, checker or failed route was reset.

At run start I reread the campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, `operations/NEW_METHODS_2026-09-16.md`, the newest R13 report, current R12/R16 directory state, existing R12 Komlós audit, and repository-wide Komlós hits. The intake JSONL corpus is too large for literal connector rendering of every row; I recovered the relevant Komlós ownership/history hits and did not treat an old `admitted=true` flag as current status.

## 2. Current primary-source check — 17 September 2026 (Asia/Jerusalem)

Fresh bounded searches checked:

- Bansal--Jiang, arXiv:2508.03961, current navigation source for the classical Boolean statement and their earlier `tilde O(log^(1/4)n)` Boolean bound;
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 Sep 2026, whose abstract states the full deterministic **real Boolean** theorem with universal bound `<3 sqrt(2 pi)`;
- Guillen--Kobzar, arXiv:2609.15071v1, submitted 14 Sep 2026, whose theorem is unit-modulus complex/rank-two discrepancy, not Boolean signing;
- Bentkus--Dzindzalieta, arXiv:1307.3451 / Bernoulli 21 (2015), for the sharp Gaussian comparison for normalized weighted Rademacher sums;
- Dzindzalieta--Sileikis--Juskevicius, arXiv:1111.6332, Theorem 1, for the exact bounded-random-walk one-sided tail comparison;
- bounded queries combining `Komlos`, `Bentkus`, `Dzindzalieta`, `Rademacher tail`, the exact current constants, and searches for correction/withdrawal/erratum of arXiv:2609.11189.

No later correction or withdrawal of arXiv:2609.11189 was found in this bounded check. The bounded prior-art search did not locate the deterministic finite-column compiler or the table below. **That negative search is not a novelty certificate.**

## 3. Runtime / scheduler interface

The exposed scheduler interface still has **no model field and no reasoning-effort field**. GPT-6/maximum can only be requested in prompt text and is not authenticated runtime telemetry.

There is one correction to earlier operational wording: current root `RESULTS.md` records that in a later authorized P/C context the P26 prompt update *did* succeed, while a separate exposed context denied edits for all R-series IDs. Thus the historical `You cannot modify this task` result is context/ownership-dependent, not evidence that P26 can never be modified. What would be required to set a real GPT-6/maximum runtime is a native scheduler/platform control that exposes model/reasoning fields (or an authorized owner/workspace context that does); prompt text alone cannot do it. A task that still returns a modification denial must be repaired through the authorized owner/workspace interface or platform support, not duplicated or bypassed.

No scheduler mutation was attempted in this run.

## 4. Method #6 — deform the n=8 split into a general finite-n theorem

The previous n=8 argument used two complementary one-row tail estimates. The new move is to make `n` and the threshold `t` parameters and derive the exact criterion under which the same *type* of split gives a deterministic Komlós theorem.

Let
\[
X=\sum_{j=1}^n a_j\varepsilon_j,
\qquad |a_j|\le1,
\qquad S=\sum_{j=1}^n a_j^2.
\]
For `t>0`, set
\[
c=\lfloor t\rfloor+1
\]
(the strict-event ceiling), and define
\[
\ell=
\begin{cases}
n,&c+n\ \text{even},\\
n-1,&c+n\ \text{odd}.
\end{cases}
\]
Because `c` and `ell` have the same parity, define the exact simple-walk tail
\[
q_n(t)
=
2^{-\ell}
\sum_{j=(\ell+c)/2}^\ell
\binom{\ell}{j}.
\tag{4.1}
\]

For noninteger `t`, Theorem 1 of Dzindzalieta--Sileikis--Juskevicius gives directly
\[
\Pr(X>t)\le\Pr(X\ge t)\le q_n(t).
\]
For integer `t=k`, apply their theorem at `k+delta`, `delta>0`, then let `delta downarrow0`; the events increase to `{X>k}` and the simple-walk right side is constant for sufficiently small `delta`. Thus in all cases
\[
\boxed{\Pr(X>t)\le q_n(t).}
\tag{4.2}
\]

Now put
\[
S_0=2nq_n(t),
\qquad
x_0=\frac{t}{\sqrt{S_0}}.
\tag{4.3}
\]

Let
\[
c_*=
\frac1{4\bar\Phi(\sqrt2)}.
\]
Bentkus--Dzindzalieta prove that for a weighted Rademacher sum `Y` with coefficient-square sum at most one,
\[
\Pr(Y\ge x)\le c_*\bar\Phi(x).
\tag{4.4}
\]

### R13-C16 — Parametric mixed-tail compiler

**PROVED.** Suppose
\[
0<S_0<n,
\qquad
x_0>\sqrt2,
\qquad
c_*\bar\Phi(x_0)<q_n(t).
\tag{4.5}
\]
Then for every real `m x n` Komlós matrix,
\[
\boxed{\operatorname{disc}_\infty(A)\le t.}
\tag{4.6}
\]

### Proof

Fix one row `r=(a_1,...,a_n)` and its energy `S`.

If `S=0`, the row spoils no signing.

If `S>S_0`, (4.2) gives
\[
\Pr(X>t)\le q_n(t)=\frac{S_0}{2n}<\frac{S}{2n}.
\tag{4.7}
\]

Assume `0<S<=S_0`. Normalize `Y=X/sqrt(S)`. Then the squared coefficients of `Y` sum to one. Put
\[
x=\frac{t}{\sqrt S}\ge x_0>\sqrt2.
\]
For
\[
f(x)=x^2\bar\Phi(x)
\]
the Mills inequality `barPhi(x)<phi(x)/x` gives
\[
f'(x)
=
2x\bar\Phi(x)-x^2\phi(x)
<
(2-x^2)\phi(x)<0
\qquad(x>\sqrt2).
\tag{4.8}
\]
Therefore
\[
x^2\bar\Phi(x)
\le
x_0^2\bar\Phi(x_0).
\]
Using (4.4) and (4.5),
\[
\begin{aligned}
\Pr(X>t)
&\le c_*\bar\Phi(x)\\
&\le
\frac{c_*x_0^2\bar\Phi(x_0)}{x^2}\\
&<
\frac{x_0^2q_n(t)}{x^2}
=
\frac{S}{2n},
\end{aligned}
\tag{4.9}
\]
because `x_0^2=t^2/(2n q_n(t))` and `x^2=t^2/S`.

Thus for **every** row
\[
\boxed{\Pr_\varepsilon(X>t)<\frac{S}{2n}.}
\tag{4.10}
\]

Let `b(r)` be the number of antipodal Boolean sign classes `{epsilon,-epsilon}` for which the row is bad:
\[
|r\cdot\varepsilon|>t.
\]
Every bad class has exactly one representative with `r dot epsilon>t`, hence
\[
b(r)=2^n\Pr(X>t)
<
\frac{2^{n-1}}{n}S.
\tag{4.11}
\]

For the rows `r_i` of `A`,
\[
\begin{aligned}
\sum_i b(r_i)
&<
\frac{2^{n-1}}{n}
\sum_i\|r_i\|_2^2\\
&=
\frac{2^{n-1}}{n}
\sum_{j=1}^n\|A_{\cdot j}\|_2^2
\le2^{n-1}.
\end{aligned}
\tag{4.12}
\]
There are exactly `2^(n-1)` antipodal sign classes. If every class were bad in at least one row, the incidence sum would be at least `2^(n-1)`, contradicting (4.12). Hence one class is good in every row, proving (4.6). `QED`

This is a deterministic arbitrary-row theorem. The randomness is only a counting device over the finite Boolean sign cube; no random input matrix is substituted for the worst-case matrix.

## 5. Method #19 — compile exact rational thresholds

I used C16 as an explicit finite algorithm:

1. choose rational `t`;
2. compute the exact binomial rational `q_n(t)`;
3. compute `S_0=2nq`;
4. certify `x_0>sqrt(2)`;
5. certify `c_* barPhi(x_0)<q` by rational interval arithmetic;
6. retain `t` only if it beats the previous R13 pointwise envelope.

The exact checker proves
\[
c_*<\frac{158933}{50000}=3.17866
\]
using Machin bounds for `pi`, rational brackets for `(2pi)^(-1/2)` and `sqrt(2)`, and alternating series. For every table entry it chooses a rational `x_L<x_0`, verifies `x_L^2>2` exactly, obtains a rational upper bound on `barPhi(x_L)`, and checks
\[
\frac{158933}{50000}\bar\Phi(x_L)<q_n(t)
\]
with exact rational arithmetic. The smallest certified margin occurs at `n=59` and is still positive.

The checker also verifies each threshold is strictly below the **previous** R13 envelope: below `349/125` for `n=8`, below `sqrt(n)` for `10<=n<=56`, and below `3sqrt(2pi)` for `57<=n<=61`.

## 6. New complete certified upper-bound function

Retained small-column values:
\[
B_{R13}(1)=1,\quad
B_{R13}(2)=\sqrt2,\quad
B_{R13}(3)=\frac{\sqrt{11}+\sqrt2}3,\quad
B_{R13}(4)=\sqrt3,
\]
with these four retained as exact values from earlier R13 work, and
\[
B_{R13}(5)=2,\quad
B_{R13}(6)=\frac3{\sqrt2},\quad
B_{R13}(7)=\frac{\sqrt{21}}2.
\]

This run improves
\[
\boxed{B_{R13}(8)=\frac{27919}{10000}=2.7919},
\qquad
B_{R13}(9)=3
\]
(the `n=9` value is the retained elementary `sqrt(n)` upper bound).

For `10<=n<=61` the certified values are:

| n | B(n) | n | B(n) | n | B(n) |
|---:|---:|---:|---:|---:|---:|
| 10 | 3 | 11 | 25/8 | 12 | 417/125 |
| 13 | 3473/1000 | 14 | 3657/1000 | 15 | 1893/500 |
| 16 | 3951/1000 | 17 | 4 | 18 | 4 |
| 19 | 4141/1000 | 20 | 4249/1000 | 21 | 881/200 |
| 22 | 1127/250 | 23 | 4653/1000 | 24 | 4753/1000 |
| 25 | 611/125 | 26 | 997/200 | 27 | 5 |
| 28 | 5 | 29 | 1269/250 | 30 | 521/100 |
| 31 | 662/125 | 32 | 2711/500 | 33 | 2753/500 |
| 34 | 45/8 | 35 | 5707/1000 | 36 | 5821/1000 |
| 37 | 2951/500 | 38 | 6 | 39 | 6 |
| 40 | 6 | 41 | 6049/1000 | 42 | 6123/1000 |
| 43 | 6233/1000 | 44 | 1261/200 | 45 | 6411/1000 |
| 46 | 3241/500 | 47 | 823/125 | 48 | 3327/500 |
| 49 | 6753/1000 | 50 | 3411/500 | 51 | 3459/500 |
| 52 | 1397/200 | 53 | 7 | 54 | 7 |
| 55 | 7 | 56 | 7073/1000 | 57 | 892/125 |
| 58 | 7231/1000 | 59 | 1823/250 | 60 | 1477/200 |
| 61 | 3723/500 |  |  |  |  |

Finally,
\[
\boxed{B_{R13}(n)=3\sqrt{2\pi}\quad(n\ge62).}
\tag{6.1}
\]
This last line is the Guo--Fang--Lu universal theorem; it is not claimed optimal.

Thus the pointwise metric moved at **53 distinct values of `n` in one run**: `n=8` and every `n=10,...,61`.

## 7. Method #7 — take the limit / locate the compiler boundary

The parametric criterion makes clear what the finite-column gain is using: for a chosen walk-tail plateau `q`, the high-energy threshold is `S_0=2nq`, while the low-energy side is controlled by the decreasing profile
\[
x^2\bar\Phi(x),\qquad x>\sqrt2.
\]

I numerically continued the compiler beyond the certified table to see where this route competes with the dimension-free Guo--Fang--Lu constant. The same sufficient-condition search continues to improve the old envelope through `n=61`; at `n=62` the numerically optimized threshold from this *particular* compiler is already slightly above `3sqrt(2pi)`.

**No optimality claim is made at `n=62`.** I did not certify that no different choice of tail inequality, split, or non-rowwise incidence potential can improve the universal constant there. The certified claim stops exactly at the table.

The stronger geometric route from run 9/10 also remains open: at `n=8`, `t=sqrt(6)` would follow from the still-unproved diameter-five convex-mean inequality
\[
|\mathcal F|\,
\operatorname{dist}\!\left(
0,\operatorname{conv}\{s_T:T\in\mathcal F\}
\right)^2
\le96
\]
for every diameter-five downset `F subset 2^[8]`. Numerical stress testing found the five-dimensional subcube at equality, but that is **numerical evidence only** and is not used in C16 or the metric.

## 8. What the three methods actually did

### #6 DEFORM TO A POINT YOU CAN SOLVE — succeeded

The one-off `n=8` split was promoted to the general criterion C16. The deformation parameter is the column count `n` together with the exact walk-tail plateau `q_n(t)`. This moved 53 pointwise bounds.

### #19 MAKE IT AN ALGORITHM — succeeded

C16 becomes a finite rational threshold compiler. Instead of a numerical optimizer, every accepted table entry has an exact binomial tail and exact rational Gaussian-tail certificate.

### #7 TAKE THE LIMIT — useful boundary, not a theorem of optimality

Continuation explains why the mixed-tail compiler is a finite-column supplement rather than a replacement for the dimension-free DTV proof. It no longer wins against the currently certified universal constant at the next tested range, but this is only route diagnostics.

## 9. Exact certificate

Checker:
`artifacts/R13/20260916T2231Z_parametric-tail-6e2a_checker.py`

creation commit:
`b1f499285841681839fe27a1cf4f53871caaa927`.

Archived output:
`artifacts/R13/20260916T2231Z_parametric-tail-6e2a_checker_output.txt`

creation commit:
`3ffea45abb70da7f37bdde571e575e0ed9307214`.

Both were read back at their returned commit SHAs.

The output certifies 53 table entries and ends
`ALL_EXACT_CHECKS_PASS`.
Its content SHA-256 is
`b068c7fe69c7832adaddee603528b7dc7921aa1d3159f9149f9701dd41771e3a`.

The minimum exact table margin is at `n=59`, approximately
`8.89713328019e-06`; positivity itself is checked as an exact rational inequality.

This is a self-check, not an independent audit.

## 10. Prior art / audit state / failures retained

Existing `R12-AUDIT-R13-KOMLOS-01=PASS` remains an independent OTHER-track audit of the Guo--Fang--Lu `3sqrt(2pi)` full-Boolean proof package. It does **not** audit C16 or this 53-entry finite-column table.

A repository search for `P26-AUDIT-R13` still found only earlier R13 reports saying it was absent; no P26 Komlós audit package was located. Therefore fleet closure is **not** claimed.

The latest R12/R16 workers are on other outside assignments, so they are not counted as audits of this new result.

Retained route failures/limits:

- complex/rank-two colors do not solve Boolean signs;
- multiplicative complex-to-Boolean rounding already has an exact `A=[1,1,1]` obstruction;
- the uniform-slab DTV architecture hits its recorded sign-recovery barrier;
- pure row-cardinality/energy compilers for `n=5,6,7` have their previously recorded sharp route barriers;
- the `n=8`, `sqrt(6)` diameter-five convex-mean strengthening remains unproved;
- C16 is only as strong as its two one-dimensional tail inputs and the row-incidence union count.

## 11. Next attack

The best next move is **not** another decimal refinement of the same table.

The high-value target is the intersection-aware `n=8` geometry:
\[
|\mathcal F|\,
\operatorname{dist}(0,\operatorname{conv}s(\mathcal F))^2\le96,
\qquad
\operatorname{diam}_H\mathcal F\le5,
\quad
\mathcal F\text{ a downset}.
\]
A proof gives `B_R13(8)<=sqrt(6)` and, more importantly, would expose a structural compiler not saturated by the one-row tail mixture. A counterexample gives an exact finite obstruction and tells us to stop pursuing that geometry.

No email, Drive, public posting, permission change, workflow execution or scheduler change occurred.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  source: "Janos Komlos Boolean vector balancing; Bansal-Jiang arXiv:2508.03961; Guillen-Kobzar arXiv:2609.15071 for complex/rank-two scope; Guo-Fang-Lu arXiv:2609.11189v1 for current full Boolean constant theorem"
  target: "For every deterministic real m x n matrix with column l2 norms <=1, Boolean signs with certified infinity discrepancy B_R13(n)"
  metric: "complete rigorously certified pointwise upper-bound function B_R13(n)"
  before: "B(8)=349/125; B(n)=sqrt(n) for 9<=n<=56; B(n)=3sqrt(2pi) for n>=57, together with retained n<=7 entries"
  after: "B(8)=27919/10000; B(9)=3; exact rational table above for 10<=n<=61; B(n)=3sqrt(2pi) for n>=62; retained n<=7 entries"
  status: "PARTIAL / metric moved / current literature contains a full universal Boolean theorem; fleet closure audits incomplete"
  unchanged_count: 0
  methods: [6, 7, 19]
  exact_evidence:
    checker_commit: "b1f499285841681839fe27a1cf4f53871caaa927"
    output_commit: "3ffea45abb70da7f37bdde571e575e0ed9307214"
    output_sha256: "b068c7fe69c7832adaddee603528b7dc7921aa1d3159f9149f9701dd41771e3a"
  audits:
    - "R12-AUDIT-R13-KOMLOS-01=PASS (universal GFL package only; not C16/table)"
    - "P26-AUDIT-R13: PENDING_NOT_FOUND"
  remaining_obligation: "Independent audit of C16/table if promoted; structural n=8 diameter-five convex-mean theorem or exact counterexample"
```
