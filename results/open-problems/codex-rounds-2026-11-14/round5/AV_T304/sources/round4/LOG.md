# T304 round 4 log

Task: “Verify: has open problem T304 been settled by the OpenAI math release?” Continuation requested 15 November 2026 (Asia/Tbilisi; exact request timestamp not exposed).

## Step 1 — orientation and inherited work

Read the startup memory index, compute governor state, and file inventories in both earlier folders. Read the first report and log, its full verification text, and requested the round 3 report, log, proof, and script. The first folder has no PROOF.md or scripts. The round 3 folder has audit_local.py.

Command: `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -I -B -c '<pathlib reads of memory, governor, and earlier folders>'`. The sandbox reports `nice: setpriority: Operation not permitted` but runs the short command. No simulation or compilation is planned; all local calculations will be tiny, single-threaded, and below 1 GB. Compute state: `warn`, `owner_away_open`, CPU saturated; no heavy work was started.

The current folder restriction overrides the general instructions to write brain, mesh, or checklist state outside this folder. Those scripts were not run, because even recalls can write logs. No subagents or git commands are used.

Started web searches for the sampling title, Zhou–Suzuki arXiv identifier, and OpenAI sampling error reports. Search leads include the already known proximal-sampling extension and the Zhou–Suzuki lower bound; leads are not treated as opened papers.

## Step 2 — bounded update search (completed by 04:29 +04)

Used the web search tool for the exact sampling title; Zhou/Suzuki/2611.05813; OpenAI sampling error/correction; log-concave sampling November 2026 optimal query; and paper 139 correction/error. Opened the current abstract pages https://arxiv.org/abs/2611.05813 (Huanjian Zhou, Taiji Suzuki), https://arxiv.org/abs/2611.03442 (Wei Guo, Bo Yuan, Ye He, Jiaming Liang, Molei Tao, Yongxin Chen), https://arxiv.org/abs/2611.15849 (Evan Dogariu), and repository history.md through the GitHub read connector. The arXiv pages still show v1 only; history.md still ends 29 October and records no change to the sampling candidate. No newly located matching sequential minimax bound changes the earlier picture. This bounded search is not a proof of absence.

Also opened https://news.ycombinator.com/item?id=50002650 after a search snippet mentioned retracted papers 139 and 140. It is an illustrative software-version comment, not a retraction notice; the linked primary history names three different withdrawn papers. No SOLVED_ELSEWHERE.md is warranted. Update search ended within five minutes of the first source search.

## Step 3 — prior proof read and extension selected

Read round 3 REPORT.md, LOG.md, PROOF.md, and all of audit_local.py, as well as the original implementation section and its main.tex input list. The recurrence's product-coupling argument requires independent complete supplying subtrees; the source explicitly duplicates these. The tier expansion counts one factor K per ancestor and one absolute-coefficient product per path, agreeing with the earlier formula. An independent exact-arithmetic recheck will be saved in this folder before the extension is concluded.

Choice: audit the structural coefficient and scale part of Theorem 6.2 (`thm:numerical-interface`, printed number to verify) and its use in the compiler. This is the single next step explicitly named by round 3. In particular, check the declared center coefficient A, output coefficient A_f, noise scale assignments, and the small factor lambda A. The numerical approximation and high-order analytic estimates will remain separate, unaudited inputs unless a concrete issue makes them necessary. Requested numerics.tex, centering.tex and preliminaries.tex from the original repository; all further source reads serve this one structural check.

## Step 4 — source snapshots and working derivation

Opened and saved the original numerics.tex and centering.tex, and opened preliminaries.tex (same original date as the inherited copy). Read the entire numerics.tex, including the exact numerical-interface theorem and its derivation. The coefficient assertion has c_1=10; its proof actually obtains delta^(-4t-w) in the center coefficient and delta^(-2w) direct size before enlarging those bounds. Picard state updates reset their additive direct term to the original starting state at each layer; they do not repeatedly substitute previous state sums. That reset is central to coefficient control.

Copied inherited source snapshots and VERIFY.md into this folder. The first one-line copy command had an unmatched bracket and exited before executing; corrected using a literal Python heredoc. No earlier file was edited. New source files numerics.tex and centering.tex were saved using apply_patch.

Working structural derivation: the kernel velocity retains only the forward integral correction, so its 1/(rs) prefactor cancels the correction's r. An expanded position has mean-coefficient norm bounded by the outer integration norm times the kernel norm plus at most three transport corrections. Multiplication by physical-center scale r gives O((r/sigma) delta^(-4t-w)+r^2), uniformly as r tends to zero. The exact algebra and independent checks will be in PROOF.md and audit_round4.py.

