# B12 / A058 — sparse quotient unions pay low-energy collision debt

**Run:** `20261011T212319Z-account01-B12-sparse-quotient-overlap`  
**Date:** 11 October 2026  
**Native stream:** B12, composition and decomposition  
**Primary packet:** A058, overlapping compositions  
**Attempt:** `B12-A058-ATTEMPT-002`  
**Stable gap:** `FEI-B12-A058-SPARSE-QUOTIENT-COLLISION`  
**Status:** `PROOF_CANDIDATE / DELIVERED_FOR_REVIEW / FULL_FEI_OPEN`

## Result and mathematical delta

The previous B12 result covered one affine disagreement coset and
proved a constant `4`.  Its stated next action proposed a two-coset
union.  That proposal is degenerate: over `F_2`, any two quotient
points form one affine line, so their preimage is again a single
affine coset of codimension one less.  This run corrects that handoff
and treats the first genuinely new case: a sparse, possibly non-
affine union of at least three quotient cells.

Let `L:F_2^n -> F_2^r` be surjective, let `B` be a nonempty subset of
the quotient, set `A=L^{-1}(B)` and `p=|B|/2^r`, and define the genuine
Boolean gate

`K(x,z)=1-2 1_{x=-1}1_A(z)`.

The parity rows of `L` may reuse physical coordinates arbitrarily.
The branches have inner product `1-2p`, and the selector influence is
exactly `p`, which can tend to zero.  Thus this is outside the already
proved neighboring-orthogonality and uniform-positive-selector-energy
closures.

### Main theorem (`PROVED`, pending independent review)

If `p<=1/4` and `log2(1/p)>=r/2`—equivalently, it is enough that
`|B|<=2^(r/2)` together with `p<=1/4`—then

`H(K) < 8 I(K)`.

If a disjoint Boolean leaf `w` satisfies `H(w)<=C I(w)`, then honest
tensorization gives `H(wK)<max(C,8)I(wK)`.  This last corollary is
explicitly disjoint; no false shared-variable product inequality is
used.

This is a new restricted composition class within A058, not a proof of
full FEI and not a literature-priority claim.  A090/A091 review remains
unobserved.

## Sources actually used

The current compact campaign files and their Brain mirrors were read
before the argument.  Exact open-problems blobs were:

| Source | Blob |
|---|---|
| `CURRENT_STATUS.md` | `8c9c63579ecdd4afa385bb94caf79ee6296addcf` |
| `STREAM_PACKET_INDEX.json` | `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704` |
| `assignments/B12.json` | `40935ac651643a17815d0addf664ec4c1c0313cc` |
| `EXECUTION_PROTOCOL.json` | `457358ff62cbf1141a72096bcabdf95bf18c1be2` |
| `PACKET_STATUS.json` | `3a5ca0894678a9fd9908aae9596923d3038a03f8` |
| `CLAIM_REGISTRY.json` | `6a3e1aa94f81ec01841a083c97449739b9e72baa` |
| `OBSTRUCTION_REGISTRY.json` | `dd482025647aed25166b46cc217a7ed77dcaa767` |

The corresponding Brain files had byte-identical blobs.  GitHub code
search resolved the inspected default-branch snapshot at
`87f7c6267e56e7a0eb5b8dfd572a6eaaecae6907`; the blob pins above are
the exact content identities relied on.

The prior complete B12 report was read from open-problems commit
`b5f4d89bf4429d287e03df871b95706e54802328`, path
`reports/fei-2026-10-11/runs/B12/20261011T201902Z-account01-B12-affine-defect-overlap/REPORT.md`,
blob `421da5bb30fdf6a68ef19697369a21f91997fb69`.  Its mirrored Brain
handoff is at commit `84eb6aa2c47b02025457f3e99d3c4c4dc705940e`.

Relevant original arguments inspected were:

- the restriction manuscript's exact bent-splice proof,
  `source_material/reductions/paper/restrictions.tex`, blob
  `55986205ce92bf93bbb2863b5064af001829844a`;
- the source-corrected overlapping-product note, blob
  `4d9e18018cce12d361df613b1c6dbc80bb9627f1`, which pins the prior
  refutation of unrestricted `H(fg)<=H(f)+H(g)`;
- the supplemental native mapping, blob
  `27ec2c0d811b9145acb413d518805ecc8c321fc7`.

The shared aggregate `PACKET_STATUS.json` had not yet adopted the prior
immutable A058 candidate.  This run therefore imports the original
artifact directly and does not edit shared state; reconciliation is
reserved to B20.

## Exact coefficient ledger

For `alpha in F_2^r`, write

`a_alpha = E_z[1_A(z)(-1)^(alpha·Lz)]`.

Surjectivity of `L` identifies these with the normalized Fourier
coefficients of `1_B`, so

`a_0=p` and `sum_alpha a_alpha^2=p`.

The gate has the exact decomposition

`K(x,z)=1-1_A(z)+x 1_A(z)`.

Hence its constant coefficient is `1-p`; for every nonzero `alpha`,
the data frequency `L^T alpha` has coefficient `-a_alpha` and the
selector-plus-data frequency has coefficient `a_alpha`; the selector
singleton has coefficient `p`.  The total nonconstant spectral mass is

