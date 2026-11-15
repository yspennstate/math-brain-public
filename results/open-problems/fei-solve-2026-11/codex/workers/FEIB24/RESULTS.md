# FEIB24 results

All logarithms are base two. H and E are in bits; I is the expected number of pivotal input bits at a uniform input, equivalently the expected spectral set size. Ratios are bits per unit influence. Constants and irrelevant coordinates are excluded from ratios; the enumerations include both. Truth-table bit x is one precisely when f(x)=+1, and input bit i corresponds to variable x_(i+1). DNF masks use the same input indexing. Monotone dual means -f(-x).

## Complete monotone census

CHECKED NUMERICALLY, WITH INTERVAL-CERTIFIED RANKINGS. `census.cpp` recursively generates lower-dimensional monotone pairs a<=b, then marks their complete permutation orbits. `census.log` records both the direct labelled count and orbit sum. Every representative was independently audited by direct integer character matrices, integer Walsh butterflies, direct edge counts, minterm reconstruction, Parseval, Han and singleton identities in `analysis.py`; see `audit.json`. No external monotone-census file was used.

| n | labelled functions | permutation classes | G_mono(n) | max H/I | max H^-/I |
|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 0.000000000000 | 0.000000000000 | 0.000000000000 |
| 2 | 6 | 5 | 2.000000000000 | 2.000000000000 | 2.000000000000 |
| 3 | 20 | 10 | 2.672488983973 | 2.955889582252 | 2.672488983973 |
| 4 | 168 | 30 | 2.672488983973 | 3.402475551199 | 2.704153205629 |
| 5 | 7,581 | 210 | 2.695887520153 | 3.623740399702 | 2.883566415773 |
| 6 | 7,828,354 | 16,353 | 2.944495303872 | 3.739764017898 | 3.030964070213 |

The direct-transform audit covered 16,611 representatives; the largest floating-point functional discrepancy was 5.329e-15 bits. `interval_census.py` enclosed every logarithm with outward-rounded interval arithmetic at 70 decimal digits, rounded it onto an integer grid of mesh 10^-40 bits, and performed all remaining sums, divisions, minima and comparisons with integers or rational numbers. Every finite winner is separated from all nonwinners; the surviving ties have exactly identical dyadic functional formulas. Exact rational enclosures and separation gaps are in `interval_census.json`. This certifies the monotone finite rankings, rather than merely rechecking the winning floating-point values.

Every class is in `census_n*.csv`. All maximizing permutation classes, their DNF expressions, truth tables and orbit sizes are in `all_extrema.json`. Each n>=2 has exactly two maximizing classes for each objective, related by monotone duality. One representative for each n and objective follows.

| n | objective | one extremal DNF as integer term masks |
|---:|---|---|
| 2 | minratio | 3 |
| 2 | HI | 3 |
| 2 | EI | 3 |
| 3 | minratio | 7 |
| 3 | HI | 7 |
| 3 | EI | 7 |
| 4 | minratio | 11 |
| 4 | HI | 15 |
| 4 | EI | 11 OR 13 |
| 5 | minratio | 23 OR 27 |
| 5 | HI | 31 |
| 5 | EI | 19 OR 29 |
| 6 | minratio | 15 OR 54 OR 57 |
| 6 | HI | 63 |
| 6 | EI | 45 OR 51 |

The n=6 G maximizer is MAJ3 of three disjoint AND2 gates, up to permutation or duality. Its three four-variable terms are complementary to three disjoint pairs. All six coordinate influences equal 0.1875, and every erasure equals approximately 0.552092869476 bits. H/I is maximized by AND6 and OR6. H^-/I has the separate witnesses listed above.

## Unrestricted comparison through five variables

CHECKED NUMERICALLY. `./census npn` evaluated every NPN representative saved by FEIB12, with input counts and SHA-256 hashes in `highprecision.json`; no outside worker code was imported. Input and output negation preserve squared Fourier coefficients, and coordinate permutations merely relabel the erasure ratios, so NPN representatives suffice. `./census unrestricted` independently exhausts all truth tables through n=4 up to output negation. All three unrestricted extrema through n=5 coincide with the monotone extrema above. The n=5 input has 616,126 classes. `npn.log` gives each extremum and its truth-table witness. The n=5 completeness certificate is inherited from FEIB12 rather than regenerated here; its file is pinned by hash. The unrestricted ordering uses binary64 comparisons and the same independently checked witnesses; the interval census certificate specifically covers the monotone census.

