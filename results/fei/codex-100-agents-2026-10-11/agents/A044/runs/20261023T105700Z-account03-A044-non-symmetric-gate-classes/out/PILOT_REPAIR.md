The first pilot failed at the adversary closed-form ratio assertion, after
the exhaustive seed and activation loops completed. The written derivation
and checker both omitted a factor (1+t) in C/Delta_o. Direct cancellation
gives e(1+t)/(t(3+t)), not e/(t(3+t)). The displayed exponential lower bound
is unchanged, since 1+t>=1. Both PROOF.md and the checker were corrected.
The checker also caused a reread of the endpoint prose: it is the inherited
seed's singleton indices that jump upward at the limit, not final indices
dropping. No case domain, runtime cap, or mathematical claim was enlarged.
The successful rerun, if present, is recorded separately in CHECK.json.
