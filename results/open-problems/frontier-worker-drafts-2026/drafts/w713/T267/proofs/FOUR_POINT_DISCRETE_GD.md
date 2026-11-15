# A restricted nonlinear discrete-GD double-descent construction

Status: proof draft, unaudited; novelty not established. This construction uses a zero-initialized readout, a stratified four-point design, a linear single-index teacher, and risk averaged over training-label noise. It does not settle Target 1 under fully random readout initialization or generic i.i.d. Gaussian sampling. These restrictions are part of the statement, not details to discard in reporting.

## 1. Model and claim

For 0<e<1/4 and s,t in {-1,1}, define

x_(s,t)=(1,e s,e^2 t)/sqrt(1+e^2+e^4).

The test-input distribution is uniform on these four points. The training design contains each point once (n=4). The noiseless teacher is

g(x_(s,t))=(s+t)/4=u_e^T x_(s,t),

where u_e=(0,sqrt(1+e^2+e^4)/(4e),sqrt(1+e^2+e^4)/(4e^2)). Thus this is a single-index teacher with a linear link; it is not a nonlinear ReLU teacher. Each training label is g(x_i)+xi_i, where the four xi_i are independent, equal to plus or minus 1/2 with equal probability. In particular |y_i|<=1 and ||y||_2<=2.

Train f_m(x)=m^(-1/2) sum_j a_j ReLU(w_j^T x) by full-batch GD on ||f_m(X)-y||_2^2/(2n), with step eta=1/2. Initialize w_j independently N(0,I_3) and a_j=0. Both layers are updated at every step using ReLU derivative 1_{z>0}. No first-layer freezing is imposed.

Let Q_(m,e)(k) be the clean population squared risk at integer step k, averaged over the sixteen equally likely training-noise vectors, conditional on hidden-weight initialization. The model uses an independent fresh test input; its input support is entirely covered by the stratified training design. Adding independent mean-zero test-label noise changes Q only by its constant variance.

For each sufficiently small fixed e, as m tends to infinity the probability that Q_(m,e) has strict witnesses

Q(k0)>Q(k1)<Q(k2)>Q(k3), with k0<k1<k2<k3,

tends to one. Explicit witnesses and an explicit finite-width error bound are given below. This proves two separated decreases and an intervening increase in this restricted expected-noise risk. It does not assert monotonicity throughout each intervening interval or uniqueness of all extrema.

A central local maximum can be localized in an iterated width/scale limit: with rates b1(e),b2(e) defined below, its step k_peak satisfies

b1 k_peak-log(b1/b2) -> 0

when width tends to infinity first and e tends to zero second, in the precise sense in Section 6. Since b1~e^2/4 and b2~e^4/4, its leading scale is 8 e^(-2) log(1/e) steps. This is an asymptotic localization, not an explicit finite-width equality.

## 2. The exact limiting kernel and its eigenvalues

At zero readout, the initial training tangent kernel is the random-feature Gram matrix divided by n. Its limit is K_e with entries k(x_i^T x_j)/4, where

k(r)=[sqrt(1-r^2)+(pi-arccos(r))r]/(2pi), -1<=r<=1.

This Gaussian ReLU covariance formula is also K2 in Heckel–Yilmaz arXiv:2007.10099v2, Section 3, equations (7) and the ensuing kernel display, pp.9–10. Only this formula is used from that source; their one-sided risk bound is not used to prove non-monotonicity.

Write a=e^2/(1+e^2+e^4), c=e^4/(1+e^2+e^4), and

A=k(1), B=k(1-2a), C=k(1-2c), D=k(1-2a-2c).

In the Walsh basis 1,s,t,st, orthonormal for the uniform input law, the eigenvalues of K_e are

lambda0=(A+B+C+D)/4,

lambda1=(A-B+C-D)/4,

lambda2=(A+B-C-D)/4,

lambda12=(A-B-C+D)/4.

All are positive for e>0 sufficiently small. The first three follow from positivity and monotonicity of k on the relevant interval. For lambda12, use strict monotonicity of k'(r)=(pi-arccos(r))/(2pi) and

4lambda12=integral_(1-2c)^1 [k'(r)-k'(r-2a)]dr>0.

No derivative at r=1 is taken beyond the continuous first derivative. This identity also gives lambda12=o(c), since k' tends uniformly to 1/2 on the shrinking range. Likewise the two length-2a differences in lambda1, and the two length-2c differences in lambda2, give

lambda0 -> 1/2, lambda1~e^2/2, lambda2~e^4/2, lambda12=o(e^4).

