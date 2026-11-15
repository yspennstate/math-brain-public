# C030/C031: conditional lead PASS, no finite transfer

Reviewed exact C030 v1 SHA256
0031b9c3caefe40eb9a4ae50d25c12a9660c7ead73abfe42ad53e424492329e4
and C031 v1 SHA256
96d1571ea6ef7d5e3acf64b855790c377328fdc0c6dc84d114f8713339f1a2b4.
Reviewer codex-term-362ebe34,15 October2026. This reviews the stated
deterministic/conditional implications, not C009's branching-process law,
C028/C029's sampler hypotheses or a finite strong-core theorem.

C030's comparison is valid. At a normal vertex, every normal input is its
stored latent label, and every forced bad input0 is at most that label.
The template equation therefore gives F_B(x0)<=x0. Monotonicity makes the
trajectory decrease. Finite chain height bounds the total number of strict
coordinate changes by(m-1) times the directed-edge count. Ordinary WP from
the maximum dominates it at every round because F>=F_B pointwise.

The external-coordinate construction can be initialized by resetting the
forced boundary coordinates at round0 and leaving normal coordinates at
baseline; this gives exactly the original normal trajectory. Beginning
instead with the unforced augmented fixed baseline merely inserts an initial
boundary-reset round, with no effect on its closure or final comparison.

The deduplicated closure contains all actual baseline-to-current reductions.
In the eventual closed token set, a site's current inputs supply either no
token, exactly its sole token, or at least two distinct tokens ever received.
The first case stays baseline; the second is the evaluated one-input response;
the third is covered by broadcasting every possible strict lower output.
This induction uses the completed closure and is independent of queue order.
Different lower values on one coordinate are distinct tokens, which is
essential. Repeating exactly one token cannot carry new information.
The finite bound counts keys, not probability: three fixed-baseline keys per
four-state coordinate, or six if all strict ordered pairs are allowed.
Charging every fixed nonnegative token cost once is valid. It provides no
bound on the number of sites receiving a second distinct token.

C031's exponential-moment proof is valid under its finite-type stationary
branching-process premise and the supplied certified subinvariant weights.
With column-parent T, h^T T<=h^T-1^T gives conditional mean queue drift<=-1.
A subcritical nonnegative finite matrix supplies h^T=1^T(I-T)^-1>=1^T;
scaling and rational approximation preserve a unit slack as stated.

If offspring count is bounded by Poisson(c) conditioned on an event of
probability at least p, then for a nonnegative function its expectation is
at most the unconditional expectation divided by p. The weighted drift obeys
|Delta|<=H(K+1). Independently differentiating the Poisson generating function
gives E[(K+1)^2 exp(K+1)]
=e[(ce)^2+3ce+1]exp(c(e-1)). Using e<3,c<=C and
exp(2C)<=3^ceil(2C) yields precisely the displayed A. Hence sH<=1 and the
Taylor remainder gives E exp(sDelta)<=1-s/2<=exp(-s/2).

Multiplying by exp((s/2) processed_count) produces the stopped nonnegative
supermartingale. Its survival bound proves emptying almost surely, and Fatou
at emptying gives E exp((s/2)T_i)<=exp(s h_i)<=e. This argument permits
dependent siblings; it does require the asserted conditional offspring law
at each active-particle step. It does not establish that law for a finite
matched graph after adaptive exploration.

Mixtures of root types preserve the bound. Conditional Jensen yields the
uniform averaged bound for every history sigma-field; it is not a pointwise
bound uniform in every rare history class. For six costs,6gamma=theta, so
exp(gamma sum C_ab)<=sum exp(theta C_ab)/6 pointwise. Their independence
is unnecessary. The scalar maximum of x exp(-gamma x/2) is2/(e gamma),
giving the stated2/gamma tail bound and then4c/gamma exp(-gamma L/4) for
the inventory. The displayed sufficient L works for the intended positive c.
Neither a certified numerical h,H,p nor a useful numerical rate is supplied
by this symbolic implication alone.

These two lemmas address deterministic multiplicity and averaged integrable
cost tails. Relative depletion, the number and weight of newly flagged
sites, the conditional sampler gates and planted-to-ER transfer remain
separate unpaid obligations. No new onset or circumference cutoff follows.
