# C0056: adversarial core-proof packet

The complete intake asks for both weak-disorder AC spectrum and finite-volume GOE statistics. This lane isolates the uniform-law spectral subproblem. Full-target openness is UNKNOWN: a September 23 primary preprint reports the spectral portion, but its full proof has not been audited here.

The single hardest unproved input in w480's route is (LG): for fixed lambda>0 and a bounded open J, the infinite-volume one-site cavity damping b(E,eta)=eta+Im<h,(H^(0)-E-i eta)^(-1)h> must satisfy sup_{0<eta<=1} E integral_J log(1+1/b(E,eta)) dE < infinity. This is a sufficient route-specific premise, not a characterization of every possible delocalization proof. No proof of (LG) has been obtained.

Before reading the paired statement, I saved INDEPENDENT_OBSTRUCTION.md, disproving the conversion from annealed first moments to quenched AC, and CAVITY_REDUCTION.md, proving a stronger inverse-damping reduction. Deterministic comparison gives only |S_lambda-S_0|<=6 lambda/eta^2, which loses control in the required fixed-lambda boundary limit. The lattice cavity neighbors are correlated; a tree recursion is unavailable.

After reading the paired statement, I independently derived its whole-line entropy identity and verified the constants. I also gave a direct null-set proof that annealed entropy control implies pathwise absence of singular mass; see PAIRED_LEMMA_INDEPENDENT_CHECK.md. The reduction is rigorous subject to (LG). The diagonal example has b=eta, so (LG) diverges while spectral averaging remains uniformly bounded. This rejects replacing (LG) by a first-moment bound.

At fixed finite volume the cavity damping goes to zero at almost every energy, and the logarithmic integral diverges. This does not rule out a coupled volume/eta scheme with separately proved uniform controls. Any finite-volume route must state that scheme and justify its transfer. The paired finished proof is still to be inspected at this checkpoint.

The recent preprint explicitly recognizes that positive boundary density a.e. does not alone exclude exceptional singular mass. The present counterexample is not a verdict on that preprint's certificate construction or final spectral argument.

Own derivations remain independently unchecked until w482 reviews them. Requested model names are not served-model evidence. No full solution, theorem promotion, store ingestion, or successful retrieval is claimed.

NEXT: Audit w480's finished entropy/finite-volume proof and deliver a scoped verdict; retain (LG) and GOE as unresolved.
