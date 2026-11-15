MINOR

The mathematical claim survives this audit. In the autonomous semilinear setting of the survey, the argument proves the stated instantaneous regularization on the original Hilbert couple and on the full lifetime of the endpoint maximal solution. The radius in estimate (2) really can be chosen independently of the domain norm of its center. The higher-exponent continuation estimate, deterministic restart times, stopped comparison, and covering argument are valid. The extra growth condition (5.21) is unnecessary for this argument.

The qualification is important: higher-exponent linear stochastic maximal regularity remains an assumption. This is already an assumption of Theorem 5.7, so retaining it does answer the natural reading of Problem 6. It does not give the conclusion from endpoint variational coercivity alone. I found minor citation errors and an attribution omission, but no gap requiring a new mathematical hypothesis. Novelty of the final theorem is plausible within the checked literature, not established exhaustively; its central smallness mechanism is already printed in the survey.

1. **Incorrect Portal–Veraar page reference.** In `claim_files/REPORT.md`, literature item 3, Theorem 5.3 is assigned pp. 574–575. Its statement is on journal pp. **572–573**, PDF pages 32–33 of the independently retrieved published paper. Replace that locator. The theorem does include the endpoint option p=q=2, alpha=0, as the report says. This error has no effect on the proof.

2. **Imprecise Part I locators.** Literature item 1 assigns Theorem 4.8 to preprint pp. 31–32 and describes Theorem 4.7 as on p. 31. In arXiv:2001.00512v5, Theorem 4.8 is stated on **p. 31**; Theorem 4.7 starts on **p. 30** and continues, including its regularity conclusion, on p. 31. Use those precise locators. The underlying statements invoked are correct.

3. **The literature account should identify the existing critical-smallness argument.** Proof Step 1 and the final discussion should cite the survey's **(5.5) and the discussion following it**, published pp. **51–52**, arXiv v5 p. **37**. There the authors explicitly extract the small factor given by a trace-space difference raised to the positive critical power, and absorb the resulting multiple of the top spatial norm. Their reference function is a suitable extension, rather than the fixed domain vector used here. Thus estimate (2) is a useful implementation of an existing idea. The additional contribution would be combining it with global continuation of the higher-q cutoff equations and countably many deterministic restarts. This attribution correction does not invalidate that combination.

These are the errors and material omissions I found. The technical details made explicit below are confirmations of the proof, not additional unresolved objections.

