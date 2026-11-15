# Independent referee log: I0003

Started 2026-11-13 at 21:34 Asia/Tbilisi (17:34 UTC).
Task: “You are an independent referee … Break it if it is wrong.”

Constraints: all deliverables and mutations confined to this directory; no
subagents, publication, pushes, retained PDFs, or page images. Sources will be
retrieved independently, not copied from claim_files/sources. Calculations use
one thread, inherited low scheduling priority, and small memory.

Read the supplied report and log, consulted startup memory and relevant brain
recall, and read the compute governor state. No relevant proof memory was found.
Global mesh/checklist/memory writes are excluded by the task's stricter
“work only in this directory” instruction; this log is the task record.

Initial audit: the positive-lambda resolvent identity has the correct sign.
Need independently verify all estimates, especially the circulating field and
Bosi's mixed-model hypotheses. First source metadata independently verified:
Ahmed Bou-Rabee and Yuval Peres, The randomly oriented Manhattan lattice in 2D
is transient, arXiv:2609.07621v1, submitted 7 September 2026.

21:41. Independently downloaded the source paper, Gaudillière–Landim, Bosi's
thesis, Campanino–Petritis (both papers), three Brémont papers, both
Guillotin-Plantard–Le Ny papers (functional paper obtained), Pène 2009,
Devulder–Pène, Castell et al., Ledger–Tóth–Valkó, Bosi–Hu–Peres, and the
2025–2026 works named in the submission. Source hashes, retrieval timestamps,
and failures are in sources/MANIFEST.txt. PDF bytes were converted in memory.
The arXiv dynamic-orientation paper returned HTTP 500 twice; obtaining the
authoritative mp_arc copy instead. Pène's survey publisher returned HTTP 403.

By-hand checks: A is a two-sided quadratic-form comparison with constants
independent of lambda and the site. B's annular estimate is valid: the number
of edges between square radii k and k+1 is 8k+4; summing through a dyadic
annulus gives exactly 12*4^m. C's radial dipoles and energy constants check
including radius one; all other tail arrangements reduce to a constant
sequence or a saddle. Bosi Appendix A, Theorem 9(i),(iii), has the precise
mixed Manhattan hypotheses required by D and E. No uncountable probability
intersection is needed in D.

Literature searches used the exact paper titles and combinations of
“Manhattan lattice”, “bounded stream”, “primitive”, “deterministic”,
“circulating”, “clockwise”, “recurrence”, and 2024/2025/2026. Relevant primary
hits were retrieved; mirror/rotor/sandpile models were not conflated with the
two-outgoing-edge Markov walk. No counterexample to A–E found so far.

21:45. Independent checks in code/check_audit.py passed: 24 positive-lambda
matrix checks across eight fields and their bounded-primitive perturbations;
30 exact rational face/curl identities; 24 exact rational circulating profiles;
dyadic edge counts; exact unwrapped C1 return-word counts to time 64. Matrix
identity error <2.25e-14; variational optimum error <8.0e-15. Initial NumPy
matrix multiplication emitted floating-status warnings despite finite accurate
answers; replaced matrix multiplications by explicit einsum and reran cleanly.
Checks used one numerical thread, nice 20, and about 32 MB peak RSS.

The attempted finite-change counterexample flips vertical lines -1 and 0 in
the saddle field. This creates a directed four-cycle and positive four-step
return probability, but A still gives transience. Thus local cycles do not
break the finite-whole-line-change clause.

An independent arXiv API query for Manhattan/math.PR submissions in 2024–2026
returned the Bou-Rabee–Peres and Nguyen papers and two unrelated papers.
The XML response is saved as plain text. The separately identified continuum,
mirror, and iterated-scenery works were also retrieved. Pène 2020's corrected
publisher PDF URL also returns 403; this access limit remains explicit.

21:56. REPORT.md completed with verdict ACCEPT for the partial claim. No
mathematical defect found in A–E. It includes the exact source question,
statewise recurrence and time-reversal checks, a complete equation-by-equation
audit, the explicit recurrent convergent-series example, the uniform event in
D, and verification of the sparse-defect maximal-inequality argument in E.
Literature finding: bounded-stream recurrence and Bosi's base/sparse results
are predecessors; the general comparison, unbounded criterion, tail
classification and simultaneous extension were not located as stated in the
inspected corpus. Priority remains qualified, especially with two declared
full-text access limits. The general open problem is not solved.

Final archive: 24 independently retrieved paper texts, five arXiv metadata
texts, and two arXiv query responses. All 31 successful retrieval hashes verify.
Five failed retrieval attempts are retained in the manifest. sources/INDEX.txt
records URLs, page counts, version stamps and hashes. No PDF or image is kept.
The final independent checks pass without warnings (matrix identity error
2.2426505097428162e-14; variational error 7.993605777301127e-15).
The final check process used one numerical thread, nice 20, and 31,178,752
bytes peak RSS. audit_snapshot.json pins the supplied artifacts and archive
counts. No supplied claim file was edited.

Task done: “You are an independent referee … Break it if it is wrong.” —
13 November 2026, about 21:34 Asia/Tbilisi (session start).
