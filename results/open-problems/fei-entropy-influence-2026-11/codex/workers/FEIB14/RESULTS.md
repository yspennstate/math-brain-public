# FEIB14 results

CHECKED finite results unless explicitly called PROVED. Entropies use base-two logarithms, and all ratios are bits per unit total influence. Truth-table bit x is set iff f(x)=-1; x uses little-endian coordinate bits. The five families are parity(P), meets(N), their ordered pair, total size, and count(N). Masks may be chosen independently for each coordinate. P and N range over every subset of the remaining variables, including the empty set; the joint search allows P and N to overlap.

The union chooses the least cost across the five families separately for each coordinate. It is not the minimum of their five total costs. A coarsened witness cost can exceed H; H^- itself cannot. Constants have I=0 and are excluded from ratios.

## Complete NPN census through five variables

Source: census1.json through census5.json, evaluated by witness.c on FEIB12's saved binary representatives. Input hashes and independent checks are in audit.json. Input negation preserves squared coefficients and coordinate permutation preserves the optimized mask families, so representatives suffice. This reuses the earlier verified census rather than generating it again. Rankings use binary64 logarithms; they are not interval-certified exhaustive orderings. All displayed extremizers were independently checked at high precision.

| n | classes | H/I | H^-/I | parity | meets | both | size | count(N) | union |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 0.000000000 | 0.000000000 | 0.000000000 | 0.000000000 | 0.000000000 | 0.000000000 | 0.000000000 | 0.000000000 |
| 2 | 4 | 2.000000000 | 2.000000000 | 2.000000000 | 2.000000000 | 2.000000000 | 2.000000000 | 2.000000000 | 2.000000000 |
| 3 | 14 | 2.955889582 | 2.672488984 | 2.950067265 | 2.672488984 | 2.672488984 | 2.672488984 | 2.672488984 | 2.672488984 |
| 4 | 222 | 3.402475551 | 2.704153206 | 3.598626286 | 2.723031786 | 2.704153206 | 2.799979804 | 2.723031786 | 2.704153206 |
| 5 | 616126 | 3.623740400 | 2.883566416 | 4.162634505 | 3.055036372 | 2.899222402 | 3.083274306 | 2.940080173 | 2.899222402 |

The five-variable extremizers are:

| family | ratio | hexadecimal truth table | true H^-/I at that function |
|---|---:|---|---:|
| parity | 4.162634504778 | `0x00000001` | 2.453729842625 |
| meets | 3.055036371793 | `0x00000017` | 2.462568485466 |
| both | 2.899222401541 | `0x0000001f` | 2.883566415773 |
| size | 3.083274306085 | `0x00000357` | 2.855617436260 |
| countN | 2.940080172907 | `0x00000007` | 2.861152584250 |
| union | 2.899222401541 | `0x0000001f` | 2.883566415773 |

Every entry in this extremizer table has positive coarsening loss, so none of the five families is sufficient for every function. A positive loss means it fails to recover E_i exactly; it is not by itself a counterexample to a uniform bound. PROOFS.md proves actual unbounded ratios for parity-only and total-size-only families.

## Mixed samples, dimensions six through ten

Source: samples.json. Seed and the distribution mixture are fixed in experiments.py: 96 draws per dimension, mixing uniform, biased, monotone, LTF, random read-once formulas and random DNF. These are samples, with possible duplicates and constants, not a census or a fitted model. All masks in all five families are optimized exactly by enumeration.

| n | draws | H^-/I | parity | meets | both | size | count(N) | union |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6 | 96 | 2.887649819 | 4.692596826 | 3.121878115 | 2.976796366 | 3.143264231 | 2.969674767 | 2.936769171 |
| 7 | 96 | 2.929111194 | 5.207117389 | 3.180313627 | 3.084519082 | 3.247914273 | 3.134662679 | 3.084519082 |
| 8 | 96 | 2.893378398 | 5.714268021 | 3.214632532 | 3.025516844 | 3.320326283 | 3.166977830 | 3.025516844 |
| 9 | 96 | 2.970754559 | 6.217816573 | 3.371537434 | 3.284624652 | 3.419714158 | 3.287778252 | 3.277880493 |
| 10 | 96 | 2.890859270 | 6.719584236 | 3.535879697 | 3.438399746 | 3.477901410 | 3.423015079 | 3.376171216 |

Complete hexadecimal tables and the maximizing function for every column are in extremal_truth_tables.csv; per-coordinate optimal masks are saved in samples.json. The independent direct-cell optimizer audit_large.c checks the larger extremal examples without using masked Walsh transforms. large_audit.json records its values and resources; final_audit.json re-evaluates selected optimal partitions with high-precision logarithms.

