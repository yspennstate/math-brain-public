# D0027 research record — 2026-10-11

## Exact question and conventions

FA-1f on Z has configuration space {0,1}^Z, infection state 0, infection parameter q in (0,1), and reversible product law pi with pi(eta_x=0)=q. Rate-one clocks refresh x to an independent pi spin only if a nearest neighbor is infected. The question is whether, for every initial probability law nu satisfying nu(eta=1 throughout [-l,l]) <= C exp(-kappa l) for all sufficiently large integer l, every local real observable f satisfies |nu P_t f-pi f| <= C_f exp(-c_f t).

The source's wording 'all q>0' is interpreted within its model domain (0,1). No translation invariance, independence, uniform gap bound over translated intervals, or absolute continuity is assumed. A deterministic single infection at the origin satisfies the hypothesis with zero gap probability for every l>=0.

## Audit of prior attempt D0027-A001

The prior intake record claims that subexponential finite-volume mixing times T(l,q)<=exp(o(l)) would imply exponential relaxation by choosing l of order t. This implication is invalid: a typical bound exp(-t/T(l,q)) has a nonconstant rate when T grows with l. For example T(l)=l^2 is subexponential and gives exp(-t/l^2), which does not decay for l proportional to t. Choosing l to balance exp(-kappa l) and exp(-t/l^2) gives only an exponent of order t^(1/3). This does not disprove the conjecture; it invalidates that proposed route to its resolution. Finite-volume spectral relaxation, worst-state mixing, and comparison to the infinite-volume process also must be distinguished.

## Current direction

Use finite propagation and the positive equilibrium spectral gap to obtain a fully quantified sufficient condition in terms of finite-window L2 densities. This condition is stronger than the conjecture's infection-gap condition. The single-infection law is a required stress test, not an established case.

## Theorem A: finite-window density criterion (proved special case)

Write p=1-q, B_r=[-r,r] intersect Z, and nu_r, pi_r for the marginals on B_r. Since pi_r has full support, set

    H(r) = (1/2) log(sum_z nu_r(z)^2 / pi_r(z)).

Let lambda>0 be an equilibrium L2 spectral-gap constant for FA-1f, so for every g in L2(pi) with pi(g)=0,

    ||P_t g||_2 <= exp(-lambda t) ||g||_2.                 (A1)

The positivity of this constant for fixed q in (0,1) is an established equilibrium theorem, not a new result of this attempt: N. Cancrini, F. Martinelli, C. Roberto and C. Toninelli, *Kinetically constrained spin models*, arXiv:math/0610106v1, Theorem 6.3, PDF p. 20. Its precise statement is quoted in LITERATURE.md. It also follows from the established positive spectral gap of East (ibid., Theorem 6.1, PDF p. 18): c_E(x)=1-eta_(x-1) <= c_FA(x), hence D_E(g)<=D_FA(g); East's Poincare inequality transfers directly. The pointwise Boolean comparison is in ConstraintChecks.lean and passed the Lean kernel check. The passage from Poincare to (A1) follows by differentiating ||P_t g||_2^2 on the generator domain, obtaining its derivative <= -2 lambda ||P_t g||_2^2, then approximation or the spectral theorem for arbitrary L2 functions.

If H(r)=o(r), then for every local f there are C_f,c>0 with

    |nu P_t f - pi(f)| <= C_f exp(-c t),  t>=0.          (A2)

More quantitatively, if H(r)<=K+theta r for all r>=0 and some theta>=0, then any v>2e with theta*v<lambda gives

    |nu P_t f-pi(f)|
      <= 2 ||f||_infty |S| exp(-(v-2e)t)
         + sqrt(Var_pi(f)) exp(K+theta(m+1))
                             exp(-(lambda-theta*v)t), (A3)

where S is any nonempty finite support for f and m=max{|x|:x in S}. A constant observable has zero error.

### Proof of finite propagation, including its uniformity

Couple two copies by the same rate-one site clocks and the same refresh coins. Suppose their configurations initially agree on B_r and S subset B_m, r>=m. A disagreement can first be created at a site only at its clock ring and only if a nearest neighbor already disagrees: if the site's old spins and both neighbors agree, both constraint decisions and refreshed spins agree. Trace each newly created disagreement backward through a disagreeing neighbor, stopping at an initial disagreement. If a disagreement persists through clock rings, trace back to its creation rather than treating persistence as a new step. Thus a disagreement on S at time t requires a nearest-neighbor spatial path starting in S with n>=r-m clock rings at strictly ordered times in [0,t]. Using r-m rather than the sharper r+1-m is harmless.

