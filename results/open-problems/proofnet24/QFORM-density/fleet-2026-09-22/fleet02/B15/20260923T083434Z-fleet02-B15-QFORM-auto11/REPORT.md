SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-23T08:34:34Z.
attacking: the first unpaid rough-input implication after the ruled one-sheet theorem: pay Gaussian heat modes on the ruled side, isolate exactly what remains at the critical/two-sheet side, and audit the rough-input passage without using continuity to obtain height.

# fleet02/B15 — ruled-side heat-mode payment, rough-law audit, and a posterior endpoint obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** absolute continuity and regularity; complementary constructions/source-valid counterexamples  
**Run:** `20260923T083434Z-fleet02-B15-QFORM-auto11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW_MODE-SIDE_INEQUALITY / NEW_INTERFACE_COUNTEREXAMPLE / FULL_TARGET_OPEN`

The unrestricted conjecture remains **OPEN**. This report does not infer a universal height from continuity. It proves absolute continuity directly, independently checks the rough-input passage for the completed ruled theorem, composes that theorem with the newest fleet03/B15 Gaussian-mode result to pay every heat mode lying a positive normalized distance into the ruled side, and gives two obstructions showing why the critical/minority side is genuinely still needed.

## 1. First unpaid implication

The newest compatible partner result, fleet03/B15 at

`math-open-problems@30e0239b97649cbaa02bd11bd3bd5a5bd514b5f0`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260923T073059Z-fleet03-B15-qform-auto15/REPORT.md`,

reduces the scale-invariant optimal height to Gaussian heat modes. If

\[
H_\varepsilon(y)=\mathbb E\,\gamma_\varepsilon(Q-y),
\qquad
\gamma_\varepsilon(u)=\frac{1}{\sqrt{2\pi}\varepsilon}e^{-u^2/(2\varepsilon^2)},
\]

and `y_*` is a global maximizer of `H_epsilon`, the Gaussian posterior

\[
d\nu_*(z)=\frac{\gamma_\varepsilon(z-y_*)}{H_\varepsilon(y_*)}\,d\mu_Q(z),
\qquad U=\frac{Z-y_*}{\varepsilon},
\]

satisfies the exact global constraint

\[
\boxed{\mathbb E_{\nu_*}e^{vU}\le e^{v^2/2}\quad(v\in\mathbb R).}
\tag{1.1}
\]

The same partner report proves equivalence, up to factor `3 sqrt(3)/sqrt(2 pi)<2.073`, between the full height problem and a fixed-radius small-ball estimate at such heat modes.

The first unpaid implication in the exact rank-three indefinite branch can therefore be stated without any continuity premise:

> **Given an exact rank-three target of signature `(2,1)` (or `(1,2)`), bound the Gaussian heat height at a global heat mode on or on the two-sheet/minority side of the critical value, using original-product provenance.**

Section 4 below pays every mode a positive normalized distance into the ruled/majority side. Sections 5-6 show that neither the posterior condition (1.1) nor a one-sided density cap can remove the remaining two-sheet obligation.

## 2. Completed ruled theorem and independent constant check

The specified source

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`,

proves the one-sheet theorem for

\[
q(y)=\lambda_1y_1^2+\lambda_2y_2^2-\mu y_3^2,
\qquad \lambda_1,\lambda_2,\mu>0.
\]

On the side `s>=0`,

\[
\boxed{
 p_q(s)\le C_+(\lambda_1,\lambda_2,\mu)
 :=(\lambda_1\lambda_2\mu)^{-1/2}
 \int_0^{2\pi}
 \frac{d\theta}{\sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}}.
}
\tag{2.1}
\]

If

\[
\kappa=\min(\lambda_1,\lambda_2,\mu),
\]

then

\[
\boxed{C_+\le \pi\sqrt2/\kappa.}
\tag{2.2}
\]

I rechecked the delicate geometric constant. After scaling the quadratic form to `u_1^2+u_2^2-u_3^2`, the ruled parametrization at level `s>=0` is

\[
F(\theta,t)=\sqrt s\,e_\theta+t(e_\theta^\perp+e_3).
\]

The coarea measure contributes exactly one half of `dtheta dt`, together with the spectral determinant factor `(lambda_1 lambda_2 mu)^(-1/2)`. The parameter `t` is not arclength. In the original spectral variables its direction has norm

