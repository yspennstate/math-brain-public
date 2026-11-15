VERDICT: COMPUTED all 15,016 ordered pairs in S_n for 2 <= n <= 5, with exact certificates for bottlenecks missed by subset actions.

The full random expansion problem remains open in the primary sources checked. Ewan Cassidy, arXiv:2412.13941v3, substantially advances the Schreier case to ordered distinct k-tuples for k <= n^alpha, alpha<1/20. References and scope are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).

The completed piece is a finite spectral benchmark on the group each pair actually generates, together with an exact finite obstruction to replacing the full Cayley spectrum by subset-action spectra. No asymptotic progress or priority for this finite observation is claimed.

For the pair s=(3 4 5), t=(1 5 4 2 3), the group is A_5 and the four generators are distinct. Its Cayley gap is exactly (3-sqrt(5))/8, approximately 0.095491502812526. The natural-action gap is 1-sqrt(5)/4, approximately 0.440983005625053. Every permutation action on unordered subsets, including every subset size, has nontrivial upper gap greater than 1/4. The missing eigenvalue occurs in the exterior square of standard. [PROOF.md](PROOF.md) gives the group argument, explicit six-dimensional matrix, exact characteristic polynomials and root ordering. The full 60-dimensional characteristic polynomial was independently recovered from word-return counts and Newton identities, with every integer saved in [exact_a5_newton.csv](exact_a5_newton.csv).

The exhaustive numerical results are:

| n | All ordered pairs | Pairs generating A_n, nontrivial group | Minimum A_n gap | Pairs generating S_n | Minimum S_n gap |
|---|---:|---:|---:|---:|---:|
| 2 | 4 | 0 | — | 3 | 1.000000000000 |
| 3 | 36 | 8 | 0.750000000000 | 18 | 0.500000000000 |
| 4 | 576 | 96 | 0.359611796798 | 216 | 0.156929669183 |
| 5 | 14,400 | 2,280 | 0.056383180488 | 6,840 | 0.056167907288 |

For n=5 the natural action misses the full upper gap for all 2,280 A_5-generating pairs and 6,720 of 6,840 S_5-generating pairs. Adding the sign-twisted standard representation and the sign representation still misses the gap in 3,840 S_5-generating pairs. A separate exact S_5 witness is saved in [exact_witness.json](exact_witness.json).

These minima and aggregate miss counts are floating point results. The main run uses 982 representative pairs with exact conjugacy-class weights. An independent run enumerates all 15,016 pairs directly, uses a different group construction and a shifted Laplacian, and matches every group-order count, the full eight-decimal gap histogram and every miss count. In degree five the smallest positive miss is greater than 0.059; numerical ties differ by at most 2.2e-15. The classification threshold is 1e-8. Exact arithmetic certifies the displayed A_5 and S_5 witnesses, rather than all numerical minima.

The benchmark uses P=(R_s+R_s^-1+R_t+R_t^-1)/4, retaining repeated generators and loops, and the upper gap 1-lambda_2. It is not an absolute-gap benchmark: all-odd pairs have eigenvalue -1. The A_5 witness has four distinct generators and applies to the simple unweighted Cayley graph as well. The trivial generated group is recorded separately with no second eigenvalue.

Reproduction commands, run from this directory:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 enumerate_pairs.py > enumeration_output.txt
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 audit_pairs.py > audit_output.txt
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 exact_witness.py > exact_output.txt
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 exact_a5.py > exact_a5_output.txt
OMP_NUM_THREADS=1 nice -n 15 python3 verify_certificate.py > final_check.txt
```

All scripts force numerical-library thread counts to one. The longest completed run took about six seconds; peak measured RSS across these runs was below 61 MB. Actual inherited nice was 20; macOS's warning when `nice -n 15` attempted to lower priority further did not raise the process priority.

Files: [pairs.csv](pairs.csv) contains weighted pair data, including every generated-group order; [summary.json](summary.json) summarizes it; [audit.json](audit.json) records the independent comparison; [exact_a5.json](exact_a5.json) and [exact_witness.json](exact_witness.json) contain exact factors and rational root intervals. [LOG.md](LOG.md) records commands, results and failed checks.

The standard-library verifier checks all 60 saved Newton identities, expands the claimed characteristic factorization using integer-list multiplication, and compares the radical gap formulas with the independent enumeration. Its output is [final_check.txt](final_check.txt).

What failed: the first auxiliary comparison included a trivial sign-twisted standard representation at n=2; that case was excluded. For the first S_5 witness, ordinary and sign-twisted two-subset actions both failed to contain the top eigenvalue; the exterior square supplied it. That witness also duplicated an involution in the four-term walk, which motivated the additional A_5 witness with four distinct generators. These failures are retained in the log.

What remains uncertain: the numerical minima have no exhaustive rational interval certificate; no n>5 data or asymptotic inference is supplied. Novelty of the finite witness was not established. The recent growing-tuple results do not control the full regular representation.

Next worker: use the finite data to test a proposed representation reduction before attempting a probabilistic proof. Ordered tuples and unordered subsets must be distinguished: the exterior-square obstruction is already present in A_5. A useful continuation would attach exact rational interval certificates to all representative gaps, or implement block-by-block enumeration for n=6 with the same independent audit.

Task: “push this problem forward by one checkable piece” (T085), 14 November 2026, approximately 20:53 Asia/Tbilisi, from the runner start time.
