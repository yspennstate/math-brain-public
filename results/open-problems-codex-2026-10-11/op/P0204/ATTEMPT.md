# P0204 research record — 2026-10-11

## Exact question and conventions

Let N >= 2, V be coordinatewise increasing in {0,1}^N, and m=|V|>=2^(N-1). Let G be its induced graph, d(x) its degree, D=sum d(x), and P(x,x)=1/2, P(x,y)=1/(2d(x)) for adjacent vertices. The question is whether worst-start total-variation t_mix(P,1/4)<=C N log N with universal C. N=1 has either the full two-point cube or a singleton; give the singleton mixing time zero. Logarithms are natural.

Peres's live webpage states precisely the increasing/half-volume hypotheses and calls the chain lazy simple random walk on V. The cited Ding–Mossel paper instead defines a **censored coordinate walk** Q: Q(x,y)=1/(2N) on edges, Q(x,x)=1-d(x)/(2N), with uniform stationary law mu(x)=1/m. These are distinct chains; literature results below must be transferred rather than silently applied.

## Literature status

**Resolved by a September 2026 preprint.** Yiming Chen, with an appendix by Yuval Peres (arXiv metadata lists Chen and Peres), *Mixing time under monotone censoring*, arXiv:2609.16515v2, first submitted 2026-09-15, revised 2026-09-19. Theorem 1.2 proves t_mix(Q,1/4)<=K a^(-3) N log(eN) for every nonempty increasing V, with absolute K. Equation (1.1) explicitly defines Q, not P. Section 4 supplies the stopping-time occupation inequality that avoids the failed uniform log-Sobolev route. Section 4 below gives a complete transfer to the exact induced-walk problem. No remaining gap for P0204, conditional on this cited literature theorem. This is a publicly posted preprint; no journal publication was verified.

Earlier results: Fei–Ferreira Pinto Jr., arXiv:2505.02685v2 (2026-07-03), Theorem 1.6, proves gap(Q)>=(1-sqrt(1-a))/N, a=m/2^N. Its Section 1.5 leaves the mixing conjecture unresolved at that date. Chang–Sun–Yu, arXiv:2506.09852v4 (2026-08-11), gives an elementary proof within a factor two and O(N^2) mixing. Oliveira Santos–Tripathi–Youssef, arXiv:2606.09221v1 (2026-06-08), proves O(N log N) for typical monotone sets and shows worst-case classical log-Sobolev constants of order N^2 for Q. Some discovery/citation APIs are rate limited; see LITERATURE.md.

## 1. Basic geometry, stationarity, and correction of the old diameter bound

