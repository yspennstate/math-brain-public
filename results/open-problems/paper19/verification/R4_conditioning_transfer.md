# R4 verification: deterministic row/column conditioning transfer

## Statement checked

Let `G_m` be the iid Gaussian matrix and

```tex
A_m = D_m G_m Sigma_m^{1/2},
```

where `D_m` is a positive deterministic row diagonal matrix and `Sigma_m` is
positive definite.  If

```tex
(1/m) log( min_i d_i sqrt(lambda_min(Sigma_m)) ) -> 0
(1/m) log( max_i d_i sqrt(lambda_max(Sigma_m)) ) -> 0,
```

then the extremal row-submatrix log scale of `A_m` is the same as that of
`G_m`.

## Proof audit

For every row set `T`,

```tex
A_T = D_T G_T Sigma_m^{1/2}.
```

The singular-value inequalities give

```tex
min_i d_i sqrt(lambda_min(Sigma_m)) s_min(G_T)
  <= s_min(A_T)
  <= max_i d_i sqrt(lambda_max(Sigma_m)) s_min(G_T).
```

The constants are independent of `T`, so they survive taking the minimum over
all row sets.  Taking logs and dividing by `m` gives a deterministic error
trapped between the two displayed logarithmic conditioning factors, both
`o(1)`.

The theorem then imports Shmalo's Gaussian limit for `G_m`.  No independence or
new second-moment estimate is needed after the deterministic comparison.

## Limitations

This covers common covariance, deterministic row weights, and product variance
profiles.  It does not cover arbitrary variance profiles `sigma_ij g_ij`,
because there is no uniform left/right factorization and the extremal row set
may prefer particular row types.
