# FEIB03 report

Completed the brief's proof attempts, counterexample searches, witnesses and independent checks. The general containment conjecture remains unresolved. Full proofs are in [PROOFS.md](PROOFS.md); the dimension-by-dimension table and experiment details are in [RESULTS.md](RESULTS.md). [RUN.md](RUN.md) gives reproduction commands.

The main positive result is the proposed balanced composition law:

    A(f composed with g) = A(f) + I(f) A(g).

It holds for balanced inner gates on disjoint blocks, including an unbalanced outer gate. The heterogeneous version is A(f(g_j))=A(f)+sum_j I_j(f)A(g_j). Upward probabilities factor by the blocks that the target spectral set intersects, which gives a direct proof. Self-composition preserves A/(I-1) exactly. Different balanced gates give a convex combination of their balanced ratios. Without balance of the inner gates the formula fails, already for AND_2 composed with AND_2.

This also proves equality of the two universal optimal constants, sup_all A/I = sup_balanced A/(I-1). Multiplication by a fresh dictator gives one inequality; self-composition gives the other.

For the known 18-variable K3,3 matching gate with nine coins, the audited values are

    A = 4.36182926443619665641409662023246036025881003558794... bits,
    I = 261/128,
    A/(I-1) = 4.19785072066039978963161178488537538430923071094178....

These give a lower bound for a universal A-conjecture constant. They are measurements of a known gate; I make no novelty claim. `verification.json` records exact integer Fourier data and agreement to 100 decimal digits between dense and separate sparse calculations. The sparse calculation uses direct core Walsh sums, Hall's matching condition and direct superset sums. Physical edge counts and 100 face-derivative checks supply further checks.

The strongest obstruction found is a Boolean family defeating constant payment in a coordinate restriction induction. On m even core coordinates, use a paired bent quadratic in one slice and flip its value at one point in the other. Then I_i=2^(-m), while Delta_i A/I_i=m+o(1). Multiplication by a fresh dictator makes the parent and both slices balanced without changing this ratio. Thus a potential depending only on the means cannot repair that induction. The same construction has J<=2 I_i/ln(2) while normalization entropy divided by I_i grows like m, so J cannot pay that entropy up to a constant multiple of I_i. `PROOFS.md` gives the exact grouped formula and its remainder estimate; `routes.json` checks the formulas and balanced lifts through ambient dimension twenty.

The requested verdicts are:

(a) Generalized influences: a levelwise tail estimate is proved, but factorial moments remain unpaid; parity refutes the naive estimate sum_{|S|=2}I_S<=C I. The consulted KKLMS theorem retains its logarithmic loss.

(b) Coordinate recursion: the exact identity A(g)=A(a)+A(d)-J is proved; constant local restriction payment and direct normalization payment by J are refuted by the bent-slice family, including its balanced lift.

(c) Positive association: the pointwise product estimate, a fixed exponential correction in |S|, and the uncorrected averaged replacement are false. A valid averaged replacement adds I/ln(2), but still leaves marginal influence logarithms.

(d) Second moment: the stated identity for Q=Pr[S subset U] is correct; Jensen gives a lower bound for A. A balanced mux-address family has A=3/2+3k/4 and Q=(3/16)(1+(3/8)^k), refuting a universal reverse estimate A<=C log2(1/Q).

The exact exhaustive A/I suprema for n=1,2,3,4 are respectively 0, 1, 19/12 and 31/16. The balanced A/(I-1) suprema are respectively undefined, 0, 3 and 4. `census_certificate.json` certifies the bounds and attainment with integer products and no logarithms; `audit_c.out` independently reproduces the census with direct transforms.

For n=5 through twenty, the searches scored 15,897 truth tables, covering the prescribed structured families, random DNF, compositions and hill climbs with flips or balanced swaps. AND_n supplied the largest observed A/I in each of those dimensions; at n=20 this is 2.79999828338623046875. These are observed values, not established suprema. Balanced observed maxima reach the matching-gate value above at n=18 and retain it under padding at n=19 and n=20. Every witness is indexed in `final_best.json`.

I also exhausted all 21,147 partitions of the nine matching-gate sites into shared coins. Every influence numerator was checked exactly, and all partition scores were ranked at 80 decimal digits. Independent coins remain best in that family. Some intermediate partitions improve modulo sharing slightly at n=13 through sixteen. This is a finite increase, not a diverging balanced family. The optimal witnesses were checked by dense truth tables and direct sparse calculations; see `coin_partitions.json` and `coin_partitions_exact.json`.

Verification covers every subset's face derivative for all 65,812 functions in dimensions one through four, 496 composition checks, and 300 additional random or structured cases through dimension twenty. `verification.json`, `stress.json`, `routes.json` and the integer census certificate record the checks. Larger composition towers and address examples are explicitly marked as evaluations of proved formulas, without allocating their full truth tables. The general conjecture has neither been proved nor falsified by these tests; a richer recursion potential or a useful spectral tail bound remains open.

All work stayed in this folder. The main verifier recorded priority 10, one-thread environment limits and peak resident memory 380,010,496 bytes (`verification.json`). The folder is below the storage cap; `FINAL_AUDIT.txt` records the final file check and cleanup. Source, outputs and witnesses are retained. No subagents or extra model workers were started.

The startup memory and shared NOTES.md were read. Brain recall helped identify the matching-and-coins gate and avoid repeating earlier entropy-induction claims. Math recall reported that its store was unavailable. Fleet rules prohibit shared writes, so durable findings are left in [MEMORY_HANDOFF.md](MEMORY_HANDOFF.md) for the launching session. The proofs are written out and computationally audited; an independent mathematical referee has not reviewed them.

Task: "Do the brief fully and carefully" — FEIB03, started 2026-11-10 01:09 +04.
