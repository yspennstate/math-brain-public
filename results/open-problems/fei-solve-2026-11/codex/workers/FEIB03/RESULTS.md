# FEIB03 results

The general containment conjecture remains unresolved. The assigned proof routes and bounded searches are complete. The search found no diverging balanced ratio. It did produce exact obstructions to the plain restriction induction, association replacements, and the reverse-second-moment step.

All logarithms are base 2. A is in bits; I is expected spectral-set cardinality. A/I and A/(I-1) use those units. Counts, ratios and witnesses below come from the scripts and output files named here.

## Maxima by ambient dimension

| n | A/I | witness | balanced A/(I−1) | witness | scope |
|---:|---:|---|---:|---|---|
| 1 | 0.000000000000 | 0x1 | undefined | — | exhaustive, exact |
| 2 | 1.000000000000 | 0x1 | 0.000000000000 | 0x6 | exhaustive, exact |
| 3 | 1.583333333333 | 0x1 | 3.000000000000 | 0x1b | exhaustive, exact |
| 4 | 1.937500000000 | 0x1 | 4.000000000000 | 0x35f | exhaustive, exact |
| 5 | 2.162500000000 | AND_5 | 4.000000000000 | G_4 padded | observed |
| 6 | 2.312500000000 | AND_6 | 4.000000000000 | G_4 padded | observed |
| 7 | 2.417410714286 | AND_7 | 4.000000000000 | G_4 padded | observed |
| 8 | 2.494140625000 | AND_8 | 4.000000000000 | G_4 padded | observed |
| 9 | 2.552517361111 | AND_9 | 4.000000000000 | G_4 padded | observed |
| 10 | 2.598437500000 | AND_10 | 4.108819145973 | M_1 | observed |
| 11 | 2.635564630682 | AND_11 | 4.145665821950 | M_2 | observed |
| 12 | 2.666259765625 | AND_12 | 4.164293618416 | M_3 | observed |
| 13 | 2.692101111779 | AND_13 | 4.174239089057 | M_4 | observed |
| 14 | 2.714181082589 | AND_14 | 4.181272449266 | M_5 | observed |
| 15 | 2.733280436198 | AND_15 | 4.185414426217 | M_6 | observed |
| 16 | 2.749973297119 | AND_16 | 4.189561584963 | M_7 | observed |
| 17 | 2.764692418716 | AND_17 | 4.193703561915 | M_8 | observed |
| 18 | 2.777770996094 | AND_18 | 4.197850720660 | M_9 | observed |
| 19 | 2.789470271060 | AND_19 | 4.197850720660 | M_9 padded | observed |
| 20 | 2.799998283386 | AND_20 | 4.197850720660 | M_9 padded | observed |

The first four rows are true suprema. At n=3 the exact A/I value is 19/12; at n=4 it is 31/16. `census.py` and `census.json` enumerate every truth table. `audit.c` and `audit_c.out` independently use direct Walsh sums and direct superset sums. `certify_census.py` and `census_certificate.json` prove each bound and its attainment with integer products, without logarithms. At n=1 the balanced quotient is undefined because every balanced function is a dictator. At n=2 its maximum is zero, attained by parity.

Rows n>=5 are largest observed values, not suprema over all functions. `search.py` scored 15,897 truth tables using AND, tribes, majority, recursive majority, address, bent quadratics, random DNF, balanced random functions, compositions, K3,3 coins and hill climbs with flips or balanced swaps. It covered every n from 5 to 20. Exact per-dimension evaluation counts are in `search_counts.json`, and all scored values in `search_records.json`. The fixed random seed is in the script. The score tolerances are also explicit there.

G_4 is the balanced four-variable truth table 0x35f. M_k is the matching construction with its nine exceptional sites partitioned into k shared coins, using the best partition found by exhaustive enumeration of all 21,147 partitions of nine sites (`coin_partitions.py`, `coin_partitions.json`). These are exhaustive optima within that coin-sharing family, not over all Boolean functions. Optimal partitions and their truth-table witnesses are stored in `coin_partitions_exact.json`. The optimal partitions improve the simple modulo-sharing values slightly at n=13 through n=16.

Padding means extra coordinates are unused. Dimensions in the table are ambient dimensions; no assertion is made that every witness uses every coordinate. `final_best.json` gives every witness path and the exact-arithmetic input/high-precision output source. `witnesses/*.npz` stores signed truth tables, and the table-integer convention is bit x set iff f(x)=-1.

## Strongest checked containment lower bound

For the 18-variable K3,3 gate with nine independent coins:

    A = 4.361829264436196656414096620232460360258810035587946565902982979457513672696179479523230740659587704 bits
    I = 261/128
    A/(I-1) = 4.197850720660399789631611784885375384309230710941783161169788130605727444399330626909575449657347565

