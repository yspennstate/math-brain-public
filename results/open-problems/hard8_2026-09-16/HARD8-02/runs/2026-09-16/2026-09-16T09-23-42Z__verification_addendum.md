# HARD8-02 — verification addendum — 2026-09-16T09:23:42Z

This append-only note records the exact computation and GitHub receipts for

`hard8_2026-09-16/HARD8-02/runs/2026-09-16/2026-09-16T09-20-27Z__report.md`.

## Main report receipt

Creation commit:

`05532a5ba46489975dc472cd54652d48bc112815`

The report was read back at that exact commit. GitHub returned blob SHA

`faaf62d1867a662354f5c473b4bc57a35fbbcae2`

and the expected title plus theorem summary. Therefore the mathematical report is **VERIFIED**.

## Exact verifier receipt

Artifact:

`hard8_2026-09-16/HARD8-02/artifacts/2026-09-16T09-20-27Z__repeated_star_absorber_verifier.py`

Creation commit:

`c7a76d8293a9b0b26345bdf0e54f2179cb3e3d13`

The source was read back at that exact commit. GitHub returned blob SHA

`88611d9004270d3f7104edafccadb2d02ea0f5f5`.

Therefore the source artifact is **VERIFIED**.

## Actual completed exact run

The locally identical standard-library source was executed as

`python /mnt/data/hard8_02_star_absorber_verifier.py`

and completed with

```text
PASS
absorber_cases 399
pinned_augmentation_cases 399
graft_transfer_cases 798
sum_identity_cases 13776
tiny_c2_successes 0
max_k 20
max_h_construction 20
max_c_sum_grid 41
```

Interpretation:

* 399 closed-form repeated-star absorbers were checked for every `0<=k<=20` and `2<=h<=20`;
* all 399 corresponding pinned augmented trees were checked to have vertex labels `0,...,m` and edge differences exactly `1,...,m`;
* both low-branch and high-branch one-gap graft formulas were checked in all 399 parameter cases, for 798 exact transfer checks total;
* every transfer had the claimed crossing vector `0^K 1^*`, the claimed new boundary-root label, and the exact recurrence `2K+1=(2h-1)(2k+1)`;
* 13,776 independent integer instances of the necessity identity
  
  `2(S_actual-S_required)=c(h-1)(c-2k-1)`
  
  were checked over `1<=c<=41`, `2<=h<=17`, `0<=k<=20`;
* the smallest obstructed case `k=1,h=2,c=2` was exhaustively checked over both possible leaf matchings and had zero successes, while the closed-form `c=3` construction passed.

The verifier uses only exact integer arithmetic and Python's standard library. It uses no floating point, randomized search, SAT/ILP solver, or timeout-based inference.

The finite checks are consistency tests. The arbitrary-parameter repeated-star theorem and suffix-root transfer theorem are established by the symbolic proofs in the main report.

## Status

**OPEN.** The full graceful tree conjecture is not resolved. The durable progress in this checkpoint is the exact absorber/pinned-tree equivalence, the general suffix-root transfer theorem, and the sharp `c=2k+1` classification with an explicit construction for repeated centred-star components.
