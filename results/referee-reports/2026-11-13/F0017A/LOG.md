# F0017 work log

Task: “Open problem F0017” — received 2026-11-13, approximately 08:25 local machine clock (Asia/Tbilisi environment).

## 2026-11-13: orientation and literature

- Scope: this directory only; no publication, pushes, subagents, or retained PDFs/images. Computation will use nice 10, one worker, capped memory and explicit seeds.
- Read startup memory and compute state (status ok, owner_away_open); brain recall returned no useful mathematical prior.
- Mesh hello/digest failed: readonly coordination database outside permitted workspace. No claim was bypassed on another agent's files; all deliverables stay in this isolated authorized directory. Shared checklist and brain updates are likewise excluded by the sandbox and directory-only instruction.
- Initial searches found the source and related rank-resilience and singularity papers; no verified resolution yet. Unreviewed generated web manuscripts are not treated as established results.
- Next: save primary source texts, read Section 11 and later relevant theorem statements before computation.

## Literature checkpoint

- Saved arXiv:2005.02797 as extracted text only; read all of Section 11, PDF pp.16-17. Checked published numbering via the journal/NSF text: Conjecture 11.6, printed p.195.
- Saved and inspected the relevant primary theorem statements for Tikhomirov, Bourgain-Vu-Wood, Jain-Sah-Sawhney, Ferber-Jain-Luh-Samotij, Ferber-Luh-McKinley, Bandeira-Ferber-Kwan, Meka-Nguyen-Vu, Razborov-Viola, Kwan-Sauermann, Campos-Jenssen-Michelen-Sahasrabudhe, and Nguyen-Vu. Also found 2025 permanent and 2026 sharp scalar-singularity preprints. See sources/search_log.txt and manifest.jsonl.
- No verified resolution located. Negative search is qualified; scalar singularity results, including the 2026 sharp asymptotic claim, do not give diagonal resilience.
- nice command emitted a sandbox setpriority warning; independent os.getpriority check shows inherited nice=10, so computations already satisfy the requested priority.

## Mathematical checkpoint (before computation)

- Tikhomirov plus a union bound proves all switchings in every deterministic family of size exp((log 2 - delta)n) are nonsingular with exponentially high probability. This includes every Hamming ball of radius cn for any fixed c<1/2 and every fixed set of at most (1-epsilon)n freely switchable positions. These are direct corollaries, not claimed new theorems.
- The determinant polynomial has principal-minor coefficients and top coefficient 1. Its conditional zero mass is an integer multiple of 2^-n. A typical-coefficient bound strictly below 2^-n would prove the conjecture; an averaged bound o(2^-n) is impossible because of rare clustered row-pair obstructions.
- Derived an elementary Bonferroni bound for diagonal-repairable proportional row/column pairs: failure probability at least (8+o(1))n^2 2^-n. Each such event creates at least 2^(n-2) singular switchings. It tends to zero and is not a counterexample.
- Plan exact exhaustive enumeration through n=6 using row/column sign symmetry, then seeded samples through n=24 with all diagonal assignments checked. Proof and audit details will be in REPORT.md.

## Exact computation checkpoint

- Saved complete partial proofs in REPORT.md. Proof audit corrected a tempting restriction error: after fixing diagonal variables, the surviving full-product coefficient is a complementary completed minor, not necessarily 1.
- C++ enumerator uses the prime 2^61-1, Schur-complement branching over the diagonal cube, and a two-position pivot/fallback for zero pivots. Hadamard's bound for n<=24 is less than half this prime, so centered residues recover actual integer determinants. No floating-point determinant decisions.
- Every matrix checks the full number of visited assignments and the exact determinant-sum and top-character Fourier identities.
- Independent Python Bareiss validation passed 6,120 exact determinants and 96 sign-invariance checks; unreduced exhaustive n<=4 histograms agree with the symmetry quotient.
- A separate integer permutation-expansion/Walsh-transform implementation independently reproduced every exhaustive histogram through n=6. It uses no modular arithmetic or elimination.
- First Monte Carlo plan through n=24 completed with full diagonal cubes. All 100 n=24 samples had at least one zero. Additional odd sizes 15,17,19,21,23 are being filled in to audit parity effects before fitting.
- Computation is single-threaded at inherited nice 10. C++ sets a 3 GiB address-space limit; actual data and stack use are much smaller. Sources occupy about 1.3 MB at this checkpoint. No PDFs/images/scans retained.

## Resource-limit audit correction

- A later check showed macOS/sandbox setrlimit rejects AS/DATA/RSS limits. The initial code attempted AS=3 GiB without checking its return; that was not an enforced cap. Removed the ineffective call. This corrects the earlier log statement.
- Allocation is bounded by design: n<=24, fixed 24x24 stack matrices, sequential traversal; the 2^n determinant output vector is enabled only for n<=10 validation. Large-cube runs retain no exponential table. The final witness audit also measures child peak RSS, to substantiate the under-4-GB requirement directly.

## Completion and final audit

- Completed all dimensions 1–24: exhaustive quotient through 6, then 12,100 seeded samples with full diagonal enumeration. Main runs evaluated 4,293,332,502 exact integer determinants. Timed experiments total about 444 seconds, one computational thread, nice 10.
- Full raw count histograms and summary tables are saved. Size 24: 0 stubborn out of 100, median zero count 2,529, range 155–17,307, 95% Wilson interval for stubbornness [0,0.036993]. Exact size-six probability is 2845/262144.
- Added the missing odd dimensions before fitting. The median-count factorial fit peaks near size 21; the binomial logistic fit to stubbornness over 7–24 has negative slope. Neither is an asymptotic claim. The original plot is data/trend.svg; no source-paper images exist.
- Rechecked all exhaustive histograms by an independent integer permutation/Walsh implementation. Re-enumerated 15 larger matrices and checked explicit zero/nonzero witnesses with arbitrary-precision Bareiss elimination. Largest measured child RSS in that audit: 1,556,480 macOS bytes. Re-ran the independent small determinant validation after final code instrumentation; all checks pass.
- Verified the Mersenne prime by Lucas–Lehmer and all Hadamard comparisons by integer squares. Confirmed that rare proportional-pair events create the predicted clusters in the saved data.
- Added a complete elementary proof excluding left/right kernel support <=0.16n uniformly over all diagonal completions, and a precise sufficient reduction to an o(2^-n) nontrivial scalar-singularity bound. Neither settles the full conjecture.
- REPORT.md has final status PARTIAL. It includes the exact source statement, theorem/page literature locators, complete partial proofs, experimental methods, full tables, fit limitations and remaining gap. No verified literature resolution was located in the documented search.
- No subagents, external publication, pushes, schedules, or modifications outside this authorized directory. Shared brain/checklist/mesh updates remain unavailable under the read-only sandbox; this log is the local task record.

Task completed: “Open problem F0017” — received 2026-11-13, approximately 08:25 Asia/Tbilisi.