## Which coordinate

CHECKED NUMERICALLY on every six-variable class. Ties in a simple score are resolved adversarially. W2_i is Fourier level-two mass through i.

| rule | worst selected E_i/Inf_i |
|---|---:|
| rule_maxInf | 2.944495303872 |
| rule_minInf | 5.019930166880 |
| rule_shortest | 3.645797072921 |
| rule_minW2 | 5.019930166880 |
| rule_maxW2 | 4.833940887931 |
| rule_term_clause | 2.944495303872 |
| term_clause_adverse_pair | 3.650196658624 |
| term_clause_maxInf | 2.944495303872 |
| tied_constant_singleton_score | 5.019930166880 |

`rule_term_clause` takes the minimum spectral ratio over variables that belong to some shortest minterm and some shortest zero-certificate. It is a restricted spectral oracle. If the two shortest certificates are chosen first and adversarially, then the best coordinate in their intersection has worst ratio 3.650196658624 (`term_clause_adverse_pair`). `term_clause_maxInf` is a simple-data alternative: select a largest influence within the union-intersection candidate set. These interpretations are kept separate.

For monotone functions, Inf_i²/mu({i}) is exactly one on every relevant coordinate; its ties therefore allow the all-coordinate maximum, 5.019930166880. Private singleton mass divided by influence equals influence and reproduces the largest-influence rule. `extra_rules.json` and `census_summary.json` include the witnesses.

PROVED failures in arbitrary dimension, in `PROOFS.md` sections 6–7: smallest influence and maximum W2_i/Inf_i select the original hidden coordinate; largest influence fails after sufficiently large majority substitutions; most shortest minterms fails after MAJ3 substitutions. A complementary-pair hidden construction makes W2_x exactly zero while every other W2 is positive, defeating minimum W2_i/Inf_i. Its exact-table x ratios are:

| k | total variables | exceptional E_x/Inf_x | minimum over all coordinates |
|---:|---:|---:|---:|
| 6 | 7 | 3.370696860024 | 1.520790791237 |
| 8 | 9 | 5.240170201832 | 1.613238041292 |
| 10 | 11 | 7.037576189143 | 1.629851092872 |
| 12 | 13 | 8.822318835186 | 1.625089157912 |
| 14 | 15 | 10.621997125606 | 1.616306511782 |
| 16 | 17 | 12.441974751248 | 1.607996239383 |
| 18 | 19 | 14.280651067362 | 1.600971140591 |

Commands: `python3 priority.py python3 extra_rules.py` and `python3 priority.py python3 paired_hidden.py`. The proof gives divergence, not just the finite table. The shortest-minterm/shortest-zero-certificate selectors remain open in arbitrary dimension; no universal bound for them is claimed.

## Larger monotone hunt

CHECKED NUMERICALLY. `hill.cpp`, seed 241110, proposes legal single-point flips and accepts them by a cooling rule with a small H^-/I tie reward. All saved record DNFs were independently rebuilt and their spectra evaluated by `structured.py`. The following are search outcomes, not exhaustive maxima.

| n | evaluated legal proposals | raw hill best min E/Inf |
|---:|---:|---:|
| 7 | 400,000 | 2.954683814183 |
| 8 | 180,000 | 3.304701322451 |
| 9 | 60,000 | 2.943943956729 |
| 10 | 30,000 | 2.854608613409 |
| 11 | 12,000 | 2.890131816103 |
| 12 | 5,600 | 2.842916610161 |
| 14 | 1,598 | 2.505685809968 |
| 16 | 160 | 2.675019398238 |

The hill search evaluated 689,358 legal proposals. Separate n=7 sampling used 2,000 DNFs, seed 241111, with the distribution fixed and recorded in `sample7.json`. Larger-dimension raw records can be worse than smaller ones because the search is incomplete; unused-variable padding preserves ratios.

