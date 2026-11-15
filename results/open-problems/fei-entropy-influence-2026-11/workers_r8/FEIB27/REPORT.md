# FEIB27 report

| Allowed terms | Local C, approximately | Summed C, approximately | Status beyond the census |
| --- | ---: | ---: | --- |
| Inf | 9.428632 | 3.606847 | local bound disproved; summed bound open |
| singleton + B | 9.428632 | 3.606847 | local bound disproved; summed bound open |
| M + B | 9.465607 | 4.028236 | local bound disproved; summed bound open |
| noise(0.95) + B | 9.465607 | 3.999338 | local bound disproved; summed bound open |
| degree cap 2 + B | 9.465607 | 4.067699 | local bound disproved; summed bound open |
| all linear terms except Inf | 9.428632 | 3.606847 | local bound disproved; summed bound open |
| B alone | 9.465607 | 4.093796 | local bound disproved; summed bound open |
| M alone | 42.511875 | 10.688295 | both forms disproved |
| degree cap 2 alone | 21.444786 | 5.930623 | both forms disproved |
| noise(0.5) alone | 209715.200000 | 9986.438095 | both forms disproved |
| noise(0.8) alone | 86.651553 | 12.134961 | both forms disproved |
| noise(0.95) alone | 14.063432 | 4.751033 | both forms disproved |
| perspective alone | 32.625678 | 8.598106 | both forms disproved |
| singleton alone; low-level truncation alone, r=1,2,3 | infeasible | infeasible | explicit zero-denominator witnesses |

CHECKED NUMERICALLY. This table comes first as requested. It gives finite-census LP optima, with the sharper shared spectral influence budget for linear mixtures. B_i=Inf_i-fhat({i})^2, M_i=sum_{S containing i}mu(S)/|S|, and noise(rho) uses multiplier rho^(2(|S|-1)). The perspective is Inf_i log2(1+M_i/Inf_i). Constants are rounded; full coefficients are in joint_fit_frozen.json and fit_frozen.json. Feasibility means a floating-point check on the recorded census and attack streams, not a universal theorem.

The computational brief is complete. FEI is still open. The useful outcomes are proofs ruling out the whole local dictionary and most of its summed directions, a certified obstruction for the eight tested potentials, and an exact transitive counterexample to the half-mass candidate at p<=4q. No general inequality surviving the search has been proved.

## What was proved

PROVED. Every tested local term is at most Inf_i. A hidden-coordinate construction from a quadratic bent function has Inf_i=2^-k and p/q=(2^(k/2) plus or minus 1)^2 under the derivative law. Its erasure ratio grows as k+log2(e). Thus no fixed nonnegative combination of this dictionary gives a dimension-independent per-coordinate bound. In particular, even the local Inf-only fit in the table is broken by the next larger members of this explicit family. The exact table is hidden_bent.json.

PROVED. Except for Inf_i and B_i, all dictionary terms sum to a constant times Var. Balanced tribes have summed erasure entropy growing with clause width while Var stays bounded. Every summed combination omitting both Inf_i and B_i therefore fails. A mixture containing Inf cannot improve the optimum over Inf alone; singleton+B reproduces Inf exactly under the shared budget.

PROVED. A further local estimate, with A_i=Var-Inf_i and B_i as above, is

    E_i <= B_i [2+log2(e)+log2(1+A_i/B_i)].

The right side is zero when B_i=0. The proof bounds the empty Fourier pair by 2B_i and aggregates the nonempty pairs by the log-sum inequality. Its logarithmic term still lacks an O(I) sum estimate. PROOFS.md gives every step, including the scalar entropy inequality used. refined.json checks it independently on the retained hard witnesses. No novelty claim is made.

## Census and restriction closure

CHECKED NUMERICALLY. The primary scans contain 33,573,370 function instances and 172,593,426 relevant-coordinate instances. Repeated restrictions, repeated hill proposals, and overlap between classes are included in those counts. Frozen-coefficient replays are excluded. laws.json contains the count by source.

The NPN catalogue has 2, 4, 14, 222 and 616126 representatives at dimensions one through five, read from ../FEIB13/npn1.bin through npn5.bin. I read the catalogue generator and saved SHA-256 hashes in input_hashes.txt. Its sign/permutation invariance was checked independently. No general six-variable census is claimed.

The monotone census enumerates every function through six variables, by all ordered pairs a<=b of monotone functions in the preceding dimension. The counts are 3, 6, 20, 168, 7581 and 7828354, including constants.

