# E0112 — source correction and rigorous partial results

Date: 2026-10-11. Verdict: PARTIAL, not a solution of Conjecture 4.3.2.

## 1. Objects and the exact question

Fix d>=1, nu>0 and r>0. Write gamma_d for unit-ball volume, R=r gamma_d^(-1/d), U=B(0,R), and v0=|U|=r^d. The environment omega is a Poisson random measure on (0,infinity) x R^d with intensity nu ds dx. Brownian motion has generator (1/2)Delta. For a path B let V_t(B)={(s,x):0<s<=t, x-B_s in U}. Put lambda=exp(beta)-1 and c=nu v0 lambda.

Let E denote environment expectation, P path expectation, and rho_t(x) the Brownian heat kernel. Define

    W_t = P exp{beta omega(V_t)-ct},
    U_t(x) = P_bridge(0 -> x at time t) exp{beta omega(V_t)-ct},
    a_t = E sqrt(U_t(0)),  b_t = E sqrt(W_t).

The source's W_t^{dir,xi} is U_t(t xi). These are annealed-mean-one random variables. Unlike W_t, the family U_t(t xi) is NOT asserted to be a martingale.

The negative critical point is inf{beta<=0: lim_t a_t>0}, NOT the intake's inf over beta>=0. Under the intake definition the latter infimum is always zero, since beta=0 gives U_t=1. This observation corrects the transcription; it is not a counterexample to the source conjecture.

The TeX source resolves bars lost by PDF extraction: the conjectured equality is overline(beta)_c^±=overline(beta)_c^{±,dir}. These are the weak-disorder thresholds, not section 2's unbarred free-energy thresholds. Write B^± for the weak-disorder thresholds and D^± for the directional half-moment thresholds. The exact first conjecture is D^±=B^±. The second conjecture asks for the local limit theorem throughout weak disorder. The displayed preliminary interval in the TeX uses an unbarred upper beta_c; this weaker bound must not be confused with the barred equality being conjectured.

## 2. Shear invariance and the necessary direction (proved)

For every t>0 and x, U_t(x) has the same distribution as U_t(0). Indeed B_s-(s/t)x is a zero-endpoint Brownian bridge. Replacing omega by its pushforward under the inverse shear (s,y)->(s,y-(s/t)x) preserves the intensity nu ds dy (Jacobian one) and the Poisson law. This replacement sends the tube of the original bridge to the tube of the zero-endpoint bridge, with the same normalization. The sign convention on the pushforward is immaterial to invariance but must be reversed consistently. Thus direction xi has no effect on a_t.

Disintegration of Wiener measure by its endpoint gives, almost surely,

    W_t = integral rho_t(x) U_t(x) dx.

All integrands are nonnegative. Jensen for the probability measure rho_t(x)dx and then Tonelli give

    b_t >= integral rho_t(x) E sqrt(U_t(x)) dx = a_t.       (2.1)

For completeness, b_t -> E sqrt(W_infinity): W_t is the source's mean-one nonnegative martingale, so W_t -> W_infinity almost surely. Also

    E[sqrt(W_t) 1{sqrt(W_t)>K}] <= E[W_t]/K = 1/K.

Hence sqrt(W_t) is uniformly integrable. Truncation and bounded convergence prove convergence of its expectations. If W_infinity=0 almost surely then (2.1) proves a_t ->0, including existence of this limit. If liminf a_t>0 then E sqrt(W_infinity)>0, so W_infinity is nonzero with positive probability; the source's zero-one theorem 3.1.1 implies weak disorder. In particular D^+<=B^+ and D^->=B^- whenever D is defined using existing positive limits.

This is only one direction. Jensen cannot be reversed with a time-uniform constant.

## 3. The half-moment identity in the L2 region (proved using a stated theorem)