The trace is 1/2, and K_e is positive semidefinite by its covariance representation. Therefore 0<eta lambda_h<1 for every mode. Set q_h=1-eta lambda_h and b_h=-log(q_h)>0. Then b1~e^2/4, b2~e^4/4, b12/b2->0, and b0->-log(3/4)>0.

## 3. Expected risk of the limiting discrete iteration

The limiting prediction iteration is fbar_(k+1)=fbar_k-eta K_e(fbar_k-y), fbar_0=0. The teacher coefficients in modes 1 and 2 are 1/4 and those in modes 0 and 12 are zero. Each Walsh coefficient of label noise has mean zero and variance v=(1/2)^2/4=1/16. Noise Walsh coefficients need not be independent: Parseval eliminates cross terms between modes, so only their individual second moments are needed.

The exact expected clean risk is

Q_e(k)=v[(1-q0^k)^2+q1^(2k)+(1-q1^k)^2+q2^(2k)+(1-q2^k)^2+(1-q12^k)^2].

For real nonnegative z define Q_e(z) by the same expression with q_h^z=exp(-b_h z). This interpolation is used only to analyze the limiting curve; the actual algorithm remains discrete GD.

Choose

k0=ceil(e^(-1)),

k1=floor(log(2)/b1),

k2=ceil(e^(-3)),

k3=floor(log(2)/b2).

For sufficiently small e these are increasing. The mode asymptotics above give

Q_e(k0)/v -> 3,

Q_e(k1)/v -> 5/2,

Q_e(k2)/v -> 3,

Q_e(k3)/v -> 5/2.

For example, b1 k1->log(2), b2 k1->0, b12 k1->0, and b0 k1->infinity; the other three limits follow by substituting their clocks. Integer rounding errors vanish because b1,b2,b12 tend to zero and b0 k_i tends to infinity. Thus there is e0>0 such that every 0<e<e0 has all three strict limiting witness margins greater than v/4.

These limits supply actual positive lower margins, not a non-monotone upper envelope.

## 4. Finite-width nonlinear discrete-GD comparison

This argument avoids a differentiability assumption on ReLU. Let X contain the four input rows, L=2, S=6, Y=2 and n=4; ||X||op<=L. Put S_m=(1/m)sum_j||w_j(0)||^2. Work on S_m<=S.

The following deterministic recurrences depend only on the finite horizon, not on m or the particular label-noise vector:

A_0=D_0=0, B_0=1,

R_k=Y+L S A_k B_k,

c_k=eta L R_k/n,

A_(k+1)=A_k+c_k B_k,

D_(k+1)=D_k+c_k A_k,

B_(k+1)=1+D_(k+1).

Let p_j(k)=sqrt(m)|a_j(k)| and r_j=||w_j(0)||. Induction using the exact GD updates gives

p_j(k)<=A_k r_j,

||w_j(k)-w_j(0)||<=D_k r_j/m,

||w_j(k)||<=(1+D_k/m)r_j<=B_k r_j,

||f_m(X;k)-y||<=R_k.

Indeed ||ReLU(Xw)||<=L||w||, the update of sqrt(m)a_j has norm at most c_k||w_j||, and the weight update has norm at most c_k p_j/m. Finally ||f_m(X;k)||<=L S A_k B_k. These inequalities remain valid when a gate crosses zero because only ReLU's global Lipschitz property and |1_{z>0}|<=1 are used.

Write h_j(k)=ReLU(Xw_j(k)), and K_m=(1/(n m))sum_j h_j(0)h_j(0)^T. With U_k=(L^2 S/n)(2D_k+D_k^2),

||(1/(n m))sum_j h_j(k)h_j(k)^T-K_m||op<=U_k/m.

This follows by adding/subtracting h_j(0) in the product and using ||h_j(k)-h_j(0)||<=L D_k r_j/m.

Let b_j(k)=sqrt(m)a_j(k). The exact prediction update, including movement of the first-layer features, is

f_m(k+1)=f_m(k)-eta K_RF(k)(f_m(k)-y)+E_k,

E_k=(1/m)sum_j b_j(k+1)[h_j(k+1)-h_j(k)].

The same bounds give ||E_k||<=L c_k A_k A_(k+1) S/m. This is the term that would be lost by incorrectly treating the network as a fixed-feature model.

On the additional event ||K_m-K_e||op<=m^(-1/4), ||K_m||op<=3/2, so ||I-eta K_m||op<=1. Define

Z_0=0,

Z_(k+1)=Z_k+eta U_k R_k+L c_k A_k A_(k+1) S.

Subtracting the frozen-K_m prediction iteration and inducting proves a training prediction error at most Z_k/m. Subtracting the frozen-K_e iteration adds at most eta k Y m^(-1/4), since ||I-eta K_e||op<=1 and its residual norm is at most Y. Therefore, uniformly over the sixteen label-noise vectors and k<=T,

