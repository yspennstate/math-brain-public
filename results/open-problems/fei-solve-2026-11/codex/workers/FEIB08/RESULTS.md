# FEIB08 results

All entropies and logarithmic costs are in bits. Influence is the expected spectral-set cardinality, or equivalently a sum of edge-flip probabilities. Ratios are dimensionless. Decimal entries are rounded from the named JSON files. All Fourier and restriction coefficients are computed using integer Walsh transforms; logarithms and radicals are evaluated in double precision. These are arithmetic checks, not model-comparison benchmarks.

## Exhaustive four-variable check

Generator: `clang++ -O2 -std=c++17 exact4.cpp -o exact4 && ./exact4 > data/exact4.json`. The tool shell inherits nice 10 (checked with `os.getpriority(os.PRIO_PROCESS,0)`). One computation thread. An extra `nice -n 10` attempts to add to the inherited niceness and is denied by the sandbox; the command still runs at the inherited priority.

The census covers 65,536 Boolean functions, 1,802,480 nonzero restriction/level cases, and 983,040 nonempty Boolean-convolution checks. Each function uses every nonempty proper live block J and every retained level r=1,...,|J|. Lower-dimensional functions are included as functions independent of some coordinates.

The tested quantities are X=E max h_T^2, Y=E(sum |h_T|^(8/3))^(3/4), E2=max E h_T^2, Z=sum E h_T^2, with h_T the coefficients of the Boolean restriction to J at level r. Lemma 3.5 gives X<=3^q sqrt(E2 Z); Lemma 5.1 with h′=h gives Y<=3^q E2^(1/4)Z^(3/4). q is the actual degree in the fixed-outside variables.

| Ratio | Maximum | First truth table | J mask | r | q | Left side | Right side |
|---|---:|---|---|---:|---:|---:|---:|
| X / sqrt(E2 Z) | 1.41421356237 | 0x001b | 0x6 | 1 | 2 | 0.5 | 0.353553390593 |
| Y / (E2^(1/4)Z^(3/4)) | 1.189207115 | 0x001b | 0x6 | 1 | 2 | 0.5 | 0.420448207627 |
| Lemma 3.5, including 3^q | 1 | 0x0003 | 0xe | 3 | 0 | 0.0625 | 0.0625 |
| Lemma 5.1, including 3^q | 1 | 0x0003 | 0xe | 1 | 0 | 0.14246919106 | 0.14246919106 |

The two deletion maxima are exactly sqrt(2) and 2^(1/4). PROOFS.md section 7 proves the upper bounds independently of the enumeration. The witness has X=Y=1/2, E2=1/4, Z=1/2; its restricted coefficient table is saved in `data/independent_audit.json`. The published-bound maxima include q=0 equality cases; they do not show sharpness of the exponential factor.

| Arithmetic or inequality audit | Maximum absolute error or positive violation |
|---|---:|
| integer_or_inequality_failures | 0 |
| max_identity_error | 1.33226762955e-15 |
| max_magnitude_bound_error | 4.4408920985e-16 |
| max_jensen_violation | 6.66133814775e-16 |
| max_tree_error | 6.66133814775e-16 |
| max_chain_error | 8.881784197e-16 |
| max_talagrand_violation | 0 |
| max_isoperimetric_violation | 0 |

Zero integer failures includes Parseval, every nonempty Boolean convolution, and derivative granularity. The identity error includes H=2A1+2Gamma and the min-entropy split. The tree audit uses L1 and L-infinity in one fixed coordinate order. The chain audit includes its total flow I+1. The Talagrand and support-isoperimetry violations are both zero. Integer moments are exact; norm ratios, logarithms, and the resulting bounds use double precision.

The maximum level-one expected-log-minimum-influence ratio in the census is 1.40625. The proved universal bound is 4log2(3)+4/(e ln2)=8.46280138458; this decimal is obtained by `python3 -c "import math; print(4*math.log2(3)+4/(math.e*math.log(2)))"`.

| Budget or level right side divided by I | Maximum | First truth table | Detail |
|---|---:|---|---|
| sum at one subset level / I | 1.5 | 0x6996 | r=2; numerator 6, I=4 |
| sum_r u1 / I | 2.08333333333 | 0x6996 | r=0; numerator 8.33333333333, I=4 |
| J / I | 1.4649755512 | 0x0001 | r=0; numerator 0.732487775599, I=0.5 |

