# FEIB07 report

The coding route recovers the requested influence-log bound, and the four-variable kernel search is complete. The strongest finite result is a conditional half-retention rule whose worst R/I is certified as 1.601162892531273549..., within 1.801e-9 of the optimal worst ratio among all kernels with E(|T| | U)=|U|/2. The requested proof for a previously unresolved general class remains open.

## What is proved

PROOFS.md gives full proofs. With output law nu=mu r, the exact coding slack is R_r-B=D_2(mu||nu). The explicit product choice lambda_i=1-I_i gives

    B <= R_r <= sum_i h_2(I_i)
             <= sum_i I_i log_2(1/I_i)+(log_2 e)I.

It also has R_r>=sum_i I_i log_2(1/I_i), so that choice cannot yield CI on AND or majority. Applying the brief's Theorem 1 recovers H<=2 sum_i I_i log_2(1/I_i)+(2+2log_2 e)I-2Var. Direct entropy subadditivity already gives the stronger H<=sum_i h_2(I_i). This is a recovery of the requested shape, not a new entropy bound. Han's theorem has that shape; KKLMS instead supplies a degree-log entropy estimate and concentration. The primary links and precise distinctions are in SOURCES.md and PROOFS.md section 2.

Direct calculations give explicit bounds for AND, address, disjoint-term DNF with unequal term widths, and balanced formulas over finitely checked gates. For disjoint-term DNF, writing w_min for the shortest term and c=log_2 e, the proof gives B<=(1+4c/w_min)I and erasure/delete-one cost <=[1+(4c+2)/w_min]I. This does not cover overlapping DNF. Majority can use the established symmetric-class theorem; no general FEI assumption is needed for that class.

A useful negative result is exact: a CI theorem for all functions whose individual influences are below I/sqrt(n) would prove general FEI. Taking 4d disjoint XOR copies of any d-variable function preserves H/I and B/I while meeting that strict influence condition. The explicit truth-table check is in audit.json.

## Kernel verdicts

- Identity: optimal, but its cost is B itself; no independent FEI argument.
- Influence-matched product: proves the requested influence-log shape; fails uniform CI for AND and majority.
- Fixed product thinning: cost lies between B and B+cI; general CI is equivalent to FEI. It works on the named known classes using their structural bounds.
- Keep or erase: cost is B plus at most Var, and exactly B+1 when balanced. Strong simple baseline; it leaves the B estimate unresolved.
- Keep or delete one: same variance slack bound; best tested nonidentity census maximum 1.501685622478. It retains more than half on larger rows, so it is not comparable as an equal-shrinkage optimum.
- Uniform prefix with an f-dependent order: cost <=B+E log(|S|+1). All coordinate orders were evaluated in the four-variable census. No order-selection theorem removing B was found.
- Uniform retained size/random order: the same diagonal bound; a valid restriction-mixture interpretation. No new general-class bound.
- Convex mixtures: improve finite ratios; optimizing erasure plus half-thinning reaches worst 1.602039014689 on four variables. This optimization alone is not a structural proof.
- Rational retained-size stopping: the best half-retention rule found. Worst ratio 1.601162892531, certified within 1.80038215607357646893285138681376574E-9 of the half-retention minimax optimum on four variables. The explicit extension to all dimensions obeys B<=R<=B+I; no universal CI theorem is obtained.
- Fixed-cap live sets and deterministic proper stops: can give infinite cost at maximal supported spectral sets. Positive diagonal mass is essential there.

Without a prescribed amount of shrinkage, nonidentity kernels can approach identity and hence B arbitrarily closely. Conditional half retention was introduced to make the finite optimization nonvacuous; it is not a constraint present in the original lemma.

## Numerical results and verification

RESULTS.md has the complete comparison table. census4.npz stores every cost on all 65,536 truth tables, and census4_summary.json records maxima. H and B are in bits; R/I is bits per unit of total influence. Every four-variable maximum in the comparison table occurs at 0x0001, up to the stated ties.

The fitted retained-size rule has exact rational row probabilities. certify_size_kernel.py evaluates every four-variable output law with integer numerators and bounds logarithms by a rational series with an explicit remainder. It also constructs an AND_4 dual bound valid for every kernel satisfying conditional half retention, including f-dependent ones. certified_size_kernel.json contains the interval and the gap certificate. This finite near-optimality result does not extend the numerical maximum to higher dimensions.

The checks in audit.json include 9,660 seeded larger random/biased functions, every four-variable Fourier transform checked against a direct character matrix, edge-flip influences, 51 recognized monotone disjoint-term DNF cases, and 12 scalar rational cases with 70-digit logarithms. audit_exact_census.json independently checks all fixed rational output laws and all prefix orders across the whole census; its largest float-log discrepancy is 3.55e-15 bits. The fitted rule alone also has a rigorous interval census, rather than only float checks.

structured.json contains 27 named finite cases, including both five-variable truth tables, tribes, majority, AND, address and explicit compositions. symmetric.json evaluates majority through n=257; there B/I=2.389216120157, already above the four-variable maxima. compositions.json gives the balanced 0x008eeeee composition limit 2.153759374820 for both B/I and erasure cost/I. These are explicit warnings against extrapolating the census as a universal constant.

Run `python3 run_validation.py` from this folder. The final run passed all 6 stages. validation_run.json records one numeric-library thread, nice 10, and peak measured process RSS 314,818,560 bytes, below the requested process cap. The discovery scripts search_size_kernel.py and search_general_size.py reproduce the parameter search separately; the validation uses the fixed rational rule.

## Remaining mathematical obstruction

No proof is supplied for all monotone functions or general overlapping width-w DNF. The disjoint-DNF proof uses a factorization that overlap destroys; a bound on the resulting interactions and cancellations is missing. The small-influence class is equivalent to the full conjecture by the proved reduction. The coding comparisons B<=R<=B+O(I) do not fill that gap. The brief is complete as a computational investigation and partial proof package; its requested new-class FEI theorem is unresolved.

Brain recall was consulted for orientation, but it did not provide the coding step; the math-store command reported no installed store. The supplied NOTES.md was useful. Fleet rule 3 was followed: all writes stayed in this worker folder, with no mesh, checklist, brain, publishing, git-push, or external-message writes.

Task: “the coding route to B <= C I (Lemma 2 and its kernel generalisation)” — 10 Nov 2026, 01:29 +04, worker start record.
