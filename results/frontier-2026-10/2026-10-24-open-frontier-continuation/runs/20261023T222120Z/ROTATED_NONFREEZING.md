# T384: later kernel motion for two rotated orthogonal inputs

**PROVED (internal): independently reviewed by c03; see reviews/c03_root_review.md.** Fix 0<alpha<2 and inputs x1=(1,1)/sqrt(2), x2=(1,-1)/sqrt(2). Use iid standard symmetric alpha-stable hidden coordinates and output weights, no biases, output normalization (m log m)^(-1/alpha), learning rate (log m)^(2/alpha), both layers trained on half the squared error, and the absorbing ReLU solution. Take the fixed label vector y=0. There exist fixed 0<delta<T=2 and eta,p>0 such that

liminf P(sup_{delta<=t<=2} ||H_m(t)-H_m(delta)||op > eta) >= p.

Thus the scaled kernel can move by order one at macroscopic positive times after the initial switching layer. This refutes the straightforward extension of the coordinate-input constant-effective-kernel theorem to arbitrary orthogonal rotations. It does not identify the complete rotated-input limiting dynamics.

## 1. Initialization and positive-probability event

Write V_i1=(U_i1+U_i2)/sqrt(2), V_i2=(U_i1-U_i2)/sqrt(2). Set a_m=m^(1/alpha), L_m=(log m)^(1/alpha), beta_m=L_m/a_m, and

C_m=m^(-2/alpha) sum_i V_i+ V_i+^T,

A_j,m=m^(-2/alpha) sum_i W_i^2 1{W_i>0,V_ij>0},

P_m=C_m+diag(A_1,m,A_2,m).

The initialization lemma proved separately in agents/c01.md gives joint convergence of the initial residual r_m(0), C_m and A_m. The C limit is

C=(1/2)[[S0+S1,S0],[S0,S0+S2]],

where the three S variables are independent positive alpha/2-stable with Laplace exponent c_alpha Gamma(1-alpha/2)s^(alpha/2). The initial output is F=(Z0+Z1,Z0+Z2)/sqrt(2), with independent symmetric alpha-stable Z variables having characteristic exponent c_alpha |t|^alpha. F,C and the output-weight marked Poisson process are mutually independent. The positive-W marked sums A have positive probability in every neighborhood of (.5,.5): the three nonzero gate-pattern clouds give A=(T10+T11,T01+T11), with independent positive stable T variables. All four gate patterns have probability 1/4 by symmetry and exchangeability of U1,U2.

Consequently any sufficiently small fixed neighborhood of

r0=(1,3), C0=[[1.5,1],[1,1.5]], A0=(.5,.5)

has positive limiting probability. Fix this neighborhood now so both initial residual components exceed 3/4, A_1,m>.4, ||P_m||op<4, and the constant-P_m integral Jbar_1(2)<-.18, as justified by the center calculation in Section 3. Only after fixing this neighborhood choose K, then delta, then h. Let S_m=m^(-2/alpha)sum_i(W_i^2+U_i1^2+U_i2^2). S_m is tight. Choose K sufficiently large that intersection with S_m<=K retains positive liminf probability p0. Let E_m be this intersection. Choose R bounding ||r_m(0)|| on the neighborhood. No independence of S_m from the other variables is assumed.

## 2. Uniform small coordinate motion, frozen C, and early sign selection

The orthogonal transformation preserves Euclidean hidden energy. The exact equations in V coordinates are

V_ij'=beta_m W_i r_j 1{V_ij>0}, W_i'=beta_m sum_j r_j(V_ij)_+,

r'=-H_m r, H_m=diag(H1_1,m,H1_2,m)+C_m(t).

Absorption makes every reached zero coordinate stay zero. The star-matrix energy estimate of the prior coordinate proof does not require independence of the V coordinates. On E_m and for t<=2 it gives ||r(t)||<=R, ||H_m(t)||op<=2K for large m,

sup_t ||C_m(t)-C_m(0)||op=o(1),

sup_t m^(-2/alpha)sum_i |W_i(t)^2-W_i(0)^2|=o(1),

max_i sup_t |W_i(t)-W_i(0)|/a_m=O_K,R(beta_m)=o(1).

For completeness, set G_i=W_i^2+V_i1^2+V_i2^2. Along each active segment, |G_i′|<=2 beta_m R G_i, hence G_i(t)<=exp(2 beta_m R t)G_i(0). Absorption is continuous and does not increase G_i. Integrating the coordinate derivatives gives ||(W_i,V_i)(t)-(W_i,V_i)(0)||<=O_R(beta_m)sqrt(G_i(0)) uniformly through time 2. The bound ||aa^T-bb^T||op<=(||a||+||b||)||a-b||, and its scalar square analogue, give the normalized sum bounds at rate O_R(beta_m)S_m. Also ||H_m(t)||op<=m^(-2/alpha)sum_i G_i(t)<=2K eventually. Since max_i sqrt(G_i(0))/a_m<=sqrt(K), the individual W bound follows. Residual contraction follows from r′=-H_m r and positive semidefiniteness. These estimates need no independence of the V coordinates.

All these bounds are deterministic on E_m, uniform in the initialization there. In particular every |W_i(0)|>=epsilon a_m keeps its sign for any fixed epsilon>0 and large m.

