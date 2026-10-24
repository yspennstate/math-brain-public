# account03/B17 — noncentral Gaussian closure and a fully mixed Walsh stress family

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Run:** `account03-B17-20260922T140220Z-r11`  
**Assignment:** Sharp constant and witnesses  
**Classification:** `NEW SUPPORTING THEOREM / EXACT ROTATED STRESS / FULL CONJECTURE OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction state

The target remains the unrestricted statement: for every dimension, every independent real input vector with coordinate densities bounded by one, and every real symmetric matrix with at least three eigenvalues of magnitude at least one, prove a universal essential-density bound for `X^T A X`, or give a valid counterexample. Continuity is tracked separately.

This report does **not** prove the full target. It respects the current corrections: law-uniform pointwise quadratic-phase decay is false; rotation does not preserve input independence; one physical minor is not enough; conditional density caps cannot be substituted for independence; and fiberwise trace estimates can fail before product aggregation.

The exact assigned partner `account04/B17` had no completed QFORM handoff or canonical report visible at the pre-publication check. I therefore do not invent a partner result. I apply two compatible completed inputs instead:

1. `account02/B17`, canonical report `yspennstate/math-open-problems@cdd32fd16a694a5f8acc7ba758e0db6596a3e4a1`, proves the sharp centered-Gaussian three-mode envelope
   `||p||_infinity <= 1/(2 sqrt(2) s)` when three Gaussian quadratic coefficients have magnitude at least `s`, with equality for `s diag(1,1,-1)`.
2. `account04/B18`, canonical report `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, proves the minority-pivot Schur-complement smoothing theorem. I use it below to show that a new exact rotated family lies entirely in its declared unpaid branch.

I also apply the newer regularized-determinant theorem at `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a` to the same stress family, obtaining an explicit dimension-free bound.

## 2. New lemma: noncentral squares are central squares plus independent positive noise after Poisson mixing

### Lemma 2.1

Let `G~N(0,1)` and `nu in R`. Put `Y=(G+nu)^2`. Let `N~Poisson(nu^2/2)`. Conditional on `N=k`,

`Y law = chi^2_(1+2k)`.

Equivalently, conditional on `N=k`, one may write in distribution

`Y = Z^2 + W_k`,

where `Z~N(0,1)`, `W_k~chi^2_(2k)`, and `Z,W_k` are independent.

### Proof

For `t<1/2`, direct Gaussian integration gives

`E exp(t(G+nu)^2) = (1-2t)^(-1/2) exp( nu^2 t/(1-2t) ).`

For the Poisson mixture,

`E[(1-2t)^(-(1+2N)/2)]
 = (1-2t)^(-1/2) E[(1-2t)^(-N)]`

`= (1-2t)^(-1/2)
   exp[(nu^2/2)((1-2t)^(-1)-1)]`

`= (1-2t)^(-1/2) exp( nu^2 t/(1-2t) ).`

The moment generating functions coincide on a neighborhood of zero. The additive representation follows from gamma/chi-square additivity. QED.

## 3. New theorem: shifts cannot worsen the sharp Gaussian three-mode constant

### Theorem 3.1 — noncentral Gaussian envelope

Let `G~N(0,I_d)`, `m in R^d`, and `B` be real symmetric with at least three eigenvalues of magnitude at least `s>0`. Then

`(G+m)^T B (G+m)`

has a continuous density and

`boxed( ||p||_infinity <= 1/(2 sqrt(2) s) ).`

The constant is sharp: equality is attained at `m=0`, `d=3`, `B=s diag(1,1,-1)`.

### Proof

Orthogonally diagonalize `B`. Rotational invariance of the standard Gaussian gives

`(G+m)^T B(G+m) = sum_j mu_j (Z_j+eta_j)^2`

with independent standard normals `Z_j`. Select three indices with `|mu_j|>=s`; all remaining modes form an independent summand, whose convolution cannot increase an `L^infinity` density norm.

For the selected three modes, apply Lemma 2.1 independently. Conditional on the three Poisson counts `N=(N_1,N_2,N_3)`,

`S_eta law = S_0 + R_N`,

where

`S_0=sum_(j=1)^3 mu_j Z_j^2`

is the centered three-mode quadratic form and `R_N` is an independent signed sum of chi-square variables. Hence

