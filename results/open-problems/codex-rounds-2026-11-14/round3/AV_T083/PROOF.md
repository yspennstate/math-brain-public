# The local estimate implies the triple oscillation bound

This is a verification of the transference argument in OpenAI, *Pointwise convergence of triple ergodic averages for mixing transformations* (October 4, 2026), Section “Local forms and the orbit oscillation estimate”. Its local depth-variation theorem is an assumption throughout. No assertion about the correctness of that analytic theorem is made here.

## Statement and assumed estimate

Fix a real compactly supported smooth profile φ of integral one whose moments of orders 1, 2, 3 vanish. Assume its derivatives satisfy the bounds in the paper's Definition “Averaging profiles”. Write

\[
 \varphi_a(t)=a^{-1}\varphi(t/a),\qquad
 b=\varphi_2-\varphi,\qquad
 \Delta_k(t)=2^{-k}b(2^{-k}t).
\]

For a block B of consecutive integers define

\[
 \mathcal V_B(h)(y)=\max_{s\in B}|h_s(y)|
       +\sum_{s,s+1\in B}|h_{s+1}(y)-h_s(y)|.
\]

The analytic assumption is the paper's Theorem “Local estimate with variation in depth”. Precisely, in a finite dyadic tree under a root J, let s(I) be the depth of I and let

\[
 H_I(z_0,z_1,z_2,z_3)=|I|^{-2}
   \int_{\mathbb R^2}w_I(x,t)\prod_{j=0}^3z_j(x+jt)\,dx\,dt.
\]

The kernels are supported where every x+jt lies in I at distance at least |I|/8 from its boundary. They satisfy ∫w_I(v−jt,t)dt=0 for each j and v, and the paper's uniform smooth derivative bounds after rescaling by |I|. For each slot j, its prescribed values at all depths are partitioned into W_j deterministic consecutive blocks, with block variation at most W_j^(-1/2) almost everywhere. The assumption is

\[
 \sum_{I\in\mathcal I}|I|
  |H_I(f_{0,s(I)},f_{1,s(I)},f_{2,s(I)},f_{3,s(I)})|
 \leq C_{\rm loc}|J|.                                      \tag{1}
\]

The constant depends only on the kernel admissibility parameters, not the tree, schedules or block counts.

We prove that (1) implies, on every invertible probability-preserving system and for measurable |f_j|≤1,

\[
 V_k(x)=\sum_{n\in\mathbb Z}\varphi_{2^k}(n)
                   \prod_{j=1}^3f_j(T^{jn}x),
\]

\[
 \sum_{i=1}^w\int_X\max_{k_i\leq\ell\leq k_{i+1}}
            |V_\ell-V_{k_i}|\,d\mu\leq C_\varphi\sqrt w      \tag{2}
\]

for every deterministic list 0≤k_1<⋯<k_{w+1}. Mixing is not needed for this implication.

## Exact kernel normalization

The moments of b through order 3 vanish: its j-th moment is (2^j−1)∫t^jφ(t)dt. Choose B≥1 containing the support of b, and put

\[
 g(t)=\frac16\int_{-\infty}^t(t-v)^3b(v)\,dv.
\]

Then g^(4)=b. For t<−B the integral vanishes; for t>B, expanding (t−v)^3 shows that it also vanishes, by the four zero moments. Thus g is smooth and supported in [−B,B]. Its derivatives through order 3 are bounded integrals over this fixed interval; higher derivatives are derivatives of b. It therefore belongs to the same allowed derivative class, with a larger constant.

Choose a smooth mass-one bump u supported in [−1/8,1/8], in the derivative class specified by the paper, and a dyadic integer D>12B. Define

\[
 F(z,\sigma)=u(z)D^{-3}g(D\sigma),\quad
 L_j=\partial_\sigma-j\partial_z,\quad
 W=L_0L_1L_2L_3F.
\]

All four operators commute. Differentiation preserves support, so on the support of W,

\[
 |z+j\sigma|\leq1/8+3B/D<3/8.
\]

For an interval I with midpoint m and length r=Da, set w_I(x,t)=W((x−m)/r,t/r). This places each coordinate x+jt at distance greater than r/8 from the boundary of I. Let G_j=∏_{i≠j}L_iF. The chain rule gives

\[
 w_I(v-jt,t)=r\frac{d}{dt}G_j((v-jt-m)/r,t/r).
\]

Compact support makes its integral in t zero. Product differentiation and fixed rescaling preserve the required derivative bounds. Finally every term containing a z derivative integrates to zero, while the term with four σ derivatives gives