\[
|v_\theta|=
\sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}.
\]

The line integral of the three-dimensional projected density along that ruling equals `1/|v_theta|` times the corresponding two-dimensional projection density. The latter is at most `2` for a product source with coordinate density caps one. The factor two cancels the coarea one-half, giving (2.1). Finally

\[
|v_\theta|^2\ge
\frac{\sin^2\theta+\cos^2\theta+1}{\max(\lambda_1,\lambda_2,\mu)}
\]

is not the useful estimate; instead, directly writing `a=lambda_1`, `b=lambda_2`, `c=mu` and using `a,b,c>=kappa`,

\[
(abc)^{-1/2}|v_\theta|^{-1}
=
\frac{1}{\sqrt{bc\sin^2\theta+ac\cos^2\theta+ab}}
\le \frac{1}{\sqrt2\,\kappa},
\]

because each of `bc`, `ac`, `ab` is at least `kappa^2` and `sin^2+cos^2=1`. Integrating over `2pi` gives (2.2).

This is an **essential-density** theorem for the ruled submeasure. It is not a continuity theorem.

## 3. Rough-input bridge: no continuity is needed

The ruled derivation is easiest for smoothed marginals, so the rough passage must be justified rather than hidden inside an output-continuity assertion.

Consider first three independent original coordinates with cap-one densities `f_1,f_2,f_3`. Let

\[
f_i^{(\eta)}=f_i*\gamma_\eta.
\]

Then each `f_i^(eta)` is a probability density, remains bounded by one, and

\[
\|f_i^{(\eta)}-f_i\|_1\to0.
\]

For the product laws,

\[
\left\|\prod_{i=1}^3f_i^{(\eta)}-\prod_{i=1}^3f_i\right\|_1
\le \sum_{i=1}^3\|f_i^{(\eta)}-f_i\|_1
=:\delta_\eta\to0.
\tag{3.1}
\]

A deterministic measurable pushforward contracts total variation. Hence for every fixed quadratic-plus-affine map `T`,

\[
\|T_\#P_\eta-T_\#P\|_{TV}\le \tfrac12\delta_\eta.
\tag{3.2}
\]

If `c` is the critical value, restriction to the majority half-line is also a contraction. Thus, writing

\[
\nu_\eta(B)=P_\eta(T\in B,\ T\ge c),
\qquad
\nu(B)=P(T\in B,\ T\ge c),
\]

we have `||nu_eta-nu||_TV ->0`. For every interval `I`, the smooth ruled estimate gives

\[
\nu_\eta(I)\le C_+|I|.
\]

Passing to the limit in total variation gives

\[
\boxed{\nu(I)\le C_+|I|\quad\text{for every interval }I.}
\tag{3.3}
\]

Therefore `nu` is absolutely continuous with essential density at most `C_+`. No continuity of the rough output was invoked.

The same argument works after conditioning on arbitrary outside **original** coordinates around an invertible physical `3x3` block `B`. Given outside value `w`, completing the square translates the active three original coordinates; translations preserve independence, the cap, and the `L^1` error in (3.1). The error is independent of `w`. Thus the conditional majority submeasure obeys the same interval inequality with the eigenvalue constant of `B`, and averaging in `w` preserves it. This proves the rough ambient majority-side submeasure estimate at exactly the scope claimed by the completed ruled theorem. It does **not** make the random conditional critical value into one global heat-mode threshold; that distinction matters in Section 4.

At the cone vertex itself there is no atom: the zero set of a nonzero quadratic polynomial has Lebesgue measure zero, and the product law is absolutely continuous. Hence no endpoint mass is lost in passing from the smooth to rough majority restriction.

## 4. New theorem: heat modes on the ruled side are quantitatively paid

Now specialize to a whole exact rank-three indefinite quadratic law, so there is one deterministic critical value `c` (for the homogeneous target `c=0`; affine completion merely translates it). Let the multiplicity-two sign be called the majority sign and write the form after sign choice as in Section 2. Let

\[
H(y)=\mathbb E\gamma_\varepsilon(Q-y),
\]

and let `y_*` be a global heat mode. Suppose it lies on the ruled side and define its normalized distance from the critical value by

