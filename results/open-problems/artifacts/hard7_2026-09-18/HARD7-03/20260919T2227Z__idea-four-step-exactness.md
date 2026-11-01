Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# HARD7-03 idea-before-code — close the entire four-step sign atlas

The latest checkpoint completed the strict central `(+,+)` triple-slack chamber, but its prose still treated some non-local-minimum sectors as potentially lossy. I will attack that claim by negation before deriving another inequality.

For a fourth-step interior endpoint write the predecessor gaps as `(u,v)=(S_{d-1}-S_d,S_{d+1}-S_d)`. The existing exact branch work already covers every sector with a positive gap: edge / near-edge / center strict mixed-sign sectors, all structural `(+ ,0)` / `(0,+)` sectors, and now the unique central `(+,+)` sector. The only atlas sectors apparently left are `(-,0)`, `(0,-)`, and `(0,0)`. But on these sectors the old global kernel lower bound is not merely a lower bound: directly from the integral definition,

`Phi_theta(u,0)=kappa exp(u)` for `u<=0`, `Phi_theta(0,v)=kappa exp(v)` for `v<=0`, and `Phi_theta(0,0)=kappa`,

where `kappa=theta/((2-theta)(3-theta))`.

So the candidate stronger statement is: **after the 21:23Z correction, the four-layer exponential moment is exact, not just upper-bounded.** The deterministic max/min identity is exact; earlier checkpoints already made all adjacent-pair terms exact; and an exhaustive `5!` strict-order atlas should show that the triple-slack branch partition is complete.

Methods for this run:

- **B6 — deform to a point already solved.** Deform the remaining “unknown sector” claim to the boundary sectors where the kernel collapses to an elementary Laplace identity. Expected test: the supposed residual loss vanishes identically.
- **B17 — look for the same numbers elsewhere.** Interpret the sign atlas as a phase-type partition: the repeated zero-gap patterns are exactly the sectors where the baseline coefficient `theta(1/(2-theta)-1/(3-theta))` equals `kappa`.
- **B27 — swap the quantifiers.** Instead of seeking one stronger pointwise minorant over all `(u,v)`, partition all strict layer-two orderings first and use the exact kernel appropriate to each chamber.

Counterexample-first test: enumerate all 120 strict orderings of `(Y_-2,...,Y_2)` and attempt to find one sign pattern not matched by an existing exact branch or the exact nonpositive boundary identity. If one exists, exactness fails and that chamber becomes the target. If none exists, prove coverage by explicit rank equivalences, combine the parameter-uniform exact-pair formula with all later exact triple corrections, and only then reoptimize the Chernoff parameter.
