# Renyi containment results

All numerical tables below are CHECKED within the stated corpus. They are not universal bounds. All logarithmic costs and entropies are in bits; ratios have units of bits per unit total influence. Truth-table bit x is one exactly when f(x)=-1. Input and output negations and coordinate permutations preserve the statistics, so an NPN census suffices. A quoted witness need not be the unique extremizer.

PROVED: the raw quadratic target fails near constants. The valid general bounds obtained are L_1<=16I^2+13I and L_1=O(I log(2+I)); the latter follows from the read KKLMS theorem. Linear WC holds for monotone/unate, symmetric, read-once and fixed-real-degree classes. The general linear exponent is OPEN. See PROOFS.md and LITERATURE.md.

## Complete small-function census

CHECKED: compute.py enumerated every truth table through four variables. npn5.c independently generated 616,126 five-variable NPN classes, covering all 2^31 truth tables after output complements are identified. Its largest allocation is exactly 268,435,456 bytes. npn_generation.txt is the coverage receipt. verify_census.c independently recomputed every q maximum on every five-variable representative.

| n | tables / classes | max L_1/I | witness hex | I | H | A | WC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 0 | 0x1 | 1 | 0 | 0 | 1 |
| 2 | 16 | 0.8300749986 | 0x1 | 1 | 2 | 1 | 0.5625 |
| 3 | 256 | 0.9433583329 | 0x1b | 1.5 | 2 | 1.5 | 0.375 |
| 4 | 65536 | 1.205960524 | 0x0357 | 1.5 | 3.32537578 | 2.13143789 | 0.2854003906 |
| 5 | 616126 | 1.249081408 | 0x018bf5cd | 2 | 4.304229297 | 2.979064844 | 0.1770019531 |

For n=1 every nonconstant function is a dictator and the maximum is zero. Constants have I=0 and are omitted from ratios. The balanced denominator I-1 excludes dictators. At n=1 its domain is empty; at n=2 parity gives zero.

| n | max balanced L_1/(I-1) | witness hex | I | H | A | WC |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | empty domain | — | — | — | — | — |
| 2 | 0 | 0x6 | 2 | 0 | 0 | 1 |
| 3 | 2.830074999 | 0x1b | 1.5 | 2 | 1.5 | 0.375 |
| 4 | 3.284895991 | 0x035f | 1.5 | 3 | 2 | 0.3203125 |
| 5 | 3.284895991 | 0x000f33ff | 1.5 | 3 | 2 | 0.3203125 |

The n=4 maximum L_1/I is attained by width-two tribes with two tribes, up to NPN equivalence (witness 0x0357). The n=5 maximum is balanced, at 0x018bf5cd. The balanced normalized maximum at n=4 and n=5 is the H=3, I=1.5, A=2 function. A balanced (I-1) denominator is a descriptive statistic here; the O’Donnell–Tan entropy amplification theorem has not been transferred to WC.

CHECKED: H/I and A/I at the very same WC-maximizing functions, together with their independent maxima, are as follows. This prevents confusing a maximum of one functional with another.

| n | max L_1/I | H/I at WC max | A/I at WC max | independent max H/I | independent max A/I |
| --- | --- | --- | --- | --- | --- |
| 2 | 0.8300749986 | 2 | 1 | 2 | 1 |
| 3 | 0.9433583329 | 1.333333333 | 1 | 2.955889582 | 1.583333333 |
| 4 | 1.205960524 | 2.216917187 | 1.420958593 | 3.402475551 | 1.9375 |
| 5 | 1.249081408 | 2.152114648 | 1.489532422 | 3.6237404 | 2.1625 |

## Large random samples

CHECKED: 200,000 draws per dimension, with seed 20261110+n. In each corpus 100,000 draws are independent unbiased truth tables and 100,000 are uniform among balanced truth tables. Draw counts are not claims of unique-function counts. Each maximum has a complete hexadecimal witness in its JSON receipt. These are sample maxima, not suprema over all functions at those dimensions.

