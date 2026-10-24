# P0334 attempt — 2026-10-12

Exact target: for finite 1<p<infinity characterize distributions P for which sqrt(n)(Q_n-Q) converges weakly in L^p(0,1), with standard left-continuous empirical quantiles.

Answer: Q is locally absolutely continuous and integral [t(1-t)]^(p/2)|Q'(t)|^p dt is finite. Limit: -Q'B (the sign does not change its law).

This criterion is proved below. The argument combines verified published ingredients with a signed-envelope approximation step. It was not found stated as a theorem in the literature search.

The critical quantitative bound is Bobkov–Ledoux Theorem 5.3, verified in its original PDF. Applied to the increasing primitive of the absolute derivative error, it makes approximation by smooth compactly supported derivatives uniform in sample size, closing the endpoint tightness issue.

The completed proof follows.

## Theorem (finite p>1)

Let P be ANY Borel probability measure on R, Q its standard left-continuous quantile, and Q_n the empirical quantile of n iid observations. For every fixed real 1<p<infinity, sqrt(n)(Q_n-Q) converges weakly as an L^p(0,1)-valued random element if and only if Q is locally absolutely continuous and

 K_p(Q) = integral_0^1 [t(1-t)]^(p/2)|Q'(t)|^p dt < infinity.

These conditions automatically imply Q in L^p. The limit is -Q'B, equivalently +Q'B in law, for a standard Brownian bridge B. If P has a positive density on an interval, Q'=1/(f composed with Q) a.e., so K_p is exactly the source's J_p. No endpoint monotonicity is needed. The quantile formulation includes measures with atoms and singular components when Q is locally absolutely continuous. A point mass gives Q'=0 and the zero process. No statement about p=infinity is made.

## Verified external inputs

Bobkov–Ledoux, *One-Dimensional Empirical Measures, Order Statistics, and Kantorovich Transport Distances*, author-hosted 140-page PDF `bobkov_ledoux.pdf`, Theorem 5.3, printed/PDF p.46:

 E W_p(mu_n,mu)^p <= (5p/sqrt(n+2))^p J_p(mu), for every p>=1 and n>=1.       (BL)

For a locally absolutely continuous quantile H, J_p(mu)=integral |H'(t)|^p[t(1-t)]^(p/2)dt, precisely by Corollary A.22, p.109. The book uses the absolutely continuous COMPONENT of a measure, not an assumption that the whole measure is absolutely continuous; see pp.44,46, Appendix A.5 and Proposition A.17, p.104. The book's absolute continuity is local, explicitly stated in Lemma 5.8, p.51. Flat quantile segments are permitted. Theorem 5.3 imposes no endpoint monotonicity, and is proved using Theorem 4.6 and Proposition B.13 (p.125). We weaken its constant to (5p)^p after multiplication by n^(p/2).

Beare–Kaji, arXiv:2502.01254v4, Theorems 3.1 and 3.2, PDF p.16: an integrable Q has an L^1 quantile-process limit if and only if Q is locally absolutely continuous and integral sqrt(t(1-t))dQ(t)<infinity. Under these conditions the limit is -Q'B. (BK)

Other standard inputs are Donsker's uniform empirical-process theorem (including asymptotic equicontinuity), Fernique's theorem for a Gaussian Radon element in a separable Banach space, smooth approximation in L^p, Hölder, and Tonelli. The argument below supplies the passage to L^p tightness; it never infers tightness merely from bounded expected norms.

## Lemma 1: moment finiteness

If r is locally absolutely continuous and K=integral [t(1-t)]^(p/2)|r'(t)|^p dt<infinity, then r is in L^p. Monotonicity is unnecessary.

Proof. Let c=1/2 and p*=p/(p-1). For 0<t<c, Hölder and comparability of s(1-s) with s give

 |r(t)-r(c)|^p <= C_p K (integral_t^c s^(-p*/2)ds)^(p-1).

For p>2 the last factor is bounded; for p=2 it is log(c/t); for 1<p<2 it is at most C_p t^(p/2-1). Each is integrable down to zero. Reflect t about 1/2 to treat the other endpoint. Add the finite constant r(c). This proves the lemma.

## Lemma 2: uniform signed-function approximation bound

Take iid uniforms U_1,...,U_n, their order statistics U_(i), and V_n(t)=U_(ceil(nt)) for 0<t<=1. Define T_n r(t)=sqrt(n)[r(V_n(t))-r(t)]. For every locally absolutely continuous real r with finite K_p(r),

 E||T_n r||_p^p <= (5p)^p K_p(r),
 E||T_n r||_p <= 5p K_p(r)^(1/p).                         (A)

