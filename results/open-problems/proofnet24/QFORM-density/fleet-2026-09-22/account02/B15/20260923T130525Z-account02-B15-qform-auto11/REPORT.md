SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T13:05:25Z.
attacking: independently verify the moving-sheet rough-input closure, then combine it with a new quantitative truncation/compactness obstruction that keeps essential height separate from continuity.

# QFORM account02/B15 — weak trace is not normalized small-ball trace

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Role:** Absolute continuity and regularity; complementary constructions/source-valid counterexamples  
**Status:** `NEW_TARGET_VALID_PROOF_INTERFACE_OBSTRUCTION / RULED_ROUGH_BRIDGE_RECHECKED / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication

The owner target is still the genuinely uniform small-ball/height estimate

\[
\boxed{
\sup_{\substack{A:\,s_3(A)\ge1\\ X_i\text{ independent},\;0\le f_i\le1}}
\sup_{I\subset\mathbb R}\frac{\Pr(X^TAX\in I)}{|I|}<\infty .
}
\tag{1.1}
\]

Equivalently, one needs a universal essential `L^infinity` bound for the output density. This run does not prove (1.1) and does not give a QFORM counterexample.

The new result instead closes a subtle regularity/limit question relevant to every proposed rough-input reduction:

> **Theorem A (target-valid optimality of weak trace).** There are smooth compactly supported cap-one product inputs for the fixed target matrix `A=I_3`, and a subsequence converging weakly to another cap-one product input, such that the quadratic-output laws converge uniformly on **all unnormalized interval masses**, but their densities do not converge in `L^1` or `L^infinity`; moreover the **normalized shrinking-interval profiles fail to converge by an explicit positive amount**. Every output density in the sequence and the limit is continuous, compactly supported and bounded by `1/2`.

Thus the latest completed account03/B15 trace theorem is essentially optimal for weak convergence: a common bound `mu_m(I)<=C|I|` passes to the limit exactly, but weak convergence plus atomlessness/continuity/common height cannot manufacture such a bound by convergence of normalized profiles or densities.

This is a proof-interface obstruction inside the exact target, not a failure of the conjecture.

## 2. Completed sources actually used

### 2.1 Latest designated partner result

The latest compatible account03/B15 result is

`yspennstate/math-open-problems@be22adf9f67e9fa02063418c000bc5ee2d2d0c43`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T122734Z-account03-B15-qform-auto18/REPORT.md`.

It proves, among other things:

1. If probability laws `mu_m=>mu` weakly on `R` and `mu` is atomless, then

\[
d_K(\mu_m,\mu)=\sup_t|F_m(t)-F(t)|\to0
\tag{2.1}
\]

and hence

\[
\sup_{a\le b}|\mu_m((a,b])-\mu((a,b])|\le2d_K(\mu_m,\mu)\to0.
\tag{2.2}
\]

2. Fixed-dimensional cap-one product laws are weakly closed. If their marginals converge weakly and the coefficients of a nonconstant quadratic polynomial converge, then the output laws converge weakly to an atomless law.

3. Therefore a **common** estimate

\[
\mu_m(I)\le C|I|\qquad\text{for all intervals }I
\tag{2.3}
\]

passes to the limit with exactly the same `C`, without using continuity of any output representative.

4. The same zero-loss closure holds for moving sheet submeasures

\[
\sigma_m(B)=\Pr(r_m(X_m)\ge0,\ q_m(X_m)\in B)
\tag{2.4}
\]

when `q_m,r_m` converge locally uniformly and the limiting product law assigns zero mass to `{r=0}`.

The partner explicitly warns that (2.2) is **unnormalized** and does not imply convergence after division by shrinking interval length. Theorem A below shows this warning is sharp inside the exact QFORM class.

### 2.2 Partner phase-aligned family

I also apply the completed account03/B15 construction

`yspennstate/math-open-problems@a5094ce57d028af28c2c114f92ca26ac277d4cec`.

For every `s>=2`, it constructs a probability density

\[
f_s\in C_c^\infty((1,10)),\qquad 0\le f_s\le1,
\tag{2.5}
\]

such that, for three iid coordinates with this density and