`profile_search.py` exhausts 60 ordered regular threshold-layer profiles with at most twenty leaves and 798 threshold assignments; it is exhaustive only in this specified structured class. The best was OR3 of AND3 of OR2 on eighteen variables, with every coordinate ratio 3.713716018539, H/I=4.227591363295, H=7.153219279242 bits, and I=110889/65536 exactly. `records.py` rebuilt it separately from its twenty-four DNF terms and matched the full truth table. The formula and complete DNF are in `record18.json`, and its truth table is `witnesses/profile_best.npz`.

The largest raw H/I among the retained, re-evaluated witnesses is OR of ten disjoint AND2 terms, on twenty variables: 4.522797166104 bits per influence. `tribes_10x2.json` and `witnesses/tribes_10x2.npz` record it. This directly answers the question whether a monotone function can exceed four in entropy/influence. None of our functions through twenty variables had minimum coordinate erasure ratio above four; the best search result was 3.713716018539. This is not an upper bound.

`structured.json` contains 216 finite cases: original hidden gadgets through twenty variables, majority substitutions, threshold compositions, random overlapping DNFs and two independently checked inherited seeds. `more_constructions.json` adds 42 cases consisting of thresholds/tribes of hidden gadgets and hidden-gadget self-composition towers. These did not beat the record. Source paths and hashes distinguish the inherited eighteen-variable seeds from the published record certificate; no published-certificate replay is claimed.

## Charging and the remaining gap

PROVED in `PROOFS.md` sections 2–5: E_i <= h2(even spectral mass) for every Boolean function; H^-<=2I for the original hidden gadget; H^-<=5I after arbitrary disjoint balanced odd monotone substitutions. The exceptional coordinate keeps its large ratio, but its absolute entropy cost is at most one bit and the total influence budget is at least one. Every block leaf has ratio below four. This explicitly pays for the bad coordinate.

PROVED in section 9: the singleton mass identities and sum Inf_i²<=1 alone are insufficient. A conditioned sparse product law plus singleton atoms satisfies both identities and has unbounded H^-/I. These laws are not asserted to be Boolean spectra. General monotone FEI therefore still needs additional Boolean or monotone structure.

The bound in the brief equating optimal H/I and optimal minimum-coordinate erasure constants is not established by the supplied reductions. What follows is C_*-2log2(e)<=G_*<=A_*<=C_*; the boundedness assertions are equivalent. No equality or transfer of the full entropy lower-bound constant to G_* is claimed.

## Literature and prior memory

`LITERATURE.md` contains neutral clauses from opened primary sources on monotone FEI, monotone FMEI, read-k DNFs, special separated monotone DNFs, and general logarithmic-loss bounds. In particular, Hod already gives monotone entropy lower bounds above 6.45, and the published 6.521845710923046575 amplified certificate is explicitly monotone. It is an amplified H/(I-1) seed bound, not the seed H/I or its minimum erasure ratio. No resolution of general monotone Shannon FEI appears in the sources opened.

Brain recall helped locate the earlier monotone-DNF argument and its census as a sanity check. That note is provisional and was not used as a proved theorem. The math-recall program reported no installed math store. No shared memory edits were made.

## Checks, resources and reproduction

`proof_checks.json` checks parity leakage on 16,611 representatives and the exact leaf formula on 54 substituted functions, including nonmajority odd monotone blocks. The maximum leaf-formula residual is 5.551e-17 bits. `highprecision.json` recomputes 26 distinct selected witnesses at 70 decimal digits; its largest binary64 discrepancy is 9.77e-15 bits or bits per influence, according to the compared functional. This high-precision calculation complements the outward interval certificate for every monotone finite winner.

`python3 priority.py python3 reproduce.py` passed all 16 sequential units. `resources.json` records 94.503 seconds elapsed, 92.510 child CPU seconds and 915,177,472 peak child resident bytes (872.781 MiB). Numerical libraries were restricted to one thread, compute nice was at least 10, and only one reproduction unit ran at a time. All files stay in this folder. There were no helpers, extra model workers, shared writes, mesh/board posts, pushes, messages or trading-stack launches. The final consistency audit and folder size are saved in `final_audit.json`.

OPEN: general monotone FEI and general overlapping-DNF Shannon FEI; a proof for either shortest-certificate selector; a higher finite min-coordinate record beyond the specified searches. The brief has been carried through the complete finite census, the requested searches, the successful family charging argument, and explicit descriptions of the mathematical gaps.
