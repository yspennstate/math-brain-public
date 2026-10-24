# Direct adversarial audit of w573's C0029 candidate

Read w573/ATTEMPT.md only after saving S1.w574.1--3 independently. This audits the author proof, not another review. Full paired proof was available at this checkpoint; it makes no C0029 solution claim.

Scoped verdict: KEEP the deterministic statements and inference obstruction in Lemmas A--E as author proofs pending the designated referee/served-model gates. Gaussian fixed-t convergence must retain its finite-n error eta; the author explicitly does so. Lemma C is a continuous-CDF counterexample to an implication, not a Bernoulli counterexample.

For Lemma D, let A=N^T N and tau>=0. If lambda_2(A)<=tau, a vector orthogonal to X within the bottom two-dimensional eigenspace has Rayleigh quotient at most tau; this covers rank deficiency and the boundary tau=lambda_2(A). Otherwise the positive spectral block of A-tau I is invertible. Completing the square leaves a one-dimensional sign test z_0^2/(1+sum z_i^2/(d_i-tau))-tau<=0. This includes tau=0 and equality. Multiplicities do not change the weighted squared projections. The conditional CDF identity separates disjoint N events; no row probabilities are multiplied.

For Lemma E, d_i>=mu>tau gives the upper ratio (1-tau/mu)^(-1/2). The proposed refinement for tau/mu<=1/2 follows from (1+r)^2(1-r)>=1. The denominator replacement without its correction is invalid.

Concrete strict witness: N=(1,0), X=(1,1), n=2, tau=2/5. Then mu=1 and s_min([N;X])^2=(3-sqrt(5))/2<2/5. The exact row threshold is (2/5)(1+1/(1-2/5))=16/15>=z_0^2=1, whereas dropping tau produces (2/5)(1+1)=4/5<1. Thus the simplified event excludes a matrix in the true event. This witness is for the deterministic row identity; N has a zero entry and is not a Bernoulli-law counterexample.

No false step was found in the saved Lemmas A--E. The parent proof stops at an explicitly unproved signed Bernoulli comparison. An additional minimal premise for any Gaussian radius argument is independence of the one-dimensional Gaussian coordinate from the radius. A finite unconditional third moment or cutoff is needed for the cubic remainder estimate. Even that remainder is generally polynomial, so it alone does not give a uniform exponential remainder.

Exact remaining gap: bound the signed Bernoulli exact-row expectation relative to the finite-n Gaussian CDF uniformly through the small-threshold window, retaining the mu<=tau branch and the joint row-coordinate dependence. Independent referee: w575. Response-side served-model evidence: not available to w574; this document is not a promotion receipt.

NEXT: w575 independently checks S1.w574.1--5 and the scoped KEEP; integration contact admits only the kept DRAFT/source-correction scope after identity gates.
