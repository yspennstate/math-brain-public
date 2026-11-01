# Exact composition census and the scope of the lower-bound seeds

For nonconstant Boolean f on n>=2 uniform bits, use phi(f)=min L_A/I_A over nonempty proper physical blocks with I_A>0. All entropy is in bits. Every value below is certified by rational intervals; decimals only display those certificates. The full block is never included.

## Precisely enumerated Boolean family

Let N_r(b_1,...,b_r)=1-product_j b_j on 0/1 inputs, r>=2. Each gate is a point defect: only the all-one input has output zero. Interpret the output as the sign 2b-1. Start with independent literal leaves, compose only these gates, allow arbitrary arities and depths, and forbid unary internal nodes. Child order is immaterial; canonical sorted rooted trees enumerate all such read-once formula shapes. Every occurrence of a literal has a distinct physical coordinate.

The recursion takes every integer partition n=s_1+...+s_r with r>=2, then every unordered choice of already generated child trees of sizes s_j. Repeated equal sizes are selected with combinations with replacement. Induction on n proves completeness and uniqueness as unordered formula shapes. Counts are 33,90,261,766 at n=6,7,8,9, respectively. Different shapes are not asserted to compute inequivalent Boolean functions; possible duplicates make this an exhaustive formula census with benign overcounting. These are not arbitrary Boolean functions or all repeated-variable FEI lower-bound seeds.

At each node independent automorphisms of each child, together with permutations of isomorphic children, preserve the Boolean function. By induction, a selected physical block is represented by a multiset of child selection-orbits within each identical-child class. The canonical representative orders those orbits. If child selection multiplicities are m_j and counts c_j, the labelled-orbit size is r!/(product_j c_j!) times product_j m_j^(c_j). Take products across different child types. This proves representatives are disjoint and exhaustive under the declared subgroup. The total multiplicity is checked to be 2^n; deleting empty/full blocks leaves 2^n-2. This reduction concerns actual physical blocks, not spectral subsets or component removals.

In total the calculation certifies 117,240 block orbits representing 470,340 labelled proper blocks on 1,150 formulas.

## Exact extrema of this finite family

Write Q=N_2(N_2(x_1,x_2),N_2(x_3,x_4)) on four fresh bits, with fresh disjoint copies whenever Q occurs twice.

| n | formulas | max phi | formula attaining max phi | minimizing block size | max H/I |
|---|---:|---:|---|---:|---:|
| 6 | 33 | 4.3198821089 | N_6 | 1 | 3.7397640179 |
| 7 | 90 | 4.1919153810 | N_7 | 1 | 3.8043570698 |
| 8 | 261 | 4.2044382917 | N_5(Q,x_5,x_6,x_7,x_8) | 7 | 3.8891054198 |
| 9 | 766 | 4.3104363691 | N_3(Q_1,Q_2,x_9) | 8 | 3.9489250136 |

At n=8 the H/I maximizer is the same displayed formula. At n=9 its maximizer is N_6(Q,x_5,...,x_9). Exact expressions, endpoint intervals, maximizing case indices, truth-table hashes and tied minima are in out/AGGREGATE_CERTIFICATES.json and the referenced out/full_case_*.json. Thus point defects do not dominate these objectives in every dimension, correcting the extension of the lead's small-dimensional pattern. Nevertheless every one of these 1,150 formulas has phi<227/50=4.54. There is no first composition exceeding that threshold in this frozen family through n=9. The maximum over the entire census is the six-bit point defect, approximately 4.3198821089.

The largest observed phi/(H/I) in the four dimensional groups is approximately 1.1551215767,1.1132055968,8/7,1.1071428571. The universal co-singleton bound in UNIVERSAL_DESCENT_SQUEEZE.md explains why these ratios cannot exceed 6/5,7/6,8/7,9/8 for any Boolean function, so that comparison is not a new payment.

