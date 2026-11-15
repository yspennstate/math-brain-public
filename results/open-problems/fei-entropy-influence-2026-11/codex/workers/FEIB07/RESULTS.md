# FEIB07 results

The product-kernel part is proved. The finite kernel search is complete, including a rigorous near-optimality certificate under conditional half retention. A new CI theorem for a previously unresolved FEI class was not obtained.

## Four-variable census

All entries are bits of coding cost per unit of total influence. Every maximum in this table is attained at truth table 0x0001, an input-negated AND_4. Source: census.py -> census4_summary.json and census4.npz. audit_exact_census.py independently recomputes rational output laws. Except for the retained-size rule, the table uses floating logarithms and is not an interval certificate.

| Kernel | Maximum R/I |
| --- | ---: |
| Identity baseline | 1.464975551199 |
| Product, retain i with probability I_i | 3.210843288753 |
| Independent half-thinning | 1.777176048303 |
| Keep or erase, equal probabilities | 1.619100963802 |
| Keep or delete one, equal probabilities | 1.501685622478 |
| Uniform retained size | 1.654570661729 |
| Uniform prefix, best coordinate order | 1.717301689758 |
| Uniform prefix, worst coordinate order | 1.717301689758 |
| Erasure/half-thinning mixture, weight 7/32 on thinning | 1.602039532377 |
| Erasure/uniform-size mixture, weight 1/3 on uniform-size | 1.602119834920 |
| Erasure/half-thinning mixture, optimized for f | 1.602039014689 |
| Rational retained-size rule | 1.601162892531 |

The best tested nonidentity envelope has maximum 1.501685622478, attained by the delete-one rule at the worst witness. It shrinks less than half in rows of size above one. Near-identity perturbations can approach B arbitrarily closely, so this is not an unrestricted optimum.

The retained-size rule retains |U|/2 coordinates in conditional expectation in every row. Its certified maximum lies in the interval

    [1.60116289253127354937605371588406570678648642,
     1.60116289253127354937605371588406847027166180].

For every kernel satisfying the same mean-retention constraint, including f-dependent kernels, the worst four-variable ratio is at least 1.60116289073089139330247724695121708345789606. The certified gap is at most 1.80038215607357646893285138681376574E-9. Source: certify_size_kernel.py -> certified_size_kernel.json; exact series proof in PROOFS.md section 12.

## Named examples

Source: structured.py -> structured.json and structured.csv. These are complete finite sums on explicit truth tables. Prefix orders are exhaustively searched only up through five variables.

| Function | H (bits) | B (bits) | I | R_half/I | R_erase/I | R_delete-one/I | R_fitted/I |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| AND_5 | 1.132418875 | 0.456637625 | 0.312500000 | 1.795637472 | 1.578425702 | 1.490284688 | 1.570378499 |
| majority_5 | 3.325375780 | 1.513999507 | 1.875000000 | 1.554132888 | 1.340799737 | 1.340799737 | 1.344200241 |
| tribes_w2_t5 | 5.830604224 | 2.313544727 | 1.582031250 | 1.740808433 | 1.709102475 | 1.504985086 | 1.678455376 |
| tribes_w3_t3 | 5.255148258 | 1.969254437 | 1.722656250 | 1.521523855 | 1.504294562 | 1.233059868 | 1.467894128 |
| address_3 | 6.000000000 | 1.500000000 | 2.500000000 | 1.249022500 | 1.000000000 | 0.775069542 | 1.012935046 |
| extremal_0x0000000e | 2.334164454 | 1.017182569 | 0.687500000 | 1.774980138 | 1.656559353 | 1.519652872 | 1.636739865 |
| extremal_0x008eeeee | 3.608458593 | 1.346099609 | 1.625000000 | 1.435984187 | 1.443753606 | 1.194585391 | 1.413519910 |

Source symmetric.py -> symmetric.json: at majority_257, B/I=2.389216120157, independent half-thinning R/I=2.709122424472, erasure R/I=2.467319695043. The influence-matched product ratio is 4.798675050454; its provable lower bound is 4.327156943029.

Source structured.py -> compositions.json: repeated balanced composition of 0x008eeeee has limiting B/I and erasure R/I equal to 2.153759374820. These limits already invalidate extrapolation of the four-variable maxima.

## Proved statements

Full derivations are in PROOFS.md.

- R_r=B+D_2(mu||nu); identity is the only minimizer on positive-input-mass rows.
- Choosing lambda_i=1-I_i gives sum_i I_i log(1/I_i) <= R_r <= sum_i h_2(I_i) <= sum_i I_i log(1/I_i)+(log_2 e)I. This recovers the requested shape, but that kernel fails a uniform CI bound for AND and majority.
- Any diagonal bound r(U,U)>=2^{-|U|} gives B<=R_r<=B+I. Erasure and delete-one improve the slack bound to the variance v. These comparisons leave the unknown B.
- Direct calculations prove CI bounds for AND, address and disjoint-term DNF; balanced gates propagate explicit B/(I-1) bounds through disjoint composition. These are known FEI classes, not a new class.
- The class with every influence below I/sqrt(n) is equivalent to general FEI under disjoint XOR amplification. It is not a weakening of the general problem.
- Fixed-cap restrictions or deterministic proper shrinking can have infinite cost.

## Checks

Sources: audit.py -> audit.json, audit_exact_census.py -> audit_exact_census.json, and run_validation.py -> validation_run.json.

- 65,536 four-variable truth tables, including 65,534 nonconstant ones. Direct character-matrix Fourier transforms and edge-flip influences agree exactly with the main implementation.
- 9,660 seeded random and biased cases beyond four variables; no tested universal inequality was violated.
- 51 monotone disjoint-term DNF cases in the full four-variable census satisfy the exact formula; maximum float error 2.22e-16 bits.
- 12 independent scalar rational cases, with 70-digit logarithms; maximum discrepancy 4.44e-16 bits.
- Every fixed rational family and every prefix order was checked over the complete census using integer output numerators; maximum difference 3.55e-15 bits.
- All 6 validation processes exited successfully at nice 10, with 1 numeric-library thread. Largest measured RSS was 314,818,560 bytes, from resource.getrusage on Darwin.

No reported numerical maximum is claimed in dimensions beyond those computed. Only the retained-size maximum and its minimax gap have rigorous interval certification.
