# A cubic Gaussian replacement bound at an omitted input

Let d,k be positive integers and let

\[
 \varphi(z)=(z^3-3z)/\sqrt6,\qquad
 F_W(x)=k^{-1/2}\sum_{i=1}^k\varphi(w_i\cdot x/\sqrt d).
\]

The weight prior has independent N(0,I_d) rows. All readouts equal one. The input X has distribution N(0,I_d). All norms of tensors below are Euclidean norms of their coordinate arrays.

## Statement

Suppose W^1,...,W^s have any joint distribution such that each W^a individually has the weight prior. Suppose X is independent of their joint distribution. Auxiliary randomness A may depend on the weights but is independent of X jointly with them. Put F_a=F_{W^a}(X). Define, for each network,

\[
 u_i=w_i/\sqrt d,\quad r_i=\|u_i\|^2,\quad
 T=k^{-1/2}\sum_i u_i^{\otimes3},\quad
 b=\sqrt{3/(2k)}\sum_i(r_i-1)u_i.
\]

Use a superscript a for tensors and vectors belonging to W^a. Define the random covariance matrices

\[
 C_{ab}=\langle T^a,T^b\rangle
     ={1\over k}\sum_{i,j}(u_i^a\cdot u_j^b)^3,
 \qquad K_{ab}=C_{ab}+b^a\cdot b^b.
\]

Both matrices are positive semidefinite, and K is the actual covariance of F conditional on all the weights.

Write

\[
 M_p=\prod_{j=0}^{p-1}(1+2j/d),\quad
 \rho=M_3-2M_2+M_1,\quad
 \eta=M_6-4M_5+6M_4-4M_3+M_2,
\]

\[
 \delta={M_6\over k}+{k-1\over k}M_3^2
 \left({1\over d}+{3\over d(d+2)}+
 {15\over d(d+2)(d+4)}\right),
\]

\[
 \beta={9\over4}\left[{\eta\over k}
       +{k-1\over k}(1+2/d)\rho^2\right],\qquad
 \ell={3\over2}\rho={3\over d}+{12\over d^2},
\]

and

\[
 \varepsilon^2=6\delta+
 2\left[2\sqrt\delta+{4\over\sqrt6}(\delta\beta)^{1/4}\right]^2.
 \tag{1}
\]

There is an explicit, generally nonsymmetric random matrix \(\Gamma(X,W)\) with

\[
 \mathbb E_X\Gamma_{ab}=K_{ab},\qquad
 \mathbb E_{W,X}|\Gamma_{ab}-K_{ab}|^2\leq\varepsilon^2.
 \tag{2}
\]

For every C^1 function h=h_{W,A}:R^s to R with bounded first derivatives, the conditional identity

\[
 \mathbb E_X[F_a h(F)]
   =\sum_{b=1}^s\mathbb E_X[\Gamma_{ab}\partial_b h(F)]
 \tag{3}
\]

holds. In particular, if \(|\partial_b h|\leq L_b\) uniformly in the weights and A, then

\[
 \mathbb E_{W,A}\left|
 \mathbb E_X[F_a h(F)]-
 \sum_b K_{ab}\mathbb E_X[\partial_b h(F)]\right|
 \leq\varepsilon\sum_b L_b.
 \tag{4}
\]

Let G_K and G_C, conditionally on W,A, be centered Gaussian vectors with covariance K and C, respectively. For every C^2 h=h_{W,A} with bounded first derivatives and \(|\partial_{ab}h|\leq H_{ab}\) uniformly,

\[
 \mathbb E_{W,A}\left|
 \mathbb E_X h(F)-\mathbb E_{G_K}h(G_K)\right|
 \leq {\varepsilon\over2}\sum_{a,b}H_{ab},
 \tag{5}
\]

\[
 \mathbb E_{W,A}\left|
 \mathbb E_X h(F)-\mathbb E_{G_C}h(G_C)\right|
 \leq {\varepsilon+\ell\over2}\sum_{a,b}H_{ab}.
 \tag{6}
\]