There is an exact sharp example at n=8: F=N_2(Q_1,Q_2), the three-level complete binary NAND tree. Its minimizing blocks have size7 and the symbolic entropy vectors certify phi(F)=(8/7)H(F)/I(F). Hence the n/(n-1) pointwise factor cannot be improved at n=8. This is an exact finite lower obstruction to reducing that comparison factor, not a counterexample to FEI or to bounded block descent.

## Separate repeated-variable lower-bound seed controls

The primary [Hod paper, Section 1.2, PDF page3](https://arxiv.org/pdf/1711.00762) defines g3,g3-prime,g4,g4-prime with repeated variable occurrences. Their six/eight-variable finite versions and three fresh NAND extensions were evaluated separately, without orbit reduction. Clauses are frozen in code/check_seeded_and_replay.py. This distinction matters: recursive composition of a six-variable balanced seed with itself has 36 variables already, outside the requested range. No dimension36 computation was started, and no exhaustive statement about that family is inferred from n<=9.

| function | n | H/I | phi | phi/(H/I) | minimizing block size |
|---|---:|---:|---:|---:|---:|
| Hod g3 | 6 | 2.4149789433 | 2.3486815659 | 0.9725474304 | 1 |
| Hod g3-prime | 6 | 2.4411798072 | 2.5388269995 | 1.04 | 5 |
| Hod g4 | 8 | 2.5170425881 | 2.3755331817 | 0.9437794946 | 1 |
| Hod g4-prime | 8 | 2.5215727995 | 2.3692513049 | 0.9395926643 | 1 |
| N_2(g3,literal) | 7 | 3.0187964887 | 3.0924256714 | 1.0243902439 | 6 |
| N_2(g3,N_2) | 8 | 3.0022823412 | 3.0864584816 | 1.0280373832 | 7 |
| N_2(g3,N_3) | 9 | 2.8577591433 | 2.8318785880 | 0.9909437591 | 6 |

All seven controls also have phi<4.54. The seed's asymptotic amplification coefficient H/(I-1) is distinct from its finite H/I and from phi. None is substituted for the other in this calculation.

## Arithmetic certificate and independent representation check

For a truth table of length 2^n, integer Walsh coefficients w_S give p_S=w_S^2/4^n. Parseval is checked exactly. The entropy is the rational prime-log expression

H=2n-(2/4^n)sum_S w_S^2 log2|w_S|,

omitting zeros. Factor each nonzero integer |w_S| into primes and collect rational coefficients. Restriction averages and ratios preserve this representation. Identical coefficient vectors prove equality; signs use rational logarithm intervals.

For x=2^k y with 1<=y<=2 put z=(y-1)/(y+1). Use the positive series

ln y=2sum_(j=0)^(47) z^(2j+1)/(2j+1)+tail,
0<=tail<=2 z^97/[97(1-z^2)].

The same bound encloses ln2. Dividing positive intervals encloses log2 x; every log-prime interval is rounded outward to a 110-bit dyadic interval. Signed linear expressions use reversed endpoint order for negative coefficients. At each formula, every non-symbolically-tied competitor is interval-separated from the minimal ratio. The aggregator proves every phi upper endpoint is strictly below 227/50 and certifies the exact dimensional maxima against every competitor.

The census uses recursive formula restriction and tree symmetry. A second checker reconstructs physical children directly from bit indices, enumerates every labelled block of the seven seeds and five selected census extrema, and compares prime-log decrement vectors against the orbit certificates. Root integer FWHTs are also checked against direct character sums; spectrum-derived influence is checked against pivotal edges. It passes 4,927 assertions covering 2,984 labelled blocks in1.756 seconds. The shared logarithm enclosure is proved above; the second checker is an independent physical-child/transform representation, not an independent logarithm implementation or an external review.

The full census passes 140,692 assertions in154.8 seconds. Domain, counts, symmetry, arithmetic, memory estimate and runtime limits were frozen before execution. No floating-point result supplies a proof. A090/A094 review is pending. The first unsupported extrapolation is a dimension-independent bound on K_desc(n) for arbitrary Boolean functions; even an all-dimensional theorem for these read-once NAND formulas would not supply universal admission.
