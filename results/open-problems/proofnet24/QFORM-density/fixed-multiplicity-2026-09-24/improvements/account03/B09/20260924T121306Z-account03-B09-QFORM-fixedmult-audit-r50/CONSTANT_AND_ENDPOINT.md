# account03/B09 improvement — sharpened constant and exact endpoint barrier

Pinned baseline: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, source blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

## 1. Same 17-eigenvalue theorem, smaller proved constant

In the normalized `K=s=1` proof, the scalar-pivot truncated half-potential estimate is not merely `<600`. Its displayed derivation gives exactly the upper bound

\[
C_H=10(20+12\log16).
\]

The remaining alternatives entering the nine-direction half-potential proposition are smaller: the no-pivot full half potential is `<200`, the definite-pair truncated potential is `<160`, and the indefinite-pair truncated estimate is `<444`. Therefore for every quadratic polynomial with `s_9(A)>=1`,

\[
\sup_a\mathbb E|Q-a|^{-1/2}\le C_H+1.
\]

At the scalar pivot in the main theorem, `|A_ii|>=1/100`, so the conditional square profile contributes a factor at most ten. Consequently

\[
\|p_Q\|_\infty
\le 10(C_H+1)
=2010+1200\log16
=5337.106466687737\ldots.
\]

The no-pivot density branch is `<=800e=2174.625462767236...`; the definite-pair main branch is `<40`; the indefinite-pair main branch is `<251`. Thus the scalar branch remains the maximum and the same proof establishes

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_\infty
\le(2010+1200\log16)\frac{K^2}{s}
}
\]

under the identical hypothesis `s_17(A)>=s>0` and with all original arbitrary-law, signature, dimension, remaining-spectrum, and affine-term quantifiers unchanged.

## 2. Exact B09 algebraic bottleneck

At a sampled ratio index `r`, the completion gives global correction rank at most `3r`, restricted complement rank at most `r`, and diagonal part zero on the `2r` seed coordinates. If `m` singular values of the original symmetric matrix are at least one, singular-value rank perturbation forces at least `m-3r` diagonal entries of the diagonal part to remain large. The restricted-rank contradiction needs at least `r+1` such entries. Therefore this exact mechanism requires

\[
m\ge4r+1.
\]

For the order-five crossing theorem, the terminal possible ratio is `r=4`, hence the algebraic threshold is `m>=17`. The strict diagonal-dominance slack in this terminal chamber is exactly

\[
\frac{371}{400}-\frac{23}{28}=\frac{297}{2800}>0.
\]

With `m=16`, only four large complement-diagonal entries are forced, which is compatible with restricted rank four. Thus no purely arithmetic tightening of the existing B09 contradiction lowers 17.

## 3. Analytic endpoint bottleneck

The regularized determinant theorem converts order-`k` crossing volume into the envelope

\[
|\phi_Q(t)|\lesssim |t|^{-k/4}.
\]

Order five is integrable. Order four gives exactly `|t|^{-1}`, so absolute Fourier inversion has a logarithmic divergence. Hence replacing order five by order four requires a genuinely new endpoint argument rather than a change of constants.

A threshold reduction can therefore come from either:

1. an order-four physical-crossing theorem proving a direct `O(|I|)` interval bound despite the borderline Fourier envelope;
2. a new completion with better than the present global-rank `3r` / restricted-rank `r` tradeoff while preserving original-coordinate provenance; or
3. a dedicated terminal `r=4` receiver using residual bilinear/Schur structure not captured by the crude rank count.

No multiplicity below seventeen is claimed here.