\[
Q_s=X_{s,1}^2+X_{s,2}^2+X_{s,3}^2,
\qquad A=I_3,
\tag{2.6}
\]

the output density satisfies

\[
p_s\in C_c^\infty((3,300)),\qquad
\|p_s\|_\infty\le\frac12,
\tag{2.7}
\]

while its Fourier transform has the phase-aligned spike

\[
\boxed{|\widehat p_s(s)|\ge\frac{27}{64}.}
\tag{2.8}
\]

This fixed matrix has exactly three eigenvalues of magnitude one, so (2.5)-(2.8) lie completely inside the owner target.

### 2.3 Required newest Claude result

The required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

contains the ruled one-sheet theorem for signature `(+, +, -)`. I independently recheck its coarea constant and rough-input passage in Sections 6-7 and apply it to the positive tent inequality (7.5).

No pointwise stationary-phase decay, post-rotation independence, arbitrary-joint rank-three coarea bound, conditional projection-moment bound, bounded support assumption for the owner theorem, or generic X-ray bound on the two-sheet side is used.

## 3. Compactness of the source family and the limiting target law

Take any sequence `s_m->infinity`, for example positive integers. Each source law in (2.5) is supported in the fixed compact interval `[1,10]`. Hence there is a subsequence, still denoted `s_m`, whose one-dimensional laws converge weakly:

\[
\mu_{s_m}\Rightarrow\mu.
\tag{3.1}
\]

The cap-one class is weakly closed. Indeed, for every nonnegative `phi in C_c(R)`,

\[
\int\phi\,d\mu
 =\lim_m\int\phi f_{s_m}\,dx
 \le\int\phi\,dx.
\tag{3.2}
\]

Therefore `mu=f dx` for a probability density `0<=f<=1`, and `mu` is still supported in `[1,10]`.

Finite products preserve weak convergence, so

\[
\mu_{s_m}^{\otimes3}\Rightarrow\mu^{\otimes3}.
\tag{3.3}
\]

The map

\[
q(x_1,x_2,x_3)=x_1^2+x_2^2+x_3^2
\tag{3.4}
\]

is continuous. Thus the output laws

\[
\rho_m:=q_\#\mu_{s_m}^{\otimes3}
\Rightarrow
\rho:=q_\#\mu^{\otimes3}.
\tag{3.5}
\]

The limit law is absolutely continuous. Here this can be seen directly, without any general coarea theorem: because `X>=1`, the density of `X^2` is

\[
h(u)=\frac{f(\sqrt u)}{2\sqrt u}\,\mathbf 1_{[1,100]}(u),
\tag{3.6}
\]

so

\[
0\le h\le\frac12,\qquad \|h\|_1=1.
\tag{3.7}
\]

Hence

\[
p=h*h*h
\tag{3.8}
\]

is a density for `rho`, supported in `[3,300]`, and

\[
\boxed{\|p\|_\infty\le\frac12.}
\tag{3.9}
\]

Moreover `p` is continuous. Indeed translation continuity in `L^1` gives

\[
\|\tau_t(h*h)-h*h\|_\infty
 \le \|\tau_t h-h\|_1\,\|h\|_\infty\to0,
\tag{3.10}
\]

and convolving once more with `h` preserves continuity and compact support. Thus the limiting output is in `C_c`, not merely atomless.

Now apply the latest partner theorem to (3.5):

\[
\boxed{
\sup_{a\le b}|\rho_m((a,b])-\rho((a,b])|\to0.
}
\tag{3.11}
\]

This is the strongest all-center/all-width **unnormalized** trace statement available from weak convergence alone.

## 4. Density convergence nevertheless fails strongly

All `p_m:=p_{s_m}` and `p` are supported in `[3,300]`. By (2.8),

\[
|\widehat p_m(s_m)|\ge\frac{27}{64}.
\tag{4.1}
\]

Since `p in L^1`, the Riemann-Lebesgue lemma gives

\[
\widehat p(s_m)\to0.
\tag{4.2}
\]

Therefore

\[
\begin{aligned}
\liminf_m\|p_m-p\|_1
&\ge
\liminf_m|\widehat{p_m-p}(s_m)|\\
&\ge\frac{27}{64}.
\end{aligned}
\tag{4.3}
\]

