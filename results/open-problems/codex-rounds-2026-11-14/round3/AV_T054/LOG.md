# T054 continuation log

Task: “Verify: has open problem T054 been settled by the OpenAI math release?”
Session start observed: 2026-11-15 00:51 +04 (2026-11-14 20:51 UTC).

## Step 1 — earlier work and local restrictions

Read the earlier REPORT.md, LOG.md and VERIFY.md in `~/codex_op_1114/briefs/AV_T054`, and listed that directory. No PROOF.md or computation scripts are present. The earlier result is a statement comparison (bulk universality claimed, spatial QUE not stated), plus an algebraic check of the tensor-coercivity lemma. The report leaves the precise QUE formulation unresolved; VERIFY.md explicitly does not derive an exchangeability corollary from complete delocalization.

Commands: short reads/listings under `OMP_NUM_THREADS=1 nice -n 15`; startup-memory and compute-state reads. Compute state: `warn`, `owner_away_open`, CPU saturated; no heavy work is planned. `nice` prints `setpriority: Operation not permitted`, as in the earlier session; that session measured inherited niceness 20. A new priority check will confirm this before computation. `ps` is blocked by the sandbox. No git, subprocess workers, or writes outside this folder. Task-specific local-only instruction precludes shared mesh/checklist/brain writes.

Started the requested five-minute update search with web queries on fixed-degree QUE, the exact OpenAI GOE title plus errors/corrections, arXiv:2610.08127, and family-219 corrections. Results will be recorded after opening the sources.

## Step 2 — bounded update search and independent recheck

Completed the update search within five minutes. Opened: arXiv:2610.08127 abstract (still v1, October 6); Huang–Yau arXiv:2102.00963v3 full HTML, especially Theorem 1.4; Bauerschmidt–Huang–Yau arXiv:1609.09052 PDF, Corollary 1.3(ii) and its proof; current OpenAI `history.md`; the clean GOE introduction's raw TeX; and the community manuscript page. No later result settling an additional QUE formulation or changing the earlier report was identified. Repository history still ends October 29 with no named correction of family 219. Community page says no contributed notes and labels its collected notes unreviewed. No SOLVED_ELSEWHERE.md is warranted by this search.

The earlier main scope claim holds: freshly opened Theorem 1.1 has exactly the fixed-degree, fixed-energy Laplace-functional conclusion described in REPORT.md. Its quantifiers contain no spatial observable or QUE assertion. Independently read the original BHY Corollary 1.3(ii): deterministic, mean-zero, Euclidean-normalized tests, simultaneous over bulk eigenvectors and a prescribed finite test family; equation (1.7) is a polylogarithmic factor divided by N. Its proof applies exchangeability to squared eigenvector coordinates. Thus the earlier caveat that fixed-degree QUE is not wholly open also holds. This recheck verifies statement scope, not the GOE proof.

Priority check: `OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os,resource; ...'` printed niceness 20, OMP_NUM_THREADS 1, peak RSS 11,730,944 bytes. The warning is harmless inherited lower priority. No heavy computation is used.

## Step 3 — chosen extension (recorded before doing it)

Choose ONE extension: remove the unresolved degree-range caveat for deterministic bounded diagonal QUE by deriving a self-contained permutation-concentration corollary of the all-eigenvector delocalization theorem of Jiaoyang Huang and Horng-Tzer Yau. Their Theorem 1.4 covers every fixed d>=3, all eigenvectors, and polylog(N)/sqrt(N) coordinate bounds on a label-invariant high-probability event. The earlier VERIFY.md explicitly left this implication unproved. Address multiplicities by bounding eigenspace dimension and all entries of the observable compressed to each eigenspace; do not assume a simple spectrum or an equivariant chosen eigenbasis. The intended conclusion is for each prescribed deterministic bounded vertex observable, simultaneously for all unit eigenvectors, with probability tending to one. Graph-dependent tests and all tests at once are excluded.

Plan for independent checks: derive the permutation martingale increments explicitly; check its mean/variance by a separate exact permutation calculation; check the eigenspace dimension bound via projection diagonals; and exhibit a delocalized vector for which a vector-dependent test defeats any illicit uniformity over tests. The proof will be written in PROOF.md. This is an elementary consequence of published delocalization, not a validation of the OpenAI proof or a claim of a new literature theorem.

## Step 4 — proof and exact audit saved

Wrote PROOF.md and an initial REPORT.md before further verification. The proof gives, for permutation-invariant real symmetric matrices and all-eigenvector bound L/sqrt(N), a failure estimate `epsilon_N + 2 N^2 exp(-N s^2/(32 L^8))` for every prescribed mean-zero test in [-1,1]. It handles all vectors in repeated eigenspaces by the projection identity `m_lambda <= L^2` and an entrywise bound on the compressed observable. It then applies the actually opened Huang–Yau Theorem 1.4. This is the single extension selected in Step 3.

Wrote and ran `OMP_NUM_THREADS=1 nice -n 15 python3 audit_permutation.py`. Exact rational enumeration checks conditional expectations from all permutation completions independently of the displayed martingale formula, plus the variance identity, for flat, point-supported and signed weights, N=2,...,7. Output:

```
nice 20
OMP_NUM_THREADS 1
PASS cases=18 permutations=17736 prefix_checks=48207
PASS projection trace and adaptive-test obstruction N=4,6,8
peak_rss_bytes 19365888
elapsed_seconds 0.537
```

Examples: N=2 point-weight variance 1 and maximum increment 1; N=7 point-weight variance 4/9 and maximum increment 1; N=7 signed-weight variance 1928/64827 and maximum increment 13/49; all flat-weight variances and increments zero. These are finite algebra checks, not numerical evidence for the RRG theorem. The analytical proof rederives the exponential constant and logarithmic threshold independently.

## Step 5 — fresh candidate sources and formalization scope

Opened the Anderson introduction through web at the correct `build/sections/01-introduction.tex` path and through the read-only GitHub fetch connector. The attempted path without `01-` returned a cache miss. Opened Ising `build/sections/model.tex`, `lean/formalization.yaml`, and `lean/docs/218.md` through web. The Lean catalogue has no GOE or Ising-conformal title match; the 218 scope note is only a finite-graph likelihood comparison. Fetching the lean directory listings and current clean/Ising theorem sources next to make local snapshots and compare theorem environments exactly. Opened the repository Apache-2.0 LICENSE as well. No external mutation or git command was used.

Fresh clean GOE, Anderson and Ising theorem sources have now been saved here as `goe-theorem-source.tex`, `anderson-theorem-source.tex`, and `ising-theorem-source.tex`. GitHub fetch on a `blob/main/lean/...` directory URL returned INVALID_ARGUMENT; the corresponding `tree/main/lean` and `tree/main/lean/docs` URLs succeeded. Directory responses were larger than expected; only their filename inventories are needed. No Lean build was run. Reopening each candidate README to confirm metadata and any local correction notice before finalizing VERIFY.md.

## Step 6 — theorem comparison and row update saved

Each current README confirms author OpenAI and the supplied date, without a correction or withdrawal notice. Fresh lean/docs listing has 245 files, including 218.md and excluding 219.md; saved the filename inventory locally. Wrote VERIFY.md with all three exact theorem environments extracted directly from fresh source, comparison of every clause, the source register, and a revised three-sentence status. Quoted theorem lengths: clean GOE 385 characters, Anderson 800, Ising 1624. The report distinguishes an explicit release theorem from an inference using published results.

New status qualification: for prescribed deterministic bounded diagonal tests, the whole row is covered by bulk universality plus known delocalization and the elementary implication in PROOF.md. A stronger intended QUE statement remains unspecified; no blanket assertion that all fixed-degree QUE is open is retained. The implication is not presented as a novel theorem or an audit of the release. The counterexample in PROOF.md tests the illicit interchange of “each prescribed test” and “all tests on one event”; it is an abstract delocalized-vector example, not a constructed RRG eigenvector.

Final review independently checked all factors: 4b martingale increments, denominator 32Nb^2, at most N^2 compressed entries, eigenspace dimension at most L^2, final L^8 exponent, and tail 2N^(-D). Enumeration counts checked separately: 3*(2!+3!+4!+5!+6!+7!)=17,736. The projection step uses delocalization for all unit eigenvectors, as stated in Huang–Yau, and would fail if only a selected basis were known to be delocalized. The argument preserves the exceptional-graph probability and makes no claim of unconditional overwhelming probability.

## Step 7 — source audit and final report

Ran `OMP_NUM_THREADS=1 nice -n 15 python3 audit_sources.py`. All three quotations exactly equal both the fresh source theorem and the earlier worker's theorem; none changed. The saved Lean filename inventory has the expected 245 entries, 218 present and 219 absent. No control characters found in the deliverables. Process reported niceness 20, OMP_NUM_THREADS 1, peak RSS 16,318,464 bytes.

Finalized REPORT.md in the continuation format `VERDICT: PROVED ...`, explicitly limited to the proved delocalization-to-QUE implication and its application using Huang–Yau. Added the verification commands, failure of the stronger test-uniform conclusion, remaining ambiguity, and the next worker's concrete task. VERIFY.md retains a separate PARTIAL-CLAIMED assessment of the release's explicit main statement. PROOF.md contains the self-contained argument and independent checks. No external writes, git, accounts, subagents, GPU, MLX, torch, or large computations were used. All newly written files are inside this task folder.

After finalizing REPORT.md, reran the source audit to verify the changed report. All checks passed again; peak RSS 16,875,520 bytes. Final REPORT.md SHA-256: 416c1ef2faa79f6937c7c4dc6fa54c310436ab0dac3c0cfa171eec252aea684f; VERIFY.md: 57a914dd71389b3eb11c5aa65127fe0e27296634a08126d474e2d62955b9a8ed; PROOF.md: 1f5ac3cbe816719237c1753faab69a3f6ac9b7feb71ab976a935cd697b127792. Completion observed 2026-11-15 01:00 +04.
