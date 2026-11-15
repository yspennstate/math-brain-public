# Harmonic derivative and angle errors

Source: OpenAI, *Subpolynomial query complexity for well-conditioned log-concave sampling*, September 26, 2026, [Lemma 6.2](sources/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/numerics.tex), labelled `lem:kernel-angle-errors`. Its derivative input is Lemma 5.4 in [centering.tex](sources/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/centering.tex).

The result below proves the harmonic derivative implication and the resulting angle and harmonic interpolation errors. It assumes the spatial jet bounds of Proposition 3.2, the spatial transport bounds of Lemma 5.1, the exact probability-transport law, and the probability-circuit accuracy bound of Proposition 6.1. These inputs are stated explicitly below. Their complete proofs, the later endpoint-error quadrature, and the complete sampling theorem are outside this result.

## 1. Recheck of the inherited structural result

Write the forward correction as
\[
 C_{ij}=-r\sum_k w_{ijk}M_{ijk}.
\]
Its contribution to the kernel velocity is exactly
\[
 -\frac1{rs}\sum_{i,j}q_i d_j C_{ij}
 =\frac1s\sum_{i,j,k}q_i d_jw_{ijk}M_{ijk}.
 \tag{1}
\]
Thus no inverse power of r survives in the mean coefficients. Physical centers multiply normalized states by r; their coefficient sum is bounded by a fixed multiple of
\((r/\sigma)QD_\theta+r^2\), with \(s=\sigma/2\). The bound is uniform as r decreases to zero. This agrees with the round 4 proof.

