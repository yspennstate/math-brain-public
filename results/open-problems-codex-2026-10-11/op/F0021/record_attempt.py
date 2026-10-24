from pathlib import Path
p=Path('.')
p.joinpath('ATTEMPT.md').write_text(r'''# F0021 — attempt, 2026-10-12

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
''',encoding='utf-8')
p.joinpath('STATUS.md').write_text('STATE: WORKING\nNEXT: Complete literature follow-ups and verify single-site/truncation bounds with finite computations and Lean algebra.\nVERDICT: PARTIAL\n\n2026-10-12: Verified Question 5 and Assumption 3 directly from source PDF. Proved a single-site entropy bound and a conditional truncation transfer; corrected false constant-cost claim in earlier attempt. Full KPZ/Airy limit remains unproved.\n',encoding='utf-8')
