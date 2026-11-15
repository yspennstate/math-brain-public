# T095 continuation log

Task: “take the NEXT checkable step on this problem, building on that work.” Started 15 November 2026, 04:16 Asia/Tbilisi.

## Step 1 — earlier work and constraints

Read both earlier REPORT.md and LOG.md files and round 3 PROOF.md; the original folder has no PROOF.md or scripts. Reading round 3 audit.py and the crossing source next. Compute state: warn, owner_away_open, CPU saturated; only small single-thread text and exact-arithmetic checks are planned. All shell programs use OMP_NUM_THREADS=1 and nice -n 15; the sandbox prints “nice: setpriority: Operation not permitted”, so actual inherited niceness is checked separately. No git or subagents.

The task-specific instruction confines writes to this folder. Brain recall/checklist/mesh commands that write outside it are therefore excluded; startup-memory and compute-state reads are allowed. Earlier conclusion: Gamma-only claim scope; the characteristic-length reduction is conditional on rare-fast crossings and localized travel.

Commands: bounded pathlib reads under `OMP_NUM_THREADS=1 nice -n 15 python3`; web search initiated for subsequent differentiability results and criticism. No mathematical conclusion drawn from search snippets.

## Step 2 — bounded update search and independent recheck

Web queries: exact shape title with error/November 2026; first-passage continuous differentiability OpenAI 2026; df:cr:rare-fast/GammaPassage refutation; first-passage differentiability after 2026-11-13; exact title with correction/refutation/review. Reopened arXiv:2610.42124, Scott Armstrong and Ahmed Bou-Rabee, *Fluctuation bounds for rotationally invariant first-passage percolation*: its continuum fluctuation result is not T095. No new full continuous-law theorem or specific refutation was located. GitHub read-only latest-commit API still returns 4eaee87548250b2682affda7d05d947c05554bae (30 October 2026). Update search closed within five minutes.

Read startup memory. Actual process niceness is 20 (lower priority than requested), OMP_NUM_THREADS=1. Read all of round 3 audit.py. Re-ran it without edits via runpy: four source/theorem checks, 36 exact Gamma integrals, 30 edge counts (maximum M/(ns)=115, bound 144), and 50 tail identities all PASS. Re-derived the main likelihood independently: E[(dQ/dP)^2]=[alpha(2-alpha)]^(-kappa M), so log cost is O(M delta^2)=O(s^3/n), bounded at n=s^3. This confirms the earlier conditional reduction, not its unproved crossing inputs.

Fresh GitHub crossing source saved here and compared byte-for-byte with round 3: identical.

## Step 3 — choice of extension

Chosen ONE extension: check df:cr:rare-fast, including its high-density oriented-path lemma, trial independence, connectors, and the order of constants. This is the precise next step named by round 3. The central issue is whether k0 is fixed before M and D0, and whether a fixed-scale infinite concatenation really contradicts the origin shape theorem. A complete conditional derivation and an independent finite contour/geometry audit will be written here. No full differentiability proof is claimed.

## Step 4 — primary source reopens

Opened and saved the actual shape introduction, differentiability/preliminaries.tex and crossings.tex, the two other candidates’ 01-introduction.tex files, lean/docs/212.md, ComparatorChallenges/GammaPassage.lean, and GammaPassage/Differentiability.lean at the pinned revision. Initial guesses using sections/introduction.tex for the other two candidates returned file-not-found; corrected to the paths recorded in the earlier VERIFY.md. Four exact main theorem environments are available. Lean was read, not built. Interim REPORT.md saved before the detailed check.

## Step 5 — rare-fast derivation saved

Wrote PROOF.md. Re-derived localized travel directly from the uniform origin shape theorem, interval travel by bounded nets and Gamma exponential moments, the oriented-path contour lemma, disjoint trial placement, all-endpoint connectors, and fixed-scale concatenation. The fixed radius is k=ceil(4(A+3)+8)+1, chosen before M or D0. Derived an explicit sufficient bad-site probability zeta=2^(-48(2k+1)^2); the contour sum has ratio 1/16 and is below 3/256. This explicit threshold is only a conservative audit bound, not a claimed optimal constant.

