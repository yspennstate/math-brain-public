# FEIB26 results

Completed on 10 Nov 2026. Ratios below are bits per unit influence. Entropies are in bits; influences are expected spectral set sizes. All logarithms are base two.

## Finite transitive record

Ninety-digit outward intervals give **4.50504996749762 < G < 4.50504996749764** for the seven-layer alternating PM9/complemented-PM9 function on 4,782,969 variables. `interval_witness.py` writes `interval_witness.json`. The function is specified completely in PROOFS.md section 13; no giant truth table is needed.

Independent biased-coefficient calculations give leaf influence 1.43210796476062e-05, total influence 68.4972800010312, H=438.520970709336 bits, H/I=6.40202020726566, and sum_i E_i=308.583669042321 bits. See `periodic_audit.json`, from `python3 periodic_audit.py`.

Already the two-layer PM9 self-composition on 81 variables has G=4.048135961762372, also enclosed in `interval_witness.json`. The five-layer PM9 self-tower gives G=4.474995805835325. Thus the brief's 3.7137 benchmark is exceeded by explicit transitive functions. These are lower bounds, not upper bounds or novelty claims.

## Composition and towers

PROVED in `PROOFS.md` sections 1–6: balanced-inner composition, the corrected biased spectral law for unbalanced inner functions, entropy/influence/erasure recurrences, convergence for every nonconstant transitive self-tower, and an explicit finite-gate truncation bound. Empty-block amplitudes must be added before squaring. The monotone quantity is R=(E_i-Phi(c²,s²))/Inf_i, rather than G itself. The limit of G equals the limit of R.

For a balanced transitive base with singleton mass b, coordinate influence delta and thinned function T, the exact limit is sum_{j>=0} T(b^j)/delta^(j+1). H_r=H_base (I_base^r-1)/(I_base-1), I_r=I_base^r and sum E_i=I_r G_r. The unbalanced case uses the finite bias-dependent kernels in the proofs.

| Base or bottom-to-top repeating period | Limit G | Evidence |
|---|---:|---|
| PM9 | 4.474150253078 | pm_audit.json |
| complemented PM9 | 4.501578800702 | periodic_towers.json; mixed_audit.json |
| complemented PM9, PM9 | 4.505015258443 | periodic_audit.json |
| tribes_2x2 | 3.655710535228 | towers.json |
| tribes_2x3 | 2.574333462779 | towers.json |
| tribes_3x2 | 4.126377832472 | towers.json |
| tribes_3x3 | 2.962629739677 | towers.json |
| tribes_4x2 | 3.909867701738 | towers.json |
| tribes_4x3 | 3.249737141752 | towers.json |
| tribes_2x4 | 2.255668487354 | towers.json |
| bent_inner_product2 | 2.000000000000 | towers.json |
| bent_inner_product4 | 2.474169509928 | towers.json |
| bent_inner_product6 | 2.186492002085 | towers.json |

`periodic_towers.py` evaluates 400 ordered pairs of small transitive gates, including both output signs. The best retained limit is the alternating PM period above. `mixed_search.py` performs a separate variable-gate beam search; its best nine-layer finite value was 4.503373453940 and was independently checked in `mixed_audit.json`. The periodic construction later improved it. Balanced-only mixed towers are in `mixed_towers.json`.

`bent_census.py` checks all eight bent functions on two variables and all 896 on four variables; respectively four and sixteen are transitive under coordinate permutations. It also checks symmetric quadratic examples on six and eight variables. `bent_census.json` and its log hold the full results. The largest retained bent-base self-tower limit is about 3.655710535228.

The balanced nine-input functions formed by invariant modifications of the PM host are recorded in `balanced_pm.json`; its best limit is about 4.341134068602. This is below the best unbalanced PM periods.

## Exhaustive small transitive functions

The following finite maxima and self-tower maxima are numerical results of exhaustive orbit-sign enumeration. The entries are approximate, not formal optimization certificates. Prime degrees are covered up to relabeling by cyclic enumeration; every degree-four and degree-six transitive group action was also exhausted. `GROUPS.md` explains this coverage and the GAP generator provenance.

| n | Maximum finite G | Maximum balanced-base tower limit | Maximum self-tower limit, both output signs |
|---:|---:|---:|---:|
| 2 | 2.000000000000 | 0.000000000000 | 3.655710535228 |
| 3 | 2.672488983973 | 0.000000000000 | 2.962629739677 |
| 4 | 2.634003390886 | 1.342941553101 | 4.137065543117 |
| 5 | 2.453729842625 | 2.170653474386 | 3.503745851673 |
| 6 | 2.944495303872 | 2.026910737025 | 4.126377832472 |
| 7 | 2.938629714949 | 3.271795870183 | 3.515013925538 |

The cyclic self-tower enumeration evaluated 1,065,304 orbit-sign assignments, including constants and both output complements. Every row is in `census/*.tower.csv.gz`; the extra group actions have their own compressed row files under `groups/`. The 128 flagged endpoint rows at degree seven were replayed at high precision and are below the maximum (`census_audit.json`). Every stored catalog-action maximum was independently replayed (`group_audit.json`).