We use the finite-window version of the source's Theorem 4.3.1, attributed to Vargas (2006), Theorem 2.9. In the source's L2 regime, for x=0 and any ell_t -> infinity with ell_t=o(t^alpha), alpha<1/2,

    U_t(0) = W_ell_t(omega) W_ell_t(theta_reverse(t,0) omega) + delta_t,
    E |delta_t|^2 ->0.                                   (3.1)

Here U denotes the normalized bridge partition function; the source changes its Z notation in this statement, so normalization is explicit here. Taking ell_t=t^(1/4) makes the two factors depend on disjoint time windows (0,ell_t] and [t-ell_t,t), for all sufficiently large t. The Poisson environment has independent restrictions on disjoint time slabs, and time reversal plus spatial reflection preserves its law. Therefore these two factors are independent and each has the law of W_ell_t. Boundary times have no Poisson points almost surely and cause no overlap issue.

For nonnegative z,y,

    |sqrt(z)-sqrt(y)|^2 <= |z-y|.

For example, if z>=y the assertion follows from sqrt(z)>=sqrt(y) and y<=sqrt(zy); interchange z and y in the other case. This algebraic step is formalized in OverlapChecks.lean. Cauchy-Schwarz twice gives

    |E sqrt(U_t(0)) - E sqrt(W_ell_t W_ell_t reversed)|
       <= (E |delta_t|)^(1/2) <= (E |delta_t|^2)^(1/4) ->0.

Independence gives E sqrt(product)=b_ell_t^2. Section 2 proves b_ell_t -> E sqrt(W_infinity). Consequently

    lim_t E sqrt(U_t(t xi)) = (E sqrt(W_infinity))^2 >0    (3.2)

for every fixed xi and every beta in the open L2 regime. Positivity follows either from the source's L2 weak-disorder conclusion or from L2 convergence, E W_infinity=1, and its zero-one law.

This is a proved special case, not novel resolution of the conjecture. The same proof needs only E|delta_t| ->0, rather than the L2 error in (3.1). Endpoint critical membership is not required for equality of the suprema/infima, but existing positive half-moment limits in the interior are required.

### 3a. A weaker sufficient factorization hypothesis (proved)

In fact finite-window factorization in probability suffices; no L1 error bound is needed. Suppose ell_t->infinity, 2ell_t<t eventually, and

    U_t(0) - Y_t ->0 in environment probability,
    Y_t = W_ell_t(omega) W_ell_t(theta_reverse(t,0) omega).

Disjoint windows give E Y_t=1 and E sqrt(Y_t)=b_ell_t^2. Also E U_t(0)=1. For eta>0 put A_t={|U_t(0)-Y_t|>eta^2}. On its complement the square-root inequality gives |sqrt(U_t)-sqrt(Y_t)|<=eta. On A_t use the triangle inequality and Cauchy-Schwarz separately for the two square roots. This yields

    E|sqrt(U_t)-sqrt(Y_t)| <= eta + 2 sqrt(P(A_t)).

For each fixed eta the probability tends to zero, so the limsup of the left side is at most eta. Let eta decrease to zero. This proves the same identity (3.2). Therefore proving this weaker finite-window factorization throughout the interior of weak disorder would already prove D^±=B^±. This conditional implication is complete; its premise is the remaining analytical gap.

## 4. Exact two-replica formula (proved)

Define v(z)=|U intersect (U+z)|. Take two independent paths under either Wiener measure or the same bridge measure. For their deterministic tubes A,C, the Poisson Laplace functional gives

    E exp{beta omega(A)+beta omega(C)-2ct}
      = exp{nu lambda^2 |A intersect C|}.

To verify the coefficient, on A intersect C the exponent in the uncompensated functional is exp(2beta)-1; subtracting the two individual contributions 2(exp(beta)-1) leaves (exp(beta)-1)^2. Outside the intersection the individual terms cancel exactly. Both tubes have measure v0 t. All exponentials are nonnegative, so Tonelli interchanges path and environment integrals without an integrability assumption.

