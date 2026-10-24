# B13 FEI joint-derivative stability: one-block residual paid by the global row-defect bank

**Account/slot:** account03/B13  
**Joint interface:** B — compatibility and integrability of several derivative rows  
**Execution:** WITHOUT_VERIFIED_BRAIN  
**Full FEI status:** **OPEN / NOT PROVED**.  
**Claim scope:** a universal Boolean stability implication obtained by composing completed peer inputs. It does not pay the restriction Shannon cost and therefore does not close FEI. No novelty or publication-priority claim is made.

## 0. Exact statement attempted

Work after the usual character recentering so every active folded influence is an ordinary influence

\[
0<j_i=\operatorname{Inf}_i(f)\le \tfrac12,
\qquad J=\sum_i j_i.
\]

For the ternary derivative row `g_i=D_i f`, put

\[
d_i=\sum_{k\ne i}\|D_k g_i\|_2^2,
\qquad
\Delta_i=\frac{d_i}{j_i}-\frac12\log_2\frac1{j_i}\ge0,
\]

and define the **global weighted row-defect bank**

\[
\mathcal D(f)=\sum_i j_i\Delta_i.
\tag{0.1}
\]

The universal statement attacked in this run was:

> Is there a dimension-independent constant `C_*` such that one physical restriction block can reduce the expected centered influence to at most `C_* mathcal D(f)`?

Using the completed account02/B12 physical support-stability theorem, the preceding account03/B13 compatibility DAG, and the new account04/B13 source-frontier one-shot theorem, the answer is **YES**, with an absolute finite constant inherited from the quantitative cube-isoperimetric stability threshold.

More precisely, let `epsilon_E>0` denote the absolute validity threshold in the support-stability statement recorded by account02/B12:

\[
\epsilon_{\rm iso}:=\frac{S_{\rm iso}}{2j}\le\epsilon_E
\quad\Longrightarrow\quad
\frac{\mu(E\triangle Q)}j
\le \frac{2\epsilon_{\rm iso}}{\log_2(1/\epsilon_{\rm iso})}
\tag{0.2}
\]

for some coordinate subcube `Q`. Set

\[
\eta_0:=\min\{\epsilon_E/2,\,1/32\}.
\tag{0.3}
\]

Then there is one physical block `A` such that

\[
\boxed{
\mathbb E_z J(f_{A=z})
\le \left(1+\frac1{\eta_0}\right)\mathcal D(f).
}
\tag{0.4}
\]

This is a genuine all-dimensional implication. The numerical value of `epsilon_E` was not pinned in the peer report, so this run does **not** invent a numerical value for `C_*`.

## 1. Peer results consumed, not merely cited

### Peer input P1 — account02/B12 physical support stability

Consumed artifact:

`proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260921T175134Z-physical-erasure-budget/REPORT.md`, read at scientific revision `b6d717a423581c36373aba68f8c9170f73865b6c`.

That report records the exact defect identity

\[
S_{\rm iso}+S_{\rm sign}=4j\Delta
\tag{1.1}
\]

and the dimension-free support stability (0.2), using the quoted Ellis cube-isoperimetric stability theorem. Therefore

\[
\epsilon_{\rm iso}=S_{\rm iso}/(2j)\le2\Delta.
\tag{1.2}
\]

The report also gives sign/Palm stability, but only the **physical support** consequence is needed below.

### Peer input P2 — account04/B13 one-shot source-frontier elimination

Consumed artifact:

`proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260921T2122Z-source-frontier-one-shot/REPORT.md`, blob `8cced1e67ed2181463caaf877946717e81e4e7c8`.

It consumes this slot's preceding compatibility-DAG theorem and proves: if `R` is a family of rows satisfying the simultaneous low-defect / physical-near-subcube hypotheses, `E` is the arbitrary complement, and `e_i=mu(E_i triangle Q_i)` is the physical support error, then a single source-frontier block `A` obeys

\[
\boxed{
\mathbb E_zJ(f_{A=z})\le J_E+\sum_{r\in S}e_r,
}
\tag{1.3}
\]

where `S subset R` is the surviving source-representative family. No ambient-dimension factor occurs.

The prerequisite compatibility theorem is this slot's previous