| n | sample max L_1/I | witness hex | same H/I | same A/I | sample max balanced L_1/(I-1) | balanced witness hex |
| --- | --- | --- | --- | --- | --- | --- |
| 6 | 1.165548977 | 0x4fc06bfb5f502311 | 1.999940329 | 1.374257323 | 2.04434109 | 0x80aaa2ac05fff4ec |
| 7 | 1.05934326 | 0x82d590d5cfd1b7c6b0f318984c03efaa | 1.908581402 | 1.246405468 | 1.647008912 | 0x8eae0cc4000c1f0a9cff0c72fa5fbb37 |

Receipts: census_n6_sample.json and census_n7_sample.json. The extra unbiased arm can also produce balanced tables; the total balanced counts are n=6: 110038, n=7: 107179.

## Structured families

CHECKED: families.json contains explicit truth tables through n=18, including every requested family. There are 200 random read-once AND/OR/XOR formulas (50 each at n=6,7,10,14), and 40 further random uniform functions (10 each at those dimensions). analytic_families.json evaluates the PROVED compressed formulas at much larger dimensions with 180 decimal digits of working precision; it constructs no truth tables at those dimensions.

| family | n | I | L_1/I | H/I | A/I |
| --- | --- | --- | --- | --- | --- |
| AND | 5 | 0.3125 | 0.579019496 | 3.6237404 | 2.1625 |
| majority | 17 | 3.338470459 | 0.8257620682 | 2.398736058 | 0.8962318315 |
| AND | 18 | 0.0001373291016 | 0.1603000467 | 3.938060981 | 2.777770996 |
| bent_quadratic_pairs | 18 | 9 | 0.8300749986 | 2 | 1 |
| tribes w=3, t=5 | 15 | 2.198181152 | 1.687428324 | 3.245009995 | 2.166286966 |
| address_MUX k=3 | 11 | 2.5 | 1.698044999 | 2.4 | 1.8 |
| PM_K33 | 9 | 2.00390625 | 1.549692188 | 3.241921348 | 2.089946662 |
| PM_K33_plus_9_coins | 18 | 2.0390625 | 1.534509933 | 3.323392642 | 2.139134658 |
| address_MUX k=128 | 340282366920938463463374607431768211584 | 65 | 2.786535383 | 3.938461538 | 2.953846154 |
| tribes w=8, t=177 | 1416 | 5.555090585 | 1.960526095 | 3.981362345 | 2.810665827 |
| tribes w=128, t=235865763225513294137944142764154484399 | 30190817692865701649656850273811774003072 | 88.72283911 | 2.036156283 | 4 | 2.988728945 |
| majority | 255 | 12.75369214 | 0.3762934917 | 2.796038759 | 0.4083465203 |

PM_K33 is the nine-edge perfect-matching property. PM_K33_plus_9_coins is the balanced record construction: a coin acts on the two core sets consisting of a cross and that cross with its central edge removed. CHECKED: its H/(I-1) is 6.521845711. Both tables are saved in families.json; the 18-variable table is too long to print here.

CHECKED: maxima among the sampled read-once and additional random families are below. Full witnesses are copied to family_witnesses.json.

| sampled family | n | draws | max L_1/I | same H/I | same A/I | rep id |
| --- | --- | --- | --- | --- | --- | --- |
| random_read_once_AND_OR_XOR | 6 | 50 | 1.180280704 | 2.54558373 | 1.596267109 | 0 |
| random_uniform | 6 | 10 | 0.8706318993 | 1.802890306 | 1.049815086 | 7 |
| random_read_once_AND_OR_XOR | 7 | 50 | 1.189843694 | 2.475769925 | 1.575383605 | 38 |
| random_uniform | 7 | 10 | 0.8859329438 | 1.790462683 | 1.074300689 | 1 |
| random_read_once_AND_OR_XOR | 10 | 50 | 0.9113914521 | 3.396907208 | 2.017101157 | 25 |
| random_uniform | 10 | 10 | 0.8366329591 | 1.836569862 | 0.9949784117 | 8 |
| random_read_once_AND_OR_XOR | 14 | 50 | 1.179670748 | 2.436780633 | 1.600436011 | 11 |
| random_uniform | 14 | 10 | 0.8338516994 | 1.851235662 | 1.010445696 | 5 |

PROVED: address functions force a universal WC constant at least 2log(8/3)=2.830074999. Their L_1/I approaches this bound from below as k grows. Asymptotically balanced tribes with growing width have limit 2.041467583, and bent functions have ratio 0.8300749986. The finite census and known families do not determine the global extremizers.