\[
 \int W(z,\sigma)\,dz=Dg^{(4)}(D\sigma)=Db(D\sigma).
\]

Consequently

\[
 r^{-1}\int W(z,t/r)\,dz=a^{-1}b(t/a).
                                                               \tag{3}
\]

At a=2^k, this is exactly Δ_k. In particular there is no missing factor r or D.

## Averaging translated dyadic lattices

Fix k_-≤k_+ and w blocks of this scale interval. Let h_1,h_2,h_3 and h_{0,k} be supported in a common real interval of length L, with |h_j|≤1 and block variation of h_0 at most w^(-1/2). Put r_k=D2^k and R=r_{k_+}. For 0≤a<R use the single translated dyadic lattice consisting of [a+m2^q,a+(m+1)2^q).

All contributing intervals lie under roots of length R that meet the support interval. These roots have total length at most L+2R. Every progression coordinate on a kernel's support lies in its summation interval, so restricting inputs to the root changes no form. Depth equals k_+−k. Reversing a consecutive block preserves its maximum and the sum of absolute differences. Hence the depth schedule satisfies (1), with W_0=w and W_j=1 for j=1,2,3. Summing (1) over roots bounds the absolute value of the signed sum ∑_k∑_{|I|=r_k}r_kH_I by C_loc(L+2R).

At fixed r=r_k, periodicity in a and r dividing R give

\[
 \begin{split}
 \frac1R\int_0^R\sum_{|I|=r}r^{-1}w_I(x,t)\,da
 &=\frac1r\int_0^r\sum_{m\in\mathbb Z}r^{-1}
   W((x-a-(m+1/2)r)/r,t/r)\,da\\
 &=\frac1r\int_{\mathbb R}W(z,t/r)\,dz=\Delta_k(t).
 \end{split}
\]

The unfolding contributes a factor r from da=−r dz; it cancels one of the two reciprocal factors. Since rH_I is the integral against r^(-1)w_I, averaging the signed sum yields

\[
 \left|\sum_k\int h_{0,k}(x)\prod_{j=1}^3h_j(x+jt)
                        \Delta_k(t)\,dx\,dt\right|
 \leq C_c(L+D2^{k_+}),\qquad C_c=2C_{\rm loc}.                \tag{4}
\]

Only finitely many scales and intervals occur on the bounded supports. All integrands are absolutely integrable. These facts justify unfolding and exchanging the integrals.

## Planting the integer sequences

Assume 0≤k_-≤k_+. Fix e=1/100. For a sequence h supported on the integer interval {q,…,q+L−1}, put its value h(m) on [m−e,m+e), and zero elsewhere. These intervals are disjoint. Common support is contained in a real interval of length L, and all size and block variation bounds persist.

If the four planted inputs have a nonzero product, let p_j be the unique integer center near x+jt. Set m=p_0, n=p_1−p_0, ξ=x−m, η=t−n. Then |ξ|≤e and |η|≤2e. For j=2,3,

\[
 |p_j-(m+jn)|\leq(2j+2)e\leq8e<1.
\]

The quantity is an integer, so it vanishes. Thus there are no extra integer configurations. Conversely the progression lies in its four planted intervals exactly on translates of

\[
 Q_e=\{(\xi,\eta): |\xi+j\eta|\leq e,\ j=0,1,2,3\},
\]

up to boundaries. The middle two coordinates are convex combinations of the endpoint coordinates; hence they add no restriction. The variables u=ξ, v=ξ+3η range independently over [−e,e], and the Jacobian has absolute value 3. It follows that

\[
 A_e:=|Q_e|=4e^2/3,\quad |\eta|\leq2e/3,\quad
 \int_{Q_e}\eta=0,\quad
 A_e^{-1}\int_{Q_e}\eta^2=2e^2/27.                            \tag{5}
\]

For the last equality, (v−u)^2 has mean 2e^2/3 on the square and η=(v−u)/3. Distinct (m,n) give disjoint regions because p_0 and p_1 determine them uniquely. Write c_k(m,n)=h_{0,k}(m)∏_{j=1}^3h_j(m+jn), so |c_k|≤1, and let

\[
 I_k=\sum_{m,n}c_k(m,n)\int_{Q_e}\Delta_k(n+\eta)\,d\xi\,d\eta,
 \qquad D_k=\sum_{m,n}c_k(m,n)\Delta_k(n).
\]

These are exactly the planted continuous integral and the desired discrete sum.