`q=p^2+2 sum_{alpha!=0}a_alpha^2=2p-p^2`.

There are at most `2^(r+1)-1` nonconstant atoms.  Maximizing entropy
inside the nonconstant sector at fixed mass gives

`H(K) <= h2(q)+q log2(2^(r+1)-1) < h2(q)+q(r+1)`.          (1)

The selector contribution to influence is exactly `p`.  The two data
sectors give

`I(K)=p+2 sum_{alpha!=0}|L^T alpha|a_alpha^2`.

For `D_A=1-2 1_A`, its nonzero Fourier coefficients are `-2a_alpha`,
so the exact physical-input identity is

`I(K)=p+I(D_A)/2`.                                        (2)

This formula keeps all coordinate reuse: the weights are the actual
physical Hamming weights `|L^T alpha|`, not quotient degrees.

The weak cube edge-isoperimetric inequality gives, for `p<=1/2`,

`I(D_A)>=2p log2(1/p)`.

Writing `ell=log2(1/p)`, equation (2) yields

`I(K)>=p(1+ell)`.                                         (3)

If `p<=1/4`, then `q<=1/2`.  For `q<=1/2`, the second summand of
`h2(q)` is no larger than the first, so

`h2(q)<=2q log2(1/q)<=4p ell`.

Also `q(r+1)<=2p(r+1)`.  Combining with (1) and (3),

`H(K)/I(K) < [4ell+2(r+1)]/(ell+1)`

`             = 4 + 2(r-1)/(ell+1) < 8`,

because `ell>=r/2`.  This proves the theorem.  The logarithmic cost of
the rare label is paid by the actual data boundary, not by the
vanishing selector influence.

## Stress tests and obstruction memory

- **Bent splice / selector-only payment.** The original construction
  has selector influence `2^{-m}` and local entropy ratio at least
  `m-1`.  Nothing here bounds entropy by selector influence alone;
  equation (3) uses the full boundary of `A`.
- **Rare restrictions and sparse defects.** The proof retains the
  necessary `p log(1/p)` term exactly through edge isoperimetry.
- **Addressing and activation equivalence.** The theorem assumes
  `log2(1/p)>=r/2`.  Whole-set addressing or arbitrary activated
  pieces need not satisfy this support-density condition and are not
  claimed.
- **Near tensors.** Only the final `wK` corollary uses disjoint
  tensorization.  The overlapping parity rows are already handled in
  (2), without tensorizing them.
- **Shared-variable products.** The guard `O-OVERLAP-PRODUCT` is
  respected: no inequality `H(fg)<=H(f)+H(g)` is invoked.
- **Prime quotient gates.** The proof allows every indicator `1_B`,
  including irreducible/non-affine quotient truth tables, subject only
  to the explicit sparsity condition.  The finite checker exhausts all
  such `B` through quotient dimension five; it does not infer a general
  prime-gate closure beyond the proved hypotheses.
- **Parity-zero erasure.** Empty `B` is excluded.  Fourier zeros are
  simply omitted under the stipulated `0 log(1/0)=0` convention.

## Exact finite verification (`NUMERICAL` only for logarithms)

Command:

`python3 check_sparse_quotient.py`

Python `3.12.14`; no randomness.  The checker exhaustively enumerated
all `245,380` nonempty subsets `B` for `2<=r<=5` satisfying the theorem
hypotheses, using integer Walsh transforms, exact integer Parseval and
boundary counts, and floating evaluation only for logarithms.  It also
checked all `650` two-point subsets for the affine-line collapse.

The maximum observed exact ratio was `3.739764017898052`; the minimum
support-entropy-bound slack was `0.001397817206548080`; all cases passed
`H<=8I`.  These checks audit the formula and endpoints but are not a
substitute for the all-dimension proof.

## Status, review, and next action

Previous tracked scope: one affine quotient cell, constant `<4`,
`PROOF_CANDIDATE`, A090/A091 review pending.

New tracked scope: every quotient union with `p<=1/4` and
`log2(1/p)>=r/2`, including genuine non-affine unions, constant `<8`,
`PROOF_CANDIDATE`, A090/A091 review pending.  Mathematical movement is
the increase from one cell to as many as `2^(r/2)` cells with a complete
coefficient and physical-boundary ledger.  The unchanged-obstruction
counter is zero because the prior exact target was enlarged.

There are now two complete unreviewed A058 candidates in this stream,
so the next action is not to create a third broad theorem.  A090 should
adversarially reconstruct the support-entropy maximization, physical
normalizations, two-cell collapse, and separation from C035.  A091
should independently reconstruct the edge-isoperimetric payment and
the optional tensor corollary.  After review, the next mathematical
extension is to replace quotient support size `2^r` by an effective
spectral-support or Rényi quantity while preserving equation (2),
seeking a condition that covers denser unions without reverting to a
selector-only payment.

No independent review was observed in this run.  No native Brain
ingestion, full-FEI solution, new worker, schedule change, merge, or
deployment is claimed.
