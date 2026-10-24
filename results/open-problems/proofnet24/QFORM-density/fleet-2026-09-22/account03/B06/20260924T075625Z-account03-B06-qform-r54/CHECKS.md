# r54 deterministic checks

The committed `check_r54.py` was evaluated on 10,000 fixed-seed random symmetric rank-two indefinite 3x3 hub matrices. It checks only the finite-dimensional algebra used by the proof; it is not evidence for the probability inequalities by itself.

Output:

```
QFORM_B06_R54_CHECK_PASS
max_normalized_det_identity_error 2.2899950095657363e-15
max_normalized_zero_schur_error 9.225415354448772e-16
max_normalized_null_slope_error 5.5271421607602644e-15
```

The checked identities are:

1. `|det P_i| = kappa_F v_i^2` when `F` is symmetric rank two indefinite, `v` is its unit null vector, and `P_i` is the complementary physical 2x2 principal block.
2. The scalar Schur complement `F_ii-r_i^T P_i^{-1}r_i` vanishes.
3. For every affine hub vector `b=(c,d)` in that physical split, `gamma=d-c^T P_i^{-1}r_i=(v^T b)/v_i`.

The logarithmic averaging bounds in the report are proved analytically by layer cake and the cap-one/cap-two density bounds, not numerically.