For x,y in V let z=x OR y coordinatewise. Flip each zero of x that is one in y to obtain z, then reverse the upward path from y to z. Both segments lie in V by monotonicity. Each differing coordinate is flipped once, so this is a path of Hamming length dist_H(x,y)<=N. No cube path can be shorter. Consequently G is connected and isometric in the cube, with diameter at most N (improving the earlier brain record's 2N bound). For N>=2 the volume hypothesis gives m>=2, so all degrees are positive.

The stationary law of P is pi(x)=d(x)/D: on every edge pi(x)P(x,y)=1/(2D)=pi(y)P(y,x). Summing detailed balance over x proves stationarity, and connectedness makes it unique. For V equal to the cube with only 0 removed, unit vectors have degree N-1, vertices of weight >=2 have degree N. For N>=3 the two degree classes are adjacent, so the uniform law fails detailed balance and, since the stationary law is unique, is not stationary.

## 2. Exact spectral and log-Sobolev transfer (proved)

This argument works on any connected induced subgraph of the N-cube with at least two vertices. Put c=Nm/D=N/(average degree). Then pi(x)<=c mu(x). Write S(f)=sum_{unordered edges {x,y}}(f(x)-f(y))^2. Direct substitution in the reversible Dirichlet forms gives E_P(f,f)=S(f)/(2D) and E_Q(f,f)=S(f)/(2Nm). Thus E_P=c E_Q exactly.

For every real f, choose b=E_mu f. Since variance is the minimum over centers,

Var_pi(f)=min_a E_pi[(f-a)^2] <= E_pi[(f-b)^2] <= c E_mu[(f-b)^2]=c Var_mu(f).

If gamma_Q Var_mu(f)<=E_Q(f,f), multiply the variance comparison by the nonnegative gamma_Q, then apply the inequality and the energy identity: gamma_Q Var_pi(f)<=c gamma_Q Var_mu(f)<=c E_Q(f,f)=E_P(f,f). Taking the infimum of Rayleigh quotients proves gamma_P>=gamma_Q. All inequalities hold for arbitrary f, including constants.

For entropy, let h>=0 and define phi(h,b)=h log(h/b)-h+b for b>0, with 0 log 0=0. The function u log u-u+1 is nonnegative: its derivative is log u, its unique minimum is zero at u=1, and its limit at zero is 1. Thus phi>=0. Direct expansion shows inf_{b>0} E_nu phi(h,b)=Ent_nu(h); if E_nu h>0 the minimum is at b=E_nu h, and if h is identically zero the infimum is zero. Taking b=E_mu h (or treating h=0 separately), domination gives Ent_pi(h)<=c Ent_mu(h). Therefore Ent_mu(f^2)<=L_Q E_Q(f,f) implies Ent_pi(f^2)<=L_Q E_P(f,f). The classical log-Sobolev constant L_P is at most L_Q. This does not assert a comparison of discrete-time TV distances.

## 3. Updated universal induced-walk bound (literature theorem + proved transfer)

Apply Fei–Ferreira Pinto Jr., Theorem 1.6, with a=m/2^N>=1/2. Their energy is N times E_Q, so gamma_Q>=(1-sqrt(1-a))/N >= (1-1/sqrt(2))/N. Section 2 proves the same lower bound for gamma_P.

Here is the full conversion to mixing. Reversibility makes P self-adjoint in L2(pi). Since P=(I+R)/2 for a reversible stochastic kernel R, all eigenvalues are in [0,1]. For a start x, the density of delta_x relative to pi, minus 1, has squared L2 norm 1/pi(x)-1. Spectral contraction and Cauchy–Schwarz imply

||P^t(x,.)-pi||_TV <= (1/2) sqrt(1/pi(x)-1) (1-gamma_P)^t <= (1/2) sqrt(D) exp(-gamma_P t),

because d(x)>=1. Since D<=Nm<=N2^N, choosing

t >= N/(1-1/sqrt(2)) * [log 2 + (log N + N log 2)/2]

makes the upper bound at most 1/4. Taking ceilings gives a uniform O(N^2) induced-walk bound. This is not O(N log N).

## 4. Complete transfer of the literature solution to the degree-weighted induced walk

### 4.1 Uniform domination of the stationary measure

For N>=2 and a>=1/2, the average degree dbar=D/m is at least N/2. To prove this when N>=4, put W(x)=|x| and let X be uniform on the full cube. Every zero bit of each x in V leads upward to another vertex of V. Counting every edge once from its lower endpoint gives D=2 sum_{x in V}(N-|x|), hence dbar=N-2(E[W|X in V]-N/2). Independence of the full-cube bits gives E W=N/2 and Var(W)=N/4. Also Var(1_V)=a(1-a). Cauchy–Schwarz for the covariance yields

E[W|X in V]-N/2 = Cov(W,1_V)/a <= (1/2) sqrt(N(1-a)/a) <= sqrt(N)/2.

Therefore dbar>=N-sqrt(N)>=N/2 for N>=4. For N=2,3, connectedness gives |E|>=m-1, so dbar>=2-2/m. Since m>=2 when N=2 and m>=4 when N=3, this is respectively at least 1 and 3/2. Thus the claim holds in all cases N>=2. As d(x)<=N,

pi(x)/mu(x)=d(x)/dbar<=2.

Consequently pi(B)>=1/4 implies mu(B)>=1/8. This bound is on stationary masses; it does not identify the two stationary laws.

### 4.2 Hitting times decrease under this time change

Both P and Q have the same embedded jump chain: from x choose an induced neighbor uniformly. For P, the waiting time at each successive embedded state before its next jump is geometric on {1,2,...} with parameter 1/2. For Q, it is geometric with parameter d(x)/(2N)<=1/2. Construct the common embedded path first and use independent uniform random variables for inverse distribution functions of these waiting times. For each visit the P waiting time is at most the Q waiting time, because the geometric law decreases stochastically as its parameter increases. Conditional on the common path these constructions have exactly the correct kernels. The index of the first embedded visit to a fixed target B is the same for both chains. Summing the waiting times before that index gives tau_B(P)<=tau_B(Q) pathwise, including the zero hitting time when the start belongs to B. Finite connectedness ensures finite expectations. Hence E_x^P tau_B<=E_x^Q tau_B for every x,B.

### 4.3 From the Chen–Peres mixing theorem to hitting times

Let t0=t_mix(Q,1/4). For N>=2 there are at least two states, so t0>=1. Define d_Q(t)=max_x ||Q^t(x,.)-mu||_TV and bard_Q(t)=max_{x,y}||Q^t(x,.)-Q^t(y,.)||_TV. The triangle inequality gives bard_Q(t)<=2d_Q(t). Contraction of signed zero-mass measures by a Markov kernel gives d_Q(s+t)<=d_Q(s)bard_Q(t): decompose a zero-mass signed measure into positive and negative parts of equal mass, normalize each to a probability law, and bound the TV distance of their images by bard_Q(t). Taking s=t=t0 and then s=2t0,t=t0 yields d_Q(3t0)<=1/16.

If mu(B)>=1/8, then from any state x,

Pr_x^Q(X_{3t0} in B)>=mu(B)-1/16>=1/16.

Being in B at the endpoint entails having hit B by that endpoint. By the Markov property, conditional on avoiding B up to any multiple of 3t0 the chance of avoiding it for another block is at most 15/16. Thus Pr(tau_B>j*3t0)<=(15/16)^j. The tail-sum formula, grouping times in these blocks, gives E_x^Q tau_B<=3t0 sum_{j>=0}(15/16)^j=48t0. Together with sections 4.1–4.2 this proves

t_H^P(1/4):=max_{x,B:pi(B)>=1/4} E_x^P tau_B <=48t0.

### 4.4 Finish using the precise hitting-to-mixing theorem

Yuval Peres and Perla Sousi, *Mixing times are hitting times of large sets*, J. Theoret. Probab. 28 (2015), 488–519; arXiv:1108.0133v3, Theorem 1.1: for each fixed alpha in (0,1/2), every finite irreducible reversible kernel R obeys t_mix((I+R)/2,1/4)<=C_alpha t_H^R(alpha). This is also quoted as Theorem 2.3 in Chen–Peres.

Apply it to R, the nonlazy simple random walk on the induced graph, so P=(I+R)/2. R is finite, connected, and reversible with stationary law pi. Independent geometric holding with mean 2 gives E_x^P tau_B=2 E_x^R tau_B (condition on the embedded hitting index and sum expectations). Thus

t_mix(P,1/4)<=C_(1/4) t_H^R(1/4) <=48 C_(1/4) t0.

(Using the exact factor two would improve 48 to 24, but is unnecessary.) By Chen–Peres Theorem 1.2, t0<=K a^(-3) N log(eN)<=8K N log(eN). Hence

t_mix(P,1/4)<=384 C_(1/4) K N log(eN)=O(N log N),

with universal constants for N>=2. N=1 is handled as at the start of this record. This settles precisely the user-specified chain, rather than merely its uniform-stationary censored variant.

## 5. Computations and hostile checks

Before the final literature discovery, experiments.py enumerated increasing sets recursively: a set in dimension n is represented by sections A0 subseteq A1, each increasing in dimension n-1. Every such pair is included once. The resulting numbers of half-volume sets were 4, 12, 96, 4101 for n=2,3,4,5. For each, it built both kernels and checked stationarity, numerical spectral gaps, and worst-start TV mixing using matrix powers with binary search for the first integer time at distance <=1/4. Maximum induced mixing times were 1,4,7,10. The minimum observed gap(P)-gap(Q) was zero in each dimension; stationary and row-sum residuals were <=1.12e-16. These are floating-point diagnostics, not certified asymptotic evidence or a proof of pointwise mixing-time domination. All dense matrices were at most 32 by 32; measured computation time was about four seconds, with memory far below 1 GB. Raw output is experiment_results.json.

branch_results.json contains exploratory exact-integer counts followed by floating-point logarithms for an attached-subcube family. No counterexample to TV mixing is claimed from these numbers; that investigation stopped when the literature solution was identified.

Transfer.lean, checked by Lean 4/Mathlib from ~/lean_verify, proves the scalar Rayleigh-comparison implication, two rational flow equalities/inequalities in the 3-cube with zero removed, and an unrelated branch-mass algebraic bound. It uses specific imports and norm_num/nlinarith, no sorry and no native_decide. The first run exposed a missing Real import; it was fixed and the final run exited 0 (lean_check.txt). **The Lean file does not formalize the Chen–Peres theorem or the full hitting-time transfer.**

Potential failure points and resolutions:

1. Wrong stationary law: distinguished P and Q explicitly and used pi<=2mu, not equality.
2. Applying an older partial result as a solution: the decisive result is the September preprint's Theorem 1.2, not the earlier spectral/typical-set papers.
3. Comparing TV mixing directly under faster holding: no such assertion is made. Only hitting times are coupled, and the Peres–Sousi theorem converts them back to mixing.
4. Using target sets large under the wrong measure: pi(B)>=1/4 is converted rigorously into mu(B)>=1/8 using the average-degree proof, including N=2,3.
5. Endpoint versus first-hit probabilities: endpoint membership only supplies a lower bound for hitting; this direction is correct and is iterated conditionally by the Markov property.
6. Laziness in Peres–Sousi: the theorem is applied to the nonlazy R, whose lazy version is exactly P; connectedness/reversibility hold despite possible bipartiteness of R.

## Final verdict

SOLVED_IN_LITERATURE. The decisive reference is arXiv:2609.16515v2, Theorem 1.2 and Corollary 1.3, together with the complete chain-convention transfer above. No mathematical gap remains in that transfer. The preprint theorem is used as an external published-on-arXiv result, not claimed to have been independently formalized or fully re-proved here.