For a prescribed spatial path of n ring sites, the expected number of ordered ring tuples is t^n/n!, even when sites repeat: this is the factorial moment identity for independent rate-one Poisson processes, with strictly ordered times. There are at most |S|*2^n such paths. Markov's inequality and a union bound give

    P(disagreement somewhere on S at t)
      <= |S| sum_(n>=r-m) (2t)^n/n!
      <= |S| exp(2e*t-(r-m)).                          (A4)

The second inequality multiplies each term by exp(n-(r-m))>=1 and then sums the full exponential series. For r=m the n=0 contribution simply makes this a trivial upper bound. Infinite backward chains cannot invalidate the construction: for fixed t the tail sum of (2t)^n/n! tends to zero as n tends to infinity. Equivalently, first do the construction in finite boxes, then pass to the graphical infinite-volume limit using this same bound. This bound does not use attractiveness, infection density, or any property of the initial law.

### Proof of Theorem A

For each r define mu^(r)=nu_r tensor pi_(Z outside B_r). Its global density relative to pi is h_r(eta)=nu_r(eta_B_r)/pi_r(eta_B_r), and ||h_r||_2=exp(H(r)). Couple an initial sample from nu with one from mu^(r) so that they agree on B_r: retain nu's inside spins and replace all outside spins by fresh independent equilibrium spins. Applying (A4) to this coupling,

    |nu P_t f-mu^(r)P_t f|
      <= 2||f||_infty |S| exp(2e*t-(r-m)).              (A5)

Let g=f-pi(f). Cauchy-Schwarz and (A1) imply

    |mu^(r)P_t f-pi(f)|
      = |pi(h_r P_t g)|
      <= exp(H(r)-lambda t) sqrt(Var_pi(f)).            (A6)

Take r=m+ceil(vt), so r-m>=vt and r<=m+vt+1. Combining (A5) and (A6) proves (A3). If H(r)=o(r), take v=6>2e and theta=lambda/12. There is a finite K such that H(r)<=K+theta r for every integer r: absorb the finitely many exceptional radii into K. Then lambda-theta*v=lambda/2>0 and v-2e>0; (A2) follows with c=min(lambda/2,6-2e). This proves the statement for all t>=0, not just for an asymptotic subsequence. QED.

### Theorem A's hypothesis implies the conjecture's gap hypothesis

Apply Cauchy-Schwarz to the event E_r={eta=1 on B_r}:

    nu(E_r) <= exp(H(r)) sqrt(pi(E_r))
            = exp(H(r)) p^((2r+1)/2).                  (A7)

With a=-log(p)>0 and H(r)=o(r), the right side is <=exp(-a*r/2) for all sufficiently large r. Thus Theorem A really proves a subclass of D0027. It does not assume a different gap definition.

## Corollary B: sparse deterministic pinning, including globally singular laws

Let T subset Z be deterministic with k(r)=|T intersect B_r|=o(r). Fix arbitrary spins a_x in {0,1} for x in T; on Z outside T take independent equilibrium spins. The resulting product law nu satisfies exponential relaxation for every local observable and every q in (0,1).

Proof. Let w_x=q if a_x=0 and w_x=p if a_x=1. Its B_r density is

    h_r = product_(x in T intersect B_r) 1_{eta_x=a_x}/w_x.

Independence gives ||h_r||_2^2=product_(x in T intersect B_r) 1/w_x. Consequently

    H(r)=(1/2) sum_(x in T intersect B_r) log(1/w_x)
        <= (k(r)/2) log(1/min(p,q))=o(r).

Apply Theorem A. QED. In particular all-healthy pins on an infinite zero-density set are allowed. Such a law need not admit any global density: if T is infinite, pi(all pins match)=0, since each additional pin has matching probability at most max(p,q)<1, whereas nu assigns this event probability one. This establishes global singularity directly and explains why the global L2-density special case does not cover it.

An explicit example is T={plus or minus 2^j:j>=0}, pinned healthy. Here k(r)=O(log(r+2)). Its exact infection-gap probability is p^(2r+1-k(r)), so it also satisfies the original gap condition directly.

## Stress test and exact obstruction to this proof

For the deterministic configuration with a single infection at 0 and all other sites healthy,

    H(r)=(1/2) log(1/(q*p^(2r)))
        = -r log(p) -(1/2)log(q).

It satisfies D0027's hypothesis, yet H(r) is linear rather than sublinear. Formula (A3) only yields a rate if a propagation speed v>2e can be chosen with (-log p)*v<lambda. This proof establishes no such inequality for general q. Linear H is a failure of the sufficient hypothesis, not a counterexample to the conjecture.

