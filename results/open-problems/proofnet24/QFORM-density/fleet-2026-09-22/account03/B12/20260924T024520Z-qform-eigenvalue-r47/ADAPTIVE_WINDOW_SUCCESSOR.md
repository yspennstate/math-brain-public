# r47 correction and successor — adaptive spectral window gives a stronger physical-resource export

## 0. Source reconciliation: first r47 reduction was already known

After the first r47 report was committed, a source search found the exact earlier theorem

`QFORM-RIDGE-OR-PHYSICAL-RESOURCE-v1`

in account02/B19 r15, source

`yspennstate/math-open-problems@48841f2d72a1faf741d5a75f6569107537221e7e`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260922T151209Z-account02-B19-qform-r15/RIDGE_ADDENDUM.md`.

It already proves that the `|lambda|>=1/64` spectral-window branch is continuously bounded by `<64`, while failure gives

`|A_ii|>=1/512` or `||A[i,i^c]||_2>1/512`.

Therefore Sections 1–2 of the initial r47 `REPORT.md` are an **independent rederivation, not a new result**, and no novelty is claimed for that exact scope. The orthogonal spectral-completion bookkeeping in Section 3 remains valid, but the useful successor below changes the spectral-window parameters and proves a strictly stronger physical-resource export.

## 1. General two-parameter spectral-window lemma

Let `A=A^T` have at least three eigenvalues of modulus at least one. Fix

`0<h<1`, `0<eps<1`,

and let

`P_h=1_{[h,infinity)}(|A|)`.

Set

`delta(eps)=1/2-eps-sqrt(2 eps)`

and assume

`delta(eps)>h`.                                                (1.1)

Write

`sigma=delta(eps)-h`.                                          (1.2)

Assume also

`sqrt(eps/delta(eps)) + sqrt(6) h/sigma <=1/sqrt(2).`          (1.3)

### Theorem 1.1 — `QFORM-ADAPTIVE-SPECTRAL-WINDOW-v1`

If

`max_i (P_h)_ii <= eps`,                                      (1.4)

then for every independent cap-one product source the full quadratic form `X^T A X` has a continuous density vanishing at infinity and

`||p_(X^T A X)||_infinity <= 9 sqrt(3e)/(2 sigma).`            (1.5)

All eigenvalues below `h` may be nonzero, arbitrarily numerous, of either sign, and arbitrarily oriented. No post-rotation independence is used.

### Proof

Let `A_H=U Lambda U^T` be the spectral truncation of `A` to `P_h`, where the columns of `U` are orthonormal, and let

`E=A-A_H`.

Then

`||E||op<=h`,                                                  (1.6)

and every row `u_i` of `U` satisfies

`||u_i||^2=(P_h)_ii<=eps`.                                    (1.7)

The two-part Marcus–Spielman–Srivastava frame partition used in the completed ridge-window theorem gives a partition of the ORIGINAL coordinates into `I,J` for which

`delta I <= M_I=U_I^T U_I, M_J=U_J^T U_J <= (1-delta) I`,     (1.8)

where

`1-delta=(1/sqrt(2)+sqrt(eps))^2`
`       =1/2+eps+sqrt(2 eps)`.                                (1.9)

The high-window cross block is

`B_0=A_H[I,J]=U_I Lambda U_J^T`.                               (1.10)

Since `Lambda` has at least three singular values at least one and both Gram matrices in (1.8) are bounded below by `delta I`,

`s_3(B_0)>=delta`.                                             (1.11)

For the actual final cross block

`B=A[I,J]=B_0+E[I,J]`,

operator-norm Weyl and (1.6) give

`s_3(B)>=delta-h=sigma`.                                       (1.12)

Because `Lambda` is invertible on the high spectral subspace and `M_I,M_J` are positive definite,

`range(B_0)=range(U_I)`.                                       (1.13)

Therefore the row-side range projection has diagonal

`(P_range(B_0))_ii`
` =u_i^T M_I^(-1)u_i`
` <=eps/delta`.                                                (1.14)

Now use the completed ridge-leverage stability lemma from

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

Set the ridge scale

`rho=sigma/sqrt(6)`.                                           (1.15)

For

`K=B B^T (rho^2 I+B B^T)^(-1)`,

the perturbation estimate and (1.14) give

`K_ii <= [sqrt(eps/delta)+h/rho]^2`
`     = [sqrt(eps/delta)+sqrt(6)h/sigma]^2`
`     <=1/2`                                                   (1.16)

by (1.3). Also (1.12) gives

`theta=tr K`
` >=3 sigma^2/(rho^2+sigma^2)`
` =18/7>2`.                                                    (1.17)

The completed `q=1` ridge criterion therefore applies to the ACTUAL cross block `B`, retaining arbitrary self blocks and all other coefficients. Its three-singular-value specialization is

`||p_Q||infinity <=9 sqrt(3e)/(2 sigma)`.                      (1.18)

The same theorem gives continuity and vanishing at infinity. QED.

## 2. A clean stronger global dichotomy

Choose

`h=1/20`, `eps=1/64`.                                         (2.1)

Then

`delta=(31-8 sqrt(2))/64`
`     =0.307598304703363...`,                                 (2.2)

and

`sigma=delta-1/20`
`     =(139-40 sqrt(2))/320`
`     =0.257598304703363....`                                 (2.3)

The ridge-leverage expression in (1.3) is

`L=1/sqrt(31-8 sqrt(2))`
`  +16 sqrt(6)/(139-40 sqrt(2))`
`  =0.700828952077477... <1/sqrt(2).`                         (2.4)

For a completely elementary rigorous numerical check, use

`sqrt(2)<1.4143`, `sqrt(6)<2.4495`.

Then

`31-8sqrt(2)>19.6856>4.4368^2`,

so the first term in (2.4) is `<1/4.4368<0.2254`; and

`139-40sqrt(2)>82.428`, `16sqrt(6)<39.192`,

so the second term is `<39.192/82.428<0.4755`. Hence

`L<0.7009`, and `0.7009^2<1/2`, proving (1.3) without relying on decimal equality.

Theorem 1.1 therefore gives, under `max_i(P_(1/20))_ii<=1/64`,

`||p_Q||infinity`
` <= 9 sqrt(3e)/(2 sigma)`
` =49.8858505783748... <50`.                                  (2.5)

The final `<50` follows for example from `sqrt(2)<1.4143`, `e<2.719`: these give `sigma>0.2575`, `sqrt(3e)<2.857`, and hence the right side of (2.5) is `<49.929`.

If instead

`max_i(P_(1/20))_ii>1/64`,                                   (2.6)

then spectrally

`A^2 >= (1/20)^2 P_(1/20)`.                                  (2.7)

For some ORIGINAL coordinate `i`,

`||A e_i||_2^2=(A^2)_ii> (1/20)^2(1/64)=1/25600`,

so

`||A e_i||_2>1/160`.                                          (2.8)

Using the exact physical row decomposition

`||A e_i||_2^2=A_ii^2+||A[i,i^c]||_2^2`,                     (2.9)

one obtains

`|A_ii|>1/(160 sqrt(2))`

or

`||A[i,i^c]||_2>1/(160 sqrt(2)).`                             (2.10)

### Theorem 2.1 — `QFORM-ADAPTIVE-WINDOW-OR-STRONG-HUB-v1`

Every matrix in the exact owner target satisfies at least one of:

1. `X^T A X` has a continuous `C_0` density with `||p_Q||infinity<50`; or
2. there is an ORIGINAL coordinate with

   `|A_ii|>1/(160 sqrt(2))` or `||A[i,i^c]||_2>1/(160 sqrt(2))`.

The physical-resource scale

`1/(160 sqrt(2))=0.00441941738241592...`                       (2.11)

is `2.2627416998...` times the previous `1/512` export. The theorem is an alternative exhaustive window dichotomy; it does not claim that its diffuse premise contains the earlier `h=1/64,eps=1/32` diffuse premise.

## 3. Additional-eigenvalue interpretation

For an exact spectral completion

`A=A_0+R`, `A_0R=0`,                                          (3.1)

the threshold projector satisfies

`P_h(A)=P_h(A_0)+P_h(R)`                                      (3.2)

for every `h>0`. Thus arbitrary added eigenvalues of either sign and arbitrary magnitude enter Theorem 2.1 only through the diagonal leverage they add to the `h=1/20` projector. All added eigenvalues below `1/20` are free in this certificate.

If the total high-window leverage remains at most `1/64`, the full completed matrix has continuous density `<50`. If it does not, the final matrix necessarily exports the stronger physical resource (2.10). This is coefficient-level spectral accounting, not probabilistic convolution.

## 4. Designated account04/B12 equation

Retain the account04/B12 r8 source

`yspennstate/math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001`.

On its concrete carrier it proves

`sqrt(lambda_6((A_*^2)[H,H]))>=g`

with

`g=sqrt(5)-1-1/100=1.2260679774997898...`.                    (4.1)

For every symmetric orthogonal spectral completion `S` with `A_*S=0`,

`(A_*+S)^2=A_*^2+S^2>=A_*^2`,                                (4.2)

hence the actual final matrix still satisfies

`sqrt(lambda_6(((A_*+S)^2)[H,H]))>=g`.                        (4.3)

The completed six-mode receiver gives

`||p_(X^T(A_*+S)X)||_(infinity,ess)`
` <=720 sqrt(pi)/g`
` =1040.86135195729...<1040.862`.                              (4.4)

Independently, Theorem 2.1 says that this completed family either has continuous density `<50` through its final `1/20` window, or possesses a literal physical resource at scale `1/(160sqrt(2))`. This is the designated partner result applied to an actual final-matrix inequality, with arbitrary signed spectral completion retained.

## 5. Status

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

The first r47 `1/512` reduction is source-matched and is not claimed as new. The retained new supporting advance is the two-parameter adaptive-window theorem and its clean `h=1/20, eps=1/64` consequence exporting a physical resource at `1/(160sqrt(2))` while paying the complementary branch continuously by `<50`.

The next exact implication is to use that stronger physical resource together with the remaining spectral structure to force a physical pair/Schur, grouped, ridge, projected-crossing, or hub/common-plane receiver without using the refuted one-heavy-row same-square absorption shortcut.
