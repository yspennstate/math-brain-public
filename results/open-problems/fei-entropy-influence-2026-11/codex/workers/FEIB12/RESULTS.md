# FEIB12 results

All numerical tables below are CHECKED within the stated finite scopes. Logs and functionals use bits; I is dimensionless. Ratios are bits per unit influence. Undefined ratios are excluded from extrema. Bit x of a hexadecimal truth table is 1 precisely when f(x)=-1, with x encoded by its input-bit mask. NPN moves preserve every reported spectral quantity. Constants have zero functionals and undefined ratios.

PROVED results and full arguments are in PROOFS.md. OPEN: a universal Phi(1/2)<=CI theorem, the requested dimension-independent monotone/LTF class bounds, and a universal unrestricted recursion potential. The finite searches do not settle these questions.

## Exhaustive census through five variables

CHECKED: census.c / census1.json through census5.json. The generator scans output-sign representatives in increasing truth-table order, marking complete orbits under coordinate permutations, coordinate negations and output negation. Every unmarked table becomes a representative. The bitmap at n=5 occupies 268,435,456 bytes; the final scan covered 4,294,967,296 truth tables. audit.py re-evaluated every representative independently in NumPy, reconstructed the complete four-variable orbit partition independently in Python, and recomputed each displayed extremal truth table by exact rational character sums and 80-decimal-digit logarithms. The maxima are numerical census claims, not interval-certified rankings.

| n | NPN classes | Truth tables covered |
|---:|---:|---:|
| 1 | 2 | 4 |
| 2 | 4 | 16 |
| 3 | 14 | 256 |
| 4 | 222 | 65,536 |
| 5 | 616,126 | 4,294,967,296 |

CHECKED sup Phi(u)/I, from the census JSON files:

| n | u=0 | u=1/4 | u=1/2 | u=3/4 | u=7/8 | u=1 | Extremal representative |
|---:|:---|:---|:---|:---|:---|:---|:---|
| 1 | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0.000000000000 | 0x1 |
| 2 | 2.000000000000 | 1.678071905113 | 1.415037499279 | 1.192645077942 | 1.093109404391 | 1.000000000000 | 0x1 |
| 3 | 2.955889582252 | 2.605525090476 | 2.263765477643 | 1.922981684460 | 1.752851151664 | 1.583333333333 | 0x01 |
| 4 | 3.402475551199 | 3.056741260721 | 2.714676048303 | 2.347315081455 | 2.148343288753 | 1.937500000000 | 0x0001 |
| 5 | 3.623740399702 | 3.285099735400 | 2.958137471919 | 2.597997092338 | 2.392145164941 | 2.162500000000 | 0x00000001 |

CHECKED: for each n every displayed u has the same unique NPN extremal class listed above, as checked in census_audit.json. In n=1 the only nonconstant NPN class is a dictator, and all six values are zero. For n>=2 these Phi/I extremizers are AND_n up to NPN. Padding a function with unused variables leaves all its ratios unchanged.

| n | sup (Phi(1/2)-A)/I | Truth table | sup (Phi(1/2)-A)/(I-V) | Truth table |
|---:|---:|:---|---:|:---|
| 1 | 0.000000000000 | 0x1 | undefined | undefined |
| 2 | 0.415037499279 | 0x1 | 1.660149997115 | 0x1 |
| 3 | 0.680432144310 | 0x01 | 1.660149997115 | 0x03 |
| 4 | 0.777176048303 | 0x0001 | 1.660149997115 | 0x000f |
| 5 | 0.821862628209 | 0x00010117 | 1.660149997115 | 0x000000ff |

CHECKED: over the union n<=5, the half-noise cancellation cost is 0.821862628209331 bits per influence, at n=5, tt=0x00010117. The maximum over I-V is 1.66014999711538, attained by AND_2 and its padded equivalents. exact_extrema.json stores long exact-character-sum evaluations; census_audit.json lists every tied NPN representative within the stated numerical tolerance. I-V=0 cases are constants and signed dictators, where the numerator is also zero.

## Structured families and random draws

