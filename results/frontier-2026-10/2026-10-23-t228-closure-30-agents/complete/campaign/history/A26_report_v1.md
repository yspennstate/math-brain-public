# A26 — reproducibility, version provenance, and package integrity audit

Audit date: 23 October 2026. Reviewer: A26. No subagents or remote writes. Only A26-owned files were created or edited. The parent recovered source bytes and maintained the campaign ledgers.

**Verdict: the tested current mathematical evidence and local provenance checks pass; final campaign packaging remains pending.** This is an integrity and reproducibility audit, not a proof-assistant verification, a new independent review of every analytic argument, or verification of remote branch ancestry. The preserved partial T336 and conditional T421 results remain partial and conditional.

## Exact tested state

The binding machine-readable snapshots are `campaign/checks/A26_current_verification.json`, `A26_proof_verification.json`, and `A26_optimized_verification.json`. Each records the verifier's SHA-256, Python version, UTC time, all individual checks, and the source-pin calculations.

| Run | UTC on 2026-10-23 | PASS | WARN | PENDING | FAIL |
|---|---|---:|---:|---:|---:|
| Current bundle and roster | 19:35:52.845380 | 234 | 5 | 2 | 0 |
| Proof/evidence mode | 19:36:01.136585 | 202 | 5 | 1 | 0 |
| Proof/evidence mode under `python -O` | 19:36:00.172394 | 202 | 5 | 1 | 0 |

The exact executable used for these runs is `campaign/checks/A26_verify_bundle.py`, SHA-256 `35951404ba5d315688b04f4dd0ead0785e761e3e791d9c02352f217fd30f9961`.

At the current-run snapshot, `campaign/AGENT_ROSTER.json` had **30 distinct task names and agent numbers, but only 28 completed entries**. Agents 26 and 30 were still pending. Every completed entry's report path and SHA-256 were checked. No final package manifest was supplied to this run. This report therefore does not assert that all 30 agents had completed or that the final package had already passed a manifest check. The obsolete 18-entry in-progress roster is retained as history and is superseded when the final roster exists. Requested model/effort metadata is not independent verification of the backend runtime model.

## Proof bytes and reproducible evidence

The verifier pins all five current T228 proof files: the explicit zero-teacher closure, nonzero-teacher theorem, index dependence, moment dynamics, and batch-two theorem. It also checks the A16 TeX/PDF/source hashes, the A18 reviewed-proof hashes, A03's local source manifest, and the relevant current/historical A02 manifest entries. Markdown tables binding review reports to exact file hashes are checked against the named current file or an explicitly identified preserved historical version.

The A08 rational checker was executed on exact temporary copies of its script and frozen reviewed source using an isolated, nonoptimized Python process. Its **37 checks**, stdout, generated `.out`, and preserved author output reproduced byte-for-byte. The author directory was not used as the execution output location. This verifies its finite polynomial/Fraction calculations; it does not mechanically formalize its separate analytic assumptions.

The A13 accepted JSON and the A24 full replay JSON have valid strict endpoint signs when read as exact rational numbers. The verifier checks the bracket exponents, interval ordering, inclusion of stated quadrature and tail allowances, calibration containing `h_1(2)=2`, mesh/precision metadata, and source/script provenance. **A26 did not repeat the expensive quadrature.** A24's full replay and separate analytic audit are preserved, and the numerical brackets remain supplementary to the analytic theorem.

`campaign/checks/A24_optimized_falsepass.json` is **INVALID HISTORICAL NEGATIVE-TEST EVIDENCE**, despite its internal `"status": "PASS"`. All six endpoint intervals fail to certify the required signs; A26 independently rejects all six. It must never be counted as an accepted numerical certificate. The original A13 script is retained at `campaign/history/A13_tail_index_certificate_v1.py`; the historical accepted JSON correctly pins that original script. The current executable has a different hash because it rejects optimized execution before computation.

A26 tested the current A13 executable with `-O`, `-OO`, and `PYTHONOPTIMIZE=1`, supplying a nonexistent proof path and a temporary output path. Every run failed with the explicit optimization-guard error before reading the proof, and produced no certificate. The A26 verifier itself has no assertion-based verification gates and gives the same evidence disposition under ordinary and optimized Python.

## Source pins and exact registry semantics

All **19 A01 private Brain source files** match their recorded Git blob SHA-1 over the exact raw bytes. Their embedded source payloads agree with the recovered files and cover the same 19 unique paths. Git blob hashes are computed as `SHA1(b"blob " + decimal_byte_length + NUL + exact_bytes)`; they are not plain file SHA-1 hashes.

