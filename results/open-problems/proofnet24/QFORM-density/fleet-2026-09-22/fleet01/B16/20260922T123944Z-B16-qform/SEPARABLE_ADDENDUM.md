# Addendum — half-order hybrid theorem with arbitrary residual coordinate-separable phases

This addendum strengthens `REPORT.md` from the same run. Full QFORM conjecture remains OPEN.

## A. Phase-stable rank-two Riesz lemma

In Lemma 3.1 of `REPORT.md`, keep the same two-dimensional Parseval frame `V`, leverage bounds `d_k=||v_k||^2<=1/2`, independent scalar densities `f_k<=1`, and invertible symmetric `S`. Let `G_k:R->R` be arbitrary measurable functions, finite almost surely, and define

`R = (V^T X)^T S (V^T X) + sum_k G_k(X_k)`.

Then the same bound holds:

`boxed{ ess sup_t E|t-R|^(-1/2) <= 4 sqrt(2e)|det S|^(-1/4). }`        (A.1)

### Proof

For every Fourier-time `tau`, define the complex one-dimensional amplitudes

`h_{k,tau}(x)=f_k(x) exp(i tau G_k(x))`.

Their absolute values are exactly `f_k`, so for every `1<=p<=2`,

`||h_{k,tau}||_p=||f_k||_p<=1`.

Let `mu_tau` be the phase-weighted projection of the product measure under `W=V^T X`. Its Fourier transform is

`Psi_tau(xi)=prod_k widehat{h_{k,tau}}(<v_k,xi>)`.

The same geometric Brascamp--Lieb plus sharp Hausdorff--Young calculation as in Lemma 3.1 therefore gives, **uniformly in tau**,

`||Psi_tau||_1 <= (2pi)^2 e`.                                         (A.2)

Pairing this complex projected measure with the two-dimensional quadratic Fresnel kernel by Gaussian regularization yields

`|E exp(i tau R)| <= pi e |det S|^(-1/2)|tau|^(-1)`                    (A.3)

for `tau!=0`. This is exactly the complex-amplitude/separable-phase stability mechanism used in `QFORM-DIFFUSE-SEPARABLE-PHASE-v1`, but here in dimension two.

Combining (A.3) with the trivial characteristic-function bound `1`, the half-order Fourier multiplier calculation in Lemma 3.1 is unchanged and proves (A.1). `QED`

## B. Strengthened heavy-coordinate theorem

Under every hypothesis of Theorem 4.1 in `REPORT.md`, let `G_k` be arbitrary real measurable functions for `k!=i`. Then

`Q_G=(U^T X)^T Lambda(U^T X)+sum_{k!=i}G_k(X_k)`

still satisfies

`||p_{Q_G}||_infinity <=4 sqrt(2e)c^(-1/2)|a|^(-1/4)|det Lambda|^(-1/4)`. (B.1)

Indeed the same square completion gives

`Q_G=ac[X_i+theta(Z)]^2 + [W^T S W+sum_{k!=i}G_k(X_k)]`,

and Section A pays the bracketed residual by its half-order potential.

### Matrix corollary

If a symmetric matrix admits a decomposition

`A=U Lambda U^T + D`,

where `D` is arbitrary diagonal, the rank-three data `(U,Lambda)` obey Theorem 4.1, and the selected heavy physical coordinate satisfies `D_ii=0`, then the same density bound (B.1) holds for `X^T A X`; simply take `G_k(x)=D_kk x^2` for `k!=i`.

Thus arbitrary diagonal curvature on every **residual** original coordinate may be retained rather than discarded as independent noise. This is a genuine extra-spectrum branch, but it is not a decomposition theorem for an arbitrary target matrix.

## C. Remaining implication

The first missing extension is to allow nonseparable residual couplings and/or a quadratic perturbation on the heavy coordinate itself. A nonzero extra `D_ii X_i^2` changes the coefficient used in the square completion and generally leaves a three-dimensional residual rather than the rank-two Schur complement, so (B.1) cannot simply be asserted in that case.

No full-solution promotion is made.