There is a proved low-q obstruction to this particular bound. Theorem 6.4 of Cancrini et al., PDF p. 20, gives gap_FA(q)<=C*q^3 in dimension one, for an absolute C. Any usable lambda in (A1) is at most that spectral gap, while -log(1-q)>=q. Thus for every v>2e and every sufficiently small q,

    lambda-v*(-log(1-q)) <= C*q^3-2e*q < 0.

The L2/clock-path proof therefore cannot establish exponential relaxation of the single-infection law at small q even with the optimal equilibrium spectral-gap constant. A genuinely different nonequilibrium estimate is necessary to fill that case. This is an obstruction to the displayed proof method, not to other uses of spectral information.

Nor can one substitute a BABP result: its refresh rate when both neighbors are infected is 2, while FA-1f's is 1. Although D_FA<=D_BABP<=2 D_FA, this compares equilibrium quadratic forms, not arbitrary-start expectations or their convergence rates.

## Hostile-referee checklist

1. Quantifiers: Theorem A covers every local f and all q in (0,1), with constants permitted to depend on q, nu, and f. Its initial-law assumption is explicitly stronger than D0027.
2. Non-attractiveness: only equal-configuration graphical propagation is used. No ordered coupling or stochastic domination is claimed.
3. Density: only finite marginals are used; mu^(r) is allowed to depend on t. (A6) is applied separately at each t, so this dependence is legitimate.
4. Repeated clock sites: use Poisson factorial moments, not independence of repeat visits.
5. Propagation path indexing: the relaxed threshold r-m is safely smaller than the number of necessary steps; extra counted paths only weaken the bound.
6. Sparse pins: the exact density norm is checked by finite rational enumeration in checks.py. Singular-law assertion uses continuity from above of the finite pin events.
7. Spectral input: established positive equilibrium gap is required. It alone does not control deterministic single-infection initial data after the finite propagation cost.
8. Main missing step: obtain a local relaxation estimate for arbitrary configurations with a nearby infection, strong enough to integrate against the centered exponential gap tail. Neither Theorem A nor the cited span-growth theorem supplies it.

## Lemma C: exact quantitative integration of a deterministic estimate

For eta containing an infection, let R(eta)=min{|x|:eta_x=0}. Suppose, for a fixed q and local f, that constants A,c>0 and b>=0 satisfy the still-unproved uniform estimate

    |P_t f(eta)-pi(f)| <= A exp(b R(eta)-c t)          (C1)

for every such eta and t>=0. Then every initial law in D0027 satisfies exponential relaxation with rate c*kappa/(b+kappa).

Proof. The events {R>n} are exactly the no-infection events on B_n. Increase C so nu(R>n)<=C exp(-kappa n) for every integer n>=0. Also nu(R=infinity)=0 by continuity from above. For n>=0 split the integral at R<=n and use (C1) on this event and |P_t f-pi(f)|<=2||f||_infty on its complement. The triangle inequality gives

    |nu P_t f-pi(f)|
      <= A exp(b n-c t)+2||f||_infty C exp(-kappa n).

Take a=c/(b+kappa)>0 and n=floor(a t). Since n<=a t and n>=a t-1, the bound becomes

    |nu P_t f-pi(f)|
      <= (A+2||f||_infty C exp(kappa))
                    exp(-c*kappa*t/(b+kappa)).        (C2)

This handles b=0 as well. QED. Unlike the old subexponential mixing-time assertion, this reduction has a genuine constant exponential rate. The assumption (C1) is not proved here. Pointwise exponential relaxation with uncontrolled eta-dependent constants would not justify it.

## Explicit finite obstruction to attractiveness

Use infection coordinates xi_x=1-eta_x. Consider xi=(0,1,0) and zeta=(1,1,0) at sites -1,0,1, with every other site healthy, so xi<=zeta coordinatewise. For the increasing function g(xi)=xi_0, initially g(xi)=g(zeta)=1. The central infected spin is isolated under xi, giving Lg(xi)=0. Under zeta it has an infected neighbor and heals at rate p, giving Lg(zeta)=-p<0. The derivative at t=0 of P_t g(zeta)-P_t g(xi) is -p. Therefore P_t g(zeta)<P_t g(xi) for sufficiently small t>0: the semigroup is not attractive. Locality makes these derivatives well-defined in infinite volume. This explains exactly why adding infections cannot be used to dominate deterministic starts.

## Earlier six-run handoff read and limitations checked

