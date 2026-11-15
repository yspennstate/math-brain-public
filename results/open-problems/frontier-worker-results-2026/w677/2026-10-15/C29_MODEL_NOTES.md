# C29: slowly growing entry budgets, target 1

Status: design and numerical protocol, not a recurrence claim. No threshold has been determined.

Keep the C27 ordinary motion and suppressed overflow excursions, but at absolute depth j use K_j, the smallest positive integer with 4^K_j >= (j+2)^2. The parent response has K_j inputs and uses children with K_(j+1)-input cumulative responses. The resident still appears once. The joint child responses persist between inputs. Waking below the chosen horizon is suppressed, while ordinary excursions below that horizon remain possible.

This differs concretely from C28: there is no common finite entry cap throughout the infinite subtree. At p=1/4 its all-parent sterile-prefix probabilities satisfy delta_j=4^(-(K_j+1)) <= 1/(4(j+2)^2). Their sum is at most 1/4 by comparison with the integral of x^-2 on [1,infinity). Consequently the probability that a fixed ray segment has none of THESE sterile prefixes is at least 3/4, uniformly in its length. This is NOT a lower bound on activation: absence of these barriers is only a necessary condition. It proves neither infinite expectation nor recurrence. It shows only why C28's particular summability argument no longer closes this family.

At maximum awakening horizon H, initialize the true ordinary leaf response at absolute level H, then apply T_(K_j,K_(j+1)) from j=H-1 down to 0. C27's queue argument extends to unequal finite input and child caps: use cumulative child maps of length K_(j+1), K_j serial seeds, and the same first-zero identity. The stochastic order and ordinary lower coupling have the same proof. This extension is not independently audited.

Numerical protocol: separate independent empirical-population runs, starting with H=20,32,64; p=1/4 and the known-transient negative control p=6/25. Record conditional PGF and tail standard errors and variation between complete independent runs. All inherited population bias remains unbounded. Checkpoints carry their absolute level: an unfinished intermediate response is not a depth-H root result. A phase threshold cannot be read off positive PGF because of C26's extinction atom. Use the root tail profile and depth growth as numerical evidence only.

Memory estimate for M samples: M*(1400+350 max_j K_j) bytes, under 800 MB; require 2 GB free RAM and 1 GB free disk. One CPU thread, NumPy integer counts guarded before 10^11, no rigorous rounding claim. Each command advances at most 300 seconds, checkpoints after every level, and exits.

Frontier check 2026-10-15: exit 0, nothing close known. This is target 1, not a biased S_m refinement and not another T4 finite-cap obstruction.
