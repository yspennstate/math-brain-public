# F0021 — attempt, 2026-10-12

## Exact target and hypotheses
The source is Nikos Zygouras, *Directed polymers in a random environment: a review of the phase transitions*, arXiv:2401.01757, Question 5, PDF page 42. Its exact question is: “Derive the limiting behaviours in the rest of the phase diagram. Do Airy and KPZ asymptotics extend when γ = 0 and α > 5 ?”
We address only the fixed-temperature part. Let S be simple symmetric nearest-neighbour random walk on Z, S_0=0, and let omega_{i,x} be iid real disorder independent of S. Set

Z_n^beta = E_S exp(beta sum_{i=1}^n omega_{i,S_i}), beta>0 fixed.

Assumption 3, page 37, gives P(omega>t)=t^{-alpha}L(t), L slowly varying, and E omega=0, E omega^2=1 for alpha>2. Its additional left-tail comparison applies only for alpha<=2. We do NOT assume a comparable left tail when alpha>5. Alpha here is a right-tail exponent; a nondegenerate alpha-stable probability distribution with alpha>2 does not exist. The model is the exponential-weight polymer of Section 5.1, not the product-weight model of Section 5.2.

The goal would be a KPZ-scale limiting distribution with appropriate deterministic centering and nonuniversal constants, and Airy spatial process limits for a precisely specified endpoint geometry. The source question does not fix a single process topology or normalization. We do not resolve any of these full limits.

## Lemma 1: power envelope for the right tail (proved)
For each 0<q<alpha there exist C,T>0 with P(omega>t)<=C t^{-q} for t>=T.

Proof. Regular variation implies Fbar(2t)/Fbar(t) -> 2^{-alpha}<2^{-q}. Choose T so this ratio is at most 2^{-q} for all t>=T. For t>=T choose integer k>=0 with 2^k T<=t<2^{k+1}T. Monotonicity and iteration give Fbar(t)<=Fbar(2^k T)<=Fbar(T)2^{-qk}. Since t<2^{k+1}T, this is at most Fbar(T)(2T)^q t^{-q}. This proves the assertion (enlarge C if necessary).

## Proposition 2: no macroscopic single-site reward after quadratic travel cost (proved)
Let alpha>5 and beta>0. Define the nonnegative random variable

M_n = max(0, max_{1<=i<=n, |x|<=i, x=i mod 2} [beta omega_{i,x} - x^2/(2i)]).

Then M_n/n^{1/3} -> 0 in probability. More explicitly, for any 5<q<alpha, sufficiently large a and all n,

P(M_n>a) <= C beta^q [n a^{-q} + 2 sqrt(2) J_q n^{3/2} a^{1/2-q}],
J_q = integral_0^infty (1+y^2)^{-q} dy < infinity.

Proof. Use Lemma 1 at thresholds (a+x^2/(2i))/beta, all at least T once a>=beta T. A union bound, extended to every x in Z, gives
P(M_n>a)<=C beta^q sum_{i=1}^n sum_{x in Z}(a+x^2/(2i))^{-q}.
For a decreasing nonnegative function f on [0,infinity), sum_{k=1}^infty f(k)<=integral_0^infty f(t)dt, by integrating on [k-1,k]. Thus the inner sum is at most

a^{-q}+2 integral_0^infty(a+t^2/(2i))^{-q}dt
= a^{-q}+2 sqrt(2i) a^{1/2-q} J_q.

The integral J_q is finite because its integrand is at most 1 on [0,1] and at most y^{-2q} on [1,infinity), where 2q>1. Sum sqrt(i)<=n sqrt(n) to obtain the displayed bound. Substitute a=epsilon n^{1/3}. The two n-exponents are 1-q/3 and (5-q)/3, both strictly negative when q>5. This proves convergence for every epsilon>0. Independence is not needed for this upper bound.

This proposition concerns a single reward minus a bare-walk cost. It is NOT an upper bound on the centered full polymer free energy: a path collects many rewards and its other rewards are correlated with its optimizing route.

