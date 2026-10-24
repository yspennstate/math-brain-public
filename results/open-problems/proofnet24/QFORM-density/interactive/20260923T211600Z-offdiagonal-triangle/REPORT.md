# Uniform density for the three-original off-diagonal triangle

Status: proved scoped result. This does not prove the unrestricted QFORM/RMT density theorem.

## Theorem

Let X_1,X_2,X_3 be independent real random variables, each with Lebesgue density bounded by one. Let A be a symmetric 3 by 3 matrix with zero diagonal and nonzero off-diagonal entries

A_12=alpha, A_13=beta, A_23=gamma.

For every affine coefficient b in R^3, Q=X^TAX+b·X has a density satisfying

||p_Q||_infinity ≤ (3+log 8)/m,

where m=min(|alpha|,|beta|,|gamma|).

If s_3(A)≥1, then m≥1, so

||p_Q||_infinity ≤ 3+log 8 < 5.08.

More generally, the three variables may be any physical coordinate triple of an n-input quadratic form. All couplings from this triple to the remaining independent originals are allowed. Condition the remaining inputs: their cross terms become arbitrary affine coefficients on the triple, and their own terms become a target shift. The same bound therefore holds whenever a principal 3 by 3 physical submatrix has this zero-diagonal triangle form. The spectral hypothesis s_3(A)≥1 in the displayed absolute bound refers to that principal submatrix, not to the full n by n matrix.

## Product density bound

If U,V are independent real variables with density caps one, then for every nonzero t a version of the product density obeys

p_{UV}(t) = integral f_U(u) f_V(t/u) du/|u|
 ≤ 2+2log_+(1/|t|).

To see this, split the integral into |u|≤|t|, |t|<|u|<1, and |u|≥1. The first part is at most one: use f_U≤1 and substitute v=t/u to obtain integral_{|v|≥1} f_V(v)dv/|v|≤1. The middle part is at most 2log_+(1/|t|), using both density caps. The final part is at most one, using f_V≤1 and integral f_U=1. Translations of U and V preserve the caps, so the estimate is uniform in their centers.

## Completing the triangle

Relabel the three originals so |alpha|=m. Condition on X_3=z and write

U=X_1+(gamma/alpha)z+b_2/(2alpha),
V=X_2+(beta/alpha)z+b_1/(2alpha).

Given z, U and V are independent and have density caps one. Direct expansion yields

Q=2alpha UV+g(z),

g(z)=b_3z-2alpha[(gamma/alpha)z+b_2/(2alpha)]
                     [(beta/alpha)z+b_1/(2alpha)].

The quadratic coefficient of g is -2beta gamma/alpha. Consequently, a version of the conditional density at s satisfies

p_{Q|X_3=z}(s)
 ≤ (1/|alpha|)[1+log_+(2|alpha|/|s-g(z)|)].

The right side is allowed to be infinite at roots of s-g(z); these roots have zero X_3 probability.

## Averaging the logarithm

For any nonzero kappa, any real r, and any delta>0, the set of z satisfying |kappa z^2+linear z+r|≤delta has length at most

2sqrt(2delta/|kappa|).

Proof: complete the square, rescale to |y^2-c|≤delta, and observe that the longest such set occurs when c=delta and has length 2sqrt(2delta).

Here |kappa|=2|beta gamma/alpha|. By layer cake and the density cap of X_3,

E log_+(2|alpha|/|s-g(X_3)|)
 = integral_0^infinity P(|s-g(X_3)|≤2|alpha|e^(-t))dt
 ≤ integral_0^infinity min(1,C e^(-t/2))dt,

where C=2sqrt(2)|alpha|/sqrt(|beta gamma|). Since |alpha| is the smallest edge magnitude, C≤2sqrt(2). Therefore the last integral is at most

integral_0^infinity min(1,2sqrt(2)e^(-t/2))dt
 = log 8+2.

Averaging the conditional product bound gives ||p_Q||_infinity≤(3+log 8)/|alpha|.

## Spectral normalization

Deleting the alpha edge from A leaves a matrix of rank at most two. The deleted symmetric two-entry edge matrix has operator norm |alpha|. The rank-approximation inequality therefore gives s_3(A)≤|alpha|. The same argument applies to each edge, so s_3(A)≤m. If s_3(A)≥1 then m≥1 and the claimed absolute bound follows.

For the equal-weight triangle alpha=beta=gamma=1, the eigenvalues are 2,-1,-1 and s_3(A)=1. This is a genuinely indefinite rank-three example that the definite two-hub and independent-star receiver lemmas do not cover.

## Scope

The theorem applies to any physical principal triangle block, including arbitrary couplings to every remaining original input. It does not handle nonzero diagonal coefficients on that triangle, nor does the full-matrix condition s_3(A)≥1 guarantee the existence of a principal triangle whose own third singular value is at least one. No assertion about the full conjecture follows from this scoped result.