The random/DNF census contains 10000 random functions and 10000 random DNFs total, spread evenly over dimensions six through ten. There are both monotone and signed DNFs and multiple truth-table biases. The seeds are 2026111027 and 2026111028. Every restriction with at least six free coordinates was enumerated; lower-dimensional restrictions are already covered by the NPN catalogue. This adds 21984000 restriction instances.

There are 177 named roots: thresholds, weighted thresholds, tribes, majority-hiding functions, clique-with-pendant graph functions, quadratic bent and bent-hiding functions, PM(K33), its row/column presentation, small AND/OR/majority/parity towers, small TD functions, and parity-times-AND controls. High-dimensional disjoint tribes restrictions are compressed by their sorted live clause widths; dummy coordinates and permutations do not affect these quantities. close_named.py produces 113 compressed instances. Generic named roots add 116180 restrictions with at least six free coordinates; the lower ones are NPN-covered. The parity-times-AND controls restrict to other listed controls or to pure characters, which have zero erasure and step cost.

The fixed two-block skeleton potential is not permutation invariant. This does not undermine the supersolution feasibility check: the optimal potential is zero, and its inequality was checked through the permutation-invariant full-step cost. The lower-bound witness was checked at every coordinate for the actual labeled partition.

## Adversarial checks and LP validation

CHECKED NUMERICALLY. Two streams contain 1000000 hill-climb proposals each, with four objectives apiece and 50 restarts per objective. The objectives cover summed erasure, best-coordinate erasure, positive log moment, median ratio mass, best full-step cost, the B-only summed ratio, and the noise/B and degree-cap/B violations. Every proposal, including rejected ones, was measured. These are proposal instances, not a claim of two million distinct functions.

An additional 1000000 six-variable functions are provably distinct: their truth tables are the images of distinct counters under the invertible SplitMix64 permutation. All frozen inequalities were checked on this separate stream. distinct.json records its count and residuals. These distinct functions are a stress test; the directed attacks are the hill-climb streams.

Each fitted linear mixture was then checked across the full initial census, its restrictions, both attack streams, and the distinct stream. The largest normalized violation over the saved oracles is 5.642e-14 bits per influence, within rounding error. validation.json names every oracle. Selected constraints supply the LP lower bound, and a successful separation scan supplies feasibility over the full census, so the reported optima are numerical optima rather than sample-only fits.

For independent term budgets, C=sum c_k is valid. For linear spectral mixtures I also optimize the stronger C=max_d sum c_k w_k(d); only degrees one, two and three need checking because the kernels decrease thereafter. The nonlinear perspective is kept in the independent-budget fit. This distinction matters: paying separate budgets for singleton and B would overcharge their exact decomposition of Inf.

## Supersolutions

CHECKED NUMERICALLY, WITH A DIRECTED INTERVAL CERTIFICATE FOR THE LOWER BOUND. The optimum delivered constant C+K is 6.003746056559 bits per influence, attained with Theta=0. The binding function is OR of eight disjoint two-variable clauses. Its full-step ratio is enclosed at 70 decimal digits around 6.0037460565590882514. The interval audit verifies every candidate potential drop at every coordinate is at most that potential's certified budget times Inf_i. Hence every nonnegative mixture has C+K at least this witness ratio; zero potential attains it on the census. milp.json independently solves the actual coordinate-choice disjunction on the witness.

The candidate budgets Theta_k<=b_k I are: I, Var, log-degree moment and squared influences each have b=1; the degree-times-2^-degree moment has b=1/2; level entropy has b=3; nonempty entropy has b=2; and the two-block skeleton entropy has b=2+log2(3). The certificate concerns these explicit budgets. It does not prove that no different potential, sharper budget proof, or larger universal constant can work.

PROVED within the same certified budgets. For the literal form (T), in which the same C bounds both the step term and Theta/I, the finite-census optimum is about 3.001873028279544 with Theta=C I. Its influence drop adds another C Inf_i, producing the same delivered constant 2C=6.003746056559088... . The witness forces C+K>=R and K<=C, so it also proves C>=R/2. common_constant.json records this convention separately; it is not an improved bound.