**Independently verified source statements.** All page numbers in this paragraph and the mathematical statements below refer to the 150-page published survey unless an arXiv page is explicitly specified. The downloaded plain texts are independent of `claim_files/sources`. The principal reference is Agresti–Veraar, [survey, DOI 10.1007/s00030-025-01090-2](https://doi.org/10.1007/s00030-025-01090-2), with [arXiv:2501.18561v5](https://arxiv.org/abs/2501.18561v5) downloaded separately. Theorem 4.7 is on pp. 42–43; Theorem 5.1 on p. 48; Theorem 5.7 on pp. 59–60; Assumption 6.1 on pp. 64–65; Problem 6 on p. 130. Their arXiv v5 locations are pp. 30–31, 34, 42–43, 46, and 92, respectively.

Write

\[
 X_\theta=[X_0,X_1]_\theta,\qquad
 X_{\theta,s}=(X_0,X_1)_{\theta,s},\qquad
 E_{p,\kappa}=X_{1-(1+\kappa)/p,p},\qquad
 w_\kappa^a(t)=(t-a)^\kappa.
\]

The first construction is complex interpolation; the second is real interpolation. The background is a filtered probability space with the usual stochastic integration framework, a real separable noise Hilbert space U and an adapted U-cylindrical Brownian motion W. Initial data are strongly measurable with respect to the initial sigma-field. L^0 imposes no moment assumption. X1 embeds densely and continuously in X0. The equation is

\[
 du+Au\,dt=F(u)\,dt+(Bu+G(u))\,dW,\qquad u(0)=u_0. \tag{E}
\]

The survey's presentation here is autonomous and semilinear. The broader time-dependent or quasilinear versions of other papers are not needed.

Assumption 4.1, pp. 38–39, requires X0 to be UMD with type 2, and some lambda0 >= 0 such that lambda0+A is sectorial on X0, with X1=D(A) carrying an equivalent domain norm. The linear operators have the types

\[
 A\in\mathcal L(X_1,X_0),\qquad
 B\in\mathcal L(X_1,\gamma(U,X_{1/2})),
\]

and F:X1 -> X0, G:X1 -> gamma(U,X1/2). The parameters satisfy

\[
 2\le p<\infty,\quad
 \kappa\in[0,p/2-1)\cup\{0\},\quad
 m\in\mathbb N,\quad
 1-(1+\kappa)/p<\beta_j<1,\quad \rho_j\ge0.
\]

For each integer n>=1 there is Ln>0 such that, for u,v in X1 with both E_{p,kappa} norms at most n,

\[
 \|F(u)-F(v)\|_{X_0}+\|G(u)-G(v)\|_{\gamma(U,X_{1/2})}
 \le L_n\sum_{j=1}^m
 (1+\|u\|_{X_{\beta_j,1}}^{\rho_j}
    +\|v\|_{X_{\beta_j,1}}^{\rho_j})
 \|u-v\|_{X_{\beta_j,1}}. \tag{A}
\]

The parameter restriction (4.3) is

\[
 \frac{1+\kappa}{p}\le
 \frac{(1+\rho_j)(1-\beta_j)}{\rho_j}
 \quad (j=1,\ldots,m),
\]

with its nonsingular interpretation (4.4a)

\[
 \rho_j(\beta_j-1+(1+\kappa)/p)+\beta_j\le1. \tag{C}
\]

The latter handles rho_j=0. Critical means equality for at least one j; subcritical means strict inequality for every j. This matches the claim report.

For completeness, the linear hypotheses in Definitions 3.7–3.8, pp. 27–28, have the following quantifiers. Membership (A,B) in SMR_{p,kappa} means that for every finite T there is CT, uniformly for deterministic a in [0,T] and stopping times tau in [a,T], such that every progressive pair

\[
 f\in L^p(\Omega;L^p(a,\tau,w_\kappa^a;X_0)),\qquad
 g\in L^p(\Omega;L^p(a,\tau,w_\kappa^a;\gamma(U,X_{1/2})))
\]

has a unique strong zero-initial-data solution of the linear version of (E), and

\[
 \|v\|_{L^p(\Omega;L^p(a,\tau,w_\kappa^a;X_1))}
 \le C_T\bigl(\|f\|_{L^p(\Omega;L^p(a,\tau,w_\kappa^a;X_0))}
       +\|g\|_{L^p(\Omega;L^p(a,\tau,w_\kappa^a;\gamma(U,X_{1/2})))}\bigr).
\]

The bullet version additionally gives, on deterministic [a,b] subset [0,T], the corresponding L^p(Omega;H^{theta,p}(a,b,w_kappa^a;X_{1-theta})) estimates for every 0<theta<1/2 if p>2, with constants depending on T and theta, uniformly in the endpoints. At (p,kappa)=(2,0), its additional estimate is instead in L^2(Omega;C([a,b];X1/2)). The claim report uses these bullet hypotheses explicitly. In particular it does not infer an L^q forcing norm from an L^2 forcing norm. In the user's formulation, if SMR_{q,0} is meant without the bullet, this distinction does not obstruct the Hilbert-space claim: for a zero-data linear solution v, rewrite its equation with A_* in place of A, deterministic forcing f+(A_*-A)v and stochastic forcing Bv+g. The positive self-adjoint A_* has the bullet estimates. Its forcing norms are controlled by the given L^q(X1) estimate for v and by f,g. This supplies the missing fractional-time and trace bounds, uniformly on a fixed horizon. Thus ordinary unweighted MR also suffices here; the report itself assumes the bullet version.

Theorem 4.7 assumes all the preceding conditions and (A,B) in SMR^bullet_{p,kappa}. For every u0 in L^0_{F0}(Omega;E_{p,kappa}) it gives a maximal local solution (u,sigma), sigma>0 almost surely, with the following properties for each localizing sequence sigma_n increasing to sigma:

\[
 \begin{array}{ll}
 p>2:&u\in H^{\theta,p}(0,\sigma_n,w_\kappa;X_{1-\theta})
          \cap C([0,\sigma_n];E_{p,\kappa}),\\
     &u\in H^{\theta,p}_{\rm loc}((0,\sigma);X_{1-\theta})
          \cap C((0,\sigma);X_{1-1/p,p}),\\
     &\hfill 0\le\theta<1/2;\\[2mm]
 p=2:&\kappa=0,\quad
 u\in L^2(0,\sigma_n;X_1)\cap C([0,\sigma_n];X_{1/2}).
 \end{array}
\]

All memberships are almost sure. Its part (2), also relevant to the proof, says that maximal solutions from u0 and v0 agree, with equal lifetimes, on the initial-measurable event {u0=v0}. The report's short restatement omits this separate clause but uses the same standard localization principle correctly.

Definitions 4.5–4.6 specify the solution class. A strong solution on a stopped interval has progressive paths, the displayed L^p weighted integrability and continuous trace, and satisfies the integrated equation in X0, with the stochastic integrand stopped. A local solution lives on [0,sigma), where sigma is a stopping time with values in [0,infinity], and admits increasing stopping times sigma_n -> sigma on which its restrictions are strong solutions. Nonlinear forcing integrability follows from (A), (C), and the interpolation estimate. Uniqueness means equality on the common stochastic lifetime. Maximality means that every other unique local solution has lifetime at most sigma and agrees before its lifetime; in this semilinear setting this is equivalent to comparison with every local solution. Global means sigma=infinity almost surely. Thus sigma is the lifetime of this specified local solution class, not an externally imposed terminal time or a global-existence assertion.

Theorem 5.1 assumes exactly the conditions of Theorem 4.7 for the stated admissible (p,kappa), and takes its maximal solution. Both conclusions are

\[
 \mathbb P\{\sigma<\infty,\ \lim_{t\uparrow\sigma}u(t)
                    \text{ exists in }E_{p,\kappa}\}=0, \tag{B1}
\]

\[
 \mathbb P\{\sigma<\infty,
    \sup_{t<\sigma}\|u(t)\|_{E_{p,\kappa}}
       +\|u\|_{L^p(0,\sigma;X_{1-\kappa/p})}<\infty\}=0. \tag{B2}
\]

The second time norm is unweighted. There is no extra coercivity, subcriticality, higher-exponent MR, or (5.21) in this theorem. In particular (B1) is available at the Hilbert endpoint, and at the higher-q exponents for the modified equations. The claim uses (B1), correctly, after constructing an actual continuous trace limit. A finite time integral by itself is not asserted to imply such a limit.

Theorem 5.7 assumes all the conditions of Theorem 4.7 with **p>2 and kappa=0**, and uses its maximal solution. In addition, for each n>=1 there must be Cn>0 such that, for x in X1 satisfying ||x||_{X_{1-1/p,infinity}}<=n,

\[
 \|F(x)\|_{X_0}+\|G(x)\|_{\gamma(U,X_{1/2})}
 \le C_n\sum_{j=1}^m(1+\|x\|_{X_{\beta_j,1}}^{\rho_j+1}). \tag{5.21}
\]

These m,beta_j,rho_j are from Assumption 4.1, not newly chosen exponents. Finally it assumes

\[
 (A,B)\in\mathcal{SMR}^{\bullet}_{r,\alpha}
 \quad\text{for every }2<r<\infty,
 \quad0\le\alpha<r/2-1. \tag{all-MR}
\]

Its conclusion is, almost surely,

\[
 u\in H^{\theta,r}_{\rm loc}((0,\sigma);X_{1-\theta})
       \cap C^{\theta-\varepsilon}_{\rm loc}((0,\sigma);X_{1-\theta}),
 \quad 0\le\theta<1/2,\quad 2\le r<\infty,
 \quad0<\varepsilon<\theta. \tag{R}
\]

At theta=0 the Sobolev conclusion is local L^r(X1); there is no positive Holder assertion there. Infinity is not an admissible r. These are local path statements, not bounds at zero, at sigma, or in expectation without localization. The report restates these hypotheses and exponents correctly. The real interpolation ball in (5.21) has second index **infinity**, whereas the trace ball in (A) has second index **p**. At p=2, X_{1/2,2}=X_{1/2} up to equivalent norms for this Hilbert couple; X_{1/2,infinity} is generally strictly larger. Neither it nor X_{beta,1} may be silently replaced by a different interpolation space.

Assumption 6.1 is in the Gelfand triple V -> H -> V*, all embeddings dense and continuous, of real Hilbert spaces, with the H inner product inducing the duality pairing. Set X0=V*, X1=V, H=[V*,V]_{1/2}=(V*,V)_{1/2,2}; let V_{beta,1}=(V*,V)_{beta,1}. It requires A in L(V,V*) and B in L(V,L2(U,H)), and constants vartheta>0, M>=0 such that

\[
 \langle v,Av\rangle-\tfrac12\|Bv\|_{L_2(U,H)}^2
 \ge\vartheta\|v\|_V^2-M\|v\|_H^2\qquad(v\in V).
\]

The nonlinearities have the types F:V -> V*, G:V -> L2(U,H) and satisfy (A), with V*,H,V_{beta_j,1} replacing X0,X1/2,X_{beta_j,1}, on each bounded H ball. The exponents are beta_j in (1/2,1), rho_j>=0 and

\[
 (2\beta_j-1)(\rho_j+1)\le1\quad(j=1,\ldots,m). \tag{6.1}
\]

There is no additional growth bound, nonlinear coercivity, or monotonicity in Assumption 6.1. Its linear coercivity supplies endpoint MR, not automatically (all-MR). Equality in (6.1) implies rho_j>0. All this agrees with the report.

**Audit of Proof Steps 1–4.** I checked the algebra and the required solution classes independently rather than treating the claimant's artifact checker as a proof verifier.

For Step 1, real reiteration gives

\[
 (X_{1/2,2},X_1)_{a_j,1}=X_{\beta_j,1},
 \qquad a_j=2\beta_j-1\in(0,1).
\]

The elementary real-interpolation bound on X1 therefore gives precisely (1), with the second index 1 retained. This is also the pointwise inequality used in the proof of survey Lemma 4.3. For ||y||_E<=N and ||w||_E<=2d<=2, (A) bounds the nonlinear difference by a constant depending on N times

\[
 \sum_j\big[(1+\|y\|_{X_{\beta_j,1}}^{\rho_j})
                   \|w\|_{X_{\beta_j,1}}
          +\|w\|_{X_{\beta_j,1}}^{\rho_j+1}\big].
\]

Put Z=||w||_{X1}. The first terms have power Z^{a_j}, strictly below one. Young's inequality puts any chosen small coefficient before Z; its additive constant may depend on y. The last term is bounded by

\[
 C\|w\|_E^{(1-a_j)(\rho_j+1)}Z^{a_j(\rho_j+1)}.
\]

If a_j(rho_j+1)<1, the same Young argument works, with d<=1. At equality the factor is exactly

\[
 C\|w\|_E^{\rho_j}Z\le C(2d)^{\rho_j}Z,
 \qquad\rho_j>0.
\]

Only the constants on the fixed E ball and the finitely many exponents enter the choice of d. Large ||y||_{X1} increases the additive constant, not the required radius. This answers question 2(a) affirmatively. As a second algebraic check, (C) at p=2 becomes 2 beta_j(rho_j+1)<=rho_j+2, which is equivalent to (6.1); subtracting the top-norm exponent from rho_j+1 gives exactly rho_j at equality. No logarithmic endpoint interpolation estimate is being substituted here.

For Step 2, choose q>2 with a=1-1/q>max beta_j and put E_q=X_{a,q}. Such q exist in the assumed unbounded sequence. The strict spatial gap gives E_q -> X_{beta_j,1} and E_q -> E. Consequently F,G on X1 extend by density to locally Lipschitz functions on E_q. On an E_q ball, (A) bounds both the coefficient values and their differences; this also controls the cutoff product. The modified functions (7) are thus locally Lipschitz on E_q. To apply Theorem 4.7, one may choose new rho'=0 and any beta' in (a,1), using X_{beta',1} -> E_q. There is no unjustified reuse of critical exponents from the endpoint equation.

The cutoff supplies the global growth bound

\[
 \|F_y(x)\|+\|G_y(x)\|\le\eta\|x\|_{X_1}+K_y.
\]

This is a growth estimate, not a small Lipschitz constant for the cutoff. Local well-posedness and continuation are separate steps. The correct initial-data space for exponent q is **E_q**, not all of E. X1 embeds into E_q, so the application to domain-valued restarts is valid. Boundedness of the initial E_q norm, not boundedness of its X1 norm, is what the expectation estimate needs.

Nonzero initial data are allowed by Part I Proposition 3.10, arXiv pp. 22–23, and Part II Proposition 3.9, published pp. 21–23. The report's alternative construction is valid as well. A dense Hilbert couple admits a positive invertible self-adjoint A_* with D(A_*)=X1, with equivalent domain norm; the survey uses precisely this fact in the proof of Theorem 3.13. For e(t)=exp(-(t-s)A_*)xi, the equation for z=v-e has forcings

\[
 f+(A_*-A)e,\qquad g+Be.
\]

Both signs and the linear noise correction are correct. Deterministic trace theory bounds e in W^{1,q}(X0) intersect L^q(X1) by ||xi||_{E_q}. The zero-initial-data estimates then give (9), with a deterministic M_{q,T} uniform in s<=T. Trace continuity in E_q follows from the bullet estimates, choosing 1/q<theta<1/2, and Proposition 2.1. Self-adjointness of A itself is not being assumed.

Choose eta after q and T so that M_{q,T} eta<=1/2, then choose d(N,eta). No uniformity in q or in infinite horizons is necessary. Stop the local q solution where its accumulated L^q(X1) norm is bounded, intersecting with its localizing sequence. The killed forcings are progressive and have finite product-space L^q norms; endpoints of indicators do not affect either integral. Solve the linear equation on the full deterministic horizon. Its solution agrees with v up to the stopping time. This gives exactly the absorption inequality (10) in L^q(Omega times dt), without a pathwise stochastic operator norm.

Fatou gives finite L^q forcing and solution norms up to tau wedge T. Killing these forcings at tau and solving once more on [s,T] produces a solution continuous in E_q which agrees with v before tau. Hence v has a trace limit on {tau<=T}. Apply (B1) to the modified equation to rule out that finite explosion. This proves existence and uniqueness throughout [s,T] for the bounded E_q-valued initial data used below. One may paste along initial-measurable partitions for merely measurable E_q data. Part II Theorem 4.15, published pp. 39–41, contains the same small-linear-growth continuation principle; its discussion explicitly allows a sufficiently small fixed coefficient for a fixed horizon. The report does not require smallness independent of the horizon.

For Step 3, adaptedness is handled correctly. Since u is locally L^2(X1) almost surely before sigma, Fubini, after localization if needed, gives a deterministic full-Lebesgue-measure set S of times s such that 1_{s<sigma}u(s) is strongly F_s-measurable and X1-valued almost surely. Choose a countable dense D subset S. Arbitrary rational times would not suffice, and the report does not use them for this purpose.

For s in D, the event

\[
 \Gamma_{s,k,q}=\{s<\sigma,\ \|u(s)\|_{E_q}\le k\}\in\mathcal F_s
\]

and xi=1_Gamma u(s) give bounded E_q-valued initial data. Membership and norm events can be formed using the strongly measurable X1-valued version at a good time and the continuous embedding X1 -> E_q. Thus no future event is used as initial information. One constructs all cutoff solutions first, for countably many s,k,q,N,T and deterministic centers y.

The needed uniqueness is local on an equality region of the two coefficients. For fixed s,y, intersect Gamma with the F_s event that u(s) is inside the ball; stop both paths at their first E-ball exits and before the original lifetime. On that interval the modified solution has the original coefficients. A q solution on a finite interval belongs to L^2(X1) intersect C(E), and its forcings belong to L^2 in the required spaces. It is therefore in exactly the endpoint comparison class. Pathwise uniqueness, with initial-event localization as in Theorem 4.7(2), gives equality up to the first exit. This can equivalently be formalized by comparing both stopped solutions to the original equation started at xi. It is not an assertion of global uniqueness between two different equations. All stopping times here are legitimate exits of adapted continuous paths, capped by the lifetimes.

A single countable family of centers suffices. If E is not separable, the essential ranges of the countably many E-valued variables 1_{r<sigma}u(r), for rational r, lie in a deterministic separable closed subspace. Continuity brings all path values before sigma into that subspace on one probability-one event. Approximate a countable dense subset of it by domain vectors in E. These centers need not belong to the subspace itself. Choosing integer N with a margin handles their norm bound. Uniformity of d in ||y||_{X1} is essential and has already been proved.

Now fix one sample point outside the countably many null sets and any t in (0,sigma). For each q, choose integer T>t, integer N>||u(t)||_E+2, and a center with distance <d/4 from u(t). Continuity gives a neighborhood of t inside (0,sigma wedge T) on which the distance from y is <d/2. There is s in D just before t and b>t in this neighborhood; choose k with the sample point in Gamma_{s,k,q}. Equality before exit implies the modified path cannot exit the d ball on [s,b], since the original path stays in its d/2 ball. Thus u agrees there with a q solution, on an interval containing t in its interior.

This argument covers **every** t in (0,sigma), rather than almost every time. It also covers times arbitrarily near sigma: for each t<sigma there is still room to choose b between t and sigma. No neighborhood of the point sigma is claimed. Finite covers of each compact subinterval and the local nature of Bessel potential regularity yield the asserted H^{theta,q}_loc bounds. There is no implicit uniform bound on K_y over all centers.

For Step 4, take a countable unbounded sequence of the admissible q, and initially a countable increasing sequence theta_l ->1/2, including theta=0 separately. On compact intervals H^{theta,q} embeds in H^{theta,r} for finite r<=q. To obtain all theta simultaneously without changing the spatial space, use mixed complex interpolation between L^q(X1) and H^{theta_l,q}(X_{1-theta_l}); the Hilbert couple supplies [X1,X_{1-theta_l}]_lambda=X_{1-lambda theta_l}. This gives exactly X_{1-theta} at theta=lambda theta_l. Local extension/cutoff operators allow the interpolation on deterministic intervals inside the comparison neighborhoods.

Finally, for 0<epsilon<theta<1/2 choose q with 1/q<epsilon. Time Sobolev embedding gives C^{theta-1/q}(X_{1-theta}), hence C^{theta-epsilon}(X_{1-theta}). Countable parameters followed by these deterministic embeddings give a common probability-one event. All finite r and the full Holder range in (R) follow; theta=1/2 and r=infinity do not.

**Literature, attribution, and the question of value.** The earlier papers contain the ingredients but I did not find this same-couple endpoint theorem stated in them.

Part II Proposition 6.8, published pp. 76–80 / arXiv v4 pp. 66–70, requires a second couple with

\[
 Y_\delta=X_0,\quad Y_1=X_{1-\delta},\quad
 \frac1p=\frac{1+\alpha}{r}+\delta,
 \quad r\ge p,\ r>2,\ 0\le\alpha<r/2-1.
\]

It also requires delta<1-max_j phi_j, 1/r>=max_j phi_j-1+1/p, the nonlinear growth condition (6.22), Hypothesis H and Assumption 4.7 on the shifted couple, shifted SMR^bullet_{r,alpha}, and shifted unweighted SMR_q for every q in [2,r]. It expressly requires p>2 if delta=0. At p=2 its identity forces delta>0. Its initial conclusion is H^{theta,r}_loc(X_{1-delta-theta}). Neither extending F,G nor extending the MR of (A,B) to that rougher couple follows from the present hypotheses. One cannot simply apply Theorem 5.7 on a shifted couple and claim to have proved the present result. Recovering the spatial loss requires additional information.

The Navier–Stokes paper, Theorem 4.1 Part C, published pp. 34–35, carries out that strategy for a concrete model with such additional scale structure. It begins with q=p=d=2, delta=0, introduces a rougher space and positive weight, then recovers spatial regularity. This supports the report's distinction between a concrete result and the abstract question.

Survey Proposition 5.9, pp. 60–61, assumes a genuinely sublinear top-norm growth exponent phi in (0,1), on bounded X1/2 balls, as well as u0 in L^0(X_{1/2+epsilon}) for some epsilon>0 and (all-MR). It does not apply directly at critical linear growth. The new proof effectively supplies small linear growth after a trace cutoff, and uses domain-valued good times to remove the extra initial smoothness. Its use of arbitrary positive restart times is significant; merely solving from the original rough initial datum in E_q would be invalid.

The obstacle in the printed weighted method is real: preserving the old trace exponent while increasing time integrability requires (1+alpha)/r=1/p. At p=2 this is alpha=r/2-1, excluded by the stochastic weight range. The cutoff argument avoids that identity by starting at smoother values and proving continuation of a modified equation. One cannot infer the authors' reasons for posing the problem. The fact that they already knew the small-critical-factor estimate is reason to scrutinize the synthesis, not a mathematical contradiction. The argument above supplies the missing checks of that synthesis.

I independently examined the 2025–2026 papers singled out by the claim and searched the problem wording, the survey identifier with endpoint/Hilbert/critical/regularization terms, and the authors' publication lists. [Agresti–Veraar's temporal-threshold note](https://arxiv.org/abs/2509.07803v3) disproves a different assertion: for positive invertible self-adjoint A and constant noise x, its Theorem 1.1 gives L^2(Omega;W^{alpha,2}(D(A^{1/2}))) if and only if x belongs to D(A^alpha). In the variational version this is regularity in V itself. In (R), X_{1-theta} is rougher than V for theta>0. Thus this note neither disproves nor settles Problem 6. Increasing energy moment exponents in classical variational results likewise does not give higher time integrability in V.

[Agresti, arXiv:2602.21981v3](https://arxiv.org/abs/2602.21981v3), Lemma 3.11, pp. 22–23, assumes the instantaneous-regularization property used in its abstract statement. [Agresti–Germ–Veraar, arXiv:2606.07417v3](https://arxiv.org/abs/2606.07417v3), Theorem 4.8, p. 30, still requires p>2; Theorem 2.12, p. 15, is its concrete regularization result. Its cited 2026 book/project in preparation is not a checked accessible theorem. I found no earlier printed resolution of the present assertion in these sources. This is a bounded literature finding as of 13 November 2026, not certification of priority over all papers or unpublished work. Claims of first discovery should remain correspondingly limited.

The all-MR assumption is substantial for B nonzero, but it is not a new condition added to evade Problem 6: it is printed in Theorem 5.7 itself. The proof actually needs only an unbounded sequence of unweighted higher-q bullet estimates. For B=0, Theorem 3.13 gives all the required linear exponents for an analytic generator on a Hilbert space. For general B, endpoint coercivity cannot be silently substituted for higher-q MR. On the ordinary reading that “extend Theorem 5.7” retains its other hypotheses, the proved result is affirmative, and stronger concerning (5.21). On the different reading that asks for (R) from Assumption 6.1 alone, this proof is conditional and does not answer that stronger question.

**Citation audit.** The following checks cover the citations in the claim report, including the auxiliary literature. Statements not directly accessible are distinguished from directly read ones. Source-version pinning and DOI metadata are in `data/sources.jsonl` and `sources/bibliography_metadata.txt`; theorem locators are in `data/source_locations.json`.

| Citation in the claim | Independent check |
|---|---|
| Survey: NoDEA 32(6), article 123 (2025), DOI 10.1007/s00030-025-01090-2; 150 pp.; online 1 September 2025 | Correct: publisher, first page, and DOI metadata. arXiv:2501.18561v5 is 103 pp., version 27 August 2025, first submission 30 January 2025. |
| Survey Assumption 4.1 pp. 38–39; Definitions 3.7–3.8 pp. 27–28; Theorem 4.7 pp. 42–43; Theorem 5.7 pp. 59–60; Assumption 6.1 pp. 64–65; Problem 6 p. 130 | Correct. ArXiv Theorem 5.7 pp. 42–43, (6.1) p. 46, Problem 6 p. 92 are also correct. |
| Survey Theorem 3.13 pp. 31–33; Proposition 3.11; Lemma 4.3; Theorem 5.1(1); Proposition 5.9 pp. 60–61 | Correct statements and uses; Theorem 3.13's proof uses the self-adjoint reference. Proposition 3.11 requires an analytic generator, satisfied in the setting; the report also gives its independent initial-extension construction. Theorem 5.1 is on p. 48. |
| Survey Remark 5.8(1), p. 60, sign of delta, compared with p. 57 | The printed sign is inconsistent with positivity/admissibility, as the report says. Correct delta=1/2-(1+alpha)/r>0 at p=2. |
| Part I: Nonlinearity 35(8) (2022), 4100–4210, DOI 10.1088/1361-6544/abd613; arXiv:2001.00512v5, 29 April 2022 | Bibliography/version correct. Proposition 3.10 pp. 22–23 and Proposition 3.12 pp. 23–24 are correct. Theorem 4.8 p. 31 and Theorem 4.7 pp. 30–31 have the pinpoint corrections in item 2 above. |
| Part II: J. Evol. Equ. 22(2) (2022), article 56, 96 pp., DOI 10.1007/s00028-022-00786-7; arXiv:2012.04448v4 | Correct. Published Proposition 3.9 pp. 21–23; Theorem 4.15 pp. 39–41; Theorem 6.3 pp. 70–74; Corollary 6.5 pp. 74–75; Proposition 6.8 pp. 76–80 agree with the cited locations and mechanisms. |
| Portal–Veraar: Stoch. PDE Anal. Comp. 7 (2019), 541–597, DOI 10.1007/s40072-019-00134-w, arXiv:1810.01183 | Bibliography/identifier correct. Lemma 2.7 pp. 551–552 and Theorem 3.9 pp. 556–559 are correct. Theorem 4.5 pp. 569–570 is correct; Theorem 5.3 is pp. 572–573, not 574–575. Both have the stated p=q=2 endpoint option. |
| Krylov–Rozovskii, Russian original 1979, Itogi Nauki i Tekhniki 14, 71–146; English J. Soviet Math. 16 (1981), 1233–1277, DOI 10.1007/BF01084893 | Bibliographic data agree with DOI metadata and institutional/original-reference records. My publisher PDF request returned HTML. No claim to have read original Theorems II.2.1–II.2.2 directly. Liu–Röckner Theorem 4.1, arXiv p. 17, explicitly cites them and gives the described energy solution/Itô identity. |
| Liu–Röckner 2010: JFA 259, 2902–2922, arXiv:1005.0632, Definition 1.1 / Theorem 1.1 pp. 3–4 | Bibliography correct; DOI metadata additionally identifies 10.1016/j.jfa.2010.05.012. Definition and theorem are on p. 4, with assumptions on preceding pages. The theorem's moment exponent p is distinct from its time-integrability exponent alpha; the report's distinction is correct. |
| Liu–Röckner book (2015), DOI 10.1007/978-3-319-22354-4, Theorem 4.2.4 | Title, authors, year and DOI verified at publisher/DOI metadata. My full-text request returned HTML. The critical-variational paper p. 972 explicitly cites Theorem 4.2.4 and its proof for the nonrandom-start linear energy estimate; this verifies the report's accurately qualified indirect use, not a direct full theorem audit of the unavailable book. |
| Critical variational paper: PTRF 188 (2024), 957–1015, DOI 10.1007/s00440-023-01249-x, arXiv:2206.00230 | Correct; independently fetched arXiv v4 and published text. Theorem 3.3 pp. 968–969; Theorems 3.4–3.5 pp. 969–970; Theorem 3.8 p. 971; Lemma 4.1 p. 972 match. Their conclusions are energy-class statements, as reported. |
| Navier–Stokes: CMP 405(2) (2024), article 43, 57 pp., DOI 10.1007/s00220-023-04867-7, arXiv:2107.03953 | Correct; independent arXiv v4 has 53 pp., published version 57 pp. Theorem 2.4 starts published p. 11; Theorem 4.1 starts p. 29; Part C is pp. 34–35. The report correctly distinguishes this from the survey's incompatible pp. 43–44 pointer. |
| Temporal threshold: arXiv:2509.07803v3, 29 May 2026, 8 pp.; C. R. Math. 364 (2026), 371–379, DOI 10.5802/crmath.833 | Correct. Theorem 1.1 preprint p. 2 becomes Theorem 1, journal p. 372; Theorem 1.3 preprint pp. 3–4 becomes Theorem 3, journal p. 374. The download has an extra cover page; PDF page numbers must not be mistaken for journal pages. |
| arXiv:2602.21981v3, 28 October 2026; Lemma 3.11 pp. 22–23 | Correct title, author, date, version and assertion. |
| arXiv:2606.07417v3, 9 November 2026; Theorems 2.12 p. 15 and 4.8 p. 30; 2026 work in preparation | Correct title, authors, date, version, theorem locations and p>2 restriction. The in-preparation reference is present. |

**Verification record and precise result.** I read every part of the claim report and its mathematical audit, independently downloaded the four required arXiv works plus the relevant published and later versions, and checked the supporting theorem statements in the extracted texts. The source downloads use PDF bytes only in memory and pipe them to pdftotext; no PDFs or images are retained. Hashes, retrieval URLs and page counts record provenance. Source pinpoints were checked against both PDF-page markers and printed journal pagination. DOI metadata was independently retrieved for every journal/book identifier. The scripts verify provenance and artifact constraints; they do not machine-verify this mathematical proof. The mathematical checks are the derivations and solution-class arguments above.

The accepted mathematical result is: under the endpoint Hilbert hypotheses of Theorem 4.7 and the stated critical bounds, an unbounded sequence of unweighted higher-q bullet maximal-regularity estimates implies (R) on (0,sigma), for the endpoint maximal solution, without (5.21). No global existence, global moment estimates, regularity at the initial time, or temporal half-derivative endpoint is proved. Subject to the minor corrections listed, this is a valid affirmative answer to Problem 6 with Theorem 5.7's remaining assumptions retained.

Task: “Break it if it is wrong … Write REPORT.md” — 13 November 2026, 16:50 +04 (referee task start).