`account03/B13/20260921T203308Z-integrability-dag/REPORT.md`, blob `56210613208b533b79a875f1289133924ec74ab8`,

which applies when the row defect and relative physical support error are both at most the stated `1/16` scale.

## 2. PROVED FROM P1+P2: low-defect rows have defect-paid physical error

Take one active row with

\[
\Delta_i\le\eta_0.
\]

By (1.2),

\[
\epsilon_{{\rm iso},i}\le2\Delta_i\le\epsilon_E,
\]

so P1 gives a coordinate subcube `Q_i` with relative error

\[
\frac{e_i}{j_i}
\le
\frac{2\epsilon_{{\rm iso},i}}
     {\log_2(1/\epsilon_{{\rm iso},i})}.
\tag{2.1}
\]

The function `x -> 2x/log_2(1/x)` is increasing on `(0,1)`. Hence

\[
\frac{e_i}{j_i}
\le
\frac{4\Delta_i}{\log_2(1/(2\Delta_i))}.
\tag{2.2}
\]

Because `Delta_i<=eta_0<=1/32`, the denominator in (2.2) is at least four. Therefore

\[
\boxed{e_i\le j_i\Delta_i.}
\tag{2.3}
\]

In particular `e_i/j_i<=1/32<1/16` and `Delta_i<=1/32<1/16`, so every such row lies inside the physical-near-subcube regime required by the account03 compatibility DAG and account04 source-frontier theorem.

This is stronger than merely assigning one common `epsilon` to all robust rows: the physical error is charged **row by row to its own depth defect**.

## 3. PROVED FROM P1+P2: arbitrary exceptional rows are also defect-paid

Split the active rows at `eta_0`:

\[
R=\{i:\Delta_i\le\eta_0\},
\qquad
E=\{i:\Delta_i>\eta_0\}.
\]

The exceptional folded-influence mass satisfies the exact Markov payment

\[
J_E=\sum_{i\in E}j_i
\le\frac1{\eta_0}\sum_{i\in E}j_i\Delta_i
\le\frac{\mathcal D(f)}{\eta_0}.
\tag{3.1}
\]

Apply P2 to `R`, treating `E` as completely arbitrary. By (1.3), then (2.3),

\[
\begin{aligned}
\mathbb E_zJ(f_{A=z})
&\le J_E+\sum_{r\in S}e_r\\
&\le \frac{\mathcal D(f)}{\eta_0}
   +\sum_{r\in S}j_r\Delta_r\\
&\le \left(1+\frac1{\eta_0}\right)\mathcal D(f).
\end{aligned}
\]

This proves (0.4).

### Consequence

If

\[
\frac{\mathcal D(f)}J
<\frac{\eta_0}{1+\eta_0},
\]

then the block strictly contracts expected centered influence. If

\[
\frac{\mathcal D(f)}J
\le\frac{\eta_0}{2(1+\eta_0)},
\]

then it contracts by a factor at least two:

\[
\mathbb E J(\text{child})\le J/2.
\]

Thus the previous two separate interface-B gaps — low-positive-defect row shape and uncontrolled exceptional influence mass — collapse, in the small-global-defect branch, to one scalar bank `mathcal D(f)`.

This does **not** say `mathcal D(f)=O(J)` universally. Indeed

\[
\mathcal D(f)
=
\sum_i d_i-rac12\sum_i j_i\log_2(1/j_i),
\]

and the first term is the second-factorial spectral-depth bank. The universal Shannon payment remains open.

## 4. Decisive dead route: the tempting local constant 2 is false

A much cleaner proof would follow if every constant-sign derivative support satisfied

\[
\frac{\mu(E\triangle Q)}{\mu(E)}\le2\Delta
\tag{4.1}
\]

for some coordinate subcube `Q`. This is **REFUTED by an actual Boolean derivative row**, not by a non-Boolean relaxation.

Take three physical row variables and

\[
E=\{000,100,010\},\qquad g=1_E.
\]

It is a genuine derivative row: define a Boolean parent on an extra bit by `f(0,y)=1` and `f(1,y)=1-2 1_E(y)`.

Here

\[
j=3/8,
\qquad I(1_E)=5/4,
\]

so, since the sign slack is zero,

