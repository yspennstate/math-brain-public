# account03/B06 r47 checks

These computations are finite sanity checks only; the symbolic arguments in `REPORT.md` are the proofs.

Running `check_r47.py` produced:

```text
QFORM_B06_R47_CHECK_PASS
max_projected_residual 8.164670392435785e-15
max_cut_factorization_error 1.2088396559389988e-14
cauchy_binet_error 1.7763568394002505e-15
partition_identity_error 4.440892098500626e-16
leverage_identity_error 1.1102230246251565e-16
paid_constant_16_times_64_pow_1_8 26.908685288118864
```

Checks performed:

1. For 1000 random rank-two shear frames `E`, symmetric `M`, and diagonal `D`, verified that `K=E^T M E+D` has vanishing projected off-diagonal anchored-`K` row residual to numerical precision.
2. For 1000 random cuts, verified the exact singular-product factorization
   `sigma_1 sigma_2 = |det M| sqrt(det(E_I E_I^T) det(E_J E_J^T))`.
3. For a random eight-column frame, verified Cauchy--Binet `det(EE^T)=sum_{p<q} det(e_p,e_q)^2`.
4. Exhaustively averaged all `2^8` bipartitions and verified
   `E[W_I W_J]=(1/16) sum_{P cap Q=empty} w_P w_Q`.
5. Verified that the normalized pair-law vertex marginal equals the whitened two-frame leverage
   `alpha_h=e_h^T(EE^T)^(-1)e_h`.
