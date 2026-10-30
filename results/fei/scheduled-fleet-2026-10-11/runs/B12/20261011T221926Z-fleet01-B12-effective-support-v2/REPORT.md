# B12 / A058 — effective Fourier support improves the overlap constant

**Run:** `20261011T221926Z-fleet01-B12-effective-support-v2`  
**Date:** 11 October 2026  
**Native stream:** B12, composition and decomposition  
**Primary packet:** A058, overlapping compositions  
**Attempt:** `B12-A058-ATTEMPT-003`  
**Stable gap:** `FEI-B12-A058-SPARSE-QUOTIENT-COLLISION`  
**Status:** `PROOF_CANDIDATE / SUPERSEDES V1 / FULL_FEI_OPEN`

## Exact movement

The preceding A058 candidate proved `H(K)<8I(K)` for the Boolean gate

`K(x,z)=1-2 1_{x=-1}1_{Lz in B}`

under `p=|B|/2^r<=1/4` and `log2(1/p)>=r/2`.  It left replacing the
crude quotient dimension by effective spectral support as the next
action.

This run performs that replacement and sharpens the same candidate,
rather than opening a third unreviewed B12 theorem.  Let

`M=#{alpha in F_2^r : Fourier(1_B)(alpha) != 0}`,

`d=log2(2M-1)`, and `ell=log2(1/p)`.  The revised result is:

### Effective-support overlap theorem (`PROVED`, review pending)

For every surjective `L:F_2^n->F_2^r` and every nonempty
`B subset F_2^r`, if

`p<=1/2` and `d<=2ell+1`,

then

`H(K)<6I(K)`.

Since `M<=2^r`, the earlier condition `ell>=r/2` remains a sufficient
condition.  Thus version 2 improves the constant from `8` to `6`,
drops the separate `p<=1/4` assumption in that corollary, and covers
additional quotient sets whose effective Fourier support is smaller
than the ambient quotient.

This is a restricted theorem, not full FEI and not a novelty claim.
Independent A090/A091 reconstruction remains pending.

## Work selection and source state

The current A059 contract was inspected first because A058 already had
two complete unreviewed artifacts.  Completing a new A059 theorem would
have created a third source-complete unreviewed B12 candidate, contrary
to `EXECUTION_PROTOCOL.json`.  This run therefore strengthens and
re-verifies the existing A058 candidate; version 2 supersedes version 1
and does not enlarge the stream's pending-candidate count.

The current governing blobs were unchanged from the preceding run:

| Source | Blob |
|---|---|
| `CURRENT_STATUS.md` | `8c9c63579ecdd4afa385bb94caf79ee6296addcf` |
| `STREAM_PACKET_INDEX.json` | `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704` |
| `assignments/B12.json` | `40935ac651643a17815d0addf664ec4c1c0313cc` |
| `EXECUTION_PROTOCOL.json` | `457358ff62cbf1141a72096bcabdf95bf18c1be2` |
| `PACKET_STATUS.json` | `3a5ca0894678a9fd9908aae9596923d3038a03f8` |
| `CLAIM_REGISTRY.json` | `6a3e1aa94f81ec01841a083c97449739b9e72baa` |
| `OBSTRUCTION_REGISTRY.json` | `dd482025647aed25166b46cc217a7ed77dcaa767` |

The newest canonical B12 report was read at open-problems commit
`21d81fc67d500fd7a0fd131d0694aeb055bf2036`, report blob
`401bf59495c18f5709c735b94c5c453021a3ef9b`.  Its Brain mirror was
read independently at the same blob.  Code search subsequently
resolved the default-branch artifact at commit
`1860d2e923f4357320d180b4ba44fc57ab458c2a`; no A090/A091 review of
the claim was found.

The original bent-splice proof remains pinned at
`source_material/reductions/paper/restrictions.tex`, blob
`55986205ce92bf93bbb2863b5064af001829844a`.  The source-corrected
overlapping-product obstruction remains blob
`4d9e18018cce12d361df613b1c6dbc80bb9627f1`.

The shared packet index remains stale relative to the immutable B12
runs; it was not edited because B20 owns reconciliation.

## Complete proof

Identify the data cube with `F_2^n`.  Let `L:F_2^n->F_2^r` be
surjective, `B` nonempty, `A=L^{-1}(B)`, and

`a_alpha=E_y[1_B(y)(-1)^(alpha·y)]`.

Then `a_0=p` and Parseval gives

`sum_alpha a_alpha^2=p`.

Because

`K(x,z)=1-1_A(z)+x 1_A(z)`,

the constant Fourier coefficient is `1-p`; the selector singleton has
coefficient `p`; and every nonzero `alpha` with `a_alpha!=0` creates
two coefficients, at `L^T alpha` and at the selector-plus-data
frequency, both of magnitude `|a_alpha|`.  Consequently the total
nonconstant mass is

