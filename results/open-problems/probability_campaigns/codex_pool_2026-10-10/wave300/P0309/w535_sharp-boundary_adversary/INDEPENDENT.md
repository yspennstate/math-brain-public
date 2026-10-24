# P0309: independent short-range boundary obstruction

Worker w535, 10 October 2026. Written before reading w534's proof. This is an elementary independently derived special case, with no novelty claim and independent review pending from w536. It does not solve or refute P0309.

## Exact assumptions

Let P be a probability law on locally finite configurations in R^d. Fix finite activity 0 < z < infinity and finite inverse temperature 0 < beta < infinity. Assume the ordinary grand-canonical DLR specification for a measurable nonnegative pair potential v, with no neutralizing background, no particle-number constraint, and no negative external field. In a bounded Borel set B, conditional on exterior eta, its unnormalized partition function is

    Xi_B(eta) = sum_{n>=0} z^n/n! integral_{B^n} exp(-beta H_B(x_1,...,x_n;eta)) dx,
    H_B = sum_{i<j} v(x_i-x_j) + sum_i sum_{y in eta} v(x_i-y).

The empty configuration has energy zero and weight one. Infinite positive interaction energies are allowed, with exp(-infinity)=0. In particular this applies, conditional on existence of an ordinary DLR law, to v(x)=|x|^{-s} in d=3, s>3. It makes no claim about renormalized long-range specifications for s<=3.

## Proposition A: uniform conditional void bound

For every bounded B and P-almost every exterior,

    1 <= Xi_B(eta) <= exp(z |B|),
    P(N_B=0 | F_{B^c}) = 1/Xi_B(eta) >= exp(-z |B|).

Proof. All interaction energies are nonnegative, so each integrand is at most one. Summing the resulting terms gives exp(z|B|). The n=0 term is one. The DLR empty probability is its weight divided by Xi. This is a conditional bound uniform in the exterior, not a marginal estimate.

The constant is sharp uniformly over nonnegative pair potentials: for v=0 the DLR law is the Poisson process of intensity z and equality holds. At fixed z it is also approached by finite-volume Riesz specifications with empty exterior as beta tends to zero, by dominated convergence. This does not assert equality at positive beta for the interacting infinite-volume Riesz gas.

## Proposition B: arbitrarily large holes without independence

For disjoint bounded sets B_1,...,B_m of the same volume V, put A_i={N_{B_i}=0} and p=exp(-zV). Then

    P(intersection_{i=1}^m A_i^c) <= (1-p)^m.

Proof. For each i, every event A_j with j!=i is measurable with respect to F_{B_i^c}. Hence

    E[ product_{i<m} 1_{A_i^c} 1_{A_m^c} ]
      = E[ product_{i<m} 1_{A_i^c} E(1_{A_m^c}|F_{B_m^c}) ]
      <= (1-p) E[ product_{i<m} 1_{A_i^c} ].

Induct on m. This is the required tower-property argument; neither independence nor translation invariance nor ergodicity is assumed.

For any R>0 choose a deterministic infinite sequence of disjoint open radius-R balls. Applying the finite bound to each tail shows that the probability of no empty ball in that tail is zero. The countable union over tails shows that infinitely many of these balls are empty almost surely. Intersect these probability-one events over integer R>=1. The configuration therefore has arbitrarily large empty balls almost surely.

The finite estimate also supplies a confidence bound: at least one of m chosen balls is empty with probability at least 1-(1-exp(-zV))^m. For V>0, to make the failure probability at most delta in (0,1), it suffices that m>=ceil(log(delta)/log(1-exp(-zV))). For V=0 the conditional void probability is one, so no logarithmic inversion is needed and any one such region is empty almost surely.

## Corollary C: no globally bounded displacement from a lattice

Almost surely there is no full-rank lattice L (even selected depending on the configuration), shift a, and bijection f:L+a -> eta such that sup_{ell in L+a}|f(ell)-ell| is finite.

Proof. Every full-rank lattice has a finite covering radius c: for every center x some ell in L+a satisfies |ell-x|<=c. A bijection with displacement bound M would place f(ell) in the open ball of radius R about x whenever R>c+M. Thus every such ball would be occupied. Choose an integer R>c+M and use Proposition B's probability-one property. The contradiction is pathwise, so no uncountable union over lattices or shifts is taken.

More generally the same argument excludes bounded displacement from any relatively dense reference set having a finite covering radius.

## Scope and missing premise

This refutes an auxiliary bridge of the form 'a finite-temperature crystal is almost surely a uniformly bounded perturbation of a lattice' for ordinary repulsive grand-canonical Riesz DLR laws with s>3. It leaves open periodic Gibbs laws, nonconstant periodic correlation densities, Bragg order, finite local displacement moments, and crystalline phases with rare vacancies or large holes. It cannot be transferred to the neutralized s<=3 model by pretending its renormalized energy is nonnegative.

The hardest original piece remains construction of an unpinned finite-temperature Riesz Gibbs state with nontrivial spatial order, with the exact source's definition and exponent range. Neither ground-state optimality nor local harmonic stability supplies that construction.

## Independent-review questions

1. Check the empty-weight normalization and the ensemble restriction.
2. Check that the other void events are exterior-measurable in the induction.
3. Check the countable tail/radius passage and the pathwise treatment of random lattices.
4. Do not replace the target's periodic law with an exactly periodic configuration.

Primary context: Mathieu Lewin, Coulomb and Riesz gases: The known and the unknown, arXiv:2202.09240v2, short-range DLR discussion and Section VI. The proofs above are campaign derivations under an explicitly stated specification, not attributed to a numbered theorem in that review.

Boundary clarification after the independent KEEP: the supplementary confidence inversion explicitly requires V>0; the main void, tower, hole and lattice assertions are unchanged.
