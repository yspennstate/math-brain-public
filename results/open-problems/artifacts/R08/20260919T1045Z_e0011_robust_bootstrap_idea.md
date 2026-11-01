# R08/E0011 idea before the final certificate

The preceding width-eight poisoning calculation shows that merely waiting longer on the current width-three seed cannot yield a near-one robust local stage. Before rebuilding the whole seed geometry, inspect the exceptional **first one-column bootstrap stage**: it is much more expensive than the later generated-shield stages because it accepts only the ten support-closed core labels and suppresses every other owned clock.

There is a different route that changes neither the protected Harris family nor its hazard. The sound adversarial-boundary terminal calculation already identified seven additional adsorption identities whose reaction supports become local after exposing four halo cells. In bootstrap coordinates these seven identities are

- `CO(0,-1)`, `CO(0,2)`, `CO(1,1)`;
- `O2[(0,-1),(0,0)]`, `O2[(0,1),(0,2)]`, `O2[(0,1),(1,1)]`, `O2[(1,0),(1,1)]`.

All seven identities are already inside the first stage's paid-for owned-clock family. Thus accepting them does not enlarge the stage hazard `D=140` or the block dependency family.

The exterior values needed by those seven labels cannot be frozen. Instead, before every accepted arrival allow an adversary to reset the four halo cells to any stable assignment. To obtain a cheap but rigorous strict improvement, do **not** solve the full robust Bellman problem. Accept histories containing at most one of the seven halo-dependent labels. Let `O_n(s)` be the exact successful reaction-weight mass for `n` accepted arrivals using only the old ten labels, and let `F_n(s)` be the mass using at most one halo-dependent label. Then

`F_0 = O_0 = 1_target`,

and for `n>=1`,

`F_n(s) = sum_old T_l F_{n-1}(s) + min_{stable halo h} sum_new T_{l,h} O_{n-1}(s)`.

The same halo assignment must be used across all seven new labels at that arrival; old labels are halo-independent. This gives a source-valid lower event against an adaptively refreshed exterior. Every term is nonnegative, so `F_n(s) >= O_n(s)` pointwise.

The old lambda-4 bootstrap polynomial can therefore be computed on all 48,027 entrance descriptors and sorted. Evaluate the new `F` polynomial first at the old minimizer to obtain an exact cutoff. Any descriptor whose old polynomial already exceeds that cutoff can be discarded by monotonicity `F>=O`; only descriptors below the cutoff need the more expensive adversarial-halo recursion. If the resulting exact minimum beats the later lambda-87/20 bootstrap factor inherited by the sound `b17_rob` certificate, the frozen metric moves without changing any other stage.