CHECKED: families.py / families.json and families.csv. These are finite tested maxima, not suprema over an unbounded family. There are 205 saved rows. Every row has all six Phi/I values, I, V, both cancellation ratios, and either its full hexadecimal truth table or an exact compact symmetric description. extremal_truth_tables.json collects the maximizing row for every column in this table. Large majority truth tables have exponentially many bits and are specified by their exact weight-threshold vector instead of materialized. The exhaustive-census extremal truth tables above are all materialized.

| Family | Rows | n range | u=0 | u=1/4 | u=1/2 | u=3/4 | u=7/8 | u=1 |
|:---|---:|:---|:---|:---|:---|:---|:---|:---|
| AND | 21 | 1–256 | 3.995646055007 | 3.673717960120 | 3.410683554286 | 3.188291132949 | 3.088755458646 | 2.984375000000 |
| LTF | 32 | 6–16 | 3.065468242976 | 2.797723722944 | 2.473567253780 | 2.060860862771 | 1.857929214964 | 1.666192385988 |
| PM_K33 | 1 | 9–9 | 3.241921347547 | 2.961110244311 | 2.676379380865 | 2.384747163490 | 2.237509383183 | 2.089946662057 |
| address | 3 | 3–11 | 2.400000000000 | 2.206843143068 | 2.049022499567 | 1.915587046765 | 1.855865642635 | 1.800000000000 |
| majority | 14 | 1–513 | 2.825362819384 | 2.508335671655 | 2.122045045113 | 1.611162778180 | 1.277974051639 | 0.985458829588 |
| random | 96 | 6–16 | 2.832773675378 | 2.602593421866 | 2.381560927146 | 2.116985951317 | 1.946508955266 | 1.750000000000 |
| read_once | 30 | 4–16 | 4.130634124020 | 3.796291201454 | 3.492180020709 | 3.171730946413 | 2.975492387685 | 2.722350286200 |
| tribes | 8 | 2–16 | 3.442915775573 | 3.100709810142 | 2.777515318329 | 2.458546878090 | 2.298414922106 | 2.166286965912 |

| Family | max half-noise cost / I | Witness | max half-noise cost / (I-V) | Witness |
|:---|---:|:---|---:|:---|
| AND | 0.795637471919 | AND_5 | 1.660149997115 | AND_2 |
| LTF | 1.053500415401 | LTF_16_5 | 1.588747955146 | LTF_6_2 |
| PM_K33 | 0.586432718808 | perfect_matching_K33 | 1.169144203173 | perfect_matching_K33 |
| address | 0.249022499567 | address_3 | 0.415037499279 | address_1 |
| majority | 1.804608909604 | majority_513 | 1.910262088402 | majority_513 |
| random | 0.648858023247 | random_8_1 | 0.966077262079 | random_6_7 |
| read_once | 0.876111440977 | formula_16_2 | 1.588747955146 | formula_4_2 |
| tribes | 0.640490071690 | tribes_w4_t4 | 1.660149997115 | tribes_w1_t2 |

CHECKED family definitions: AND_n includes every n=1..16 and n=24,32,64,128,256. Majority includes odd n=1..15 and n=17,33,65,129,257,513; the large evaluations use a closed spectral formula, independently compared to dense transforms in overlapping dimensions. Tribes uses (width,tribes)=(1,2),(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4). PM(K33) is the monotone graph property that a selected edge set in K_{3,3} contains a perfect matching. Address functions have k=1,2,3 address bits and 2^k data bits. Read-once formulas use AND/OR/NOT with six seeded random trees at each n=4,6,8,12,16. Their exact trees, including leaf negations, are saved. Random means 24 mixed unbiased/biased draws at each n=6,8,12,16; constants can occur and are excluded from ratios. The 32 LTFs have positive integer weights, eight draws at each of the same dimensions, with three threshold quantiles. All weights, thresholds and seeds are in the source/data.

## The four proposed routes

