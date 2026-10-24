# Possible approaches to the full Fourier entropy-influence conjecture

21 September 2026. These are routes, not results. Each one says what the idea is, why it is not obviously dead,
what to compute or prove first, and what would kill it. The facts they lean on are in REPORT.md (the read-once
theorem, the restriction identity, the measured step constants). Constant names: FEI asks for C with
H(f) <= C I(f) for every Boolean f; the best lower bound is Hod's beta(1/2) = 6.4548 (read-once), which is also the
sharp read-once constant.

## 1. FEI as a compression statement about the spectral sample

The spectral sample S has Pr[S] = f-hat(S)^2, Pr[i in S] = Inf_i(f), and E|S| = I(f). FEI says H(S) <= C E|S|:
a random set whose marginals are the influences has entropy at most a constant times its mean size. By the chain
rule H(S) = sum_i H(1[i in S] | 1[j in S], j < i), so FEI holds if and only if there is an order and a sequential
predictor of the membership bits whose average log-loss is at most C E|S|. A predictor built from the function's
structure (a decision tree, a certificate, the sensitivity set of a random input) is a proof. First compute: for the
hard families (tribes, Hod's functions, addressing, one-point flips) the conditional entropies under the natural
orders; see which order makes the per-bit loss proportional to the marginal. Killed if the sum of conditional
entropies exceeds C times the marginal sum for every order on some explicit family.

## 2. The block-influence profile determines the spectral sample

Pr[S avoids T] = sum_{S subset of T^c} f-hat(S)^2 = E[f(x) f(x^{(T)})], where x^{(T)} rerandomises the block T
(for +-1 functions this is 1 - 2 Inf_T). By Mobius inversion the whole distribution of S is a function of the
block-influence profile T -> Inf_T, an input-side quantity. So FEI is a statement about correlations under block
rerandomisation and Booleanity is the only constraint on the profile. Route: characterise the profiles that arise
from Boolean functions (the profile of a product-set S with tiny independent marginals would violate FEI, so
Booleanity must exclude it) and prove the entropy bound from the profile's structure. First compute: the profile of
the n = 6 record function and of tribes, and the entropy as a functional of the profile; test which inequalities
on profiles (supermodularity, log-concavity along chains of blocks) hold for all Boolean functions on up to 5
variables. Killed by a Boolean function whose profile is close to a small-marginal product profile.

## 3. Coupling the spectral sample to the sensitivity set

For every f, E|S| = E|Sens(x)| (average sensitivity equals total influence). Conjecture to test: there is a coupling
of S with the sensitivity set of a uniform input under which H(S) <= H(Sens(x)) + E|Sens(x)| (a subset of a random
set costs at most one bit per element on top of the set's own entropy). Then FEI reduces to H(Sens(x)) <= C' I(f),
an entropy bound on an input-side random set. First compute: H(Sens(x)) / I(f) over all functions on up to 5
variables and on the hard families (for majority and tribes it is small; for addressing it is linear in the
address length). If H(Sens(x)) can exceed C I(f), the route is dead; if it cannot, prove it and then build the
coupling (a Fourier-analytic sampler of S that first samples x and a subset of Sens(x)).

## 4. Typical Fourier coefficients are not exponentially small

H(f) = E_S[log2(1/f-hat(S)^2)], so FEI says: on average over the spectral sample, log2(1/f-hat(S)^2) <= C |S|; a
random coefficient drawn by its own weight is at least 2^{-C|S|/2} in a logarithmic average. Granularity gives
f-hat(S) in 2^{1-n} Z, hence the trivial H <= 2(n-1). The question is why coefficients carrying the mass at level k
cannot typically be much smaller than 2^{-Ck/2}. First compute: for the hard families, the distribution of
log2(1/f-hat(S)^2)/|S| under the spectral sample, level by level; the conjecture is that its weighted mean stays below
C. Then look for a structural reason: a coefficient f-hat(S) is an average of
f over a subcube-like structure of dimension |S| (the S-parity correlation), and small parities of a Boolean function
are constrained by the values at nearby points.

## 5. Bound the potential-free step, or show it is unbounded

Section 6 of REPORT.md: with rho_0(f) = min_i Delta_i H / Inf_i, FEI follows with constant sup_f rho_0 if that
supremum is finite. Measured: 4.8677 on all functions of at most 5 variables, 6.0037 on width-2 tribes, bounded on
every structured family tried, and never above 6.1. Two directions. (a) Search for functions with rho_0 > 7: compose
tribes with addressing, iterate Hod's construction under restriction, take random restrictions of parity-heavy
functions, use the n = 6 monotone class exhaustively (7,828,354 functions) and NPN-class enumeration at n = 6. A
family with unbounded rho_0 tells the shape of the potential that a proof must carry. (b) If nothing exceeds about
6.1, try to prove sup rho_0 <= C directly from the identity Delta_i H = JS_i + sum_S m(S) h(q_{i,S}): the second term
is at most h(Inf_i), so a large ratio needs JS_i >> Inf_i at EVERY coordinate, i.e. the value of every bit is very
informative about the spectral sample of the restriction while the bit itself is rarely in the sample. Prove that a
Boolean function cannot have that property at all coordinates at once (the "ubiquitous informative bit" lemma).

## 6. A potential that absorbs the Jensen-Shannon term

The read-once proof works because the potential depends only on Pr[f], and disjoint composition transforms spectra
as products. Under restriction (the MUX gate with shared inputs) the JS term appears and a measure-only potential
cannot absorb it. Candidates that are computable under restrictions and might drop by at least JS_i: the entropy of
the influence profile (H of the distribution Inf_i / I), the spectral entropy of the derivative D_i f, the entropy
of the level distribution W^{=k}, a Renyi-alpha version of H for alpha < 1. First compute: for each candidate Psi, the
quantity Psi(f) - (Psi(f_0) + Psi(f_1))/2 - JS_i at the binding coordinate of the record functions (n = 6, 7) and
of tribes; a candidate is alive when this is nonnegative and bounded by a multiple of Inf_i. Killed by the same
test. Section 6 of REPORT.md already kills the four simplest statistics.

## 7. Prove the sharp constant conjecture for a bigger class first

Read-once formulas over any gate of fan-in at most three give the same constant numerically (REPORT.md section 5).
Natural next classes where a composition-type potential might still work: read-once formulas over arbitrary
fan-in gates (the k-input inequality is explicit); read-twice formulas where the two copies of a variable are far
apart (an inequality version of the composition lemma with an error term controlled by the shared influence);
decision lists; functions computed by depth-2 decision trees. For each class, run the Pareto search for the maximal
H/I and check whether it stays at beta(1/2). A class where the ratio exceeds 6.4548 refutes the conjecture that
Hod's construction is extremal in general, which would itself be news.

## 8. Is Hod's constant the sharp FEI constant?

Nothing on record has H/I above 6.4548: read-once search, all functions on at most 5 variables (maximum 3.6237),
the structured families tried. Test the conjecture C_FEI = beta(1/2) as hard as possible, because a counterexample
redirects everything: exhaustive over monotone functions of 6 variables; NPN representatives of 6 variables
(200 million classes, a Walsh transform each, feasible in C); hill climbing from every known extremal family at
n = 8..24; random restrictions of Hod's functions; compositions of Hod's functions with tribes and majorities.
Report the largest ratio found and the function.

## 9. Close the read-once case exactly

The certified constant is 6.4573 against the true value 6.4547837. Two steps: an enclosure that keeps the cancellation
in G(x) + G(y) - G(x + y) (exact corner minimum on each piecewise-linear cell plus a mean-value form for E) and the
M = 96 candidate, which should give about 6.4554; then an exact description of the fixed point of the value
iteration, which is known at the dyadic points (the AND-chain slack) and is log-periodic in between. A closed form,
or a proof that the fixed point equals Hod's limit slack on a dense set, would give C_RO = beta(1/2) exactly. Useful
by itself: the sharp constant of a natural class, and the method transfers to any class with a composition lemma.

## 10. Interpolate along the noise semigroup

Let p_rho(S) be proportional to f-hat(S)^2 rho^{2|S|}. Then H(p_rho) = log Z(rho) - 2 log(rho) E_rho|S| - E_rho log f-hat(S)^2
with Z = Stab_rho(f). Differentiate in rho: the derivative involves the variance of |S| under p_rho and the
covariance of |S| with log f-hat(S)^2. A proof would bound the derivative of H by C times the derivative of a
functional that integrates to I(f). This is the shape of the semigroup proofs of KKL and of log-Sobolev
inequalities; the hypercontractive inequality controls exactly how Stab_rho depends on rho. First compute: the two
derivatives along rho for the hard families and the ratio between them; killed if the ratio is unbounded on a
family where H/I is bounded.

## 11. Decision trees, paths and the spectral sample

For a decision tree every S in the support of the spectral sample is a subset of the variables on some root-to-leaf
path. Wan, Wright and Wu turn this into H(f) <= O(average depth) through the restriction identity. The gap to FEI
is that average depth can exceed total influence by a factor of order sqrt(n) (majority). Route: replace the tree by
a randomised tree adapted to the function (query the most influential coordinate first, restrict, repeat) and
bound the entropy contributed at each node by a multiple of the influence spent there; the restriction identity
says the price of a node is JS + h(Inf) and the JS term must be paid by structure. First compute: for tribes and
majority, the influence-greedy tree's per-node JS terms and their sum against I(f).

## 12. Duality and the finite-n linear programme done right

On a finite universe the best potential is trivial (Psi = C I - H is admissible), so a linear programme over all
functions of n variables says nothing. The useful dual is over a restricted family of potentials (measure-only,
level-distribution, influence-profile) with the constraint imposed on every function of n variables: its value at
n = 4 and 5 (exhaustive, cheap) says which family of potentials can carry an induction and which cannot, before any
proof is attempted. First compute: the LP over measure-plus-level potentials at n = 4, then n = 5.

## 13. Two-sided constraints from Booleanity on the profile

Booleanity (f = +-1) is what separates the spectral sample from an arbitrary distribution on subsets. Known
consequences: the level-1 weights are the first-order influences of a monotone function; the sum over T of
Pr[S subset of T] over blocks of a fixed size has an input-side meaning; the parities f-hat(S) are averages of f
over subcubes. Route: find an inequality of the form "if the spectral sample has entropy > C E|S| then some
correlation E[f(x) f(x^{(T)})] would be outside [-1, 1]" - i.e. derive FEI as a consequence of the constraints
that the correlations be genuine correlations of a +-1-valued function. First compute: for the hypothetical
product-set spectral sample with small marginals (which violates FEI), the correlation function it implies and the
block T for which it leaves [-1, 1].

## 14. Transfer from coding theory and point processes

Entropy-versus-mean-size inequalities of this exact shape appear as "the description length of a random selection
is at most a constant times its expected size" in coding, and as bounds on the entropy of a random position set in
sequential prediction. The information-theoretic literature on such bounds (e.g. entropy of a random subset with
given marginals under negative dependence or under a determinantal structure) has tools that have not been tried on
the spectral sample: for a determinantal point process the entropy IS bounded by a multiple of the mean size. First
question: is the spectral sample of some natural class of Boolean functions negatively associated or determinantal?
For read-once formulas the spectral sample has a product-like structure under composition; check whether that gives
negative association, and whether negative association alone implies an entropy bound of the FEI shape.