Parity gives the first two maxima: C(4,2)/4=1.5 and H_4=25/12. The first J/I maximum is the single-negative-input AND/OR variant 0x0001. These are maxima only at four variables.

## Requested extremals and structured restrictions

Generator: `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 verify_and_families.py > data/families.txt`; raw data: `data/families.json`. The independent witness audit also recomputes Fourier coefficients by direct character sums. All proper live blocks are used for the two five-variable extremals. For larger families the chosen blocks are listed below; maxima apply only to those blocks and all of their retained levels.

| Function | n | I | H | B | J/I | Max X/R3 | Max Y/R5 | Harmonic/I |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| extremal_0000000e | 5 | 0.6875 | 2.334164454 | 1.017182569 | 1.54653626 | 1 | 1 | 1.60842803 |
| extremal_008eeeee | 5 | 1.625 | 3.608458593 | 1.346099609 | 0.9788287451 | 1.118861856 | 1.116282968 | 1.471955128 |
| majority_3 | 3 | 1.5 | 2 | 0.75 | 0.5 | 1 | 1 | 1.416666667 |
| majority_5 | 5 | 1.875 | 3.32537578 | 1.513999507 | 0.8074664035 | 1 | 1 | 1.689583333 |
| majority_9 | 9 | 2.4609375 | 5.260150303 | 2.858340831 | 1.161484528 | 1 | 1 | 2.059669519 |
| majority_15 | 15 | 3.142089844 | 7.402862073 | 4.523790949 | 1.439739528 | 1 | 1 | 2.422733105 |
| tribes_w2_t2 | 4 | 1.5 | 3.32537578 | 1.19393789 | 0.8324611714 | 1.272792206 | 1.151365692 | 1.378472222 |
| tribes_w2_t3 | 6 | 1.6875 | 4.620958172 | 1.663947638 | 1.037305213 | 1.5011107 | 1.25285921 | 1.496064815 |
| tribes_w3_t3 | 9 | 1.72265625 | 5.255148258 | 1.969254437 | 1.26598565 | 1.643227689 | 1.291760627 | 1.588201942 |
| tribes_w3_t4 | 12 | 2.009765625 | 6.287984805 | 2.179874086 | 1.236022765 | 2.205507037 | 1.508361836 | 1.649016055 |
| tribes_w4_t4 | 16 | 1.647949219 | 5.673750363 | 2.152041277 | 1.495778624 | 2.338325821 | 1.539383959 | 1.736009407 |
| address_1 | 3 | 1.5 | 2 | 0.5 | 0.5283208336 | 1.414213562 | 1.189207115 | 1.333333333 |
| address_2 | 6 | 2 | 4 | 1 | 0.7054820237 | 2 | 1.414213562 | 1.5625 |
| address_3 | 11 | 2.5 | 6 | 1.5 | 0.7871996431 | 2.828427125 | 1.681792831 | 1.741666667 |
| parity_4 | 4 | 4 | 0 | 0 | 0 | 1 | 1 | 2.083333333 |
| parity_16 | 16 | 16 | 0 | 0 | 0 | 1 | 1 | 3.380728993 |

R3=sqrt(E2 Z), R5=E2^(1/4)Z^(3/4); the table deliberately omits 3^q to test its deletion. The paper bounds include that factor.