These conclusions hold even when C or K is singular. If k/d tends to gamma in (0,infinity),

\[
 d\delta\longrightarrow1+1/\gamma,\qquad
 d^2\beta\longrightarrow9,\qquad
 \sqrt d\,\varepsilon\longrightarrow
       \sqrt{14(1+1/\gamma)}.
 \tag{7}
\]

Thus (4)--(6) have error O(d^-1/2) for a fixed number of networks and fixed derivative bounds. These are bounds for test functions of network outputs, not a Bayes prediction-error formula.

## Wick polynomials and contractions

For a symmetric order-p tensor S, define its Wick polynomial I_p(S) by linear extension of the coefficients in

\[
 \exp(t\cdot X-\|t\|^2/2)
 =\sum_{p\geq0}{1\over p!}I_p(t^{\otimes p}).
\]

In particular, I_1(v)=v dot X and

\[
 I_2(B)=\sum_{i,j}B_{ij}(X_iX_j-\mathbf1_{i=j}),\quad
 I_3(v^{\otimes3})=(v\cdot X)^3-3\|v\|^2(v\cdot X).
\]

For a nonsymmetric tensor, I_p means I_p of its symmetrization. Taking the expectation of the product of two generating functions gives exp(t dot z); comparing coefficients gives

\[
 \mathbb E I_p(S)I_q(U)=\mathbf1_{p=q}\,p!\langle S,U\rangle
 \tag{8}
\]

for symmetric S,U. The coefficients of the product of the generating functions also give

\[
 I_2(B)I_2(D)=I_4(\operatorname{sym}(B\otimes D))
 +4I_2(\operatorname{sym}(BD))+2\langle B,D\rangle.
 \tag{9}
\]

To see the coefficients in (9), a product of two pairs has zero, one or two cross contractions. There is one way to make no contraction, four choices of a single cross pair, and two bijections making two cross pairs. This also proves (9) for arbitrary symmetric B,D by linearity.

For symmetric order-three tensors S,U define

\[
 (S\otimes_1 U)_{ij\ell m}=\sum_p S_{ijp}U_{\ell mp},
 \qquad (S\otimes_2 U)_{ij}=\sum_{p,q}S_{ipq}U_{jpq}.
\]

For a vector v let \((S\otimes_1 v)_{ij}=\sum_pS_{ijp}v_p\). Symmetrization is an orthogonal projection and cannot increase a tensor's norm.

Set D(S)=||S contraction_2 S||^2. Flatten S into a matrix whose row is its first index and whose column is the remaining pair of indices. The two self-contractions have the form MM^T and M^TM. Expanding their squared norms gives the same trace, Tr((MM^T)^2), so

\[
 \|S\otimes_1 S\|^2=\|S\otimes_2 S\|^2=D(S).
 \tag{10}
\]

Directly summing the contracted coordinates yields

\[
 \|S\otimes_1 U\|^2
   =\langle S\otimes_2 S,U\otimes_2 U\rangle,
 \quad
 \|S\otimes_2 U\|^2
   =\langle S\otimes_1 S,U\otimes_1 U\rangle.
\]

Cauchy--Schwarz and (10) imply, for r=1,2,

\[
 \|S\otimes_r U\|^2\leq\sqrt{D(S)D(U)}.
 \tag{11}
\]

Also,

\[
 \|S\otimes_1 v\|^2
   =v^T(S\otimes_2 S)v
   \leq\sqrt{D(S)}\,\|v\|^2.
 \tag{12}
\]

The last inequality bounds the operator norm of the positive matrix S contraction_2 S by its Euclidean matrix norm. No relationship between S,U,v is assumed.

## Exact prior moments

For a Gaussian row, r=||w||^2/d has moments E[r^p]=M_p. This follows by differentiating (1-2t/d)^(-d/2), its moment generating function, p times at zero. Independent rows have independent radii and independent uniform directions.

