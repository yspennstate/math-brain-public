from pathlib import Path
import json
p=Path('.')
with p.joinpath('ATTEMPT.md').open('a',encoding='utf-8') as f:f.write(r'''

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
''')
claims=[
 ('Regularly varying right tails admit every lower polynomial power envelope q<alpha.','proved','ATTEMPT.md, Lemma 1','None for the stated tail envelope.','Full dyadic proof; no left-tail or moment assumption.'),
 ('For alpha>5, the positive maximum of beta omega_{i,x}-x^2/(2i) over the full reachable cone is o_P(n^(1/3)).','proved','ATTEMPT.md, Proposition 2','This controls isolated rewards and does not control random-background polymer free-energy fluctuations.','Full union-bound/integral proof; CHECKS.json sum-integral and exponent checks; Lean exponent arithmetic pending.'),
 ('The constant bare-walk travel-cost assertion in earlier attempt F0021-A001 is false: P(S_n=n)=2^(-n).','counterexample','ATTEMPT.md, Lemma 3','This refutes an earlier argument, not Question 5.','Exact all-right path probability; binomial/Chernoff verification through time 1200.'),
 ('If alpha*kappa>1+xi then capping positive weights at n^kappa leaves every weight in a deterministic n^xi tube unchanged with probability tending to one.','proved','ATTEMPT.md, Proposition 4','Confinement of the polymer to this tube remains unproved.','Complete site-count and tail-union-bound proof.'),
 ('For alpha>5, given original-polymer tube mass Q_n with -log Q_n=o_P(n^(1/3)), a suitable cutoff n^kappa, kappa<1/3, changes log Z_n by o_P(n^(1/3)).','proved','ATTEMPT.md, Proposition 5','The confinement hypothesis and a KPZ limit for capped disorder are unproved; no Airy-process transfer is claimed.','Exact deterministic partition inequality; exhaustive n=10 path test; Lean ratio algebra pending.'),
 ('For any 5<q<alpha, E M_n=O(n^(3/(2q-1))), so E M_n/n^(1/3) tends to zero.','proved','ATTEMPT.md, Corollary 6','Single-site model only; no L1 universality statement for the full polymer.','Integrated explicit union bound; Lean rational exponent check pending.'),
 ('Finite exact Pareto single-site exceedance probabilities decrease for alpha=6, remain close to 0.333 for alpha=5, and increase for alpha=4 at tested sizes.','numerical_evidence','CHECKS.json; verify.py','No asymptotic theorem or full-polymer conclusion follows from these finite computations.','Independent Pareto product CDF, floating-point log1p sum; n through 4096.')]
p.joinpath('CLAIMS.jsonl').write_text(''.join(json.dumps({'problem_id':'F0021','claim':c,'status':s,'proof_location':l,'remaining_gap':g,'checks':v},ensure_ascii=False)+'\n' for c,s,l,g,v in claims),encoding='utf-8')
