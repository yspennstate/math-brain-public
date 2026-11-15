# T287 work log

Task: “push this problem forward by one checkable piece.” Session began 2026-11-14, approximately 22:09 Asia/Tbilisi (18:09 UTC).

## Initial orientation and constraints

Read the local startup memory index, brain navigation references, mesh protocol, and compute state. The later task-specific instruction confines every write to this folder; therefore no shared mesh, checklist, recall logger, or brain-memory writes are being made. No subagents, git, or external posting.

The compute state reported `warn`, `owner_away_open`, 68% memory free, and high CPU use. Only a small single-thread exact computation is planned. Shell invocations will use `OMP_NUM_THREADS=1 nice -n 15`; this sandbox prints `nice: setpriority: Operation not permitted` before executing. Effective inherited niceness must be checked before computation. Initial read-only orientation commands were not prefixed; subsequent shell commands are.

## Literature check (started 18:09 UTC)

Web searches: `extensive rank matrix factorization mutual information non Gaussian priors Bayes optimal 2025 2026`; `"2110.08775" matrix factorization mutual information solved`; `"extensive-rank" "2026" "factorization" mutual information`; `"extensive-rank" "2025" "non" "Bayes"`; `"extensive-rank" "denoising-factorisation"`.

Opened https://arxiv.org/abs/2110.08775: Antoine Maillard, Florent Krzakala, Marc Mézard, Lenka Zdeborová, *Perturbative construction of mean-field equations in extensive-rank matrix factorization and denoising*, arXiv:2110.08775, revised June 2022. Search located later work on the symmetric model and sublinear rank, which needs opening before a status conclusion.

Opened arXiv pages 2411.01974, 2403.07189, 2609.07771 and the HTML of 2110.08775v3. Further searches included `"extensive-rank" "mutual information" "2026" proof non-Gaussian` and `"extensive-rank" "rectangular" "2026" "Bayes"`. No solution to the stated general problem was found. The symmetric phase-diagram paper is heuristic/numerical; the sublinear-rank paper has a different rank regime; the HCIZ paper concerns rotationally invariant integrals. These predate the supplied November 2026 status. Literature checking ends at approximately 18:12 UTC, within ten minutes. Bibliographic details and scope will be retained in REPORT.md. This is a bounded search, not a proof of absence.

## Chosen piece (before proof or computation)

Prove the exact fourth-order, finite-dimensional low-SNR mutual-information coefficient for independent bounded symmetric unit-variance entry priors. Compute its proportional-dimension limit. The coefficient measures a surviving rectangle-cycle dependence invisible to independent scalar Gaussian approximations. This is a local constraint on a future limiting formula, not a formula for fixed positive SNR, and novelty over the source's related perturbative calculations is not claimed. If possible, obtain the corresponding finite-size product-MMSE coefficient by a direct Gaussian score calculation.

Independent checks planned: enumerate full Rademacher products in tiny dimensions using integer fourth moments; separately enumerate one-column sparse priors using exact rational weights; evaluate the Hermite polynomial norm directly by Gaussian polynomial integration, without the cumulant-tensor norm identity.

Niceness check: `env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -c 'import os; print("effective_nice", os.getpriority(os.PRIO_PROCESS, 0))'` printed `effective_nice 20`. The warning arises from attempting to increase an already lowest-priority process further. All numerical work inherits nice 20 and uses the requested nice wrapper.

## Proof drafted

Wrote PROOF.md. The candidate exact coefficient is

`C = M^2/(48 N^4) * [(ab-3)^2 + 3(P-1)(a-1)^2 + 3(N-1)(b-1)^2 + 6(N-1)(P-1)]`,

where a,b are the fourth moments. The finite-size claims are `i(t)=log(1+(M/N)t)/2-Ct^4+O(t^5)` and `e(t)=(M/N)/(1+(M/N)t)-8Ct^3+O(t^4)`. The proof uses bounded-vector density expansions with Gaussian-weighted remainder control, exact fourth-cumulant classification, and a separate posterior-score argument for MMSE. A potentially dangerous step, differentiating a small-o remainder, is avoided. The constants in the remainder may depend on dimension.

In the proportional limit only rectangle cumulants survive, giving `C -> alpha^2 beta/8`. The proof does not address the quotient loss for U and does not establish a fixed-SNR thermodynamic formula.

## First verification attempt

Command: `env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 check_coefficients.py > verification.stdout 2> verification.stderr`

Exited 1 before any computation: macOS rejected `resource.setrlimit(resource.RLIMIT_AS, (768*1024**2, 768*1024**2))` with `ValueError: current limit exceeds maximum limit`. Removed this unsupported address-space limit. The exact enumeration is small, standard-library only, has a 90-second CPU limit, and now checks actual peak resident bytes before each case and before saving. The first failure is retained here; successful output will replace the attempt's empty stdout and error file.

## Exact verification, first successful run