CHECKED / PROVED: the raw median inequality is false even for a unique median. unique_median_counterexample.json gives n=4, tt=0xaaa9, S mask 1, q=(9,3,3,1)/16, median 0, and F(1/2)/up=91/128. PROOFS.md proves the corrected quantile inequality and the atom-plus-conditional-mean bound, each tested before proof on all four-variable functions and the six-variable sample.

| Majority n | I | true half-noise cost / I | old Jensen / I | atom bound / I | quantile bound / I | median level / I | H_nu(S given U) / I |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 17 | 3.338470458984 | 1.040519690463 | 2.420180172757 | 1.188228296020 | 1.181847940913 | 2.521107370277 | 1.950002263616 |
| 33 | 4.618347825017 | 1.256626557541 | 3.737326132973 | 1.453373212136 | 1.379912305215 | 3.835641781145 | 2.213653263328 |
| 65 | 6.457538993618 | 1.439225660429 | 5.626844358088 | 1.674897590357 | 1.540376820317 | 5.754583732056 | 2.407694616599 |
| 129 | 9.079805889932 | 1.588824412159 | 8.319175790457 | 1.856663238013 | 1.668707701053 | 8.501627809885 | 2.547150100630 |
| 257 | 12.803511253588 | 1.709122424472 | 12.141544246878 | 2.002598110741 | 1.770369540991 | 12.405328101671 | 2.646299110447 |
| 513 | 18.080498004235 | 1.804608909604 | 17.557969908000 | 2.117776146227 | 1.850567397932 | 17.924447343327 | 2.716472066717 |

CHECKED: these rows show the mean and median costs growing while the atom/quantile costs stay much smaller. PROVED: the atom bound is at most B and at most the old Jensen bound, so the supplied symmetric B theorem gives an O(I) majority bound without its old mean defect. OPEN: a new universal O(I) bound for this expression.

CHECKED: reverse hypercontractivity for |g| at u=1/2 passed the actual derivative checks, but the weighted noisy sign ratio remains the unresolved term. The largest weighted log-ratio / I was 0.414018236434 over all4 and 0.543105129599 in the 12,000-draw six-variable sample; these are finite maxima, not universal constants. PROVED: the exact u-derivative formula is in PROOFS.md; its numerical finite-difference check is in check_*.json.

PROVED: H_nu(S|U)<=CI is equivalent up to constants to FEI; it has not removed the missing inequality. CHECKED: its ratio is already greater than 2 on majority_33 and reaches 2.716472066717 in the saved family table. The n<=5 census alone, whose largest ratio is 1.940162007464, would miss this.

## Classes

| Class | Verdict | Explicit result |
|:---|:---|:---|
| Monotone / unate | PROVED partial; OPEN uniform target | Singleton Gamma terms vanish; higher alpha(S)<=min_{i in S} Inf_i. Higher Gamma terms need not vanish. |
| Symmetric | PROVED, inherited from FEIB02 | B<=3.459354 I; Gamma<=1.6 I; hence every noise cancellation cost is <=3.459354 I. |
| Linear threshold | PROVED partial; OPEN uniform target | Same unate first-level statement; majority_5 disproves higher-level sign purity. |
| Read-once AND/OR/NOT | PROVED | Gamma=b^2 log(1/|b|)<=I/(2 ln 2). This is not a B/Phi theorem. |
| All nonempty derivatives have one sign | PROVED | Same exact bias formula and Gamma bound; if the empty derivative is included, only constants qualify. |
| Degree d | PROVED with d-dependent C | H, B, Phi(u)<=[2(d-1)+1/ln 2]I; Gamma<=[d-1+1/(2 ln 2)]I. Degree 0 and 1 are handled separately. |

PROVED correction to FLOW.md section 3b: a read-once formula need not have Gamma=0. AND_2 has Gamma=1/4 bit, entirely at S=empty. FEIB04 already recorded this correction. The symmetric coefficient in the brief was an intermediate value; the final FEIB02 proof sharpens it to 3.459354.

CHECKED: classes_all4.json covers all 65,536 four-variable functions, including 168 increasing monotone functions and 1,146 functions whose nonempty derivatives all have one sign. classes_sample6.json adds 3,000 mixed draws. The class identities, degree granularity and entropy bound had no violations. families_audit.json independently reconstructs every read-once tree and checks signs on all derivatives up to n=8, plus 16 sampled nonempty derivatives per larger tree.