In total-variation language,

\[
\boxed{
\liminf_m d_{TV}(\rho_m,\rho)\ge\frac{27}{128}.
}
\tag{4.4}
\]

Thus the output laws converge in Kolmogorov distance by (3.11) while staying a fixed positive distance apart in total variation.

Because the difference is supported on an interval of length `297`,

\[
\|p_m-p\|_1\le297\|p_m-p\|_\infty.
\tag{4.5}
\]

Combining (4.3)-(4.5),

\[
\boxed{
\liminf_m\|p_m-p\|_\infty
\ge\frac{27}{64\cdot297}
=\frac{27}{19008}
>1.42\times10^{-3}.
}
\tag{4.6}
\]

This occurs although every `p_m` is smooth, `p` is continuous, all are supported in the same compact interval, and every one has height at most `1/2`. Hence neither continuity nor a common height bound upgrades weak source convergence to density convergence.

## 5. Normalized shrinking-interval profiles fail to converge

The preceding statement can be put exactly in the owner-relevant small-ball language.

For `r>0` define the normalized box

\[
\beta_r(x)=\frac{1}{2r}\mathbf 1_{[-r,r]}(x).
\tag{5.1}
\]

Its Fourier transform is

\[
\widehat\beta_r(\xi)=\frac{\sin(r\xi)}{r\xi}.
\tag{5.2}
\]

Choose

\[
r_m=\frac{\pi}{2s_m}.
\tag{5.3}
\]

Then

\[
\widehat\beta_{r_m}(s_m)=\frac2\pi.
\tag{5.4}
\]

Put

\[
D_m=(p_m-p)*\beta_{r_m}.
\tag{5.5}
\]

Pointwise,

\[
D_m(y)=
\frac{\rho_m([y-r_m,y+r_m])-\rho([y-r_m,y+r_m])}{2r_m}.
\tag{5.6}
\]

Endpoints are irrelevant because both laws are absolutely continuous. From (4.1), (4.2), and (5.4),

\[
\liminf_m |\widehat D_m(s_m)|
\ge\frac2\pi\frac{27}{64}.
\tag{5.7}
\]

Since `||D_m||_1>=|hat D_m(s_m)|` and the support of `D_m` has length at most `297+2r_m`,

\[
\|D_m\|_\infty
\ge
\frac{|\widehat D_m(s_m)|}{297+2r_m}.
\tag{5.8}
\]

Letting `m->infinity` gives the explicit target-level obstruction

\[
\boxed{
\liminf_m\sup_y
\left|
\frac{\rho_m([y-r_m,y+r_m])-\rho([y-r_m,y+r_m])}{2r_m}
\right|
\ge
\frac{27}{9504\pi}
>9.04\times10^{-4}.
}
\tag{5.9}
\]

Yet (3.11) says the corresponding **unnormalized** interval-mass differences converge uniformly to zero. Thus division by a width that tends to zero fundamentally changes the limiting statement.

This proves that the latest partner trace theorem cannot be strengthened, even in the fixed diagonal target `I_3`, to

\[
\sup_{I}\frac{|\rho_m(I)-\rho(I)|}{|I|}\to0.
\tag{5.10}
\]

In fact (5.9) already refutes (5.10) when the supremum is restricted to the single widths `|I|=\pi/s_m`.

### Consequence for rough-input proofs

There are two valid but distinct rough-limit mechanisms:

* If one has already proved a common interval estimate `rho_m(I)<=C|I|`, partner Theorem 3.1 passes it to the weak limit with **zero loss**.
* If one wants convergence of densities themselves, or wants to infer the common interval estimate by taking a smooth limit, weak convergence plus continuity/common height is insufficient. One needs a stronger source topology together with a quantitative output-stability estimate, or a direct small-ball domination before the limit.

This distinction is exactly the difference between essential boundedness and continuity that B15 is assigned to preserve.

## 6. Independent check of the ruled coarea constant

I now recheck the required newest-Claude ruled theorem rather than importing its geometry blindly.

Consider

