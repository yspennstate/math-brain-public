# T142 working log

Task received: 2026-11-14, approximately 22:02 Asia/Tbilisi (18:02 UTC).
Task: “push this problem forward by one checkable piece.”

## 1. Orientation and literature search (18:02–18:06 UTC)

Read the local prompt, startup memory/navigation, and compute state. The governor
reported `status: warn`, `mode: owner_away_open`, CPU saturation, and about 43%
free memory. All calculations will be single-threaded under `nice -n 15`, with
`OMP_NUM_THREADS=1`, and kept far below 1 GB. No subagents, git, or external writes.
The task's explicit folder-only rule overrides the earlier standing instructions
to update the external brain, mesh, and checklist; those programs were not run.

Web searches so far:

- `longest common subsequence variance uniform binary Waterman conjecture 2024 2025 2026`
- `longest common subsequence variance lower bound unbiased binary random strings 2025 2026`
- `"longest common subsequence" "variance" "2026"`
- `"longest common subsequence" "variance" "2025"`
- `"Waterman" "variance" conjecture binary 2024`

No resolution appeared. Some recent results concern the mean, not the variance.
The search also surfaced a finite-variance OEIS entry and a 2026 open-problem
listing. These are leads, not yet accepted citations. Papers actually opened
and the final search outcome will be recorded below.

## 2. Chosen piece (recorded before implementation)

Prove the symmetry-improved finite-n upper bound `Var(L_n) <= n/4` using the
Walsh expansion on the `2n` independent bits. Global complementation leaves LCS
unchanged, so odd degrees vanish; changing one bit changes LCS by at most one.
The ordinary Poincare estimate then gains a factor of two. This is a modest
finite-n result, not the conjectured lower bound; its novelty is not assumed.

Make the proof checkable and useful for the lower-bound problem by computing
exact Walsh variance by degree for small n, and a same-word quadratic projection
for somewhat larger n if cheap. The degree-two identity gives a concrete
candidate lower-bound mechanism that survives fair-letter symmetry. Independently
verify the LCS values with a different algorithm and recompute all reported
fractions from integer histograms. Stop at a safe small cutoff rather than fit
an asymptotic exponent from small cases.

## 3. Opened primary literature (18:04 UTC)

Opened the arXiv pages, not merely search snippets:

- Jüri Lember and Heinrich Matzinger, *Standard deviation of the longest common
  subsequence*, [arXiv:0907.5137](https://arxiv.org/abs/0907.5137), Ann. Probab.
  37 (2009), 1192–1235: linear variance for sufficiently small Bernoulli parameter.
- Christian Houdré and Ümit Işlak, *A Central Limit Theorem for the Length of the
  Longest Common Subsequences in Random Words*,
  [arXiv:1408.1559v6](https://arxiv.org/abs/1408.1559v6), EJP 28 (2023), paper 3:
  the CLT still assumes a variance lower bound; the page says the main result
  was unchanged in its latest revision.
- Saba Amsalu, Raphael Hauser and Heinrich Matzinger, *A Monte Carlo Approach to
  the Fluctuation Problem in Optimal Alignments of Random Strings*,
  [arXiv:1211.5489](https://arxiv.org/abs/1211.5489): the abstract explicitly says
  the equiprobable binary case remains open and symmetry obstructs its method.
- Christian Houdré and Qingqing Liu, *On the Variance of the Length of the
  Longest Common Subsequences in Random Words With an Omitted Letter*,
  [arXiv:1812.09552](https://arxiv.org/abs/1812.09552): the alphabets of the two
  words differ; this does not settle the present setting.

Additional targeted searches: `"longest common subsequence" variance "n/4"`,
`"longest common subsequence" variance Fourier symmetry`, and arXiv-restricted
variance searches after 2023. No matching proof of the fair-binary conjecture
or explicit n/4 citation was found. This is not an assertion that the n/4
observation is new.

## 4. Proof and implementation (18:04–18:09 UTC)

The literature check is finished, well within ten minutes. Further targeted
2024–2026 searches returned no resolution or matching substantial advance on
the fair-binary variance lower bound. This is a bounded search, not a guarantee
that every recent paper was indexed.

Saved `PROOF.md`: the n/4 bound, exact Fourier remainder identity, quadratic
projection formula, and a sufficient derivative criterion using symmetric
Markov words. No asymptotic interchange of limit and derivative is used.

Implemented `exact_lcs.c`: exhaustive pair enumeration, full integer Walsh
transform, histogram, flip-edge count, all quadratic coefficients, same-word
conditional means, and direct adjacency covariance. Two enumeration modes use
different LCS recurrences (bit-parallel and ordinary prefix DP). They also
apply the transform's coordinate stages in opposite orders.

Build command:

```sh
OMP_NUM_THREADS=1 nice -n 15 clang -std=c11 -O3 -Wall -Wextra -Wconversion exact_lcs.c -o exact_lcs
```

The first build exposed only signed-conversion warnings; explicit casts removed
them. `nice` reports `setpriority: Operation not permitted` in this sandbox.
The executable independently reads its inherited priority with `getpriority`:
`observed_nice=20`, which is already lower priority than requested, and refuses
to compute if it is below 15. An attempted address-space cap returned
`setrlimit AS: Invalid argument`; that failed preliminary run did no enumeration.
The cap was removed. The fixed n<=12 limit bounds the large allocation to 64 MiB;
two row arrays add 64 KiB and the remaining storage is small. A 1,100-second
CPU limit is enforced. A wall-time limit will be added to the reproduction runner.

Started the primary run:

```sh
OMP_NUM_THREADS=1 nice -n 15 ./exact_lcs bits 12 > results_bits.jsonl 2> run_bits.txt
```

The first n=1 probe was unsuccessful solely because of the unsupported AS cap;
its output was replaced by the full run after that correction.

## 5. Exact enumeration and independent audit (18:08–18:11 UTC)

Primary run finished. `run_bits.txt` reports assertions passed at each n=1..12;
the n=12 run used 1.039 CPU seconds. Then ran:

```sh
OMP_NUM_THREADS=1 nice -n 15 ./exact_lcs dp 12 > results_dp.jsonl 2> run_dp.txt
cmp results_bits.jsonl results_dp.jsonl
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt
```

`cmp` returned zero with no output. The ordinary DP run used 2.558 CPU seconds
at n=12; inherited niceness was independently reported as 20. Both methods
enumerated 22,369,620 ordered pairs across n=1..12. Data are in
`results_bits.jsonl`, `results_dp.jsonl`, `summary.csv`, `spectrum.csv`, and
`quadratic.csv`. `audit.py` derives all fractions with `fractions.Fraction`.

Exact audit output (rounded columns are for display only):

```text
n= 1 pairs=       4 variance=0.2500000000 W2/variance=1.00000000 Markov_derivative/n=0.00000000 PASS
n= 2 pairs=      16 variance=0.3593750000 W2/variance=0.95652174 Markov_derivative/n=-0.12500000 PASS
n= 3 pairs=      64 variance=0.4648437500 W2/variance=0.93277311 Markov_derivative/n=-0.16666667 PASS
n= 4 pairs=     256 variance=0.5775756836 W2/variance=0.90584381 Markov_derivative/n=-0.17578125 PASS
n= 5 pairs=    1024 variance=0.6855316162 W2/variance=0.88421217 Markov_derivative/n=-0.17500000 PASS
n= 6 pairs=    4096 variance=0.7832906246 W2/variance=0.86987206 Markov_derivative/n=-0.17171224 PASS
n= 7 pairs=   16384 variance=0.8765034080 W2/variance=0.85903601 Markov_derivative/n=-0.16838728 PASS
n= 8 pairs=   65536 variance=0.9653547853 W2/variance=0.85010309 Markov_derivative/n=-0.16506958 PASS
n= 9 pairs=  262144 variance=1.0505692640 W2/variance=0.84234742 Markov_derivative/n=-0.16193305 PASS
n=10 pairs= 1048576 variance=1.1322370113 W2/variance=0.83558359 Markov_derivative/n=-0.15896759 PASS
n=11 pairs= 4194304 variance=1.2107665692 W2/variance=0.82957345 Markov_derivative/n=-0.15621324 PASS
n=12 pairs=16777216 variance=1.2866691397 W2/variance=0.82415085 Markov_derivative/n=-0.15368025 PASS
```

`audit.json` has `verdict: PASS`. Independent and adversarial checks:

- Ordinary prefix DP versus bit-parallel LCS, with exact equality of all output
  data. No symmetry quotient was used to omit pairs.
- At n<=5 a third method forms literal sets of subsequences and takes their
  intersections, then computes every Walsh coefficient by its defining sum
  rather than a transform. All histograms and degree masses agree.
- Variance rederived both from raw histogram moments and from centered squared
  deviations; each agrees with the sum of nonconstant Walsh masses.
- Direct flip-edge counts agree with spectral energy; all odd masses vanish.
- Every quadratic coefficient agrees between the two enumeration/transform
  orders. Same-word coefficients are also checked by direct sums of conditional
  means, and the adjacent statistic is accumulated directly over word pairs.
- n=1 attains n/4 exactly. n=0 is treated separately in the proof. The adjacent
  derivative bound is only asserted for n>=2, avoiding division by zero.
- The Markov derivative is finite-n; the calculation does not exchange
  differentiation and an infinite-n limit. No inference of a linear lower
  bound from small n is made.

The attempt to obtain a lower bound stalls at estimating the derivative
uniformly in n. The data cannot rule out `F_n'(0)/n -> 0`; its magnitude already
decreases over n=4..12. Similarly, a large observed W2/variance fraction does
not prove that W2 grows linearly.

## 6. Final reproduction and handoff (18:12–18:13 UTC)

Added `DATA.md`, `REPORT.md`, and `reproduce.py`. The report begins with
`VERDICT: PARTIAL` and distinguishes the proved upper bound from the unproved
linear lower bound. Added a full derivation of the conditional-word projection
and all data normalizations to `PROOF.md`.

Strengthened the ordinary-DP run to compare **every individual score** with the
independent bit-parallel score, for all 22,369,620 ordered pairs. Added peak-RSS
reporting. The exact data did not change.

Final command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 reproduce.py > reproduction.txt
```

Output: twelve `PASS` rows and `{"verdict": "PASS", ...}` as in `audit.txt`.
The final run records inherited nice 20. At n=12:

```text
bits n=12 pairs=16777216 cpu_seconds=0.954 maxrss_raw=90882048 assertions=passed
dp n=12 pairs=16777216 cpu_seconds=2.577 maxrss_raw=90914816 assertions=passed
```

On macOS these RSS values are bytes: both are below 91 MB, independently of the
64 MiB main-allocation calculation. Exact n=12 values were read back from
`summary.csv` and checked against the report table:

- variance = 5658830720631/4398046511104;
- W2 = 1165932541151/1099511627776;
- F_12'(0) = -1933745/1048576;
- derivative lower bound = 339942702275/2199023255552.

Every computation stayed single-threaded, sequential, and far below the time
and memory limits. No files outside this folder were intentionally written;
there was no git use, external publication, or account creation.

Task completed as a partial result: “push this problem forward by one checkable
piece” — 14 November 2026, approximately 22:02 Asia/Tbilisi.