\[
\Delta
=\frac{I(1_E)-2j\log_2(1/j)}{4j}
=\frac56-\frac12\log_2(8/3)
=0.1258145836939\ldots.
\]

Every coordinate subcube has power-of-two cardinality, so a three-point set cannot itself be a subcube. The four-point face containing the L-shape differs in exactly one point, hence the optimal relative distance is

\[
\delta=1/3.
\]

But

\[
2\Delta=0.2516291673878\ldots<1/3.
\]

Therefore (4.1) is false. A proof of interface B cannot simply replace the cube-stability modulus by `2 Delta`.

## 5. Executed finite counterexample search

`check_support_defect.py` exhaustively enumerates every nonempty support `E` of density at most `1/2` through physical row dimension four, computes its exact edge influence, its depth defect, and its closest coordinate subcube.

Recorded output:

- `m=1`: 2 supports; 0 violations of `delta<=2 Delta`; 0 of `delta<=4 Delta`.
- `m=2`: 10 supports; 0 violations of either bound.
- `m=3`: 162 supports; **24** violations of `delta<=2 Delta`; 0 of `delta<=4 Delta`; maximum `delta/Delta = 2.649401393277941`.
- `m=4`: 39,202 supports; **192** violations of `delta<=2 Delta`; 0 of `delta<=4 Delta`; maximum `delta/Delta = 2.649401393277944`.

The maximizer is the three-point L-shape above (or an embedding/symmetry image). The absence of a `delta<=4 Delta` violation through `m=4` is **finite evidence only**, not a theorem. P1's dimension-free theorem, not this enumeration, is what supports Section 2.

## 6. What changed in the joint proof state

**PROVED from completed peer inputs, at their stated scopes:**

1. Low-depth-defect rows can be made physically near-subcube with their support error paid by `j_i Delta_i`, once inside the absolute stability regime.
2. High-defect exceptional influence is paid by `mathcal D/eta_0` with no ambient-dimension factor.
3. One source-frontier physical block therefore satisfies the universal residual bound (0.4).

**REFUTED here:** the stronger local shortcut `relative support distance <= 2 Delta`.

**OPEN:**

- a dimension-free payment of the **Shannon cost of the selected reveal block** by `J` plus already-counted credits;
- a universal way to spend or amortize `mathcal D(f)` without assuming `mathcal D=O(J)`;
- full uniform-cube FEI.

The account04 one-shot trigger-load estimate still routes raw trigger multiplicity through `sum_i d_i`; (0.4) shows that the **post-restriction residual** can instead be routed through the smaller defect bank `mathcal D`, but it does not by itself replace the reveal-block entropy/depth payment.

## 7. Next attack

The next interface-B attack should use the account02/B12 exact physical-erasure identity

\[
j_i\mathcal E_{\rm phys}(g_i)\asymp j_i\Delta_i
\]

(rowwise, with factor between one and two) as a **telescoping payment for the reveal decision itself**. The concrete target is an inequality of the form

\[
B_A \le C_1 I_A + C_2\sum_i j_i\Delta_i
      - \text{nonnegative crossing / information credits},
\]

for the actual source-frontier block `A`, with every row used at most once. Combining such a bound with (0.4) would turn the current compatibility theorem into a recursive FEI step without ever asserting the false `sum_i d_i=O(J)` shortcut.

## 8. Joint handoff fields

`consumed_peer_artifact`:
- `account02/B12/20260921T175134Z-physical-erasure-budget/REPORT.md` at revision `b6d717a423581c36373aba68f8c9170f73865b6c`;
- `account04/B13/20260921T2122Z-source-frontier-one-shot/REPORT.md`, blob `8cced1e67ed2181463caaf877946717e81e4e7c8`.

`applied_to_claim`: the universal one-block residual estimate `E J(child) <= (1+1/eta_0) mathcal D(f)`.

`remaining_implication`: pay the source-frontier reveal-block Shannon cost using `J`, the row physical-erasure banks, and existing negative/crossing credits, without substituting uncontrolled second factorial moment.

`next_recipient`: account04/B13 and account04/B18 for source-frontier integration; account02/B12 for the physical-erasure-to-reveal-entropy payment.

`full_problem_change`: interface B now has a dimension-free global row-defect-to-residual-influence theorem. Full FEI remains OPEN.
