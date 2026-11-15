#!/usr/bin/env python3
"""Insert completed numerical results; retain the mathematical proof and source audit."""
import csv,json,datetime,os
from pathlib import Path
assert os.getpriority(os.PRIO_PROCESS,0)>=10
with Path('data/samples.csv').open() as f:raw=list(csv.DictReader(f))
assert len(raw)==7680
with Path('data/summary.csv').open() as f:summary=list(csv.DictReader(f))
assert len(summary)==21
trends=json.loads(Path('data/trends.json').read_text())
d1=json.loads(Path('data/d1_summary.json').read_text())
peak=max(int(r['max_rss_bytes']) for r in raw)
text='''The main experiment contains 7,680 independent configurations: d=2,3,4; n=32,64,128,256,512,1024,2048; respectively 500,500,400,400,320,240,200 samples per dimension. The sample plan was fixed before the run. Each sample uses a complete-graph **Blossom V** solve for the non-bipartite perfect matching. No geometric edge truncation or bipartite solver was substituted.

The implementation is Vladimir Kolmogorov's Blossom V 2.05, described in *Mathematical Programming Computation* 1 (2009), 43–67, [author's source distribution](https://pub.ista.ac.at/~vnk/software.html). The research-only source, licence, archive checksum and local modifications are in code/vendor/. The private wrapper uses 64-bit integral costs round(10^12 times distance). Every instance passes the integral dual-feasibility and complementary-slackness checker at zero tolerance, over all edges of the complete graph. The reported cost is the selected matching's ordinary Euclidean length.

**Numerical exactness:** this is an exact optimizer of the discretized weights, not a symbolic exact comparison of sums of square roots. With S=10^12 and n/2 edges, rounding contributes at most n/(4S) to the cost of any matching, so the selected real cost exceeds the true optimum by at most n/(2S), plus floating-point distance-evaluation error. At n=2048 the explicit quantization part is 1.024e-9. This error is negligible relative to the observed fluctuations.

Checks before sampling: 120 exhaustive enumerations for n<=12 in dimensions 1–4; 36 independent NetworkX integer-weight comparisons for n=16,32,64; 15 comparisons to consecutive pairing in d=1 through n=2048; and 12 duplicate-pair tests. All passed. The largest difference in ordinary lengths between independently obtained matchings in those NetworkX checks was 1.78e-15. The final audit additionally regenerates one configuration and re-solves one sample in each of the 21 groups, verifies its point hash and partners, and independently re-sums its edge lengths.

The run used one numerical thread and nice 10 throughout. Peak recorded resident memory was PEAK_MIB MiB (PEAK_GB GB). The sample count, priority, integer-certificate status and memory are recorded in data/samples.csv. The source inventory contains only plain text; the final filesystem audit checks that no PDFs or raster images were retained.

The following are unbiased sample variances (denominator samples minus one). Intervals are approximate 95% percentile nonparametric bootstrap intervals from 4,000 resamples within each (d,n) group. They describe Monte Carlo uncertainty at fixed n, not asymptotic validity of a proposed scaling law.

TABLE

For n>=256, exploratory regressions of log sample variance on log n give:

| d | fitted slope | 95% bootstrap interval | target exponent 1-2/d |
|---:|---:|---:|---:|
SLOPES

The planar variance falls overall from 0.0342 at n=32 to 0.0195 at n=2048, with a small rise between the last two sizes. The variances in dimensions 3 and 4 grow overall, while the target-normalized variances also retain finite-size drift. These observations neither establish nor refute a positive asymptotic variance constant. In particular, a finite-range fitted exponent is not a theorem about liminf or anti-concentration. Fits over the full n>=32 range are also retained in data/trends.json.

A separate d=1 calibration used 10,000 sorted-sample exact pairings at each of n=32,128,512,2048. The empirical/exact variance ratios were D1RATIOS, respectively; see data/d1_summary.json. These additional 40,000 observations are not counted among the 7,680 Blossom experiments.

The written proof was checked independently at its main identities: duplicate deletion by an edge exchange; the projection inequalities by orthogonality and covariance; the boundary identity both by integration by parts and differentiation of the scaled-cube integral; and the d=1 variance both from beta moments and Dirichlet spacing covariances. For n=2,d=1, exact polynomial integration gives Var(g(X))=1/180 and integral h^2=2/45, so 2 Var(g(X))+integral h^2=1/18. The rational audit checks the corresponding one-dimensional mean, increment and variance identities for every even n from 2 to 200. These finite checks support the analytic arguments; they are not proofs of a higher-dimensional asymptotic claim.

Raw observations, per-group summaries, bootstrap trends, run metadata, saved example point sets, verification results, and the plot data/variance.svg are in data/. Reproduction commands are in code/README.txt. The final audit is data/final_audit.json and the artifact checksums are data/manifest.json.

The uniform all-large-even-n lower bound c_d n^(1-2/d) in d>=2, and the target-scale anti-concentration conclusion, remain unproved here. The label PARTIAL refers to the proved weaker bounds and subsequence result, not to a full solution or a confirmed literature resolution.

Task: “Open problem E0031.” Request/run start: 13 November 2026, 13:15 Asia/Tbilisi (+04), as recorded in the original run log.
'''
text=text.replace('PEAK_MIB',f'{peak/1024**2:.1f}').replace('PEAK_GB',f'{peak/1e9:.3f}')
text=text.replace('TABLE',Path('data/numerical_table.md').read_text().strip())
slope_lines=[]
for r in trends['slopes']:
 if r['min_n']==256:
  slope_lines.append(f"| {r['d']} | {r['loglog_slope']:.3f} | [{r['bootstrap_ci_low']:.3f}, {r['bootstrap_ci_high']:.3f}] | {r['target_exponent']:.3f} |")
text=text.replace('SLOPES','\n'.join(slope_lines))
text=text.replace('D1RATIOS',', '.join(f"{r['variance_ratio']:.3f}" for r in d1['summary']))
p=Path('REPORT.md');s=p.read_text();pending='The simulation is running. Code and raw observations are being flushed in code/ and data/. The final numerical table will be inserted here after completion.'
if pending in s:
 p.write_text(s.replace(pending,text))
else:
 p.write_text(s.split('## Computation and verification')[0]+'## Computation and verification\n\n'+text)
meta=Path('data/run_metadata.json');m=json.loads(meta.read_text());m.setdefault('completed',datetime.datetime.now().astimezone().isoformat());m['observations']=len(raw);m['max_rss_bytes']=peak;meta.write_text(json.dumps(m,indent=2)+'\n')
print('Final numerical section inserted; analytical status remains PARTIAL.')