`||p_(S_eta | N)||_infinity
 = ||p_(S_0) * mu_(R_N)||_infinity
 <= ||p_(S_0)||_infinity
 <= 1/(2 sqrt(2) s),`

where the last inequality is exactly the completed `account02/B17` centered-Gaussian theorem. Averaging over `N` preserves the same bound.

For continuity, `S_0` has an `L^1` characteristic function because three nonzero Gaussian-square factors give `O(|t|^(-3/2))`. Thus `p_(S_0)` is continuous and vanishes at infinity. Each conditional density is a probability convolution of this same continuous bounded function, and the Poisson mixture converges uniformly by the bound above. Therefore the selected noncentral sum has a continuous density; convolution with the remaining independent modes preserves continuity. QED.

### Corollary 3.2 — noncentral covariance version

Let `Y~N(m,Sigma)` with `Sigma >= v I`, `v>0`, and let `A` be symmetric with at least three eigenvalues of magnitude at least one. Then

`boxed( ||p_(Y^T A Y)||_infinity <= 1/(2 sqrt(2) v) )`

and the density is continuous.

Indeed write `Y=Sigma^(1/2)(Z+nu)` and `B=Sigma^(1/2) A Sigma^(1/2)`. The singular-value inequality

`s_k(PAQ) >= s_min(P) s_min(Q) s_k(A)`

shows that `B` has at least three eigenvalues in modulus at least `v`; Theorem 3.1 applies.

### Corollary 3.3 — all Gaussian diffuse limits are capped at `3 sqrt(2)`

Every one-dimensional law with density at most one and finite variance has variance at least `1/12`; the completed `account02/B17` proof gives this sharp covariance floor. Therefore any Gaussian limit of projected density-one product inputs whose covariance retains the product-law floor `Sigma >= (1/12) I` obeys

`boxed( ||p||_infinity <= 3 sqrt(2) ).`

Crucially, **the limiting Gaussian need not be centered**. This closes the explicit noncentral-Gaussian sharp-witness branch left open by the centered theorem. A witness exceeding `3 sqrt(2)` must therefore use a genuinely non-Gaussian / non-Lindeberg / mesoscopic mechanism, not merely a diffuse mean shift.

## 4. A fully mixed Walsh-Hadamard target family

Let `n=2^d`, `d>=3`, identify physical coordinates with `x in F_2^d`, and choose three linearly independent Walsh characters `a_1,a_2,a_3`. Define

`r_j(x)=n^(-1/2) (-1)^(a_j dot x),`

let `R` be the `n x 3` matrix with columns `r_j`, and set

`J=diag(1,1,-1),   A_n=R J R^T.`

Then `R^T R=I_3`, hence

`spec(A_n)={1,1,-1,0^(n-3)}`.

This is an exact target-admissible, maximally delocalized rank-three matrix.

### 4.1 Exact physical-principal-triple geometry

Every physical diagonal entry is

`(A_n)_(xx)=n^(-1)(1+1-1)=1/n>0.`

For a physical triple `I`,

`(A_n)_I=R_I J R_I^T.`

The sign rows `sqrt(n) R_I` lie in four antipodal classes of `{+/-1}^3`, each class occurring exactly `n/4` times. Three such rows are linearly independent iff they come from three distinct antipodal classes; in that case the sign determinant has modulus `4`. Therefore:

* exactly `C(4,3)(n/4)^3 = n^3/16` physical triples are nonsingular;
* every nonsingular triple has inertia `(2,1)`;
* every nonsingular triple satisfies
  `|det (A_n)_I|=16/n^3`;
* consequently
  `sum_(|I|=3) |det (A_n)_I| = 1`.

Because **all three diagonal pivots are positive**, every nonsingular `(2,1)` triple has only majority-sign pivots. Thus the `account04/B18` minority-pivot Schur theorem has no eligible triple anywhere in this family. This is not a failure of that theorem; it places the family exactly in the branch its report declares unpaid.

## 5. The same fully mixed family is controlled by aggregate cross-block smoothing

Now assume `d>=4` and choose a fourth Walsh character `a_4` independent of the first three. Split the original coordinates into

`I={x: (-1)^(a_4 dot x)=+1},   K={x: (-1)^(a_4 dot x)=-1}.`

Walsh orthogonality gives exactly

`R_I^T R_I = R_K^T R_K = (1/2) I_3.`

Hence the cross block

`B=A_n[I,K]=R_I J R_K^T`