All 50 degree-eight transitive group actions were surveyed: 21 with at most twenty input orbits were exhausted; the other 29 were annealed. This is a partial function search at degree eight. Its largest finite G was about 3.304701322451. Generators, orders, orbit counts and witness functions are saved.

## Larger searches

`search.py` and `search.py other` made 126,867 total objective evaluations, including scale probes, with cyclic structured seeds, random seeds, single-orbit and pair-orbit flips, and G/H-I objective mixtures. Each retained function is one stored sign per orbit. `tower_search.py` made another 80,036 objective evaluations using the tower residual as its objective, including two transitive nine-coordinate grid groups. These are bounded annealing searches; none is an upper bound.

| Action | Variables | Best finite G | Actual objective evaluations |
|---|---:|---:|---:|
| cyclic | 12 | 3.129190264398 | 20,562 |
| cyclic | 13 | 3.175299634414 | 12,558 |
| cyclic | 14 | 3.211474596841 | 8,556 |
| cyclic | 15 | 3.223062956179 | 5,566 |
| cyclic | 16 | 3.239282352713 | 3,565 |
| cyclic | 17 | 3.250613950966 | 2,369 |
| cyclic | 18 | 3.291358270324 | 1,564 |
| cyclic | 19 | 3.325803939710 | 1,219 |
| cyclic | 20 | 3.352335440440 | 966 |
| dihedral | 8 | 3.304701322451 | 16,560 |
| graph5 | 10 | 3.267746965382 | 30,438 |
| translation | 8 | 3.304701322451 | 16,434 |
| translation | 16 | 2.528084706018 | 6,510 |

The four-vertex graph-property class has eleven input orbits, so 2,048 functions were covered using 1,024 output-complement representatives; its best finite G is 2.944495303872. Five-vertex graph properties were annealed. Translation actions are on coordinates indexed by F_2^3 and F_2^4. The extra n=4 translation census also covers the Klein four group. `verification.json` independently rebuilds every retained search witness and checks pivotal influences, equality across coordinates, and two entropy formulas.

## Six-variable amplification base

Hod's published correction supplies a balanced replacement for the inconsistent displayed O'Donnell–Tan DNF. `hod_reconstruct.py` obtains H=3.924340782942887 bits, I=13/8 and amplified H/(I-1)=6.278945252709. The base is not transitive. `ot_tower_dp.py` minimizes over all leaf-path types, using exact product-influence state keys and a uniform analytic tail bound.

| Reconstructed balanced base | Minimum tower limit over every leaf-path type |
|---|---:|
| Hod_g3_OT_replacement | [3.684862634064, 3.684862634074] |
| Hod_g3_prime | [4.014846466000, 4.014846466027] |

These brackets include analytic truncation error; floating arithmetic is not outward-rounded here. Minimizing only constant-coordinate paths would overestimate the minimum. The source and diagnostic failed literal reconstructions are retained in `LITERATURE.md`, `odonnell_tan.json`, `ot_reconstruction.json` and `ot_literal_search.json`.

## Proof attempts and remaining questions

PROVED in `PROOFS.md` sections 7–11: E_1<=12.04 Inf_1 for symmetric functions using the published symmetric FEI theorem; E_1<=(w+7.94)Inf_1 for ORs of cyclic shifts of a width-w literal pattern; E_1<=(wl+7.94)Inf_1 for a threshold of l such shifts; the exact size-biased deletion identity; and an obstruction showing why invariance/Han alone cannot suffice. An exact product spectral law with rational inclusion p is excluded by Boolean singleton-shift convolution unless p=1/2. This does not give a stability estimate.

OPEN: one absolute constant for all transitive Boolean functions; any identification of the transitive supremum with G_* or with C_* minus a specific constant; and general FEI. The convolution attempt and its precise missing estimate are written in section 11. The bounds depending on w or l do not settle their unbounded-width cases.

## Verification and resource record

`checks.py` checks 401 small compositions. Its largest H error is 3.55e-15 bits; amplitude and influence errors are zero. `subclass_checks.py` checks all 65,536 four-variable truth tables at all four coordinates (262,144 coordinate checks), the scalar two-point inequality, and 120 shift-pattern examples. No inequality violation was found.

`verify.py` rebuilds 50 saved witnesses; the largest absolute G discrepancy from the compiled search is 1.13e-11, and its two erasure-entropy formulas differ by at most 1.16e-14 bits. The finite record has the stronger separate interval check.

The verification process inherited nice 10, set all three math thread controls to one, and measured peak RSS 396,197,888 bytes (377.84 MiB). Work used at most two concurrent single-thread computations; arrays were sized below the process memory limit. The folder was 37,952,869 bytes when `run_summary.json` was generated, below the 150 MB limit. Compressed census rows replace raw scratch CSVs.

Brain recall was read-only and helped recover the earlier FEI cautions; no recalled claim was used as a theorem. Math recall reported no installed store. The named `relative_step.py` was missing, so the local checks implement their own formulas. The fleet rule prohibiting writes outside this folder was followed: no mesh/checklist/brain mutation, posting, pushing or publication was attempted. `LEARNINGS.md` is a local handoff for the launching session.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 2026, 22:20 ask; worker FEIB26.
