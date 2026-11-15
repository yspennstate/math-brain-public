# FEIB23 report

The universal theorem for all linear monotone DNFs remains unresolved. This worker completed the exhaustive census through eight variables, proved explicit mixed-width and short-term bounds, and isolated a regular family on which those bounds lose uniformity. It did not find a counterexample to FEI or prove that the actual best coordinate or tree averages diverge.

The proofs are in PROOFS.md. Each proved statement has a hostile second read recorded there. Numerical data and exact expressions are in the JSON files named below; external literature is in LITERATURE.md.

## Exhaustive ground truth

The following counts concern nonconstant functions depending on all n variables, modulo variable permutations. Ratios are in bits per unit influence. Dummy variables are handled by taking the union of the smaller essential dimensions; constants have H=I=0 and are omitted from ratios.

| n | Isomorphism classes | max min_i E_i/Inf_i | max H/I |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 |
| 2 | 2 | 2.000000000000 | 2.000000000000 |
| 3 | 5 | 2.672488983973 | 2.955889582252 |
| 4 | 16 | 2.634003390886 | 3.402475551199 |
| 5 | 72 | 2.695887520153 | 3.623740399702 |
| 6 | 592 | 2.944495303872 | 3.739764017898 |
| 7 | 10,808 | 2.954683814183 | 3.804357069772 |
| 8 | 552,251 | 3.304701322451 | 3.889105419815 |

Sources: census1.json through census8.json, their *.certified.json files, exact_values.json and final_audit.json. The maximum H/I increases throughout this finite range. The essential-dimension minimum-coordinate maximum drops between three and four variables, then rises. Nothing here establishes asymptotic growth.

All entropy maximizers through seven variables are AND_n and OR_n, with the dictator counted once. The eight-variable entropy maximizer is unique: four singleton terms disjoint from a four-cycle's four edge terms. Its widths are four ones and four twos, degrees are four ones and four twos, and P[F=1]=249/256. Its exact H/I is

    (114688 - 864 log2(3) - 735 log2(7) - 29282 log2(11))/2560.

The coordinate-ratio maximizers are AND_n/OR_n at n<=4; OR_3 disjoint from AND_2 at n=5; the edge DNF of K_(2,2,2) at n=6; the join of an independent triple with C4 at n=7; and two disjoint C4 components at n=8. The latter has eight width-two terms, every degree is two, and P[F=1]=207/256. The n=6 degrees are all four and P[F=1]=27/32; the n=7 degrees are 4,4,4,5,5,5,5 and P[F=1]=57/64. Sources: analysis.json and the independent graph isomorphism checks in graph_names.json. Full term lists, widths, degrees, sign biases, and exact prime-log expressions for every attainer are in analysis.json.

With dummy coordinates and the two constants included, the eight-variable ground truth comprises 563,749 isomorphism classes. The census stores every representative in census1.families through census8.families. Nine variables were optional in the brief and were not attempted: the class count already increased from 10,808 to 552,251 between the last two completed dimensions, so it was not a cheap extension within the process and folder budgets.

Verification used exact integer Walsh transforms, rigorous integer-series enclosures of logarithms at precision 2^-52 bits, and outward rounding of the final ratios. The eight-variable nonwinner upper bounds are below 3.866364698630 for H/I and 3.108449690058 for the minimum-coordinate ratio, giving large separation from both winners. Independently, a recursion packing pair-disjoint cliques counts 18,785,639,553 labeled families, exactly matching the orbit–stabilizer sum over the census. Both counting methods agree in every dimension through eight. A separate labeled truth-table enumeration through five variables and direct character-matrix transforms of all maximizers also agree. Sources: *.labeled_check.json, analysis.json, census8.certified.json, PROOFS.md section E.

## What is proved

PROVED, PROOFS.md section A: every term t of width w in any monotone DNF supplies a coordinate—any maximizer of influence inside t—with

    Inf_i >= 2 P[F=0]/(2^w-1),
    E_i/Inf_i <= 2+log2(2e(2^w-1)).

Thus width-one and width-two terms are handled even in the presence of arbitrary wider terms. If every term has width at most W, restriction induction proves

    H <= [2+log2(2e(2^W-1))+2/ln 2] I.

For monotone 2-DNFs this coefficient is 8.913047623388046, computed in final_audit.json. One short term at the root alone does not justify induction after that term is killed.

PROVED, section B: the mixed-width certificate (MIX) replaces the uniform residual degree load by

    ell_j = sum_(s contains j, i not in s) 2^-(|s|-1),
    eta_t = sum_(j in t minus i) ell_j.

It allows a different Fourier threshold for every incident term, gives all constants explicitly, and recovers (LIN) on specialization. It proves every coordinate passing its finite inequality good; it does not prove that some coordinate must always pass.

PROVED, section C: if t has width L+1>=4 and every variable in t has load at most

    (1+1/(64L^2)) 2^-L,

then every variable of t satisfies E_i<6 Inf_i, without any load restriction outside t. The threshold is close to a private term's minimum possible load; no optimality claim is made. Small widths are covered by section A.

PROVED, section D: for minority probability m and r=log2(1/m), every Boolean function satisfies

    H/I <= 2[n/r+1+(log2 e)/r].