Re-ran the same command after the portability fix. All ten complete-prior enumerations passed, including N=1, P=1, two-column sums, unequal rectangular shapes, and unequal sparse fourth moments. Selected exact outputs: Rademacher (N,P,M)=(2,2,2) has C=5/96 and 8C=5/12; sparse fourth moments (a,b)=(4,9) at (2,2,1) give C=219/128. Direct monomial integration of A² and ||gradient A||² agrees with the tensor formula in every case. The scalar tanh posterior gives MMSE `1-t+t^2-(5/3)t^3+O(t^4)` independently. A non-square scaling M=2N,P=3N gives C=1.4998000083333334 at N=10000, tending to 3/2. Runtime 0.014330 s; peak RSS 15,663,104 bytes; effective nice 20.

Added one independent scalar mutual-information check using the exact log-cosh likelihood rather than integration of MMSE. Its degree-eight Taylor polynomial gives `i=t/2-t^2/4+t^3/6-(5/24)t^4+O(t^5)`, and hence C=1/12. A final run will save this extra check too.

## Final verification and attempts to break the result

The final identical command exited 0. Complete output is in verification.stdout; exact rational data are in verification.json. It passed all ten cases plus both independent scalar-channel checks. Runtime 0.014677 s; peak RSS 16,039,936 bytes (about 15.3 MiB); nice 20. verification.stderr contains only the already-explained nice warning.

Audited the density expansion in L²/L³ rather than assuming a pointwise expansion integrates; boundedness supplies Gaussian domination for each fixed dimension. Audited the inverse density in the score calculation using Jensen's inequality, followed by Hölder, so no unproved lower bound or derivative of an asymptotic remainder is used. Recounted repeated edges, shared rows, shared columns, disjoint doubled edges, and all-distinct rectangles. Exact sparse tests with different fourth moments check row/column orientation, while N=1 or P=1 checks the vanished rectangle terms. Transposing rectangular examples changes the normalization N and the enumerations correctly reflect this.

The source already contains related fourth-order perturbative corrections; this result is an explicit finite-size information/MMSE identity with a self-contained proof and exact checks, not a claim of a new physical phenomenon or a priority claim. Clarified that priors must be fixed across dimensions. Removed an unnecessary comparison with unbounded Gaussian factors, because the bounded-density-expansion proof does not cover them. Non-centered or asymmetric priors, dimension-dependent sparse priors, and unbounded priors are outside the theorem.

The serious unresolved issue is the order of limits. The bounds used to justify Taylor expansion depend on dimension and do not give a uniform t interval or uniform normalized remainder. It would be invalid to promote (5) to a Taylor expansion of an unproved thermodynamic limit. The proof explicitly avoids doing so. U under the sign/permutation quotient loss is untouched.

As a direct corollary of the same coefficient calculation, added the total-correlation coefficient (17), subtracting the one-dimensional entry expansions. At N=P=M=2 with Rademacher entries, its coefficient is `5/96 - 1/48 = 1/32`; the full enumeration and the scalar calculation provide the two independent inputs. This identifies the surviving term specifically as inter-entry dependence.

Final verification.stdout, from the command printed above:

```text
PASS N=1 P=1 M=1 U=rad V=rad C=1/12 8C=2/3
PASS N=1 P=2 M=2 U=rad V=rad C=1/3 8C=8/3
PASS N=2 P=1 M=2 U=rad V=rad C=1/48 8C=1/6
PASS N=2 P=2 M=1 U=rad V=rad C=5/384 8C=5/48
PASS N=2 P=2 M=2 U=rad V=rad C=5/96 8C=5/12
PASS N=2 P=3 M=2 U=rad V=rad C=1/12 8C=2/3
PASS N=2 P=2 M=1 U=sparse2 V=rad C=17/384 8C=17/48
PASS N=2 P=2 M=1 U=rad V=sparse3 C=39/128 8C=39/16
PASS N=2 P=2 M=1 U=sparse2 V=sparse3 C=219/128 8C=219/16
PASS N=1 P=2 M=2 U=sparse2 V=sparse3 C=93 8C=744
PASS scalar posterior MMSE = 1-t+t^2-(5/3)t^3+O(t^4)
PASS scalar likelihood MI = t/2-t^2/4+t^3/6-(5/24)t^4+O(t^5)
Rademacher alpha=2 beta=3: C(N=10000)=1.4998000083; predicted limit=1.5
ALL 10 exact cases passed; data: verification.json
elapsed_seconds=0.014677 peak_rss_bytes=16039936 nice=20
```

Final verification.stderr:

```text
nice: setpriority: Operation not permitted
```

Wrote REPORT.md with the PROVED verdict restricted to the finite-size local theorem, bibliographic scope, the failed portability attempt, all commands and data links, and the next precise analytic target. Final artifact audit checks the report's first line, all expected files, JSON contents, and consistency of the scalar and rectangle constants. No shared-state writes, git, agents, or external posting were used.

Artifact audit completed successfully (a short standard-library Python assertion command under `env OMP_NUM_THREADS=1 nice -n 15`): `Artifact audit passed: 7 deliverables, 10 exact cases, total-correlation coefficient 1/32.` Report first line matched the required `VERDICT: PROVED ...` format. This audit only read files.
