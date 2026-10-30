# Known falsifiers and controls for B10-A046-HALF-BIAS-TAX v1

The frozen candidate is

\[
J_A\le M_A+\tfrac12\Delta_A(p).
\]

It is **OPEN**.  The coefficient-one theorem is independently accepted at its exact local scope; the coefficient one-half is a new candidate, not a theorem.

## Direct boundary controls

- The tax-free claim `J_A<=M_A` is refuted by the genuine two-bit AND sign at `p=1/8,q=1/4`, with the corrected rational certificate `J_A-M_A>0.1195` bits.
- For the same AND family and fixed `q`,
  \[
  \frac{J_A-M_A}{\Delta(p)}\longrightarrow4q(1-2q)
  \]
  as `p downarrow 0`.  The maximum over `q in (0,1/2)` is exactly `1/2`, attained at `q=1/4`.  Thus every coefficient below one-half is refuted.
- This lower-bound family saturates but does not prove the frozen half-tax candidate.

## Mandatory distinct controls

- `O-B05 / B05_RARE_REFUNDS`: rules out fixed local all-coordinate refunds.  It does not refute a logarithmic bias tax.
- `O-PIVOTAL-ONE / WEIGHTED_PIVOTAL_CREDIT`: refutes a different coefficient-one pivotal-credit proposal.  It is not evidence for or against the half-tax formula.
- `O-PHYSICAL-TC` and `O-COORD-PHYSICAL-TC`: weighted-threshold conditional-TC failures concern different quantities.
- `O-RAW-CONV / RAW_CONV_TENSOR`: raw collision `L` is not tensor additive.  The present Shannon restriction ledger is exactly additive only for disjoint tensor products.
- `FIXED_CONV_PREFIX` and `FIXED_CAP_PREFIX`: non-Boolean prefix laws do not establish or refute this Boolean restriction inequality.
- Fixed-reserve repairs such as the obsolete `0.337/0.34` numerical tuning are not versions of this formula and remain retired.
- `O-RENYI`: the point defect has `H_alpha/I -> infinity` for every fixed spectral Renyi order `alpha<1`, while Shannon `H/I->4`.  This does not refute auxiliary piece Renyi quantities, and the frozen candidate uses Shannon conditional entropy only.
- `O-ACTIVATION-EQUIV`: a rare activated core can retain arbitrary FEI difficulty.  Even a proved half-tax local lemma would still need a nonreusing global payment plus terminal entropy.

## Finite diagnostic performed here

All 16 two-bit Boolean truth tables, both singleton reveals, and 235 biases in each coordinate were tested: 1,767,200 instances.  No grid violation was observed; the maximum ratio was `0.49303368801064995`, at the rare revealed bias `2^-40` and the other bias `1/4`.  This is numerical evidence only and does not cover continuum biases or higher arity.
