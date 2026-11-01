P0017 referee-integrator attempt, 2026-10-10, w350

The target is a universal bound C_P(mu) <= C for every isotropic log-concave probability measure in every dimension. C_P multiplies the squared-gradient energy. Current openness is UNKNOWN in this packet: primary October 2026 preprints claim full solutions, and this packet has not independently checked a full proof. The September intake's Gaussian calculation is only a special case. No novelty or parent-solution claim is made here.

This lane is a Gaussian-observation variance-retention bridge. It is disjoint from w348's deterministic block-symmetry tensor recovery. The following arguments were derived before reading w348's proof. Own results require w353's independent review.

For t > 0, let X have law mu, let G be independent standard Gaussian in R^n, and set Y = sqrt(t) X + G. Define

q_f(t) = E[Var(f(X) | Y)],
R_mu(t) = inf_{f in L^2(mu), Var_mu(f) > 0} q_f(t)/Var_mu(f).

All gradients below are Euclidean. The channel normalization matters: observation sqrt(t)X + G, or equivalently tX + sqrt(t)G, gives posterior curvature t. Observation tX + G would instead give curvature t^2.

Claim A: Poincare implies quantitative retention, without log-concavity.

Assume mu satisfies Var_mu(h) <= C int |grad h|^2 dmu on its Sobolev domain, with finite C. Then R_mu(t) >= 1/(1+Ct) for every t > 0.

Proof. Initially take bounded smooth g with compactly supported derivatives and define h(x) = E_G[g(sqrt(t)x+G)]. Gaussian integration by parts gives

grad h(x) = sqrt(t) E_G[G (g(sqrt(t)x+G)-h(x))].

The coordinate functions G_1,...,G_n are orthonormal in centered Gaussian L^2. Bessel's inequality therefore gives the dimension-free estimate

|grad h(x)|^2 <= t Var_G(g(sqrt(t)x+G)).

Applying the assumed Poincare inequality and the law of total variance yields

Var_mu(h) <= Ct E_X Var_G(g(Y)|X)
             = Ct(Var_Y(g)-Var_mu(h)).

Consequently Var_mu(h) <= [Ct/(1+Ct)] Var_Y(g). This extends to all centered g in L^2(law(Y)) by density of bounded smooth functions and the L^2 contraction of conditional expectation. To see the adjoint explicitly, let T g = E[g(Y)|X] on the centered L^2 spaces. For centered f and g,

<f,Tg>_{L^2(mu)} = E[f(X)g(Y)] = <E[f(X)|Y],g>_{L^2(law(Y))}.

Thus T* f = E[f(X)|Y], and ||T*|| = ||T|| <= sqrt(Ct/(1+Ct)). Applying total variance once more gives

q_f(t) = Var_mu(f)-Var_Y(E[f(X)|Y]) >= Var_mu(f)/(1+Ct).

This uses a Hilbert-space adjoint, not independence between posterior coordinates. Independence is needed only for the auxiliary Gaussian noise and X, as stated. The use of C_P in this direction is an ASSUMPTION, so it cannot be used to prove the parent target.

Claim B: retention implies Poincare for log-concave mu.

Assume mu is a full-dimensional log-concave Borel probability law and R_mu(t0) >= eta > 0 at a deterministic t0 > 0. Then C_P(mu) <= 1/(eta t0).

Proof. Write mu(dx) proportional to exp(-V(x))dx on its convex support, allowing convex extended-valued V. The posterior at observation y is proportional to

exp[-V(x)-t0|x|^2/2+sqrt(t0)y.x]dx.

It is t0-uniformly log-concave. The log-concave Lichnerowicz/Brascamp-Lieb inequality gives C_P(mu_y) <= 1/t0, including convex supports by the standard generalized inequality. This is the precise external input, recorded in Klartag 2303.14938v2, equation (1.7). For any locally Lipschitz f in L^2(mu) with finite Dirichlet energy, apply that inequality in almost every posterior and average:

q_f(t0) <= (1/t0) E_Y int |grad f|^2 dmu_Y
         = (1/t0) int |grad f|^2 dmu.

The equality is conditional expectation/tower, not a product assumption. Combining this with q_f(t0) >= eta Var_mu(f) proves the claim. If using only the elementary smooth form of Brascamp-Lieb, restrict first to smooth convex V and smooth f, then invoke the stated generalized Lichnerowicz input for the extension; do not invent a boundary condition.

The hardest still-unproved input IN THIS ROUTE is:

VR: There exist deterministic universal t0 > 0 and eta > 0 such that R_mu(t0) >= eta for all isotropic log-concave mu in all dimensions, with the infimum over ALL L^2 test functions.

VR gives the full target by Claim B. Conversely, an assumed universal KLS constant C gives VR with t0 = 1/C and eta = 1/2 by Claim A. Thus VR is equivalent to the target up to explicit constants. This equivalence identifies the load-bearing input; it does not make that input easier or prove it. Linear or quadratic tests alone do not establish the all-function infimum. A good path event for covariance alone does not establish weighted variance retention for an arbitrary f.

Claim C: exact Gaussian reproduction.

For mu = N(0,I_n), R_mu(t) = 1/(1+t). The standard Gaussian Poincare inequality with sharp C=1 gives the lower bound through Claim A. For f(x)=u.x with |u|=1, the Gaussian posterior covariance is I_n/(1+t), so q_f(t)/Var_mu(f) = 1/(1+t), giving the matching upper bound. Claim B then yields C_P <= (1+t)/t, while the existing Hermite proof gives the sharper exact C_P=1. These constants expose the loss of Claim B and verify the channel normalization. This adds a quantitative bridge; it does not replace the earlier Gaussian special case with a new solution.

Sources: Klartag, Logarithmic bounds for isoperimetry and slices of convex sets, https://arxiv.org/html/2303.14938v2, equations (1.3)-(1.8); local intake brain_bundle_C006a04.json entry at-p0017 for the prior Gaussian argument. Claims A-B are self-contained campaign derivations except the explicitly named uniform-log-concavity Poincare input. Independent reviewer: w353, pending. No formal proof assistant receipt exists.

NEXT: Send Claims A-B to w353 for a narrow adjoint/domain/normalization audit, then check w348's stated tensor operator and w349's obstruction against exact hypotheses.
