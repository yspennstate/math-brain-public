# B14 — physical core-block selector and one-pair changed-support rigidity

**Outcome:** `AUXILIARY_ONLY` (decisive current-family selector theorem; the universal prime-gate implication remains open).  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were read directly, but no installed/native research-brain retrieval/context was used.

## 1. Exact live candidate and compact conditional end-to-end argument

I bind this run to account01/B18's immutable candidate

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`

as read from scientific master `6b48fd1938d81bd7bcd977c22231a072f76cbb7c`.  Its stable candidate is

\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p),
\]

and `LIMIT-PRIME-GATE-LIFT-v1` is

\[
D_{\Gamma_*}(P;p)\ge 0
\tag{1.1}
\]

for every finite composition-prime Boolean gate `P` and every interior product bias vector `p`.

The exact named other-account theorem consumed and applied is account02/B17,

`proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`,

at the same source snapshot.  It proves the slack/Poincare cocycle under disjoint composition, hence (1.1) for all prime gates implies the same gate inequality for every Boolean gate.  The all-gate reformulation then gives

\[
H(f)\le C_* I(f)
\]

for every uniform-cube Boolean function.  Therefore the first **global** missing implication remains exactly (1.1).  Nothing below proves it.

The second exact other-account theorem used substantively is account03/B18,

`proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T035359Z-fixed-support-host-partitions/REPORT.md`,
report blob `cbb4f5cecdd1f1f9dba695cfca0b5e1bc9173411`.

That theorem proves that, on the published 18 exceptional core cells, arbitrary repartition into one-host blocks cannot beat the published nine-edge pairing for any `C>4`.  It explicitly names **changed exceptional support** as the next adversarial move.  This run executes that move locally and simultaneously specifies an actual physical block policy.

## 2. The actual physical block-selection policy

Consider the source-valid shared-host form with nine physical core coordinates

\[
X=\{x_0,\ldots,x_8\}
\]

and host coordinates whose switch-sets are disjoint subsets of base-false core cells.  The selector is:

> **Reveal the entire nine-coordinate physical core block `X` in one step.**

This uses only original coordinates.  There are no component labels, affine-coordinate charges, hidden selectors, or reused refunds.

For the pair-host family used below, after conditioning on `X=x`, the remaining function is either a constant or exactly one host literal, because the host switch-sets are disjoint and the selected core cell belongs to at most one host block.  Constants and characters have spectral entropy zero and Poincare defect zero.  Hence, for every balanced member `F` of this family,

\[
\Delta_X H=H(F),
\qquad
\Delta_X P=P(F)=\frac{I(F)-1}{4},
\tag{2.1}
\]

where `P(F)=I(F)/4-p_F(1-p_F)` and balance gives `p_F=1/2`.  Consequently the physical-block selector inequality at constant `C` is **exactly**

\[
\Delta_X H\le 4C\,\Delta_XP
\iff
\frac{H(F)}{I(F)-1}\le C.
\tag{2.2}
\]

Thus the core reveal is not a heuristic selector: on this current critical host-switch family it terminates the restriction tree in one physical step.  The only question is the exact balanced ratio.

I do **not** extrapolate this policy to arbitrary Boolean functions.  The existing addressing/fixed-coordinate obstruction, tensor replication obstruction, sparse-defect examples, and biased-limit failures in the shared research state rule out precisely that sort of unsupported coverage claim.  Majority/tribes/tensor behavior also cannot be replaced by this source-specific core geometry.

## 3. Source decomposition for a changed-support pair

The source base core is the same exact 512-cell Boolean core reconstructed in account01/B12's

`proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260922T011847Z-prime-n18-gate/REPORT.md`,
report blob `9ab98c0e82f7cf0f34eac98923df23b7b160670b`.

It has 247 true and 265 false cells.  The published nine disjoint source edges are

\[
\begin{aligned}
P_0=\{&(78,79),(113,121),(228,484),(170,186),(149,151),\\
      &(338,466),(284,316),(291,295),(393,457)\}.
\end{aligned}
\tag{3.1}
\]

Fix one source edge `E_j`, keep the other eight source edges unchanged, and replace `E_j` by an arbitrary distinct pair

\[
B=\{u,v\}
\]

of base-false core cells disjoint from the fixed sixteen cells.  This preserves exactly 18 switched cells, hence the resulting gate is balanced.  The replacement pair is not required to be an edge.

Let `f_0` be the signed base core, and for the resulting 18-cell support `T` define the empty-host Fourier numerator

\[
A_S=\sum_x f_0(x)\chi_S(x)-\sum_{x\in T}\chi_S(x),
\qquad S\subseteq[9].
\tag{3.2}
\]

The empty-host Fourier coefficient is `A_S/512`.

For any distinct two-point host block `B={u,v}`,

\[
W_B(S)=\chi_S(u)+\chi_S(v).
\]

Exactly half of the 512 core characters have `W_B=0` and half have `|W_B|=2`.  Therefore every distinct pair has the same host spectral entropy

\[
\boxed{H_B=\frac1{16}.}
\tag{3.3}
\]

Its host-plus-core influence is

\[
\boxed{
I_B=\begin{cases}
5/256,& |u\oplus v|=1,\\
11/512,& |u\oplus v|\ge2.
\end{cases}}
\tag{3.4}
\]

Indeed, the nonzero host spectrum is the codimension-one subspace orthogonal to `u xor v`; if the difference is a coordinate vector one core coordinate is forced absent, whereas otherwise every core coordinate is present on exactly half of that subspace.

Thus every candidate ratio is determined by the 512 integer numerators `A_S`, the exact core weights `|S|`, and whether the replacement pair is adjacent.

## 4. Rigorous exhaustive theorem: every nontrivial one-pair support replacement is far below `C_*`

The adjacent checker enumerates **all 277,875 non-identity replacements** described above.

For each integer numerator `r=|A_S|`, the entropy term is

\[
\frac{r^2}{2^{18}}
\left(18-2\log_2r\right).
\tag{4.1}
\]

The checker constructs a rational **upper** bound for (4.1) by using the positive atanh series for `ln`, with an explicit geometric tail bound, to obtain a rational lower bound for `log_2 r`.  It then rounds each term upward on a `10^{15}` integer scale.  Hence every reported entropy is an outward upper bound, not a floating-point estimate.

Influence is exact integer arithmetic with denominator `2^{18}`.  Across all candidates only 13 exact influence numerators occur.  The checker groups candidates by that exact numerator, retains the largest rigorous entropy upper bound at each level, and performs the final comparison with

\[
C_*=\frac{4076157}{625000}
\]

in exact rational arithmetic.

The result is

\[
\boxed{
\sup_{\text{nontrivial one-pair replacements}}
\frac{H(F)}{I(F)-1}
\le
\frac{1357333420684069}{209375000000000}
<6.482786486849284.
}
\tag{4.2}
\]

Therefore

\[
\boxed{
C_*-\sup R(F)
\ge
\frac{8179174315931}{209375000000000}
>0.0390647131507152.
}
\tag{4.3}
\]

One maximizing upper-bound witness is obtained by replacing `(78,79)` with `(14,78)`; its exact influence numerator is

\[
I(F)=\frac{536576}{262144}=2.046875.
\]

The published source gate itself is excluded from (4.2), and remains much closer to the center:

\[
R_0<6.521845710923046575658143972948578468366662293173<C_*.
\tag{4.4}
\]

Combining (2.2), (4.2), and (4.4) proves:

### Theorem 4.1 — local changed-support core selector

For the published pair-host gate and for every gate obtained by replacing any one of its nine host pairs by an arbitrary disjoint pair of base-false core cells, the physical selector `X={x_0,...,x_8}` satisfies

\[
\boxed{
\Delta_X H\le 4C_*\,\Delta_X P.
}
\tag{4.5}
\]

For every non-identity replacement the selector has the large quantitative reserve (4.3); the narrow case is the published source gate itself.

## 5. What this changes, and what it does not

**Old global missing implication:** prove `LIMIT-PRIME-GATE-LIFT-v1`, namely `D_{Gamma_*}(P;p)>=0` for every composition-prime Boolean gate and every product bias, or produce a genuine counterexample.

**New proved inference:** the actual nine-core physical block is a terminating paid selector for the strongest source-valid pair-host obstruction and for its entire one-host changed-support neighborhood.  The next adversarial move suggested by account03/B18 cannot succeed by changing only one source pair: every such nontrivial change drops the balanced ratio below `6.482787`, far away from `C_*`.

**Global missing implication after this run:** unchanged.  The theorem does not cover simultaneous replacement of two or more host blocks, a changed base core, overlapping/reused host channels, nonuniform product biases, or arbitrary composition-prime gates.  Those are genuine remaining directions.  In particular, this report does not convert a local rigidity theorem into universal coverage.

**Classification:** `AUXILIARY_ONLY`, deliberately.  The calculation is decisive for the current critical family and supplies the requested actual block policy, but it does not itself prove a new universal arrow in the conditional end-to-end argument.

## 6. Reproduction and privacy scope

`CHECKER.py` contains the exact base-core source strings, source pairs, rational atanh bounds, exact influence accounting, and exhaustive 277,875-candidate enumeration.  `CHECK_OUTPUT.txt` records `PASS`, 13 exact influence levels, the exact maximum ratio upper bound, and the exact positive gap to `C_*`.

Scoped review: the artifacts contain only FEI mathematics, public-in-repository source constants, logical account/slot labels, and source-bound hashes/paths.  They contain no credentials, scheduler IDs, machine paths, unrelated private data, email/Drive content, paid/remote compute actions, public-posting actions, or permission changes.