## Lemma 3: actual walk cost and correction of the earlier attempt (proved)
For simple symmetric random walk and any reachable x at time i,

P_S(S_i=x) <= exp(-x^2/(2i)).

Proof. For lambda>=0, E exp(lambda S_i)=(cosh lambda)^i<=exp(i lambda^2/2). To see the inequality, g(lambda)=lambda^2/2-log cosh lambda has g(0)=0 and derivative lambda-tanh lambda>=0: h(lambda)=lambda-tanh lambda starts at zero and has derivative tanh^2 lambda>=0. For x>=0, Markov's inequality applied to {S_i>=x}, with lambda=x/i, gives exp(-x^2/(2i)); the point event is a subset. Symmetry gives the negative x case, and x=0 is immediate.

If all disorder is zero except at one site (i,x), of value w, the exact point-to-line partition function is

Z_n = 1+p_i(x)(exp(beta w)-1), p_i(x)=P_S(S_i=x), i<=n.

Proof. Split paths by whether they visit that site. They receive weight exp(beta w) or 1 respectively. For w>=0, Lemma 3 gives

0 <= log Z_n <= log(1+exp(beta w-x^2/(2i)))
<= log 2 + max(0,beta w-x^2/(2i)).

The last inequality follows separately for a nonpositive and a nonnegative exponent. Proposition 2 consequently controls the supremum of the free-energy increase from any SINGLE spike inserted into the zero environment, divided by n^{1/3}. It does not compare insertion into a random polymer environment, whose visit probability need not be p_i(x).

The intake attempt F0021-A001 claimed the maximum among order n^2 cone sites costs O(1) to visit, and inferred a threshold 6. This is false. At (n,n) the probability is exactly 2^{-n}, so the cost is n log 2. At distance proportional to i even the quadratic upper bound incurs order i cost. The threshold 6 from counting the whole cone without travel cost does not refute the source's threshold 5.

## Proposition 4: truncation in a deterministic tube (proved)
Fix xi in (0,1), define D_n(xi)={(i,x):1<=i<=n, |x|<=min(i,ceil(n^xi)), x=i mod 2}, and cap omega above at T_n=n^kappa, kappa>0. If alpha kappa>1+xi then

P(any omega_{i,x}>T_n in D_n(xi)) -> 0.

Proof. The number of sites is at most n(2ceil(n^xi)+1)<=5 n^{1+xi}. Choose q<alpha with q kappa>1+xi, and apply Lemma 1 and a union bound. The probability is at most 5 C n^{1+xi-q kappa}, which tends to zero. On the complementary event, every path staying in this tube has exactly the same weight in the original and capped environments.

For xi=2/3+delta, choose 0<delta<min(1/3,(alpha-5)/3). Then (1+xi)/alpha<1/3, and one can choose (1+xi)/alpha<kappa<1/3. Thus the upper-tail cap is below the KPZ fluctuation scale and does not change any weights in this somewhat enlarged KPZ tube, with probability tending to one. This concerns positive tails only; it remains valid with precisely the source's left-tail hypotheses.

## Proposition 5: conditional transfer using original-polymer confinement (proved)
Let Z_n^T be the full partition function of the capped environment, R_n the original partition function restricted to paths that stay in D_n(xi), and Q_n=R_n/Z_n. Q_n is the quenched probability that the ORIGINAL polymer stays in the tube. It is strictly positive for every finite n (all weights are finite and some such paths exist). On the event of no capped site in the tube,

R_n <= Z_n^T <= Z_n,
0 <= log Z_n-log Z_n^T <= -log Q_n.

Proof. The first inequality follows by retaining only the tube paths in Z_n^T and using equality of their original and capped weights. The second follows from omega^T<=omega and beta>0. Divide by Z_n>0 and use monotonicity of log, which proves the displayed logarithmic bound.

