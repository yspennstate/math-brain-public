# A physical-pair theorem for arbitrary rank and arbitrary remaining spectrum

Programme QFORM-DENSITY-3EIG-20260922. Continuation of interactive record 20260922T180015Z-pair-log.

Status: complete supporting analytic argument supplied, pending independent mathematical review. The full arbitrary-matrix conjecture remains unproved. This removes the exact-rank-three restriction from the companion pair-pivot argument, at a weaker numerical bound, not from the original conjecture.

## 1. Theorem

Let A be any real symmetric matrix and let s_3(A)>=s>0 be its third singular value (the third-largest eigenvalue magnitude). Let X have independent real coordinates with probability densities bounded by one. Suppose two ORIGINAL coordinates have an invertible indefinite principal pair B, and put

`D=|det B|`, `kappa=sigma_min(B)>0`.

Then, for arbitrary b and d, Q=X^T A X+b^T X+d has an essentially bounded density with

`||p_Q||_infinity <=3*400^(1/3) * (D^2*kappa*s)^(-1/6)`.    (1.1)

All additional eigenvalues and all couplings are arbitrary. Neither scalar diagonal of B is required to be nonzero. A convenient quantitative branch is

`s_3(A)>=1, |A_ij|>=1/2, |A_ii|,|A_jj|<=1/4`

which gives the sharper cutoff estimate

`||p_Q||_infinity <=4*(2sqrt(2)+4+log(625/2))<51`.          (1.2)

There is no claim that the bare three-large-eigenvalue condition guarantees such a pair. The unresolved part remains a dimension-free aggregation when all useful physical coefficients/pairs are small. Only essential boundedness, not a continuous representative, is proved here.

## 2. Dependency: the unrestricted cross-block determinant estimate

