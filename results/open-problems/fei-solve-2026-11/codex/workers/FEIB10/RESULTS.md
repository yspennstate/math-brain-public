# FEIB10 results

Task started 2026-11-10 02:58 +04. All logarithms in information quantities are base 2.

PROVED: for nonempty R, Boolean spectral measures obey
`sum_{U >= R, |U-R| <= k} mu(U) <= 3^k 2^(|R|-1) up(R)^(3/2)`.
The empty-R axiom is trivial because up(empty)=1. The full proof is in PROOFS.md and computational checks are in boolean_output.json.

PROVED: containment does not follow, even from the sharper nonempty prefactor. See PROOFS.md section 2. The law has three nonempty layers:

`n=2^s`, `d=2^(2s/3)`, `mu(level s)=1-2^-s-4^(1-d)`, `mu(level d)=2^-s`, `mu([n])=4^(1-d)`.

Here s is any multiple of 6 at least 36. Both levels are uniform. Then A/I=s/3+1+o(1). It satisfies Csharp, the Boolean mean-granularity bound D, and the scalar existential support-probability analogue P. It violates the square-Parseval constraints for every possible Fourier sign assignment.

CHECKED: verify_counterexample.py produced counterexample_output.json, including exact integer sufficient certificates for all R,k and the following numerical evaluations (bits per expected element):

| s | I (expected elements) | A/I (bits per expected element, approximate) |
|---:|---:|---:|
| 36 | 36.0002441401 | 12.9999269065 |
| 48 | 48.0000152588 | 16.9999952395 |
| 60 | 60.0000009537 | 20.9999996980 |
| 96 | 96.0000000002 | 32.9999999999 |
| 192 | 192.0 | 65.0 |
| 384 | 384.0 | 129.0 |

These are evaluations of a proved unbounded family, not optimized suprema. The script labels floating evaluations separately from its exact integer certificate. Binary64 rounds some tiny positive terms away.

CHECKED: direct local optimization over all atom probabilities on n<=6, followed by a feasibility repair toward the full-set atom. File small_repaired.json writes every atom explicitly. These are lower bounds on the true suprema, not global certificates.

| n | best feasible A/I found |
|---:|---:|
| 1 | 1.99999999997 |
| 2 | 2.51200169367 |
| 3 | 3.23251675125 |
| 4 | 3.73493200534 |
| 5 | 4.03190136968 |
| 6 | 4.18661643908 |

The n=1 supremum is exactly 2: the nonempty atom p must satisfy p>=1/4, and A/I=log2(1/p). All other finite-dimensional global suprema remain OPEN. See search_small.py, small_output.json, repair_small.py, and small_repaired.json.

CHECKED: structured-family searches, all under C(3,2,1/2). Entries are best feasible local values found, in bits per expected element. File families_output.json contains the full probabilities and constraint ratios. EXTREMAL_MEASURES.md writes out every nonzero atom of every finite witness.

| n | nested chains | exchangeable | two-scale | cyclic blocks | products |
|---:|---:|---:|---:|---:|---:|
| 1 | 2.000000000 | 2.000000000 | 2.000000000 | 2.000000000 | 2.000000000 |
| 2 | 2.333796471 | 2.512001694 | 2.512001694 | 2.512001694 | 2.512001694 |
| 3 | 2.715004173 | 3.232516757 | 3.041276143 | 3.041276142 | 2.298701923 |
| 4 | 2.872632898 | 3.734935634 | 2.978049612 | 2.801916713 | 2.512001694 |
| 5 | 2.926146611 | 4.031909603 | 2.939373808 | 2.652025671 | 2.377035426 |
| 6 | 2.942209398 | 4.187125460 | 2.962066145 | 2.557811227 | 2.512001694 |

Nested chains use the empty set and the prefixes {1,...,j}. Exchangeable measures have independently optimized total mass at each cardinality. Two-scale measures use the empty set, a uniform s-layer, and [n], with s also searched. Cyclic blocks replace the uniform layer by the cyclic translates of an interval. Products use independent factors on disjoint blocks of size two, plus one singleton when n is odd. Each product is checked against the full C constraints; closure under products is not assumed. Family classes vary with n, and local maxima can decrease between dimensions. At n=1 the overlapping families are the same two-atom law. Searches use ten starts per linear-orbit family, six per cyclic-block candidate, and twelve per product family; see search_families.py. The unrestricted search uses the restart counts specified in search_small.py.

PROVED: the three-layer family has unbounded A/I, whereas these small finite searches give only moderate values. In particular the largest value found at n=6 is 4.187125460 in the exchangeable family. The main counterexample was found after the initial direct numerical searches, by separating the two large scales.

CHECKED independently with exact rational arithmetic: a smaller diagnostic member of the same parameter form, s=12, n=4096, d=256, q=1/4096, h=4^(-255), has A/I approximately 5.01378983506. check_counter_exact_finite.py checked all 4,096 ranks and all 4,364 distinct Csharp jump constraints exactly after squaring, plus D at all ranks. This lies outside the convenient sufficient range s>=36 of the general proof, and is verified directly. Output: exact_finite_output.json.

CHECKED: check_boolean.py checked all 65,536 Boolean functions on four variables and 4,232 functions on six variables (seed 10010: 2,048 unbiased random, 2,048 biased random, 136 structured entries, possibly repeated). For every R and all nontrivial k it checked C, Csharp, the norm inequality, support/granularity inequalities, derivative square-Parseval, and the derivative level-1 inequality L1D of PROOFS.md. The largest C and Csharp violations were both 0. The largest roundoff residual in the auxiliary comparisons was 1.1102230246251565e-16. These are numerical checks, not exact-arithmetic assertions. Source: boolean_output.json.

PROVED and CHECKED: the proposed restriction-thinning closure with unchanged constants is not a Boolean necessity. A thinned dictator at rho=1/8 gives C left side 0.125 and right side 0.08838834764831845. Each individual restricted function remains Boolean; the averaged spectral measure need not satisfy C. Output: properties_output.json.

PROVED: both the derivative-level inequality L1D and the scalar existential-p analogue hold for the counterexample, so neither excludes it. Its square-Parseval violation is independent of signs: for W=[n] minus an s-set, the only contributing unordered spectral pair is that s-set and [n]. See PROOFS.md section 3 and audit_output.json. CHECKED: check_properties.py verified C and L1D for all 36 finite searched witnesses; maximum C left/right was 0.99999999999 and maximum L1D violation was 0.

PROVED: the same counterexample also has B/I unbounded, with lower bound asymptotic to `(2/3)s-log2(s)-2`; see PROOFS.md section 4. The conditional search for an added cancellation axiom was not triggered.

CHECKED: `python3 run_checks.py` reran all six verification scripts successfully, at inherited nice 10 and with one thread requested for each numerical backend. Peak child RSS during this verification run was 63,209,472 bytes. Source: verification_output.json. Optimization searches are saved separately and are not rerun by this command.

OPEN: exact global finite-n suprema beyond n=1; whether a useful subset of the Boolean square-Parseval constraints, added to the scalar axioms, suffices for containment; containment for actual Boolean spectra; FEI.
