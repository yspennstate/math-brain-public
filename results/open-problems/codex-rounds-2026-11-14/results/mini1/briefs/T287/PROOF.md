# A fourth-order constraint on extensive-rank matrix denoising

Let the entries of U and V be mutually independent, with iid entries within each matrix. Their two entry laws are fixed independently of N,P,M, bounded, symmetric about zero, and have variance one. Write

\[
 X=N^{-1/2}UV^\top,\quad d=NP,\quad \rho=M/N,
 \quad a=\mathbb E U_{11}^4,\quad b=\mathbb E V_{11}^4.
\]

Let W have independent standard Gaussian entries, independently of the factors, and put Y_t=√t X+W. All logarithms are natural. Define

\[
 i_{N,P,M}(t)=d^{-1}I(X;Y_t),\qquad
 e_{N,P,M}(t)=d^{-1}\mathbb E\|X-\mathbb E[X\mid Y_t]\|_F^2.
\]

The mutual information also equals I((U,V);Y_t)/d: the conditional distribution of Y_t given the factors depends only on X.

## Theorem

For each fixed positive N,P,M, as t decreases to zero,

\[
 i_{N,P,M}(t)=\frac12\log(1+\rho t)-C_{N,P,M}t^4+O_{N,P,M}(t^5),                 \tag{1}
\]
\[
 e_{N,P,M}(t)=\frac{\rho}{1+\rho t}-8C_{N,P,M}t^3+O_{N,P,M}(t^4),             \tag{2}
\]
where

\[
 C_{N,P,M}=\frac{M^2}{48N^4}
 \left[(ab-3)^2+3(P-1)(a-1)^2+3(N-1)(b-1)^2+6(N-1)(P-1)\right].             \tag{3}
\]

Consequently, if M/N→α>0 and P/N→β>0, then

\[
 \lim C_{N,P,M}=\frac{\alpha^2\beta}{8}.                                  \tag{4}
\]

Thus the iterated limit of the normalized Gaussian entropy deficit is

\[
 \lim_{N\to\infty}\lim_{t\downarrow0}
 \frac{\frac12\log(1+(M/N)t)-i_{N,P,M}(t)}{t^4}
 =\frac{\alpha^2\beta}{8}.                                               \tag{5}
\]

No uniform remainder or interchange of these limits is asserted. Formula (2) concerns X. The per-entry MMSE of the unscaled product UVᵀ is N e_{N,P,M}(t).

## 1. A bounded-vector Gaussian-channel calculation

First let X be any bounded random vector in R^d satisfying X equal in law to −X and Cov(X)=ρI_d. Denote its fourth cumulant tensor by

\[
 K_{ijkl}=\mathbb E X_iX_jX_kX_l
 -\rho^2(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}),
 \qquad \|K\|^2=\sum_{i,j,k,l}K_{ijkl}^2.
\]

Let φ be the standard Gaussian density, s=1+ρt, and let f_t be the density of Z_t=Y_t/√s relative to φ. Put r=√(t/s), so that Z_t=rX+√(1−ρr²)W. Direct division of Gaussian densities gives

\[
 f_t(z)=(1-\rho r^2)^{-d/2}
 e^{-\rho r^2\|z\|^2/[2(1-\rho r^2)]}
 \mathbb E\exp\left\{
 \frac{r z\cdot X}{1-\rho r^2}
 -\frac{r^2\|X\|^2}{2(1-\rho r^2)}\right\}.                              \tag{6}
\]

Taylor expansion of (6), in any fixed finite L^p(φ), and also after one z derivative, yields

\[
 f_t=1+t^2 A+O_{L^p}(t^3),\qquad
 \nabla f_t=t^2\nabla A+O_{L^p}(t^3),\qquad
 A=\frac1{24}\sum_{i,j,k,l}K_{ijkl}H_{ijkl}.                              \tag{7}
\]

Here H_{ijkl}(z)=φ(z)^{-1}∂_i∂_j∂_k∂_l φ(z) is the fourth Gaussian Hermite tensor. The analytic justification and the coefficient can be checked as follows. Boundedness of X makes every fixed r derivative of (6) bounded, for small |r|, by a polynomial in ||z|| times exp(ε||z||²+C||z||), with ε arbitrarily small on a sufficiently short r interval. This bound is integrable to every fixed finite power against φ. Taylor's theorem with an integral remainder therefore applies in these spaces, including after a z derivative. Symmetry removes the odd powers. The second-order term vanishes because the covariance is exactly matched. For the fourth-order term use the generating identity