Thus, with q=nu(exp(beta)-1)^2,

    E W_t^2 = E_D exp{q integral_0^t v(D_s)ds},            (4.1)
    E U_t(x)^2 = E_D_bridge(0->0) exp{q integral_0^t v(D_s)ds}. (4.2)

The difference D of two independent Brownian motions has generator Delta, not (1/2)Delta. The difference of two independent bridges to the same endpoint is a bridge of this diffusion from zero to zero. Its covariance is 2(s wedge u-su/t)I, independent of x. The cancellation algebra is formalized in OverlapChecks.lean.

## 5. An explicit sufficient L2 condition (proved)

For d>=3 let

    K = sup_z E_z integral_0^infinity v(D_s)ds.

We calculate K exactly. The Green density for generator Delta is

    G(z)= |z|^(2-d) / ((d-2)d gamma_d).

This constant follows by integrating (4 pi s)^(-d/2) exp(-|z|^2/(4s)) in s, or by its flux through a sphere. The function v=1_U*1_U is radial nonincreasing: its value at distance h<=2R is twice the volume of a spherical cap cut at h/2, and it is zero for h>2R. Convolution with a radial nonincreasing kernel is maximal at zero. Here is a justification avoiding a rearrangement assumption: layer-cake represents each function by nonnegative integrals of concentric-ball indicators. For two balls their intersection volume after a translation is at most the volume of the smaller ball; at zero translation that volume is attained. Tonelli then proves (v*G)(z)<=(v*G)(0), also for the singular, nonintegrable-at-infinity G by truncation or directly by its ball level sets.

To evaluate the value at zero, let H(x)=integral_U G(x-y)dy. On |x|<=R this potential satisfies

    H(x)=R^2/[2(d-2)] - |x|^2/(2d).                       (5.1)

A full verification: the exterior radial harmonic function decaying at infinity is A |x|^(2-d). Inside, -Delta H=1 requires C-|x|^2/(2d). Matching derivative at R gives A=R^d/[d(d-2)]. Matching value gives C=R^2/[2(d-2)]. These formulas define a C1 function, solve -Delta H=1_U distributionally without a boundary delta term, and decay at infinity. The convolution G*1_U is another such function. Their difference is distributionally harmonic on all R^d, hence smooth harmonic; it is bounded and decays at infinity. The mean-value property (or maximum principle on growing balls) forces the difference to zero. This proves (5.1).

Finally integral_U |x|^2 dx = d gamma_d R^(d+2)/(d+2), by polar integration. Fubini and v=1_U*1_U now give

    K = integral_U H(x)dx
      = 2 gamma_d R^(d+2)/[(d-2)(d+2)]
      = 2 r^(d+2) gamma_d^(-2/d)/[(d-2)(d+2)].            (5.2)

If qK<1 then sup_t E W_t^2 <= 1/(1-qK). Proof: put I_t=integral_0^t v(D_s)ds. For n>=1,

    E_z[I_t^n/n!] = integral_{0<s1<...<sn<t} E_z product_i v(D_si) ds.

The Markov property at s1 and induction bound this integral by K^n uniformly over z,t: the remaining n-1 ordered integrals are at most K^(n-1), and the first integrated factor has expectation at most K. For n=0 the value is one. Expand the exponential by monotone convergence and sum the geometric series. This proves the asserted estimate through (4.1). L2 boundedness makes the martingale L2 convergent with E W_infinity=1; hence it is weak disorder and (3.2) applies in the strict L2 range.

For example d=3,R=1 gives K=8pi/15. With nu=1 the sufficient condition is |exp(beta)-1|<sqrt(15/(8pi)). This supplies a concrete nonempty interval on both sign branches. It is a sufficient bound, not the true critical temperature.

### 5a. Equality of the entire negative branch at sufficiently low intensity (proved)

