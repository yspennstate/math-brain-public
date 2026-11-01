from pathlib import Path
import json
p=Path('SECOND_ATTEMPT.md');s=p.read_text(encoding='utf8');s+='''

## 5. Full finite-alphabet representation argument
For clarity, the exact representation needed above can be derived directly from finite sampling. Let (A_i) be an infinite exchangeable sequence in the finite alphabet E, and let Q_N(e)=N^{-1}#{1<=i<=N:A_i=e}. Fix k<=N and directions e_1,...,e_k. By exchangeability, sampling k distinct ordered indices uniformly from {1,...,N}, independently of A, gives the same joint law as (A_1,...,A_k).

Couple these distinct indices J with k independently sampled uniform indices I as follows: if the I's are distinct, set J=I; otherwise draw J independently and uniformly among distinct ordered k-tuples. Both branches give the same uniform conditional law for J, so this is a valid coupling. The probability of a collision among I is at most sum_{r<s}P(I_r=I_s)=k(k-1)/(2N). Conditional on the sequence A_1,...,A_N, sampling I with replacement gives probability product_j Q_N(e_j). Therefore
|P(A_1=e_1,...,A_k=e_k)-E[product_j Q_N(e_j)]| <= k(k-1)/(2N).

The probability simplex Delta_E is a compact metric space. Standard weak compactness of probability measures on a compact metric space gives a subsequence N_m along which the laws of Q_{N_m} converge weakly to a probability measure rho on Delta_E. The monomial product_j q(e_j) is continuous and bounded there. Send m to infinity in the displayed estimate to obtain
P(A_1=e_1,...,A_k=e_k)=integral product_j q(e_j) rho(dq).
The same subsequence works for every k and every choice of directions because weak convergence tests every continuous function. Thus every finite-cylinder probability agrees with the law obtained by sampling q~rho and then drawing all A_i independently with law q. Equality on cylinders yields equality of the full infinite-sequence laws. Under this mixture construction the ordinary IID strong law, conditionally on q, implies Q_N(e)->q(e) for every e almost surely; integrate over rho and intersect the finitely many directions. Consequently the directing q is a measurable empirical-frequency limit, so the conditional representation used in Section 1 is available in the original sequence as well.

External standard inputs here are only weak compactness on a compact metric space, the countable product construction, and the ordinary IID strong law. Finite exchangeability without an infinite extension would leave a nonzero sampling error and would not give this exact conclusion. This is why a two-cookie exchangeable prefix is insufficient.

## 6. Exact obstruction to extending the reduction to all IID elliptic stacks
In d=2 set q=1/4 and 0<a<1/4. At each site choose an independent fair sign S_x. The first cookie assigns probabilities q+S_x a and q-S_x a to +e_1 and -e_1, and probability q to each vertical direction. The second cookie has the opposite horizontal biases, and every subsequent cookie is placebo. This is an IID uniformly elliptic, bounded-stack environment. Every individual cookie's averaged transition vector is the fair vector, and even the first two cookie vectors are exchangeable as a pair (replace S by -S). Their infinite sequence is not exchangeable.

For the finite path 0,e_1,0,e_1, independence of the origin's sign and the first cookie at e_1 gives exactly
P(path)=q E[(q+S_0 a)(q-S_0 a)]=q^3-q a^2.
For a=1/8 this is 3/256, while the fair walk gives q^3=4/256. The pair of origin departure indicators for +e_1 has covariance -a^2.

This path law cannot equal that of ANY IID Markovian RWRE with the same averaged first-step distribution. Such a RWRE would have E[Q_x(+e_1)]=E[Q_x(-e_1)]=q, and its same path probability would be
E[Q_0(+e_1)^2] E[Q_{e_1}(-e_1)] >= q^2 q=q^3,
because E[(Q_0(+e_1)-q)^2]>=0. Thus the exact RWRE representation proved under (AE) fails within the original hypotheses, even with UEL and two non-placebo cookies. This is a counterexample to a proposed universal representation, NOT a counterexample to zero velocity on the non-transient event.

In contrast, using the same sign at every cookie (a genuinely exchangeable infinite stack) gives P(path)=q^3+q a^2=5/256, exactly the persistent-sign RWRE formula. The extra correlation is retained by the latent transition vector, not averaged away.

## 7. Exact computations and formal checks
second_experiments.py uses fractions.Fraction. It verified the three probabilities 3/256, 4/256 and 5/256 above and the opposite-bias covariance -1/64. It also checked all 4^3=64 three-arrow strings for a model with a latent horizontal bias +/-1/16 and independent vertical cookie noise of magnitude 1/16 at odd visits and 1/32 at even visits. Each cookie is strictly elliptic. Direct summation over latent signs and all noise choices matched the latent RWRE joint law in every string. Yet the vertical cookie-parameter variances are 1/256 and 1/1024, so the cookie vectors themselves are not exchangeable. This verifies a concrete instance of class 3(b) beyond cookie-vector exchangeability.

As an ellipticity stress test, take one direction probability p_i=1/(i+1)^2 and distribute 1-p_i equally among the other directions. All cookies are strictly elliptic. Then the probability of that direction never occurring is 1/2, and of its occurring exactly once at the first index is 1/6: product_{m=3}^N(1-1/m^2)=2(N+1)/(3N)->2/3. These products were checked exactly at N=3,10,100. This arrow law is not exchangeable, since an infinite exchangeable sequence has zero probability of exactly one occurrence. It explains why positive cookie marginals alone are insufficient and why Section 2 actually uses the exchangeability plus original conditional-product structure.

The computation used negligible memory and completed in 0.085 seconds; raw output is second_experiments.json. None of these calculations estimates the non-transient event numerically.

SecondChecks.lean passed lake env lean from ~/lean_verify with exit code 0 and a 3600-second timeout. Its five declarations check the opposite-bias path formula, persistent-bias path formula, strict discrepancy from the marginal walk, two-component mixture covariance identity, and its nonnegativity. It uses only Mathlib.Data.Real.Basic, Mathlib.Tactic.Ring and Mathlib.Tactic.Linarith, with no sorry or native_decide. Printed axiom dependencies are the standard propext, Classical.choice and Quot.sound. The infinite representation, ellipticity proof and source theorem are handwritten probability arguments, not Lean formalizations.

## Hostile-referee checks so far
- Spatial IID is proved for whole arrow stacks and for the local measurable directing vectors; it is not inferred merely from common one-cookie marginals.
- The infinite representation is exact. A finite exchangeable prefix is explicitly excluded, and Section 6 supplies a valid IID/UEL example showing why.
- Each departure uses a distinct site/visit pair, so the finite-path product conditional on the latent environment has no repeated-arrow dependency.
- Strict ellipticity of the directing vector has its own proof; it is not inferred just from its positive expectation.
- Equality is of averaged full-path laws. No claim is made of equality conditional on the original cookie realization.
- Discovery-order sums use an unconditioned IID strong law on a full-probability event, never a false IID assertion conditioned on recurrence.
- The sparse-budget argument is taken for positive integer cutoffs K, giving a single full-probability event on which K can tend to infinity.
- No statement that every recurrent site eventually depletes its cookies is substituted for a density estimate on unfinished moving sites.
''';p.write_text(s,encoding='utf8')
print('finite representation, obstruction, exact checks, and referee audit saved')
