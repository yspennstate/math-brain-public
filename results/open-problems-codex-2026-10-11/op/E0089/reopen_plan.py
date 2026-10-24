from pathlib import Path
p=Path('SECOND_ATTEMPT.md')
p.write_text('''# E0089 second attempt — 2026-10-12

Remaining gap from ATTEMPT.md: establish a fixed-K quenched conditional-success bound, or equivalently a sufficient independent-two-initial-set factorization, for complete bootstrap occupation in the critical n^-1/2 window. The first attempt only proved an abstract sufficient criterion and threshold tightness.

Two genuinely new approaches:

A. **Finite-round core peeling, local weak convergence, and dependency-graph CLTs.** Replace final core emptiness by the number of vacant vertices after t fixed rounds. On tree neighbourhoods its conditional mean and covariance are universal local polynomials. Show that graph fluctuations of that conditional mean are O(1), while seed fluctuations have order sqrt(n); obtain actual quenched Gaussian limits and independent-replica factorization for this local statistic. Then ask whether t can grow enough to resolve the critical bottleneck. For d=4,k=2 compute the critical recursion and its relaxation rate exactly.

B. **Two-colour density-dependent exploration of the configuration model.** Run two independent seed/core processes on one pairing, track the joint type of each half-edge (degrees remaining in each process), and try to apply a multivariate martingale CLT at the common saddle-node. A zero cross-covariance theorem for the limiting exploration noises would imply the desired graph concentration. Unlike the first attempt this would construct the actual coupled exploration, rather than merely restating the replica identity. The difficulty is that adaptive discovery in one process changes the conditional pairing law seen by the other, and there is no verified theorem here identifying or cancelling that covariance.

Selected approach: A. It permits a full theorem for a stronger local special case, a precise algebraic test at the smallest admissible (d,k), and a rigorous assessment of the depth needed to bridge to final occupation. Approach B remains a separately identified lead, not an asserted result.

Math-store query on the gap: "quenched bootstrap percolation random regular graph independent replicas k-core concentration Janson Luczak". Returned no applicable theorem; local/dependency-graph methods will be checked independently. Results and exact requests will also be logged in LITERATURE.md.
''',encoding='utf8')
p=Path('STATUS.md');s=p.read_text(encoding='utf8');s=s.replace(s.splitlines()[1],'NEXT: Prove a fixed-round quenched core-size CLT and compute the d=4,k=2 critical relaxation rate.');p.write_text(s,encoding='utf8')