We claim

\[
 \mathbb E D(T)=\delta.
 \tag{13}
\]

Indeed, with q_ij=u_i dot u_j,

\[
 D(T)={1\over k^2}\sum_{i,j,l,h}
             q_{ij}^2q_{lh}^2q_{il}q_{jh}.
 \tag{14}
\]

Each of the four index positions contributes three occurrences of its row to the monomial. If some row index occurs an odd number of times, negating that row changes the sign of the monomial. Its expectation is zero. The surviving equality patterns are all four indices equal, or two distinct row indices each occurring twice.

The all-equal terms contribute k M6 before division by k^2. The three two-row patterns, each with k(k-1) terms, give

\[
 \begin{array}{c|c}
 i=j,\ l=h & r_i^2r_l^2q_{il}^2\\
 i=l,\ j=h & r_ir_jq_{ij}^4\\
 i=h,\ j=l & q_{ij}^6.
 \end{array}
\]

For two independent uniform directions e,f, rotational invariance reduces e dot f to the first coordinate of a uniform direction. Its even moments of orders 2,4,6 are

\[
 {1\over d},\quad {3\over d(d+2)},\quad
 {15\over d(d+2)(d+4)}.
\]

For completeness, write a standard Gaussian vector as R e, where R and e are independent. Then E[R^(2p)]=d(d+2)...(d+2p-2) and E[(R e_1)^(2p)]=(2p-1)!!. Dividing gives the stated direction moments, also for d=1. Since q_ij=sqrt(r_i r_j)(e_i dot e_j), all three radial expectations equal M3^2. Inserting the direction moments in (14) proves (13).

We also need

\[
 \mathbb E\|b\|^2=\ell,\qquad
 \mathbb E\|b\|^4=\beta.
 \tag{15}
\]

Here is a direct derivation. Set v_i=(r_i-1)u_i. These vectors are independent, centered, rotationally invariant, and

\[
 \mathbb E\|v_i\|^2=\rho,\quad
 \mathbb E\|v_i\|^4=\eta,\quad
 \mathbb E[v_iv_i^T]=(\rho/d)I_d.
\]

For i different from j, E[(v_i dot v_j)^2]=rho^2/d. In the square of
\(\|\sum_i v_i\|^2=\sum_i\|v_i\|^2+2\sum_{i<j}v_i\cdot v_j\), all mixed terms except matching unordered edges vanish by centering or row sign symmetry. Therefore

\[
 \mathbb E\|\textstyle\sum_i v_i\|^4
   =k\eta+k(k-1)(1+2/d)\rho^2.
\]

Scaling by 3/(2k), or its square, proves (15).

Because each marginal W^a is the prior, (11)--(15) imply for every pair a,b

\[
 \mathbb E\|T^a\otimes_rT^b\|^2\leq\delta\quad(r=1,2),
\]

\[
 \mathbb E\|T^a\otimes_1b^b\|^2
   \leq\sqrt{\delta\beta}.
 \tag{16}
\]

For the first inequality apply Cauchy--Schwarz to the expectation of sqrt(D(T^a)D(T^b)); for the second apply it to sqrt(D(T^a))||b^b||^2. These are valid for any coupling of the weights.

## The integration-by-parts identity

The Wick decomposition of the network is

\[
 F_a={1\over\sqrt6}I_3(T^a)+b^a\cdot X.
 \tag{17}
\]

Equation (8) proves that its covariance is K. Put H_a(X)_p=I_2(T^a_{p,\cdot,\cdot}). The gradients of the two terms of (17) are (3/sqrt(6))H_a and b^a.

The Gaussian generator L=Delta-X dot grad acts on I_p(S) as -p I_p(S). This follows by applying it to the generating function and comparing powers of t. Coordinatewise Gaussian integration by parts gives E[(-L f)g]=E[grad f dot grad g]. Apply this first to f=I_3(T^a)/3, then to f=b^a dot X, and add. For every admissible g,