`q=p^2+2 sum_{alpha!=0}a_alpha^2=2p-p^2`,

supported on at most `2M-1` atoms.  Conditional entropy maximization
at fixed mass yields

`H(K)<=h2(q)+q d`.                                         (1)

The selector influence is exactly `p`.  The data frequencies retain
the actual physical Hamming weights, giving

`I(K)=p+2 sum_{alpha!=0}|L^T alpha|a_alpha^2`

`    =p+I(1-2 1_A)/2`.                                    (2)

For `p<=1/2`, cube edge isoperimetry gives

`I(1-2 1_A)>=2p ell`,

hence

`I(K)>=p(ell+1)`.                                          (3)

For every `0<q<1`,

`h2(q)<=q log2(1/q)+q log2(e)`.                            (4)

Indeed, the second binary-entropy summand is at most `q log2(e)` by
`-ln(1-q)<=q/(1-q)`.  Since `q>=p`, equations (1) and (4) give

`H(K)<=q(ell+log2(e)+d)`

`    <=p(2-p)(3ell+1+log2(e))`,                            (5)

using `d<=2ell+1`.  Finally, `2-p<2` and
`1+log2(e)<3`, equivalently `ln 2>1/2`.  Therefore

`H(K)<2p(3ell+3)=6p(ell+1)<=6I(K)`.

This proves the theorem.  No disjoint-block chain rule was applied to
the shared parity inputs; their reuse is carried explicitly by
`|L^T alpha|` in equation (2).

## Stress tests and scope

- **Bent selector.** The result does not charge entropy to selector
  influence alone.  The full `p ell` data boundary in (3) is essential.
- **Rare events.** The logarithmic rare-event cost is preserved rather
  than replaced by `O(p)`.
- **Addressing.** No whole-set address label is charged repeatedly.
  General addressing functions need not meet the effective-support
  condition and are not claimed.
- **Near tensors.** The theorem itself concerns one shared-input gate.
  Any optional unrelated leaf multiplication remains honest disjoint
  tensorization.
- **Overlapping products.** The refuted universal inequality
  `H(fg)<=H(f)+H(g)` is not used.
- **Prime Boolean quotient gates.** Every quotient truth table `1_B`
  is allowed if its exact support count meets the displayed condition;
  the proof does not assume affine or factorizable `B`.
- **Fixed Renyi obstruction.** `M` is the exact support cardinality,
  not a fixed-order Renyi entropy.  No fixed-Renyi universal payment is
  asserted.
- **Parity-zero erasure.** Empty `B` is excluded and zero Fourier
  coefficients are omitted under `0 log(1/0)=0`.
- **Activation equivalence.** The explicit effective-support condition
  is not implied by rarity alone, so the theorem does not hide an
  arbitrary activated FEI core.

## Deterministic verification

Command:

`python3 check_effective_support_v2.py`

Environment: Python `3.12.14`; randomness `NONE`; observed runtime
`11.1` seconds.

The checker examined all `p<=1/2` quotient subsets through `r=4`, and
all subsets of sizes one through five at `r=5`: `282,200` sets total.
It found `245,432` satisfying the v2 effective-support condition,
including `52` outside the version-1 hypotheses.  Integer Walsh,
Parseval, support and edge-boundary calculations were exact; floating
point was used only for logarithms.

The maximum observed exact ratio was `3.739764017898052`.  The minimum
exact slack `6I-H` was `0.4237942466441154`; the minimum analytic slack
between `6p(ell+1)` and the upper bound (5) was
`0.3608804465268559`.  All checks passed.  This audits the formulas but
does not replace the all-dimension proof.

## Claim and review delta

Previous value: constant `<8`, conditions `p<=1/4` and `ell>=r/2`,
claim `B12-A058-SPARSE-QUOTIENT-OVERLAP-v1`, status
`PROOF_CANDIDATE`.

New value: constant `<6`, conditions `p<=1/2` and
`log2(2M-1)<=2ell+1`, claim version 2, same status.  Version 2
supersedes version 1.  The affine-defect candidate and this superseding
sparse-quotient candidate are the two complete unreviewed B12 claims.

Review request to A090: independently reconstruct the effective-
support count, entropy maximization, endpoint `p=1/2`, and strict
constant-six inequalities.  Review request to A091: independently
reconstruct the physical influence identity and isoperimetric payment,
including arbitrary overlap among the rows of `L`.

Next action: obtain or incorporate one of those reviews before opening
an A059 theorem.  If the revised claim survives, test whether the
coefficient `2` in the support condition `d<=2ell+1` can be enlarged
without violating exact prime quotient gates; any such work should be
a revision of this claim, not a third pending candidate.

No independent review, native Brain ingestion, full-FEI solution, new
worker, scheduler change, merge, deployment, or public release is
claimed.  Model and reasoning-effort telemetry were not exposed.