\[
q(y)=\lambda_1y_1^2+\lambda_2y_2^2-\mu y_3^2,
\qquad \lambda_1,\lambda_2,\mu>0.
\tag{6.1}
\]

After the linear scaling

\[
z=(\sqrt{\lambda_1}y_1,\sqrt{\lambda_2}y_2,\sqrt\mu\,y_3),
\tag{6.2}
\]

the level `q=s>0` becomes

\[
z_1^2+z_2^2-z_3^2=s.
\tag{6.3}
\]

Write

\[
e_\theta=(\cos\theta,\sin\theta,0),
\qquad
e_\theta^\perp=(-\sin\theta,\cos\theta,0).
\tag{6.4}
\]

A ruling is

\[
F(\theta,t)=\sqrt s\,e_\theta+t(e_\theta^\perp+e_3).
\tag{6.5}
\]

In the orthonormal basis `(e_theta,e_theta^perp,e_3)`,

\[
F_\theta=(-t,\sqrt s,0),\qquad F_t=(0,1,1).
\tag{6.6}
\]

Thus

\[
F_\theta\times F_t=(\sqrt s,t,-t)
=\frac12\nabla(z_1^2+z_2^2-z_3^2)(F).
\tag{6.7}
\]

Therefore the exact coarea quotient is

\[
\frac{d\sigma}{|\nabla q_0|}=\frac12\,d\theta\,dt.
\tag{6.8}
\]

Undoing (6.2) multiplies `delta(q-s)dy` by

\[
(\lambda_1\lambda_2\mu)^{-1/2}.
\tag{6.9}
\]

The ruling direction in the original `y` coordinates is

\[
v_\theta=
\left(-\frac{\sin\theta}{\sqrt{\lambda_1}},
\frac{\cos\theta}{\sqrt{\lambda_2}},
\frac1{\sqrt\mu}\right),
\tag{6.10}
\]

so

\[
|v_\theta|^2=
\frac{\sin^2\theta}{\lambda_1}
+\frac{\cos^2\theta}{\lambda_2}
+\frac1\mu.
\tag{6.11}
\]

The parameter `t` is not arclength. If `rho` is the three-dimensional spectral projection density, then the line integral in `dt` equals `1/|v_theta|` times the arclength X-ray. For a smooth product source, the latter is the value of a two-dimensional projection density, and the completed product-projection theorem used by the Claude source bounds it by `2`. Consequently

\[
\begin{aligned}
p_q(s)
&\le
(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}\frac{d\theta}{|v_\theta|}\\
&=:C_+(\lambda_1,\lambda_2,\mu).
\end{aligned}
\tag{6.12}
\]

This is exactly the source constant. In particular, if

\[
\kappa=\min(\lambda_1,\lambda_2,\mu),
\tag{6.13}
\]

then the completed source estimate gives

\[
\boxed{C_+\le\pi\sqrt2/\kappa.}
\tag{6.14}
\]

For exact rank three with the three target eigenvalue magnitudes at least one, this is `<=pi sqrt(2)` on the majority one-sheet side.

The check above also confirms the two constant-sensitive points that are easy to lose: the coarea factor is exactly `1/2`, and the ruling parameter contributes the factor `1/|v_theta|` because it is not arclength.

## 7. Rough-input ruled bridge, without continuity

The smooth proof must be transferred to arbitrary measurable cap-one marginals without evaluating an essential-supremum projection representative on a distinguished curve.

Let `F=prod_i f_i` be the original-coordinate product density and let

\[
f_i^{(\eta)}=f_i*\gamma_\eta.
\tag{7.1}
\]

Gaussian convolution preserves probability, independence and the cap `<=1`, and

\[
\|f_i^{(\eta)}-f_i\|_1\to0.
\tag{7.2}
\]

In fixed dimension, telescoping gives

\[
\left\|\prod_i f_i^{(\eta)}-\prod_i f_i\right\|_1
\le\sum_i\|f_i^{(\eta)}-f_i\|_1\to0.
\tag{7.3}
\]

For the fixed homogeneous rank-three form, let `G={q>=0}` denote the majority side and define the submeasures

\[
\sigma_\eta(B)=\Pr_\eta(G,\ q\in B),
\qquad
\sigma(B)=\Pr(G,\ q\in B).
\tag{7.4}
\]

