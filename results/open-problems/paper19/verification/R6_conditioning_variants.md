# R6 verification: conditioning transfer for geometric variants

## Fixed-excess row submatrices

The proof of the deterministic conditioning transfer does not depend on selecting
exactly `m` rows.  For `A_m = D_m G_m Sigma_m^{1/2}` and any fixed `r >= 0`,

```tex
A_T = D_T G_T Sigma_m^{1/2},   |T|=m+r.
```

The same global singular-value bounds imply

```tex
(min_i d_i) sqrt(lambda_min(Sigma)) s_min(G_T)
  <= s_min(A_T)
  <= (max_i d_i) sqrt(lambda_max(Sigma)) s_min(G_T).
```

Taking the minimum over all `|T|=m+r` and using the `exp(o(m))` conditioning
hypothesis gives an `o(1)` difference after dividing logs by `m`.  Therefore the
proved fixed-excess lower side transfers.  The exact fixed-excess base remains
conditional on the tall pair-correlation theorem.

## Two-sided minors

For two-sided minors, the deterministic transfer is safe for diagonal row and
column scalings:

```tex
A = D G E,   A_{R,C}=D_R G_{R,C} E_C.
```

If the products of the minimum and maximum diagonal factors are `exp(o(k))`,
then the two-sided extremal log scale changes by `o(1)`.  Thus the proved
two-sided lower side transfers, and the exact base remains conditional on the
two-overlap second moment.

## Caveat

Do not replace diagonal column scaling by a general non-diagonal covariance in
the two-sided theorem.  Column selection does not commute with right
multiplication:

```tex
(G Sigma^{1/2})_{R,C}=G_R (Sigma^{1/2})_{:,C},
```

not `G_{R,C} Sigma_C^{1/2}`.
