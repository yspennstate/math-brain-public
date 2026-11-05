# T390: for 1/2 N(-m,1) + 1/2 N(m,1), score matching estimates the mixing weight with asymptotic relative efficiency sqrt(2 pi) e^(-m^2/2)/m (1 - c/m^2, c about 2.5) against maximum likelihood, because the weight enters the score only in a window of width 1/m around the crossing point, where the density is e^(-m^2/2)/sqrt(2 pi)

This turns the 18 Oct numerical finding (ln ARE/m^2 -> -1/2, agent A) into a closed form with its prefactor. It is the
"exact exponent of the single-noise-level loss" that the row's statement leaves open, in the two-component one-dimensional case.

## Computation

Write the weight as w = e^eta/(e^eta + e^-eta). Then p_eta(x) = phi(x) e^(-m^2/2) cosh(m x + eta)/cosh(eta), and the score is
s = -x + m tanh(m x + eta). At eta = 0:

- g = d_eta s = m sech^2(m x);
- the per-sample Hyvarinen loss l = s^2/2 + s' has d_eta l = s g + g' = -m sech^2(m x)(x + m tanh(m x));
- the sandwich variance of the score-matching estimator is V/H^2, with H = E[g^2] and V = E[(d_eta l)^2];
- the maximum-likelihood Fisher information is I = E[tanh^2(m x)], which tends to 1.

The factor sech^2(m x) confines both integrals to |x| <~ 1/m. There p(x) ≈ phi(0) e^(-m^2/2), and x + m tanh(m x) ≈ m tanh(y) with
y = m x. So

    H ≈ m e^(-m^2/2) phi(0) ∫ sech^3 = (pi/2) m phi(0) e^(-m^2/2),
    V ≈ m^3 e^(-m^2/2) phi(0) ∫ sech^3 tanh^2 = (pi/8) m^3 phi(0) e^(-m^2/2),

using ∫ sech^3 = pi/2 and ∫ sech^5 = 3 pi/8. Hence V/H^2 = m e^(m^2/2)/(2 pi phi(0)) and

    ARE(m) = H^2/(V I) ≈ sqrt(2 pi) e^(-m^2/2)/m.

ARE does not depend on the parametrization, so the same holds for w itself.

Check by quadrature (`t390.py`, `t390_out.txt`):

| m | 1 | 2 | 3 | 4 | 5 | 6 | 8 |
|---|---|---|---|---|---|---|---|
| exact/asymptotic | 0.396 | 0.626 | 0.772 | 0.858 | 0.905 | 0.933 | 0.961 |

Here m^2 (1 - ratio) is 2.27, 2.37, 2.43 and 2.48 for m = 4, 5, 6 and 8, so the next term is about -2.5/m^2. At m = 5 the exact ARE is
1.69e-6.

Why this happens: score matching sees the weight only through the posterior's switch from one component to the other, and that
switch lives where the density is smallest. Maximum likelihood sees the weight through every sample's label. This is the same
mechanism as the Poincare-constant lower bound of Koehler-Heckett-Risteski (2210.00726). Here it has an exact constant.

## With noise (denoising score matching, noise integrated out)

At noise level sigma the smoothed mixture has components N(±m, tau^2) with tau^2 = 1 + sigma^2. The loss is invariant under
rescaling, so the smoothed model's own H and V give the effective separation m' = m/tau. The per-sample loss averages over the noise
draw, which lowers V, so H_s^2/(V_s I) is only a lower bound. Exact Gauss-Hermite values:

| m | sigma | ARE | lower bound |
|---|---|---|---|
| 3 | 0 | 0.0072 | 0.0072 |
| 3 | 1.5 | 0.842 | 0.182 |
| 3 | 3 | 0.968 | 0.332 |
| 3 | 6 | 0.916 | 0.186 |
| 5 | 2.5 | 0.886 | 0.131 |
| 5 | 5 | 0.991 | 0.331 |
| 5 | 10 | 0.967 | 0.187 |

One level at sigma = m gives 0.97 to 0.99, which agrees with agent A's 0.95 to 0.99. The bound is loose by a factor of about 3,
so the gain comes from averaging over the noise, not from smoothing alone. With sigma = c m, m' -> 1/c as m grows, and the
efficiency stays of order 1 for any fixed c.

## Conjecture for k components

For k components with known means and a unit shared variance, the same local computation applies at each crossing point between
neighbours. That suggests the weight ARE is governed by the closest pair: exponent -Δ_min^2/8, with the prefactor of the nearest
crossing. Unequal weights move the crossing to x0 = -eta/m and change the density there. Not checked.

## Files

`t390.py`, `t390_out.txt`, `DOSSIER.md`.
