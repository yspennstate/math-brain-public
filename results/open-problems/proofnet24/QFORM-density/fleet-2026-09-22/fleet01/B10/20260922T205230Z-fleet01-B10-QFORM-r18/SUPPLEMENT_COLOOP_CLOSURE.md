# Supplement — exact null coloop is fully paid by the completed partner theorem

This supplement corrects the branch accounting in `REPORT.md`. The Fourier calculations there are valid supporting estimates, including the continuous-density conclusions in their stated diffuse subbranches, but the claimed punctured residual-determinant strip is **not actually unpaid**: the completed fleet02/B10 theorem already closes every exact null-coloop orientation once its hypotheses are applied to the full residual projected pair.

## Theorem — `QFORM-NULL-COLOOP-FULL-CLOSURE-v1`

Let `A=U M U^T`, `U^T U=I_3`, `M=M^T`, `sigma_min(M)>=1`, and let the physical inputs be independent with densities bounded by one. Suppose one physical spectral row `u_i` satisfies `||u_i||=1` and `u_i^T M u_i=0`. Then `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity <= 3*2^(4/3) |det M|^(-1/3) <= 3*2^(4/3) < 7.560`.     (S.1)

No residual leverage hypothesis is needed. No independence is assumed after spectral rotation.

### Proof

Put `r=u_i`. Parseval gives `sum_j u_j u_j^T=I_3`. Since `||r||=1`,

`sum_{j!=i}(u_j dot r)^2 = r^T(I-r r^T)r=0`,

so every other spectral row lies in `r^perp`; in particular the remaining random coordinates depend only on the original independent variables `X_j`, `j!=i`, and are independent of `X_i`.

Because `r^T M r=0`, the vector `Mr` is perpendicular to `r`. Choose an orthonormal spectral basis `(r,e_1,e_2)` with `Mr=s e_1`, `s=||Mr||>=sigma_min(M)>=1`. Then

`M=[[0,s,0],[s,d,g],[0,g,f]]`.     (S.2)

Invertibility gives `f!=0`, and direct expansion gives

`det M=-s^2 f`.     (S.3)

For the residual rows write `u_j=y_j e_1+z_j e_2`, `j!=i`. Parseval on `r^perp` gives

`sum y_j^2=sum z_j^2=1`, `sum y_j z_j=0`.

Thus

`Y=sum_{j!=i}y_j X_j`, `Z=sum_{j!=i}z_j X_j`

is a two-dimensional orthogonal projection of the original product law. The product-projection theorem used in fleet02/B10 r11 gives

`||p_(Y,Z)||_infinity <=2`.     (S.4)

Moreover `X_i` is genuinely independent of `(Y,Z)` and `||p_Xi||_infinity<=1`.

The quadratic is

`Q=2s X_iY+dY^2+2gYZ+fZ^2`

` =2s X_iY+(d-g^2/f)Y^2+f(Z+(g/f)Y)^2`.     (S.5)

Apply fleet02/B10 r11, Lemma 2.1 (scaled dependence-tolerant hyperbolic-square theorem), with `W=X_i`, `K=1`, `H=2`, `a=s`, `b=f`, `F(Y)=(d-g^2/f)Y^2`, and `theta(Y)=(g/f)Y`. It yields

`||p_Q||_infinity <=3*2^(2/3) H^(2/3) K^(2/3) |s|^(-2/3)|f|^(-1/3)`

` =3*2^(4/3)(s^2|f|)^(-1/3)`

` =3*2^(4/3)|det M|^(-1/3)`.     (S.6)

Since all three nonzero eigenvalues of the exact-rank-three form have absolute value at least one, `|det M|>=1`, proving (S.1). QED.

## What remains after this correction

The exact-null **coloop** `||u_i||=1` branch is therefore completely paid in essential supremum, with no split by residual leverage or residual determinant.

This does **not** close the general heavy null-row state `||u_i||^2=c<1`. There the longitudinal leakage `T=sum_{j!=i}(u_j dot r)X_j` is nonzero and correlated with the transverse pair `(Y,Z)`, so `sqrt(c)X_i+T` is not genuinely independent of `(Y,Z)`. Fleet02/B10 r11 contains an exact counterexample showing that bounded pair density plus a bounded conditional scalar density cannot substitute for this independence. The next B10 target therefore remains the near-coloop/product-provenance bridge for `c<1`, not a residual-determinant stability problem at `c=1`.

## Continuity status

The partner hyperbolic-square theorem used for the full coloop closure supplies essential boundedness; this supplement does **not** claim a continuous representative for the entire coloop branch. The Fourier arguments in `REPORT.md` separately prove a bounded continuous density vanishing at infinity in their stated residual-diffuse singular and nonsingular subbranches.

## Source actually consumed

Completed partner: fleet02/B10 r11, canonical report `yspennstate/math-open-problems@11c9ae19edfd07e3a0bd4053a910667c20e721ab:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T130225Z-b10-qform-r11/REPORT.md`. The relevant result is Lemma 2.1 there; the same report also records the product-provenance obstruction that prevents extending the argument by replacing independence with conditional density caps.