\[
d=\frac{y_*-c}{\varepsilon}>0.
\tag{4.1}
\]

Let `nu_*` be the partner Gaussian posterior and put

\[
\alpha=\nu_*(Q\ge c)=P_{\nu_*}(U\ge-d).
\]

Let `mu_+` be the majority-side submeasure of `Q`. By (2.2)-(3.3), its density is at most `C_+`. Gaussian convolution is an `L^infinity` contraction, so

\[
H_+(y_*):=\int_{[c,\infty)}\gamma_\varepsilon(z-y_*)\,d\mu_Q(z)
\le C_+.
\tag{4.2}
\]

But by definition of the posterior,

\[
H_+(y_*)=\alpha H(y_*).
\tag{4.3}
\]

The partner subgaussian theorem (1.1) gives the Chernoff bound

\[
P_{\nu_*}(U<-d)\le e^{-d^2/2},
\]

so

\[
\alpha\ge1-e^{-d^2/2}.
\tag{4.4}
\]

Combining (4.2)-(4.4) with (2.2) yields the first new inequality:

\[
\boxed{
\kappa H(y_*)
\le
\frac{\pi\sqrt2}{1-e^{-d^2/2}}
\qquad(d>0).
}
\tag{4.5}
\]

This pays all heat modes a fixed normalized distance into the ruled side.

There is a better near-critical estimate than the quadratic loss implicit in (4.4). Because the posterior is centered,

\[
EU=0.
\]

On the minority event `{U<-d}`,

\[
E[-U;U<-d]\ge d(1-\alpha).
\]

Since `EU_+=E(-U)_+`, for any `T>0`,

\[
\begin{aligned}
d(1-\alpha)
&\le EU_+\\
&=\int_0^\infty P(U>t)dt\\
&\le \alpha T+\int_T^\infty e^{-t^2/2}dt\\
&\le \alpha T+\frac{e^{-T^2/2}}{T}.
\end{aligned}
\tag{4.6}
\]

For `0<d<=e^{-2}`, set

\[
T=\sqrt{2\log(1/d)}\ge2.
\]

Then `e^{-T^2/2}=d`, and rearrangement gives

\[
\alpha\ge
\frac{d(1-1/T)}{T+d}
\ge\frac{d}{3T}.
\tag{4.7}
\]

Therefore

\[
\boxed{
\kappa H(y_*)
\le
\frac{6\pi\sqrt{\log(1/d)}}{d},
\qquad 0<d\le e^{-2}.
}
\tag{4.8}
\]

Thus the ruled theorem plus the newest partner theorem reduce the exact-rank-three indefinite mode problem to `d<=0` and the limiting endpoint `d downarrow 0`. The remaining singularity in (4.8) is not an artifact that can be removed from (1.1) alone; Section 6 proves that precisely.

Important scope point: in an ambient matrix conditioned on outside coordinates, the completed physical block has a **random** critical value `c(W)`. A global mode of the averaged output need not be a heat mode of each conditional law. Therefore (4.5)-(4.8) are asserted for a whole exact-rank-three affine-completed law with one deterministic critical value, not automatically for the averaged ambient three-block branch. Section 3's essential-density estimate does pass through that averaging.

## 5. Source-valid target obstruction: heat modes can lie arbitrarily deep on the two-sheet side

The Gaussian-mode reduction cannot hope to prove that target modes automatically live on the ruled side. This fails already for a diagonal exact target.

Take

\[
A=\operatorname{diag}(1,1,-1),
\]

and independent cap-one inputs

\[
X_1,X_2\sim\operatorname{Unif}[0,1],
\qquad
X_3\sim\operatorname{Unif}[M,M+1].
\]

Then

\[
Q=X_1^2+X_2^2-X_3^2
\]

is a valid exact target with all three eigenvalue magnitudes equal to one, but

\[
\operatorname{supp}Q\subset[-(M+1)^2,\ 2-M^2].
\tag{5.1}
\]

For `M>sqrt(2)`, the whole output support is on the minority/two-sheet side of the critical value zero.

For any compactly supported finite positive measure `mu`, a Gaussian convolution

\[
h(y)=\int\gamma_1(y-z)d\mu(z)
\]

cannot have a global maximum outside the convex hull of the support: if `y<inf supp(mu)`, then

