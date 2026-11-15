#!/usr/bin/env python3
"""Insert the complete experiment tables into REPORT.md once counts are complete."""
import csv
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    d=json.loads((ROOT/'data/analysis.json').read_text())
    expected={100:400,300:400,1000:300,3000:200,10000:120}
    assert {r['n']:r['samples'] for r in d['main']}==expected
    lines=[
        'The complete main run contains **1,420 point sets**, including 120 at n=10000. Variances use the unbiased sample variance. Standard errors and percentile intervals below come from 5,000 nonparametric bootstrap resamples of instances; they concern the heuristic distribution only.',
        '',
        '| n | samples | mean U/sqrt(n) | sample Var(U) | bootstrap SE | bootstrap 95% interval |',
        '|---:|---:|---:|---:|---:|---:|']
    for r in d['main']:
        lo,hi=r['bootstrap_95_percentile']
        lines.append(f"| {r['n']} | {r['samples']} | {r['mean_div_sqrt_n']:.6f} | {r['variance']:.6f} | {r['bootstrap_se']:.6f} | [{lo:.6f}, {hi:.6f}] |")
    fit=d['descriptive_constant_fit'];slope=d['descriptive_log10_slope']
    lines += ['',
        f"A descriptive constant fit over these five sizes is {fit['constant']:.5f} with sampling SE {fit['se']:.5f}; chi-square {fit['chi_square']:.2f} on {fit['df']} degrees of freedom (approximate p={fit['p']:.2f}). The slope against log10(n) is {slope['slope']:.5f} with SE {slope['se']:.5f}. Thus the finite-size heuristic data are compatible with a roughly constant variance; they do not identify an asymptotic limit. The normalized mean rises with n, so a size-dependent solver bias remains a practical concern.",
        '',
        'The 20-epoch variance checkpoints were '+', '.join(f"{r['variance20_epochs']:.5f}" for r in d['main'])+' in the same size order. Their difference from the 80-epoch values shows that search effort can affect the measured variance.',
        '',
        'Matched calibration compares the 80-epoch result with the better of that result and the 320-epoch result. The two columns of variances below use only the smaller matched subsets, not all main samples. Intervals use 10,000 paired bootstrap resamples.',
        '',
        '| n | pairs | mean length improvement | SD of improvement | Var at 80 | Var after stronger search | 95% interval for variance change |',
        '|---:|---:|---:|---:|---:|---:|---:|']
    for r in d['calibration']:
        lo,hi=r['paired_variance_change_bootstrap_95']
        lines.append(f"| {r['n']} | {r['samples']} | {r['mean_improvement']:.5f} | {r['improvement_sd']:.5f} | {r['variance_baseline80']:.5f} | {r['variance_combined320']:.5f} | [{lo:.5f}, {hi:.5f}] |")
    lines += ['',
        "At n=10000 the stronger search still improves lengths by about 0.355 on average (roughly 0.49%). Its mean improvement is several times the point-to-point SD of that improvement. The calibration cannot rule out variance changes of several thousandths. The observed improvement is a lower bound on the baseline's optimization error; the error remaining after the stronger search is unknown.",
        '',
        'For the three dual-bound instances at each size, these are the worst relative-gap upper bounds U/lower_bound-1. They bound individual length error, not variance bias:',
        '',
        '| n | worst bound at 80 epochs | worst bound after stronger search |',
        '|---:|---:|---:|']
    for r in d['calibration']:
        bounds=r['lower_bound_checks']
        lines.append(f"| {r['n']} | {100*max(b['baseline_gap_bound'] for b in bounds):.2f}% | {100*max(b['relative_gap_bound'] for b in bounds):.2f}% |")
    lines += ['',
        'The observed n=10000 variance, about 0.0346, is evidence for order-one fluctuations of these near-optimal torus tours. It is not a numerical determination of the square conjecture or of the exact torus variance limit.',
        '',
        'Machine-readable results: `data/analysis.json`, `data/variance_summary.csv`, `data/analysis_complete.txt`. Original numerical plot: [variance trend](data/variance_trend.svg). Bootstrap seeds are fixed in `code/analyze.py`. Every main variance was re-derived independently with Python statistics.variance; paired variance differences were checked using their covariance identity.'
    ]
    report=ROOT/'REPORT.md'
    text=report.read_text()
    placeholder='The numerical results table and complete-run uncertainty estimates will be inserted after the saved main run finishes.'
    assert placeholder in text
    text=text.replace(placeholder,'\n'.join(lines))
    resource_text='''## Reproduction, resources and remaining gap

The session launcher and direct getpriority checks give nice 10. Both numerical jobs used one thread each; BLAS, OpenMP and Accelerate thread counts were fixed to one. The main Python peak RSS was 136,855,552 bytes and its solver peak was 5,636,096 bytes. The largest additional array was the 400,000,000-byte complete lower-bound matrix. The design stays well below the 4 GB budget. The main run took 967 seconds of wall time, with 874 seconds summed solver time; calibration ran as a second single-threaded job. There were no search-cap hits and no final feasibility or length-recomputation failures. No subagents, publication, git pushes or external messages were used.

From this directory, in a shell running at nice 10:

```sh
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
export MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1
clang++ -O3 -std=c++17 -Wall -Wextra code/torus_tsp.cpp -o code/torus_tsp
clang++ -O3 -std=c++17 -Wall -Wextra code/held_karp_bound.cpp -o code/held_karp_bound
python3 code/validate.py
python3 code/experiment.py
python3 code/calibrate.py
python3 code/analyze.py
```

The experiment resumes existing main rows; use a different --output name for a fresh sample file. Calibration overwrites its deterministic comparison file. `code/validate_edges.py` reproduces the additional small-instance audit after compiling the sanitizer binary with the command in `LOG.md`. NumPy, SciPy, a C++17 compiler and pdftotext were already installed; no solver package or dependency installation was needed. Source downloads are reproducible with `code/acquire_source.py URL name`; only text is retained.

To turn the conditional route into a solution, one still needs to prove the locality estimate (L) for the true global optimizer and the appropriate fixed-count transfer, or replace them with a direct binomial variance argument. None of the computations supplies those missing estimates.

'''
    text=text.replace('The source collection contains only plain text.',resource_text+'The source collection contains only plain text.')
    report.write_text(text)
    print('Inserted complete results and reproduction details into REPORT.md')

if __name__=='__main__':main()
