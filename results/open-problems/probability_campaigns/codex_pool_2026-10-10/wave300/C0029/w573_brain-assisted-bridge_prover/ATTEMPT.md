# C0029: exact row threshold and Gaussian error absorption

Target status: UNPROVED. Current exact openness: UNKNOWN. No novelty claim. Author is native worker w573; independent adversary w574, referee w575. Requested/served model identities are not equated; response-side served-model evidence is unavailable to this worker. All new lemmas below are author-derived proofs awaiting independent review, not an audited solution.

The target and all assumptions are in STATEMENT.md. The leading coefficient must be exactly one. Primary comparison: Sah--Sahasrabudhe--Sawhney, arXiv:2405.20308v2, Theorems 1.1--1.2, iid real mean-zero variance-one subgaussian entries. The relative error is bounded by C_xi (log n)^(-1/16), plus an exponential additive remainder. Their text explicitly separates this from the exact Rademacher conjecture. This is a black-box input, not a reproof of their theorem.

## Lemma A: cubic margin of the limiting Gaussian CDF

Define f(t)=1-exp(-t-t^2/2), D(t)=t-f(t), and k=exp(-3/2)/3. For every 0<=t<=1,

 k t^3 <= D(t) <= t^3/3.

In particular f(t)<=t, and D(t)/t^3 tends to 1/3 as t decreases to zero. This is an analytic fact about f; identifying f as the fixed-t Gaussian limiting CDF uses the cited random-matrix theorem and DOES NOT provide a finite-n or moving-t error estimate.

Proof. D(0)=D'(0)=0 and D''(u)=u(2+u)exp(-u-u^2/2). For 0<=u<=1, this lies between 2 exp(-3/2) u and 2u. For the upper bound, the function (2+u)exp(-u-u^2/2) decreases from 2: its derivative is (-1-3u-u^2)exp(-u-u^2/2). Integrating D'' twice gives D(t)=integral_0^t (t-u)D''(u)du; integral_0^t (t-u)u du=t^3/6. The limit follows from D''(u)/u -> 2. This proves all assertions. For t>=1 the inequality f(t)<=t follows from f(t)<=1.

## Lemma B: a precise sufficient absorption condition

Let P_n(t) and G_n(t) be CDF values, 0<=t<=1, and let delta>=0, eta>=0, r>=0. Suppose

 P_n(t) <= (1+delta)G_n(t)+r,  G_n(t)<=f(t)+eta.

Then

 P_n(t) <= t + r + delta*t + (1+delta)*eta - k*t^3.

Consequently P_n(t)<=t+r whenever delta*t+(1+delta)*eta<=k*t^3. If eta=0, t>=sqrt(delta/k) suffices (only meaningful where that threshold is <=1).

Proof. Insert the second bound into the first. By Lemma A, f(t)<=t-k*t^3, so (1+delta)f(t)<=t+delta*t-k*t^3. This proves the bound. No finite-n Gaussian estimate is assumed silently: eta must be supplied and justified, especially when t=t_n varies with n.

For the published delta_n=O((log n)^(-1/16)), even the idealized eta=0 calculation only covers t>=constant*(log n)^(-1/32). It leaves the essential smaller window, including subpolynomial and exponential t. Ordinary fixed-t convergence does not fill that window.

## Lemma C: counterexample to the proposed black-box inference

For any 0<delta<=1/4 define H_delta(t)=min{(1+delta)f(t),1} for t>=0 and H_delta(t)=0 for t<0. It is a continuous CDF of a nonnegative random variable and obeys H_delta(t)<=(1+delta)f(t) for every t. At t=sqrt(delta),

 H_delta(t)-t >= (1/2)*delta^(3/2).

Proof. Monotonicity and continuity of f imply the CDF properties, including the eventual saturation at 1. At t=sqrt(delta)<=1/2, (1+delta)f(t)<=(1+delta)t<=5/8<1, so the cap is inactive. Lemma A gives f(t)>=t-t^3/3. Therefore H_delta(t)-t>=delta*t-(1+delta)t^3/3=delta^(3/2)*(1-(1+delta)/3)>=(7/12)*delta^(3/2)>=(1/2)*delta^(3/2).

Take delta_n=min{1/4,(log(n+2))^(-1/16)}. It tends to zero, but the positive surplus dominates c^n for every fixed c in (0,1) for all sufficiently large n. Thus a relative Gaussian comparison of the published size, even with no additive error and even with the exact limiting Gaussian law, does not logically imply coefficient one. This is a counterexample to an inference, NOT a Bernoulli-matrix counterexample. No conclusion that C0029 is false follows.

## Lemma D: shared background exact row-append event, including the small-gap branch

Scope coordination: w567 independently owns the Schur-criterion/bordered-inverse lane. This independently derived background is retained to make the proof need precise; w573 does not submit another row-event node or repeat w567's matrix enumeration. Our distinct submission is Lemmas A--C.

