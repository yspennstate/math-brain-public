# Independent referee log

Task: “You are an independent referee … Break it if it is wrong.” First local clock reading: 2026-11-13 09:17:20 +04.

## 09:18 +04 — scope and orientation

Read claim_files/REPORT.md and LOG.md, startup memory, compute state, and mesh protocol. The current directory-only instruction overrides global requests to mutate shared mesh/checklist/memory stores; no such registrations or writes will be made. No subagents, pushes, publication, or access to claim_files/code for implementation. Claim artifacts remain unchanged. Processes inherit nice 10; computations will set numerical libraries to one thread and remain below 4 GB. Source PDFs will be fetched into memory, converted through pdftotext pipes, and never written to disk. Plain-text source pages will preserve form feeds for page references.

Initial proof review finds no immediate failure in the branching construction or exponential-moment identity. Priority and exact quantifiers remain to be checked against downloaded sources.

## 09:20 +04 — source and proof audit

Downloaded arXiv:2608.19145v1 (22 pages) and 2209.03722v3 (15 pages), directly from arXiv, with PDF bytes held only in memory. Saved extracted text and SHA-256 manifests. Question 5.2 is on PDF/printed p. 20. It asks for a tight upper bound and makes no logarithmic conjecture for all close-to-regular graphs. CMW already notes polynomial examples on d-ary trees in footnote 7 there.

Checked (A) spectral bridge estimate, parameter feasibility, tensor-product spectrum, adaptive disjoint-edge coupling, Galton–Watson second moment, independent subtree amplification and exponent conversion. All pass. Checked (B), including the explicit tail and disjoint-cycle-path lower bound: pass. DEKK Theorem 2 is exactly the arbitrary-maximum-degree logarithmic upper bound, on PDF p. 3 of v3. Checked (C), including the root contribution and constants in the MGF induction: pass. Checked (D) supermartingale signs, terminal comparison, series (16), and fixed-parameter exponent (17): pass; the improvement needs a subunit exponent and is not a parameter-uniform claim.

Retrieved ABS, BBCR, Diskin–Krivelevich I and II, Nachmias–Peres random-regular and diameter/mixing papers, and DEKK irregular products, as text. Relevant theorems are being checked against their actual assumptions rather than titles. A guessed AFK author PDF URL returned 404; locating the linked original rather than relying on the claim's reference.

## 09:22 +04 — independent computations complete

New code code/independent_audit.py imports no claim code. Exact integer quotient characteristic polynomials and rational isolating intervals verify small spectra against full adjacency matrices and Kronecker blow-ups. Independent checks also cover the second-moment recurrence, resolvent sum across all R:a regimes, direct truncated MGF recursions, and 150 component calculations cross-checked with separate BFS.

Completed 720 realizations over 12 hosts, 60 each, up to 1,118,688 vertices. Edge retention uses Bin(E,p) followed by a uniform edge subset; this is exactly independent Bernoulli percolation. This differs from the claim's geometric sampler. Maximum RSS was 302,579,712 bytes; inherited nice 10, one numerical thread, wall time 6.83 seconds. Boundary cases take p=1/Delta, q=lambda/Delta and delta=Delta/lambda-1, so q(1+delta)=1 for every host; q is allowed to vary slightly between hosts and stays below 0.707. Fixed Delta=17 makes those particular boundary hosts logarithmic by the sharper non-backtracking maximum-degree comparison; the data cannot establish sharpness of the cubic-log bound.

## 09:30 +04 — completed review and final audit

Expanded the computation to add four growing-degree boundary blow-ups and two boundary hosts with Delta/lambda about 1.09. The final run has 18 hosts, 60 repetitions each, 1,080 realizations, maximum n=1,271,586, measured peak RSS 459,538,432 bytes, nice 10 and one numerical thread. Wall time was 11.65 seconds. Boundary equality error in floating arithmetic is at most 2.22e-16. The original 720-trial run is superseded by these final raw data and metadata.

Located AFK through the actual author publication link, CubeMatching.pdf, and converted it in memory. Its date is 27 August 2026; CMW appears in background on p. 2 and reference [7] on p. 10. No overlap with A/C/D. Semantic Scholar returns exactly this one citer; OpenAlex returns zero. Also inspected the September 2026 Krivelevich lecture notes (77 pages); their extracted text has no CMW citation or spectral/resolvent statement. No located exact antecedent of A's calibration/blow-up, C's uniform quantitative bound, or D's explicit refinement; no universal novelty certification inferred.

Wrote REPORT.md with first line MINOR. It gives the exact Question 5.2 on p. 20, numbered status/provenance/scope/sharpness revisions, a full independent proof audit of A–D, exact small-instance algebraic spectra, simulation evidence and limits, and the primary-literature comparisons. Mathematical results pass; honest research status PARTIAL; B is known; A/C/D are potentially new incremental refinements. Question 5.2 remains unresolved.

Final artifact check passed: all 18 files in sources/ are UTF-8 plain text, and no PDF, page image or scan exists anywhere in this directory. Mathematical inline delimiters were repaired and checked. No claim code was reused, no subagents were started, and no publication or push was made.

Task: “You are an independent referee … Break it if it is wrong.” — first local clock reading 2026-11-13 09:17:20 +04.