The endpoint-rule recheck uses an independent construction. Let \(u_i=i/(m-2)\), \(0\le i\le m-2\), and let \(P_i\) be their ordinary Lagrange basis. Set \(v(u)=\prod_i(u-u_i)\). Then
\[
 H_i(u)=P_i(u)-\frac{P_i'(0)}{v'(0)}v(u)
\]
has the same nodal values as \(P_i\), has derivative zero at zero, and has degree at most m−1. Since the homogeneous interpolation problem has a double zero at zero and m−2 other zeros, these are precisely the Hermite value bases. Integrating \(H_i'(u)/u\) gives the weights computed in round 4, by a construction that uses no linear-system solve. The scale identity \(1-\rho_e^2=\eta^2/(4+\eta^2)\ge\eta^2/5\) and the exponent identities \(1/2-5/640=63/128>1/3\), \(1/3-1/4=1/12\) also hold. No defect was found in the earlier structural conclusion.

## 2. A weighted-divergence estimate

Let \(\mu(dz)\propto e^{-S(z)}dz\) on \(\mathbb R^n\), with \(\|D^2S\|_{\rm op}\le M\). Write \(D_i^*=-\partial_i+\partial_iS\), and \(D^*V=\sum_iD_i^*V_i\). Assume Gaussian tails and polynomial growth of the functions and derivatives used. Integration by parts gives
\[
 \|D^*V\|_2^2
 =\mathbb E\sum_{i,j}(\partial_jV_i)(\partial_iV_j)
   +\mathbb E\sum_{i,j}V_i(\partial_{ij}S)V_j
 \le\|DV\|_{F,2}^2+M\|V\|_{F,2}^2.
 \tag{2}
\]
Indeed, start with \(\mathbb E(D^*V)^2=\sum_i\mathbb EV_i\partial_i(D^*V)\), use
\(\partial_iD_j^*V_j=D_j^*\partial_iV_j+(\partial_{ij}S)V_j\), and integrate the first term once more. The cross sum is bounded by \(\sum_{ij}|\partial_jV_i|^2\), by Cauchy–Schwarz. The Hessian term is at most M times the squared vector norm. For tensor-valued V, apply this identity to each uncontracted component and sum. The constant is independent of n. Cutoffs justify the integrations by parts under the stated tails and growth.

For a list I of j labelled derivative slots, Leibniz's rule gives the exact commutation formula
\[
 D_I(D^*V)=D^*(D_IV)+
 \sum_{\varnothing\ne J\subseteq I}
       (D_J DS)_i(D_{I\setminus J}V_i).
 \tag{3}
\]
In each summand only the index i is contracted. If every one-slot unfolding of \(D^vDS\) has operator norm at most \(C_vR^{-(v-1)}\), its action on the corresponding slot of V multiplies the Frobenius norm by this bound. The remaining slots carry identity operators. There is no dimension factor; the number of summands depends only on j.

## 3. Stationary harmonic derivatives with one extra power of R

Fix a probability time rho, and put
\[
 S(w,p)=H_\rho(w)+|p|^2/2,\qquad
 A=\begin{pmatrix}0&-I\\I&0\end{pmatrix},\qquad
 \mathcal L=D^*AD.
\]
Since A is constant and skew symmetric, its second-order contribution vanishes and
\[
 \mathcal L\phi=p\cdot D_w\phi-DH_\rho(w)\cdot D_p\phi.
 \tag{4}
\]
This is the generator of \(\dot W=P,\ \dot P=-DH_\rho(W)\). A bounded Hessian gives a globally Lipschitz vector field and a complete flow. Its ordinary divergence is zero and it preserves S, hence its weighted divergence is zero. The Jacobian change-of-variables formula therefore proves invariance of \(\xi_\rho\otimes N(0,I_d)\).

Suppose \(0<R\le1\), n=2d, the score derivatives obey the one-slot bounds preceding (3), and, for every fixed j≥1,
\[
 |D^j\phi|_F\le C_j a_0\sqrt d\,R^{-(j-1)}.
 \tag{5}
\]
Then, for every fixed k≥1 and j≥0,
\[
 \|D^j\mathcal L^k\phi\|_{F,2}
 \le C_{j,k}a_0\sqrt d\,R^{-(j+2k-1)}.
 \tag{6}
\]
Here and below constants may depend on the fixed derivative orders. To prove (6), let \(\phi_k=\mathcal L^k\phi\) and \(V=A D\phi_{k-1}\). For k=1, (5) gives
\(\|D^hV\|_{F,2}\le C_h a_0\sqrt d R^{-h}\).
For k>1, the induction hypothesis at order h+1 gives the common formula
\[
 \|D^hV\|_{F,2}\le C_{h,k}a_0\sqrt d\,R^{-(h+2k-2)}.
\]
Apply (2) to the main term \(D^*(D^jV)\) in (3). Its two bounds have exponents j+2k−2 and j+2k−1. A commutator with v derivatives on the score has exponent
\[
 (v-1)+(j-v+2k-2)=j+2k-3.
\]
There are no commutators for j=0. Since R≤1, all terms are bounded by the right side of (6). This proves the induction, including k=1; no bound on the value of \(\phi\) is needed. Along a stationary trajectory the kth time derivative is \(\mathcal L^k\phi\) at the current state, so (6) with j=0 bounds its RMS norm uniformly at every fixed time.

The sharper hypothesis (5) is available in the source's two harmonic applications. For \(\phi=T_\rho-\mathrm{id}\), Lemma 5.1 states that every split of its order-j derivative is bounded by \(C_jlR^{-(j-1)}\). Isolating a derivative slot yields a matrix with d input coordinates, so its Frobenius norm is at most \(\sqrt d\) times its operator norm. Thus (5) holds with \(a_0=l\). Proposition 3.2 gives
\[
 |D^jM_\rho|_{\rm split}\le C_jL(\sqrt{1-\rho^2})^{-(j-1)}
 \le C_jLR^{-(j-1)},
\]
so (5) holds with \(a_0=L\). Finally \(DH_\rho=w+r\rho M_\rho\) gives a bounded Hessian, and for v≥2 gives the required score bound \(C_v lR^{-(v-1)}\le C_vR^{-(v-1)}\); the Gaussian momentum adds only an identity Hessian. Regularity and polynomial growth are the source's Gaussian-smoothing hypotheses.

Consequently, with exact stationary harmonic input,
\[
 \left\|\frac{d^m}{dz^m}(T_\rho-\mathrm{id})(W_z)\right\|_2
 \le C_m l\sqrt d\,R^{-(2m-1)},\qquad
 \left\|\frac{d^m}{dz^m}M_\rho(W_z)\right\|_2
 \le C_m L\sqrt d\,R^{-(2m-1)}.
 \tag{7}
\]
The source uses the weaker exponent 2m. The extra factor R in (7) follows from (5); it does not require a stronger jet estimate than the one stated there. Center-dependent constant and linear terms in the potential do not enter (2)–(7), which use score derivatives rather than score magnitude.

## 4. Exact-input angle stencil

Let \(y\sim\xi_*\), and independently \(G\sim N(0,I_d)\). Exact backward probability transport gives \(Y_\rho(y)\sim\xi_\rho\), still independent of G. Start harmonic motion at \((Y_\rho(y),G)\). For \(F(z)=(T_\rho-\mathrm{id})(W_z)\),
\[
 F'(0)=(DT_\rho(Y_\rho)-I)G=(B_\rho-I)G.
\]
Use m≥2 nodes \(z_j=j\psi\), 0≤j≤m−1. Their derivative weights reproduce every polynomial of degree at most m−1 and have absolute sum \(C_m/\psi\). Subtract the Taylor polynomial of F at zero. Its remainder obeys, by (7) and Minkowski's inequality,
\[
 \left\|F(z)-\sum_{k=0}^{m-1}\frac{z^kF^{(k)}(0)}{k!}\right\|_2
 \le\frac1{(m-1)!}\int_0^z(z-v)^{m-1}\|F^{(m)}(v)\|_2\,dv
 \le C_m l\sqrt d\,z^mR^{-(2m-1)}.
\]
Multiplication by the absolute stencil sum proves
\[
 \left\|\sum_jd_jF(j\psi)-(B_\rho-I)G\right\|_2
 \le C_m l\sqrt d\,\psi^{m-1}R^{-(2m-1)}
 =C_m l\sqrt d\,\delta^{2tm-3t}.
 \tag{8}
\]
This is one factor R smaller than Lemma 6.2's \(\delta^{2tm-4t}\). The equality follows from \(4t(m-1)-t(2m-1)=2tm-3t\). The argument uses bounds on the RMS norm at each time, not an expected supremum of a path.

## 5. Harmonic interpolation and computed forward corrections

On a requested angle interval [0,z], with \(0<z\le(m-1)\psi\le1\), interpolate \(Q(v)=M_\rho(W_v)\) at a fixed number m of equally spaced nodes. The Taylor remainder bound from (7) and reproduction of its Taylor polynomial give
\[
 \|Q(v)-\mathcal I Q(v)\|_2
 \le C_m L\sqrt d\,z^mR^{-(2m-1)}.
\]
For the exact harmonic integral equation, the interpolation defect is therefore at most \(C_ml\sqrt d\,\psi^mR^{-(2m-1)}\). Here rL=l, rho≤1, and the extra sine integration factor is at most z²/2≤1 and has been discarded. The harmonic Picard map has contraction factor at most \(C_ml\): indeed, the absolute sine-weight row sums are at most \(C_mz^2\), and \(r\operatorname{Lip}(M_\rho)\le Cl\). For fixed m and sufficiently large dimension this factor is at most 1/2.

Conditional Jensen gives \(\|M_\rho(W_v)\|_2\le CD(x)\) on the stationary marginal. The initial free sine/cosine path thus differs from the exact path by at most \(CrD(x)\). Solving the geometric error recurrence proves, after N≥1 iterations with the exact starting position,
\[
 E_H\le C_ml\sqrt d\,\psi^mR^{-(2m-1)}
                 +(C_ml)^NCrD(x)
 =C_ml\sqrt d\,\delta^{2tm+t}+(C_ml)^NCrD(x).
 \tag{9}
\]
The zero-angle interval has zero defect. The same contraction recurrence for deterministic starting states shows that the computed harmonic map has global Lipschitz constant \(C_m\) jointly in position and momentum.

Retain the source's probability-circuit estimate as an input:
\[
 E_P=B_dl\sqrt d\,h_0^m+(C_ml)^NCrD(x),\qquad
 \operatorname{Lip}(\widehat T)\le C_m,\quad
 \operatorname{Lip}(\widehat T-\mathrm{id})\le C_ml.
 \tag{10}
\]
Use it backward at input y to obtain \(\widehat Y_\rho\). Its RMS error is at most \(E_P\). Transmit this error through the harmonic map with factor \(C_m\); comparison to the exact harmonic state has total error at most \(C_mE_P+E_H\). Evaluate the approximate forward correction at this computed state. By its global Lipschitz constant in (10), this changes the correction by at most \(C_ml(C_mE_P+E_H)\). At the exact harmonic state, whose marginal is \(\xi_\rho\), its own forward approximation error is at most \(E_P\). Hence the complete pre-stencil correction error obeys
\[
 E_C\le E_P+C_ml(C_mE_P+E_H)
 \le B_dl\sqrt d\,(h_0^m+\delta^{2tm+t})
                      +(C'_ml)^NCrD(x).
 \tag{11}
\]
Constants are enlarged to cover the finite geometric factors; N≥1 permits their absorption into \((C'_ml)^N\). This improves the displayed \(\delta^{2tm}\) term in Lemma 6.2 by R, under the stated inputs. It also implies that lemma's original weaker bound. Composing the bounded-Lipschitz backward and harmonic maps with the \(C_ml\)-Lipschitz forward correction proves the asserted joint global Lipschitz bound \(C_ml\) in (y,G).

All comparisons use the same exact stationary path. Approximate states need not be stationary, and no derivative estimate is applied to their laws. No independence between different node errors is used.

## 6. Limits and failure checks

The gain in (6) depends on the spatial exponent j−1 in (5). If only the weaker j exponent is assumed, the same induction yields \(R^{-(j+2k)}\), recovering the source's bound without the extra R. No extra factor R can be obtained by silently changing that base hypothesis. Both hypotheses actually needed in Section 3 are explicit statements in the source, not consequences of the numerical algorithm.

Independence of the initial momentum is essential to the product stationary law. For H(w)=w²/2, take W₀=G₀=Z standard Gaussian. Both marginals are correct, but \(W_z=(\cos z+\sin z)Z\), so \(\mathbb EW_z^2=1+\sin(2z)\), which equals 2 at z=π/4. The source starts with independent y and G, so this is a failure of a weakened hypothesis rather than a counterexample to its lemma.

The stencil has fixed m. Its constants and the threshold making \((m-1)\psi\le1\) need not be uniform when m grows with dimension. Positive r and R are required; no assertion is made at R=0. Large center gradients remain in D(x) only for initial displacements and finite-iteration residuals. The exact-arithmetic script checks the exponent identities independently, tests the leading omitted stencil moment, and checks the stationary operator and weighted-divergence identity for translated quadratic potentials, including large translations and positive and negative perturbations.

Equations (8) and (11) are local analytic refinements. They do not improve a stated final query-complexity rate or certify the endpoint quadrature error, compiler query cap, final-target reduction, or Lean import graph.