Wrote audit.py with a 768 MiB address-space cap and 60-second alarm. It tests arbitrary finite cell sets, including holes and corner contacts, independently of the manuscript’s trial construction; exact rational arithmetic also checks lattice-phase rounding and the inverse dependence coordinates. It will run after the source-comparison document is saved.

## Step 6 — theorem comparison and initial audit failure

Saved VERIFY.md with all four exact theorem environments, clause-by-clause comparisons, actual source links, the reopened Lean scope/target/final proof, MathVet’s pinned family-212 row, arXiv abstract-page finding, and a three-sentence status recommendation. Reopened all three actual build/main.tex files: each author is OpenAI, and the dates match September 24/25, 2026.

First command `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py` failed before any mathematical check: macOS rejected the 768 MiB RLIMIT_AS with ValueError: current limit exceeds maximum limit. Replaced it with a 768 MiB data-allocation limit, retaining any stricter inherited hard limit. The audit’s mathematical cases remain unchanged. This is an execution-guard issue, not a failure of the earlier result.

## Step 7 — exact finite audit and attempts to break the result

The second audit launch also stopped before mathematical checks: RLIMIT_DATA was rejected with the same ValueError as RLIMIT_AS. The final script catches this unavailable setter, retains a 60-second alarm, checks its measured peak RSS below 1 GiB, and uses only tiny bounded standard-library allocations. No heavy computation was attempted.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py`. Exit 0, output:

```text
nice: setpriority: Operation not permitted
Data-limit setter unavailable: current limit exceeds maximum limit
OMP_NUM_THREADS=1
Process nice value: 20
Eight reopened sources unchanged: PASS
Independent likelihood base checks: 15 PASS
Contour decomposition/winding/forced sites/packing: 2307 sets PASS
Exact contour union bound: 181/48000 ; independent forms agree PASS
Explicit density exponent checks: 10 PASS
Exact rational strip placement cases: 1536 PASS
Dependence-coordinate cases: 1734 PASS
Four exact theorem blocks, verdict, local links: PASS
Elapsed seconds: 0.307
Peak RSS bytes (macOS): 15974400
```

The contour audit covers every subset containing the origin of a 3x3 and a 4x3 grid, plus explicit holes, corner contacts and disconnected pieces. It tests cancellation, closed-trail decomposition, winding sum one, forced forward-neighbor bad sites, and greedy independent-site selection. This is finite verification of bookkeeping, not a proof of all finite sets; the all-set proof is in PROOF.md.

Second derivations: the contour sum is computed from (1+a)/(1-a)^3 after subtraction and independently by shifting m=j+4; both give 181/48000. The weaker analytic majorant gives 3/256. The previous likelihood is rechecked by a sum Laplace-transform base identity. The support-overlap coordinate bounds are checked both by inequalities and exact integer enumeration. Tested negative slopes, signs, translations and half-integer phases, M=1 and large M, nonintegral s, holes and diagonal contacts. Reviewed p0=1, repeated path edges, random endpoints, and the fixed-scale order of limits. No counterexample or gap was found in the checked section.

An attempted combined final patch failed on an unmatched VERIFY.md line (the quoted line belonged to PROOF.md). The final report and verification additions are applied separately below; no mathematical finding depends on that editing failure.

## Step 8 — final artifact audit

Finalized REPORT.md in the later continuation format: PARTIAL for the rare-fast input checked from the fixed-Gamma uniform shape theorem. VERIFY.md preserves the separate literature conclusion PARTIAL-CLAIMED, all exact main theorem quotations, the general-law limitation, reopened sources and follow-ups, and the three-sentence replacement status. PROOF.md supplies the full section-level derivation and audit.py the reproducible finite checks. A final small text audit passed: four report lines, three status sentences, required files and matching numerical findings. No rerun of unchanged mathematical cases was needed.

Remaining uncertainty: the uniform shape theorem is an input here, not newly proved; later transverse-witness/final differentiability steps, strict convexity, and the full Lean dependency chain remain unaudited. Next worker should inspect the transverse-witness argument against the endpoint estimates already checked in the first session. No writes outside this folder, git, pushes, external messages/posts, accounts, subagents, GPU, simulation, or Lean build occurred.
