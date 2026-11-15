# C0034 work log

Task received: 2026-11-13, approximately 10:07 Asia/Tbilisi (06:07 UTC), "Open problem C0034".
Scope: literature first, rigorous special cases, exact rational transportation certificates and adversarial search. No publication or pushes. Work confined to this directory; no subagents.

## 2026-11-13 10:10 +04

- Read the two prior brain cards on C0034. They provide numerical feasibility evidence and explicitly no proof. One old card calls floating LP results "exact" in its body; that wording is not evidence of rational certificates.
- Compute governor: warn / owner_away_open, substantial existing load. All our numerical commands will use nice 10 and one BLAS/OpenMP thread (at most four total), with small matrices.
- Attempted required mesh hello; failed with "attempt to write a readonly database". No mesh claim can be acquired in this sandbox. Later task instruction limits writes to this directory; task/checklist and durable-memory notes are kept here instead of writing outside it.
- Original survey located at https://arxiv.org/abs/1406.2707 and author mirror https://rdlyons.pages.iu.edu/pdf/icm.pdf. Literature checking in progress.

## 2026-11-13 10:13 +04 — literature finding

- Downloaded arXiv:1406.2707 and read all of Section 2 (pp. 2–8), using pdftotext without rendering or saving page images. All saved source payloads are text and JSON provenance.
- Read Lyons (2003), Section 10. Important prior-art correction: Lemma 10.4 already proves the finite-rank rank-one difference assertion; Proposition 10.3 extends the coupling to infinite-dimensional nested spaces. Lyons explicitly notes that duality settles all |E| <= 5. The requested rank-one special case is known, not a new theorem of this run.
- Møller–O'Reilly, arXiv:1806.07347, Lemma 1 repeats the finite-rank singleton-difference result in the continuous setting. Their Theorem 1 concerns reduced Palm measures.
- Kassel–Lévy (2022), Proposition 5.15 is monotone coupling of determinantal linear processes, not a union-marginal splitting theorem.
- Bufetov–Qiu–Shamov (2021), Theorem 1.4 is the Lyons–Peres completeness conjecture; Theorem 1.6 concerns tails. Neither is Question 2.8.
- Lyons' ICM errata dated 30 Dec 2025 reports resolutions of tail triviality, and clarifies the completeness conjecture, but gives no resolution of Question 2.8. This absence is not a proof of openness.
- Process priority is already nice 15, more yielding than the requested nice 10. The attempted nice wrapper was refused by the sandbox; numerical code will assert inherited priority >= 10. One numeric thread will be used.

## 2026-11-13 10:16 +04 — special cases saved

- Saved data/special_cases.md with a constructive weighted-Hall/max-flow proof from exterior minors for rank one, a countable-E extension, three-color complement symmetry, codimension one, and closure under independent coordinate blocks.
- These existence special cases follow from known Lyons 2003 results. No claim of novelty.
- Found a simple exact failure of arbitrary composition on four coordinates using the rational Hadamard matrix: both successive couplings are valid, but the resulting two-point first color has masses 1/2,1/2 instead of the required four masses 1/4. A standalone exact check is being saved.
- Literature phase complete: no full resolution located. The later Poinas (2026) paper constructs marked/attractive couplings; its Proposition 4.1 splits by pointwise thinning and does not imply the prescribed subspace-union law. Search scope and limitations saved in sources/SEARCH.md. Proceeding to exact certificates.

## 2026-11-13 10:22 +04 — exact certificates and adversarial search

- Generated 288 certificate files (286 distinct (Q, column-set-1, column-set-2) instances; two overlaps between the suites). Suite 1: 168 instances, every p,q>=1 with p+q<=n, three rational orthogonal matrices at each n=2,...,7 (two Cayley, one product of rational Givens rotations). Suite 2: every exceptional column allocation modulo color permutation for one fixed Cayley matrix, 15 allocations of (2,2,2) at n=6 and 105 of (2,2,3) at n=7.
- HiGHS only proposes a vertex support. Fraction-free integer solves reconstruct exact rational masses, then every marginal row and nonnegativity is checked exactly. No rational approximation to a floating mass is accepted on tolerance.
- Independent code/verify_certificates.py uses only Python Fraction and Gaussian elimination on principal projection-kernel minors, not squared basis minors and not the producer. It verified all 288 certificates and 14,772 marginal equalities. Peak resident memory: producer 116,277,248 bytes (~111 MiB), independent verifier 19,087,360 bytes (~18 MiB). Nice 15; numeric libraries and HiGHS explicitly use one thread.
- Implemented exact Edmonds–Karp rank-one construction: data/rank_one_flow.json, 19 augmentations and 19 positive masses; saves the conditional q_e laws. Independently checked with kernel minors.
- Implemented 32 targeted Grassmannian searches: n=6,7, both real and complex Cayley charts, eight starts per shape/field; 23,742 fixed-dual objective evaluations. Each search uses an exactly feasible rational Farkas functional and minimizes it on the orthogonal/unitary group. Full min-L1 phase-I LPs are also evaluated. No positive violation above numerical error; no counterexample.
- Positive control is deliberately inconsistent with the subspace-sum hypothesis: singleton laws delta_{0}, delta_{1}, union delta_{0,2}. Exact Farkas vector has nonnegative column pairings and rhs pairing -1; numerical min-L1 residual 2. This tests the detector but is not a C0034 counterexample.
- Sandbox rejects both RLIMIT_AS and RLIMIT_DATA updates. Matrices are tiny, peak RSS is measured and guarded below 3 GiB; all observed peaks are under 0.12 GB. No worker or subagent was started.

## 2026-11-13 — final audit

- REPORT.md now starts exactly PARTIAL and contains the full special-case proof, explicit composition failure, literature distinctions, exact certificate method and counts, numerical limitations, resources and reproduction commands.
- Re-ran both independent verifiers and the exact composition check after finishing the report. All passed: 288 certificates / 14,772 exact marginal equalities; 4,800 exact search-dual inequalities; exact artificial Farkas pairing -1; exact rank-one flow; all composition-stage marginals correct and composed marginal demonstrably wrong.
- Recounted certificate identities separately: 286 distinct, two duplicates between suites. Rechecked every local report link and all source file suffixes; sources contains text/JSON/Markdown only.
- Final verifier peak RSS 20,316,160 bytes; adversarial run 114,376,704 bytes; certificate producer 116,277,248 bytes. All ran at inherited nice 15, with explicit single-thread numerical settings.
- Saved data/brain_note.md as a local durable-learning handoff; no shared brain or checklist writes were possible/authorized outside this directory. No full theorem or C0034 counterexample is claimed.

Task complete as an investigation: “Open problem C0034”, received 13 November 2026 approximately 10:07 Asia/Tbilisi. Outcome PARTIAL.
