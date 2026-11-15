# Physical-p threshold sanity check

This is a standard first-moment observation, not a new drift bound or a proposed theorem of novelty.

For parent-step probability p<1/2 put beta=p/(1-p). A frog born at distance m from the original root hits it with probability beta^m. There are d^m potential resident origins at that distance. Thus in the all-active comparison the expected number of resident frogs ever hitting the root is sum_(m>=1)(d*beta)^m, finite whenever p<1/(d+1). The original root frog is one further frog. Each ordinary reflected-root personal walk is transient for p<1/2, so finitely many root-hitting frogs make finitely many root visits almost surely. No activation independence is needed for this all-active upper comparison.

Consequently every genuine original-path lower family on T3 has physical-p recurrence threshold at least1/4. The target of C29 and C31 is to attain recurrence at1/4; a strict below-quarter recurrence threshold cannot occur in this parametrization. Numerical apparent growth below1/4 may be a finite-height crossover and is not a rigorous phase bracket. This observation does not settle the boundary p=1/4. It does not concern differently transformed parameters in the nonbacktracking self-similar model.

Context: C27v2 and C31v1 write out beta via finite gambler's ruin; C30v1 is the independently passed all-active first-hit envelope at ordinary p. The reviewer instruction asking for a threshold below1/4 is interpreted as seeking a model strong enough at ordinary drift, with this physical-p restriction explicit.