Choose delta>0 so small that 2KR delta<1/4. On E_m, both initial residuals exceed 3/4 by the already fixed neighborhood, hence both remain >=1/2 through delta. Any initially active negative-W extreme surviving to delta requires V_ij(0)>=c epsilon delta L_m. Since W_i and V_ij(0) are independent and V_ij is alpha-stable, the probability that any such extreme exists is O_epsilon,delta(1/log m). Positive-W extremes with initially active gates remain active through delta. The normalized small-W mass

Z_m,epsilon=m^(-2/alpha)sum_i W_i(0)^2 1{|W_i(0)|<epsilon a_m}

satisfies E Z_m,epsilon<=C epsilon^(2-alpha). Send m to infinity, then epsilon to zero. The moved-weight bound yields

P(E_m intersect {||H_m(delta)-P_m||op>h}) ->0 for every h>0.                 (1)

## 3. A constant post-layer kernel predicts a forbidden negative integrated residual

At the center of the initialization event, P0=[[2,1],[1,2]]. Its constant-kernel residual is

rbar_1(t)=2 exp(-3t)-exp(-t), rbar_2(t)=2 exp(-3t)+exp(-t).

Its first integrated component is

Jbar_1(t)=-(1/3)+exp(-t)-(2/3)exp(-3t),

so Jbar_1(2)<-0.19. By continuity, the neighborhood fixed in Section 1 can and does ensure that the analogous Jbar_1(2), computed from P_m and r_m(0), is below -0.18 throughout E_m. Also A_1,m>=0.4 there and ||P_m||op<=4.

For h>0 let B_m(h)={sup_{delta<=t<=2}||H_m(t)-P_m||op<=h}. Variation of constants against constant P_m, using positive semidefinite contraction and ||r(t)||<=R, gives

sup_{t<=2} ||r(t)-exp(-P_m t)r(0)|| <= R[(2K+4)delta+2h].

Thus the integrated residual J_1,m(2)=int_0^2 r_1(t)dt differs from its constant-P_m counterpart by at most 2R[(2K+4)delta+2h]. Decrease delta and then fix h>0 so that this is less than .08. On E_m intersect B_m(h),

J_1,m(2)<-.10.                                                       (2)

## 4. Surviving gates contradict that prediction

An initially active positive-W extreme which remains active through time 2 satisfies exactly

V_i1(2)=V_i1(0)+beta_m W_i(0)J_1,m(2)+beta_m int_0^2 (W_i(t)-W_i(0))r_1(t)dt.

After division by L_m, the last term is bounded uniformly by O_K,R(beta_m), since beta_m/L_m=1/a_m and max_i sup_t |W_i(t)-W_i(0)|/a_m=O(beta_m). If W_i(0)>=epsilon a_m, (2) and positivity of V_i1(2) therefore require V_i1(0)>=.05 epsilon L_m for large m. The probability that any such extreme exists is again O_epsilon(1/log m). Negative-W extremes were already absorbed by delta, except on the small-probability event from Section 2. Initially inactive gates never activate under the stipulated flow.

It follows that for every q>0,

P(E_m intersect B_m(h) intersect {H1_1,m(2)>q}) ->0.                    (3)

To justify (3) without bounding rare extreme magnitudes by expectation, remove the large survivors by the probability bounds, bound all remaining normalized initial squares by Z_m,epsilon, and use the uniform moved-square bound. Markov gives limsup error probability <=C epsilon^(2-alpha)/q; then epsilon decreases to zero.

But C_m(t) freezes uniformly, and B_m(h) implies H1_1,m(2)>=A_1,m-h-o(1)>=.4-h-o(1). Choose h<.1. Equation (3) is incompatible with this inequality. Hence P(E_m intersect B_m(h))->0.

Finally (1) shows that sup_{delta<=t<=2}||H_m(t)-H_m(delta)||<=h/2 would imply B_m(h), apart from an event of vanishing probability on E_m. Therefore the theorem holds with eta=h/2 and any p<=liminf P(E_m).

## 5. What this proves and does not prove

PROVED (internal), with the separate initialization lemma and independent review completed: positive-probability macroscopic kernel variation for two rotated orthogonal inputs, beyond a fixed positive time delta. The fixed scalar/coordinate laws from the prior package are not contradicted.

The exact constant-phase cumulative residual crosses zero at t*=log(1+sqrt(3)); its instantaneous residual crosses earlier. This distinguishes cumulative gate motion from instantaneous residual sign. A proposed two-phase limiting system removes A1 at t*, with second matrix [[1.5,1],[1,2]], but this note does not prove convergence of the full finite-width path to that hybrid system or identify a random switching-time law. Those are the next unpaid steps.

The result uses the explicit absorbing solution. Discrete steps, smooth activations, arbitrary nonorthogonal geometry and deep networks remain open. External priority is not established. Primary model source: Favaro–Fortini–Peluchetti, TMLR 11/2024, https://iris.unibocconi.it/retrieve/1d4101f5-ffcd-480d-8966-6c0f01de8f2b/2651_Large_width_asymptotics_a.pdf; its second-layer freezing does not imply first-layer freezing.