||f_m(X;k)-fbar(X;k)||_2<=E_T(m):=Z_T/m+eta T Y m^(-1/4).

All population inputs are the four training-design inputs. Since ||fbar(X;k)-g(X)||<=4, the difference between the actual and limiting clean risks is at most

J_T(m)=2E_T(m)+E_T(m)^2/4.

Averaging over label noise preserves this error bound. No independence of the nonlinear trajectory and initialization is assumed.

The event has an explicit probability lower bound. Gaussian norm moments give P(S_m>6)<=2/(3m). Each entry of K_m has variance at most 3/(16m): use Cauchy-Schwarz and E[(w^T x)^4]=3 for unit inputs. If all sixteen entry errors are at most m^(-1/4)/4 then the operator error is at most m^(-1/4). Chebyshev and a union bound give failure probability at most 48/sqrt(m). Thus both events hold with probability at least 1-2/(3m)-48/sqrt(m). A negative lower bound for small m makes no assertion; the theorem is for sufficiently large m.

For fixed e and T=k3, the recurrences produce finite constants and J_T(m)->0. Choosing m with J_T(m)<v/8 transfers every limiting witness margin greater than v/4 to a strict actual margin. This proves Section 1's restricted finite-width statement. It is an explicit sufficient width criterion, though the recurrence constants may be extremely large and no practical width is claimed.

## 5. Limiting central peak time

Put B=log(b1/b2), which tends to infinity. At z=(B+s)/b1, uniformly for s in any fixed compact interval,

Q_e'(z)/(2v b2) -> exp(-s)-1,

Q_e''(z)/(2v b1 b2) -> -exp(-s).

To check this directly, differentiate the six terms in Section 3. The fast signal/noise term, divided by b2, is exp(-s)-2(b2/b1)exp(-2s). The slow signal/noise term tends to -1, since (b2/b1)(B+s)->0. The constant-mode term and its derivative are exponentially smaller than either scale. The interaction-noise term is O[(b12/b2)^2(b2/b1)(B+|s|)] and its normalized derivative also vanishes. All these bounds are uniform on the fixed compact interval.

Hence, for sufficiently small e, there is a unique interpolated critical point in s in [-1,1], it is a strict maximum, and its coordinate s_e tends to zero. This gives z_peak=(log(b1/b2)+o(1))/b1. The same differentiation near b1 z=log(2) and b2 z=log(2) gives a limiting first and second local minimum, respectively; neither is needed to infer the four finite witness inequalities.

## 6. What peak localization means for finite-width discrete GD

Let I_e be the integer interval with endpoints floor((B-1)/b1) and ceil((B+1)/b1), and let k_peak,m maximize Q_(m,e) on that interval. For fixed small e, its limiting interpolated curve is strictly increasing before its central maximum and decreasing after it throughout this interval, by Section 5 (enlarging the compact s interval slightly covers rounded endpoints). Consequently every maximizing integer of Q_e on I_e is within one step of z_peak, and both endpoints have strictly smaller values than some interior integer.

Couple widths using prefixes of one infinite i.i.d. Gaussian hidden-weight sequence. The strong law applied to its squared norms and the sixteen kernel entries, together with the deterministic finite-horizon error recurrences above, gives Q_(m,e)->Q_e uniformly on this finite integer interval almost surely. For this almost-sure argument, replace m^(-1/4) in E_T by the actual operator error ||K_m-K_e||, which tends to zero; the Chebyshev failure bound is not summable and is not used as an almost-sure rate. For large m every k_peak,m is an interior local maximum and its distance from the set of maximizing integers of Q_e tends to zero. Therefore

limsup_(m->infinity)|b1 k_peak,m-B|<=|s_e|+b1

almost surely for each fixed small e. Taking e to zero gives the iterated localization in Section 1. For an almost-sure statement simultaneously along decreasing scales, take any fixed countable sequence e_l->0 and intersect the corresponding probability-one events. No uncountable intersection is claimed.

## 7. Scope and remaining Target 1 work

This is a finite-support, stratified-design theorem for expected risk over independent training noise. The network is a two-layer ReLU network and both layers are updated by discrete GD; the first-layer-motion error is explicitly retained. The teacher is single-index but linear. The readout is initialized at zero. These are substantive restrictions. The construction does not give generic i.i.d. sampling, a centered-ReLU teacher, fully random readout initialization, high probability over label noise, or a sharp practical width threshold. Its risk mechanism is inherited from separated random-feature modes; it does not demonstrate macroscopic feature learning. Independent review must assess both the proof and whether this restricted model counts toward the dossier's intended target. No full target or novelty claim is made.