\[
 \mathbb E\exp(h\cdot Z_t-\|h\|^2/2)
 =\mathbb E\exp(rh\cdot X-\rho r^2\|h\|^2/2)
 =1+\frac{r^4}{24}\sum K_{ijkl}h_ih_jh_kh_l+O(r^6).
\]

The order-r⁴ coefficient in (6) is a polynomial of degree at most four. The generating identity identifies all its Hermite coefficients, proving (7), since r⁴=t²+O(t³).

Gaussian Hermite orthogonality gives

\[
 \int A\,\phi=0,\qquad
 \int A^2\phi=\frac{\|K\|^2}{24},\qquad
 \int\|\nabla A\|^2\phi=4\int A^2\phi.                                 \tag{8}
\]

For completeness, the expectation of H_{ijkl}H_{abcd} is the sum of the 24 products of Kronecker deltas matching the four indices of the first tensor to those of the second. Contracting with the symmetric tensor K twice and dividing by 24² gives the middle equality. For the last equality, multivariate Hermite polynomials of total degree four satisfy (Δ−z·∇)A=−4A; Gaussian integration by parts gives the stated gradient norm. Both identities follow as well by differentiating exp(h·z−||h||²/2).

For x≥−1 the function

\[
 (1+x)\log(1+x)-x-\tfrac12x^2
\]

has absolute value at most a universal constant times |x|³. This follows by Taylor expansion near zero, continuity on a compact interval including −1, and its O(x²+x log x) growth at infinity. Apply this to x=f_t−1 and use (7) in L² and L³. Since ∫(f_t−1)φ=0,

\[
 D(f_t\phi\|\phi)=\tfrac12t^4\int A^2\phi+O(t^5)
 =\frac{t^4}{48}\|K\|^2+O(t^5).                                       \tag{9}
\]

The output has covariance sI_d. Subtracting its relative entropy to its matching Gaussian from that Gaussian's entropy gives exactly

\[
 I(X;Y_t)=\frac d2\log s-D(f_t\phi\|\phi).                              \tag{10}
\]

This proves the vector version of (1).

Here is a separate calculation of its MMSE, without differentiating the remainder in (9). The Gaussian likelihood implies

\[
 \mathbb E[X\mid Y_t=y]=\frac{y+\nabla_y\log p_{Y_t}(y)}{\sqrt t}
 =\frac{\rho\sqrt t}{s}y+
 \frac{1}{\sqrt{ts}}\nabla\log f_t(y/\sqrt s).                           \tag{11}
\]

Indeed, differentiating p_{Y_t}(y)=E φ(y−√tX) under the expectation gives the first equality. The best linear estimate is L(y)=ρ√t y/s and has error dρ/s. The posterior mean minus L(Y_t) is orthogonal to Y_t: E[X Y_tᵀ]=ρ√t I_d, and E[L(Y_t)Y_tᵀ] is the same matrix. The usual conditional-expectation orthogonality then gives

\[
 \mathbb E\|X-\mathbb E[X\mid Y_t]\|^2
 =\frac{d\rho}{s}-\frac1{ts}\int\frac{\|\nabla f_t\|^2}{f_t}\phi.          \tag{12}
\]

To justify expansion of the denominator, Jensen's inequality in (6) gives

\[
 f_t(z)\ge (1-\rho r^2)^{-d/2}
 \exp\left[-\frac{\rho r^2\|z\|^2+r^2d\rho}{2(1-\rho r^2)}\right].       \tag{13}
\]

Thus f_t^{-1} is bounded in every fixed finite L^p(φ) for sufficiently small t. In (7) let B_t=∇f_t/t²=∇A+O_{L^p}(t). Hölder's inequality and (13) show

\[
 \int \frac{\|B_t\|^2}{f_t}\phi
 =\int\|\nabla A\|^2\phi+O(t).
\]

In detail, the contribution of (||B_t||²−||∇A||²)/f_t is O(t), using the L⁴ bounds for B_t,∇A and the L² bound for f_t^{-1}. The remaining difference uses f_t^{-1}−1=(1−f_t)/f_t and Hölder with the finite polynomial moments of ∇A, the O(t²) bounds for f_t−1, and (13). Substitution into (12), followed by (8), proves

