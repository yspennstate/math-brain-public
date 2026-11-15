# C0097 work log

Task received: 2026-11-13 06:34 +04 (Asia/Tbilisi).
Scope: literature audit, mathematical attack, coefficient reproduction for the high-dimensional nearest-neighbour SAW connective constant. No publication or pushes. One worker; numerical work will run at nice 10 with one thread.

## Stage 1 — orientation and first sources

Read the local memory index, identity and creativity-method memories, compute state, and mesh protocol. The mesh hello and digest commands both failed with `attempt to write a readonly database`. The task's directory-only restriction and filesystem sandbox prevent shared coordination/checklist/memory writes; all task records therefore stay here. No subagents started. Compute state reports owner away, CPU saturated; avoid heavy computation.

Opened the actual arXiv PDFs through the web reader, without saving PDFs or page images. Sources will be converted in memory to plain text only. Graham arXiv:0911.5163, Theorem 1.1, p. 2 gives a factorial remainder upper bound; Section 2, pp. 2–3 calls SAW Borel summability conjectural and explicitly says complex continuation is unavailable. His spherical-model discussion already gives a related divergent/Borel-summable example; any partial theorem here must acknowledge that prior result.

Next: obtain plain texts of the four requested sources, audit later literature, then attempt a self-contained rigorous related-model result.

## Stage 2 — source correction and later evidence

The requested passage is Section **1.4**, not 1.5, of arXiv:1206.2092, pp. 4–5, equations (1.19)–(1.20). Section 1.5 treats critical exponents. Saved both lecture and Graham arXiv texts by sending downloaded PDF bytes directly to pdftotext stdin; no PDFs were written. An attempted os.nice(10) raised PermissionError before fetching; this is a sandbox limitation, not a numerical result. All computation remains small and single-threaded.

Heydenreich–Matzke, Combinatorics, Probability and Computing 31 (2022), 430–454, pp. 431–432, explicitly calls zero-radius behaviour of the related percolation series expected with rigorous evidence lacking. It cites Graham only for SAW Borel-type bounds, and Gerber–Fisher (1974) for the already solved spherical-model analogy. Searches through 2026 have not located a proof for SAW; the final report must describe this as a search outcome, not a proof that no publication exists.

Possible partial results to examine after the literature audit: (i) a self-contained zero-radius proof for SRW Green/return series via the inverse of x-log I0(x), explicitly crediting the spherical-model precedent; (ii) fixed-memory walk series have positive radius by a finite quotient transfer matrix, explaining why taking memory to infinity is essential. Main obstruction remains cancellation among signed lace contributions.

## Literature audit checkpoint (06:42 +04)

Read the lecture passage, Graham's statement and Borel discussion, CLS Section 1.3 (equation (1), author pp. 3–4) and Section 6.4, Mejía Miranda–Slade (2013) Theorem 1.1 and open-problem discussion (author pp. 2–3), and Heydenreich–Matzke (2022) Theorem 1.1 and summability discussion (journal pp. 431–432). Queried combinations of SAW/connective constant, zero radius/divergence, Borel/factorial bounds/nonanalyticity, inverse dimension, percolation, lattice trees, with later-year filters through 2026; inspected Slade's publication list (includes 2026 preprints). No SAW divergence or full Borel-summability theorem found. This is a bounded literature search, not an exhaustive certification.

Hara–Slade's publisher abstract and full bibliographic record are available; publisher full text has been difficult to retrieve. The author's linked `93-288.pdf` is explicitly an unpublished calculation appendix, not the 1995 article; saved its extracted text with that distinction. Do not substitute its numbering for the published theorem. Attempts continue only to verify the original statement and theorem locator.

CLS coefficients transcribed: mu = s^-1 -1 -s -3s² -16s³ -102s⁴ -729s⁵ -5533s⁶ -42229s⁷ -288761s⁸ -1026328s⁹ +21070667s¹⁰ +780280468s¹¹ +O(s¹²). The sign change matters; no positivity argument is available for the full series.

The launcher `launch.sh` explicitly starts the Codex process under `nice -n 10`. Children inherit priority. Attempts to increase niceness again were rejected by the sandbox. No heavy computation has been run; subsequent exact small calculations inherit the launcher priority and use one thread.

## Attack checkpoint

