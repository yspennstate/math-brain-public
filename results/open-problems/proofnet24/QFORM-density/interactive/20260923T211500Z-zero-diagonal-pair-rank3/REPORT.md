# Rank-three receiver with a zero-diagonal physical pair

Status: proved scoped theorem, including arbitrary affine terms and arbitrary couplings to conditioned outside originals.

## Theorem

Let X_1,X_2,X_3 be independent real random variables with Lebesgue densities bounded by one. Let

A = [[0, alpha, beta],
     [alpha, 0, gamma],
     [beta, gamma, d]]

be symmetric. If s_3(A)≥sigma>0, then for every b in R^3 the quadratic-affine form Q=X^TAX+b·X has a density bounded by

||p_Q||_infinity ≤ (3+log 16)/sigma < 5.773/sigma.

More generally, let this A be a physical principal 3 by 3 submatrix of any larger symmetric matrix, with arbitrary couplings to all remaining independent original inputs and arbitrary affine coefficients. The same bound holds for the full quadratic-affine form, because conditioning the remaining inputs only changes b and adds a constant shift.

In particular, this covers the all-off-diagonal triangle, a bilinear edge with an independent square, and arbitrary values of beta,gamma,d satisfying the third-singular-value hypothesis.

## Algebraic reduction and spectral scales

Since s_3(A)>0, alpha is nonzero. Set

kappa = d - 2 beta gamma/alpha.

Condition on X_3=z and define

U=X_1+(gamma/alpha)z+b_2/(2alpha),
V=X_2+(beta/alpha)z+b_1/(2alpha).

For every z, U and V are independent with density caps one. Expansion yields

Q=2alpha UV+g(z),

where g is a real quadratic polynomial with leading coefficient kappa. The affine b changes the lower-degree coefficients of g but never kappa.

Both |alpha| and |kappa| are at least sigma. Indeed, deleting the alpha edge gives a matrix of rank at most two and changes A by an operator-norm |alpha| matrix, so s_3(A)≤|alpha|. Replacing d by 2 beta gamma/alpha gives a rank-two matrix and changes A by an operator-norm |kappa| matrix, so s_3(A)≤|kappa|.

## Product and quadratic estimates

For independent density-cap-one U,V and nonzero t,

p_{UV}(t)≤2+2log_+(1/|t|).

To prove this, write p_{UV}(t)=∫f_U(u)f_V(t/u)du/|u|. On |u|≤|t|, use f_U≤1 and v=t/u to obtain at most ∫_{|v|≥1}f_V(v)dv/|v|≤1. On |t|<|u|<1, use both density caps to obtain at most 2log_+(1/|t|). On |u|≥1, use f_V≤1 and ∫f_U=1 to obtain at most one. If |t|≥1 the first and third regions overlap, which only increases this upper bound.

Also, for any real quadratic polynomial g with leading coefficient kappa nonzero,

Leb{z:|s-g(z)|≤delta}≤2sqrt(2delta/|kappa|)

for every s and delta>0. Complete the square and maximize the length of |y^2-c|≤delta over c; the maximum is 2sqrt(2delta).

It follows that a conditional density version satisfies

p_{Q|X_3=z}(s)
 ≤ |alpha|^(-1)[1+log_+(2|alpha|/|s-g(z)|)].

The roots of s-g(z) have zero X_3 probability. By layer cake and the density cap of X_3,

E log_+(2|alpha|/|s-g(X_3)|)
 ≤ ∫_0^infinity min(1,C e^(-t/2))dt,

C=4sqrt(|alpha|/|kappa|).

The integral is 2C when C≤1, and 2+2log C when C≥1. Because |kappa|≥sigma,

C≤4sqrt(|alpha|/sigma).

Therefore

||p_Q||_infinity
 ≤ |alpha|^(-1)[3+log 16+log(|alpha|/sigma)].

For x=|alpha|/sigma≥1, the right side is
[3+log 16+log x]/(sigma x), a decreasing function of x. Its value at x=1 is (3+log 16)/sigma, proving the theorem.

## Scope

The theorem relies on two exactly zero diagonal entries in a physical principal triple. A global condition s_3(A_full)≥sigma need not provide such a triple with its own s_3≥sigma. Arbitrary nonzero diagonal entries on both members of the bilinear pair require another receiver. Thus the unrestricted QFORM/RMT density theorem remains open.
