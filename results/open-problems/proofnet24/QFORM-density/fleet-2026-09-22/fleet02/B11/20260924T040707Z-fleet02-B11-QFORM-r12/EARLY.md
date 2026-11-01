SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-24T04:07:07Z.
attacking: exact-null near-coloop same-bank puncture; spend a genuine original-coordinate transverse Pluecker atom before collapsing the residual product source to marginal norms.

# EARLY — null-hub Pluecker-atom payment

Full QFORM is OPEN. This note records the first substantive implication before the final report.

## Affine null-scalar/dependent-pair extension

Let X be independent of a pair (C,D), with density cap ||f_X||_infinity<=F and joint pair-density cap ||g||_infinity<=M. Let beta,gamma be nonzero and allow arbitrary real alpha,delta and arbitrary affine terms. Then

Q = 2 beta X C + alpha C^2 + 2 delta C D + gamma D^2
    + l_X X + l_C C + l_D D + const

has an essentially bounded density satisfying

||p_Q||_infinity <= 3 (2 M F)^(2/3) |beta^2 gamma|^(-1/3).

Equivalently, if B is the 3x3 quadratic matrix after an area-preserving rotation of the pair so that the null scalar couples only to C, then beta^2 gamma=-det B and

||p_Q||_infinity <= 3 (2 M F)^(2/3) |det B|^(-1/3).       (E.1)

Proof: condition on (C,D)=(c,d). The affine slope in X is L(c)=2 beta c+l_X, so the conditional kernel is

K_s(c,d)=|L(c)|^(-1) f_X((s-R(c,d))/L(c)),

where R is quadratic in d with leading coefficient gamma. If K_s>u, then |L(c)|<F/u. For fixed c, E_m={x:f_X(x)>m}, m=u|L(c)|, has Lebesgue measure <=1/m. The map d -> (s-R(c,d))/L(c) is quadratic with leading coefficient -gamma/L(c); the preimage of a set of length 1/(u|L(c)|) therefore has d-length at most 2/(sqrt(|gamma|) sqrt(u)). The allowed c-interval has length F/(|beta|u). Hence

|{(c,d):K_s(c,d)>u}| <= [2F/(|beta|sqrt(|gamma|))] u^(-3/2).

Using both g<=M and int g=1, layer cake gives

p_Q(s) <= int_0^infinity min(1, A u^(-3/2)) du = 3 A^(2/3),
A=2MF/(|beta|sqrt(|gamma|)),

which is (E.1). This is the affine version of the completed fleet02/B16 null-scalar/dependent-pair receiver; no independence is asserted inside the pair.

## New exact-rank-three consequence: QFORM-NULL-HUB-PLUCKER-ATOM-v1

Let A=R M R^T have exact rank three, R^T R=I_3, and all three nonzero eigenvalues of M have modulus at least s. Suppose original coordinate 0 has exact null pivot A_00=0 and leverage q=||r_0||^2>0. Rotate only the spectral bookkeeping so r_0=sqrt(q)e_1. Write each residual row as

r_i = a_i e_1 + b_i,  b_i in e_1^perp ~= R^2.

Parseval gives sum_{i!=0} b_i b_i^T=I_2. Therefore Cauchy-Binet gives

sum_{i<j, i,j!=0} det(b_i,b_j)^2 = 1.                 (E.2)

For a pair (i,j), put omega_ij=det(b_i,b_j)^2. Then

det(R_{0ij})^2 = q omega_ij,
|det A[{0,i,j}]| = |det M| q omega_ij.                (E.3)

Choose omega_*=max omega_ij>0. Condition on every original coordinate except X_0,X_i,X_j. The remaining polynomial has arbitrary affine terms and quadratic block B=A[{0,i,j}], with B_00=0. Rotate only the two-dimensional pair (X_i,X_j) to align the coupling from X_0. Its joint density stays <=1 by the determinant-one change of variables and remains independent of X_0. Applying (E.1) with F=M=1 and averaging the conditional densities yields

boxed:
||p_{X^T A X}||_{infinity,ess}
 <= 3*2^(2/3) (|det M| q omega_*)^(-1/3)
 <= 3*2^(2/3) (q omega_*)^(-1/3) / s.                (E.4)

Thus a true same-bank puncture can only remain hard if its transverse two-frame has no macroscopic original-coordinate Pluecker atom.

If exactly m residual original coordinates carry the active frame, (E.2) implies omega_*>=1/binom(m,2), hence

boxed:
||p||_infinity <= 3*2^(2/3) [binom(m,2)/q]^(1/3) / s. (E.5)

At the partner near-coloop threshold q>=63/64 and m=3 this is <6.905/s. This already closes every r45 null-pivot same-bank model whose residual orthogonal triple lives on three original coordinates, including arbitrary internal dependence created by a 3x3 orthogonal rotation of those coordinates.

## First unpaid implication

QFORM-R48-DIFFUSE-TRANSVERSE-PLUCKER-COMPILER-v1:
After the already-paid large-leaf/pair-area exits, and after (E.4) removes every fixed transverse Pluecker atom, prove a uniform opposite-two-sheet bound in the regime

max_{i<j} det(b_i,b_j)^2 -> 0,

using the exact orthogonal-product factorization of the residual source before any dependence-blind L^3 x L^(3/2) split; or force a source-disjoint square / rank-two crossing / volume exit. Partner r48 shows that joint and coordinate-marginal caps alone cannot perform this diffuse aggregation.