Proof. Define the oriented integral H(t)=integral_(1/2)^t |r'(s)|ds. It is finite at each interior t, nondecreasing, continuous, locally absolutely continuous, and H'=|r'| a.e. The fundamental theorem on each interior interval gives, for all u,v in (0,1),

 |r(v)-r(u)| <= |H(v)-H(u)|.                              (D)

H belongs to L^p by Lemma 1 and K_p(H)=K_p(r). Let mu be the law of H(U). Its standard quantile is H: if x>=H(t), then F_mu(x)>=t; if x<H(t), left continuity provides t_0<t with H(t_0)>x and monotonicity gives F_mu(x)<=t_0<t. Thus the generalized inverse is H(t), even on flat segments. Ordering H(U_i) gives H(U_(i)), including ties; consequently its empirical quantile is H(V_n). The one-dimensional quantile formula gives ||T_n H||_p^p=n^(p/2)W_p(mu_n,mu)^p. Apply (BL) and (D), noting n/(n+2)<=1. Hölder on the probability space gives the first-moment assertion. Every evaluation is at an interior finite value a.s. and Lemma 1 ensures L^p-valuedness.

The residual r need not be a quantile or have a nonnegative derivative. The increasing envelope H is what makes the published transport theorem applicable. All comparisons use the SAME uniform sample and order statistics.

## Lemma 3: smooth reference process convergence

If g_0 is nonnegative, smooth, and compactly supported in (0,1), let Q_0(t)=a+integral_(1/2)^t g_0(s)ds. Then T_n Q_0 converges weakly to -g_0 B in L^p.

Proof. Q_0 extends to C^1[0,1] with uniformly continuous derivative. Let G_n be the uniform empirical cdf, alpha_n=sqrt(n)(G_n-id), and beta_n=sqrt(n)(V_n-id), setting V_n(0)=U_(1). By Donsker, alpha_n converges to B in the usual uniform empirical-process sense, has tight uniform norm, and is asymptotically equicontinuous. Uniform samples have no ties a.s. Since |G_n(V_n(t))-t|<=1/n for all t in [0,1],

 beta_n(t)=-alpha_n(V_n(t))+e_n(t), ||e_n||_infinity<=1/sqrt(n).

Therefore ||V_n-id||_infinity <= (||alpha_n||_infinity+1/sqrt(n))/sqrt(n) ->0 in probability. Asymptotic equicontinuity implies ||alpha_n composed with V_n-alpha_n||_infinity->0 in probability. Thus beta_n converges to -B and its uniform norm is tight. If omega is the modulus of continuity of g_0, the fundamental theorem gives

 ||T_n Q_0-g_0 beta_n||_infinity
 <= ||beta_n||_infinity omega(||V_n-id||_infinity) ->0 in probability.

Multiplication by g_0 and inclusion into L^p are continuous in the uniform norm, proving the lemma. The final L^p random elements are measurable in a separable Banach space. This use of Donsker does not assume point evaluation is continuous in L^p.

## Sufficiency: full proof

Suppose Q is locally absolutely continuous and K_p(Q)<infinity. Write g=Q'>=0 a.e., w(t)=[t(1-t)]^(p/2). Choose nonnegative smooth compactly supported g_m with

 a_m^p=integral w(t)|g(t)-g_m(t)|^p dt ->0.

To justify the choice, first discard g outside [delta,1-delta]; the discarded weighted integral tends to zero. On this interval the weight is bounded above and away from zero, so the retained function is in ordinary L^p. Extend by zero to R and convolve with a nonnegative compactly supported smooth approximate identity of radius less than delta/2. The result is nonnegative and supported in [delta/2,1-delta/2], and approximates the truncation in ordinary L^p, hence also in weighted L^p since w is bounded above. A diagonal choice of delta and smoothing radius gives the assertion.

Define Q_m(t)=Q(1/2)+integral_(1/2)^t g_m(s)ds. The signed residual r_m=Q-Q_m has derivative g-g_m. Lemma 2 yields

 sup_n E||T_n Q-T_n Q_m||_p^p <= (5p)^p a_m^p,
 sup_n E||T_n Q-T_n Q_m||_p <= 5p a_m.                    (E)

For each fixed m, Lemma 3 gives T_n Q_m=>-g_m B. Set M_p=E|N(0,1)|^p. Brownian bridge marginal variances and Tonelli give

 E||gB||_p^p=M_p K_p(Q)<infinity,
 E||g_m B-gB||_p^p=M_p a_m^p.                            (G)

Thus -gB is a measurable L^p random element; measurability follows either from joint measurability and separability or from the L^p approximation by g_m B. For any bounded real 1-Lipschitz phi on L^p, the triangle inequality, (E), and (G) show

 limsup_n |E phi(T_n Q)-E phi(-gB)| <= (5p+M_p^(1/p))a_m.

