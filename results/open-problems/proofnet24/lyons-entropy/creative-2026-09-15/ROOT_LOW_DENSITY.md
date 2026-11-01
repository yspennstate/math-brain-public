# A full-Hessian low-density theorem in every finite dimension

Date: 2026-09-15. Root's creative derivation; this is not one of the 100 agent executions. All assertions below are restricted theorems. The full Lyons conjecture remains open, and historical priority is not established.

## The theorem

Let n >= 2 and let B be a positive definite Hermitian n-by-n matrix with B_ij != 0 for every i != j. There is an explicit epsilon_0(B)>0 such that, at every marginal kernel K=epsilon B with 0<epsilon<=epsilon_0(B), the Shannon entropy of the occupation DPP has a negative definite Hessian on the entire real vector space of Hermitian directions. The same holds at I-epsilon B.

In particular, the result is not limited to radial directions or to dimension three. It gives an ambient neighborhood of strict concavity around each such base. No conclusion about sparse B, or about the whole segment up to its spectral boundary, is inferred.

Here is one deliberately conservative explicit radius. Define

\[
\lambda=\lambda_{\min}(B)>0,\quad \beta=\|B\|_{\rm op},\quad
b_* = \min_{i<j}|B_{ij}|>0,
\]
\[
Q=\max\{1,|\log\lambda|,|\log(2\beta)|\},\quad
c_*={b_*^2\over16\beta^2},\quad V=\beta+n\beta^2,
\]
\[
C_0=4nQ(n-1),\qquad
R=\sum_{k=3}^n {n\choose k}2^k nQ\,{(k+1)\beta^k\over\lambda^2}.
\]
The empty sum for n=2 is zero. Take

\[
\boxed{\epsilon_0=\min\left\{1,{1\over2\beta},
{b_*\over4\beta^2},{c_*\over2(R+1)},
{1\over2V(C_0+R+1)}\right\}.}
\tag{1}
\]

Writing a=diag(A) and A_off=A-diag(a), the quantitative conclusion is

\[
\boxed{D^2H(\epsilon B)[A,A]
\le -{\|a\|_2^2\over2V\epsilon}
     -{c_*\over2}\|A_{\rm off}\|_F^2.}
\tag{2}
\]

## 1. Remove the singular modular part of the atom logarithms

For an interior marginal kernel K its odds are L=K(I-K)^{-1}, and p_S=det(L_S)/det(I+L). For K=epsilon B write

\[
L_\epsilon=\epsilon M_\epsilon,\qquad
M_\epsilon=B(I-\epsilon B)^{-1}.
\]

The frozen atom weight f_epsilon(S)=-log p_S consists of a constant, the modular function -|S| log epsilon, and -log det((M_epsilon)_S). A constant or modular set function has an affine DPP expectation and contributes no second derivative in K. Thus all nonzero frozen curvature comes from the degree-at-least-two Boolean Mobius coefficients c_T(epsilon) of -log det((M_epsilon)_S).

For 0<epsilon<=1/(2 beta), all eigenvalues of M_epsilon and of its principal submatrices lie between lambda and 2 beta. Consequently

\[
|\log\det (M_\epsilon)_S|\le |S|Q\le nQ,
\qquad |c_T(\epsilon)|\le 2^{|T|}nQ.
\tag{3}
\]

All coefficients extend analytically to epsilon=0: M_epsilon does, all its limiting principal minors are positive, and the real logarithm is analytic there. In particular, the logarithmic singularity in epsilon has disappeared from the frozen Hessian.

For a pair T={i,j},

\[
c_{ij}(\epsilon)=
-\log\left(1-{|(M_\epsilon)_{ij}|^2\over
(M_\epsilon)_{ii}(M_\epsilon)_{jj}}\right)>0.
\tag{4}
\]

Moreover,

\[
\|M_\epsilon-B\|_{\rm op}
=\|\epsilon B^2(I-\epsilon B)^{-1}\|_{\rm op}
\le2\epsilon\beta^2.
\]

If additionally epsilon<=b_*/(4 beta^2), each off-diagonal magnitude of M_epsilon is at least b_*/2, while its diagonal entries are at most 2 beta. Since -log(1-r)>=r for 0<=r<1, (4) gives

