# fleet03/B15 auto33 — rigor check

Run: `20260924T052811Z-fleet03-B15-qform-auto33`

## 1. Rational chattering mass identity

For the construction in REPORT.md,

- `sum_k a_k = 1-delta`,
- `s = sum_k(a_k-q_k)`,
- `d = 1-sum_k q_k = delta+s`.

Hence the reserve interval has nonnegative rational length `d`, and

`|E| = sum_k q_k + d = 1` exactly.

The cap is exactly one because the approximant density is `1_E`.

## 2. Weak-convergence sign check

For `phi in C_c`, the reserve interval is eventually outside `supp(phi)`. On each cell,

`int_L phi - int_J phi f`

is decomposed by adding/subtracting `phi(x_J)q` and `phi(x_J)a`. Summing gives

`abs(error) <= ||phi||_inf s + omega_phi(h)(sum q + sum a)`

`<= ||phi||_inf eps + 2 omega_phi(h) -> 0`.

Thus the approximants converge vaguely to `f dx`; since all measures and the limit have mass one, vague convergence is weak convergence.

## 3. Matrix approximation stays inside the target

For `B=(1+4 eta)A`, every positive eigenvalue of `A` at least `1` becomes at least `1+4 eta`, and every negative eigenvalue at most `-1` becomes at most `-1-4 eta`. If `||A_Q-B||_op<eta`, Weyl leaves those eigenvalues respectively above `1+3 eta` or below `-1-3 eta`. Therefore the rational generic approximant still has at least three eigenvalues of modulus strictly greater than one.

## 4. Portmanteau direction

Weak convergence `mu_m => mu` gives, for every open interval `I`,

`mu(I) <= liminf_m mu_m(I)`.

Each `mu_m(I)` is bounded by `C_Q |I|`: first enlarge `I` to rational-endpoint open intervals `J_r` with `|J_r| downarrow |I|`, then use monotonicity and the defining rational-interval bound. Hence

`mu(I) <= C_Q |I|`.

The inequality direction is therefore correct for transporting an upper density bound.

## 5. Countability

For each fixed `n`, rational symmetric matrices are countable; finite rational-endpoint unions of total length one are countable; finite products remain countable; rational open intervals are countable. The union over `n in N` is countable.

## 6. No conflict with fragment-count correction

The number of cells, hence possible occupied interval components, grows with the approximation scale and support window. No finite universal fragment-count bound is asserted or needed.

## 7. Partner application

Fleet04/B15 Theorem 6.1 at `math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e` was read in full. It applies after the transported interval inequality because every owner-target matrix has rank at least three. The resulting `C_0` representative has the identical height constant; no continuity modulus is inferred.

## 8. Status

The reduction is exact but does not establish a finite value of `C_Q`. Full QFORM remains open.
