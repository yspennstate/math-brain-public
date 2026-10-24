# C0014: wiring annulus interfaces gives a lower comparison

Label: proof of a deterministic gluing correction, pending w347. It does not identify the DGFF log-resistance limit.

For a finite positive-resistance network separated into successive layers by interfaces, identify all vertices in each intermediate interface and replace the boundary terminal sets by wired terminals. If the resulting quotient is a series chain of wired layer networks, its total effective resistance is the sum of their wired effective resistances. Rayleigh monotonicity gives

    sum of wired layer resistances <= original effective resistance.

Identification introduces extra zero-cost connections and decreases effective resistance. It does not, by itself, give the reverse upper bound. For an upper bound by Thomson's principle, unit flows in consecutive layers must have matching distributions on the intermediate interface.

An explicit counterexample has vertices s,a,b,t and resistances r(s,a)=r(b,t)=1, r(a,t)=r(s,b)=M>0. Before wiring a to b there are two parallel paths, each of resistance M+1, so R_original=(M+1)/2. Wiring a and b gives two successive parallel pairs with resistance M/(M+1), so their sum is R_wired=2M/(M+1). The ratio is (M+1)^2/(4M), unbounded as M grows. At M=100, R_original=50.5 and R_wired=200/101, a factor 25.5025 smaller.

The independently optimal wired-layer unit flows have incompatible interface currents. In the first layer the low-resistance edge into a carries M/(M+1); in the second layer the edge leaving a carries 1/(M+1). Their mismatch is (M-1)/(M+1). Joining these minimisers as a flow in the original graph violates Kirchhoff's law unless M=1. Wiring supplies the missing current transfer artificially.

The earlier C0014 attempt says "Rayleigh monotonicity gives R_eff(x, D_N^c) <= sum over dyadic annuli around x of the resistance across the annulus". If those layer resistances are independently wired terminal minima, this implication has the wrong comparison direction. The counterexample does not invalidate an upper construction using matched flows or a different, explicitly justified layer quantity. The Brownian-functional limit in that attempt remains a heuristic, not a consequence of Rayleigh alone.

Checks: exact Kirchhoff potentials, series/parallel values, the equality case M=1, and the mismatch of interface currents. No Gaussian-network limit is claimed.
