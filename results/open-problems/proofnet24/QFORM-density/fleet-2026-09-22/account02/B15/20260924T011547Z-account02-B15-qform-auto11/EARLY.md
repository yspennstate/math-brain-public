# Early calculation — collective semidefinite Schur smoothing

Run `20260924T011547Z-account02-B15-qform-auto11`.

Take an ORIGINAL-coordinate invertible indefinite physical pair with block `D`, `Delta=|det D|`, `kappa=sigma_min(D)`. After completing the pair in a homogeneous quadratic form,

`Q=(U+D^{-1}BZ)^T D (U+D^{-1}BZ)+R(Z)`, `R(Z)=Z^T S Z`, `S=C-B^T D^{-1}B`.

The completed pair-log envelope gives, for every `r>0`,

`p_Q(t) <= 2 sqrt(2)/r + Delta^(-1/2) E log_+(2 r^2/(kappa |t-R|))`.

If the Schur remainder is semidefinite of rank two with nonzero eigenvalue magnitudes `sigma_1,sigma_2`, account03/B15 auto29 gives the orientation-free product-law bound

`||p_R||_infinity <= M := 2 pi / sqrt(|sigma_1 sigma_2|)`.

Thus for every `a>0`,

`E log_+(a/|t-R|) = int_0^infinity P(|t-R|<a e^{-v}) dv <= 2 M a`.

With `a=2r^2/kappa`,

`p_Q(t) <= 2 sqrt(2)/r + 4 M r^2/(kappa sqrt(Delta))`.

Optimizing gives `r^3=kappa sqrt(Delta)/(2 sqrt(2) M)` and therefore

`||p_Q||_infinity <= 6 (M/(kappa sqrt(Delta)))^(1/3)`

`<= 6 (2 pi /(kappa sqrt(Delta) sqrt(|sigma_1 sigma_2|)))^(1/3)`.

This is a genuine collective rank-two Schur receiver: it pays the two Schur eigenvalues together, never rotates the independent coordinates, and does not use continuity to obtain height.

The semidefinite hypothesis cannot simply be replaced by an `L^infinity` claim for rank-two indefinite Schur remainders: account03/B15 auto29 proves logarithmic blow-up for every indefinite orientation under the centered cube law. The next useful target is therefore a product-provenance logarithmic small-ball upper bound for the indefinite Schur remainder, not a nonexistent bounded-density bound.