\[
h'(y)=\int(z-y)\gamma_1(y-z)d\mu(z)>0,
\]

and if `y>sup supp(mu)`, the derivative is negative. Hence every global heat mode `y_*` for the law in (5.1) satisfies

\[
y_*\le2-M^2<0.
\tag{5.2}
\]

As `M to infinity`, the normalized distance of every unit-scale heat mode into the two-sheet side tends to infinity. This is a **source-valid target family**, not a counterexample to QFORM: the diagonal density theorem already controls it. Its purpose is structural. It proves that the newest mode reduction cannot remove the two-sheet branch by a universal mode-location argument.

## 6. New abstract endpoint obstruction: posterior subgaussianity plus a majority cap does not control heat height

The preceding target family shows minority modes occur. The next construction isolates an even sharper obstruction at the critical interface: the exact partner posterior condition (1.1), absolute continuity, compact support, and an arbitrarily small majority-side density cap still do not control the heat height.

Fix `0<p<=1/4` and set

\[
a_p=\frac{3p}{4(1-p)}.
\]

Define a probability density `rho_p` by placing mass `1-p` uniformly on

\[
[-3a_p/2,-a_p/2]
\]

and mass `p` uniformly on

\[
[1/2,1].
\]

Explicitly,

\[
\rho_p(u)=
\frac{1-p}{a_p}\mathbf1_{[-3a_p/2,-a_p/2]}(u)
+2p\mathbf1_{[1/2,1]}(u).
\tag{6.1}
\]

Its mean is exactly zero, because the two contributions are

\[
-(1-p)a_p=-3p/4,
\qquad
2p\int_{1/2}^1u\,du=3p/4.
\]

Its support lies in an interval of diameter

\[
1+3a_p/2\le11/8<2.
\]

Hoeffding's lemma for a centered random variable supported in an interval of length `L` gives

\[
E e^{vU}\le e^{v^2L^2/8}\le e^{v^2/2}.
\tag{6.2}
\]

Thus the probability law `nu_p(du)=rho_p(u)du` satisfies exactly the partner mode posterior constraint.

Let `gamma=gamma_1` and define

\[
M_p=\int\frac{1}{\gamma(u)}d\nu_p(u),
\qquad
m_p(u)=\frac{\rho_p(u)}{M_p\gamma(u)}.
\tag{6.3}
\]

Then `m_p` is an absolutely continuous compactly supported probability density. Let `mu_p(du)=m_p(u)du`. Its Gaussian heat value at zero is

\[
H_p(0)=\int\gamma(u)m_p(u)du=\frac1{M_p}.
\tag{6.4}
\]

Moreover the Gaussian posterior at zero is exactly `nu_p`:

\[
\frac{\gamma(u)m_p(u)}{H_p(0)}du=\rho_p(u)du.
\tag{6.5}
\]

By the partner equivalence between global heat modes and the posterior bound (1.1), (6.2) and (6.5) imply that **zero is a global Gaussian heat mode** of `mu_p`.

On the positive half-line the density of `mu_p` is supported on `[1/2,1]`, and because `gamma` decreases there,

\[
C_p:=\|m_p\mathbf1_{[0,\infty)}\|_\infty
=\frac{2p}{M_p\gamma(1)}.
\tag{6.6}
\]

Combining (6.4) and (6.6) gives the exact ratio

\[
\boxed{
\frac{H_p(0)}{C_p}=\frac{\gamma(1)}{2p}\longrightarrow\infty.
}
\tag{6.7}
\]

Also `nu_p=>delta_0` as `p downarrow0` and all supports stay in a common compact interval, so

\[
M_p\to1/\gamma(0),
\qquad H_p(0)\to\gamma(0)=1/\sqrt{2\pi}.
\tag{6.8}
\]

Therefore there is no universal implication of the form

\[
\text{global Gaussian heat mode + exact 1-subgaussian posterior + majority-side density cap }C
\Longrightarrow H(y_*)\le K C.
\]