| Function and maximized step | Live mask | r | q | Left side | Right side without 3^q | Exact E2 | Exact Z |
|---|---|---:|---:|---:|---:|---|---|
| extremal_0000000e, 3.5 | 0x1 | 1 | 4 | 0.0625 | 0.0625 | 1/16 | 1/16 |
| extremal_0000000e, 5.1 | 0xf | 4 | 1 | 0.0078125 | 0.0078125 | 1/128 | 1/128 |
| extremal_008eeeee, 3.5 | 0xd | 1 | 2 | 0.40625 | 0.363092188707 | 9/32 | 15/32 |
| extremal_008eeeee, 5.1 | 0xb | 1 | 2 | 0.397589828766 | 0.356172977649 | 5/32 | 15/32 |
| majority_3, 3.5 | 0x1 | 1 | 2 | 0.5 | 0.5 | 1/2 | 1/2 |
| majority_3, 5.1 | 0x1 | 1 | 2 | 0.5 | 0.5 | 1/2 | 1/2 |
| majority_5, 3.5 | 0x1 | 1 | 4 | 0.375 | 0.375 | 3/8 | 3/8 |
| majority_5, 5.1 | 0x3 | 2 | 3 | 0.1875 | 0.1875 | 3/16 | 3/16 |
| majority_9, 3.5 | 0x1 | 1 | 8 | 0.2734375 | 0.2734375 | 35/128 | 35/128 |
| majority_9, 5.1 | 0xff | 3 | 0 | 0.0312364082029 | 0.0312364082029 | 25/16384 | 175/2048 |
| majority_15, 3.5 | 0x1 | 1 | 14 | 0.20947265625 | 0.20947265625 | 429/2048 | 429/2048 |
| majority_15, 5.1 | 0x3fff | 7 | 0 | 0.00267264061213 | 0.00267264061213 | 25/4194304 | 10725/524288 |
| tribes_w2_t2, 3.5 | 0x5 | 1 | 2 | 0.5625 | 0.441941738242 | 5/16 | 5/8 |
| tribes_w2_t2, 5.1 | 0x5 | 1 | 2 | 0.605112051907 | 0.525560259534 | 5/16 | 5/8 |
| tribes_w2_t3, 3.5 | 0x15 | 2 | 3 | 0.1015625 | 0.0676582346707 | 5/128 | 15/128 |
| tribes_w2_t3, 5.1 | 0x15 | 2 | 3 | 0.111558648882 | 0.0890432444123 | 5/128 | 15/128 |
| tribes_w3_t3, 3.5 | 0x49 | 2 | 6 | 0.0361328125 | 0.021988926268 | 13/1024 | 39/1024 |
| tribes_w3_t3, 5.1 | 0x49 | 2 | 6 | 0.0373823311103 | 0.028939054434 | 13/1024 | 39/1024 |
| tribes_w3_t4, 3.5 | 0x249 | 2 | 8 | 0.0557250976562 | 0.025266343172 | 169/16384 | 507/8192 |
| tribes_w3_t4, 5.1 | 0x249 | 2 | 8 | 0.0596466062841 | 0.0395439640934 | 169/16384 | 507/8192 |
| tribes_w4_t4, 3.5 | 0x1111 | 2 | 12 | 0.0183753967285 | 0.00785835599396 | 841/262144 | 2523/131072 |
| tribes_w4_t4, 5.1 | 0x1111 | 2 | 12 | 0.0189328706703 | 0.0122989917909 | 841/262144 | 2523/131072 |
| address_1, 3.5 | 0x6 | 1 | 1 | 1 | 0.707106781187 | 1/2 | 1 |
| address_1, 5.1 | 0x6 | 1 | 1 | 1 | 0.840896415254 | 1/2 | 1 |
| address_2, 3.5 | 0x3c | 1 | 2 | 1 | 0.5 | 1/4 | 1 |
| address_2, 5.1 | 0x3c | 1 | 2 | 1 | 0.707106781187 | 1/4 | 1 |
| address_3, 3.5 | 0x7f8 | 1 | 3 | 1 | 0.353553390593 | 1/8 | 1 |
| address_3, 5.1 | 0x7f8 | 1 | 3 | 1 | 0.594603557501 | 1/8 | 1 |
| parity_4, 3.5 | 0x3 | 2 | 2 | 1 | 1 | 1 | 1 |
| parity_4, 5.1 | 0x3 | 2 | 2 | 1 | 1 | 1 | 1 |
| parity_16, 3.5 | 0xff | 8 | 8 | 1 | 1 | 1 | 1 |
| parity_16, 5.1 | 0xff | 8 | 8 | 1 | 1 | 1 | 1 |

For exact left sides, X is stored as `exact_X`. Y is stored as an algebraic expression in `exact_Y_terms`: divide the sum over terms of multiplicity times (sum over magnitudes v of count*v^(8/3))^(3/4) by `outside_rows*retained_size^2`. Thus the tables can be reconstructed from integers and radicals, rather than treating a rounded floating-point result as an exact number.

