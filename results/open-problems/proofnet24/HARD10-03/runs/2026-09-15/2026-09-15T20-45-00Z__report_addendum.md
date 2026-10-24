# HARD10-03 — finite-state certificate addendum

This addendum belongs to

`proofnet24/HARD10-03/runs/2026-09-15/2026-09-15T20-27-00Z__report.md`

commit

`0e0db2eb2557583ccba849bf41b203036887a06f`

read back at that exact commit with blob

`ae45a5f01a06494bb6b0670a64bf2d34a88c5598`.

The main report is therefore **VERIFIED** for GitHub delivery. Mathematical verification remains self-review.

## Reproducible checker

The finite-state checker was archived append-only at

`proofnet24/HARD10-03/artifacts/2026-09-15T20-39-00Z__adaptive_unique_cycle_check.py`

commit

`6c7c8fe60ef17ffa23914114815d2fe668f28810`

and read back at that exact commit with blob

`25cd9b1d916c7d30f5c1b14d677b08a727cdaa8e`.

The code artifact is therefore **VERIFIED** for GitHub delivery.

## What the checker does

On the four-cycle it fixes a concrete admissible partial space-time exposure history:

* edge `(0,1)` is exposed for the full period, with one known mark at time `0.25`;
* edge `(2,3)` is exposed only on `[0,0.5]`, with one known mark at time `0.40`;
* all other edge-time regions remain fresh Poisson.

Conditional on this history, the remaining interchange process is time-inhomogeneous. The script computes both the full conditional permutation law on `S_4` and the conditional one-particle propagator by exact finite-state matrix exponentiation.

It then checks:

1. the one-particle propagator reconstructed from the full permutation law;
2. `NEW-L28`, `E det(I-A Pi | F)=det(I-AK^F)`, for eight seeded dense test matrices `A`;
3. `NEW-L30` for `S={0,1}` by direct enumeration of permutations;
4. the elementary geometric-series resolvent estimate used in `NEW-L31` on `S={0}`.

## Executed numerical output

The checker was executed in the research runtime and returned:

```text
one_particle_kernel_error                 = 1.6653345369377348e-16
conditional_determinant_max_error         = 3.3306690738754696e-16
unique_anchor_cycle_identity_error        = 5.551115123125783e-17
unique_anchor_cycle_probability_S01       = 0.3127645721877772
unique_anchor_cycle_rhs_S01               = 0.31276457218777715
singleton_row_sum_q                       = 0.07006287588828532
singleton_entry_bound_a                   = 0.07006287588828532
singleton_resolvent_diag                  = 0.07534151941208937
singleton_a_over_1_minus_q                = 0.07534151941208937
singleton_fixed_point_probability         = 0.07006287588828533
nonselfadjointness_max                    = 0.0022186357646802324
```

All programmed assertions passed. The nonzero nonselfadjointness confirms that the check is not accidentally restricted to a symmetric conditional kernel.

These computations are finite-state sanity checks only. They do not constitute an independent proof, do not establish the infinite-volume conjecture, and do not upgrade any conditional/restricted statement in the main report.
