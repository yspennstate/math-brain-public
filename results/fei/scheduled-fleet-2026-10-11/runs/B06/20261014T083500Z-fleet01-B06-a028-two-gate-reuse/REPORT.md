# B06 / A028 — first branch-reused stopping block with arbitrary terminal core

**Status:** proved for the stated all-dimensional disjoint-product family; independent review pending. Universal shared-data stopping, universal GU, and full FEI remain open.

## Frozen target

- Primary packet: **A028**.
- Stable gap: `G-GU-STOPPING-RESIDUAL`.
- Claim: `B06-A028-TWO-GATE-REUSE-v1`.
- Prior bound: the independently accepted paid-boundary theorem reduces universal stopping to one aggregate residual inequality with terminal \(U\), exact influence decrement, and branchwise coordinate reuse retained.

The selected first-reuse case is
\[
F(x_1,x_2,y)=q(x_1,x_2)h(y),
\]
where \(q\) is any two-bit Boolean gate and \(h\) is an arbitrary Boolean core of unrestricted dimension on disjoint coordinates. Query \(x_1\), then query the same physical coordinate \(x_2\) on both children.

## New theorem

For the resulting tree,
\[
\boxed{\mathcal R(\mathcal T)\le\Pi_I(\mathcal T)=I(q),}
\]
while the four leaves are \(\pm h\) and retain exactly
\[
\mathbb E U(F_\ell)=U(h),\qquad \mathbb E I(F_\ell)=I(h).
\]
Thus the paid-boundary residual holds with \(A=1,b=0\), with no dependence on the core dimension or complexity. The proof uses
\[
U(F)=U(q)+U(h),\qquad I(F)=I(q)+I(h),
\]
the exact tree telescopes, nonnegativity of every subtracted root-KL row, and the complete two-bit classification \(U(q)\le I(q)\).

The proof is query-order independent: every physical tree that resolves the two gate coordinates has the same terminal ledger and only subtracts nonnegative root rows. Hence the nonreuse restriction is removed completely within this product family.

## Exact GU implication

For every \(0\le b<1\), every two-bit Boolean gate satisfies
\[
G(q)\le(2-b)I(q)+bU(q).
\]
Consequently, if the arbitrary core satisfies
\[
G(h)\le aI(h)+bU(h),
\]
then
\[
\boxed{G(F)\le\max\{a,2-b\}I(F)+bU(F).}
\]
Adjoining this entire branch-reused gate family therefore preserves an admissible universal coefficient \(b<1\).

## Verification

`verify_two_gate_reuse.py` checks all 16 two-bit gates against every Boolean core through dimension three and seeded cores through dimension six. It independently reconstructs \(U,I,G\), tensor additivity, the reused depth-two tree, exact terminal values, root-row payments, and the displayed GU transfer.

## Remaining obstruction

The first unsupported extension is shared data: if different gate branches modify or select unequal cores, the tensor factorizations disappear. A universal next step must bound that collision while preserving the signed \(-\Gamma_i\) refund and nonzero terminal \(U\); the present theorem does not assume arbitrary-leaf FEI.

## Status distinctions

This result is mathematically proved at the stated restricted scope and saved with complete code and outputs. Independent review and native Brain ingestion are not claimed. Model/effort metadata: `UNKNOWN`.
