# Independent referee log: C0159

Task: “Break it if it is wrong.” Received 13 November 2026, approximately 08:37 Asia/Tbilisi.

## 08:38 — orientation and scope

Read the supplied instructions, startup identity memory, compute state (ok), claim REPORT and LOG, and mesh protocol. Work is restricted to this directory by the present task, overriding older instructions to mutate the global mesh, checklist, or brain. This log is the task record. No subagents, publication, pushes, or outside writes. Processes inherit nice 10; calculations will be sequential with thread limits set to one. Downloaded PDFs will be converted through pipes in memory, never saved.

Initial review finds the five-step proof structurally plausible. Main audit targets: independence and two-terminal reduction for infinite branches, least-fixed-point justification, exact cutsets, sprinkling direction, and prior results for tree-like/hyperbolic graphs. Claim code will not be used or copied.

## 08:41–08:43 — primary-source and exact checks

Downloaded and extracted BCRTT v1/v2, Timár (neighboring and nonunimodular papers), HPS, Tang, Hutchcroft (hyperbolic and nonunimodular), Terlov–Timár, Špakulová, Ménard–Sénizergues, the Häggström–Jonasson survey, and Peres–Pete–Scolnicov. URLs and hashes are recorded in the text headers. No PDF was saved. BCRTT v2 Question 1.1 remains explicitly open; Lemma 3.5 uses precisely right-continuity from above.

Fresh standard-library code passed 15 rational cone checks and 9 rational finite-core checks by complete configuration enumeration versus separate connectivity-partition elimination. Three buffered structural checks (b=2,3,4) verified degree, common neighbours, cone attachments, exact boundary, and spacing-3 disjointness. An initial structural-test loop reached an unbuffered top vertex; corrected the test margin, not the mathematical formula. Nine in-cone Monte Carlo comparisons (three pairs, three p values, 5000 samples each) all agreed within 1.40 standard errors. Maximum bottom truncation bias from the exact formula was 1.41e-5. Full-graph comparisons with a long ancestor core are next.

No fatal mathematical defect found. Fixed-point ambiguity is removed either by uniqueness or explicitly by increasing finite-depth reliabilities r_0=p, r_(d+1)=1-(1-p)(1-p*r_d)^b. Literature already contains the same scalar equation after x=1-pr (Ménard–Sénizergues equation (7)); no target finite-cardinality theorem located so far.

## 08:46 — full graph and literature conclusions

Full-graph comparisons finished: a 180-ancestor core, six generations below each off-core child, 23,424 vertices, 46,845 edges, 2000 configurations per p=.22,.32,.42. All three estimates agree within 0.75 standard errors. The analytic omitted-ancestor bounds are 5.67e-13, 4.24e-7, and 6.59e-4; integrated finite-branch biases are 2.45e-5, 1.74e-4, and 1.93e-4. Runtime 63.13 s, peak RSS 70,565,888 bytes, nice 10, one thread. A separate rerun after making sample ordering deterministic regenerated the in-cone results and hashes.

Read Peres–Pete–Scolnicov Note 2.4 (spatial exponential decay for decorated trees), Hutchcroft hyperbolic Theorems 1.3/1.4/2.1, Tang Theorems 1.1/1.3/2.9, and Terlov–Timár Theorem 1.8 plus GP example. None is a theorem asserting the target all-p two-point continuity or finite-cardinality touching on GP. The same cone scalar equation is printed by Ménard–Sénizergues equation (7), and GP decomposition into pieces of border size two is already in Špakulová Section 5.3. Correctness is accepted; novelty remains unconfirmed.

## 08:50 — final audit

REPORT.md begins ACCEPT. Checked its table against JSON outputs; re-derived all three ancestor error bounds using exact Fraction powers, and verified output code hashes against the final independent scripts. The deterministic final in-cone rerun has maximum |z|=2.392 (the earlier exploratory ordering had 1.390); all full-graph |z|<.750. Added three primary-source cross-checks (Hermon–Hutchcroft and two Hutchcroft–Pan papers), bringing the total to sixteen paper texts. Regenerated the source index. All source files are UTF-8 .txt, with no NUL bytes; recursively checked this folder for PDF signatures and PDF/image suffixes and found none. No publication, pushes, global writes, or subagents.

Verdict: ACCEPT for the fixed-p GP_b class theorem. No mathematical errors or unresolved proof gaps found; no novelty certification. General C0159 remains open in the checked literature. Task: “Break it if it is wrong.” — received 13 November 2026, approximately 08:37 Asia/Tbilisi.
