# FEIB25 status
Started 2026-11-10. Task: edge form of FEI level by level, from the author's 9 Nov 22:20 ask to solve FEI.

Read fleet rules, brief, FLOW 7, 12(g), 12(p), 12(u), and the two requested code files. Read startup memory; recall found the erasure-equivalence note. Math recall reports no installed store. Fleet rule 3 requires all writes here and prohibits mesh posting; no shared checklist/brain mutations are made.

arXiv v2 HTML opened through web. Shell networking has no DNS. Journal metadata/abstract opened, full journal text is subscription-only. Existing NPN representative files and generation source found in ../FEIB13.

Exhaustive census generated locally and profiled for n<=5. Five-variable file has 616126 representatives. Level arrays saved in census_n*.npz, with exact integer W numerators. Independent Walsh/edge/pivotal tests pass on 96 random cases. Families and hill searches through n=16 are saved.

PROVED by direct construction: parity times selector-majority makes A_d unbounded at every fixed d with all W_0,...,W_d bounded. Therefore L1 and every dimension-independent lower-level-only repair are false. Draft details are being written in PROOFS.md.

DONE: all five brief tasks are covered in REPORT.md, PROOFS.md, PAPER.md and the saved data. FEI remains open. The main proved result is that no fixed lower-level-only linear weights can bound A_d at any fixed d. Elementary A_1/A_2 bounds and a full deduction of the known logarithmic edge bound from the paper's technical corollary are written.

The exhaustive census covers all 616368 NPN representatives across n<=5; independent direct/pivotal audits pass. Families, hill witnesses through n=16, analytic profiles and matching towers through n=6561 are saved. Tiny tower tails were recomputed at 40 and 50 decimal digits; all coefficients agree to relative error below 1.74e-37. The primary tower file is towers_decimal_50.json. The earlier binary64 towers.json is superseded.

Folder audit is in workspace_audit.json; primary artifacts total about 22.4 MB. No shared state was published. Full journal theorem comparison is inaccessible through the available subscription preview and is explicitly recorded as unverified.

NEXT: launching session should read REPORT.md and PROOFS.md, review the fixed-level counterexample and tail-payment proposal, and publish any durable result under its own authority. No worker computation remains pending.
