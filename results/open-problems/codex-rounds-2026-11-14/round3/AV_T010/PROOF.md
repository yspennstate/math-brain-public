# Bounded potential shifts and retained-port stability

This note verifies the bounded-twist change of law and acceptance-status argument in Section 9 of OpenAI, *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder*, September 23, 2026. It proves the local probability estimate from the definitions below. It does not prove the screening or energy-comparison theorems, the vanishing-energy proposition, or localization.

The source passages are [vanishing.tex, bounded twist](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/vanishing.tex), lines 612–698; [hierarchy.tex, acceptance and stages](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/hierarchy.tex), lines 38–91, 153–158 and 208–218; and [matrix.tex, common-phase closure](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/matrix.tex), lines 118–148. Line numbers refer to the web views opened November 15, 2026; these main-branch sources are mutable.

## 1. A finite product law

Let mu be uniform probability measure on [-h,h], h>0. Let theta be continuously differentiable, vanish at both endpoints, and have bounded derivative. Write

\[
L=\|\theta'\|_\infty,\qquad
J=\int_{-h}^h |\theta'(x)|^2\,d\mu(x),\qquad
T_s(x)=x+s\theta(x).
\]

Assume |s|L<=1/2. If L=0, theta=0 and every conclusion below is immediate. Otherwise, T_s' lies between 1/2 and 3/2. The map is strictly increasing and fixes both endpoints. It is therefore a C1 diffeomorphism of the interval onto itself. The density of (T_s)_*mu relative to mu is