The middle comparison of T_n Q_m with -g_m B tends to zero for fixed m. Let m tend to infinity. Bounded Lipschitz functions characterize weak convergence on separable L^p, so T_n Q=>-gB. Finally X_i=Q(U_i) has law P and its empirical quantile equals Q(V_n) a.e., since monotone transforms preserve sorting. Hence T_n Q has exactly the required empirical-process law. Lemma 1 supplied Q in L^p. Sufficiency is proved.

## Necessity: full proof

Suppose Z_n=sqrt(n)(Q_n-Q) converges weakly to Y in L^p. The empirical quantile has finitely many finite values and belongs to L^p; thus L^p-valuedness of Q_n-Q forces Q in L^p, hence in L^1. The inclusion i:L^p->L^1 is continuous, linear, and injective with norm at most one. Therefore i(Z_n)=>i(Y) in L^1. By (BK), Q is locally absolutely continuous, g=Q'>=0 a.e., J_1=integral sqrt(t(1-t))g(t)dt<infinity, and

 i(Y) has the L^1 law of -gB.                            (L)

We prove Gaussianity of Y in L^p before using any norm moments. For bounded measurable h, integral h(t)g(t)B(t)dt is a centered Gaussian real variable. Indeed Minkowski bounds its L^2 norm by integral |h|g sqrt(t(1-t))dt<infinity. Truncating to interior compact intervals converges in L^2 by this same bound. On each such interval g is in L^1; step approximations of the L^2-continuous process B, integrated against the deterministic integrable weight hg, converge in L^2. Each approximation is a finite linear combination of bridge values, hence centered Gaussian, and so is its limit. By (L), integral hY is centered Gaussian for every bounded h.

An arbitrary continuous linear functional on L^p is given by h in L^(p*) with p*=p/(p-1)<infinity. Bounded truncations h_k converge to h in L^(p*). Hölder gives

 |integral (h_k-h)Y| <= ||h_k-h||_(p*)||Y||_p ->0 a.s.

Each integral h_k Y is centered Gaussian. A distributional limit of centered Gaussians is centered Gaussian, possibly degenerate: tightness bounds their variances, every convergent subsequence of variances gives a Gaussian characteristic-function limit, and uniqueness of the distributional limit gives the result. Consequently every continuous linear functional of Y is centered Gaussian. Since L^p is separable, Y has a Gaussian Radon law. Fernique yields E||Y||_p^p<infinity.

The extended p-integral A(f)=integral |f|^p on L^1 is Borel measurable: it is the increasing limit of integrals min(|f|^p,K), which are continuous in L^1 because the truncated scalar function is globally Lipschitz. By (L), A(i(Y)) and A(-gB) have the same law. Tonelli now yields

 infinity > E||Y||_p^p = E integral |g(t)B(t)|^pdt
 = M_p integral [t(1-t)]^(p/2)|g(t)|^pdt.

Thus K_p(Q)<infinity. Necessity is proved. Sufficiency already identifies the limit, so no separate lifting-of-laws argument is required.

## Hostile-referee audit

1. Bounded moments do not imply tightness. The proof uses uniformly SMALL approximation errors (E) and a bounded-Lipschitz convergence argument.
2. A signed residual is not a quantile. The increasing absolute-derivative primitive in Lemma 2 permits the transport theorem to apply, with pathwise domination.
3. Atoms and flat segments are allowed. The auxiliary quantile identity and sorting identity were proved allowing ties; no reciprocal-density identity is used for arbitrary measures.
4. The fundamental theorem is used only on compact interior intervals. Moment finiteness is proved separately at endpoints; the original book convention is local AC.
5. Weak convergence does not imply convergence of norm moments. Necessity obtains moments of the LIMIT via Gaussianity and Fernique, not uniform integrability of Z_n.
6. Point evaluation is not continuous in L^p. Necessity uses integral functionals and the verified L^1 theorem.
7. The L^1 theorem alone cannot establish L^p sufficiency. The quantitative bound for signed residuals is essential.
8. Empirical processes are compared on the same sample, while Gaussian approximants use the same bridge. No strong approximation across n is asserted.
9. For p>2 the condition forces bounded Q, consistently with Lemma 1. The p=2 logarithmic boundary is retained; no compact-support assumption is used.
10. Theorem 5.3 rather than the survey's paraphrase of Corollary 5.10 supplies the required quantitative control. The new theorem is not claimed to have been found stated in print.

Remaining mathematical gap: none identified in the full proof, subject to the explicitly cited standard theorems. Numerical and Lean checks concern finite auxiliary steps only, not the infinite-dimensional theorem; their outcomes are recorded in CHECKS.md.