The earlier report

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`

Section 5 proves, for any disjoint original-coordinate cut with cross block T and arbitrary within-block phases,

`|phi(t)| <=det(I+4t^2*T*T^T/(pi^2 e^2))^(-1/8)`.          (2.1)

In particular, if ||T||>=sigma then

`|phi(t)| <=(1+4sigma^2*t^2/(pi^2 e^2))^(-1/8)`
`         <=(pi*e/(2*sigma*|t|))^(1/4)`.                  (2.2)

Extra small singular values can be discarded from the regularized determinant without loss. Original-coordinate affine terms are within-block phases and are allowed. No moment assumptions enter.

This supporting estimate, not a conjectured scalar Fresnel bound, is the analytic input below. Its proof uses independent-copy decoupling and geometric Brascamp--Lieb with difference densities; the exact sharp Young/Hausdorff--Young constants are given in that report. A scoped passing independent review of Sections 3--6 was recorded by fleet02/B02 at math-open-problems commit e3fe4ce35f6aa4a90cca913051886c96c7febfc3; that review does NOT certify the present extension.

The logarithmic pair-density envelope is proved directly in the companion PAIR_LOG_THEOREM.md, canonical commit f7f0fedb2d93b46824f96cac1164af6f8a55626f. All its coordinate-independence requirements are retained here.

## 3. An arbitrary-rank one-eigenvalue small-ball bound

### Lemma

For every nonzero real symmetric S, arbitrary affine terms, and independent cap-one coordinates Z,

`sup_w P(|Z^T S Z+b^T Z+d-w|<rho)`
` <=min(1,5*(rho/||S||)^(1/4))`, rho>0.                  (3.1)

### Proof

Put L=||S||>0 and M=max_i |S_ii|.

If M>=L/2, condition on all coordinates except one attaining M. A univariate quadratic with coefficient a has an inverse image of an interval of length 2rho of total length at most 2sqrt(2rho/|a|). Thus the conditional probability is at most 4sqrt(rho/L). When rho<=L this is at most 4(rho/L)^(1/4), and when rho>=L the trivial bound one proves (3.1).

Otherwise put S0=S-diag(S). It has zero diagonal and ||S0||>=L/2. For a uniformly random diagonal sign matrix E, set

`C_E=(S0-E*S0*E)/2`.

Then E[C_E]=S0/2, since the diagonal of S0 is zero. By convexity of the operator norm, at least one choice of signs has ||C_E||>=||S0||/2>=L/4. For the cut into positive and negative signs, C_E is the symmetric off-diagonal matrix [[0,T],[T^T,0]], so its norm equals ||T||. This is an ORIGINAL-coordinate cross block of S, with sigma=||T||>=L/4.

Using (2.2) for the full polynomial, including its affine terms, gives

`|phi(t)| <=(2*pi*e/(L*|t|))^(1/4)` for t!=0.

For v>0 use `1_(|x|<rho)<=exp(v)*exp(-v*x^2/rho^2)`. Gaussian Fourier inversion gives

`P(|R-w|<rho)`
` <= exp(v)*rho/(2sqrt(pi*v)) * integral exp(-rho^2*t^2/(4v))*|phi(t)| dt`.

For 0<alpha<1 the exact Gaussian integral is

`integral_R exp(-a*t^2)|t|^(-alpha)dt =a^((alpha-1)/2)*Gamma((1-alpha)/2)`.

Substitute alpha=1/4 and v=1/8. The resulting prefactor of (rho/L)^(1/4) is

`2^(3/8)*pi^(-1/4)*exp(3/8)*Gamma(3/8)<5`.

The strict inequality does not rely on a numerical approximation: splitting the gamma integral at one gives Gamma(3/8)<=8/3+exp(-1)<73/24. Also 2^(3/8)<4/3, pi^(-1/4)<4/5, and exp(3/8)<3/2. Their product is less than 73/15<5. This proves (3.1). QED.

The exponent 1/4 is weaker than the rank-one exponent 1/2. Its advantage is that it is valid with no rank restriction or small-tail assumptions on S.

## 4. Two-coordinate completion preserves a remaining large scale

Reorder the chosen pair first and write

`A=[[B,E],[E^T,C]]`, `S=C-E^T*B^(-1)*E`.

The matrix

`A0=[[B,E],[E^T,E^T*B^(-1)*E]]`

has rank exactly two, because it factors as `[I;E^T B^(-1)] B [I,B^(-1)E]`. Furthermore A-A0=diag(0,S). Therefore

`s_3(A)<=||A-A0||=||S||`.                                (4.1)

For completeness, this rank-approximation inequality follows directly from the singular-value min-max principle: ker(A0) has codimension two, and on that subspace ||Ax||=||(A-A0)x||<=||A-A0||||x||. No bound on E is needed.

Completing the pair in the full affine polynomial gives

`Q=(X_pair+m(Z))^T B (X_pair+m(Z))+R(Z)`

where Z comprises all remaining ORIGINAL coordinates, m is affine, and the quadratic matrix of R is S. By (4.1), ||S||>=s. Lemma (3.1) consequently gives

`P(|R-t|<rho)<=5*s^(-1/4)*rho^(1/4)`

uniformly in t, with every induced affine term retained. The original pair is independent of Z; no spectral conditioning has been introduced.

## 5. Logarithmic averaging and the explicit constant

For any gradient cutoff r>0 the companion pair envelope yields

`p_Q(t)<=2sqrt(2)/r`
` +D^(-1/2)*E log_+(2r^2/(kappa*|t-R|))`.

Layer cake and the quarter-power small-ball estimate give, for a>0,

`E log_+(a/|t-R|)`
` =integral_0^infinity P(|t-R|<a*exp(-v))dv`
` <=20*s^(-1/4)*a^(1/4)`.

Hence

`p_Q(t)<=A1/r+B1*sqrt(r)`,

`A1=2sqrt(2)`,
`B1=20*2^(1/4)*D^(-1/2)*kappa^(-1/4)*s^(-1/4)`.

The minimum over r>0 is attained at r=(2A1/B1)^(2/3), and equals

`3*(A1*B1^2/4)^(1/3)`
` =3*400^(1/3)*D^(-1/3)*kappa^(-1/6)*s^(-1/6)`.

This is (1.1). Absolute continuity follows from the conditional pair-density formula and Tonelli; the common uniform bound gives essential boundedness.

For (1.2), the physical pair is a diagonal perturbation of [[0,Aij],[Aij,0]] by a matrix of norm at most 1/4. It is indefinite and kappa>=1/4; also D>=kappa^2. Take r=kappa rather than the optimized r, retain the cap one in the remainder small-ball bound, and use

`integral_0^infinity min(1,M*exp(-v/4))dv <=4+4log_+ M`.

With M=5*(2kappa/s)^(1/4) and s>=1 this gives

`p_Q(t)<=[2sqrt(2)+4+log_+(1250*kappa)]/kappa`.

This expression is decreasing for kappa>0: outside its constant-log branch the derivative has numerator 1-(2sqrt(2)+4)-log(1250kappa)<0. Evaluate at kappa=1/4 to obtain (1.2), about 50.29. QED.

## 6. What this does and does not settle

The two-coordinate branch no longer requires exact rank three, a low-rank remainder, separable extra directions, or an affine-in-range restriction. It uses ONLY the original independence/density normalization, s_3(A)>=s, and the quantitative indefinite physical-pair certificate. Zero scalar pivots remain allowed.

It still requires such a quantitatively useful original-coordinate pair. The singleton-plus-two-banks family with spectrum {1,1,-1} has every indefinite physical pair poorly conditioned as the bank size grows. Diffuse/ridge arguments and genuine coordinate grouping remain necessary; no exhaustive reduction combining them with this theorem has been established here. Thus the unrestricted conjecture is not declared proved.

Claim IDs: QFORM-ARBITRARY-RANK-QUARTER-SMALLBALL-v1; QFORM-FULL-MATRIX-INDEFINITE-PAIR-LOG-v1.