Let n>=2, let N be any real (n-1) by n matrix, let X in R^n, and let M be N with row X appended. Write mu=lambda_2(N^T N), with eigenvalues in increasing order and multiplicity; lambda_1(N^T N)=0. Let tau>=0.

If mu<=tau, then s_min(M)^2<=tau for EVERY X.

If mu>tau, N has rank n-1. Choose an orthonormal eigenbasis v_0,...,v_(n-1) of N^T N, with v_0 in its one-dimensional kernel and d_i>tau the other eigenvalues. Write z_i=<X,v_i>. Then EXACTLY

 s_min(M)^2<=tau  iff  z_0^2 <= tau*(1+sum_(i=1)^(n-1) z_i^2/(d_i-tau)).

Proof of the first branch. In the span of two orthonormal eigenvectors for lambda_1=0 and lambda_2=mu, choose a unit vector y perpendicular to X; the two-dimensional span guarantees such y. Then ||My||^2=||Ny||^2<=mu. This includes rank-deficient N, where mu=0.

Proof of the second branch. In the indicated basis M^T M-tau I=diag(-tau,d_1-tau,...,d_(n-1)-tau)+zz^T. Its lower-right block C=A+z'z'^T is positive definite, where A=diag(d_i-tau). The Schur complement of C is

 S=z_0^2-tau-z_0^2*z'^T C^(-1)z'=z_0^2/(1+z'^T A^(-1)z')-tau.

The last equality follows by solving (A+z'z'^T)C^(-1)z'=z' or by the rank-one inverse identity. The full matrix is positive definite iff S>0, since C is positive definite (complete the square). Therefore its least eigenvalue is <=0 iff S<=0, exactly the stated event. Equality and tau=0 are included. No distinctness of the positive eigenvalues or probabilistic independence of the z_i is required.

The EXACT CDF identity for independent random N and last row X, with tau=t^2/n, is

 P(s_min(M)<=t/sqrt(n))
 = P(mu<=tau) + E_N[1_(mu>tau) P_X(z_0^2<=tau*(1+sum z_i^2/(d_i-tau)) | N)].

This separates disjoint N events; it is not a product of conditional row probabilities. A measurable eigenbasis may be selected, and the displayed quantity is invariant under choices within repeated-eigenvalue subspaces. On the first branch no kernel basis needs to be chosen.

## Lemma E: shared background amount lost by replacing the exact denominator

For the second branch above define chi_tau^2=1+sum z_i^2/(d_i-tau) and chi_0^2=1+sum z_i^2/d_i. Then

 chi_tau^2-chi_0^2=tau*sum z_i^2/(d_i*(d_i-tau))>=0,
 1<=chi_tau/chi_0<=(1-tau/mu)^(-1/2).

If tau<=mu/2, chi_tau/chi_0<=1+tau/mu.

Proof. The difference is an exact algebraic identity. Since d_i>=mu, 1/(d_i-tau)<=1/(d_i*(1-tau/mu)); adding the constant 1 preserves the resulting upper bound. For 0<=r<=1/2, (1+r)^2(1-r)=1+r-r^2-r^3>=1, so (1-r)^(-1/2)<=1+r. All bounds are deterministic, with no concentration input. They show that dropping tau from the denominator shrinks the event: that replacement cannot be used as an upper bound without compensating for the loss.

## Independence trap and the single hardest gap

For independent signs X=(X_1,X_2), orthogonal projections on (1,1)/sqrt(2) and (1,-1)/sqrt(2) are uncorrelated, but their product is identically zero and their squared sum is 2. They are not independent. A Gaussian row has independent orthogonal coordinates by rotational invariance; a Bernoulli row does not. Applying a Gaussian row-factorization to the Bernoulli row is an invalid route.

The single hardest remaining gap is a signed, Bernoulli-specific estimate for the EXACT row-append expectation in Lemma D. With F_B,n and F_G,n the Bernoulli and Gaussian CDFs at t/sqrt(n), one sufficient bridge is

 F_B,n(t)-F_G,n(t) <= t-F_G,n(t) + C exp(-a n)

uniformly in the small window 0<t<1, for some fixed a,C>0. This is a deliberately explicit target inequality, not a theorem or a solved reformulation. Neither the logarithmic relative comparison, Lemma E's deterministic control, nor the orthogonality of row projections supplies its sign. The small-gap branch P(mu<=tau) must remain in the analysis; dropping it invalidates an upper bound. A conditional anti-concentration argument must retain dependence between numerator and denominator.

NEXT: Bound the Bernoulli exact-row CDF's signed difference from the finite-n Gaussian CDF, treating mu<=t^2/n explicitly and retaining joint row-coordinate dependence.
