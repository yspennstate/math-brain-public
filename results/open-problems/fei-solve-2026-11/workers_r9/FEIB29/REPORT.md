# FEIB29 report

PROVED. The summed B inequality is equivalent to FEI. It remains unproved in general and was not broken by these searches. A constant of 4.094 is too small: a stored 14-variable read-once function has R=4.160114440563878, and a succinct PM(K33) tower has R=4.505226154110238. PROVED. The asymptotic supremum near dictators is exactly the unrestricted erasure/influence constant K_E, possibly infinite. Consequently an unconditional constant for every sufficiently near dictator would resolve FEI itself.

## The equivalence and the near-dictator limit

PROVED. Let p_i=Inf_i(f), B=I-W1, and E=sum_i E_i. Multiplying f by a character translates its Fourier distribution and preserves each E_i. Boolean derivatives give |fhat({i})|<=p_i, hence

    B_i>=p_i(1-p_i),
    min_R I(chi_R f)=sum_i min(p_i,1-p_i)<=2B.

Therefore E<=K_E I for all Boolean functions implies E<=2K_E B. The converse follows from B<=I. The erasure sandwich supplied in BRIEF.md then gives equivalence to ordinary entropy FEI. FKN, Kindler-Safra, and quantitative dictator-stability constants are unnecessary for this implication.

PROVED. At distance delta from a signed dictator, put g=that dictator times f. Every influence of g is at most 2delta, so

    (1-2delta) I(g)<=B(f)<=I(g)+4delta(1-delta).

The right inequality and edge isoperimetry show B(f)/I(g)->1 uniformly as delta->0. If A(delta) denotes the supremum of E/B over all finite dimensions at exact dyadic distance delta, then

    K_E<=A(delta)<=K_E/(1-2delta),
    lim_(delta->0) A(delta)=K_E.

For the lower bound, balance tensor powers of an arbitrary h with a fresh sign, activate that core on a control event of probability 2delta, and multiply the result by another fresh sign. Its numerator retains at least the activated tensor erasure; increasing the tensor power makes all control and variance costs negligible. A point-control version also has B->0, I->1, and W1->1. PROOFS.md gives the full construction and proves a direct quantitative dictator-stability statement for B/I<1/8.

K_E is an unknown optimal constant, not a numerical answer to FEI. It can differ from the optimal full spectral-entropy constant K_H; the proved comparison is K_E<=K_H<=K_E+2/ln 2. No equality of those constants is claimed.

CHECKED NUMERICALLY (`python3 precision.py`, precision.json). An explicit rare-activation example has delta=4.336808689942017736029811203479766845703e-19, B approximately 6.37930632193615e-8 influence units, and R approximately 4.505049965270276. It is specified by a depth-seven alternating PM core, its balanced tensor power, point controls, and a fresh dictator. The exact parameter counts and high-precision values are in precision.json. These are succinct compositions, not materialized truth tables. Thus small dictator distance by itself does not force the subcube family's limit of two.

## Reproducing and improving the census witness

CHECKED NUMERICALLY WITH A DIRECTED INTERVAL CERTIFICATE (`python3 evaluate.py --n 8 --hex ...`, `python3 interval_audit.py`; census_witness.json and interval_audit.json). FEIB27's finite-census maximum is attained by the eight-variable table

    ffff0000ffff0000ffaa000000000000ffea0000c0c00000ffaa000000000000

Truth-table bit x is one when f(x)=-1; bit zero is the least significant bit. In 0/1 event variables, its negative-output event has minimal clauses {1,5,6}, {4,5,6}, {2,3,5,7}, {5,7,8}. Equivalently it is

    b5 AND [b6 AND (b1 OR b4) OR b7 AND (b8 OR (b2 AND b3))].

All eight variables are relevant. It is a read-once monotone formula, not AND2 with dummy variables. Its E is 3.803951735870403 bits, I=1.390625, W1=0.46142578125, B=0.92919921875, and R=4.093795667400203 bits per unit of B. The recorded finite-census optimum is attained, not merely approached. That does not make it a supremum over all Boolean functions, or even all eight-variable functions; I did not replay FEIB27's full census.