This construction is **not** claimed to be a quadratic-form output and does not refute QFORM. It refutes only a proposed interface: at the critical/minority endpoint, the one-sheet bound and the newest posterior self-consistency condition are insufficient without further product-provenance-sensitive geometry. This is fully compatible with the live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE`.

## 7. Absolute continuity is paid independently of height and continuity

For completeness, the exact target law is always absolutely continuous, and this fact uses neither rank-three smoothing nor any bounded-density theorem.

Let

\[
q(x)=x^TAx,
\qquad F(x)=\prod_i f_i(x_i).
\]

For every Lebesgue-null `N subset R`, apply the coarea formula on a ball `B_R` to the locally Lipschitz map `q`:

\[
\int_{q^{-1}(N)\cap B_R}F(x)|\nabla q(x)|dx
=
\int_N\left(\int_{q^{-1}(t)\cap B_R}F\,d\mathcal H^{n-1}\right)dt
=0.
\tag{7.1}
\]

Here

\[
\nabla q(x)=2Ax.
\]

Because the target has rank at least three, `A` is nonzero and its critical set `ker A` is a proper linear subspace, hence Lebesgue-null. The input law is absolutely continuous, so it assigns zero mass to `ker A`. From (7.1), outside `ker A` the integrand can vanish only on an `F dx`-null subset. Letting `R to infinity`,

\[
P(q(X)\in N)=0.
\]

Thus

\[
\boxed{q_\#(Fdx)\ll dx.}
\tag{7.2}
\]

This proves absolute continuity under the full target hypotheses. It says nothing quantitative about the essential supremum.

## 8. Exact logical regularity ledger

The properties must not be conflated.

1. **Having an essentially bounded density implies absolute continuity** by definition.
2. **Having a continuous density implies absolute continuity** by definition.
3. **Absolute continuity does not imply essential boundedness.** If `X` is uniform on `[0,1]`, then `X^2` has density `1/(2sqrt(t))` on `(0,1)`.
4. **Essential boundedness does not imply a continuous representative.** The uniform law on `[0,1]` has bounded density but no continuous representative equal to it almost everywhere.
5. **Continuity does not imply boundedness on the whole line.** Let disjoint triangular spikes be centered at the positive integers, with height `n` and half-width `w_n=2^{-n}/n`; the total area is `sum_n n w_n=1`, the resulting density is continuous, and its values at the integers tend to infinity.

For the actual target, (7.2) establishes absolute continuity. The universal essential-height statement is the central conjecture and remains open. The canonical live claim state also tracks the full continuous-representative conclusion separately. Scoped Fourier-integrable branches can yield `C_0` after their height has already been paid; the ruled theorem in Sections 2-3 yields an essential-density bound for a positive submeasure and makes no continuity claim. No step in this report uses continuity to infer an `L^infinity` bound.

## 9. What changed and what remains

The specified `e5f71d...` completed result was applied to the real inequality (4.5), not merely cited. The newest compatible fleet03/B15 mode theorem was then used to sharpen the near-critical ruled-side estimate to (4.8). The new source-valid diagonal family (5.1) proves that global heat modes can lie arbitrarily deep on the unpaid two-sheet side. The new abstract construction (6.1)-(6.8) proves that even the exact posterior subgaussian self-consistency cannot combine with a majority-side density cap to pay the critical endpoint in the absence of additional structure.

So the first unpaid implication is now more precise:

\[
\boxed{
\text{control the Gaussian heat mode on the minority/two-sheet side, or at the critical endpoint,}
}
\]

using original-coordinate product provenance. A generic X-ray norm is known insufficient. For higher-rank ambient matrices, one must additionally join this curved branch to the live volume/high-leverage/near-null structural alternatives without assuming a uniformly conditioned physical triple.

No hidden moment, support, log-concavity, diagonal-basis, or post-rotation independence assumption was used.

## 10. Source and correction ledger


Completed sources actually used:

- `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md` — ruled one-sheet density bound.
- `math-open-problems@30e0239b97649cbaa02bd11bd3bd5a5bd514b5f0`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260923T073059Z-fleet03-B15-qform-auto15/REPORT.md` — Gaussian-mode posterior subgaussian theorem and fixed-radius mode-centered compiler.

Relevant corrections consumed include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`, and especially `QFORM-TWOSHEET-XRAY-ONLY-FALSE`. None is used as a positive premise.

Independent-review status: this report is a worker derivation/supporting result, not an end-to-end proof of QFORM. The full target remains open.
