# FEIB16 report

CHECKED: no FEI counterexample was found. The strongest construction in this work is the self-composition tower of the balanced PM(K33) host with nine independent coin sites. The best values, stated as limits of that explicit family, are:

| Ratio | Value to 12 decimals | Evidence |
|---|---:|---|
| H/I | 6.521845710923 | entropy_highprecision.json |
| H^-/I | 4.588257057307 | highprecision.json, tail_bounds.json |
| min_i D_i/Inf_i | 7.111618180512 | highprecision.json, tail_bounds.json |

PROVED: all three tower limits are finite. CHECKED: finite depth 20 already gives H^-/I > 4.5882570573 and min_i D_i/Inf_i > 7.1116181805. Its number of variables is 18^20 = 12,748,236,216,396,078,174,437,376, as recorded in tower.json. The analytic remainder after depth 30 is below 4.9e-18 for both the erasure and minimum-drop ratios. The logarithms were checked at 80 decimal digits; these are numerical evaluations with an analytic tail bound, not directed-rounding interval certificates. The H/I value reproduces the known record limit, rather than improving it. All entropy quantities are in bits; ratios are bits per unit influence.

## Verdict on each brief item

1. PROVED, CHECKED: exact composition laws for arbitrary biased, nonidentical inner blocks are in FORMULAS.md. Messages retain the mean, nonempty spectral mass, entropy, and each coordinate type's influence, singleton coefficient, erasure and restriction drop. The empty-inner-remainder edge supplies the necessary correction. Direct truth tables verified 177 random compositions, plus the explicit tribes and threshold cases, to tolerance 1e-12; the largest error was below 1.8e-15 in validation.json.

2. PROVED, CHECKED: formulas cover tribes, majority and iterated majority, recursive tribes, AND/OR trees, address, every bent/MM spectrum, complete quadratics, bent point replacements, PM host and coin lifts, PM compositions, disjoint XOR and AND. The plain-tribes scan evaluated 4,679,850 width/count pairs up to one million variables; analytic bounds exclude larger widths from its maxima. Its best H^-/I and minimum-drop ratios are 3.606847002096 and 6.003746056559, both at width 2 and 8 tribes. Every requested regular-tree depth through six was evaluated with logarithmic probability messages; the smallest minority log-probability was about -973574.565246 bits. Additional depth-20 evaluations and finite-limit proofs describe growth. Exact arbitrary point-set bent patches use O(m 2^m) core-spectrum work; affine-subspace patches reach m=200 without allocating the fresh dictators. See families.json, stable_readonce.json, family_limits.json, majority_large.json and pm_biased_towers.json. OPEN: optimization over unrestricted point sets, all PM lifts, and all family parameters was not certified. Extra biased PM seed towers have an explicit variance cutoff; no value beyond that cutoff is claimed.

3. CHECKED: two-level and three-level top-20 tables for each ratio, with exact construction parameters, are in RESULTS.md and ranked_compositions.json. Every outer four-variable NPN class and input phase was included. The two-level inner pool has 701 choices; the three-level beam has 52 two-level messages. Uniform assignments were exhaustive within those pools. Mixed assignments used coordinate ascent and three starts per objective. The best found values were:

| Search | H/I | H^-/I | min D_i/Inf_i |
|---|---:|---:|---:|
| Two-level | 5.100527688049 | 3.850121291403 | 6.258363742048 |
| Three-level | 5.299241089783 | 4.059086444978 | 6.468607549690 |

OPEN: the mixed and three-level searches are heuristic, and no global optimum over arbitrary inner parameters is claimed. Symmetry-equivalent parameterizations can tie. “Levels” count census-gate layers around the permitted primitive inner family; a tribes primitive already has its own AND/OR description.

4. CHECKED: all 616,126 imported five-variable NPN representatives, all 32 input phases, and 13 AND/threshold choices gave 256,308,416 evaluations. Uniform blocks remove the need to repeat variable permutations, and output complement leaves these ratios unchanged. Thus every outer function on at most five variables is represented, for the stated inner choices. A separate stable entropy rescan covered the same cases. The best H/I, H^-/I and minimum-drop values were 4.128880076270, 3.433874258511 and 5.784103212114. Exact inner parameters and winning outer tables appear in RESULTS.md, pool5.tsv, census5.tsv and census5_entropy.tsv. OPEN: thresholds outside the listed parameter range and all possible biases.

5. PROVED, CHECKED: WITNESSES.md gives explicit parity, block and level predictors. pm_orbits_depth6.csv and pm_orbits_depth10.csv list every core/coin type-word orbit at those depths, with E_i/Inf_i and D_i/Inf_i; the exact word formula covers larger depths without an exponential listing. The record tower's sufficient statistic is the first relevant block/level together with the base gate's spectral amplitude-pair class. Plain tribes use a three-cell block statistic; odd functions use degree parity. OPEN: a bounded-cost witness scheme for general Boolean spectra.

## Checks and numerical limitations

CHECKED: independent Python and native composition calculations agree within 2.7e-15 on the ranked candidates in audit.json. Direct restriction entropies independently verify the base PM drops. Exact dyadic edge histograms, a path dynamic program, and 80-digit arithmetic independently check the tower. All 90 saved small truth-table entries were checked directly; the largest ratio error was below 3.6e-15 in results_build_audit.json. The large-majority calculation checks Parseval separately and records its finite-precision residual; its million-variable figures are not 1e-12 claims.

CHECKED: the wide biased scan initially produced spurious large entropy ratios when the empty coefficient rounded near a constant. Those rankings were rejected and recomputed using the nonempty spectral mass and log1p. Extreme regular trees use the separate logarithmic recursion. The corrected outputs and the explicit UNRELIABLE float diagnostics are separated. No spurious large value is treated as a counterexample.

CHECKED: no helper agents, truth-table hill climb, external posts, git push or production processes were used. All writes stayed in this folder. The scripts are single-threaded; numerical-library thread counts were set to one. The process scheduling check in make_pool.py recorded nice 10. Folder size, input hashes, validation status and final audit resources are recorded in final_audit.json and manifest.json. Brain recall helped identify the exact nine-coin PM record and relevant earlier pitfalls; the launching session can import LEARNINGS.md without this worker modifying shared memory.

CHECKED: reproduce.sh gives the ordered commands. It reads the existing NPN census files in FEIB13 and writes only in FEIB16. It reruns the full scans and therefore takes longer than the audits alone.

OPEN: FEI, the optimal universal constants, unrestricted mixed-composition optimization, and interval-certified decimal bounds remain open. The task's derivations, finite searches, family evaluations, orbit formulas and artifacts are complete within the explicit scopes above.

Task: “Do the brief fully and carefully” — FEIB16, 10 Nov 2026 04:38 +04 (observed worker start).
