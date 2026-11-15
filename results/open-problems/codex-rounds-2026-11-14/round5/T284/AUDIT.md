# Audit of the feasibility obstruction

## Two counts of the component fluctuation

On four labelled vertices there are four stars (choose the centre) and twelve paths (24 orderings, identified in reversed pairs). A separate Prüfer-code construction produces sixteen different labelled trees and exactly the same edge sets as exhaustive enumeration of the 64 graphs. Exhaustive independent-set enumeration gives independence numbers three for the four stars and two for the twelve paths. The Bernoulli parameter is 1/4, not 1/2 or 3/4.

For a fixed four-set, three internal edges are present, three internal pairs are absent, and 4(n-4) external pairs are absent. Thus the absent-edge exponent is 4n-13, and the expected count divided by n tends to (16/24)d^3 exp(-4d). This agrees with mu_d=(2/3)d^3 exp(-4d).

For two disjoint four-sets, six edges are present. The required absent pairs are six internal pairs, sixteen pairs between the four-sets, and 8(n-8) pairs to the rest. Their total is 8n-42. This independently agrees with twice (4n-13) minus sixteen. In the covariance ratio the sign is positive: shared absences are double-counted by the product probability. Distinct overlapping four-sets have joint probability zero. Therefore the variance upper bound has order n, not n^2.

## Conditional independence and selection

The exposed information includes the actual component vertex sets, not their shapes. Every completion has exactly three edges per component, exactly the same absent pairs, and the specified remainder H. Replacing a path by a star changes neither the connected-component partition nor any outside edge. The fibre is a full Cartesian product of sixteen possibilities per component; conditional independence follows. There is no conditioning on an algorithm-selected successful tree or graph.

The theorem selects histories on which conditional infeasibility is at least 1/6. Their probability is bounded below using the unconditional assumption. Intersecting with the linear-component-count event costs only a fixed fraction of their measure, eventually. The final tiny probability is then lower-bounded inside every retained history. Subtracting the O(1/n) exception after evaluating the tiny tail would invalidate the claim for large L; the proof explicitly avoids that subtraction.

The condition P(alpha<k_n)>=1/3 is essential. A polynomial-time solver's constant success at k_n does not imply this condition. In the concrete example it is supplied separately by a central limit theorem for alpha.

## Tail sign, constants and integer boundaries

For B~Bin(t,1/4), variance is 3t/16. If h<t/4-2sqrt(t), Chebyshev gives probability at most 3/64, below 1/6. This places h above that location. To lower-bound the left tail farther down, the tilted parameter must decrease: q'=1/4-(r+4sqrt(t))/t. Increasing it would give the wrong comparison.

The direct log-likelihood is b log(q/q')+(t-b)log((1-q)/(1-q')). Subtracting its value at b=tq' gives slope log(q(1-q')/(q'(1-q)))>0. Its centre value is -tD(q'||q). Thus a window of radius sqrt(t) loses at most sqrt(t) times the positive slope in the lower bound. The verifier checks this identity by both expressions at both window endpoints.

There are two proofs of the entropy bound needed for the constant six. Applying log u<=u-1 gives D(q'||q)<=Delta^2/[q(1-q)]=(16/3)Delta^2<6Delta^2. Alternatively, for fixed q, the second derivative of D(x||q) is 1/[x(1-x)]<=64/7 on [1/8,1/4]; Taylor's integral remainder gives D(q'||q)<=(32/7)Delta^2<6Delta^2. The same derivative bound also proves theta<=16Delta.

With u=r/sqrt(t), the cost is at most 6(u+4)^2+16(u+4). The first relaxation to 10(u+4)^2 uses u+4>=4. For the second relaxation, 20u^2+320-10(u+4)^2=10(u-4)^2>=0. Multiplication of the retained-history mass 1/12 by window mass 3/4 gives 1/16. Since t>=mu_d n/2, 20r^2/t<=40r^2/(mu_d n). The inequality becomes weaker in the required direction. No constant is intended to be sharp.

The tail event is alpha<k_n-r_n. With integer targets and losses it is B<=k_n-1-Z-r_n. This explains the minus one in h; it is not dropped. The tilted window uses strict absolute inequality, whose complement is exactly the event to which Chebyshev applies. Its upper endpoint lies below h-r_n with an extra sqrt(t) of slack, so a nonintegral mean causes no boundary problem.

## Explicit example and its limits

Pittel's theorem supplies a Gaussian limit with positive variance for d=1/2. Only convergence at a central threshold is used. A central limit theorem alone would not justify the polynomially small tail estimate; that estimate is proved separately by the binomial likelihood argument.

The variance coefficient was computed as a-6beta^2 and independently as exp(-2beta)[exp(beta)(1-beta/2)-1]. Both give approximately 0.0848844, which is positive. A rational bracket using an exponential series and a Decimal Newton iteration independently give beta approximately 0.3517337 and a approximately 0.8271840. These decimal values are checks, not constants used to define the target. The target is specified through certified rational approximations.

The exhaustive component solver has polynomial worst-case running time because it checks the cutoff before enumerating subsets. It has an intentionally large exponent, and is only an existence example; no large exhaustive graph search was run. During component exploration, potential edges are exposed once. Fresh dummy Bernoulli trials dominate the number of new neighbours at each processed vertex. This supports a binomial moment bound for their sum without assuming the explored component is a tree.

The component-cutoff exponent has two checks. Direct evaluation of 1-64(log 2-1/2)/log 2 is about -16.8338. The simpler inequalities log 2>=2/3 and log 2<=1 give the weaker upper bound 1-64/6<0. Either suffices for probability tending to zero.

At central targets the obstruction is feasibility, including for unlimited computation. At the overlap density for large d the target is generally well below the optimum, so the constant-infeasibility assumption has not been established and should not be expected automatically. The example proves optimality in order for the full generality of round 4, not for the original large-d barrier.

## Source and numerical limitations

The source for the component decomposition is fully accessible and agrees with the independent count. The publisher's abstract of Pittel's paper states the central limit theorem and formulas; its full proof was not accessible. This use of a published input is explicit in PROOF.md. No quantitative normal approximation or moderate-deviation theorem is imported.

Finite graph enumeration reaches six vertices; separately enumerated forests contain three four-vertex components. Exact binomial tails reach 16384 trials. Those checks exercise the application, not asymptotic theorems. The verifier used approximately 158 MB of RAM, one thread, inherited nice 20, and under one second of recorded runtime. No claim about a practical independent-set algorithm follows from it.