CHECKED: the failure of a raw CI^2 bound is visible directly in the AND formula. These ratios are computed before conversion to binary floating point; the WC float in the JSON can round to one, so use its stored Lq_bits and ratios.

| AND n | I | L_1/I^2 |
| --- | --- | --- |
| 32 | 1.490116119e-08 | 6051101.582 |
| 64 | 6.938893904e-18 | 6.497320849e+15 |
| 128 | 7.523163845e-37 | 2.996360371e+34 |
| 256 | 4.4217183e-75 | 2.549021498e+72 |

## The interpolation

CHECKED: the following are maxima over the complete five-variable NPN census, which also contains every smaller function by adding dummy variables. The last row is q=0, meaning the limit A. Sources: census_n5_npn.json and independent_census.json.

| q | max L_q/I | witness hex | max balanced L_q/(I-1) | balanced witness hex |
| --- | --- | --- | --- | --- |
| 1.0 | 1.249081408 | 0x018bf5cd | 3.284895991 | 0x000f33ff |
| 0.5 | 1.382959988 | 0x00071357 | 3.602100195 | 0x000f33ff |
| 0.25 | 1.499613132 | 0x00071357 | 3.79165077 | 0x000f33ff |
| 0.1 | 1.818876557 | 0x00000001 | 3.914609299 | 0x000f33ff |
| 0.05 | 1.981362554 | 0x00000001 | 3.956985169 | 0x000f33ff |
| 0.01 | 2.124693304 | 0x00000001 | 3.991347725 | 0x000f33ff |
| 0.0 | 2.1625 | 0x00000001 | 4 | 0x000f33ff |

CHECKED: growth over this grid is from 1.249081408 to 2.1625, a factor 1.731272267. At small q the extremizer switches to AND_5. Finite-census boundedness as q decreases is not evidence of a dimension-uniform theorem by itself. The individual n=1,2,3,4 maxima and the n=6,7 sample grids are retained in their census JSON files.

PROVED: for each fixed q>0, FMEI would imply a linear bound with factor (1+1/q). Present general theorems yield the same factor times I log(2+I). Uniformity at q=0 is the OPEN containment conjecture.

## Independent checks and resources

CHECKED: audit.py uses dense direct integer character sums and an explicit containment incidence matrix on every truth table through four variables. It also recomputes every recorded extremizer using Python integers and alternating sums on restrictions, tests degree granularity and the monotone identity, and compares compressed family formulas with complete truth tables.

| audit | result |
| --- | --- |
| all-through-four direct integer tables | 65812 |
| maximum direct integer WC error | 0 |
| independent NPN4 class count | 222 |
| five-variable independent C/Python maximum-ratio error | 3.952393968e-14 |
| analytic/complete-table comparisons | 46 |
| maximum analytic comparison absolute error | 1.243449788e-14 |
| random NPN invariance checks | 1000 |
| tensor product checks | 200 |
| maximum tensor L_q error in bits | 1.33226763e-15 |

CHECKED: restriction_address.json tests the data-coordinate and address-coordinate restriction formulas at k=1,2,3, then evaluates the PROVED induction obstruction for larger k. The local charge and uniform-coordinate charge both diverge. This disproves those induction rules, not the WC conjecture.

Reproduce all numerical receipts with `python3 run.py --regenerate-npn`, then `python3 summarize.py`. run.py uses one numerical thread and retains niceness at least 10. The initial direct `nice -n 10` calls emitted a sandbox warning; os.getpriority independently confirmed that the processes already inherited niceness 10. The final runner checks this without attempting an unnecessary priority change.

CHECKED: run_receipt.json records the completed numerical run, with peak child RSS 270204928 bytes (0.2516479492 GiB), below the brief’s per-process cap. Each compute mode has a separate resources_*.json receipt. The NPN file checksum is `cd3f0326074d3349fe05991a2d7a54d45398776891c67a29a8e4a0532213ce55`. No external Python project code is imported; NumPy and mpmath are the numerical libraries used.

OPEN: the universal linear WC conjecture, its best constant and extremal families, and the uniform q-to-zero containment bound. No claimed proof of any of these is made.
