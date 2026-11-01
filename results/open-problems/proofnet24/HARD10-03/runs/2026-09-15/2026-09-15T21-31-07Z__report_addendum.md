# HARD10-03 — correction/checker addendum

This addendum belongs to

`proofnet24/HARD10-03/runs/2026-09-15/2026-09-15T21-28-05Z__report.md`

created in commit

`acba544088d7372816381c27f8cc8aa156630f5b`

and read back at that exact commit with blob SHA

`794e297cfe36c1517dba03454969d2a2b7f7247f`.

The mathematical Markdown checkpoint is therefore **VERIFIED for GitHub delivery**. Mathematical correctness remains self-review.

## Finite-state checker

The append-only checker is

`proofnet24/HARD10-03/artifacts/2026-09-15T21-30-03Z__diagonal_cluster_correction_check.py`

created in commit

`8f86caa1e0c5397fd918be172dfe046f62adf3d2`

and read back at that exact commit with blob SHA

`8b9a24698b675701971d1bb97ba33910f4df9596`.

The code artifact is therefore **VERIFIED for GitHub delivery**.

Its executed output was archived at

`proofnet24/HARD10-03/artifacts/2026-09-15T21-30-03Z__diagonal_cluster_correction_check_output.json`

created in commit

`1275941302f9f234ee8e787db8ed7e76dbfa446b`

and read back at that exact commit with blob SHA

`06260bb8837c84af10b965915bc7f44afd56bfec`.

The output artifact is therefore **VERIFIED for GitHub delivery**.

## Executed checks

The checker uses the same concrete time-inhomogeneous conditional law on the four-cycle as the previous adaptive-exposure certificate. The conditional one-particle kernel is genuinely non-self-adjoint.

Executed values:

```text
conditional_kernel_reconstruction_error      = 1.6653345369377348e-16
conditional_kernel_nonselfadjointness         = 0.0022186357646802324
old_offdiag_actual_unique_same_cycle          = 0.25713473047151847
old_offdiag_claimed_rhs                       = 0.42809899531926343
old_offdiag_claim_gap                         = 0.17096426484774496
conditional_two_anchor_lhs_p2_minus_p1        = -0.22234198363606356
conditional_two_anchor_rhs                    = -0.22234198363606342
conditional_two_anchor_error                  = 1.3877787807814457e-16
unconditioned_p1_same_unique_cycle            = 0.12046302310630444
unconditioned_p2_two_distinct_cycles          = 0.15817219993649878
unconditioned_pair_compensation               = 0.03770917683019434
unconditioned_shadow_dpp_exact_pair           = 0.0377091768301966
unconditioned_dpp_pair_inclusion_bound        = 0.04361132829768967
```

All programmed assertions passed.

The `0.170964...` gap is a direct finite-state counterexample to the withdrawn off-diagonal same-cycle interpretation. It does **not** contradict the master determinant identity. The mixed diagonal two-anchor identity agrees to about `1.4e-16` in the same non-self-adjoint conditional example.

In the ordinary unconditioned reversible law, the pair compensation is positive, agrees with the shadow-DPP exact-pair probability to numerical precision, and is below the DPP two-point inclusion determinant as stated in `NEW-L34`.

These calculations are finite-state sanity checks only. They do not constitute an independent proof and do not resolve the `Z^3` conjecture.