\[
 \mathbb E_X[F_a g(X)]
 =\mathbb E_X[(H_a/\sqrt6+b^a)\cdot\nabla g(X)].
\]

Using g(X)=h(F(X)) and the chain rule proves (3) with

\[
 \Gamma_{ab}={1\over2}H_a\cdot H_b
  +{1\over\sqrt6}H_a\cdot b^b
  +\sqrt{3/2}\,b^a\cdot H_b+b^a\cdot b^b.
 \tag{18}
\]

Bounded derivatives ensure all integrals exist, since h grows at most linearly and F and Gamma are polynomials of X. A smooth cutoff and Gaussian integrability justify integration by parts for these functions.

Summing (9) over the common coordinate p gives

\[
 \Gamma_{ab}-K_{ab}
  ={1\over2}I_4(\operatorname{sym}(T^a\otimes_1T^b))
  +I_2\left(2\operatorname{sym}(T^a\otimes_2T^b)
      +{T^a\otimes_1b^b\over\sqrt6}
      +\sqrt{3/2}\,T^b\otimes_1b^a\right).
 \tag{19}
\]

This proves E_X Gamma_ab=K_ab. The two terms in (19) are orthogonal by (8). The first has averaged squared norm at most 4!/4 times delta, namely 6 delta. By the triangle inequality in the space of random tensor arrays and (16), the order-two tensor in parentheses has root mean-square norm at most

\[
 2\sqrt\delta+(1/\sqrt6+\sqrt{3/2})(\delta\beta)^{1/4}
 =2\sqrt\delta+{4\over\sqrt6}(\delta\beta)^{1/4}.
\]

Its Wick polynomial has twice its squared tensor norm by (8). This proves (1)--(2). Subtracting the constant K term from (3), using the derivative bounds, and then Cauchy--Schwarz proves (4). More generally the same argument bounds the absolute value of the averaged remainder by
\(\varepsilon\sum_b(\mathbb E|\partial_bh(F)|^2)^{1/2}\) whenever cutoff approximation justifies (3) and these moments are finite.

## Smooth Gaussian replacement

Condition on W,A and take G_K independent of X. For 0<t<1 set Y_t=sqrt(t)F+sqrt(1-t)G_K. Differentiate E h(Y_t), use (3) on F, and use ordinary Gaussian integration by parts on G_K. The factors sqrt(t) and sqrt(1-t) from the chain rule cancel their denominators in the derivative. The result is

\[
 {d\over dt}\mathbb E h(Y_t)
 ={1\over2}\sum_{a,b}\mathbb E[
       (\Gamma_{ab}-K_{ab})\partial_{ab}h(Y_t)].
 \tag{20}
\]

Integrating from zero to one and applying (2) proves (5). One can first integrate on [z,1-z], then send z to zero; bounded first derivatives and finite Gaussian polynomial moments ensure convergence at both endpoints. No inverse covariance is used.

For (6), let G_C have covariance C and let Z_b, independent of G_C, have covariance (b^a dot b^b)_ab. Then G_C+Z_b has covariance K. Ordinary Gaussian integration by parts along G_C+sqrt(t)Z_b gives

\[
 |\mathbb E h(G_K)-\mathbb E h(G_C)|
 \leq {1\over2}\sum_{a,b}H_{ab}|b^a\cdot b^b|.
\]

The expectation of |b^a dot b^b| is at most
sqrt(E||b^a||^2 E||b^b||^2)=ell. Combine this with (5) to prove (6).

## Rates and an independent check of the previous constants

For fixed p, expanding the finite product for M_p gives
\(M_p=1+p(p-1)/d+O(d^{-2})\). Consequently

\[
 \rho=2/d+8/d^2,\quad
 \eta=12/d^2+O(d^{-3}),\quad
 \delta=(1+1/\gamma)/d+o(d^{-1}),\quad
 \beta=9/d^2+o(d^{-2}).
\]

