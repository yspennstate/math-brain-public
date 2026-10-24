# Independent check of the arbitrary-rank Gaussian-mixture theorem

The proof in paper_work/gaussian_mixture.tex, Theorem gm:main, was
independently checked both from the proposed derivation and from the
completed manuscript. No mathematical gap was found.

## Quantifiers

The independent pairs (M_i,T_i) may have arbitrary dependence within
each pair. Component centers may be random. The variances obey
0<T_i<infinity almost surely and E T_i^(-1/2)<=sqrt(2pi).
The matrix A has arbitrary rank, dimension, signature, and eigenvectors.
All original-coordinate affine terms are allowed.

## Fourier normalization

Conditional on the mixture parameters, write Q=G^TBG+ell^TG+c,
where B=D^(1/2)AD^(1/2) and D=diag(T_i).
The scalar Gaussian modulus is

    (1+4t^2 mu^2)^(-1/4)
       exp[-t^2 beta^2/(2(1+4t^2 mu^2))].

Thus arbitrary centers and affine terms only contribute a factor at
most one. If W=e_k(B^2), conditional inversion gives

    ||p_cond||infinity
      <= (I_k/(2pi)) W^(-1/(2k)),
    I_k=integral_0^infinity (1+u^(2k))^(-1/4) du.

The two-sided t integral and the factor2 in u=2t W^(1/(2k))
cancel exactly. There is no missing factor2 or pi.

## Random determinant average

Cauchy-Binet gives the sum over ordered pairs of coordinate subsets:

    W=sum_{|I|=|J|=k} det(A_IJ)^2 T_I T_J.

Intersections I cap J are allowed and correctly double the power of
their variance. With weights det(A_IJ)^2/Z and
alpha_i=Pr(i in I)+Pr(i in J), one has0<=alpha_i<=2 and
sum alpha_i=2k. Weighted AM-GM therefore yields

    W^(-1/(2k))
       <=Z^(-1/(2k)) prod T_i^(-alpha_i/(2k)).

Apply concavity to S_i=T_i^(-1/2), with exponent alpha_i/k<=2/k<1.
Independence gives

    E W^(-1/(2k))
      <=Z^(-1/(2k)) prod (E S_i)^(alpha_i/k)
      <=2pi Z^(-1/(2k)).

This cancels the conditional inversion denominator2pi.
It also gives integrability of the averaged Fourier majorant, hence
a C0 density (the manuscript states bounded and continuous).

## Constants and scope

The beta expression is

    I_k=(1/(2k)) B(1/(2k), 1/4-1/(2k)).

Both beta parameters are positive for k>2. Splitting at u=1 gives
I_k<1+2/(k-2)=k/(k-2). For s3(A)>=1, Z3>=1, so the density is
strictly less than3.

For each deterministic coordinate center m_i, the centered mixture
density increases to its peak as x approaches m_i. Monotone convergence
shows that its essential peak is exactly
(2pi)^(-1/2) E T_i^(-1/2), including infinite values. Thus capone is
equivalent to the moment condition for this centered class.
For random separated centers the cap does not imply the moment bound;
the manuscript states this restriction correctly.

The theorem is a rigorous positive result for a broad input class.
It does not establish the unrestricted bounded-density conjecture.
