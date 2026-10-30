# B19 / A091 — review of B12 adjacent two-coset payment

**Run:** `20261013T081921Z-fleet01-B19-b12-adjacent-two-coset-review-a091`  
**Primary packet:** A091 (Composition referee)  
**Reviewed target:** B12/A057 run `20261013T073110Z-fleet01-B12-adjacent-two-coset`  
**Target report blob:** `fbf1b90d96033a4c07a7ca0f55ba6a4ff3c656a0`  
**Verdict:** local theorem ACCEPTED; hierarchy corollary REFUTED at stated scope.  
**Full FEI:** OPEN.

## Claim-by-claim verdict

| Claim | Verdict | Exact scope |
|---|---|---|
| `B12-A057-TWO-AFFINE-ADJACENCY-v1` | **INDEPENDENTLY ACCEPTED** | Every pair of nonempty disjoint affine cosets; arbitrary physical adjacency, codimensions, and spectral overlap; one local genuine-Boolean splice; nats. |
| `B12-A057-JOINING-COLUMN-RANK-v1` | **INDEPENDENTLY ACCEPTED** | The submitted quotient-column rank inequality, with every physical coordinate counted. |
| `B12-A057-HADAMARD-COLLISION-REFUND-v1` | **INDEPENDENTLY ACCEPTED** | The common-annihilator collision of two disjoint affine cosets does not increase raw spectral entropy. |
| `sum_v w_v Omega_v <= 8 ln(2) I(b)` for every adaptive nonreusing hierarchy of restrictions of one source | **REFUTED AS STATED** | Pathwise nonreuse of revealed coordinates does not make the full reached-source influence charged by the local theorem single-use. |

The accepted local result is
\[
\Omega\le8\ln2\,I(d),
\]
and \(8\ln2\) is the sharp supremum.  It removes the preceding distance-two
hypothesis and improves the earlier constant \(16\ln2\) by a factor of two.

## Independent reconstruction

The proof was reconstructed from the original artifact rather than from its
status label.  The three essential steps all hold:

1. On the common annihilator \((V+W)^\perp\), disjointness makes the relative
   phase a nontrivial character, so exactly half of the coefficients add and
   half subtract.  The normalized Hadamard entropy bound gives
   \(\mathcal E(s)\le2\ln2(xk_1+yk_2)\).
2. If \(q\) coordinate directions join the two cosets, the exact physical
   cancellation is
   \(I(s)=(xm_1+ym_2)/2-qxyr\).  The joining columns have only one-dimensional
   image in the further quotient, yielding
   \(m_j\ge\max(k_j,q+\ell-1)\).  The submitted integer inequality then gives
   \(xk_1+yk_2\le2I(s)+p\).
3. Selector coefficient pairing gives
   \(\Omega=\mathcal E(s)+C(p)\) with \(C(p)\le0\), while
   \(I(d)=I(s)/2+p/4\).  These identities give the claimed constant exactly.

The full derivation is in `PROOF_RECONSTRUCTION.md`.

## Precise failure of the hierarchy transfer

The local theorem charges \(I(d_v)\), the full influence of every reached
source.  The standard nonreuse derivative ledger controls only influence on
the newly owned/query blocks.  In general,
\[
\sum_vw_v I(d_v)\nleq I(b).
\]

An exact finite falsifier is obtained from the submitted checker’s extremal
pair \(A=\{0\}\), \(B=\{1,2\}\subset\mathbb F_2^4\).  Here
\[
\Omega=0.507167337318501\ldots,\qquad I(d)=11/64.
\]
Adjoin two free coordinates and reveal them at two successive tree levels.
The tree is pathwise coordinate-nonreusing, all reached sources are
restrictions of one source and retain the required two-coset form, and the
weighted charge is \(2\Omega\).  But
\[
2\Omega=1.014334674637002\ldots
>8\ln2\,(11/64)=0.953077373269924\ldots.
\]
Thus the hierarchy sentence must be removed or strengthened with an actual
single-use ownership hypothesis.

The minimal repair is to prove a directional local estimate
\(\Omega_v\le8\ln2 I_{B_v}(b_v)\) on explicitly owned blocks, or to impose an
edge-disjoint support condition that directly makes the complete local
influence packets single-use.  Neither follows from pathwise coordinate
nonreuse alone.

## Verification

`CHECK_REVIEW.py` is independent of the submitted checker.  It uses exact
rational Walsh transforms and 90-digit evaluation only for logarithms.  It
checked:

- all 23,000 disjoint affine-coset pairs through four variables;
- all 23,000 local \(8\ln2\) inequalities;
- all 23,000 Hadamard collision refunds;
- 518,400 rank-scalar tuples;
- the exact two-free-coordinate hierarchy falsifier.

Randomness: none.  The all-parameter local result is proved analytically;
finite enumeration is corroboration.

## Primary-literature scope

O'Donnell--Tan's composition theorem applies to functions on disjoint input
blocks and an outer product-biased `FEI+` inequality; it does not supply this
shared-variable signed associator.  Wan--Wright--Wu prove decision-tree/read-k
bounds whose constants retain the read parameter; they do not justify the
rejected full-influence telescope.  Potapov's plateaued and partially bent
theorems cover flat/plateaued spectral classes; a general non-affine union of
two affine cosets has several spectral magnitudes and is not covered merely by
that classification.  The local B12 result is therefore a legitimate proper-
class extension, but its hierarchy step is not supplied by prior literature.

## Status and next unpaid step

This review accepts a one-node two-coset collision payment, not a depth-uniform
hierarchy theorem and not full FEI.  The next exact task is to strengthen the
local proof so its right side uses only a declared owned derivative block, then
test that strengthened statement on adjacent two-coset restrictions before
moving to three-piece collision graphs.

No protected source, held payload, public release, scheduler change, new
worker, or native-state mutation was used.
