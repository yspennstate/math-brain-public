"""Assemble the report only after every requested computation is complete."""
import study as s
import hashlib
import json
from pathlib import Path
import platform
import os
from datetime import datetime

read=lambda p:json.loads(Path(p).read_text())
small=read('small_centre_table.json');audit=read('audit.json');ea=read('audit_estimators.json')
plan=read('resource_plan.json')
assert audit['passed'] and ea['passed'] and read('validation.json')['passed'] and read('optimal_L5.json')['complete']
win={L:read(f'window_L{L}_original_s{L*1000+7}.json') for L in (8,12,16,24)}
for L,a in win.items():assert a['batches']==32 and a['N']==(1048576 if L==8 else 2097152) and 'M' in a
block={(L,r):read(f'block_L{L}_r{r}_s{L*1000+r}.json') for L in (8,12,16,24) for r in (1,2)}
fmt=lambda v,e,d=4:f'{v:.{d}f} ± {e:.{d}f}'
rows=[]
for a in small:
    rows.append(f'| {a["L"]} | {fmt(a["influence"],0,7)} | {fmt(a["nested"],0)} | {fmt(a["two"],0)} | {fmt(a["block"]["1"]["ratio"],0)} | {fmt(a["block"]["2"]["ratio"],0)} | {fmt(a["erasure_ratio"],0)} |')
for L,a in win.items():
    b1,b2=block[L,1]['tangent'][0],block[L,2]['tangent'][0]
    rows.append(f'| {L} | {fmt(a["influence"],a["influence_se"],7)} | {fmt(a["nested"],a["nested_se"])} | {fmt(a["two_jackknife"],a["two_se"])} | {fmt(b1["ratio"],b1["se"])} | {fmt(b2["ratio"],b2["se"])} | not enumerated |')