CHECKED NUMERICALLY (`python3 composition.py 14`, read_once.json). Enumerated 640,441 read-once monotone AND/OR formula shapes through 14 leaves, counting both dual root gates and the one-leaf case. Numerically, only one orientation of each dual pair is evaluated. The enumeration uses unordered multisets of alternating gate children and covers these functions up to variable permutation and duality. Input sign changes preserve R as well. The maximum in this restricted class through 14 leaves is

    R=4.160114440563878217..., n=14,
    E=5.382765309643219434... bits,
    I=1.5625, W1=0.2686016261577606,
    B=1.2938983738422394.

Its complete 4,096-digit hex truth table is [best_witness.hex](best_witness.hex); [best_witness.json](best_witness.json) also records its formula. The formula, with leaves numbered left to right, is

    A(O(x,A(x,x)),O(x,A(x,x)),O(A(x,O(x,x)),A(x,O(x,A(x,O(x,x))))))

A is AND and O is OR of the negative-output events. interval_audit.json encloses this ratio using exact integer Walsh coefficients and directed interval logarithms. This is the largest fully stored truth table found here. It is not a maximum over arbitrary 14-variable functions.

## Numerical attacks and named families

CHECKED NUMERICALLY (`./hill seeds.txt champions.txt 4000` and `./hill refine_seeds.txt refine_champions.txt 20000`). There were 774 starts at dimensions six through twelve and 10,884,992 proposal evaluations, including final greedy-neighbor checks. These are evaluation instances, not distinct functions. The starts cover random and biased near-constant functions, perturbed dictators, heavy thresholds, shared selectors, x1 times a core, XOR-free conditional mixtures, tribes, leading read-once formulas, parity translations, and perturbations. The proposal stream uses single truth-table flips and occasional pairs, annealing followed by greedy improvement.

The largest hill result was R=4.147284358433192 at n=12, E=5.313063393394726 bits, B=1.2810945510864258. Its complete table is in [best_hill_witness.json](best_hill_witness.json). It was already a leading read-once seed; the directed attacks did not improve it. The first search reproduced the old 4.0937956674 witness. The log files record both searches and deterministic seeds.

CHECKED NUMERICALLY (`python3 evaluate.py --families`; families.json and families.log). The final named run contains 220 instances. It includes AND through dimension 16; OR-of-ANDs with widths two through four; weighted thresholds with one heavy coordinate; address functions; PM(K33); uniform and biased random functions; and subcube perturbations of dictators. Selected ratios, in bits per unit of B, are:

| Function | Variables | R |
| --- | ---: | ---: |
| AND_2 | 2 | 4.000000000000 |
| AND_3 | 3 | 3.563318645298 |
| AND_8 | 8 | 2.121418182182 |
| AND_16 | 16 | 2.000959581499 |
| tribes_2x5 | 10 | 4.026140027477 |
| tribes_3x4 | 12 | 2.916741083760 |
| tribes_4x3 | 12 | 2.936015096694 |
| PM_K33 | 9 | 3.382355570122 |
| address_3 | 11 | 1.263157894737 |

PROVED. AND_n has R<=4, equality at n=2, and limit two. The k-control address function has E=k, I=1+k/2, W1=2^-k. Those exact formulas agree with the independent evaluations. Raw family tables and all threshold/random instances remain in families.json.

CHECKED NUMERICALLY WITH A DIRECTED INTERVAL CERTIFICATE (`python3 composition.py 14`, `python3 precision.py`, `python3 interval_audit.py`). The largest ratio among all functions tested here is

    4.505226154110238035...,

for a depth-six alternating-sign PM(K33) tower on 531,441 variables. Set G0=x and Gr=(-1)^r M(Gr-1,...,Gr-1) on nine disjoint blocks, where M=-1 exactly when the edge set of K33 contains a perfect matching. Thus the signs from leaves to root are -,+,-,+,-,+. E is approximately 246.808565021390526 bits, I approximately 54.788373253899363, and W1 approximately 0.005648352016138377. The base gate's 128-digit hex and the circuit parameters are retained in towers.json. An expanded truth table for this dimension cannot fit the folder or any practical storage; its exact circuit replaces that table. The best stored table and the best succinct tower are reported separately.

