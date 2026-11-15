# C0159 work log

Task received: 13 November 2026, approximately 08:07 Asia/Tbilisi (04:07 UTC).
Task: “Open problem C0159” — cluster repulsion beyond unimodularity.

## 2026-11-13 approximately 08:09 Asia/Tbilisi — orientation and literature first

- Read the supplied instructions, relevant brain identity/relationship memories, and compute state (ok, owner away).
- No subagents, publication, git operations, or external writes. The task-specific instruction to work only here overrides global requests to update the shared mesh/checklist/brain; this log is the local task record.
- All paper files will be plain extracted text. PDF responses may be decoded in memory; no PDF or page image will be written to disk.
- Initial primary-source search located Häggström–Jonasson, Timár, HPS, and arXiv:2509.10631.
- Important version check: arXiv lists BCRTT v2, revised 4 November 2026. Search excerpts state finite weight for touching sets of any two infinite clusters, not only two heavy clusters. Must read and compare versions before drawing conclusions.
- Survey pagination check: cluster-repulsion paragraph closes Section 5, immediately before Section 6, on printed pp. 308–309 / PDF pp. 20–21.

## 2026-11-13 approximately 08:14 Asia/Tbilisi — literature corrections and a class proof

- Saved and read the survey's repulsion passage and all of Section 6; saved Timár's neighboring-clusters paper and read its proof, including the finite modification argument and final mass transport.
- Saved BCRTT v1 and v2; checked Theorem 1.2 in both, v2 Lemma 3.5, Theorem 3.8, and the two proofs. The v1 heavy-heavy statement and v2 all-infinite-clusters statement have the same substantive content because a subset of a light cluster is light.
- Crucial correction: heavy and infinite light clusters do not coexist at fixed p. HPS Theorem 1.8 in the author manuscript (cited as book Theorem 4.1.6), explicitly applied on manuscript p. 27; Tang Theorem 2.9, arXiv PDF p. 9, repeats this consequence. The heavy-light case in the question is therefore vacuous for the stipulated Bernoulli model.
- Saved Hutchcroft 2020, Tang 2019, Timár's other 2006 paper, and Terlov–Timár 2025. Search also located Ménard–Sénizergues arXiv:2611.09762, submitted 6 November 2026, on grandparent percolation thresholds. Its scope must be checked before any novelty claim.
- No full resolution located. BCRTT v2, dated 4 November 2026, explicitly says its Question 1.1 remains open.
- Candidate independent class proof: for a b-ary descendant cone plus its parent, terminal reliability r satisfies r=1-(1-p)(1-pr)^b. This equation has a unique solution for 0<p<1. Finite ancestor cores plus finitely many such two-terminal networks should give continuous two-point functions. Independent all-closed cutsets of size b+2 toward the distinguished end give a uniform error bound for this reduction. Then sprinkling gives finite touching sets.
- Resource check: processes inherit nice 10. An initial attempt to add another 10 was refused by the sandbox; corrected the helper to preserve the inherited priority. Computation remains sequential and single-threaded.

## 2026-11-13 08:19 Asia/Tbilisi — proof and computation checked

- The grandparent-graph proof works: cone terminal reliability has a unique fixed point, finite core reliabilities are continuous, and independent upward closed cutsets give uniform approximation on every compact p-interval below 1. The sprinkling argument then proves finite touching sets for every fixed p on every regular grandparent graph.
- This is a result for a natural nonunimodular class, not a resolution of the general conjecture and not a claim of novelty. HPS already records p_h=p_u=1 for grandparent graphs; thus the nontrivial cluster regime here consists of light clusters.
- Exact finite audits passed: 9 terminal-network reliability checks (including complete enumeration of 8192 configurations), 3 separate two-terminal-core checks, and boundary enumeration for b=2,3,4. Rational arithmetic was used for the reliability comparisons.
- Ran 108 finite-cone samples (depths 10,12,14; p=.55,.65,.75; 12 seeds), all in an infinite-graph nonuniqueness regime verified independently using the underlying binary tree and disjoint isolated cones. Maximum graph: 32767 vertices, 65530 edges. Runtime 1.419 seconds, peak RSS 49,250,304 bytes, nice 10, one thread.
- Saved aggregate and per-pair adjacencies, contacts by level, and pairs selected at the smallest depth and followed through larger windows. The 16 selected pairs stayed distinct in all three windows with unchanged adjacency counts in this run. The maximum pair adjacency anywhere was 14. These are finite observations, not inferred infinite-cluster identities.
- Forward searching found two primary-source citations of BCRTT: Tserunyan–Tucker-Drob (arXiv:2512.24741v2, 26 October 2026) and Higgins–Spaas–Tenenbaum (arXiv:2602.05185). Their relevant discussion concerns measured graphs, not a resolution of cardinality repulsion.
- Replaced problematic font extraction for two sources with piped pdftotext; PDFs remain memory-only. Removed extraction NULs so source files are plain UTF-8 text.
- Corrected initial clock labels after checking both local time and UTC explicitly; the machine's displayed 08:xx clock is Asia/Tbilisi, not UTC.

## 2026-11-13 final audit

- REPORT.md now contains the full class theorem, all five proof steps, the precise unresolved general cases, and a literature table with theorem and page locators.
- Independently recomputed all 36 depth-10 samples by breadth-first search, rather than the simulation's union-find: all component and contact summaries and 396 level counts agree. All 48 tracked-pair rows also agree with their separate level files.
- Checked original source headers and corrected the Špakulová journal range to 2262–2296; verified Tang Theorem 1.1 on saved PDF p. 2, Lyons–Schramm Theorem 3.3 on printed p. 1815 / PDF p. 7, and the Higgins forward citation on p. 42.
- Read Hermon–Hutchcroft Section 5.1, saved PDF p. 28, to check why continuity of the two-point function cannot be assumed for a general graph.
- Added explicit depth-14 contacts-by-level counts to the report; raw counts remain in data/.

Completed: PARTIAL. All 9 summary-table rows and 15 level-table rows were checked against raw CSVs. The source index records 20 paper texts (2,249,292 bytes); all sources are UTF-8 .txt files, and the recursive artifact check found no PDF or image files. Code, data, source texts, REPORT.md, and LOG.md are saved locally. No publication or pushes.
