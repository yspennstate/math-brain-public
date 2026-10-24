# Independent audit of the uniform-time RF logistic-GD proof

**Conclusion, 2026-10-24.** The proof in fullproof/b02_uniform_time_GD.md passes this independent audit. I found no substantive mathematical gap in its coercivity, deletion-robust curvature, finite MLE, common contraction, all-time coefficient delocalization, positive-norm bound, or use of the deterministic TV transfer theorem. The scope is exactly its explicitly stated sufficiently large fixed sample-to-width ratio and sufficiently small fixed positive step. This audit does not enlarge those quantifiers.

The fixed-horizon deterministic-overlap input required by its Section 9 is supplied by the independently checked B01/B03 route. The RF matrix and AMP applicability details are audited in fullproof/b05_RF_universality_audit.md, including the source-level spectral comparison and the state-covariance positive-definiteness addendum.

## 1. Constants and noisy-label coercivity

All arguments condition first on the feature-only event
\[
\|F\|_{\rm op}\le L,\qquad
\Sigma_F\succeq sI,\qquad
\Sigma_F-g_Fg_F^\top\succeq sI.
\]
The Hermite proof of this event is valid. In particular, the offdiagonal remainder satisfies
\[
\mathbb E\|E\|_F^2
\le \frac{15m(m-1)}{d(d+2)(d+4)}=O(d^{-1}),
\]
while the diagonal nonlinear residual converges uniformly to \(\nu>0\). Subtracting the teacher covariance removes only
\(D_AF\theta\theta^\top F^\top D_A\) from the positive linear-Hermite part. Thus both lower covariance bounds follow on the same feature-only event.

For every unit \(u\), \(f_u(X)=u^\top\tanh(FX)\) is centered and \(L\)-Lipschitz. Gaussian Poincaré twice gives
\[
\mathbb E f_u^2\ge s,\qquad
\mathbb E f_u^4
\le(\mathbb E f_u^2)^2+4L^2\mathbb E f_u^2
\le5L^4.
\]
The proposed \(\kappa=\sqrt{s/2}\) and \(p_0=s^2/(20L^4)\) therefore satisfy the uniform small-ball inequality. The tail cutoff
\(B=\sqrt{2\log(4/p_0)}\) gives
\(\Pr(|Z|>B)\le p_0/2\).

The signed inequality correctly accounts for dependence between the teacher and feature vector. Conditional on each complete \(X\) with \(|Z|\le B\), the label opposing the sign of \(f_u(X)\) has probability at least
\(q_\beta=\sigma(-\beta B)>0\). Consequently
\[
\Pr(-(2Y-1)f_u(X)\ge\kappa)\ge q_\beta p_0/2=p_1.
\]
No independence between \(Z\) and \(f_u(X)\) is required.

The cutoff class has Lipschitz constant \(2/\kappa\), range \([0,1]\), and vanishes at zero. Symmetrization and the absolute-value contraction inequality give the bound
\[
\mathbb E\sup_u |(P_n-P)f_u|
\le \frac{8L}{\kappa}\sqrt{\frac mn}.
\]
The numerical constant eight is conservative. For the signed class, the Rademacher second moment uses
\((2Y_i-1)^2=1\); it never assumes label-feature independence. The same estimate applies directly to the scalar cutoff \(x\mapsto\psi(|x|)\) in the unsigned class.

The displayed \(C_*\) makes this expectation at most \(p_1/4\). Bounded differences with deviations \(p_1/4\) and \(p_0/4\) gives the claimed probabilities. For the unsigned class, its total deviation is at most
\(p_1/4+p_0/4\le p_0/2\), which is enough. The resulting coercivity
\[
\mathcal L_n(b)\ge \frac{\kappa p_1}{4}\|b\|
\]
is simultaneous over every direction and every radius. Therefore the full initial sublevel set lies in the deterministic radius-\(R_0\) ball.

## 2. Arbitrary deletions and curvature

The unsigned event supplies at least \(p_0n/2\) rows with
\(|u^\top h_i|>\kappa/2\), for every unit \(u\). After deletion of any at most \(p_0n/4\) rows, at least \(p_0n/4\) remain for that direction. Thus
\[
\frac1n\sum_{i\in I}h_i h_i^\top
\succeq \frac{\kappa^2p_0}{16}I
\]
holds for every retained subset \(I\) with the stated cardinality. This is deterministic on one event; no subset independence or union bound over deletion sets is needed.