has exactly three nonzero singular values, all equal to `1/2`.

The coordinate leverage of `range(B)=col(R_I)` is constant:

`ell_x=r_x^T (R_I^T R_I)^(-1) r_x
      =2 ||r_x||^2=6/n.`

For `n>=16`, `6/n<=3/8<1/2`, so the `q=1` branch of the completed regularized-determinant theorem applies with `r=3`, `sigma=1/2`. It gives the explicit all-law target bound for this family

`boxed( ||p_(X^T A_n X)||_infinity <= 3 sqrt(2) e
       = 11.53269308447735... )`

for **arbitrary independent coordinate densities bounded by one**.

This is a concrete target-relevant implication of the aggregate theorem: it controls a fully mixed family for which every local minority-pivot triple is unavailable. The constant is exactly a factor `e` above the sharp diffuse Gaussian stress identified next.

## 6. Shifted unit-interval inputs: an exact diffuse stress with arbitrary Gaussian mean

Let

`X_x = U_x + (R m)_x,`

where the `U_x` are iid `Uniform[-1/2,1/2]` and `m in R^3` is fixed. Every physical input still has density exactly one. Since `R^T R=I`,

`R^T X = R^T U + m.`

As `n=2^d -> infinity`, the multivariate Lindeberg central limit theorem applies because every frame coefficient has modulus `n^(-1/2)` and

`Cov(R^T U)=(1/12)I_3.`

Therefore

`X^T A_n X
 = (R^T X)^T J(R^T X)
 => (G_1+m_1)^2+(G_2+m_2)^2-(G_3+m_3)^2,`

where the `G_j` are independent `N(0,1/12)`.

By Corollary 3.2, **every fixed mean shift** in this exact fully mixed family has limiting density norm at most `3 sqrt(2)`, and the centered case attains `3 sqrt(2)` at zero.

This gives a rigorous universal-constant lower bound without histogram or local-limit assumptions. If all finite members had density norm at most a universal `C`, then for every open interval `G`,

`P(Q_infinity in G) <= liminf P(Q_n in G) <= C |G|`

by Portmanteau. The limiting law therefore has density norm at most `C`. Since the centered limit has density value `3 sqrt(2)` at zero,

`boxed( C >= 3 sqrt(2) = 4.242640687119286... ).`

The lower bound itself was known from an earlier diffuse block family; the new information is that the same sharp stress occurs in a **fully mixed Walsh geometry** that defeats every single minority-pivot triple while remaining directly controlled by the aggregate cross-block theorem.

## 7. Executed finite certificate

`CHECK.py` in this run root was executed for `n=16`. It verifies:

* `R^T R=I` exactly to floating arithmetic;
* spectrum `{-1,1,1,0^(13)}`;
* constant physical diagonal `1/16`;
* exactly `256=n^3/16` nonsingular physical triples;
* every such triple has `|det| n^3=16` and inertia `(2,1)`;
* the balanced Walsh cut has cross singular values `(1/2,1/2,1/2)`;
* maximum range leverage is `3/8=6/n`;
* the regularized-determinant bound is `3 sqrt(2)e=11.532693084477351`, while the Gaussian stress is `3 sqrt(2)=4.242640687119286`.

This finite check supports the exact algebra; it is not used as a proof of the universal conjecture.

## 8. Implication for the full target

The full conjecture remains **OPEN / NOT PROVED**. This run removes one sharp-constant escape route and sharpens one structural stress test:

1. **Closed branch:** noncentral Gaussian diffuse limits cannot exceed the centered sharp ceiling `3 sqrt(2)`.
2. **Exact stress:** fully mixed Walsh rank-three matrices can have all nonsingular physical triples in the all-majority-pivot branch while retaining aggregate determinant mass one.
3. **Positive mechanism test:** the regularized cross-block theorem pays this family dimension-freely, with explicit constant `3 sqrt(2)e`.
4. **Next sharp-witness obligation:** to force a larger lower bound than `3 sqrt(2)`, search in non-Gaussian mesoscopic/non-Lindeberg product laws or mixed-leverage structures; mean-shifting a diffuse Gaussian limit is now ruled out analytically.
5. **Next proof obligation:** bridge heavy/mixed leverage to an aggregate cross-block or other product-preserving smoothing mechanism without first selecting a single reciprocal minor.

No claim here is a complete proof or counterexample to QFORM.