The paper bounds I_k−A_eD_k by a first derivative. Its argument is valid. Symmetry gives a sharper bound: Taylor's theorem and (5) imply

\[
 \left|\int_{Q_e}[\Delta_k(n+\eta)-\Delta_k(n)]\,d\xi\,d\eta\right|
 \leq A_e\frac{e^2}{27}\|b''\|_\infty 2^{-3k},                \tag{6}
\]

because the linear Taylor term integrates to zero and ||Δ_k''||∞=2^(-3k)||b''||∞. A nonzero error requires |n|≤B2^k+2e/3. For k≥0 there are at most

\[
 (2B+4e/3+1)2^k=:C_{B,e}2^k
\]

such integers, and at most L values of m. Thus

\[
 |I_k-A_eD_k|
 \leq A_e\frac{e^2}{27}C_{B,e}\|b''\|_\infty L\,2^{-2k}.     \tag{7}
\]

Summing the geometric series ∑_{k≥0}2^(-2k)=4/3 gives

\[
 A_e^{-1}\left|\sum_{k=k_-}^{k_+} I_k-A_e\sum_{k=k_-}^{k_+}D_k\right|
 \leq E_\varphi L,\qquad
 E_\varphi=\frac{4e^2}{81}C_{B,e}\|b''\|_\infty.              \tag{8}
\]

Combining (4) and (8), one admissible discrete-test constant is

\[
 \left|\sum_kD_k\right|\leq C_d(L+D2^{k_+}),\qquad
 C_d=C_c/A_e+E_\varphi.                                      \tag{9}
\]

The improved error is O(2^(-2k)) per scale, rather than the paper's O(2^(-k)). It is not a uniform numerical improvement over the first-derivative bound for every profile, since it uses ||b''||∞ instead of ||b'||∞. Both bounds suffice for (9).

## Linearizing the oscillation and transferring to orbits

Let h_1,h_2,h_3 be bounded by one and supported in an integer interval K of cardinality L, and let E⊂K. Define

\[
 \mathsf V_k(m)=\sum_n\varphi_{2^k}(n)\prod_{j=1}^3h_j(m+jn).
\]

For m in the testing interval E and each block i, choose the smallest maximizing index ℓ_i(m) in [k_i,k_{i+1}]. Put d_i=𝖵_{ℓ_i}−𝖵_{k_i}, and α_i=conj(d_i)/|d_i| when d_i≠0, zero otherwise. On k_i≤k<k_{i+1}, set h_{0,k}(m)=α_i(m)/(4√w) for m∈E and k<ℓ_i(m), zero otherwise. In each block there is at most one jump. Its maximum plus variation is at most 2/(4√w)≤w^(-1/2), including the empty and full prefix cases. The block endpoints remain deterministic.

Telescoping Δ_k, with the complex phase α_i, makes the sum in (9) exactly

\[
 (4\sqrt w)^{-1}\sum_{m\in E}\sum_{i=1}^w
       \max_{k_i\leq\ell\leq k_{i+1}}
                    |\mathsf V_\ell(m)-\mathsf V_{k_i}(m)|.
\]

It is nonnegative and real. Consequently this oscillation sum is bounded by 4C_d√w(L+D2^{k_{w+1}}).

For the given dynamical system, fix all endpoints first. If supp φ⊂[−B_φ,B_φ], choose Q=ceil(3B_φ2^{k_{w+1}}). For each x and M≥1 plant the finite sequences h_{j,x}(r)=f_j(T^r x) on 1−Q≤r≤M+Q and zero outside. Their common support has cardinality M+2Q. For 1≤m≤M and every scale used, |jn|≤Q for every nonzero summand, so there is no cutoff error and 𝖵_k(m)=V_k(T^m x).

Apply (9) after linearization, integrate in x, and use measure preservation of T^m. The left side is M times the left side of (2), and the right side is

\[
 4C_d\sqrt w\,(M+2Q+D2^{k_{w+1}}).
\]

Divide by M and let M→∞ with endpoints, hence Q, fixed. This proves (2) with C_φ=4C_d. Finite sums and finite maxima are measurable and bounded, so integration is legitimate on an arbitrary probability space. Negative n require the invertibility and measurable inverse assumed in the manuscript.

## What the check leaves open

The transference bridge is valid conditional on (1). The stronger remainder (7) follows independently from exact polygon moments and Taylor's theorem. Neither conclusion proves (1), the depth-dependent analytic estimate. That estimate remains the first unverified input in this chain; this calculation does not establish pointwise convergence for general systems or certify any of the three candidate main theorems.