The brief calls the log-degree moment not O(I); in fact log2(1+d)<=d proves it is O(I). Level entropy is also O(I), as established in Theorem 5 of [O'Donnell, Wright and Zhou](https://yuanz.web.illinois.edu/papers/fei-icalp.pdf). The argument in FLOW comparing a single bad coordinate for equal (Var,influences) statistics does not rule out every best-coordinate potential of those statistics: the existential coordinate can change, and zero potential is itself in that class. PROOFS.md separates these quantifiers.

## The conditional ratio law

CHECKED NUMERICALLY. Across the complete scans, max_f min_i E_i/Inf_i is 3.606847002096, and max_f min_i E_rho_h[log2(p/q)]_+ is 1.851658579311; both are attained by the eight-clause width-two tribes function. The full best/worst coordinate bucket laws and exact witnesses are in LAWS.md and laws.json.

The statement that some coordinate has at least half its derivative mass at p<=q is false. A monotone ten-variable perturbation of five width-two tribes has maximum coordinate mass only 0.159481095679. Its minimal one-sets have masks 3, 12, 48, 192, 421, 602 and 768: the original disjoint pairs plus two added boundary points.

The weaker half-mass candidate at p<=4q survives the main scans, with minimum best mass 0.500000000000, but is DISPROVED by a larger stress function. Take OR of nine disjoint two-variable clauses and add the conjunction of the first element of every pair and the conjunction of the second element of every pair. This function is transitive. At every coordinate the exact conditional mass is 429970409/859963392 = 0.4999868750226986, strictly less than one half. The integer gap is 22574 between the denominator and twice the numerator. transversal_certificate.py derives a multinomial formula and independently matches its full (g,h) Fourier-numerator histogram to an integer Walsh transform. PROOFS.md gives the derivation.

CHECKED NUMERICALLY. The rounded positive-log candidate min_i E_rho_h[log2(p/q)]_+<=2 remains unbroken. The larger stress family raises the observed maximum to about 1.863061 at seven pairs with the two transversal clauses. A weaker half-mass threshold at p<=16q also survives these checks. HEURISTIC: either statement might hold universally, but neither is proved here, and a single quantile does not control the remaining tail or imply FEI.

Sixteen larger or structured stress checks, outside the restriction-closed LP census, cover a balanced eighteen-variable PM(K33) lift, width-two tribes with nine and ten clauses, tribes with two complementary transversals, and majority-hiding functions through k=17. None breaks the surviving summed fits or the positive-log bound of two; the half-mass bound at p<=4q does fail as just shown. stress.json explicitly marks that their full restriction closures were not enumerated; they are excluded from the LP counts and optimality claim. Arbitrary-depth PM towers were not enumerated; only the small truth-table towers listed above were part of the closed census.

## Checks, files and remaining work

CHECKED NUMERICALLY. An independent NumPy implementation recomputed 416 saved extrema; the largest absolute discrepancy was 1.182e-11. On 200 independent random controls, Parseval, real-space pivotal influence, entropy tree identity, the positive-log sandwich, influence restriction identity, potential budgets, and NPN transformations were checked. The largest tree-identity residual was 3.997e-15 bits. audit.json gives every residual. The interval audit uses integer Walsh transforms and directed interval logarithms rather than the census floating-point lookup table.

The validation scans recorded a maximum resident set of 7,995,392 bytes and minimum nice level 10; the larger Python stress test recorded 502,398,976 bytes, below the 3 GiB process cap. Each C++ scan is single-threaded; numerical-library thread counts were fixed at one, and at most two numerical processes ran together. At the file audit the folder held 15,056,766 bytes, below the 150 MB cap. All artifacts stayed in this worker folder. No subagents were started and no mesh, fleet board, external service, or git repository was updated.

The main implementation is census.cpp and search.py; REPRODUCE.sh gives the commands. fit_frozen.json, joint_fit_frozen.json, oracle_final.txt and oracle_joint_frozen.txt retain the fitted constraints and coefficients. The validator compares coefficient vectors to their fit snapshots and records their hashes; only the uniformly frozen final_* and joint_* replays enter the final certificate. Earlier oracle_* files are preliminary runs. PROOFS.md contains the proved obstructions, the refined local estimate and the failed proof routes. RESULTS.md and STATUS.md were updated during the work.

Brain recall helped: it recovered the earlier simple-potential search, which motivated checking the delivered C+K objective and keeping the best-coordinate quantifier explicit. The math-store command reported that no math store was found. The requested relative_step.py is absent; I used its derivation in FLOW and wrote an independent implementation.

OPEN. Prove or disprove the surviving summed B-direction, prove a best-coordinate positive-log bound, or find a potential using joint spectral location that improves the explicit budgets. The computations neither prove FEI nor establish sharp universal constants.

Task: "solve the Fourier Entropy-Influence conjecture" — the author's 9 Nov 2026, 22:20 ask, as recorded in BRIEF.md; timezone not specified.