Read origin/master's three D0027 files without modifying the checkout; local copies are prior_repo_0.md through prior_repo_2.md. The September 17 handoff contains a neighbor-refresh finite-set duality and a Q/BABP energy comparison. These are leads, not certified inputs to Theorem A. The handoff itself leaves even singleton dual local relaxation unresolved. Its shield and regeneration constructions do not supply a quantitative version of (C1). This attempt uses a different, finite-window density sufficient condition and does not claim to complete those routes.

## Proposition D: the pure-infection endpoint q=1

Although the main model domain in the source's introduction is (0,1), its graphical rule extends to q=1. At this endpoint the exact initial-law hypothesis of D0027 suffices for exponential relaxation to the all-infected configuration.

Proof. Infection never heals. Choose finite nonempty support S for f and m=max{|y|:y in S}. On the event that B_r contains an infection, choose one initial infected vertex x in B_r by a deterministic rule. For any y in S, follow the straight nearest-neighbor path from x to y of length d<=r+m. Wait for each next vertex's first clock after the preceding vertex has become infected by this prescribed path. These waiting times are independent Exp(1), conditional on the initial configuration, by independence and the Poisson strong Markov property. Every such ring is legal and infects its vertex; any infections produced elsewhere only shorten the actual hitting time. Thus for s=1/2,

    P(y still healthy at t | initial configuration with a zero in B_r)
      <= P(Gamma(d,1)>t) <= exp(-t/2) 2^d.

If d=0 the failure probability is zero and the displayed upper bound is still valid. Take r=floor(t/2)-m for t>=2m. Then r>=0, r+m<=t/2, and the union bound gives

    P(some y in S still healthy at t)
      <= C exp(-kappa r)+|S| exp(-(1-log(2))*t/2)
      <= C exp(kappa(m+1)) exp(-kappa*t/2)
         + |S| exp(-(1-log(2))*t/2).

As in Lemma C, enlarge C to make the gap bound valid at every r>=0. Since pi_1 is the point mass at all-infected, the expectation error is at most twice ||f||_infty times this failure probability. Increase the final prefactor to cover 0<=t<2m. This proves exponential convergence at rate min(kappa/2,(1-log(2))/2)>0. QED. This endpoint argument depends on irreversibility of infection and does not extend to q<1.

At q=0 the conjectured conclusion would fail: a single isolated infection remains forever, so the local observable eta_0 stays zero while pi_0(eta_0)=1. The gap hypothesis holds for that initial state. This is only an excluded-endpoint check, not a counterexample to D0027.

## Verification outcomes

- checks.py completed with exact Fraction arithmetic: all 1089 pinning-norm and gap-probability identities passed (checks.json).
- From ~/lean_verify, ran `lake env lean ~/brain_workers/TRIO_1011/op/D0027/ConstraintChecks.lean` with a 3600-second subprocess timeout. It completed with exit code 0 in 692.924 seconds, including shared-machine waiting. The file imports only Mathlib.Data.Bool.Basic; its four elementary finite theorems use `decide +kernel`, with no sorry and no native_decide. Output is lean_check.txt. This certifies the Boolean constraint comparison and constraint evaluations, not the infinite-volume probabilistic theorem.
- No claim of novelty is made for the finite-window sufficient condition; its purpose here is a fully checked partial result and a precise diagnosis of why it does not close D0027.

## User-requested additional attempt

The precise original gap was reread and queried in the math store. Two new approaches and full proofs from the chosen tensor-conjugacy approach are recorded in FOLLOWUP.md. Theorems F?H classify all locally Markov two-state tensor conjugacies and exclude even site-dependent tensor conjugacies to parity-preserving operators on cycles n>=5. Corollary I also excludes transpose-duality to parity chains with positive product equilibrium. A BABP positive control recovers its DFP mechanism. These are method-obstruction results; none resolves the deterministic local-forgetting gap or the full conjecture. Exact algebraic checks and a new Lean file accompany the follow-up.

The follow-up also proves the full homogeneous global Markov-conjugacy classification (Theorem K), ruling out cancellation as an escape, and rejects domain-wall-only lumping by a same-fiber generator calculation. The geometric alternative yields a compensated-midpoint martingale with explicit exponential tails (Lemma L); the time-integrated edge imbalance remains unbounded at the required scale. Midpoint rate formulas passed 381 exact cases. These results sharpen two approaches without proving the main conjecture.

Final follow-up verification: TensorObstruction.lean passed the kernel check, exit 0 (2317.851 seconds on the shared machine). FOLLOWUP.md contains the complete statements, proofs, hostile-referee audit, computational outcomes and remaining gaps. The follow-up verdict is PARTIAL; the full conjecture remains undecided by this work.
