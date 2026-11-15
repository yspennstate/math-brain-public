import json,math,re,datetime
from pathlib import Path
small=[json.loads(Path(f'census_{n:02d}.json').read_text()) for n in range(1,25)]
dense=[json.loads(x) for x in Path('thresholds_dense.jsonl').read_text().splitlines()]
pdense=[json.loads(x) for x in Path('parity_dense.jsonl').read_text().splitlines()]
assert [r['n'] for r in dense]==list(range(1,2001))
assert [r['n'] for r in pdense]==list(range(2,2001))
for n in range(1,25):assert json.loads(Path(f'census_cert_{n:02d}.json').read_text())['B_le_2.18I_integer_certificate']
resources=json.loads(Path('parity_dense.metrics.json').read_text());assert resources['exit_code']==0
assert resources['max_rss_bytes']<3*2**30
for name in ['dense_audit.log','parity_dense_audit.log','parity_v3_audit.log','balanced_audit.log','final_audit.log','quantlog_check.log']:
 assert Path(name).exists() and Path(name).stat().st_size
assert json.loads(Path('B_final_constant_certificate.json').read_text())['passes']
assert json.loads(Path('gamma_8_over_5_certificate.json').read_text())['all_rational_checks_pass']
assert Path('functional_ratios.png').exists()
assert len(json.loads(Path('suprema_certified.json').read_text()))==188
assert Path('suprema_certificate_verification.log').exists()
n24=small[-1]['maxima'];th=dense[-1]['maxima'];par=pdense[-1]['maxima']
hill=json.loads(Path('hill_2000.json').read_text());g=json.loads(Path('refinement_high_precision.json').read_text())
bal=json.loads(Path('balanced_hill_v2_1999.json').read_text())['searches']
summary={'finished_local':datetime.datetime.now().astimezone().isoformat(),'census_sign_representatives':sum(r['representatives'] for r in small),'census_value_vectors':sum(2*r['representatives'] for r in small),'census_nonconstant_representatives':sum(r['nonconstant'] for r in small),'ordinary_threshold_vectors':sum(r['n'] for r in dense),'parity_threshold_vectors':sum(r['n'] for r in pdense),'B_uniform_upper':'3.459354','Gamma_uniform_upper':'1.6','n24_maxima':n24,'n2000_threshold_maxima':th,'n2000_parity_threshold_maxima':par,'n2000_hill_B_over_I':hill['searches'][0]['final']['B/I'],'n2000_refined_Gamma_over_I':g['metrics']['Gamma/I'],'balanced_1999_witnesses':[{k:v for k,v in r.items() if k!='value_vector'} for r in bal],'parity_dense_process_resources':resources,'folder_file_bytes_before_final_report':sum(p.stat().st_size for p in Path('.').rglob('*') if p.is_file())}
assert summary['folder_file_bytes_before_final_report']<10**9
Path('run_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
report=f'''# FEIB02 report

The closed forms, exhaustive census and both dense structured-family sweeps are complete. The new direct bounds for every symmetric Boolean function are

    B <= 3.459354 I,
    Gamma <= (8/5) I.

The proof uses no FEI upper bound. Above dimension 24 it is analytic; below it an integer-only certificate verifies B<=2.18I on every representative, which is more than enough for both conclusions. PROOFS.md contains the full argument, including the derivative-envelope lemmas and rational constant certificates. PROOF_REVIEW.md is a short reading guide.

These bounds do not improve the supplied symmetric FEI constant 4.650431 through Theorem 1. Three-variable AND has B/I=15/4-(3/2)log_2 3=1.3725562489182657..., above the required 1.3252155. witness_check.log checks it by the census, exact finite differences, a direct truth-table transform and the closed expression. Majority gives the stronger asymptotic obstruction B/I->2/ln 2. This limits that sufficient estimate; it is not a lower bound of 7.77 for the FEI constant.

## What was computed

Every symmetric value vector in dimensions 1 through 24 was covered: {summary['census_value_vectors']:,} vectors, represented by {summary['census_sign_representatives']:,} global-sign representatives. The nonconstant representative count is {summary['census_nonconstant_representatives']:,}. These counts come from census_01.json through census_24.json and are collected in census_counts.csv and run_summary.json. Constants and balanced I=1 cases have undefined ratios and are handled separately.

RESULTS.md gives the per-dimension A/I, B/I, Gamma/I and balanced ratios over I-1. extrema.csv supplies all extremal value vectors, including P and all high-precision ties up to global sign. The dimension-24 maxima are A/I={n24['A/I']['value']:.12f}, B/I={n24['B/I']['value']:.12f}, Gamma/I={n24['Gamma/I']['value']:.12f} and P/I={n24['P/I']['value']:.12f} (census_24.json and suprema_certified.json).

All {summary['ordinary_threshold_vectors']:,} nonconstant thresholds in every dimension 1 through 2000 were evaluated. All {summary['parity_threshold_vectors']:,} parity-times-threshold vectors in dimensions 2 through 2000 were also covered; at dimension 1 these products are constant. Reflection and global-sign invariance cover the omitted equivalent vectors. thresholds_dense.jsonl, parity_dense.jsonl, majority.csv and parity_family.csv contain the dimension tables. The parity convention is f_t=(-1)^t times a threshold. Ordinary parity itself has I=n and A=B=Gamma=P=0 exactly.

At n=2000 the threshold-family maxima are B/I={th['B/I']['value']:.12f} and Gamma/I={th['Gamma/I']['value']:.12f}. The parity-family maxima are B/I={par['B/I']['value']:.12f} and Gamma/I={par['Gamma/I']['value']:.12f}. The separate convolution outputs retain log2 ratios for tiny positive values that underflow ordinary floating point.

Bounded value-vector searches on the saved dimension grid through 2000 give B/I={summary['n2000_hill_B_over_I']:.12f} and Gamma/I={float(summary['n2000_refined_Gamma_over_I']):.12f} at n=2000 (hill_2000.json, gamma_refinement_2000.json and refinement_high_precision.json). These are lower bounds from finite searches, not certified optima. A separate A search retained corner AND/OR and gives A/I=2.998 at n=2000, consistent with its exact formula. Balanced paired-coordinate searches use the objective over I-1 directly; at n=1999 they give B/(I-1)=2.744446594676 and Gamma/(I-1)=1.360500539114 (balanced_hill_v2_1999.json and balanced_high_precision.json).

All logs are base 2. Functionals are in bits, I is total influence, and the ratios are bits per unit influence. functional_ratios.png and functional_ratios.pdf plot the census, dense threshold maxima, search witnesses and proved bounds.

## Why the digits are reliable

The finite census computes every derivative triangle, Fourier coefficient, absolute sum, support count and squared sum as exact integers. Only the final logarithms use floating point. An independent integer-interval census retains every possible maximizer. Exact rational logarithm expressions prove all remaining ties, and a positive-series calculation certifies all 188 defined suprema to 100 decimal places. suprema_certified.json stores the values, outward bounds and all extremal vectors; suprema_certificate_verification.log records the independent certificate replay. The original floating-point discovery agrees, with a smallest excluded-candidate gap of 5.52931572972426e-7 (candidates_audit.log). The finite proof bound is stronger evidence of a different kind: quantlog.h encloses every logarithm by exact rational inequalities, and unsigned 128-bit arithmetic checks the finite proof bound on every representative. The tighter census_interval.c scan additionally certifies the actual suprema; its log enclosures are independent of libm. generate_quantlog.py verifies all table entries without transcendental calls.

The large sweeps use exact GMP recurrences. Thresholds were independently calculated in Python by a different traversal; parity thresholds were independently calculated by exact integer polynomial convolution. dense_audit.log and parity_dense_audit.log compare the implementations. audit.log and candidates_audit.log include direct truth-table restriction checks, exact Parseval/influence/up-transform identities and independent balanced counts. large_audit.log, balanced_audit.log, parity_v3_audit.log, gamma_audit.log and final_audit.log record high-precision checks, random attempts to break the lemmas, and direct numerical checks of the Bessel integrals.

Rare spectra require care even with arbitrary precision. symmetric.py takes log1p of exact integer differences instead of subtracting nearly equal logs. stable_log_check.log verifies both AND_2000 and parity times AND_2000 at 80 and 720 decimal digits. Positive values below binary64 range are stored in logarithmic form rather than silently reported as zero. The reported precision errors are measured in the audit logs; no extrapolation from a low-precision cancellation is used.

## Mathematical conclusions and what remains open

The optimal uniform constants satisfy

    3 <= c_A <= 3.3252155,
    2/ln 2 <= c_B <= 3.459354,
    1/ln 2 <= c_Gamma <= 8/5.

The A upper bound additionally uses the supplied H<=4.650431I theorem and Theorem 1; it is not a new direct proof for A. The lower limits follow from AND/OR and majority, with a proof and exact finite majority-law checks in PROOFS.md and majority_law_check.json.

For B the computed extremizers are mostly biased tails with small additional sign runs; they need not be monotone. For Gamma they are oscillatory across the binomial bulk, with several sign runs on a scale comparable to sqrt(n). RESULTS.md gives a paragraph and explicit witnesses for each. The exact all-dimension extremizers and the sharp constants remain open. No search beyond dimension 24 is called exhaustive over all symmetric functions.

## Files and resources

The principal deliverables are PROOFS.md, RESULTS.md, extrema.csv, the two dense JSONL tables, majority.csv, parity_family.csv, balanced_large.csv, and this report. Scripts and verification logs remain beside them. run_summary.json collects the load-bearing counts and large-dimensional values with their source data.

The dense computations ran as single-threaded C processes with GMP. The parity run records inherited nice {resources['inherited_nice']}; its measured maximum resident set was {resources['max_rss_bytes']:,} bytes ({resources['max_rss_bytes']/2**30:.3f} GiB), below the 3 GiB limit (parity_dense.metrics.json). Its matrix allocation was sized before allocation. The worker's saved file size was {summary['folder_file_bytes_before_final_report']:,} bytes at final audit, below the 1 GB cap (run_summary.json).

Brain recall helped: it supplied the earlier symmetric derivative-envelope method and the distinction between within-level entropy and the up-ratio B. The final new learnings are saved locally in LEARNINGS.md for the parent session. Deliverable writes stayed in this worker folder; there was no publishing, git push, mesh post, production-system action or shared-memory edit.

Task: “Do the brief fully and carefully” — FEIB02, started 10 Nov 2026 at 01:09 +04.
'''
Path('REPORT.md').write_text(report)
Path('STATUS.md').write_text('# FEIB02 status\nCompleted the brief. Exact formulas, rigorous direct B/Gamma bounds, exhaustive n<=24 census, both dense family sweeps through n=2000, bounded A/B/Gamma and balanced searches, high-precision and integer-only checks, tables and figures are saved. See REPORT.md.\nNEXT: none for this run. Sharp constants and all-dimension extremizer classifications remain open mathematics; the parent may review/publish the saved results.\n')
print('Wrote final REPORT.md, STATUS.md and run_summary.json.')