Restriction to a measurable event and deterministic pushforward cannot increase total variation. Hence (7.3) implies `sigma_eta->sigma` in total variation. The smooth ruled theorem gives `sigma_eta(I)<=C_+|I|`; passing to the limit gives

\[
\boxed{\sigma(I)\le C_+|I|\quad\text{for every interval }I.}
\tag{7.5}
\]

No output continuity is involved.

A concrete positive-kernel consequence is obtained by integrating the triangular kernel:

\[
\begin{aligned}
\mathbb E[(\varepsilon-|q-y|)_+\mathbf 1_G]
&\le C_+\int_{-\varepsilon}^{\varepsilon}(\varepsilon-|u|)\,du\\
&=C_+\varepsilon^2.
\end{aligned}
\tag{7.6}
\]

Thus the required newest-Claude result has been applied to an actual owner-scale inequality, not merely cited.

### Ambient physical triple and moving critical value

If, after conditioning on all outside original coordinates `W=w`, an invertible physical `3x3` block `B` has signature `(2,1)`, then

\[
Q_w(x)=x^TBx+2d(w)^Tx+c_0(w)
=(x+B^{-1}d(w))^TB(x+B^{-1}d(w))+c(w).
\tag{7.7}
\]

This is a translation in the **original** independent coordinates. It preserves the cap-one product law and uses no independence after spectral rotation. The conditional majority-side estimate (7.5) is uniform in the affine translation; averaging over `W` preserves it.

If the coefficients, source laws, and therefore the critical sheet move along an approximation, the latest account03/B15 moving-sheet theorem applies. The sheet equation is a nonzero polynomial in the original variables, so the limiting absolutely continuous product law assigns its boundary zero mass. Therefore a common one-sheet density cap passes to the limit with no loss.

This independently verifies the newest continuation's ruled/rough-input bridge at its exact scope.

## 8. What remains unpaid

The implication ledger is now especially sharp.

**Absolute continuity.** For every nonconstant quadratic polynomial and every absolutely continuous input law, the pushforward is absolutely continuous by local coarea away from the proper affine critical space. This is qualitative and carries no universal height.

**Essential boundedness.** A common interval domination `P(Q in I)<=C|I|` is exactly the needed quantitative statement. The latest partner trace theorem passes such a bound through weak rough/coefficient limits once it has been proved uniformly. Theorem A proves that weak convergence cannot itself create the normalized estimate: even smooth compact target-valid approximants with continuous bounded limit density may oscillate at shrinking scales as in (5.9).

**Continuity.** The special family in Theorem A has smooth approximants and a continuous bounded limit, yet the densities remain separated in `L^1` and `L^infinity`. Therefore continuity, even together with compact support and a common height, must not be used as a substitute for the owner small-ball bound. This run does not change the shared status of the full `QFORM-CONTINUOUS-REPRESENTATIVE` claim.

**Ruled signature branch.** For an exact `(+, +, -)` rank-three form the majority one-sheet submeasure is directly paid by (7.5)-(7.6). The first unpaid local implication is still the minority/two-sheet contribution. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction rules out replacing product provenance by a generic X-ray norm. In higher-rank/no-pivot configurations, the remaining structural job is to route the form into one of the paid volume/grouped-coordinate branches before paying reciprocal local degeneracies.

So the global first unpaid implication remains (1.1). The new obstruction says precisely what a future smooth/compact reduction is allowed to do: prove a **uniform interval inequality before taking the limit**, then invoke zero-loss trace closure. It is not allowed to argue that weak convergence plus continuity makes normalized small-ball profiles or densities converge.

## 9. Correction discipline and scope

The argument preserves every owner quantifier relevant to its claims. The new obstruction itself uses a fixed target matrix `A=I_3`, smooth compactly supported independent cap-one marginals, and no extra moments or log-concavity. It is therefore source-valid and stronger than an abstract measure-theory warning.

The ruled bridge is transferred by smoothing in original coordinates; no post-rotation independence is introduced. The one-sheet result is not extended to the two-sheet side. No arbitrary-joint coarea height bound is invoked. The full universal theorem remains OPEN.