A stronger fixed-memory statement is available by an elementary matrix argument: for memory tau>=2 and L=tau-1, the normalized connective constant s*mu_tau has a holomorphic germ on |s|<1/(24 L²). The proof uses Q(s)=A+sB, where A always chooses a new coordinate axis, A^L is the rank-one reset projection, and ||B||_infinity<=4L. A resolvent contour at distance 1/(2L) from 1 gives ||(zI-A)^-1||<=6L. This will be written out and independently checked on small memories.

For SRW, G_d(0)=d*integral exp(-d*(x-log I0(x))) dx. The local inverse h of g=x-log I0(x) cannot be entire: I0(h(t))=exp(h(t)-t) would make a nonconstant entire h omit two distinct zeros of I0, contradicting Little Picard. Its finite Taylor radius implies a factorial lower bound along an infinite subsequence after the Laplace integral supplies n!. This reproduces a known spherical-model divergence mechanism; it does not control SAW lace cancellations.

The proposed analyticity shortcut for SAW has an additional gap: convergence of its formal asymptotic series would not itself identify its sum with the discrete sequence mu(d); flat corrections survive all finite-order asymptotics. Low-dimensional values cannot fix that gap or force radius zero.

## Computation checkpoint

`code/analyse.py` reproduces the 13 reciprocal critical-point coefficients from the 12 regular coefficients of mu. Independent exact reciprocal recurrences agree. The 40-term SRW calculation by Bessel/Lagrange inversion agrees through degree 12 with a separate closed-walk enumeration by occupied axes. A first run accidentally introduced floating point in an empty sum divided by an integer; the independent comparison caught the discrepancy at degree 8. Fixed the empty sum to start with Fraction(0), reran, and all comparisons are now exact. Total runtime about 0.05 seconds, one thread, small memory.

`code/memory_walks.py` constructs quotient matrices for tau=2,4,6 with 1,6,109 states. It verifies the reset identity, row-norm bound, eigenvector equations through degree 12, and compares quotient counts against literal d=2 length-8 path enumeration (8748,6444,6028). All checks pass in about 0.03 seconds. No lace expansion recomputation.

A direct lace-related factorial family is also available: length-2m polygons using m distinct axes, positive steps in first-occurrence order, then the negative of the first axis, then the remaining negatives in any order. There are at least (m-1)! canonical types. Thus the leading coefficient [s^m] s^(2m) pi^(1)_(2m)(0;d) grows at least factorially. This is a diagonal coefficient across different polynomials, not a lower bound on the coefficients of their full sum or on a_n; signed falling-factorial corrections can cancel it.

## Citation audit

Important version difference found: Graham's **published** result is Theorem **1.3**, equation (1.3), journal p. **2**, and the coefficient bound is Lemma **5.1**. In the arXiv version they are Theorem **1.1** (p. 2) and Lemma **4.1** (p. 5). Publisher-PDF text indexed by web search also independently lists all 13 alpha coefficients in equation (1.2), p. 2, exactly matching the computed reciprocal series. The final report must keep the two numberings separate. The arXiv PDF itself has a later typesetting date on its title page despite the v1 identifier; this is not evidence of a new summability theorem.

## Final audit — 2026-11-13 06:51:19 +0400

REPORT.md completed with first line exactly PARTIAL. The SAW zero-radius conjecture remains unresolved in this work. The report contains three fully stated and proved partial results, explicit cancellation limits, coefficient/Borel diagnostics, exact source-version locators, and access limitations. Published Graham Theorem 1.3 was distinguished from arXiv Theorem 1.1. No invented theorem locator for inaccessible Hara–Slade or Gerber–Fisher full text.

All three numerical scripts rerun successfully after the final code change. Exact SRW coefficients were checked independently by occupied-axis enumeration; reciprocal SAW coefficients by a second recurrence and the published list; fixed-memory quotient counts by literal paths. Peak RSS values were 15,679,488 / 14,647,296 / 14,499,840 bytes; each script ran in under 0.05 seconds, one thread. os.getpriority independently measured niceness 15 (at least as polite as the requested nice 10).

Artifact checks: sources/ contains only .txt files; no PDFs or page images anywhere in this directory. No subagents, publication, commits or pushes. Shared mesh/checklist/memory writes were unavailable and intentionally not bypassed. All results remain in the task directory.

Task done: “Open problem C0097” — received 13 November 2026, 06:34 +04. Result: PARTIAL, with rigorous analogues and reproducible coefficient audit; no proof for SAW.
