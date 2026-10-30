# B12 FEI — factorial trigger-address code for robust Palm rows

**Run:** `B12-20260921T211214Z-fei-r11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status of full uniform-cube FEI:** **OPEN / NOT PROVED**  
**Claim level:** analytic partial theorem for interface B, with exhaustive low-dimensional diagnostics. No novelty or publication-priority claim.

## 0. Live interface and exact peer result consumed

The live joint order assigns fleet04/B12 to interface B: convert robust near-subcube derivative rows into an influence-relative code without paying ambient dimension. This run uses the fresh scientific head `f536a48b1ae98e22bff294a10adbc59a3b8c907e` (the named fleet02 inputs below are preserved there from the earlier immutable snapshot `28eb593ef50251e09475a7a7aa8c20647599f376`) and substantively consumes:

1. **fleet02/B13** `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260921T180326Z-sign-stability-defect/REPORT.md`, report blob `b4812f3ae22e7f98596f4b1abcb284dc2d180457`. It proves, for a Boolean derivative row with depth defect `Delta`, the dimension-free signed-to-support Palm transfer
   \[
   \operatorname{TV}(P_g,P_E)\le 2\sqrt{\Delta},
   \]
   and, for an equal-density support proxy `C`,
   \[
   \operatorname{TV}(P_g,P_C)
   \le 2\sqrt{\Delta}
      +\sqrt{\eta/j-\eta^2/(4j^2)}.
   \]
   **Exact implication used here:** once the support-stability step supplies `eta/j` and the right side is at most `epsilon`, the *actual signed derivative Palm row* is `epsilon`-close to the uniform power-set row of the nearby coordinate subcube, with no factor depending on the ambient dimension. This is the entry condition for Theorem 3.1 below.

2. **fleet02/B12** `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260921T175134Z-physical-erasure-budget/REPORT.md`. It supplies the complementary exact physical-erasure conservation law and the Ellis-stability route to dimension-free near-subcube TV control; it also proves that TV closeness plus first-moment closeness alone cannot control Shannon entropy because rare off-subcube addresses can carry arbitrarily large entropy. **Implication used here:** the new code must pay *address information*, not apply Fannes over an ambient alphabet.

3. **fleet01/B12** `proofnet24/P03-fei/fleet-2026-09-21/fleet01/B12/20260921T201755Z-companion-factorial/REPORT.md`. Its exact spectral insertion code contains the rebate
   \[
   \mathbb E\log_2(K!),
   \qquad K=|S|,
   \]
   and its one-companion channel shows why only one actual prefix address should be charged at a time. **Implication used here:** the existing factorial term is the natural nonreuse bank into which a trigger address should be compiled.

4. **fleet03/B12**, newly landed at scientific commit `f536a48b1ae98e22bff294a10adbc59a3b8c907e`, `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B12/20260921T211211Z-ordered-parent-flag-nonreuse/REPORT.md`, blob `a76cd2ab5c03546c421c9c004cfeae3f12b1e7a9`. It gives a genuine Boolean bent-family obstruction to the unconditional prefix-total-correlation remainder and replaces it by the stop-conditioned target
   \[
   R_T=I\operatorname{TC}(P\mid T)-\mathbb E\log_2(K!).
   \]
   **Exact implication used here:** the factorial term must remain a negative nonreuse resource, not be upper-bounded by `O(J)` or cancelled against unconditional prefix total correlation. Corollary 4.2 below inserts the robust trigger-address credit directly into this corrected `R_T`.

The current fleet04/B18 mixed-curvature identity remains binding: raw depth satisfies a second-factorial-moment conservation law, but `sum_i d_i` is **not** known to be `O(J)`. Nothing below assumes or tries to prove such a bound.

## 1. Setup

Work after the current character gauge, so the spectral sample `S` has law
\[
\mu(A)=\widehat f(A)^2,
\]
and
\[
j_i=\Pr(i\in S).
\]
In the median/minimizing gauge used by the current B-interface, the sum of these inclusion probabilities is the influence budget relevant to that gauge (in particular it can be `J` after the prescribed recentering). Put
\[
K=|S|.
\]

For an active coordinate `i`, let
\[
\nu_i(B)=\Pr(S\setminus\{i\}=B\mid i\in S).
\]
Call row `i` `epsilon_i`-Palm-robust with trigger set `F_i` if
\[
\operatorname{TV}(\nu_i,U_{F_i})\le\epsilon_i,
\tag{1.1}
\]
where `U_F` is the uniform law on all subsets of `F`. Write
\[
m_i=|F_i|.
\]

The previous fleet04/B12 trigger-cluster theorem used the common threshold `epsilon_i<=1/16`. It proved reciprocal trigger-signature locking and factor-7 scale escapes. The present argument changes mechanism: instead of paying pair masses or raw depth, it partitions the **factorial rebate itself** among Palm rows.

## 2. PROVED: exact Palm partition of the factorial rebate

Define for integers `k>=1`
\[
g(k)=\frac{\log_2(k!)}{k}.
\]
Then
\[
\boxed{
\mathbb E\log_2(K!)
=\sum_i j_i\,\mathbb E_{\nu_i} g(1+|B|).
}
\tag{2.1}
\]

### Proof

For every nonempty realized set `S`,
\[
\sum_{i\in S}\frac{\log_2(|S|!)}{|S|}=\log_2(|S|!).
\]
Average over `S`, then condition each summand on `i in S`. The empty set contributes zero. QED.

Equation (2.1) is the nonreuse identity missing from a raw `sum d_i` charge: a terminal set of size `K` splits its factorial rebate into exactly `K` shares of size `log(K!)/K`, one for each occupied row. No pair or second derivative is counted at unit price.

## 3. PROVED: factorial trigger-address theorem

For `c>=1` define
\[
A_c
:=\mathbb E\left[\frac{\log_2(T!)}{T}\right],
\qquad
T=1+\operatorname{Bin}(c-1,1/2).
\tag{3.1}
\]

### Lemma 3.1 — universal logarithmic lower bound

For every integer `c>=1`,
\[
\boxed{A_c\ge\frac14\log_2 c.}
\tag{3.2}
\]

### Proof

For every integer `t>=1`,
\[
(t!)^2
=\prod_{r=1}^t r(t+1-r)
\ge t^t,
\]
because `r(t+1-r)>=t`. Hence
\[
\frac{\log_2(t!)}t\ge\frac12\log_2 t.
\tag{3.3}
\]

Now `T=1+Bin(c-1,1/2)` has the same distribution as `c+1-T`. Therefore
\[
2\mathbb E\log_2T
=\mathbb E\log_2[T(c+1-T)].
\]
For `1<=T<=c`, the concave quadratic `T(c+1-T)` is minimized at an endpoint and is at least `c`. Thus
\[
\mathbb E\log_2T\ge\frac12\log_2c.
\]
Combine this with (3.3). QED.

### Theorem 3.2 — robust trigger addresses are factorial-paid

Let `R` be any collection of Palm-robust rows satisfying (1.1), with `epsilon_i<1/4`. Then
\[
\boxed{
\mathbb E\log_2(K!)
\ge
\sum_{i\in R}
\left(\frac14-\epsilon_i\right)
 j_i\log_2(m_i+1).
}
\tag{3.4}
\]

In particular, at the current robust threshold `epsilon_i<=1/16`,
\[
\boxed{
\sum_{i\in R}j_i\log_2(m_i+1)
\le\frac{16}{3}\,\mathbb E\log_2(K!).
}
\tag{3.5}
\]

### Proof

Fix `i`. Define a bounded function on all Palm remainders by
\[
\psi_i(B)
=
1_{\{B\subseteq F_i\}}
\frac{\log_2((1+|B|)!)}{1+|B|}.
\tag{3.6}
\]
It obeys
\[
0\le\psi_i(B)\le\log_2(m_i+1).
\]
Also `g(1+|B|)>=psi_i(B)` pointwise. Therefore total-variation stability gives
\[
\begin{aligned}
\mathbb E_{\nu_i}g(1+|B|)
&\ge \mathbb E_{\nu_i}\psi_i(B)\\
&\ge \mathbb E_{U_{F_i}}\psi_i(B)
   -\epsilon_i\log_2(m_i+1)\\
&= A_{m_i+1}-\epsilon_i\log_2(m_i+1)\\
&\ge\left(\frac14-\epsilon_i\right)
   \log_2(m_i+1),
\end{aligned}
\tag{3.7}
\]
where the last line is Lemma 3.1. Insert (3.7) into the exact partition (2.1), keep only `i in R`, and use nonnegativity of the omitted rows. QED.

### Why this is influence-relative rather than ambient-dimensional

The address alphabet for robust row `i` is its actual trigger signature, of size `m_i+1`, not `[n]`. The weighted address cost is therefore
\[
j_i\log_2(m_i+1),
\]
not `j_i log n`, `j_i n`, or `d_i`. The sum of these costs is controlled by a term already present with a negative sign in the exact spectral insertion code. No claim that `E log(K!)` itself is `O(J)` is made or needed.

This also answers the abstract rare-address obstruction from fleet02/B12 in the robust sector: if the Palm row is genuinely close to a fixed subcube law, a large trigger alphabet forces a correspondingly large factorial rebate. The remaining off-trigger `epsilon_i` fraction is explicit in (3.4); it is not hidden by a Fannes estimate.

## 4. PROVED: component form compatible with the fleet04 trigger DAG

For the reciprocal robust components from the preceding fleet04/B12 theorem, trigger locking gives one exact signature `T_C` with
\[
F_i=T_C\setminus\{i\}\qquad(i\in C).
\tag{4.1}
\]
Hence `m_i+1=|T_C|` for every row in `C`. Writing
\[
W_C=\sum_{i\in C}j_i,
\]
Theorem 3.2 immediately yields, at `epsilon<=1/16`,
\[
\boxed{
\frac3{16}\sum_C W_C\log_2|T_C|
\le\mathbb E\log_2(K!).
}
\tag{4.2}
\]
for any collection of robust reciprocal components.

This is the requested component-level **address** payment. The prior scale theorem says every robust trigger leaving a reciprocal component jumps by at least a factor seven in influence, and fleet04/B18's newest sink theorem gives a canonical collision-free physical restriction of sink components. Equation (4.2) adds the missing coding fact: identifying one coordinate inside the common trigger signature does not require an ambient-dimension charge; its worst-case logarithmic address is controlled by the factorial bank with a universal constant.

What (4.2) does **not** yet prove is that every positive-defect row is robust, nor that the explicit `epsilon_i` off-trigger mass can always be eliminated without reuse. Those are still the exceptional-row/stability obligations. The factor-7 DAG and mixed-curvature conservation remain necessary to keep repeated physical peeling honest.

### Corollary 4.2 — robust-address credit inside the corrected stop-conditioned remainder

Use the newly landed fleet03/B12 corrected remainder
\[
R_T=I\operatorname{TC}(P\mid T)-\mathbb E\log_2(K!).
\]
Combining it with Theorem 3.2 gives, for any robust row family `R`,
\[
\boxed{
R_T
\le I\operatorname{TC}(P\mid T)
-\sum_{i\in R}
  \left(\frac14-\epsilon_i\right)
  j_i\log_2(m_i+1).
}
\tag{4.3}
\]
At `epsilon_i<=1/16`,
\[
\boxed{
R_T
\le I\operatorname{TC}(P\mid T)
-\frac3{16}\sum_{i\in R}j_i\log_2(m_i+1).
}
\tag{4.4}
\]
For reciprocal components this becomes the same subtraction with `sum_C W_C log_2|T_C|`. This does **not** prove `R_T=O(J)`; it identifies an explicit negative term that cancels robust trigger-address complexity *inside the repaired remainder* while leaving the stop-conditioned dependence and exceptional rows visible.

## 5. Relation to fleet02 row stability

The fleet02/B13 theorem gives, in its equal-density support-proxy normalization,
\[
\operatorname{TV}(P_g,P_C)
\le
2\sqrt{\Delta}
+\sqrt{\eta/j-\eta^2/(4j^2)}.
\tag{5.1}
\]
Thus every row satisfying
\[
2\sqrt{\Delta}
+\sqrt{\eta/j-\eta^2/(4j^2)}
\le\frac1{16}
\tag{5.2}
\]
and whose proxy `C` is the relevant coordinate subcube enters Theorem 3.2 with `epsilon<=1/16`. The consequence is the explicit dimension-free code
\[
\boxed{
\sum_{\text{such }i}j_i\log_2(|F_i|+1)
\le\frac{16}{3}\,\mathbb E\log_2(K!).
}
\tag{5.3}
\]

This is the exact cross-account implication supplied by the fleet02 stability result: its `L^2/TV` control is not converted to Shannon entropy by alphabet-size continuity; it is converted to a **factorial-paid trigger address** through (2.1).

## 6. Decisive checks

`check_factorial_trigger_address.py` performs two different diagnostics.

1. It verifies the scalar lower bound `A_c >= (1/4) log_2 c` numerically for `2<=c<=256`; the minimum observed ratio is exactly `1/4` at `c=2`, matching the analytic proof's endpoint.
2. It enumerates every Boolean truth table through dimension four modulo global output sign, computes exact Walsh-square spectra with rational arithmetic, finds the closest uniform power-set trigger law for every Palm row, and checks:
   - the exact factorial Palm partition (2.1);
   - every robust-row inequality (3.7) at `epsilon=1/16`;
   - the summed theorem (3.5).

Results:

- Boolean functions: `32,906`;
- exact factorial-partition checks: `32,906`;
- robust nontrivial row checks: `11,348`;
- summed theorem checks: `32,906`;
- violations: `0`;
- maximum ratio of the `(3/16)` address lower bound to the actual factorial rebate in this enumeration: `0.75`.

Checker SHA-256: `2504386148277896b95891c4f73873236329dcf769beb84756fbd14ed778e04a`.  
Output SHA-256: `50b0eb44775e71b7b9807a95a53433a4d0ebf69829818ea795f9ca0c61941a63`.

These finite checks are diagnostic only; Theorems 2.1 and 3.2 are analytic.

## 7. Full-problem change and remaining implication

**Before this run:** the robust trigger quotient was an exact-block, factor-7 DAG, and fleet01's one-companion theorem routed a constant fraction of robust-row mass into a first-moment flow. The open wording was still “pay the remaining codimension/address charge without reverting to raw depth.”

**After this run:** for every robust row, the trigger-address quantity `j_i log_2(|F_i|+1)` is controlled directly by the already-present factorial rebate, with no ambient dimension and no `sum d_i` charge. On reciprocal components this becomes the shared-signature payment (4.2), and in the newly corrected fleet03 stop-conditioned code it appears as the explicit negative credit (4.4). The fleet02 stability theorem supplies a dimension-free quantitative entrance condition into this paid sector.

**Remaining implication:** control the positive-defect rows that fail the robust threshold, and control the explicit off-trigger `epsilon_i` mass during repeated B18 sink peeling, using mixed-curvature integrability or a nonreusing exceptional-row elimination. A proof that `sum_i d_i=O(J)` is neither used nor suggested; the odd-majority/tensor obstructions remain binding.

Full FEI remains **OPEN / NOT PROVED**.