The operator-norm proof is also sound: conditional on \(F\), every bilinear form \(u^\top Hv\) is centered \(L\)-sub-Gaussian by independent rows. Two \(1/4\)-nets have at most \(9^{n+m}\) pairs. The proposed threshold gives
\[
2e^{(n+m)\log9-8n}\le2e^{-3n}
\]
when \(n\ge m\), as ensured by the ratio assumption.

For every \(\|b\|\le R\), the number of rows with \(|h_i^\top b|>M\) is at most
\[
\frac{\|Hb\|^2}{M^2}\le \frac{nC_HR^2}{M^2}=\delta n.
\]
Their complement therefore has the robust covariance lower bound. Since sigmoid curvature is at least \(\sigma'(M)\) on this complement, the proposed uniform Hessian lower bound \(\mu I\) follows. The upper bound \(\Lambda I\) holds globally. All statements hold simultaneously on the entire ball, including line segments between full and restricted iterates.

## 3. Finite MLE, restricted objects, and common contraction

Coercivity gives existence of a finite global minimizer; every minimizer is in the initial sublevel ball. Strict convexity there proves global uniqueness. The step constraint implies, eventually,
\[
\eta_-\le\eta_d<1/\Lambda.
\]
Global smoothness gives descent. Thus every full GD iterate stays in the initial sublevel ball. The same descent argument on each coordinate subspace works for each feature-deleted GD path; the relevant gradient is its coordinate projection.

The integrated Hessian along a segment between any two points in that ball has spectrum in \([\mu,\Lambda]\). Hence the full GD map is a contraction there with
\[
q_d=1-\eta_d\mu\le q=1-\eta_-\mu<1.
\]
The value of the full GD map at a restricted point need not stay in the ball for the difference inequality itself: only the two input points and their connecting segment matter. Therefore the later full-versus-restricted comparison does not have a hidden invariance requirement.

The restricted compact minimizer is defined on the deterministic set
\(\{b:b_j=0,\|b\|\le R\}\) for every sample, including exceptional samples. Its loss uses no \(W_j\). Its minimum-norm selector is well-defined, unique, and measurable by the Tikhonov-limit construction stated in B02. On the good event its loss is at most \(\log2\), so its norm is at most \(R_0<R\). It is consequently an interior coordinate-subspace minimizer and has gradient \(g_j^*e_j\). This resolves both existence and omitted-feature independence without conditioning on a good event involving the omitted feature.

## 4. Leave-one-feature concentration and all times

For a restricted iterate or restricted minimizer, condition on
\((X,Y,F_{-j})\). The residual vector is fixed, bounded coordinatewise by one, and independent of \(W_j\). As a function of \(G_j=\sqrt d\,W_j\),
\[
g_j=\frac1n\sum_i r_i\tanh(X_i^\top G_j/\sqrt d)
\]
is odd, centered, and Lipschitz with constant
\[
\frac{\|X\|_{\rm op}\|r\|}{n\sqrt d}
\le \frac{\|X\|_{\rm op}}{\sqrt{nd}}.
\]
The claimed Gaussian tail follows. Intersecting afterward with
\(\|X\|_{\rm op}\le B_X\sqrt d\) is valid; conditioning first on the full good event would not have been.

The choice \(\tau_d=B_X\sqrt{8\log d/n}\) gives individual failure probability at most \(2d^{-4}\). A union bound over \(m\) omitted features, a deterministic \(O(\log d)\) collection of times, and the restricted minimizers is summable up to the stated \(o(1)\) probability. No independence among these many problems is necessary.

Strong monotonicity between the full and restricted MLE gives
\[
\mu\|\bar b^{-j}-b^*\|^2
\le -g_j^*b_j^*
\le |g_j^*|\|\bar b^{-j}-b^*\|,
\]
and hence \(|b_j^*|\le |g_j^*|/\mu\).
For the trajectories,
\[
\|b^{t+1}-b^{-j,t+1}\|
\le q_d\|b^t-b^{-j,t}\|+\eta_d|g_j(b^{-j,t})|.
\]
The geometric sum is exactly bounded by \(\tau_d/\mu\), because
\(1-q_d=\eta_d\mu\). For times beyond \(T_d\), contraction to the already delocalized MLE leaves an extra \(d^{-1}\) at most. This proves one simultaneous all-time infinity-norm bound on a single good event. It does not union-bound over an infinite set of times.

## 5. Positive norm, uniform TV, and exact calibration

The first-step variance calculation is valid. Conditional label fluctuations are independent and bounded; expansion of their quadratic form, including the nonzero conditional mean, gives a variance bounded by
\[
C\{\operatorname{tr}K^2+\|K\bar r\|^2\}\le Cn\|K\|_{\rm op}^2.
\]
The normalization makes the centered fluctuation vanish. Conditional on \(F\), the bounded row terms in \(\operatorname{tr}(KD)\) are iid. Uniform convergence of feature norms and teacher correlations identifies their limit \(v\rho_\beta\). The resulting lower bound on \(\|b^1\|\) has the displayed normalization.

Descent at the first step and convexity at the origin give
\[
\|b^t\|\ge\tfrac12\|b^1\|\qquad(t\ge1)
\]
simultaneously. The MLE follows by taking the actual finite-dimensional GD limit. Therefore every positive iterate has a uniform teacher-orthogonal covariance gap, while the common coefficient ball supplies a uniform variance upper bound.

The derivative estimates used in B04's deterministic TV theorem are uniform over the entire trajectory:
\[
\|\nabla S\|\le LR_0,\qquad
\|\nabla^2 S\|_{\rm HS}\le2L^2R_0,\qquad
\|\nabla^2 S\|_{\rm op}\le2L^2\|b\|_\infty=o(1).
\]
For the Hilbert–Schmidt estimate, one may use
\[
\|F^\top\operatorname{diag}(b_j\phi''_j)F\|_F
\le\|F\|_{\rm op}
\left(\sum_j b_j^2(\phi''_j)^2\|W_j\|^2\right)^{1/2}
\le2L^2\|b\|.
\]
Oddness of every readout centers it.

The appeal to sequential uniformity is legitimate. If the supremum of TV errors over these readouts did not vanish, a deterministic sequence of violating admissible readouts would have the same fixed derivative bounds, covariance gap, and Hessian operator norm tending to zero. It would contradict B04 Theorem 2.1. Selecting a violating time among the countable integer times and the MLE causes no measurability obstruction. The random-environment conclusion follows by applying this deterministic uniform statement on the displayed good event.

The TV-Lipschitz calibration functional then supplies the uniform covariance proxy. Its strict positivity on the compact covariance set is correctly proved by the logistic-Gaussian tail argument; positive residual variance rules out an exactly logistic conditional probability curve. Thus the simultaneous positive calibration floor, arbitrary training-measurable positive stopping times, and the MLE conclusion follow within the stated regime. Time zero is appropriately excluded.

## 6. Uniform deterministic-overlap promotion and scope

The finite-time state-evolution input is now independently checked in B01/B03, including the appended-query conditional law of large numbers. Once fixed-time deterministic overlaps are known, B02's geometric tail estimate
\[
|A_{t,d}-A_{T,d}|+|Q_{t,d}-Q_{T,d}|\le Cq^T
\quad(t\ge T)
\]
passes to every pair of fixed limiting times. The deterministic overlap sequence is therefore exponentially Cauchy. Splitting the supremum into finitely many early times and the common tail proves uniform convergence over all positive integers and infinity. This is a valid exchange-of-limits argument; it does not assume that a fixed-horizon AMP theorem is intrinsically uniform in time.

The proof establishes:

* all-time convergence and calibration, including arbitrary positive stopping times, on the explicit large-sample/small-step open parameter set;
* fixed-horizon state evolution more generally for all fixed positive aspect ratios and fixed positive steps, through the separate B01/B03 result;
* no extension of the uniform-time theorem to small-sample separable regimes or dimension-dependent vanishing steps.

No correction to the displayed proof was required by this audit. Its conservative constants can be improved, but sharp constants are not needed for the stated theorem. No novelty claim is inferred from successful verification.