text='''# FEIB22 report

For a bulk site of a critical Hex crossing, I derive a board-size-independent bound on E_i/Inf_i. A geometric nested ball witness already suffices. The argument uses standard four-arm estimates and is supplied in [ARGUMENT.md](ARGUMENT.md); it is a derivation made here and awaits referee review. It does not solve general FEI.

The experiment also shows a finite witness gap. Keeping two spectral hits improves the nested estimate, but does not flatten its finite-size rise on the boards tested. A fixed local block behaves differently: I prove that every fixed finite block witness eventually grows logarithmically, even though the bulk-coordinate ratio and a suitable nested ball witness remain bounded.

## Centre-coordinate table

Entropies are in bits; ratios are bits per unit influence. Every ± is one sampling standard error. Exact entries have SE zero; floating-point error is checked below. The centre is the same zero-based site (L//2,L//2) used by mc_chain.py.

The nested column uses the original mc_chain.py cardinality-prefix ball chain. The two-hit column records the shells of its first two distinct spectral points, including same-shell ties. It is a coarsening of the vertex-resolved last-two witness and therefore also bounds that witness from above. On large boards it is a jackknife-corrected estimate, with remaining finite-sample bias audited below. The block columns on large boards estimate an independent tangent upper target, rather than an unchecked plug-in. Their numerical estimates still have sampling uncertainty. Small-board blocks are exact and are truncated by the board boundary.

| L | Inf_i | nested/Inf | two-hit shells/Inf | block r=1/Inf | block r=2/Inf | exact E_i/Inf |
|---|---|---|---|---|---|---|
'''+ '\n'.join(rows)+'\n\n'
text+='''Sources and commands: exact entries come from `python3 study.py exact 3`, `exact 4`, `exact 5 noopt`, and `python3 audit.py --no-windows`, consolidated in [small_centre_table.json](small_centre_table.json). Larger window entries come from `python3 run_suite.py windows`, plus `python3 study.py window 8 32 32768 8007 original`; final summaries are regenerated from the saved counts by `python3 finalise_windows.py`. Block entries come from `python3 run_suite.py blocks`, with fixed smoothing alpha=0.001, and their corresponding block_L*_r*_s*.json files. The input and estimator definitions are in [METHODS.md](METHODS.md).

## Exact optima at every site

All site influences, erasure ratios, and globally optimal nested and vertex-resolved last-two witnesses on L=3,4,5 are in [exact_all_sites.csv](exact_all_sites.csv). Both optimisations range over all coordinate orders using subset shortest paths. Returned orders are independently regrouped against the full spectrum. L=5 symmetries are checked entrywise before they are used.

| L | centre exact E/Inf | best nested/Inf | best vertex last-two/Inf | sampling SE |
|---|---|---|---|---|
'''
for L in (3,4,5):
    a=read(f'exact_L{L}.json')['rows'][(L//2)*L+L//2]
    if L==5:
        o=next(r for r in read('optimal_L5.json')['rows'] if r['i']==12)
    else:o=a
    text+=f'| {L} | {a["erasure_ratio"]:.8f} | {o["best_nested"]:.8f} | {o["best_two"]:.8f} | 0 |\n'
text+='\nCommands: `python3 study.py exact 3`, `python3 study.py exact 4`, `python3 study.py exact 5 noopt`, `python3 optimal5.py`. The per-site and order files are exact_L3.json, exact_L4.json, exact_L5.json, and optimal_L5.json.\n\n'

text+='''## Bias checks and independent upper targets

Every final block run uses 16 independent batches of 1,024 outside configurations. The first half chooses a positive pilot tangent and the second half estimates its expectation. Concavity gives a true entropy upper functional for every fixed pilot; quoted SEs are conditional on that pilot and include numerator/denominator covariance. The smaller-sample plug-ins are reported as estimates, not upper bounds.

| L | radius | plug-in at N=1,024 | plug-in at N=4,096 | pooled N=16,384 | jackknife at N=16,384 | tangent upper target |
|---|---|---|---|---|---|---|
'''
for L in (8,12,16,24):
    for r in (1,2):
        a=block[L,r];sp={b['N']:b for b in a['split']};b1=sp[1024];b4=sp[4096];tan=a['tangent'][0]
        # Pooled raw estimate and corrected estimate share the delete-batch SE.
        text+=f'| {L} | {r} | {fmt(b1["plugin"],b1["plugin_se"])} | {fmt(b4["plugin"],b4["plugin_se"])} | {fmt(a["plugin"],a["plugin_jackknife_se"])} | {fmt(a["plugin_jackknife"],a["plugin_jackknife_se"])} | {fmt(tan["ratio"],tan["se"])} |\n'
text+='\nThe displayed pooled plug-in SE uses the same delete-batch calculation as its corrected counterpart. Further split sizes and smoothing weights are preserved in the JSON files. The tangent has 8,192 held-out outside configurations per row.\n\n'
text+='''Window correlation differences can be negative in finite samples. The table below exposes the raw plug-in, correction, independent tangent, and discarded negative mass. The tangent evaluates unclipped held-out masses; smoothing alpha=0.1 is shown throughout for this noisy correlation estimator, with the other fixed smoothing choices retained in each JSON. It is not chosen by taking the smallest held-out value. A positive correction or an SE is not a certificate of zero remaining bias.

| L | raw two-hit estimate | jackknife estimate | independent tangent upper target | negative p mass | negative q mass |
|---|---|---|---|---|---|
'''
for L,a in win.items():
    tan=a['tangent'][2]
    text+=f'| {L} | {fmt(a["two"],a["two_se"])} | {fmt(a["two_jackknife"],a["two_se"])} | {fmt(tan["ratio"],tan["se"])} | {a["negative_p_mass"]:.3g} ± {a["negative_p_mass_se"]:.2g} | {a["negative_q_mass"]:.3g} ± {a["negative_q_mass_se"]:.2g} |\n'
text+='\nNegative masses are diagnostics in probability units, not estimates of genuine negative probabilities. Window split-sample results are saved at each available group size. The main runs have 2,097,152 independent resampling pairs in 32 batches; L=8 has 1,048,576 pairs in 32 batches.\n\n'

text+='''The resampling product M=max_j W(R_j)V(R_j+1)/Inf_i² is dimensionless. The other columns show the fraction of i-in-sample mass left in the empty local-block pattern. These finite-board estimates check the mechanism; they are not certified constants valid at all L.

| L | M ± SE | q_empty/Inf, r=1 | q_empty/Inf, r=2 |
|---|---|---|---|
'''
for L,a in win.items():
    b1,b2=block[L,1],block[L,2]
    text+=f'| {L} | {fmt(a["M"],a["M_se"])} | {fmt(b1["q_empty_over_delta"],b1["q_empty_over_delta_se"])} | {fmt(b2["q_empty_over_delta"],b2["q_empty_over_delta_se"])} |\n'
text+='\nSources: the saved window batches and `python3 finalise_windows.py` for M, and `python3 audit.py --no-windows` / block_table.json for empty-pattern mass. The SEs retain the shared-sample covariance.\n\n'
text+='''## Why boundedness is the prediction

Garban, Pete and Schramm give polynomial arm estimates and quasi-multiplicativity in equations (2.1)–(2.4), the bulk pivotal comparison in (3.1), and the spectral hit-box bound in Lemma 3.2. Their Proposition 5.1 gives a positive local clustering probability under a box-hit condition and an arbitrary exterior-avoidance condition. It does not condition on the exact exterior spectral set. [The Fourier Spectrum of Critical Percolation](https://arxiv.org/html/0803.3750).

Here is the separate derivation. For δ=Inf_i and a(r)=α_4(1,r), two configurations sharing the outside of a ball and independently resampled inside must each have four inner arms if i is pivotal in both. They must also have shared outer arms. Independence of the two inner annuli and the outer annulus yields W(B_r minus i) ≤ Cδa(r). The spectral hit-box estimate yields V(B_r minus i) ≤ Cδ/a(r). Consecutive geometric radii therefore satisfy W(R_j)V(R_j+1) ≤ Cδ². At a terminal interior radius comparable to L, W ≤ Cδ², so the chain can jump to all other sites. The two-sequence entropy lemma gives nested ≤ Cδ. A separate direct summation over geometric shells gives the same conclusion. No numerical uniform constant is extracted from the Monte Carlo maxima.

For a fixed block B of b sites, the empty block pattern instead has q_0 ≥ 2^(-b)δ, because the conditional mean of the zero-one pivotal indicator is an integer multiple of 2^(-b). Its p_0 tends to one. That atom alone contributes at least 2^(-b)δ log2(1/δ) − O_B(δ). Thus every fixed finite block witness is Θ_B(log(1/δ)) after division by δ. These are different witnesses with different asymptotic behaviour. The complete argument, scope, and handling of terminal scales are in [ARGUMENT.md](ARGUMENT.md).

The finite-size prediction is saturation of the true bulk-coordinate and geometric nested ratios, not logarithmic divergence. The existing GPS conditional statement alone would not prove this; the resampling arm bound supplies the missing control. Arbitrary restrictions of crossings need not preserve this geometric setup, so the result does not supply the restriction-closed statement needed to prove general FEI.

## Is the creep the witness or the function?

The two-hit shell witness lowers the nested curve while retaining a similar finite-size rise, and exact small boards show a substantial gap between the tested nested and two-hit radial witnesses and E_i itself. Those data do not identify how much of the larger-board rise belongs to the function: E_i is not enumerated there. The arm argument rules out an unbounded log L rise for both the bulk-coordinate ratio and a suitable geometric nested witness. The fixed-block curve does eventually diverge, for a reason proved above. Thus the DNF interpretation—an unbounded one-hit witness hiding a bounded function—is not needed for the bulk percolation ball chain; a bounded witness can still creep on these sizes.

## Verification, resources, and handoff

`python3 study.py validate` checks pivotal masks against explicit flips, spectra against the supplied evaluator, the exact restriction mixture identity, derivative-window cells against the exact small-board spectrum, and both path optimisations against every L=2 order. `python3 ~/fei_solve_agent/code/mc_chain.py selftest` also passes; its log is [provided_selftest.log](provided_selftest.log).

'''
checks=audit['checks'];sp=next(r for r in checks if r['check']=='independent_full_L5_spectrum');fl=next(r for r in checks if r['check']=='all_L5_erasure_ratios_stable_log1p')
text+=f'The independent full L=5 audit compared {sp["entries"]:,} spectral weights and found maximum absolute difference {sp["maximum_absolute_error"]:.1f}. Every site influence also matched direct truth-table flips exactly. Replacing the entropy calculation with stable log1p changed any E_i/Inf_i by at most {fl["maximum_absolute_error"]:.3g}. Those deterministic comparisons have sampling SE zero. All 50 site-wise witness inequalities pass. Results: [audit.json](audit.json), [audit_estimators.json](audit_estimators.json), [validation.json](validation.json). The tangent inequalities were also evaluated against exact small-board distributions, and the finite-block lower bound was checked in every saved outside batch.\n\n'
text+=f'The independent audit process peaked at {audit["peak_rss_bytes"]/1024**3:.3f} GiB resident, from resource.getrusage in audit.json. Other kernels were sized before allocation; the L=5 optimisation keeps {plan["optimal_L5_major_arrays_bytes"]/1024**3:.3f} GiB of major arrays, calculated in resource_plan.json. The folder held {next(r for r in checks if r["check"]=="folder_size_bytes")["value"]:,} bytes at that audit. Jobs used inherited nice 10 and at most two simultaneous single-thread numerical processes. No shared files, mesh, trading services, Git repositories, or external publishing were modified. The supplied evaluator is frozen locally as mc_chain_reference.py.\n\n'
text+='''The brain recall helped locate relevant prior work and the GPS box estimate. Its provisional global-entropy claim was not assumed. The math store was unavailable. [SOURCES.md](SOURCES.md) records the exact recall commands and primary references. The mathematical handoff remains local, as the fleet rules require.

Still open: independent referee review of the bulk-coordinate argument; a useful numerical uniform constant; the large-board exact erasure ratios and the exact values of the fully vertex-resolved last-two statistic. The larger-board window computed here is explicitly its shell coarsening. These limitations do not affect the exact small-board optima, the block bias checks, or the supplied boundedness derivation.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 2026, 22:20 ask; FEIB22 percolation brief.
'''
Path('REPORT.md').write_text(text)
prov=dict(created=datetime.now().astimezone().isoformat(),python=platform.python_version(),numpy=s.np.__version__,platform=platform.platform(),nice=os.getpriority(os.PRIO_PROCESS,0),hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('.').iterdir() if p.suffix in ('.py','.cpp','.dylib')})
s.save('provenance.json',prov)
print('REPORT READY')
