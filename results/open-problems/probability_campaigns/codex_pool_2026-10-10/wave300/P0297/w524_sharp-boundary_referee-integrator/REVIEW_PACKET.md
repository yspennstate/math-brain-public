# P0297 independent referee packet (2026-10-10)

## Source and scope

Gwynne and Miller, *Existence and uniqueness of the Liouville quantum gravity metric for gamma in (0,2)*, Problem 7.1, asks to compute the deterministic almost-sure dimension `d_gamma = dim_H(C,D_h)` for each fixed `0<gamma<2`. The associated parameters are `Q=2/gamma+gamma/2` and `xi=gamma/d_gamma`; the known anchor is `d_sqrt(8/3)=4`. [Primary statement](https://link.springer.com/article/10.1007/s00222-020-00991-6), section 7.1. A 2026 ICM primary survey still says the general value is unknown, but this is not an exhaustive search to 2026-10-10: present openness remains **UNKNOWN**. Neither peer claims a solution.

The metric KPZ paper states its exact equality only for deterministic Borel sets or random Borel sets independent of `h` (Theorem 1.4); its thick-point formula is for each fixed `alpha` (Theorem 1.5). Corollary 1.7 supplies full metric dimension of the `gamma`-thick points. [Gwynne--Pfeffer, arXiv:1905.11790v3](https://arxiv.org/html/1905.11790).

## Independent verdicts

| Peer claim | Verdict | Reproduction and limit |
| --- | --- | --- |
| w522 C1, archive normalization | KEEP | From `xi=gamma/D`, `2Q/xi=(1+4/gamma^2)D`, so the archived `D=2Q/xi` is false. At the Brownian anchor it gives 10, while `D=gamma/xi` gives 4. Only those two archive strings are cleared for repair; the rest of that attempt is not audited. |
| w522 L1, sharp thick-point maximum | KEEP | `Q-2=(2-gamma)^2/(2gamma)>0`; multiplying the deficit by `xi(Q-alpha)` gives `gamma Q-gamma alpha-2+alpha^2/2=(alpha-gamma)^2/2`. Unique equality at `alpha=gamma` in the stated interval. |
| w522 L2, critical corner | KEEP | With `delta=2-gamma`, `beta=2-alpha`, `xi F=(2beta-beta^2/2)/(beta+delta^2/(2gamma))`. For `beta/delta^2 -> k`, finite `k`, the limit is `8k/(4k+1)`; for infinite ratio it is 2. Paths `beta=delta^3`, `k delta^2`, and `delta` realize all values from 0 to 2. Algebra only, no critical metric claim. |
| w522 L3, KPZ optimizer and scale | KEEP | For `0<x<=2`, `a=Q-sqrt(Q^2-2x)` lies in `(0,gamma]`, and `x=Qa-a^2/2`. The deficit is `(alpha-a)^2/[2xi(Q-alpha)]` where the unclipped numerator is nonnegative; outside this region the clipped value is 0 below the positive maximum. At `x=0` every clipped value is 0, so uniqueness fails exactly there. `T(x)/D=a/gamma` cancels `D`; the two numerical witness functions differ by `1/36` at gamma 1. These witnesses are not alternative LQG metrics. |
| w522 L4, inverse stability | KEEP | `Y'(x)=1/sqrt(Q^2-2x)`, so the optimal fixed-gamma Lipschitz constant is `1/(Q-gamma)=2gamma/(4-gamma^2)`. The square-root difference inequality gives uniform `sqrt(2)|x-y|^(1/2)`. At `x=2-epsilon`, `y=2`, then gamma approaching 2, equality tends to `sqrt(2epsilon)`, proving both constant and exponent sharp. Only the normalized inverse `Y=xi T` is controlled. |
| w523 L1--L2, independent boundary derivation | KEEP | Its `INDEPENDENT.md` was saved before it opened w522's packet. I repeated the quadratic and endpoint substitutions above; its fixed-`xi` limit is a statement about an algebraic family, not about `xi_gamma` or critical LQG. |
| w523 C3, dependent-set KPZ counterexample | KEEP | For fixed gamma, put `X=T_h^gamma`. Source Eq. (1.11) with deterministic ambient `U=C` gives `dim_E X=2-gamma^2/2`; Cor. 1.7 gives `dim_D X=D`. If the independent-set equality were extended to this dependent set, its right side would be `xi Q D-(xi^2/2)D^2=gamma Q-gamma^2/2=2`. The discrepancy is `gamma^2/2>0`, or `4/3` at the Brownian anchor. Both source events concern one fixed gamma, so their finite intersection is valid. The thick set is Borel via a jointly continuous circle-average version and a countable rational-radius limit construction. This refutes only the unrestricted auxiliary equality, not P0297. |

## Remaining gap

None of these identities computes the actual LFPP distance normalization exponent `xi_gamma`, or equivalently the metric dimension. The next mathematical step is an independent crossing-distance exponent estimate that pins down `xi_gamma` as a function of `gamma`; optimization of formulas that already contain `xi_gamma` is circular. The archive normalization repair should be applied only after the reviewer inspects its unified diff. The two peers are not being certified as solving P0297.

## Review provenance

I checked the primary paper's equations (1.5), (1.9), (1.11), (1.12) and Corollary 1.7 directly, and independently rederived every algebraic equality above. w522's 1,126-case author run and w523's numerical checks are supporting checks, not formal proof receipts. No admitted placeholder or theorem-level machine certification is claimed. This packet is the independent review of the peer results; it does not review their review documents.

NEXT: Send this scoped KEEP packet to the validating coordinator for the two peer bundles and the narrow D0049 source correction; obtain a new independent LFPP normalization estimate before any parent-problem claim.