Consequently if -log Q_n=o_P(n^{1/3}), then (log Z_n-log Z_n^T)/n^{1/3}->0 in probability. Indeed for epsilon>0 its probability of exceeding epsilon is bounded by the probability of any capped site in the tube plus P(-log Q_n>epsilon n^{1/3}), both tending to zero. The stronger Q_n->1 in probability suffices, but is unnecessary. Slutsky's theorem now transfers ANY distributional limit for (log Z_n^T-b_n)/(c n^{1/3}) to the original free energy, for deterministic b_n and fixed c>0. This is a conditional reduction, not a KPZ theorem.

Only ORIGINAL polymer confinement is required in this inequality. The capped model's confinement alone does not bound the additional mass contributed by uncapped sites outside the tube.

## Remaining gaps
Neither the required confinement estimate at xi just above 2/3 nor a KPZ/Airy limit for the n-dependent capped, generally nonintegrable disorder has been proved here. Capping at a diverging level is not an application of any fixed-distribution KPZ theorem, and no general such fixed-distribution theorem has been identified by the present search. The single-site bound does not handle optimized sums of many rewards or polymer visit probabilities in a random background. Left-tail truncation would require additional work because Assumption 3 imposes only variance on that side. These gaps prevent a proof or counterexample to Question 5.


## Corollary 6: an L1 version of the single-site bound (proved)
For 5<q<alpha there is a finite constant K (depending on q,beta and the disorder law) such that, for all sufficiently large n,

E M_n <= K n^{3/(2q-1)}.

In particular E[M_n/n^{1/3}] -> 0 for alpha>5.

Proof. Put r=3/(2q-1), a_0=n^r, which is eventually at least beta T. A nonnegative random variable satisfies E M_n=integral_0^infty P(M_n>a)da, by Tonelli's theorem applied to its indicator representation. Bound the integral below a_0 by a_0, and use Proposition 2 above a_0. Integration gives

E M_n <= a_0 + C beta^q n a_0^{1-q}/(q-1)
 + 2 sqrt(2) C beta^q J_q n^{3/2} a_0^{3/2-q}/(q-3/2).

Here q>5 makes both integrals converge. Divide by a_0. The first tail contribution is bounded uniformly because n a_0^{-q}=n^{1-3q/(2q-1)}<=1. The second is constant in n because n^{3/2}a_0^{1/2-q}=1. This proves the first assertion with an explicit finite K. Finally r<1/3 is equivalent to q>5, so division by n^{1/3} proves the second assertion. This is still a single-site statement, not an L1 statement about the polymer's centered free energy.

## Hostile referee audit
1. **Source identity.** Read pages 37 and 42 of arXiv:2401.01757v4 (49 pages, revision September 2024). Alpha>5 is not a typo introduced by the intake. Gaussian part is Theorem 5.2(ii), not Theorem 5.3(ii).
2. **Tail assumptions.** Only positive tails enter Lemma 1 and Propositions 2 and 4; no unjustified negative-tail comparison or exponential moment is used. The proof of Lemma 1 uses monotonicity of the tail and the dyadic regular-variation limit, rather than an unproved uniform bound on L.
3. **Union bound geometry.** Parity is respected in M_n; extending to all integers only enlarges the upper bound. Early times i=1,...,n are all included. The sum-integral estimate requires q>1/2; q>5 satisfies it. The growing threshold ensures Lemma 1 applies everywhere. No iid assertion is needed in this step.
4. **Meaning of travel cost.** The Chernoff cost controls the bare-walk probability. Random-polymer visit probabilities can be far larger; substituting the bare-walk probability for them would invalidate an argument for KPZ universality. The isolated-spike example explicitly has zero background.
5. **Exponent signs.** Both probability exponents are negative for q>5; the L1 exponent r<1/3 is likewise equivalent to q>5. At q=5 the second probability exponent is zero, so the proof intentionally yields no boundary claim.
6. **Confinement is not assumed as a conclusion.** Proposition 5 is explicitly conditional on the ORIGINAL polymer mass Q_n. No confinement theorem has been proved or silently imported. On the event of agreement in the tube, positivity and order of the three partition functions give the exact comparison. This inequality is meaningful even when Q_n is very small, as the finite test illustrates.
7. **No universality from capping.** Capping does not make the model integrable, and the n-dependent cutoff does not by itself put it under intermediate-temperature results. A fixed beta is essential to the unresolved target. An Airy process result would additionally require endpoint-dependent and spatially uniform estimates and tightness, not merely a scalar Slutsky argument.
8. **Computations.** `verify.py` uses one array at a time, with maximum array size 200001, and enumerates 1024 paths for n=10. It verifies the exact spike identity (maximum absolute error 4.55e-13), the partition comparison, 27 sum-integral comparisons, and the walk Chernoff bound over all reachable sites through time 1200. Total computation time recorded in CHECKS.json is approximately 1 second; no job approaches the 1 GB limit.
9. **Boundary exploration is not a proof.** CHECKS.json computes the exact finite product CDF for M_n in an iid, *uncentered* Pareto toy environment at n=64,256,1024,4096 and alpha=4,5,6. For alpha=6 the exceedance probability at n^{1/3} falls from 0.08795 to 0.02252; for alpha=5 it stays near 0.333; for alpha=4 it rises from 0.8455 to 0.9994. These are finite exact probabilities up to floating-point summation, not simulations of the full polymer, and not a proved limiting distribution. The constant listed as 'predicted' in CHECKS.json comes from a formal continuum Riemann-sum calculation, which is not used in a proof here.