\[
r_s(y)=\frac{1}{1+s\theta'(T_s^{-1}(y))}.
\]

Changing variables y=T_s(x) yields the exact identity

\[
\int r_s(y)^2\,d\mu(y)
=\int\frac{1}{1+s\theta'(x)}\,d\mu(x).
\]

For a=s theta'(x), use

\[
\frac1{1+a}=1-a+\frac{a^2}{1+a}.
\]

The linear term integrates to zero, since

\[
\int\theta'\,d\mu
=\frac{\theta(h)-\theta(-h)}{2h}=0.
\]

Consequently

\[
\boxed{\int r_s^2\,d\mu
=1+s^2\int\frac{|\theta'|^2}{1+s\theta'}\,d\mu
\leq1+2Js^2.} \tag{1}
\]

There is a second direct derivation of the remainder. The same change of variables gives

\[
\int (r_s-1)^2\,d\mu
=\int\frac{s^2|\theta'(x)|^2}{1+s\theta'(x)}\,d\mu(x).
\]

Since integral r_s=1, adding one recovers (1). This also checks the sign and the coefficient without a Taylor approximation.

Now let v be a finite independent mu field, with auxiliary randomness independent of v. Conditional on geometric randomness, choose a set C of at most N_C sites independently of v and transform precisely these coordinates by T_s. Leave all auxiliaries fixed. Let Phi_s denote this map on the whole sample space. Independence gives its joint density

\[
\mathscr D_s(v,\mathrm{aux})=\prod_{x\in C}r_s(v_x),
\qquad
\|\mathscr D_s\|_2^2
\leq(1+2Js^2)^{N_C}
\leq\exp(2JN_Cs^2). \tag{2}
\]

If the same upper bound holds for each geometric choice, averaging over that choice preserves it. It is not necessary to condition on any potential-dependent event.

For every measurable event B, Cauchy–Schwarz therefore gives

\[
\mathbb P\{\Phi_s(v,\mathrm{aux})\in B\}
=\int 1_B\mathscr D_s\,d\mathbb P
\leq D\sqrt{\mathbb P(B)},\qquad
D=\exp(JN_Cs^2). \tag{3}
\]

## 2. The annular scales

Use nested squares of side b_l=3^l. Fix M_0>20, 0<C_0<infinity, and 0<=W<infinity. Choose

\[
e^{b_m^2}\leq L_*<3e^{b_m^2},\qquad
R=L_*/M_0^2,\qquad \tau=C_0/R,
\]

with the torus side b_N much larger than L_*. In a test square D of side L_* and center c, set

\[
C=\{x:M_0R\leq|x-c|_\infty\leq2M_0R\}.
\]

The inner retained region is a union of level-m squares with centers at distance at most R from c. The outer retained region uses those with centers at distance at least L_*/3. The other level-m squares form the gap. Ports of levels n through m-1 have been removed in the gap, and their true potentials restored. A port of level at least m is absent from D on the selector event P that no such selected square meets D.

Because b_m/R<=M_0^2 b_m exp(-b_m^2), this ratio tends to zero. Thus, for all sufficiently large m, every square of level below m meeting C is wholly inside the gap. The inner separation is at least (M_0-1)R-O(b_m). The outer separation is at least

\[
(M_0^2/3-2M_0)R-O(b_m)>0.
\]

Both are bounded below by a positive multiple of R with M_0 fixed. These bounds also apply to retained regions across adjacent test-square boundaries; C is contained strictly inside D, and the distance to its boundary is larger than the distance to the local outer retained region.

For R>=1 and M_0>20, the number of sites in C is at most (4M_0R+1)^2<=25M_0^2R^2. If |s|<=W tau, (2) implies

\[
\|\mathscr D_s\|_2^2
\leq\exp(50JM_0^2C_0^2W^2)=D_W^2. \tag{4}
\]

For sufficiently large m, |s|L<=1/2 also holds. The constants in (4) are independent of m and N. Their dependence on fixed W is harmless. The small-probe restriction also holds eventually, since

\[
\log\tau\leq\log(C_0M_0^2)-b_m^2\leq-c_*b_m.
\]

## 3. Acceptance decisions

For each square U there is a selector eta_U and an acceptance uniform t_U. Eligibility means eta_U=1 and no selected strict ancestor. A square is allowed when its own and all ancestor corner labels are valid. Acceptance is

\[
A_U=1_{\{U\ \mathrm{eligible,allowed}\}}
     1_{\{t_U\leq p_l\mathcal L_U\}}.
\]

The likelihood L_U, port strength, and reference potential depend only on data in U and its own corner boxes. Ancestor labels enter only through validity. During thinning, choices are frozen and removed roots recover their true values. To compare two underlying fields, acceptance is recomputed separately for each field with identical auxiliary variables, and the prescribed thinning is then applied.

Call a tile a candidate if it is eligible and its level and region permit a port after this thinning, irrespective of its acceptance. On P every candidate is disjoint from C: candidates below m meeting C are removed in the gap, and higher selected candidates meeting C are forbidden by P.

For a candidate U disjoint from C, Phi_s leaves its own potentials and own corner labels unchanged. It leaves eta_U, all ancestor selectors, t_U, and its local likelihood, strength, and reference unchanged. Thus the only possible change in A_U comes from a changed ancestor-validity gate. Any ancestor whose gate can change must contain a shifted coordinate and U. By the separation in Section 2 its side is at least cR, for a positive c depending only on M_0. Unchanged invalid ancestor gates need not be excluded: they reject the tile on both fields.

For completeness, the small-box probability used here follows from the box construction. On each of finitely many piece regions, fixed invertible linear coordinates turn the potential domain into a bounded polyhedron. A point in a maximal dyadic cube of width w whose double remains inside that region lies within O(w) of its boundary: otherwise the cube's parent would also have its double inside the region, contradicting maximality. The boundary has finitely many planar faces. Its xi-neighborhood has volume O(xi). The original density and the coordinate Jacobian are bounded. Hence the probability of a triple's box having width less than xi is at most C xi. Null box boundaries have probability zero.

A level-l tile has four such triples. If validity requires all widths to be at least b_l^{-K}, with K>0, a union bound gives probability at most C b_l^{-K} of an invalid tile. In the manuscript K=K_0=10^6. This estimate needs no independence between the four triples or between levels.

Let E_R be the event that some tile meeting C with b_l>=cR has an invalid own label. At level l the number of tiles meeting C is at most C_M0(1+R/b_l)^2, uniformly in the offset and torus size. Therefore

\[
\mathbb P(E_R)\leq u_R
:=C_{M_0}\sum_{b_l\geq cR}(1+R/b_l)^2b_l^{-K}. \tag{5}
\]

To evaluate this tail, let l_R be the first included level. For large R, cR<=b_{l_R}<3cR. For l>=l_R, 1+R/b_l<=1+1/c. The geometric series gives

\[
u_R\leq C_{M_0}(1+1/c)^2
\frac{b_{l_R}^{-K}}{1-3^{-K}}
\leq C'_{M_0,K}R^{-K}. \tag{6}
\]

Alternatively, expand (1+R/b_l)^2. Its three series have exponents K, K+1, and K+2 and prefactors 1, 2R, and R^2; each is O(R^{-K}). This independently checks the power in (6). Truncating at the finite torus level only reduces the bound.

By (3)–(4),

\[
\mathbb P\{\Phi_s(v,\mathrm{aux})\in E_R\}
\leq D_W\sqrt{u_R}.
\]

Outside E_R union Phi_s^{-1}(E_R), every potentially changed ancestor gate of every candidate is valid on both fields. Thus all candidate acceptance decisions agree, both accepted and rejected. Ineligible tiles remain ineligible because selectors are unchanged. Noncandidate ports are removed on both fields. Every retained port, strength, and reference therefore agrees after thinning, with exception probability at most

\[
\boxed{e_R(W)=u_R+D_W\sqrt{u_R}
=O_{M_0,C_0,W,\theta,K}(R^{-K/2}).} \tag{7}
\]

For K=10^6 the exponent in this upper bound is 500000. The constant is not claimed to be practical or uniform in W. No independence of the invalid-gate events was assumed.

## 4. Closure and the trace probability

At a probe site x in C the absorber strength is sigma_x=tau theta(v_x). Closing with common real parameter w=s/tau removes that absorber and adds the real diagonal shift

\[
w\sigma_x=s\theta(v_x).
\]

Thus the closed physical matrix has the true potential T_s(v_x) on C. All retained references and strengths agree with the recomputed hierarchy outside the event in (7). There are no other artificial probes. Consequently the retained scattering matrix and any trace formed from the same retained-port data agree with those of the no-extra-probe intermediate system evaluated at Phi_s(v,aux). This comparison does not require theta(T_s(v_x))=theta(v_x): after closure no annular probes remain.

The phase convention can also be checked directly. Set

\[
z=\frac{s+i\tau}{s-i\tau}=\frac{w+i}{w-i}.
\]

Then z/(1-z)=-(w+i)/(2i). With probe-column matrix Y_C and the open inverse G, Woodbury inversion uses

\[
I+(w+i)Y_C^\top GY_C=\frac{I-zB}{1-z},
\]

because \(B=I+2iY_C^\top GY_C\). Substitution gives the retained response

\[
S_z=A+Tz(I-zB)^{-1}T^\top.
\]

For fixed real s, the transformed potentials have an absolutely continuous law. At fixed energy the determinant of the true finite Hamiltonian minus that energy is a nonzero polynomial in its diagonal variables. Hence it vanishes only on a null set. A singular passive site matrix would have a null vector vanishing at every retained absorber, and restoring true root values leaves its equation unchanged. It would give a null vector for that true Hamiltonian. This proves that the matrix comparison is defined almost surely, even though port choices depend on the field.

Let H^0 be the no-extra-probe intermediate trace, let H_s be the closed trace, and put a=E[1_P |H^0|], assuming a<infinity. Let G_good be any measurable subset of P. The selector event P is unchanged by Phi_s. For delta>0, on the complement of the exception in (7), H_s=H^0 composed with Phi_s. Equations (3)–(4) and Markov's inequality give

\[
\begin{aligned}
\mathbb P\{G_{\rm good},\ |H_s|>\delta\}
&\leq e_R(W)
 +\mathbb P\{\Phi_s(v,\mathrm{aux})\in
            P\cap\{|H^0|>\delta\}\}\\
&\leq e_R(W)+D_W\sqrt{a/\delta}. \tag{8}
\end{aligned}
\]

This proves the bounded-twist probability estimate used in Section 9 from the stated finite hierarchy and thinning definitions. It does not establish that a tends to zero or that the good event required elsewhere has its claimed probability.

## 5. Limits of the result and checks for missing cases

Both signs of s are covered by |s|L<=1/2. Box-boundary null sets remain null after the diffeomorphism. The argument handles arbitrary shared ancestor labels without treating them as independent. It excludes invalid gates before and after the shift, rather than requiring labels to have identical identities. True values at removed gap roots are shifted even when acceptance inside the gap changes. All retained candidates, including rejected candidates, are checked, so creation of a new retained port is excluded as well as destruction of an old one.

Equation (8) holds for each fixed s with |s|<=W tau, with uniform constants. It does not produce one probability-one event for all real s. That stronger statement is unnecessary for integrating a probability estimate in s. The changed set must be chosen independently of the potentials; conditioning first on the potential-dependent good event would invalidate the product-density argument. Endpoint vanishing is also essential: a constant shift of a uniform variable creates mass outside its original support, so an absolutely continuous density relative to the original uniform law need not exist. Finally, the O(R^2) count and O(1/R) shift are exactly compatible; this calculation alone would not give a scale-independent density bound for O(R^3) shifted sites.

The remaining load-bearing inputs are the adaptive first-variation estimate making a small, screening, and the preceding construction of the good event. None is a consequence of (8).
