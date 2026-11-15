# T095 continuation log

Task: “take the NEXT checkable step on this problem, building on that work.” First clock reading: 2026-11-14 20:52:17 UTC (2026-11-15 00:52:17 Asia/Tbilisi).

## Step 1 — orientation and earlier artifacts

Read the startup memory index and compute state, then the earlier folder's REPORT.md, LOG.md, and VERIFY.md using `OMP_NUM_THREADS=1 nice -n 15 python3` with pathlib reads. The earlier folder has no PROOF.md and no Python scripts. Its saved sources are the three introduction sections and differentiability endpoints.tex. The earlier claim is Gamma differentiability only, with the arbitrary-endpoint reduction checked conditionally on its inputs.

All writes stay here: the task-specific instruction excludes brain/checklist/mesh commands that mutate other folders. No git or subagents. Compute state is warn/owner_away_open, so only small text reads and web requests are planned. The sandbox reports `nice: setpriority: Operation not permitted`; the tiny reads nevertheless finish immediately. No heavy program is launched.

Next: a five-minute-bounded search for subsequent literature; independently compare actual theorem text and inspect the earlier endpoint reduction; choose one adjacent input to check rather than repeat the same reduction.

## Step 2 — bounded update search and independent scope check

Used web search on the exact shape title with November/error, first-passage differentiability with continuous/OpenAI/2026, GammaPassage/error, and first-passage differentiability after 2026-11-13. Results locate the same Gamma claim, catalogues, and the already noted rotationally invariant FPP paper; no new full continuous-law theorem or specific refutation was located in this bounded pass. Search snippets are leads, not mathematical evidence. A GitHub read-only fetch independently reopened the actual introduction: its two theorem blocks agree with the earlier saved source and restrict the laws to exponential and Gamma. The scope conclusion holds: e.g. Uniform[1,2] satisfies T095 but is outside these statements.

Re-read the earlier endpoint spot check and its complete saved source. A first extraction command failed harmlessly with `ValueError: substring not found` because the heading was different; the corrected read succeeded. Opened the section directory and recent commit metadata next. Chosen extension: check the characteristic-length/change-of-measure input that the earlier endpoint check explicitly left conditional, including its quantifiers and its scale selection. This is the adjacent unverified input rather than another check of the same endpoint attachments.

## Step 3 — source inputs for the chosen check

Read-only GitHub tools opened `differentiability/scales.tex`, `preliminaries.tex`, and `crossings.tex` at commit `4eaee87548250b2682affda7d05d947c05554bae`. Recent-commit search returns that same October 30 snapshot, so no repository change since the earlier report was found. Reopened both other candidates' introduction sections and `lean/docs/212.md`; their scope is unchanged. Opened Scott Armstrong and Ahmed Bou-Rabee's arXiv:2610.42124 abstract and full HTML: it is a continuum fluctuation theorem, and its introduction calls the exponential shape result an announcement. It is not a proof of full T095. The update search is now closed within five minutes; no SOLVED_ELSEWHERE.md is warranted.

The chosen section's inputs are explicit: rare-fast crossings (`df:cr:rare-fast`) and local travel (`df:cr:local-travel`), plus the fixed Gamma model and supporting functionals. Plan for the check: derive the finite-product likelihood second moment twice, check the deterministic tilt implication and edge count, prove the uniform short-crossing assertion including bounded lengths, then verify the record-scale comparison used in the earlier endpoint proof. Any conclusion will retain the two crossing inputs as hypotheses.

## Step 4 — source preservation and provisional report

Saved the actual reopened theorem introductions, all three input sections, the Lean scope note, the Gamma Comparator target, and the actual final Gamma proof as local `source-*` files using apply_patch. The three main TeX entry files name OpenAI as author and give September 24, September 24, and September 25, 2026 respectively. Gamma Comparator target quantifies only over positive Gamma shape/rate, with actual passage-time definitions; its `sorry` is the challenge placeholder. The final solution file calls `CrossingBridge.gamma_no_corner` and the time-constant/boundary-chart input theorem. No Lean compilation was attempted.

Saved REPORT.md now with the continuation verdict format requested in the later instructions. Its claim is a conditional verification of a reduction, not a new differentiability theorem. Exact main theorem quotations are retained for the forthcoming VERIFY.md.

## Step 5 — conditional derivation written