## Induction LP and its failure beyond fitting

CHECKED: induction_lp.py / induction_lp.json and induction_constraints.npz. The roots are 222 NPN representatives. Every remaining coordinate at every E/D descendant is constrained: 1538 unique dyadic nodes and 4198 local inequalities. The feature definitions and root prices are in PROOFS.md. The objective minimizes c plus the priced bias feature; the request for a largest upper-bound coefficient has no finite optimum.

| Potential family | Fitted resulting coefficient | c |
|:---|---:|---:|
| none | 2.162757220863 | 2.162757220863 |
| entropy | 2.141590734044 | 2.141590734044 |
| nonnegative_root_zero | 2.130415385323 | 2.130415385323 |
| signed_root_zero | 2.023229343693 | 2.023229343693 |
| nonnegative_with_bias | 2.130415385323 | 2.130415385323 |
| signed_with_bias | 2.023229343693 | 2.023229343693 |

CHECKED: the best signed fit uses G coefficients 0.226402820504, 1.197499529471, -0.988355176971, 0.213977466950, -0.056215787372 in the first five feature order. Adding a nonnegative priced bias feature did not improve the optimum. The weaker root-only LP is 1.464975551199; it is not an induction certificate. induction_audit.json independently replays primal residuals, numerical dual constraints/objectives, the explicit J formula, and the influence recursion.

| Held-out n | Potential family | Violating rows | Largest local violation, bits |
|---:|:---|---:|---:|
| 5 | none | 337 | 0.105115415230 |
| 5 | entropy | 365 | 0.106561648599 |
| 5 | nonnegative_root_zero | 364 | 0.105957650531 |
| 5 | signed_root_zero | 547 | 0.093729750106 |
| 5 | nonnegative_with_bias | 364 | 0.105957650531 |
| 5 | signed_with_bias | 547 | 0.093729750106 |
| 6 | none | 1800 | 0.081858952035 |
| 6 | entropy | 1915 | 0.101589058037 |
| 6 | nonnegative_root_zero | 1931 | 0.103672846319 |
| 6 | signed_root_zero | 3201 | 0.103681221003 |
| 6 | nonnegative_with_bias | 1931 | 0.103672846319 |
| 6 | signed_with_bias | 3201 | 0.103681221003 |

CHECKED: each held-out dimension uses 128 independently seeded mixed Boolean roots and all their descendants. Explicit real truth-vector witnesses, the split coordinate, J and derivative mass are saved in induction_audit.json. All six fitted rules fail; none is promoted to a theorem in higher dimensions.

PROVED: no fixed nonnegative combination of the five root-zero features can satisfy the coordinate-independent local induction inequality on all Boolean E/D descendants with any finite c. AND_n forces all four logarithmic-feature coefficients to vanish; a bounded dyadic linear-plus-parity descendant then has J/||D||_2^2=log_2(N+1), defeating the remaining L1-deficit feature. The full proof and the exact Boolean embedding are in PROOFS.md. This obstruction does not rule out signed features, child slacks, special coordinate orders, or other potentials.

## Audit and provenance

CHECKED: every census representative agrees across C and NumPy; the largest reported disagreement is 4.885e-15 (the exact scientific value is stored in census_audit.json). Explicit derivative noise energies agree exactly in check_*.json. Conditional entropies are calculated both from joint conditional probabilities and by the independent B+KL formula. Centered finite differences test the noise derivative. No theorem is inferred from sampling. The final audit collects all tolerances and resource measurements in final_audit.json.

CHECKED: source files NOTES.md and FLOW.md were read from ~/fei_solve_agent; the symmetric theorem is from ../FEIB02/PROOFS.md and REPORT.md. Brain recall helped identify the pre-existing read-once-potential warnings and the distinction between finite fitting and a certificate. The math recall command returned “math store not found.” No shared brain, mesh, fleet board or checklist was written; LEARNINGS.md is a local handoff for the launching session.
