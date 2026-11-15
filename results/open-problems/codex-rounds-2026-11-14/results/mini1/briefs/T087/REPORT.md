VERDICT: PARTIAL finite-scale reduction and conditional equivalence of one-arm and averaged two-point exponent existence

For nearest-neighbour Bernoulli bond percolation on Z^d, let π(n) be the one-arm probability, X(n)=sum_{x in B_n} P(0↔x), and K_n the number of open components in the induced graph on B_{2n} meeting both B_n and ∂B_{2n}. PROOF.md proves the unconditional finite-scale inequality

    X(2n) ≥ (2n+1)^d π(3n)^2 / E K_n.

Together with a separated-arm upper bound, this gives the following conditional reduction. If E K_n is at most subpolynomial, existence of π(n)=n^(−a+o(1)) with 0<a<d/2 is equivalent to existence of X(n)=n^(s+o(1)) with 0<s<d, and s=d−2a. It also yields the supremum envelope law sup_{||x||≥n} P(0↔x)=n^(−2a+o(1)). Only logarithmic limits are assumed; no regular variation is used.

If the uniform pointwise two-point exponent b additionally exists in (0,d), any hyperscaling defect forces

    E K_n ≥ n^(b−2a+o(1)),     b≥2a.

For d=3 this defect is 1+η−2/ρ. Its vanishing, combined with separately proved β=ν/ρ and γ=ν(2−η), would give 3ν=γ+2β. None of those missing Z^3 inputs is established in this session. In particular, a supremum or averaged exponent does not prove the pointwise two-point law in T087.

The multiplicity approach is classical; this is a self-contained reduction, with finite-scale bounds and a transfer of existence in both directions. No claim of a new critical exponent or priority over earlier conditional hyperscaling work is made.

## Verification and commands

This was a proof task; no simulation, computed percolation data, or computational script was used. AUDIT.md gives a second derivation of the main factor by a variance argument, independent exact shell counts, and checks of exponent signs, boundary definitions, dependence, rare large counts, endpoint cases, and integer-scale limits.

Web queries and opened primary sources are recorded in LOG.md and SOLVED_ELSEWHERE.md. The recent-literature pass finished in less than ten minutes. No verified complete solution of T087 was found. Related high-dimensional and hierarchical results do not answer the cubic-lattice question. A September 2026 continuity manuscript was located but its PDF could not be read by the web tool, so its claim is not certified here.

Local orientation commands and relevant output are in LOG.md. In particular, the startup command `OMP_NUM_THREADS=1 nice -n 15 python3 .../brain.py recall ...` reported `nice: setpriority: Operation not permitted`; it completed, and no further Python or numerical workload was launched. The task's folder-only restriction took precedence over shared checklist/mesh writes. No git or external posting was performed.

## What failed or remains uncertain

The core unproved geometric condition is subpolynomial **expected** K_n at p_c on Z^3. A bound in probability is insufficient because rare configurations can dominate its expectation. At least one of the two exponent-existence statements must also be proved. Pointwise lower bounds and near-critical matching remain missing. The literature review establishes no novelty claim for this particular logarithmic formulation.

## Next work

Target a bound E K_n≤n^ε for every ε>0 for the exact free-boundary, induced-box component count defined above. A finite-size computation could test this quantity but would not prove an asymptotic bound. In parallel, compare the logarithmic-existence transfer with the precise hypotheses of the classical conditional hyperscaling theorems before claiming an improvement. Keep the stated boundary convention; wiring boundary vertices invalidates the pair-connectivity argument. AUDIT.md explains a separate whole-lattice-cluster variant.

Task: “push this problem forward by one checkable piece” — T087, 14 November 2026, approximately 20:54 Asia/Tbilisi.