## LTF and monotone checks

Sources: ltf.json, monotone_all5.json, monotone6.json. Constants count as draws but have no ratio. All LTFs are verified against their saved weights and thresholds, and every saved monotone truth table is checked for monotonicity in final_audit.json.

| class and scope | draws | nonconstant draws | true H^-/I max | parity max | size max | optimized union max |
|---|---:|---:|---:|---:|---:|---:|
| LTF, n=2..10; all five optimized | 576 | 563 | 2.897069578 | 6.719584236 | 3.134635311 | 3.063963495 |
| LTF, n=11..14; parity and size optimized | 256 | 254 | 2.809793090 | 4.033885420 | 3.122148735 | not searched |
| all monotone, n=1..5 | 7778 | 7768 | 2.883566416 | 4.162634505 | 3.083274306 | 2.899222402 |
| monotone n=6, sampled | 4096 | 3904 | 3.030964070 | 4.692596826 | 3.371910560 | 3.069405179 |

For n=11..14, meets/both/count(N) fields in raw rows are explicitly unoptimized unconditional upper bounds. They are excluded from `maxima`; `candidate_maxima` retains these valid costs for transparency. The union value in such a raw row only minimizes the evaluated candidates. No full-mask optimality is claimed above n=10.

All monotone functions through n=5 were generated by the exact slice recursion (a,b) with a contained in b. The n=6 functions are random upward-closed sets generated from random minterms and random middle-layer antichains. This is an allowed sampling arm, not a Dedekind census in six variables. Small positive or negative orientation choices leave the squared spectrum unchanged.

## Symmetric erasure census

Source: symmetric.json. f_0=+1, and bit t-1 of `value_mask` specifies f_t=-1 for t=1..n; this is a weight-value vector mask, not a full truth-table integer. Each dimension covers every vector up to global sign. The Gray-code update is based on FEIB02's exact Krawtchouk/finite-difference formulas. symmetric_audit.json independently recomputes the whole erasure census through n=12, all saved extrema through n=20 using FEIB02's finite differences, and the small extremizers by full truth tables.

| n | sign representatives | maximum H^-/I | value-vector mask | maximum half-norm/I |
|---:|---:|---:|---|---:|
| 1 | 2 | 0.000000000 | `0x1` | 0.000000000 |
| 2 | 4 | 2.000000000 | `0x3` | 1.000000000 |
| 3 | 8 | 2.672488984 | `0x7` | 1.500000000 |
| 4 | 16 | 2.634003391 | `0xf` | 1.750000000 |
| 5 | 32 | 2.453729843 | `0x1f` | 1.875000000 |
| 6 | 64 | 2.583206739 | `0x30` | 1.937500000 |
| 7 | 128 | 2.500857772 | `0x4f` | 1.968750000 |
| 8 | 256 | 2.392886383 | `0xc0` | 1.984375000 |
| 9 | 512 | 2.517392904 | `0x1fc` | 1.992187500 |
| 10 | 1024 | 2.320015105 | `0x33f` | 2.011718750 |
| 11 | 2048 | 2.450356607 | `0xff` | 2.010190217 |
| 12 | 4096 | 2.470648981 | `0xc0f` | 2.028320312 |
| 13 | 8192 | 2.398293653 | `0x1787` | 2.031250000 |
| 14 | 16384 | 2.564737579 | `0x30fc` | 2.083901010 |
| 15 | 32768 | 2.406230155 | `0x7c3c` | 2.021643597 |
| 16 | 65536 | 2.547505592 | `0xf03c` | 2.061462402 |
| 17 | 131072 | 2.402472691 | `0x11e1f` | 2.119048771 |
| 18 | 262144 | 2.493784804 | `0x7c0f` | 2.054504395 |
| 19 | 524288 | 2.406714950 | `0x7f83` | 2.099578857 |
| 20 | 1048576 | 2.543078024 | `0xc3f00` | 2.137646275 |

The largest erasure ratio in this finite symmetric scan is attained at AND_3. The proposed half-norm<=2I shortcut already fails in dimension ten. A uniform symmetric erasure theorem below 4.650431 is OPEN here. The inherited 4.650431 ledger has been independently replayed in inherited_audit.json; the supplied older v4 snapshot states 4.657435.

## Structured functions and failure of coarse witnesses

Source: families.json. Full witness optimization is used through n=10. It includes tribes, AND, majority and AND-of-majority blocks. The strongest finite union record among the fully optimized datasets is:

`tribes_2x5` (n=10): union cost/I=3.389192093442. Its full truth table and every chosen mask are in families.json and extremal_truth_tables.csv.