Wrote PROOF.md with the deterministic scaling implication, the density-ratio integral, a second calculation via the Gamma sum's Laplace transform, the finite-region edge bound, Cauchy–Schwarz, the uniform short-crossing argument, and record minima. The load-bearing scale is Mδ² = O(ns)·O(s²/n²) = O(s³/n), bounded at n = s³. The constants re-derive as 144ns edges, exponent 288κη₀² for the second moment, and exponent 144κη₀² after Cauchy–Schwarz. No shape estimate for the changed law is used.

Checked potential exceptions explicitly: κ < 1, repeated edge traversals versus distinct likelihood coordinates, bounded crossing lengths, negative b, nonmonotone first-threshold probabilities, terminal mesh l=1, and the order of fixed parameters versus scale limits. The two crossing inputs are still assumptions in this derivation. This is the new piece beyond the earlier endpoint-only conditional check.

## Step 6 — earlier endpoint conclusion independently re-derived; checking reports reopened

Re-derived the earlier attachment bound using the exact tail identity `sum_{j>=J} j^2 2^{-j} = 2^{1-J}(J^2+2J+3)`. Two attachments therefore cost at most `64 C1 s 2^{-J}(J^2+2J+3) + 2 max|a_sigma|`, which is arbitrarily small relative to s by fixing large J and then taking k large. Nonnegative costs give `Delta x >= -2R max|a_sigma| s/m0` for a negative-defect path; the two attachments add at least 2l_J, so the extended span exceeds l_J eventually. At fixed J, coarse-column pairs are O(2^{8J}), independent of k. The probability error is a convergent Gaussian-in-j tail after the 2^{5j} grid count. This confirms the earlier conditional endpoint conclusion, while leaving its crossing inputs conditional.

Reopened the primary MathVet fidelity table at commit `14c7f918cd336d0da03a02aae5a0eed4a429d4db` and Carlos Toledo/cert-machine statement audit at `9814e4c06281e34a113ce853d7d99ccce160b750`: both identify Gamma differentiability as the selected conclusion, with strict convexity and no-bigeodesics outside the selected targets. Reopened `history.md` at the OpenAI snapshot: it has no FPP repair or withdrawal notice. These are scope/checking records, not endorsement of the full proofs.

## Step 7 — VERIFY.md and exact audit

Wrote VERIFY.md with all four exact theorem blocks from the three actual preprints, the clause-by-clause comparison, reopened follow-ups, independent endpoint recheck, new conditional spot check, and a three-sentence status recommendation. Saved `audit.py`; command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py`.

Output (exit 0):

```text
nice: setpriority: Operation not permitted
OMP_NUM_THREADS=1
Process nice value: 20
Sources unchanged; all four exact theorem blocks present: PASS
Exact Gamma integral checks: 36 PASS
Explicit internal-edge enumeration: 30 cases PASS
Largest enumerated M/(ns): 115 (bound 144)
Attachment-tail identities: 50 exact checks PASS
Report format, three-sentence status, local links: PASS
```

The process is already at nice 20, lower scheduling priority than requested, despite the wrapper's warning. The audit uses only the standard library, exact rational arithmetic, at most 12,545 vertices per enumerated region, and a 30-second alarm; it finished immediately. The 36 integer-shape Gamma integrations and 30 finite sheared-grid counts are checks against transcription/constants, not proofs of all parameter cases. The all-parameter arguments are in PROOF.md. The 50 exact geometric-tail checks independently support the earlier endpoint bound.

No numerical or mathematical counterexample was found. The remaining uncertainty is explicit: rare-fast crossings and localized travel are inputs, the rest of the manuscript is unchecked, and selected Lean targets were read without a build. No write outside this folder, git command, post, account creation, subagent, heavy compute, or GPU use occurred.

## Step 8 — final report audit

Finalized REPORT.md in the continuation verdict format, adding the exact audit command, what is new, the remaining hypotheses, and the next lemma to inspect. Re-ran `OMP_NUM_THREADS=1 nice -n 15 python3 audit.py` after that edit; exit 0 with the same full PASS output. Deliverables are REPORT.md, VERIFY.md, PROOF.md, audit.py, this log, and the preserved source files. The verdict is PARTIAL for a conditional verification of the characteristic-length reduction, with the original claim-scope finding still Gamma-only. The mathematical reduction is verified only under the stated two crossing inputs; no full theorem is endorsed.