If d>=3 and nu K<=1, then for every finite beta<=0 one has (exp(beta)-1)^2<1, and hence qK=nu K(exp(beta)-1)^2<1. Section 5 puts every such beta strictly inside the L2 region; section 3 proves its directional half-moment limit is positive. Consequently both negative weak-disorder critical parameters are -infinity:

    B^- = D^- = -infinity, when nu K<=1.                  (5.3)

This proves one whole sign branch of the threshold equality under an additional explicit low-intensity hypothesis. For d=3,R=1 that hypothesis is nu<=15/(8pi). It is not a result at beta=-infinity itself: the definitions take an infimum over finite beta, and no zero-temperature assertion is needed.

## 6. A direct bridge bound (proved, weaker sufficient range)

Time reversal of a zero-endpoint D bridge interchanges I_first=integral_0^(t/2) v(D_s)ds and I_last=integral_(t/2)^t v(D_s)ds. Cauchy-Schwarz and identical marginals give

    E_bridge exp(q(I_first+I_last)) <= E_bridge exp(2q I_first).

For any nonnegative functional F of D up to t/2, the bridge density relative to the unconditioned diffusion is

    E_bridge F = E_0[F p_(t/2)(D_(t/2))/p_t(0)] <= 2^(d/2) E_0 F,

since p_s(z)=(4pi s)^(-d/2) exp(-|z|^2/(4s)). Therefore when 2qK<1,

    sup_t E U_t(x)^2 <= 2^(d/2)/(1-2qK) = M.              (6.1)

The bounds are justified first for bounded exponentials and then by monotone convergence; (5.2) supplies finiteness on the right. This proof uses no local limit theorem.

For a nonnegative mean-one X with E X^2<=M, Holder applied to X=(X^(1/2))^(2/3)(X^2)^(1/3) with exponents 3/2 and 3 gives

    1 <= (E sqrt(X))^(2/3) (E X^2)^(1/3),
    E sqrt(X) >= M^(-1/2).

Taking X=U_t(x), (6.1) proves a uniform positive lower half-moment bound. This alone is a liminf result; it does not prove existence of lim_t a_t. In this parameter range existence follows separately from section 3 because 2qK<1 implies qK<1.

## 7. Referee audit and precise remaining gaps

1. Sign error: corrected beta<=0 from the actual source. No claim equates positive and negative critical values.
2. Threshold notation: TeX confirms the conjectured equality uses barred weak-disorder thresholds. Directional free-energy equality (4.2.11) does not identify half-moment thresholds.
3. Nonmartingale issue: only W_t is used as a martingale. No almost-sure limit of U_t is assumed.
4. Normalization: all bridge statements include exp(-ct); without it the source local-limit factorization would be false already in annealed mean.
5. Reversal dependence: W_infinity and its reversal are not treated as independent. We use finite windows with 2ell_t<t, where independence is exact.
6. Boundary and dimension: beta=0 gives a_t=1 in every dimension. The Green bound requires d>=3. For d=1,2 and q>0, K is infinite: v is bounded below on a small ball, and the heat kernel on that ball is of order s^(-d/2) for large s, whose time integral diverges. This failure of the L2 bound is not a proof of strong disorder.
7. Direction: fixed ballistic endpoints t xi are handled by shear invariance at each t, not by applying a diffusive-endpoint estimate outside its stated range.
8. Main analytical gap: even finite-window factorization in probability (section 3a) for the Poisson Brownian model at beta in weak disorder outside L2 remains unproved here. Such factorization is enough; the stronger L1 local limit conjecture would suffice as well. General lattice results cannot simply be transferred: a time-slab kernel is random over a continuum of endpoints and has spatial dependencies induced by ball overlaps.
9. No literature theorem for a different environment or underlying path law is counted as proving this. The PDF extraction's missing bars were checked against source_ch-dir.tex; no additional free-energy equality is part of the corrected target.
10. Existence of the half-moment limit outside L2 in weak disorder is not established by the calculations here. In strong disorder the limit exists and is zero by (2.1).

No full proof or counterexample to the source conjecture has been obtained. The special cases above, the correction of the intake, and the conditional reduction are the result of this attempt.