## Step 5 — independent recheck and new structural proof saved

The numerical-interface theorem is **Theorem 6.7**, not the provisional 6.2 in Step 3. Verified using the shared theorem counter in main.tex and the six preceding theorem-like environments in numerics.tex. Wrote PROOF.md, deriving the endpoint quadrature weight norm from a scaled Hermite basis, the exact forward-correction cancellation, local affine coefficient sums, direct-expression size/depth, scale lower bounds, normalized shift ratios, and descending compiler size labels. This audits parts (i)–(iii) and their compiler use; it does not audit the ideal-law errors in part (iv).

Independently rechecked the earlier recurrence by coupling centers before adjoining seeds, then multiplying complete independent occurrence couplings and expanding path weights. It holds under its stated hypotheses. New exact-arithmetic data check a different Gaussian completion and unequal ternary trees, rather than copying the earlier binary-tree calculation. The earlier shared-center counterexample is recovered as one member of a scalar family.

Command: `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -I -B audit_round4.py`.

Output (all assertions passed):
```
Inherited recheck: new Gaussian data; 33/32 and 73/72 by two methods; unequal ternary trees, heights 1..5: PASS
Hermite endpoint order 3: two exact constructions agree; unit weight l1=4
Hermite endpoint order 4: two exact constructions agree; unit weight l1=10
Hermite endpoint order 5: two exact constructions agree; unit weight l1=16
Hermite endpoint order 6: two exact constructions agree; unit weight l1=694/27
Hermite endpoint order 7: two exact constructions agree; unit weight l1=983/27
Hermite endpoint order 8: two exact constructions agree; unit weight l1=6698/125
Angle stencil orders 2..8 exact; coefficient cancellation at r=1, 10^-6, 10^-30: PASS
Scale square identities and lower bounds: PASS
Exponent checks: 63/128 > 1/3; label slack >3t, 8t, 9t; 1/3-1/4=1/12: PASS
```
The rational endpoint weights were obtained two independent ways: polynomial Hermite bases and monomial moment equations. Scale checks square identities instead of using rounded roots; variance checks use independent-seed coefficients and covariance cross terms. The 63/128 exponent is a convenient uniform lower threshold from K_0>=2 and t<1/640, not an asserted optimal exponent or query-complexity improvement. Runtime was negligible, standard library only. The sandbox again refused nice's priority change.

## Step 6 — current sources and reports

Reopened the three original introduction files and compared them to the inherited snapshots. Also reopened the sampling README, implementation, Lean scope note, preliminaries, numerics, centering and repository history. All ten texts agree after trailing-whitespace normalization; sources_manifest.json records their URLs, dates and comparison results. The sampled README carries no withdrawal notice. Current Lean scope still matches the fixed-error joint oracle statement; no compilation was attempted.

Preserved the round 3 PROOF.md and audit_local.py under sources/round3 and redirected inherited verification links there, so the earlier local proof remains reviewable alongside the new proof. Wrote the continuation-format REPORT.md and appended the round 4 Spot check to VERIFY.md. A first combined tool script failed to parse because an inline backtick appeared inside a JavaScript template literal; it performed no writes, and the corrected calls saved the reports.

The result extends the prior report by discharging its structural coefficient/scale inputs for the stated formulas. The analytic ideal-law accuracy estimates remain open to audit. Next check: Lemma 6.2's RMS angle and harmonic estimates and their derivative inputs. No full proof-correctness judgment is made.

## Step 7 — completion audit

Command: short standard-library pathlib/re/hashlib/json script, again under `nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -I -B -`.

Output:
```
Final audit: 3 exact theorem quotations; theorem numbering 6.7; 10 reopened sources; 3-sentence recommendation; local links and artifacts: PASS
Source snapshots: 29 total bytes: 302008
```

The audit re-extracted each main theorem from its original introduction and asserted verbatim inclusion in VERIFY.md; counted the shared theorem environments to confirm 6.7; checked all reopened text comparisons, report format, paired Markdown/math fences, three sentences in the recommended status, and every local Markdown target in the proof and verification. Added SHA-256 hashes and byte sizes for all saved source snapshots to sources_manifest.json. Preserved the prior manifest separately, so inherited blob-hash references remain accurate. Clarified which verification sections belong to round 3. Added the explicit polynomial unisolvence argument to the endpoint quadrature proof; it does not change the already checked arithmetic.

Final artifacts: REPORT.md, VERIFY.md, PROOF.md, audit_round4.py, LOG.md, sources_manifest.json and sources/. No outside-folder mutation, git command, publication, message, account creation, worker, GPU or heavy computation was used.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026; user request time not supplied, first logged clock reading 04:25:48 +04.