## Proposition 7: full-cone truncation and the two distinct thresholds (proved)
Let C_n={(i,x):1<=i<=n, |x|<=i, x=i mod 2}. Its cardinality is N_n=sum_{i=1}^n(i+1)=n(n+3)/2.

(a) If alpha>6, choose 2/alpha<kappa<1/3. With probability tending to one, all weights in C_n are at most n^kappa, so the ORIGINAL and positively capped full partition functions are exactly equal. No confinement hypothesis is needed for this statement.

Proof. Choose q<alpha with q kappa>2. Lemma 1 and a union bound give P(any capped site)<=N_n C n^{-q kappa}<=2C n^{2-q kappa} for n>=1. The exponent is negative. On the complementary event every accessible site and hence every path weight is unchanged.

(b) If 5<alpha<6, let W_n=max_{(i,x) in C_n} omega_{i,x}. Then W_n/n^{1/3}->+infinity in probability, although M_n/n^{1/3}->0 in L1 by Corollary 6.

Proof. First show the lower power envelope: for q>alpha there exist c,T>0 with Fbar(t)>=c t^{-q} for t>=T. Regular variation gives Fbar(2t)/Fbar(t)>=2^{-q} eventually. Choose T with this property and Fbar(T)>0. For 2^k T<=t<2^{k+1}T, monotonicity and iteration yield
Fbar(t)>=Fbar(2^{k+1}T)>=Fbar(T)2^{-(k+1)q}>=Fbar(T)T^q 2^{-q} t^{-q}.
Choose alpha<q<6 and any fixed A>0. By independence,
P(W_n<=A n^{1/3})=(1-Fbar(A n^{1/3}))^{N_n}
<=exp(-N_n Fbar(A n^{1/3})).
The exponent in absolute value is at least (c/2) A^{-q}n^{2-q/3}->infinity. Thus this probability tends to zero for every A>0, which is the stated divergence. Corollary 6 independently supplies the assertion about M_n.

The number 6 marks when a GLOBAL cap below n^{1/3} can leave the entire reachable cone unchanged. The number 5 marks the single-site, entropy-corrected threshold and allows an unchanged somewhat enlarged KPZ tube. They answer different questions. Neither part establishes a limit for the full random-background polymer free energy.


## Example 8: capped-model confinement alone cannot justify transfer (proved logical obstruction)
This is a deterministic, n-dependent example, NOT an iid environment under Assumption 3 and NOT a counterexample to Question 5.
Fix beta>0, 1/2<xi<1, and 0<kappa<1/3. Set every accessible omega to zero except omega_{n,n}=n^2. Cap above at n^kappa. For sufficiently large n, (n,n) is outside the tube |x|<=ceil(n^xi). The unique path visiting (n,n) is the all-right path, with probability 2^{-n}. Consequently