## 8. Numerical checks (completed)

numerical_checks.py uses deterministic SciPy quadrature, not simulation of quenched partition functions. For d=3,R=1 it independently integrates the exact overlap v(h)=pi(4+h)(2-h)^2/12 on 0<=h<=2 against the Green density, giving K=1.6755160819145563, exactly matching 8pi/15 at displayed precision. The reported adaptive quadrature error is about 1.9e-14; it is not an interval-arithmetic certificate.

It also integrates expected overlap occupation for the free difference diffusion and its zero-endpoint bridge. At t=1000 these are 1.6506075006 and 3.3481619768, respectively. The latter is close to 2K=3.3510321638, consistent with contributions from both endpoints. This checks the diffusion covariance and warns against forgetting the final endpoint; it does not locate any critical beta.

A finite negative control shows the gap in reversing Jensen. On N cells choose a uniform index J and set U_i=N*1{J=i}. Each U_i has expectation one and the spatial average is exactly one, yet E sqrt(U_i)=1/sqrt(N). This is a proved finite exchangeable example, not a counterexample to a Poisson polymer conjecture. It demonstrates why mere spatial averaging, stationarity and mean-one normalization cannot prove the missing converse. numerical_results.json records N=1,4,100,10000.

## 9. Formal verification (passed)

OverlapChecks.lean imports only Mathlib.Analysis.SpecialFunctions.Sqrt, Mathlib.Tactic.Ring and Mathlib.Tactic.Linarith. Executed `lake env lean ~/brain_workers/TRIO_1011/op/E0112/OverlapChecks.lean` from ~/lean_verify, with a one-hour subprocess timeout, one Lean job at a time. Final exit code 0, elapsed 237.643 seconds. The Lean kernel checked the Poisson cancellation polynomial and the nonnegative square-root squared-error bound. No sorry, axioms introduced by this file, native_decide, or full Mathlib import. This does not formalize the stochastic proofs. The first attempt used the nonexistent Mathlib.Tactic.Nlinarith module; the import was corrected to Linarith, and the successful output is lean_check_final.log.

During the attempt, a second read-only math-store query, "Khasminski lemma Brownian exponential occupation Green function", returned generic Green-function and Markov-process definitions, not a theorem resolving the gap. The Green function and exponential bound were checked directly above.

Novelty and boundary caution: the survey already gives an unspecified sufficiently-low-density all-negative-temperature L2 regime. Section 5a supplies a direct explicit constant and includes the directional half-moment deduction; no novelty is claimed. Its d=1,2 zero-threshold remark relies partly on similar-model arguments and an unpublished reference; we did not reconstruct those arguments and therefore do not add an independently proved low-dimensional claim.

## 10. Second attempt (2026-10-11)

Reopened at user request. Full new proofs and the two untried approaches are in SECOND_ATTEMPT.md. The selected route conditions on endpoint slabs and then interpolates the middle Poisson intensity. It proves an all-temperature factorization for the BULK CONDITIONAL EXPECTATION, the universal bound limsup E sqrt(U_t)<=(E sqrt(W_infinity))^2, and an exact weighted pinned-overlap identity for the missing Hellinger deficit. The original U_t factorization and positive limit outside L2 are still not proved. The second route gives an exact Poisson thinning temperature identity and a counterexample to importing general Poisson Lp-to-Lq hypercontractivity. No counterexample to E0112 is claimed.

Second-attempt checks completed: exact finite Poisson interpolation on both sign branches agrees numerically, Gaussian joining bounds pass their finite checks, and DeficitChecks.lean passes kernel verification of two algebraic identities. The precise remaining sufficient input is a convergent pinned-overlap deficit delta<c=(E sqrt(W_infinity))^2 in weak disorder; vanishing of the weighted bulk overlap would prove the stronger full factorization identity. Neither input is established here. Final status DONE / PARTIAL.