\[
 d^{-1}\operatorname{mmse}(X\mid Y_t)
 =\frac\rho s-\frac{\|K\|^2}{6d}t^3+O(t^4).                            \tag{14}
\]

## 2. The complete fourth-cumulant tensor of the matrix product

Vectorize the matrix by indexing coordinates with edges (i,j) of the complete bipartite graph on N row and P column vertices. Each column of the factors contributes an independent vector N^{-1/2}(u_i v_j)_{ij}. Direct expansion of fourth moments of a sum of independent centered vectors shows that fourth cumulants add: terms involving two different summands cancel against the three covariance products; terms involving a summand only once vanish. Hence K for X is M/N² times the fourth-cumulant tensor of one outer product.

Its covariance is δ_{ii′}δ_{jj′}, by independence and unit variance. In a product of four edges, symmetry makes the fourth moment vanish unless every row and column vertex has even degree, counting repetitions. There are exactly four types with possibly nonzero cumulant:

1. One edge four times: fourth moment ab, with three covariance products to subtract. The value is ab−3.
2. Two distinct edges twice each, sharing their row: fourth moment a and one covariance product. The value is a−1.
3. Two distinct edges twice each, sharing their column: the value is b−1.
4. Four distinct edges forming a rectangle: fourth moment one and no covariance products. The value is one.

Two disjoint edges twice each have fourth moment one and exactly one covariance product, so their cumulant is zero. This completes the classification: an even-degree bipartite multigraph with four edges is either a union of doubled edges, a quadrupled edge, or a simple four-cycle. Any other pattern has an odd-degree vertex and zero moment; its covariance products also vanish because its edge multiset cannot be paired identically.

Counting ordered quadruples gives respectively

\[
 d,\quad 6N\binom P2=3d(P-1),\quad
 6P\binom N2=3d(N-1),\quad
 24\binom N2\binom P2=6d(N-1)(P-1).
\]

Therefore

\[
 \frac{\|K\|^2}{d}=\frac{M^2}{N^4}
 [(ab-3)^2+3(P-1)(a-1)^2+3(N-1)(b-1)^2+6(N-1)(P-1)].                      \tag{15}
\]

The vector X is bounded and centrally symmetric, with covariance ρI_d. Applying (9), (10), and (14) proves (1)–(3). In the proportional limit, the first term of the bracket in (15) contributes O(N^{-2}), the next two O(N^{-1}), and the rectangle term tends to 6α²β. This proves (4) and (5).

## 3. Rademacher specialization and limitations

For a=b=1,

\[
 C_{N,P,M}=\frac{M^2}{48N^4}[4+6(N-1)(P-1)].                            \tag{16}
\]

For N=P=M=1 this is 1/12. Expanding (1) then gives t/2−t²/4+t³/6−5t⁴/24+O(t⁵), while (2) gives 1−t+t²−5t³/3+O(t⁴). These coefficients can also be obtained directly from the scalar posterior mean tanh(√t Y_t).

The limiting coefficient is independent of the fixed bounded symmetric priors, although their finite-size coefficients differ. It does not show an advantage over a rotationally invariant estimator. It quantifies dependence relative to an independent Gaussian vector with the same covariance. No assertion about estimating U modulo column signs and permutations follows from this theorem.

One can isolate dependence from non-Gaussianity of the individual entries. Let

\[
 j_{N,P,M}(t)=\frac1d\sum_{i,j}I(X_{ij};\sqrt t X_{ij}+W_{ij}).
\]

Apply the bounded-vector calculation with dimension one to each entry. Its fourth cumulant is M(ab−3)/N², so

\[
 j_{N,P,M}(t)-i_{N,P,M}(t)
 =\frac{M^2t^4}{48N^4}
 [3(P-1)(a-1)^2+3(N-1)(b-1)^2+6(N-1)(P-1)]+O_{N,P,M}(t^5).               \tag{17}
\]

This difference equals d^{-1}D(P_{Y_t} || \prod_{i,j}P_{(Y_t)_{ij}}), since the conditional noise entropies add and cancel. It is therefore nonnegative for every t. Its t⁴ coefficient again tends to α²β/8. For Rademacher factors at N=P=M=2 the coefficient is 1/32: the full deficit is 5/96, while the one-entry deficit is 1/48. Thus convergence of individual entry distributions alone cannot justify discarding the dependence term in this order of limits.