Z_n=1+2^{-n}(exp(beta n^2)-1),
Z_n^T=1+2^{-n}(exp(beta n^kappa)-1)->1.

The tube-restricted partition function R_n is simply the bare walk's probability of staying in the tube. For each i<=n, the two-sided Chernoff bound gives P(|S_i|>ceil(n^xi))<=2 exp(-n^{2xi}/(2n)). A union bound over i shows 1-R_n<=2n exp(-n^{2xi-1}/2)->0. Thus the capped polymer's tube mass R_n/Z_n^T tends to one, whereas the original polymer's tube mass R_n/Z_n tends to zero. Moreover log Z_n is at least beta n^2-n log 2, and log Z_n^T tends to zero, so the difference is far larger than n^{1/3}. This illustrates precisely why confinement of only the capped model is insufficient for Proposition 5's application.


## Formal verification and assessment of the first attempt

`F0021.lean` passed Lean 4.33.1 / Mathlib, using only targeted imports (`Mathlib.Data.Real.Basic`, `Mathlib.Tactic.Linarith`, `Mathlib.Tactic.Positivity`). Command: `lake env lean ~/brain_workers/TRIO_1011/op/F0021/F0021.lean`, run from `~/lean_verify`, with a 3600-second timeout. Final exit code 0; elapsed 152.67 seconds. The file contains neither `sorry` nor `native_decide`. The four kernel-checked lemmas verify the union-bound exponent signs, the restricted-partition ratio inequality, the entropy-balanced exponent comparison with 1/3, and existence of the tube-cap exponent interval. They do not formalize the probability, regular variation, logarithm, or limiting-distribution arguments, whose complete handwritten proofs are above. The first run failed on a PowerShell-inserted UTF-8 BOM; that failure was corrected and is preserved separately in LEAN_INITIAL_CHECK.json and lean_initial_failure.txt.

**Final verdict: PARTIAL.** The fixed-temperature KPZ/Airy assertion has neither been proved nor refuted. The current attempt proves the entropy-corrected isolated-spike bound, including an L1 rate; tail truncation facts in tubes and in the full cone; the original-confinement conditional free-energy transfer; and the raw/penalized maximum distinction. It refutes the earlier attempt's constant bare-walk access-cost argument. No reviewed later theorem closes the exact question; OpenAlex could not be accessed successfully. A future attempt must prove original-polymer confinement on a somewhat enlarged KPZ tube and establish a KPZ law for the capped nonintegrable model (or find a different universality method); an Airy process additionally requires spatial uniformity and tightness. No part of the wider, unaddressed phase diagram is claimed solved.

## Additional serious attempt, 2026-10-12

The two new approaches, full proofs, and remaining gaps are in [SECOND_ATTEMPT.md](SECOND_ATTEMPT.md), with a separate [hostile referee report](SECOND_REFEREE.md).

The selected approach controls chains of many rare rewards using a lattice entropy count. For alpha>5 and 5/(3 alpha)<kappa<1/3, the polymer made only of weights above n^kappa, with all other weights set to zero, has Z_tail-1<=exp(-n^(1/3)/4) with probability tending to one. Its quenched path law consequently tends to the bare-walk law in total variation. This stronger special case does not silently assume the original polymer's confinement.

The growing-temperature version of that result and a finite Holder/relative-entropy comparison also give a bound for the actual original polymer. For every 0<r<(alpha-5)/(3 alpha), one can choose 5/(3 alpha)<kappa<1/3-r so that, with probability tending to one,

0 <= log Z_n(omega)-log Z_n(min(omega,n^kappa))
  <= (n log 2+exp(-n^(1/3)/4))/(1+n^r).

Thus a sublinear truncation comparison is now proved without a confinement hypothesis. The required o_P(n^(1/3)) comparison is still unproved. The displayed bound has scale n^(1-r), much larger than n^(1/3); a generic capped-model KPZ/Airy theorem is also still missing. Neither a full answer nor a counterexample to F0021 is claimed. The latest verdict remains PARTIAL.
