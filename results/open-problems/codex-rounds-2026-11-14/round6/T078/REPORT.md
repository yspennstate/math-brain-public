VERDICT: PROVED uniform sparse injection energy bound with isolated removed sites

The round 5 full-lattice bound holds. An independent pair-interaction proof in [PROOF.md](PROOF.md) recovers its coefficient 1000 (in fact 870 suffices). The brief literature check found the same previously recorded solution claim and no newly established resolution. This work does not prove T078.

The new result extends the spatial estimate to the cubic lattice with any set Z of removed vertices satisfying |z-z'|_infinity>=3 for distinct holes. Z may be infinite. An explicit linear rerouting operator preserves divergence at surviving vertices for currents with zero divergence at holes and increases undirected energy by at most a factor seven, independently of the number of holes.

Consequently, m labels satisfying the round 5 growth bound L(1+r)^alpha, 0<=alpha<1, may inject mass at most one each at surviving sites within distance R, with aggregate current energy at most

    7000 L(1+R)^alpha m/(1-alpha).

The same bound holds for every finite killed Dirichlet problem in the surviving graph. A corresponding linear capacity lower bound follows. Labels may repeat, endpoints may coincide, and finite volumes need not contain the bypass cubes. The proof treats deleted edges explicitly.

Checks: five displayed paths bypass each hole; their exact overlap calculation bounds correction energy by six times deleted-star energy. A separate extension of test functions gives the same factor seven. A two-by-two matrix calculation checks the local coefficient. Arbitrary signed currents, infinite hole sets, separation exactly three, zero masses, alpha=0 and finite-volume boundaries are included. A one-site example gives energy 1/5 next to a removed vertex versus 1/6 without it, checking the boundary convention. Six holes surrounding a source show that a component envelope alone cannot replace the source's strict local counting condition; that example does not contradict its theorem.

Commands: inventories used `rg --files`; prior reports, logs and proofs and the final proof were read with `OMP_NUM_THREADS=1 nice -n 15 cat ...`; clock and final file checks used the same prefix. There were no earlier mathematical scripts to rerun. Web search/open supplied the brief literature check; read-only GitHub connector fetches inspected RegularComponents.lean, FlowCongestion.lean, FlowRouting.lean, HullRouting.lean and RegularKernels.lean at revision `4eaee87548250b2682affda7d05d947c05554bae`. Source links are in PROOF.md. Writes used apply_patch only in this folder.

What failed or remains uncertain: raw source opens returned cache misses, then connector reads succeeded. The sandbox denied priority adjustments; no numerical script, heavy computation or Lean build was run. No source error was found and no full proof audit is claimed. The separation assumption is a different geometric restriction from Regular: it excludes nearby holes, while Regular permits controlled clusters. The factor seven is not claimed optimal. No novelty claim is made for local current rerouting.

Next worker: extend the bounded rerouting comparison from single holes to controlled finite clusters, with explicit source accessibility. For the exact source hypotheses, start with `surviving_boundary_confined` in [HullRouting.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/HullRouting.lean), especially its calls of `boundary_connected` and `interpolate_near_confined`, then the radial routing used by `routed_lattice` in FlowRouting.lean. The remaining issue is bounding detours and congestion when component sizes grow with distance. Random regularity and the return comparison still need separate checks.

Task: “take the NEXT checkable step on this problem, building on that work” — session date 2026-11-15 +04; first recorded local clock 10:36:10 +04, exact user-message clock time unavailable.
