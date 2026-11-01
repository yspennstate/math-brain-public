# B13 — exact balanced arity-5 two-quarter slice is nonbinding

**Run:** `fleet03-B13-20260922T083027Z-20185f866f`  
**Role:** fleet03/B13, FEI under the current all-gate convergence target.  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FINITE_SLICE_EXCLUDED`; full uniform-cube FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub control and mathematical sources were consumed, but no authenticated native/cognitive brain retrieval or receiver-context result entered the mathematics.

## 0. Candidate version and the missing implication attacked

The live owner target is the all-gate inequality
\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)\,
{\Gamma(p_i)+h_2(V_{p_i})\over V_{p_i}},
\qquad V_p=4p(1-p),
\tag{0.1}
\]
with one symmetric nonnegative finite-center potential.  The relevant source version is
`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`.
The earlier fleet03/B13 derivative-row assignment is superseded for this invocation by the later natural-language owner message that asks every FEI worker to converge on the gate target.

I consume two named completed peer results.

1. **fleet04/B17**,  
   `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T051537Z-quarter-half-arity5/REPORT.md`,  
   proves by exhaustive exact Boolean enumeration that every balanced arity-5 gate on
   \[
   (1/4,1/2,1/2,1/2,1/2)
   \]
   is nonbinding against the quarter-AND face, with exact center demand at most
   \(6.120601248052878\ldots\).  It names the closest genuinely new slice as **two quarter-biased coordinates and three unbiased coordinates**.

2. **fleet01/B15**,  
   `proofnet24/P03-fei/fleet-2026-09-21/fleet01/B15/20260922T0405Z-g10-terminal-atom-feasibility/REPORT.md`,  
   proves for the exact G10 stopping corridor that, writing
   \[
   C=\Gamma(1/2),\qquad g=\Gamma(1/4)=\Gamma(3/4),
   \]
   the terminal AND/OR atoms and stopped block have a common feasible value precisely when
   \[
   C\ge R(G10),\qquad
   6.4593722816378557311\ldots<R(G10),
   \]
   and every such center admits the upper endpoint
   \[
   g=C-2.
   \tag{0.2}
   \]

The prior missing implication attacked here is therefore exact and finite:

> Does the next untouched balanced arity-5 product-bias slice
> \[
> p=(1/4,1/4,1/2,1/2,1/2),\qquad p_{\rm out}=1/2
> \]
> force a center \(C\) larger than the G10 corridor, or a positive owner-comparable gate margin?

The answer is **no**.

## 1. Exact reduction on the two-quarter slice

Let the two quarter-biased inputs be \(y_1,y_2\), and let the other three inputs be unbiased.  Put
\[
A={\operatorname{It}_{y_1}+\operatorname{It}_{y_2}\over V_{1/4}}
  ={4\over3}\bigl(\operatorname{It}_{y_1}+\operatorname{It}_{y_2}\bigr),
\qquad
B=\sum_{i=1}^3\operatorname{It}_{x_i}.
\tag{1.1}
\]
For balanced output, (0.1) is exactly
\[
C+\widetilde H_G
\le
BC+A\bigl(g+h_2(3/4)\bigr).
\tag{1.2}
\]
The G10/terminal-AND corridor permits \(g=C-2\), which maximizes the right side because \(A\ge0\).  Hence every gate on this slice is simultaneously compatible with that upper face whenever
\[
\widetilde H_G+A\bigl(2-h_2(3/4)\bigr)
\le C(A+B-1).
\tag{1.3}
\]
Since
\[
2-h_2(3/4)={3\over4}\log_2 3,
\]
define, whenever \(A+B>1\),
\[
\boxed{
C_{\rm req}(G)
=
{\widetilde H_G+\frac34(\log_2 3)A\over A+B-1}.
}
\tag{1.4}
\]
The zero-currency cases are characters and satisfy (1.2) identically.

Thus this entire slice reduces to maximizing one exact scalar over actual Boolean truth tables.

## 2. Exact Boolean parameterization

Write the four three-bit restrictions of the gate as \(G_{00},G_{01},G_{10},G_{11}\), indexed by \((y_1,y_2)\), and let
\(k_{ab}\in\{0,\ldots,8\}\) be their positive-row counts.  The branch probabilities are
\[
{9\over16},{3\over16},{3\over16},{1\over16},
\]
so output balance is exactly
\[
\boxed{
9k_{00}+3k_{01}+3k_{10}+k_{11}=64.
}
\tag{2.1}
\]
There are exactly **81** feasible count quadruples and
\[
\boxed{119,655,384}
\]
raw balanced Boolean gates on this bias slice.

For each three-bit Fourier subset \(T\), let
\(s_{ab}(T)\) be the unnormalised integer Walsh sum of branch \(G_{ab}\).
The thirty-two biased squared Fourier masses of the full gate are exact rationals with common denominator \(16384=2^{14}\).  For every \(T\),
\[
\begin{aligned}
n_0(T)&=(9s_{00}+3s_{01}+3s_{10}+s_{11})^2,\\
n_1(T)&=3\,[3(s_{10}-s_{00})+(s_{11}-s_{01})]^2,\\
n_2(T)&=3\,[3(s_{01}-s_{00})+(s_{11}-s_{10})]^2,\\
n_{12}(T)&=9\,[s_{00}-s_{01}-s_{10}+s_{11}]^2,
\end{aligned}
\tag{2.2}
\]
and the corresponding masses are \(n_*/16384\).

The joint quarter-input contribution must count the \(y_1y_2\) layer twice:
\[
A={\sum_T[n_1(T)+n_2(T)+2n_{12}(T)]\over 16384(3/4)},
\tag{2.3}
\]
while
\[
B={\sum_T |T|\,[n_0(T)+n_1(T)+n_2(T)+n_{12}(T)]\over16384}.
\tag{2.4}
\]
This double-counting point is essential; omitting it gives a false center demand.

## 3. Complete orbit enumeration

The three unbiased coordinates admit the simultaneous cube automorphism group
\[
S_3\ltimes(\mathbb Z/2)^3
\]
of size \(48\).  For each feasible count quadruple, the checker canonicalizes whichever one of the four branches yields the smallest complete orbit quotient and enumerates every choice of the other three branches.

This reduces the \(119,655,384\) raw gates to
\[
\boxed{7,492,264}
\]
evaluated orbit representatives, with no loss of coverage.  Every spectral numerator and every influence quantity is integer/rational before logarithms.

The complete screen finds only 24 representatives with \(C_{\rm req}>6.15\).  They collapse to three maximizing exact spectral/influence signatures.  Every signature above 6.0 is replayed at 80-decimal precision.  The next distinct value after the maximum is
\[
6.1324298717558356823\ldots,
\]
leaving a gap exceeding \(0.095\).

The maximum is
\[
\boxed{
C_{\rm qq}
=
{51\over5}
-{27\over40}\log_2 3
-{5\over4}\log_2 5
=
6.2277401934040166426808269259734861\ldots .
}
\tag{3.1}
\]

One maximizing representative has branch masks
\[
\boxed{(7,15,119,127)}
\tag{3.2}
\]
with branch-positive counts \((3,4,6,7)\).  Its thirty-two spectral mass numerators over \(16384\) have histogram
\[
0^9,\quad 192^{14},\quad256^3,\quad1024^3,\quad1728^2,\quad6400^1.
\tag{3.3}
\]
For this witness,
\[
A={1\over2},\qquad B={9\over8},
\tag{3.4}
\]
and
\[
\widetilde H_G
=
{51\over8}
-{51\over64}\log_2 3
-{25\over32}\log_2 5.
\tag{3.5}
\]
Adding the exact quarter-child entropy term gives
\[
\widetilde H_G+{3\over4}(\log_2 3)A
=
{51\over8}
-{27\over64}\log_2 3
-{25\over32}\log_2 5,
\tag{3.6}
\]
and division by \(A+B-1=5/8\) yields (3.1).

As a separate physical-realizability check, replace each quarter-biased input by a fresh unbiased two-bit AND.  The resulting genuine balanced seven-bit Boolean function has
\[
I={13\over8},\qquad
H=3.8923376208775102\ldots,
\]
and therefore
\[
{H\over I-1}=6.227740193404016\ldots,
\]
agreeing with (3.1) by an independent ordinary Walsh transform.

## 4. Consequence for the peer G10 corridor

The exact peer corridor requires only
\[
C\ge R(G10)>6.4593722816378557311\ldots .
\]
But
\[
R(G10)-C_{\rm qq}
>
0.2316320882338390884\ldots .
\tag{4.1}
\]
Therefore, choosing the already-allowed common value
\[
g=C-2
\]
simultaneously certifies:

1. the G10 stopped block,
2. every terminal quarter-bias AND/OR atom in that corridor, and
3. **every balanced five-input Boolean gate at**
   \[
   (1/4,1/4,1/2,1/2,1/2).
   \]

So this entire next arity-5 slice adds no new center obstruction beyond the already-known G10 constraint.

This is an exact finite-slice statement, not a universal arity-5 theorem and not a proof of FEI.

## 5. Owner-comparable gate margin

For the owner's read-once base normalization
\[
C_0=\Gamma_0(1/2)=6.4548,\qquad
\Gamma_0(1/4)=C_0-2,
\]
the same exhaustive search also maximizes the comparable quadratic margin
\[
c_G=-{D_G\over I(G;p)/4-p_{\rm out}(1-p_{\rm out})}.
\tag{5.1}
\]
For the witness (3.2),
\[
I(G;p)={3\over2},\qquad
I(G;p)/4-1/4={1\over8},
\]
and hence
\[
\boxed{
c_G^{\max}
=
5(C_{\rm qq}-6.4548)
=
-1.1352990329799167865958653701325693\ldots<0.
}
\tag{5.2}
\]
Thus **no gate anywhere on this complete two-quarter balanced slice asks for positive margin**.  The entire slice is far from the binding two-input AND constraint in the units the owner requested.

## 6. Verification status and limitations

`CHECK.py` performs the full 7,492,264-representative enumeration, exact integer spectral construction, exact orbit/count checks, high-precision replay of every signature screened above 6.0, the exact closed-form maximizer check, and the independent seven-bit physical-composition Walsh check.  Its captured output is `VERIFY.txt` and reports `PASS`.

Checker SHA-256:
`d9a6a77c10bff71d6dc45121e1b80ad28310694a5a7783e3536de21182d0d610`

Captured-output SHA-256:
`c8b666e0c7f976d5b230e476e7aba6cc78140dc419141030173ef8263246e81f`

The combinatorial coverage and spectral/influence numerators are exact.  The ordering of the small set of transcendental signatures is replayed at 80-decimal precision rather than by an independent formal interval package, so this remains a self-checked finite certificate pending independent review.  The \(>0.095\) gap to the next distinct screened signature makes ordinary floating-point rank ambiguity immaterial at the displayed precision, but this report does not promote the computation to a machine-checked theorem.

## 7. Replacement obligation and next recipient

**Prior missing implication:** test the closest untouched arity-5 bias geometry after fleet04/B17's one-quarter slice.

**New proved/self-checked inference:** the complete balanced two-quarter slice is nonbinding:
\[
C_{\rm req}\le C_{\rm qq}<R(G10),
\qquad
c_G^{\max}(C_0)<0.
\]

**Replacement obligation:** a finite arity-5 falsifier must now leave both the one-quarter balanced slice and the two-quarter balanced slice.  The closest genuinely new exact target is an **unbalanced-output quarter slice**, where \(\Gamma(p_{\rm out})\) cannot be eliminated by setting it equal to the center; alternatively test three quarter-biased inputs if the common potential constraints at the resulting output measures are retained exactly.

**Primary next recipient:** `fleet04/B17`, because this closes the exact next adversarial slice named in its report.  
**Secondary recipients:** `fleet01/B15` for common-potential corridor integration, and `fleet03/B18` for all-gate proof integration.

**Implication to full FEI:** this narrows the gate-falsification search and proves compatibility of one larger finite family with an already-live common potential corridor.  It does not provide a universal potential, does not prove decomposable-gate extremality, and does not change the target-level status: **full FEI remains OPEN**.