The second term inside the square brackets in (1) is O(d^-3/4), smaller than sqrt(delta). Thus epsilon^2=14 delta+o(d^-1), proving (7).

For comparison with round 3, decompose
\(C_{aa}=k^{-1}\sum_i r_i^3+(2/k)\sum_{i<j}q_{ij}^3\).
Distinct off-diagonal edges are uncorrelated by row sign symmetry, as are diagonal and off-diagonal terms. Conditional on u_i, q_ij is Gaussian of variance r_i/d, so E[q_ij^6]=15M3/d^3. Therefore

\[
 \mathbb EC_{aa}=M_3,\quad
 \operatorname{Var}(C_{aa})={M_6-M_3^2\over k}
              +{30(k-1)M_3\over kd^3}.
\]

Since M6-M3^2=18/d+O(d^-2),
\(d^2\mathbb E(C_{aa}-1)^2\to36+18/\gamma\).
The true variance K_aa=C_aa+||b^a||^2 has mean 1+9/d+20/d^2. Formula (15) gives

\[
 \operatorname{Var}(\|b\|^2)
 ={9\over4}\left[{\eta-\rho^2\over k}
            +{2(k-1)\rho^2\over kd}\right]=O(d^{-3}).
\]

Cauchy--Schwarz makes its covariance with C_aa o(d^-2). Hence
\(d^2\mathbb E(K_{aa}-1)^2\to81+18/\gamma\), independently recovering the previous report's main constants.

## Cavity posterior and sample normalization

Let a matched Bayesian observation model use independent Gaussian inputs X_1,...,X_n, a teacher with the weight prior, and arbitrary conditionally generated labels. Delete observation mu, including its input, and call the remaining data D_-mu. Side observations of the teacher that are independent of X_mu may be included. Conditional on D_-mu, the teacher has the cavity posterior distribution. Draw any fixed number of independent replicas from that distribution.

After averaging D_-mu, each teacher or replica marginal is the original prior: for every integrable H,

\[
 \mathbb E_{D_{-\mu}}\int H(W)P(dW\mid D_{-\mu})
 =\int H(W)P(dW).
\]

Moreover X_mu is independent of the joint cavity data, teacher and replicas. Thus the theorem applies to their outputs at X_mu. Dependence between the replicas after averaging the data is permitted by (11)--(16).

For a family of such tests h_mu with uniform derivative bounds, let R_mu be the conditional remainder in (4). Then

\[
 \mathbb E\left|{1\over n}\sum_{\mu=1}^n R_\mu\right|
 \leq\varepsilon\sum_b L_b.
 \tag{21}
\]

No independence between R_mu's is needed; this is the triangle inequality. If the normalization is d^2 instead, the bound is (n/d^2)epsilon sum_b L_b. Thus when n/d^2 tends to alpha, these normalized remainders still vanish. The corresponding assertion for the smooth replacement remainder follows from (5) or (6) with the same averaging argument.

## Scope

Appendix B.6 of Jean Barbier, Francesco Camilli, Minh-Toan Nguyen, Mauro Pastore and Rudy Skerk, [*Statistical physics of deep learning: Optimal learning of a multi-layer perceptron near interpolation*, arXiv:2510.24616v5](https://arxiv.org/html/2510.24616v5#A2.SS6), assumes a Gaussian replacement in (159) before its integration by parts. The result above supplies a quantitative cubic replacement for smooth finite-dimensional tests at a fresh input under the cavity law. It includes the difference between the actual covariance K and the Hermite covariance C.

It does not prove that the full likelihood-weighted expression (158) is a test satisfying these hypotheses. The weights under the full posterior depend on the omitted input and label. Expressing that posterior through the cavity law introduces a random likelihood normalization and, for log Z, a functional of the whole cavity measure. Bounds for finitely many replicas alone do not control that functional or its derivatives. Distinct-replica concentration (166), permutation alignment, and the remaining interpolation estimates are also unresolved. No Bayes-error or gradient-descent optimality theorem follows from (21).
