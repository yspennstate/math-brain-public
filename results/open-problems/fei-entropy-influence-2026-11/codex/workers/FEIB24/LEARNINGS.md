# FEIB24 handoff notes for the launching session

These files remain local to FEIB24. No shared brain writes, checklist changes, mesh posts or publishing were made, following the fleet's narrower rule. The launching session can decide which results deserve durable memory.

PROVED: the original hidden-coordinate family has H^- <= 2I; after arbitrary disjoint balanced odd monotone substitutions the bound H^- <= 5I still holds. The proof uses parity leakage, the exact leaf activation formula, and I(phi)>=1, rather than a guessed per-coordinate bound. See PROOFS.md sections 2–5 and proof_checks.json.

PROVED: both directions of the normalized level-two coordinate rule fail uniformly. The original hidden gadget defeats maximum W_i^(2)/Inf_i. For the minimum rule, use an even-dimensional majority threshold with two complementary middle-layer points made dependent on x; all degree-two coefficients through x vanish while its erasure ratio diverges. See PROOFS.md sections 6–7. paired_hidden.json checks the finite examples through nineteen variables.

PROVED: choosing the variable in most shortest minterms fails on the original hidden gadget with MAJ3 substitutions; x becomes the unique maximizer of that term count and retains its divergent ratio. Largest and smallest influence rules also fail, with explicit constructions in section 6.

PROVED: the two necessary constraints mu({i})=Pr[i in U]^2 and sum_i Pr[i in U]^2<=1 do not force bounded erasure/influence for a probability law. The conditioned-product-plus-singletons construction in section 9 satisfies both and has an unbounded ratio. This is a limitation of a proposed proof route, not a Boolean counterexample.

CHECKED NUMERICALLY: full monotone permutation census through six variables, complete unrestricted NPN comparison through five, and finite searches/constructions through twenty. All three unrestricted extrema through five equal the monotone extrema. The six-variable best-coordinate maximum is 2.9444953038718586. The eighteen-variable OR3 of AND3 of OR2 has all-coordinate ratio 3.7137160185387623. Original truth tables, DNFs, hashes, audits, and high-precision recalculations are saved.

CAUTION: the brief's exact equality of optimal entropy and minimum-coordinate erasure constants is not proved by the supplied reductions; only C_*-2log2(e)<=G_*<=A_*<=C_* follows there. The 6.5218 record is already monotone and is an amplified bound, not a finite seed's H/I or min E_i/Inf_i. LITERATURE.md records opened primary sources.

OPEN: all-dimensional monotone FEI; a dimension-independent theorem for the shortest-minterm/shortest-zero-certificate selector; and a monotone function with minimum coordinate erasure ratio above four within the finite dimension budget. These are mathematical gaps after the stated calculations, not unrun checks.
