# F0101 work log

Task: “Open problem F0101.” Session started 2026-11-13 at approximately 09:30 Asia/Tbilisi (05:30 UTC), from launcher file timestamps and retrieval UTC timestamps.

Constraints: work only in this directory; no publication or pushes; no subagents; at most four threads, under 4 GB, nice 10. Source documents are extracted to plain text; PDF bytes will only be handled in memory and never saved here.

2026-11-13 — Read startup memory index, mesh protocol and compute state (status ok). The task-specific instruction to work only in this directory and the filesystem sandbox prevent shared brain/checklist/mesh mutations outside it. Coordination and durable task records are therefore local to this folder; no shared state is changed.

Literature-first searches found Yuansi Chen, arXiv:2511.19374v2 (1 May 2026), giving (log log t)^(3/2)/(t sqrt(log t)) uniformly in dimension. This already implies the requested o(1/t). Later preprints: Xiang–Zhang arXiv:2606.04573v2 and Lu–Guo–Fang arXiv:2608.15515v1 claim improved rates. Full statements, exact pages, publication status and Talagrand source remain to be verified before final classification. No numerical search has been started, pending the requested literature stopping condition.

Source verification: Talagrand’s current Korea2b note, Section 6, PDF pp. 14–16, explicitly acknowledges the solution by Chen and Lu–Guo–Fang, with Shaposhnikov’s alternative proof. Shaposhnikov arXiv:2609.11290v2, Theorem 3.3, p. 7, gives sqrt((1+rho)/(1-rho))/(eta sqrt(log eta)). Its Boolean proof is on pp. 5–7. These are preprints; no journal venue is asserted. The stopping condition is treated as resolution in publicly available mathematical literature, with this distinction explicit.

The old prizes/prizes.pdf is dated 2012-08-18 in the author’s directory index, whereas convolution.pdf is dated 2016-03-12. The former is titled “How to make $7000,” not “Some open problems.” Its Section 4 spans PDF pp. 2–3 and matches the requested weak statement exactly. The saved basename will be corrected to avoid calling this particular PDF a 2016 edition.

All Python child processes inherit nice 10 (checked with os.getpriority); explicit nice -n 10 attempted to add another 10 and was denied by the sandbox, without changing the inherited value. Downloads are network waits, with at most four independent single-threaded extraction processes and sub-megabyte PDF buffers.

Checked theorem locations against page-marked text: Chen Theorem 1 p. 2; Xiang–Zhang Theorem 1.4 p. 5; Lu–Guo–Fang Theorem 1.1 p. 2; Shaposhnikov Theorem 3.3 p. 7. Gaussian: Lehec Theorem 2.1 printed p. 193 (PDF page 4 including cover), Theorem 2.3 p. 194; Eldan–Lee final author version Corollary 1.4 p. 5 has sqrt(log log t), unlike the older fourth-power loss quoted in Lehec’s abstract. Ball et al. author draft Theorem 4 p. 4 is dimension dependent.

Bibliographic corrections: “Dimensional improvements of the logarithmic Sobolev, Talagrand and Brascamp–Lieb inequalities” is by Bolley–Gentil–Guillin, not the five authors listed in the prompt. The Gozlan–Li–Madiman–Roberto–Samson paper is “Log-Hessian and Deviation Bounds for Markov Semi-Groups, and Regularization Effect in L1,” Potential Analysis 58 (2023), 123–158. Its abstract and introduction still identify the cube conjecture as open; its discrete process is M/M/infinity on N, not a dimension-free hypercube solution. Eldan–Lehec–Shenfeld concerns Gaussian log-Sobolev stability; Eldan–Kindler–Lifshitz–Minzer concerns cube isoperimetry, a different Talagrand conjecture.

Derived the finite-to-infinite passage independently using conditional expectations and L1 contraction; lower thresholds r<t address the strict/non-strict tail distinction without assuming an atom-free output. Checked the sharp logarithmic order a second way using normalized point masses and the binomial mass at k approximately n(1+a)/2. No extremizer search is needed under the requested literature stopping rule.

Final audit: code/audit_sources.py passed all 15 page/theorem-location checks across 17 source text files. Report has the required first line, intact LaTeX, and no unexpected control characters. No PDFs or image files exist in the folder. Sources retain URL, retrieval UTC time, received-byte hash and original PDF page count. The source audit also hashes the saved texts and final report. data/search_audit.json records representative literature searches and coverage limits. SSRN 7462079 returned HTTP 403; it was not used for a mathematical conclusion.

A report-writing shell string initially damaged LaTeX backslashes; the report was rewritten through a literal structured patch and audited for intact commands/control characters before completion.

Done: F0101 classified RESOLVED_IN_LITERATURE, with exact resolving theorems, an explicit phi and complete finite-to-infinite deduction, bias/endpoints, Gaussian history, bibliographic corrections and source provenance. Numerical experiments were not run because the literature stopping condition was reached. No shared checklist/mesh/brain writes or publication were performed.