These are measurements of the known matching gate, not a claim to a new FEI record or a novelty claim about the containment constant. The Fourier numerators and upward sums are exact integers; logarithms were evaluated at 100 decimal digits. `verification.json` contains agreement between the dense truth-table transform and a separate sparse calculation using direct core Walsh sums, Hall's condition for matching, and direct superset sums. Physical edge counts recover every individual influence: nine core influences 57/256 and nine coin influences 1/256. Another 100 upward sums were checked from face derivatives.

The proved identity sup_all A/I = sup_balanced A/(I-1) makes this a lower bound of 4.197850720660399... for any universal constant in the A-conjecture. It is a lower bound, not an upper bound.

## Composition

For balanced inner g on disjoint blocks, A(f composed with g)=A(f)+I(f)A(g). The outer gate need not be balanced. For heterogeneous balanced inners the corresponding formula is A(f)+sum_j I_j(f)A(g_j). `PROOFS.md` proves both formulas by factoring upward probabilities; `verification.json` records 496 truth-table checks with maximum absolute A error 1.7763568394002505e-15 bits.

Self-composition of a balanced gate has exactly constant A/(I-1). For the matching gate that constant is the value above. Its A/I rises towards this value, while the balanced ratio stays fixed. `composition_towers.json` lists the predictions from the proved law through depth eight and explicitly distinguishes formula evaluations from allocated truth tables. Mixing different gates gives a convex combination of their balanced ratios; it need not stay constant. Without balanced inners the proposed law fails: AND_2 composed with AND_2 is AND_4, with A=31/32 rather than 2.

## The four routes

(a) Generalized influences: proved the levelwise tail estimate A_k <= W_k log2(4^(k-1)M_k/W_k)+W_k/ln(2), with M_k=E binom(|U|,k). The unresolved payment is the factorial moment. The naive estimate M_2<=C I is refuted by parity, where M_2/I=(n-1)/2. The KKLMS entropy theorem retains its logarithmic loss. See `PROOFS.md` (a).

(b) Recursion: the exact identity is A(g)=A(a)+A(d)-J. A bent quadratic on m even coordinates, with one input flipped in one slice of a new coordinate, gives Delta_i A/I_i=m+o(1). Multiplication by a fresh dictator preserves this ratio while making parent and both slices balanced, so a potential based only on their means cannot repair it. The same family has J<=2 I_i/ln(2) but normalization entropy divided by I_i grows like m. Thus both plain constant coordinate payment and direct entropy payment by J fail. `routes.json` compares grouped 100-digit formulas and truth tables through m=18, and evaluates the grouped formulas at m=32,64,100 without large truth tables. Balanced lifts were checked through ambient dimension twenty.

(c) Association: 0x13 on three variables violates the pointwise product bound on a set of positive spectral mass. A one-point perturbation of a mux makes the deficit unbounded even at fixed |S|=2, refuting a correction of 2^(-C|S|). The averaged uncorrected inequality fails at 0x19, with exact positive gap (1/16)log2(3^22/(2^13*5^9)). A valid generic replacement is A<=sum I_i log2(1/I_i)+I/ln(2); it still has uncontrolled marginal logarithms. See `routes.json` and `PROOFS.md` (c).

(d) Second moment: Q=Pr[S subset U]=E_U ||E[f|x_U]||_2^2 is valid, but Jensen gives a lower bound for A. A balanced mux between a dictator and a k-address function has A=3/2+3k/4, while Q=(3/16)(1+(3/8)^k) stays bounded below. It refutes a reverse estimate A<=C log2(1/Q), without refuting the conjecture. See `routes.json` and `PROOFS.md` (d).

## Verification and limits

`verify.py` checks all 65,812 functions in dimensions one through four, including every subset's upward sum by direct face derivatives, the real-function recursion, the granularity estimate, the levelwise tail bound and the corrected averaged association bound. `stress.py` adds 300 random and structured cases in dimensions five through twenty; `stress.json` records the errors. `routes.py` independently checks the explicit failure families. Exact integer-product census certification supplies an additional check of the reported small suprema.

None of the computations establishes a universal upper bound or an unbounded balanced ratio. The coin-sharing ratios increase over a finite family and stop at nine separate sites; this is not asymptotic growth in n. The largest-dimensional full truth tables here have twenty coordinates. Large composition towers and large-address examples are proved formulas, not numerical sweeps over their full cubes.

The main verifier measured priority 10, peak resident memory 380,010,496 bytes, and 3.521003 seconds; these values are in `verification.json`. Thread environment limits were one. Other runs use the same inherited priority and thread limits. The initial relative nice wrapper could not change priority under the sandbox; querying the actual priority confirmed 10. Working arrays were kept far below the process and folder caps.

## Recall and handoff

Startup memory and shared NOTES.md were read. Brain recall helped by identifying the matching-and-coins gate and warning about earlier entropy induction failures. Math recall returned `math store not found`. Fleet rules prohibit mesh posts and writes outside this folder, so no shared memory, checklist, mesh, repository or external service was modified. The launching session can promote the durable results from `PROOFS.md`; they have been numerically audited but not independently refereed.

Task: "Do the brief fully and carefully" — FEIB03, started 2026-11-10 01:09 +04.