The complete local registry has SHA-256 `c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0` and **422 unique problem IDs**. Its recorded Git blob `b8d4607e60eafcce5b3e8286cf882e8931737bd6` is reproduced by removing **exactly one terminal LF byte** for the comparison. No source file is rewritten or broadly stripped of whitespace. The full parsed T228, T336, and T421 objects equal their respective local extracts; all selected registry rows and the literal A18 statement/title/audit-route fields agree. Duplicate JSON keys and non-finite JSON constants are rejected.

The source audit originally found six side-study copies that did not match their recorded Git pins, even after removing one LF. `campaign/checks/A26_source_pin_mismatches.json` preserves that discovery state. The parent then recovered the exact originals separately and recorded `campaign/SOURCE_PIN_RECOVERY.json`. A26 positively verified every recovery: the recovered file matches the recorded Git blob and SHA-256; replacing its CRLF sequences with LF and then appending exactly one LF reproduces the preserved local copy byte-for-byte. Thus these six discrepancies are explained line-ending transformations, not unexplained content substitutions. The original local copies and recovered originals both remain preserved. The discovery file's initial unresolved status is historical and is superseded by the recovery ledger and the later A26 run.

## Version provenance and deliberate omissions

`campaign/CORRECTIONS.json` binds both reviewed and current versions for the A02 continuity wording, A05 fixed-coefficient qualification, A06 `beta1=0.9` specialization and claim ledger, and A13 optimization guard. The verifier checks those file hashes. For example, A21's old T421 proof hash resolves to its preserved historical file; it is not silently treated as the current proof hash.

Five warning events describe two deliberate archival qualifications:

1. A07, A08, and A09 each refer to the initial explicit-proof draft with hash `9d0ef065e10642dbc8967870bdc3f368300424659f9316456355775264133287`. Those exact draft bytes were not retained. The correction ledger explicitly states this, pins the current complete Version 2, and disclaims a dependency on the missing draft. A26 does not reconstruct or claim to have verified the missing bytes. The three warnings are three references to one missing historical draft, not three current proof gaps.
2. A28 records a third-party Mirek PDF and its extracted text by original URL and evidence hash. They are expressly external references rather than bundled authored work. `campaign/EXTERNAL_REFERENCES.json` records this choice, and separately permits the T421 primary-paper HTML cache to be omitted from the final package. A26 checks the declarations, not the absent cache bytes. A final run on a package omitting that HTML may therefore have additional warning events without a mathematical defect.

These warnings do not authorize omission of current authored proofs, reports, code, results, or private Brain sources. `campaign/checks/A26_required_files.json` records **173 required paths** at A26 handoff, including T336/T421 partial results and preserved history. Final-manifest coverage uses both this baseline and every additional substantive file actually present under `campaign` and `a01`–`a06`. Python caches and TeX auxiliary/log files are not required. No private email material is needed for this verifier or the mathematical package.

## Verifier self-review and use

`campaign/checks/A26_selftest.py` passed **22 tests**, including under optimized Python. The preserved result is `campaign/checks/A26_selftest.json`. The tests cover altered hashes and lengths, omission of a partial result, duplicate manifest entries, duplicate agent names/numbers, incomplete-roster detection, duplicate JSON keys, non-finite constants, absolute/traversal/noncanonical paths, symlink escape, source mutation, manifest/output self-reference, and rejection of all six false-pass signs. The synthetic fixtures do not represent completed real agents. All verification and test failure gates use explicit conditions and exceptions.

Current or proof-only checks can be rerun as follows:

```bash
python campaign/checks/A26_verify_bundle.py current
python campaign/checks/A26_verify_bundle.py proof
python -O campaign/checks/A26_selftest.py
```

For the finished package, assuming it is staged at `bundle/` with a manifest whose paths are relative to that directory:

```bash
python campaign/checks/A26_verify_bundle.py \
  --root bundle --manifest MANIFEST.json \
  --output /tmp/A26-final-verification.json
```

The manifest schema is `{"files":[{"path":"relative/path","sha256":"...","bytes":123}]}`. A path-to-hash map under `files` is also accepted. The manifest must omit itself and this run's live output. Writing the final audit output outside the package avoids a manifest cycle. The prefinal A26 run snapshots should remain immutable evidence of the state actually tested here.

Without `--manifest`, exit zero may mean `PASS_WITH_GAPS`; the JSON explicitly lists what remains pending. With `--manifest`, any failure or unresolved pending item produces exit one. That strict mode requires all 30 distinct agents to have completed status and exact report hashes, validates every manifest entry and byte count, checks preservation coverage, and detects inputs that change during the audit. Explicitly declared historical/external omissions remain visible warnings rather than false hash matches.

**Handoff:** the current local evidence is reproducible at the stated scope. The parent must mark A26/A30 completed only after their final messages, regenerate the final manifest after all report bytes settle, and run strict manifest verification. No claim that those final steps have already occurred is made here.