\[
c_*\le c_{ij}(\epsilon)\le4nQ.
\tag{5}
\]

## 2. Frozen curvature has a uniform off-diagonal negative term

For any set function f with Mobius expansion f(S)=sum_{T subset S} c_T, the defining inclusion moments give exactly

\[
F_f(K):=\mathbb E_K f(X)=\sum_T c_T\det K_T.
\tag{6}
\]

The coefficients are frozen at the base when differentiating F_f. The pair terms therefore contribute exactly

\[
2\sum_{i<j}c_{ij}(\epsilon)
\bigl(a_i a_j-|A_{ij}|^2\bigr)
\le C_0\|a\|_2^2-c_*\|A_{\rm off}\|_F^2.
\tag{7}
\]

For the diagonal estimate use 2|a_i a_j|<=a_i^2+a_j^2 and (5); for the off-diagonal estimate use ||A_off||_F^2=2 sum_{i<j}|A_ij|^2.

If |T|=k>=3, homogeneity and determinant differentiation give

\[
D^2\det((\epsilon B)_T)[A_T,A_T]
=\epsilon^{k-2}\det B_T
\left[(\operatorname{tr}B_T^{-1}A_T)^2
-\operatorname{tr}(B_T^{-1}A_T)^2\right].
\]

The matrix B_T^{-1}A_T is similar to the Hermitian matrix B_T^{-1/2}A_T B_T^{-1/2}, whose Frobenius norm is at most lambda^{-1}||A||_F. Cauchy--Schwarz on its trace therefore bounds the absolute value of the preceding display by

\[
\epsilon^{k-2}{(k+1)\beta^k\over\lambda^2}\|A\|_F^2.
\]

Combining with (3), summing the finitely many T, and using epsilon<=1 yields

\[
\left|\sum_{|T|\ge3}c_T(\epsilon)
D^2\det K_T[A_T,A_T]\right|
\le R\epsilon\|A\|_F^2.
\tag{8}
\]

No sign claim for the individual higher Mobius coefficients is used.

## 3. Occupation Fisher information controls the diagonal modes

Let s(X)=Dp_X[A]/p_X be the score, I_K(A)=E s^2, and Sigma=Cov_K(X). Interior DPPs have full support, so Sigma is positive definite. Differentiating E X_i=K_ii gives Cov(X_i,s)=a_i. The variance of s-a^T Sigma^{-1}(X-E X) is nonnegative, proving

\[
I_K(A)\ge a^T\Sigma^{-1}a.
\tag{9}
\]

At K=epsilon B,

\[
\Sigma_{ii}=\epsilon B_{ii}(1-\epsilon B_{ii}),
\qquad \Sigma_{ij}=-\epsilon^2|B_{ij}|^2\quad(i\ne j).
\]

The absolute row sums, with epsilon<=1, are at most epsilon(beta+n beta^2)=epsilon V. Hence lambda_max(Sigma)<=epsilon V and

\[
I_K(A)\ge{\|a\|_2^2\over V\epsilon}.
\tag{10}
\]

## 4. Combine the two mechanisms

The exact entropy Hessian identity at a positive atom law is

\[
D^2H(K)[A,A]=-I_K(A)+D^2 F_{f_\epsilon}(K)[A,A].
\]

Using (7)--(10),

\[
D^2H(K)[A,A]
\le-\left({1\over V\epsilon}-C_0-R\epsilon\right)\|a\|_2^2
-(c_*-R\epsilon)\|A_{\rm off}\|_F^2.
\tag{11}
\]

The choices in (1) imply R epsilon<=c_*/2 and
C_0+R epsilon<=1/(2V epsilon), giving (2). Complementation satisfies H(I-K)=H(K) in the fixed occupation basis, so the high-density assertion follows with the same constants. Continuity of the interior Hessian gives the stated ambient neighborhoods. This completes the proof.

## What remains open

The radius (1) is explicit but crude. The dense off-diagonal assumption supplies a fixed negative coefficient for every off-diagonal direction. If B_ij=0, that coefficient may vanish at the limiting scale, and the higher-degree terms can no longer be discarded by this estimate. A sparse or globally scaled extension requires additional arguments. The theorem alone does not establish arbitrary-endpoint entropy concavity.