The five-variable checks give B/I=1.47953828252 for 0x0000000e, and B/(I-1)=2.15375937482 for balanced 0x008eeeee. They agree with the values in NOTES.md; this worker did not repeat a five-variable exhaustive census.

Selected live blocks: majority uses the first j coordinates for j in {1,floor(n/2),n-1}; tribes uses one coordinate per tribe, and all coordinates in the first floor(t/2) tribes; address uses all data coordinates or all address coordinates; parity uses the first floor(n/2) coordinates. All corresponding masks are in the JSON.

## Address family obstruction for every k

PROOFS.md proves X=Y=Z=1, E2=2^(-k), q=k for live data coordinates. The following values are generated in `data/address_formula.json`; k<=3 was also evaluated from full truth tables. Larger k is a formula calculation, not a full truth-table enumeration.

| Address bits k | Variables n | I | H=Hinf | X/R3 | Y/R5 |
|---|---:|---:|---:|---:|---:|
| 1 | 3 | 1.5 | 2 | 1.414213562 | 1.189207115 |
| 2 | 6 | 2 | 4 | 2 | 1.414213562 |
| 3 | 11 | 2.5 | 6 | 2.828427125 | 1.681792831 |
| 4 | 20 | 3 | 8 | 4 | 2 |
| 8 | 264 | 5 | 16 | 16 | 4 |
| 12 | 4108 | 7 | 24 | 64 | 8 |
| 20 | 1048596 | 11 | 40 | 1024 | 32 |

This family has f^2=1 and derivative values in {0,1}; a constant-factor version of either local inequality is impossible. It does not force the logarithm in an entropy/influence theorem.

## Balanced-scale tribes: loss in the level Jensen bound

Generator: `python3 tribes_levels.py > data/tribes_levels.jsonl`; raw final data `data/tribes_levels.json`. Width w and number of tribes t=round((ln2)2^w). Integer polynomial coefficients calculate W_d and M_d over denominator 2^(2wt). J includes the empty level. H is independently calculated from the touched-tribe count, and I from the direct influence formula.

| w | t | n | I | H/I | J/I | E[|S|log2(|S|+1)]/I |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 6 | 1.6875 | 2.738345583 | 1.037305213 | 1.592162884 |
| 3 | 6 | 18 | 2.30809021 | 3.438772068 | 1.349008798 | 1.925298 |
| 4 | 11 | 44 | 2.884532613 | 3.680620884 | 1.520381669 | 2.158917818 |
| 5 | 22 | 110 | 3.529545041 | 3.843975259 | 1.688208115 | 2.384629297 |
| 6 | 44 | 264 | 4.191395992 | 3.922439142 | 1.819945996 | 2.579459379 |
| 7 | 89 | 623 | 4.881555011 | 3.965303276 | 1.933349516 | 2.755867507 |
| 8 | 177 | 1416 | 5.555090585 | 3.981362345 | 2.025814654 | 2.906757217 |
| 9 | 355 | 3195 | 6.24688282 | 3.991350123 | 2.111015886 | 3.046656001 |

Maximum discrepancy between the two entropy calculations: 1.31450406116e-13 bits. Maximum influence discrepancy: 4.4408920985e-16.

The finite table illustrates, and PROOFS.md section 8 proves, J=Theta(I log I) and H=4I(1+o(1)). No asymptotic conclusion is inferred from the table alone.

## Access and limitations

Shell `curl -L --fail --max-time 40 https://arxiv.org/pdf/1911.10579 -o sources/kklms.pdf` failed with exit 6 because DNS is blocked. The browsing tool successfully opened the complete PDF and the HTML rendering. Saved browsing excerpts are under `sources/`; online statement numbers and pages are in PROOFS.md and REPORT.md. No PDF file was downloaded locally.

The check uses the symmetric h′=h subcase of Lemma 5.1; it does not enumerate every pair of distinct f and g. Structured-function block searches are scoped as declared. Full Corollary 6.7 has enormous absolute constants and is already vacuous on these tiny coefficient scales; the informative exact tests concern its local restriction lemmas and the proposed subset/harmonic accounting. No claim that the final logarithm is necessary for FEI is made.