This gives an absolute bound when m<=2^(-alpha n) for fixed positive alpha. It leaves functions with subexponentially small bias uncovered.

Numerical checks: proof_checks.json records 5,152 per-coordinate relative-influence checks, 6,617 short-term checks, and 234 mixed-width certificates, with no violation. A mixed-width example on nineteen variables checks all four variables of a locally sparse term, including its shared variable. These are checks of the proved inequalities, not model benchmark arms or evidence for a universal theorem.

## The obstruction and the numerical tree accounting

PROVED, section F, with remaining scope in section G: take variables A times F_Q, with |A|=w, and terms the graphs y=ax+b restricted to A. This linear DNF has n=wQ, Q^2 width-w terms and degree Q. Choose Q=2^k and w=k+2ceil(log2 k)+1. All variable loads are of order k^-2, every width grows, and the zero probability tends to zero while its negative logarithm divided by n tends to zero.

On this family the finite mixed-width certificate fails to give a bounded coefficient for every choice of its thresholds, the relative-influence certificate diverges at every coordinate, the local near-private criterion fails, and the dimension-sensitive bias bound diverges. Those are failures of the bounds. The actual coordinate ratios, best tree average and H/I remain unbounded-or-bounded questions here. The full proof of this distinction matters: no divergent upper bound is presented as a divergent statistic.

Small prime-field members were computed from complete truth tables. They are not the asymptotic powers-of-two sequence above. The term tree selects a shortest remaining term and reads all its variables before selecting another term; constants stop immediately.

| w | Q | n | min E_i/Inf_i | H/I | Whole-term tree erasure average / I |
|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 9 | 2.101500499 | 3.085609496 | 1.685620617 |
| 3 | 5 | 15 | 2.715095265 | 3.879784824 | 2.179472625 |
| 3 | 7 | 21 | 2.533512450 | 4.134586221 | 2.319322774 |
| 4 | 5 | 20 | 2.471331101 | 3.902443012 | 2.203639967 |
| 5 | 5 | 25 | 2.200337308 | 3.879971689 | 2.185292569 |

Sources: TD_3_3.json, TD_3_5.json, TD_3_7.json, TD_4_5.json and TD_5_5.json; command `./structured w Q`. The largest spectral computation has twenty-five variables and reproduces the corresponding leafless-plane erasure value in the brief. Its whole-term tree has 1,090,967 nonterminal nodes, and its weighted influence sum agrees with the original influence. Independent NumPy checks on the nine- and twenty-variable cases are in proof_checks.json.

For the eight-variable coordinate-ratio maximizer, the optimal adaptive decision-tree erasure average is 1.952478932101 and the whole-term tree gives 1.962958194726. For the eight-variable entropy maximizer both give 2.091597558702. Source: analysis.json. The tree identities were checked independently against the original entropy and influence. These numbers do not suggest a counterexample.

The exact remaining set is specified by failed certificates in section G, with coefficient eight. A function whose every restriction passes one of them satisfies FEI with coefficient 8+2/ln 2. It is not established that every linear monotone DNF has that property. The next mathematical step is a conditional spectral-separation estimate, or an amortized term-tree estimate, covering the transversal regime. No such step was proved in this run.

## Literature, recall, and reproducibility

LITERATURE.md gives one neutral clause for each requested class, with links to opened primary sources. Read-k DNFs have a published min-entropy result; read-k decision trees have a distinct Shannon result. The newly opened [Paraashar–Saurabh preprint](https://arxiv.org/html/2611.06451), submitted 4 November 2026, gives one-sided unambiguous-certificate and exact conical-representation entropy bounds. No claim of priority for this worker's lemmas is made. A theorem for all L would add an absolute Shannon FEI bound with unbounded read and width; this report does not claim it.

Math recall initially lacked its store environment. Recovering the configuration from ~/.claude/settings.json produced math_recall.txt and math_width_card.txt. The store helped by surfacing the older provisional short-term/width argument; the proof here was re-derived and checked independently. The old unrefereed read-k manuscript was not treated as external literature. No brain, mesh or checklist data was written outside this folder, as the fleet rules require.

From a shell already at nice 10 or lower scheduling priority, the main reproduction commands are:

```sh
clang++ -std=c++17 -O3 census.cpp -o census
./census 8 census8
python3 log_intervals.py
clang++ -std=c++17 -O3 certify.cpp -o certify
./certify 8 census8
clang++ -std=c++17 -O3 labeled_check.cpp -o labeled_check
./labeled_check 8 census8
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 analyze.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 proof_checks.py
python3 final_audit.py
```

The smaller census files are reproduced by substituting dimensions one through seven. structured.cpp builds the transversal examples. final_audit.json contains source hashes, exact-value cross-checks, scheduling priority and measured folder size. Work used no helper agents or additional language-model workers. Census and numerical jobs used at most two single-threaded computation processes and inherited nice 10. All writes stayed in this folder. The largest structured process's recorded peak resident size is 372,736,000 bytes, below 0.4 GiB (TD_5_5.json); the folder is below 200 MB.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 2026, 22:20 ask, as recorded in BRIEF.md.