This is a finite-test maximum. It is not a candidate universal coefficient: FLOW already gives a general erasure lower bound above 3.63 through its FEI equivalence and known entropy records. The function samples here do not include those lower-bound constructions.

PROVED: parity-only cost/I on AND_n is n/2+1+1/(2 ln 2)+o(1), despite bounded true erasure. PROVED: total-size-only cost/I on XORs of increasingly many AND_w blocks tends to h(2^(1-w))/2^(1-w), which is unbounded as w grows. A block-local count witness recovers the child erasure cost. The following finite convolution checks illustrate the second obstruction.

| block width w | XOR copies s | input bits n | true H^-/I | total-size witness/I | s->infinity limit |
|---:|---:|---:|---:|---:|---:|
| 4 | 1 | 4 | 2.634003391 | 2.634003391 | 4.348515546 |
| 4 | 64 | 256 | 2.634003391 | 4.331905330 | 4.348515546 |
| 4 | 4096 | 16384 | 2.634003391 | 4.348260744 | 4.348515546 |
| 8 | 1 | 8 | 2.104844603 | 2.104844603 | 8.437044780 |
| 8 | 64 | 512 | 2.104844603 | 7.714398485 | 8.437044780 |
| 8 | 4096 | 32768 | 2.104844603 | 8.429421451 | 8.437044780 |
| 16 | 1 | 16 | 2.000898517 | 2.000898517 | 16.442673027 |
| 16 | 64 | 1024 | 2.000898517 | 8.390574381 | 16.442673027 |
| 16 | 4096 | 65536 | 2.000898517 | 14.202220712 | 16.442673027 |

The largest clipped FFT negative mass was 6.81e-15; the largest normalization residual was 1.09e-13. Independent positive convolutions in small cases disagree by at most 4.72e-13 in the ratio. These are numerical checks of a separately proved limit.

Source: majority_meets.json. On majority the true erasure, parity cost and size cost are zero. The optimized single meets-block cost is positive and grows in this finite scan; its optimized asymptotic divergence is not proved here. Symmetry makes optimizing N equivalent to scanning its cardinality.

| majority input bits | best meets cost/I | best block size |
|---:|---:|---:|
| 3 | 1.377443751 | 2 |
| 5 | 1.937262563 | 4 |
| 9 | 2.539186132 | 8 |
| 17 | 3.153540555 | 16 |
| 33 | 3.472829219 | 2 |
| 65 | 3.699249892 | 2 |
| 129 | 3.886953748 | 3 |
| 257 | 4.052109876 | 4 |
| 513 | 4.197744207 | 5 |
| 1025 | 4.327825269 | 6 |
| 2049 | 4.445529167 | 7 |
| 4097 | 4.553240085 | 8 |

## Proved degree/depth coefficients

Source: highprecision.json and PROOFS.md. The constant statistic gives C_d=2^(d-1)h(2^(1-d)) for Boolean degree at most d, and for decision-tree depth at most d. It also bounds H itself.

| d | C_d |
|---:|---:|
| 1 | 0.000000000000 |
| 2 | 2.000000000000 |
| 3 | 3.245112497837 |
| 4 | 4.348515545597 |
| 5 | 5.396641065872 |
| 6 | 6.419914378007 |
| 7 | 7.431364819505 |
| 8 | 8.437044779935 |
| 9 | 9.439873600991 |
| 10 | 10.441285240875 |
| 11 | 11.441990370529 |
| 12 | 12.442342763078 |
| 13 | 13.442518916321 |
| 14 | 14.442606982189 |
| 15 | 15.442651012435 |
| 16 | 16.442673026886 |

## Verification and open conclusions

Independent direct grouping checked 410 functions; its largest absolute entropy discrepancy was 1.31e-14 bits. The degree/support checks cover 616368 NPN representatives and have no violation. The exact biased composition formula passed 371 generated cases, and the path statistic passed 256 formula cases, with erasure residual at most 6.11e-16 bits.

The largest small-extremizer binary64/high-precision ratio difference was 4.17e-14. The larger extremizers disagree by at most 1.02e-14. The quantized likelihood inequality was checked on 1074 functions, with no upper-bound violation; its proof is independent of those tests.

OPEN: sharper all-dimensional symmetric erasure constants; a direct improved read-once erasure-cost proof; a width-only bound for all overlapping DNF; a cheap uniform LTF witness; all-monotone FEI; and a uniform bound for joint parity/block, subset-count, or their union. The cited October threshold theorem supplies LTF and mixed symmetric-threshold formula H bounds, but was not independently re-proved here. No general FEI theorem is claimed.
