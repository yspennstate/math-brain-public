# FEIB22 report

For a bulk site of a critical Hex crossing, I derive a board-size-independent bound on E_i/Inf_i. A geometric nested ball witness already suffices. The argument uses standard four-arm estimates and is supplied in [ARGUMENT.md](ARGUMENT.md); it is a derivation made here and awaits referee review. It does not solve general FEI.

The experiment also shows a finite witness gap. Keeping two spectral hits improves the nested estimate, but does not flatten its finite-size rise on the boards tested. A fixed local block behaves differently: I prove that every fixed finite block witness eventually grows logarithmically, even though the bulk-coordinate ratio and a suitable nested ball witness remain bounded.

## Centre-coordinate table

Entropies are in bits; ratios are bits per unit influence. Every ± is one sampling standard error. Exact entries have SE zero; floating-point error is checked below. The centre is the same zero-based site (L//2,L//2) used by mc_chain.py.

The nested column uses the original mc_chain.py cardinality-prefix ball chain. The two-hit column records the shells of its first two distinct spectral points, including same-shell ties. It is a coarsening of the vertex-resolved last-two witness and therefore also bounds that witness from above. On large boards it is a jackknife-corrected estimate, with remaining finite-sample bias audited below. The block columns on large boards estimate an independent tangent upper target, rather than an unchecked plug-in. Their numerical estimates still have sampling uncertainty. Small-board blocks are exact and are truncated by the board boundary.

| L | Inf_i | nested/Inf | two-hit shells/Inf | block r=1/Inf | block r=2/Inf | exact E_i/Inf |
|---|---|---|---|---|---|---|
| 3 | 0.3203125 ± 0.0000000 | 2.1627 ± 0.0000 | 1.7835 ± 0.0000 | 2.0735 ± 0.0000 | 1.4883 ± 0.0000 | 1.4883 ± 0.0000 |
| 4 | 0.1859741 ± 0.0000000 | 3.0133 ± 0.0000 | 2.6617 ± 0.0000 | 3.3491 ± 0.0000 | 2.6457 ± 0.0000 | 2.1085 ± 0.0000 |
| 5 | 0.1713845 ± 0.0000000 | 3.1219 ± 0.0000 | 2.7844 ± 0.0000 | 3.4857 ± 0.0000 | 2.5556 ± 0.0000 | 2.0008 ± 0.0000 |
| 8 | 0.0931158 ± 0.0002613 | 3.7638 ± 0.0121 | 3.4162 ± 0.0120 | 3.9586 ± 0.0062 | 3.6792 ± 0.0050 | not enumerated |
| 12 | 0.0589256 ± 0.0001624 | 4.0850 ± 0.0074 | 3.7368 ± 0.0109 | 4.2233 ± 0.0134 | 3.9112 ± 0.0040 | not enumerated |
| 16 | 0.0425010 ± 0.0001337 | 4.2483 ± 0.0087 | 3.8968 ± 0.0106 | 4.3923 ± 0.0092 | 4.0232 ± 0.0045 | not enumerated |
| 24 | 0.0261617 ± 0.0001190 | 4.4590 ± 0.0097 | 4.1151 ± 0.0169 | 4.5801 ± 0.0162 | 4.1473 ± 0.0044 | not enumerated |

Sources and commands: exact entries come from `python3 study.py exact 3`, `exact 4`, `exact 5 noopt`, and `python3 audit.py --no-windows`, consolidated in [small_centre_table.json](small_centre_table.json). Larger window entries come from `python3 run_suite.py windows`, plus `python3 study.py window 8 32 32768 8007 original`; final summaries are regenerated from the saved counts by `python3 finalise_windows.py`. Block entries come from `python3 run_suite.py blocks`, with fixed smoothing alpha=0.001, and their corresponding block_L*_r*_s*.json files. The input and estimator definitions are in [METHODS.md](METHODS.md).

## Exact optima at every site

All site influences, erasure ratios, and globally optimal nested and vertex-resolved last-two witnesses on L=3,4,5 are in [exact_all_sites.csv](exact_all_sites.csv). Both optimisations range over all coordinate orders using subset shortest paths. Returned orders are independently regrouped against the full spectrum. L=5 symmetries are checked entrywise before they are used.

| L | centre exact E/Inf | best nested/Inf | best vertex last-two/Inf | sampling SE |
|---|---|---|---|---|
| 3 | 1.48829004 | 1.96313225 | 1.64067330 | 0 |
| 4 | 2.10845167 | 2.84088737 | 2.42395029 | 0 |
| 5 | 2.00083008 | 3.04277321 | 2.55567756 | 0 |

Commands: `python3 study.py exact 3`, `python3 study.py exact 4`, `python3 study.py exact 5 noopt`, `python3 optimal5.py`. The per-site and order files are exact_L3.json, exact_L4.json, exact_L5.json, and optimal_L5.json.

## Bias checks and independent upper targets

Every final block run uses 16 independent batches of 1,024 outside configurations. The first half chooses a positive pilot tangent and the second half estimates its expectation. Concavity gives a true entropy upper functional for every fixed pilot; quoted SEs are conditional on that pilot and include numerator/denominator covariance. The smaller-sample plug-ins are reported as estimates, not upper bounds.

| L | radius | plug-in at N=1,024 | plug-in at N=4,096 | pooled N=16,384 | jackknife at N=16,384 | tangent upper target |
|---|---|---|---|---|---|---|
| 8 | 1 | 3.9701 ± 0.0069 | 3.9709 ± 0.0094 | 3.9710 ± 0.0068 | 3.9711 ± 0.0068 | 3.9586 ± 0.0062 |
| 8 | 2 | 3.6705 ± 0.0039 | 3.6718 ± 0.0042 | 3.6721 ± 0.0039 | 3.6722 ± 0.0039 | 3.6792 ± 0.0050 |
| 12 | 1 | 4.2156 ± 0.0081 | 4.2171 ± 0.0157 | 4.2173 ± 0.0082 | 4.2174 ± 0.0082 | 4.2233 ± 0.0134 |
| 12 | 2 | 3.9074 ± 0.0027 | 3.9096 ± 0.0015 | 3.9101 ± 0.0028 | 3.9103 ± 0.0028 | 3.9112 ± 0.0040 |
| 16 | 1 | 4.3711 ± 0.0068 | 4.3739 ± 0.0101 | 4.3741 ± 0.0068 | 4.3744 ± 0.0068 | 4.3923 ± 0.0092 |
| 16 | 2 | 4.0177 ± 0.0036 | 4.0206 ± 0.0041 | 4.0214 ± 0.0036 | 4.0216 ± 0.0036 | 4.0232 ± 0.0045 |
| 24 | 1 | 4.5680 ± 0.0101 | 4.5721 ± 0.0145 | 4.5724 ± 0.0101 | 4.5727 ± 0.0101 | 4.5801 ± 0.0162 |
| 24 | 2 | 4.1349 ± 0.0039 | 4.1398 ± 0.0019 | 4.1411 ± 0.0041 | 4.1415 ± 0.0041 | 4.1473 ± 0.0044 |

The displayed pooled plug-in SE uses the same delete-batch calculation as its corrected counterpart. Further split sizes and smoothing weights are preserved in the JSON files. The tangent has 8,192 held-out outside configurations per row.

Window correlation differences can be negative in finite samples. The table below exposes the raw plug-in, correction, independent tangent, and discarded negative mass. The tangent evaluates unclipped held-out masses; smoothing alpha=0.1 is shown throughout for this noisy correlation estimator, with the other fixed smoothing choices retained in each JSON. It is not chosen by taking the smallest held-out value. A positive correction or an SE is not a certificate of zero remaining bias.

| L | raw two-hit estimate | jackknife estimate | independent tangent upper target | negative p mass | negative q mass |
|---|---|---|---|---|---|
| 8 | 3.4143 ± 0.0120 | 3.4162 ± 0.0120 | 3.4475 ± 0.0195 | 0.00101 ± 0.00088 | 8.71e-05 ± 5.3e-05 |
| 12 | 3.7353 ± 0.0109 | 3.7368 ± 0.0109 | 3.7590 ± 0.0135 | 0.000319 ± 0.00013 | 0.000122 ± 5.3e-05 |
| 16 | 3.8922 ± 0.0106 | 3.8968 ± 0.0106 | 3.9131 ± 0.0185 | 0.00108 ± 0.00063 | 0.000127 ± 2.6e-05 |
| 24 | 4.1165 ± 0.0169 | 4.1151 ± 0.0169 | 4.1306 ± 0.0239 | 0.000588 ± 0.00022 | 0.000151 ± 2.5e-05 |

Negative masses are diagnostics in probability units, not estimates of genuine negative probabilities. Window split-sample results are saved at each available group size. The main runs have 2,097,152 independent resampling pairs in 32 batches; L=8 has 1,048,576 pairs in 32 batches.

The resampling product M=max_j W(R_j)V(R_j+1)/Inf_i² is dimensionless. The other columns show the fraction of i-in-sample mass left in the empty local-block pattern. These finite-board estimates check the mechanism; they are not certified constants valid at all L.

| L | M ± SE | q_empty/Inf, r=1 | q_empty/Inf, r=2 |
|---|---|---|---|
| 8 | 1.1666 ± 0.0064 | 0.2522 ± 0.0008 | 0.1338 ± 0.0003 |
| 12 | 1.1557 ± 0.0051 | 0.2488 ± 0.0011 | 0.1257 ± 0.0003 |
| 16 | 1.1576 ± 0.0080 | 0.2479 ± 0.0010 | 0.1232 ± 0.0004 |
| 24 | 1.1794 ± 0.0103 | 0.2461 ± 0.0016 | 0.1220 ± 0.0005 |

Sources: the saved window batches and `python3 finalise_windows.py` for M, and `python3 audit.py --no-windows` / block_table.json for empty-pattern mass. The SEs retain the shared-sample covariance.

## Why boundedness is the prediction

Garban, Pete and Schramm give polynomial arm estimates and quasi-multiplicativity in equations (2.1)–(2.4), the bulk pivotal comparison in (3.1), and the spectral hit-box bound in Lemma 3.2. Their Proposition 5.1 gives a positive local clustering probability under a box-hit condition and an arbitrary exterior-avoidance condition. It does not condition on the exact exterior spectral set. [The Fourier Spectrum of Critical Percolation](https://arxiv.org/html/0803.3750).

Here is the separate derivation. For δ=Inf_i and a(r)=α_4(1,r), two configurations sharing the outside of a ball and independently resampled inside must each have four inner arms if i is pivotal in both. They must also have shared outer arms. Independence of the two inner annuli and the outer annulus yields W(B_r minus i) ≤ Cδa(r). The spectral hit-box estimate yields V(B_r minus i) ≤ Cδ/a(r). Consecutive geometric radii therefore satisfy W(R_j)V(R_j+1) ≤ Cδ². At a terminal interior radius comparable to L, W ≤ Cδ², so the chain can jump to all other sites. The two-sequence entropy lemma gives nested ≤ Cδ. A separate direct summation over geometric shells gives the same conclusion. No numerical uniform constant is extracted from the Monte Carlo maxima.

For a fixed block B of b sites, the empty block pattern instead has q_0 ≥ 2^(-b)δ, because the conditional mean of the zero-one pivotal indicator is an integer multiple of 2^(-b). Its p_0 tends to one. That atom alone contributes at least 2^(-b)δ log2(1/δ) − O_B(δ). Thus every fixed finite block witness is Θ_B(log(1/δ)) after division by δ. These are different witnesses with different asymptotic behaviour. The complete argument, scope, and handling of terminal scales are in [ARGUMENT.md](ARGUMENT.md).

The finite-size prediction is saturation of the true bulk-coordinate and geometric nested ratios, not logarithmic divergence. The existing GPS conditional statement alone would not prove this; the resampling arm bound supplies the missing control. Arbitrary restrictions of crossings need not preserve this geometric setup, so the result does not supply the restriction-closed statement needed to prove general FEI.

## Is the creep the witness or the function?

The two-hit shell witness lowers the nested curve while retaining a similar finite-size rise, and exact small boards show a substantial gap between the tested nested and two-hit radial witnesses and E_i itself. Those data do not identify how much of the larger-board rise belongs to the function: E_i is not enumerated there. The arm argument rules out an unbounded log L rise for both the bulk-coordinate ratio and a suitable geometric nested witness. The fixed-block curve does eventually diverge, for a reason proved above. Thus the DNF interpretation—an unbounded one-hit witness hiding a bounded function—is not needed for the bulk percolation ball chain; a bounded witness can still creep on these sizes.

## Verification, resources, and handoff

`python3 study.py validate` checks pivotal masks against explicit flips, spectra against the supplied evaluator, the exact restriction mixture identity, derivative-window cells against the exact small-board spectrum, and both path optimisations against every L=2 order. `python3 ~/fei_solve_agent/code/mc_chain.py selftest` also passes; its log is [provided_selftest.log](provided_selftest.log).

The independent full L=5 audit compared 33,554,432 spectral weights and found maximum absolute difference 0.0. Every site influence also matched direct truth-table flips exactly. Replacing the entropy calculation with stable log1p changed any E_i/Inf_i by at most 1.64e-14. Those deterministic comparisons have sampling SE zero. All 50 site-wise witness inequalities pass. Results: [audit.json](audit.json), [audit_estimators.json](audit_estimators.json), [validation.json](validation.json). The tangent inequalities were also evaluated against exact small-board distributions, and the finite-block lower bound was checked in every saved outside batch.

The independent audit process peaked at 1.772 GiB resident, from resource.getrusage in audit.json. Other kernels were sized before allocation; the L=5 optimisation keeps 0.781 GiB of major arrays, calculated in resource_plan.json. The folder held 121,275,216 bytes at that audit. Jobs used inherited nice 10 and at most two simultaneous single-thread numerical processes. No shared files, mesh, trading services, Git repositories, or external publishing were modified. The supplied evaluator is frozen locally as mc_chain_reference.py.

The brain recall helped locate relevant prior work and the GPS box estimate. Its provisional global-entropy claim was not assumed. The math store was unavailable. [SOURCES.md](SOURCES.md) records the exact recall commands and primary references. The mathematical handoff remains local, as the fleet rules require.

Still open: independent referee review of the bulk-coordinate argument; a useful numerical uniform constant; the large-board exact erasure ratios and the exact values of the fully vertex-resolved last-two statistic. The larger-board window computed here is explicitly its shell coarsening. These limitations do not affect the exact small-board optima, the block bias checks, or the supplied boundedness derivation.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 2026, 22:20 ask; FEIB22 percolation brief.
