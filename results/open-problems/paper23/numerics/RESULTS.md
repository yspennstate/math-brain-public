# Numerical verification of the product least-sv rate

`verify_product_rate.py`, seed base 8000/10000, real Gaussian entries N(0,1/N),
square supports density 1/2. rho_k = -(1/N) log min. Predictions: rho_1 -> 2H = 1.386,
rho_k -> (k+1)H (this paper's Theorem), vs the earlier guess rho_2 -> 2H (paper22 conj:B4).
Discriminator: rho_2/rho_1 -> 1.5 (this paper) vs 1.0 (conj:B4).

```
N=8 m=70 trials=8
  rho_1 (exhaustive)      mean 1.375   2H=1.386
  rho_2 (cascade, achiev) mean 1.949   3H=2.079
  rho_2 (exhaustive)      mean 2.087   3H=2.079
  ratio rho2/rho1 (exh)   mean 1.529   (B4=1.0, cascade=1.5)

N=10 m=252 trials=4
  rho_1 (exhaustive)      mean 1.579
  rho_2 (cascade, achiev) mean 2.338   3H=2.079
  ratio rho2/rho1 (casc)  mean 1.498   (B4=1.0, cascade=1.5)
```

Reading. At N=8 the full exhaustive rho_2 = 2.087 sits on 3H = 2.079, and the exhaustive
ratio rho_2/rho_1 = 1.53 is at the cascade prediction 1.5, cleanly separated from the
conj:B4 value 1.0. The greedy cascade (two-sided-optimal F_1 then one-sided-optimal S_2)
tracks the exhaustive min from above, confirming it is the achieving construction. The
theorem rho_k = (k+1)H(alpha)/dF is supported; the earlier product conjecture 2H is refuted.
```

## Anisotropic one-sided scaling (the cascade step)

`verify_anisotropic_onesided.py`: M is N x n with i.i.d. rows ~ N(0, Sigma),
Sigma = diag(1,...,1,eps^2). Prop:aniso-mean predicts min over row-supports of smin(M[T,:])
~ sqrt(n*lambda_min)*(isotropic min) = eps*sqrt(n)*e^{-H N/dF}, i.e. LINEAR in eps in the
small-eps regime. N=10, n=5:

```
     eps     median min    min/(eps*min@1)
   1.000        0.00077              1.000
   0.300        0.00037              1.611
   0.100        0.00014              1.766
   0.030        0.00004              1.788
   0.010        0.00001              1.790
```

The ratio min/(eps*min@1) saturates to a constant (~1.79 = the sqrt(n) and finite-N factor)
for eps <= 0.1, i.e. min is proportional to eps = sqrt(lambda_min) once the small eigenvalue
dominates -- the log-log slope over eps in {0.1,0.03,0.01} is ~1.0-1.15. This confirms the
sqrt(lambda_min) prefactor that prop:aniso-mean uses and that makes the cascade telescope to
(k+1)H/dF.