This B ratio is larger than the background's depth-seven E/I value of about 4.50505; they use different denominators and attain their tested maxima at different depths. The final retained tower results above 14 variables use composition identities. Initial exploratory family code expanded two 16-variable towers; those checks were removed and the final family run was repeated.

## Proved classes and composition behavior

PROVED in [PROOFS.md](PROOFS.md):

- Symmetric Boolean functions satisfy E<=24.08B. The minimizing parity remains symmetric, so the established symmetric FEI theorem applies.
- Read-once formulas with gate arity at most k satisfy E<=(8^k/ln 2+2)B, an explicit loose consequence of product-measure FEI+. The constant is independent of formula depth and size. Allowing arbitrary unrestricted gate arity includes every Boolean function and therefore returns to FEI.
- A Boolean function computed by a decision tree of maximum depth d>=1 satisfies E<=[4(d-1)+2/ln 2]B. The proof uses the dyadic Fourier grid and parity minimization; the tree need not be read-once.
- For balanced psi, I(F o psi)=I(F)I(psi), W1(F o psi)=W1(F)W1(psi), and B(F o psi)=I(F)B(psi)+B(F)W1(psi). An exact erasure identity includes additional block-activation terms. A naive maximum-of-input-R rule fails: a balanced address gate has R=1, while its depth-two self-composition has R=1.2012050593046015. FEI+ gives the correct closure.

The general biased composition identity is proved and implemented in composition.py. It is checked against direct small truth tables before being used on large towers. These are proofs for the stated classes; no unconditional constant for every near-dictator function is asserted.

## Verification, sources, and remaining work

CHECKED NUMERICALLY (`python3 audit.py`, audit.json). Independently recomputed all 774 hill champions and 308 leading read-once shapes from their truth tables. The largest hill ratio discrepancy was 4.89386309254769e-13; the largest formula-summary ratio discrepancy was 2.6645352591003757e-15. A direct character-sum calculation matched the census witness's integer Walsh transform exactly. There were 192 random identity controls and 48 bounded-depth decision-tree controls; the latter had zero coefficient-grid failures. Real-space influences, parity invariance, empty-pair estimates, near-dictator comparison, balanced composition, and rare activation passed their checks. precision.json independently recomputes selected ratios at 90 decimal digits; interval_audit.json adds directed interval certificates at 75 decimal digits. The precision alone is not presented as proof of a universal bound.

The parity comparison D<=2B is already explicit in [the author, Lemma 2.2](https://arxiv.org/html/2610.16069v1). The same paper's Section 8.4 gives related full-entropy rare-activation reductions and cites earlier work. [O'Donnell-Tan](https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf), Lemma 2 and Theorems 1-3, supplies the established product-measure FEI+ composition result. [O'Donnell-Wright-Zhou](https://yuanz.web.illinois.edu/papers/fei-icalp.pdf), Theorem 1, supplies the symmetric constant used here. I checked these primary sources and make no claim of novelty.

CHECKED NUMERICALLY. The largest recorded process RSS was 862,896,128 bytes, below the three-GiB cap. Each numerical process used one thread and recorded nice 10; the two hill searches ran sequentially. Uptime and governor state were read before the longer searches; load exceeded nine, so no second numerical thread was used. The initial relative nice command was denied by the sandbox, but the inherited priority was already 10, confirmed in every run's record. No process priority increase or external write was needed.

REPRODUCE.sh gives the commands. STATUS.md and RESULTS.md were saved during the work. The startup MEMORY.md was consulted; broad brain recall was not used for this self-contained mathematical brief, and the brief explicitly says no math store is installed. The relevant FEIB27 files and supplied FLOW sections were useful. No subagents, model workers, mesh posts, board posts, git pushes, trading processes, or external messages were used; writes stayed in this worker folder.

OPEN. FEI, the existence and numerical value of K_E, a universal numerical B constant, and unconditional boundedness for all near dictators. The proof identifies the near-dictator asymptotic supremum with K_E, rather than claiming to evaluate an unknown FEI constant. The numerical attacks did not disprove existence of a finite constant. The largest tested B ratio is a lower bound, not an upper bound. The specific requested class result for all near dictators is obstructed by the proved equivalence to the full open problem.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 2026, 22:20 ask, as recorded in BRIEF.md; timezone unspecified.
