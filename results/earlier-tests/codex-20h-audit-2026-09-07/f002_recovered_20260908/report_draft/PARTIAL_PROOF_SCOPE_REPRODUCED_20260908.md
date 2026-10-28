```audit-report
{
  "schema": "audit-report-v2",
  "finding_id": "MB20-F002",
  "title": "Recovered source objects reproduce a proof-scope admission defect; original report evidence remains lost",
  "classification": "CONFIRMED GATE/REPORTING DEFECT",
  "severity": "HIGH",
  "state": "OPEN",
  "audited_at": "2026-09-08T11:34:19.601873+00:00",
  "audit_started_at": "2026-09-08T07:22:41+00:00",
  "audit_deadline": "2026-09-08T12:22:41+00:00",
  "mandate_status": "ACTIVE",
  "owner_stop_evidence": [],
  "auditor": "codex-math-retrieval-5h-20260908",
  "responsible_agent": "UNKNOWN",
  "mutation_boundary": {
    "mode": "AUDIT_ONLY",
    "audited_target_write_count": 0,
    "evidence": [
      {
        "subject": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\build_report_draft.py",
        "source_type": "MUTABLE_TARGET",
        "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\report_draft\\MUTATION_LOG.json",
        "sha256": "e38a1589ac6f049ffef46153ad1b6236ce60ecf2742e21feea754308ae1d1f1c",
        "observed_at": "2026-09-08T11:34:19.601873+00:00",
        "locator": "Isolated recovery write boundary",
        "kind": "MUTATION_LOG"
      }
    ],
    "owner_authorization_evidence": []
  },
  "snapshots": [
    {
      "subject": "<HOME>\\.codex/sessions/<ROLLOUT>",
      "source_type": "MUTABLE_TARGET",
      "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\recovered03\\proofs.jsonl.captured-row.json",
      "sha256": "b7bbf2aed2fed64bc1dd18c7aa4593ecb91358a58c114c16a245a9066a628171",
      "observed_at": "2026-09-08T11:34:19.601873+00:00",
      "locator": "Transcript record 8691; first complete printed JSON object; historical proofs.jsonl line 2701. Object recovery only, not original archive bytes.",
      "kind": "SOURCE_SNAPSHOT"
    },
    {
      "subject": "<HOME>\\.codex/sessions/<ROLLOUT>",
      "source_type": "MUTABLE_TARGET",
      "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\recovered03\\proofs_v2.jsonl.captured-row.json",
      "sha256": "af8b2122d953ad4739bc71633dc06a0533c8784c319df0f430b286aec6803f74",
      "observed_at": "2026-09-08T11:34:19.601873+00:00",
      "locator": "Transcript record 8691; second complete printed JSON object; historical proofs_v2.jsonl line 2701. Object recovery only.",
      "kind": "SOURCE_SNAPSHOT"
    },
    {
      "subject": "<HOME>\\.codex/sessions/<ROLLOUT>",
      "source_type": "MUTABLE_TARGET",
      "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\recovered03\\RECOVERY.json",
      "sha256": "51305cbc1edfd5247f7a4dfb92f0e08e1c179efda714883d1110af90a46265d0",
      "observed_at": "2026-09-08T11:34:19.601873+00:00",
      "locator": "Exact transcript path, one-based record indices, timestamps, normalized complete-record hashes, earlier old-row agreement and fresh eight-control reproduction.",
      "kind": "SOURCE_SNAPSHOT"
    },
    {
      "subject": "https://arxiv.org/html/2608.23135v1#S1.Thmdfn3",
      "source_type": "IMMUTABLE_SOURCE",
      "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\primary_theorem_fragment.html",
      "sha256": "ccb640eeb4dd67d5ed90641849361e12061d375af01943bdaa21b33ae2a6650a",
      "observed_at": "2026-09-08T11:34:19.601873+00:00",
      "locator": "Fresh HTML DOM serialization of exact theorem element; a bounded source fragment, not a complete paper copy.",
      "kind": "SOURCE_SNAPSHOT"
    },
    {
      "subject": "https://arxiv.org/html/2608.23135v1#S3.5",
      "source_type": "IMMUTABLE_SOURCE",
      "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\primary_proof_fragment.html",
      "sha256": "e29bc085e74ee08b7e5883567227d222676ae56701c234992a7cba0945d67066",
      "observed_at": "2026-09-08T11:34:19.601873+00:00",
      "locator": "Fresh HTML DOM serialization of the dimension-four proof; bounded source fragment.",
      "kind": "SOURCE_SNAPSHOT"
    },
    {
      "subject": "https://arxiv.org/html/2608.23135v1",
      "source_type": "IMMUTABLE_SOURCE",
      "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\PRIMARY_SCOPE_CHECK.json",
      "sha256": "67341f52bf4ba3ff17b05b01f5ce12b8f792445a2c4f9b9d330483a75bb5198c",
      "observed_at": "2026-09-08T11:34:19.601873+00:00",
      "locator": "Independent direct HTML scope oracle, element hashes, complete-response hash and read-limit disclosure.",
      "kind": "SOURCE_SNAPSHOT"
    },
    {
      "subject": "<HOME>\\.codex-worktrees\\math-brain-20h-20260907\\bank_baseline\\extract_proofs.py",
      "source_type": "MUTABLE_TARGET",
      "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\recovered03\\extract_proofs.frozen.py",
      "sha256": "26df4ed150f1cca2523addcc8e4ad2abfd8847c858c917a4853bd3f58937152f",
      "observed_at": "2026-09-08T11:34:19.601873+00:00",
      "locator": "Existing frozen extractor matches original baseline hash; no original live extractor restoration.",
      "kind": "SOURCE_SNAPSHOT"
    },
    {
      "subject": "<HOME>\\.codex-worktrees\\math-brain-20h-20260907\\heading_scope_guard.py",
      "source_type": "MUTABLE_TARGET",
      "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\recovered03\\heading_scope_guard.py",
      "sha256": "8746cd1890e64d33f378fa047fbd4c0fe19ad511e37010692ff91b6c0d7df710",
      "observed_at": "2026-09-08T11:34:19.601873+00:00",
      "locator": "Root-authored isolated review guard reused only for the stated controls.",
      "kind": "SOURCE_SNAPSHOT"
    },
    {
      "subject": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\primary_source_2608.23135v1.html",
      "source_type": "MUTABLE_TARGET",
      "evidence": "<HOME>\\.codex-worktrees\\math-brain-5h-retrieval-20260908\\f002_recovery\\PRIVATE_WEB_RESPONSE_SCAN_FINDING.json",
      "sha256": "f77ae2ab557760d73551e61f0adbf8d779642cf29892686625d4ec6ae2fb6eec",
      "observed_at": "2026-09-08T11:34:19.601873+00:00",
      "locator": "Private full-response scan exclusion, not publication approval or credential-rotation evidence.",
      "kind": "SOURCE_SNAPSHOT"
    }
  ],
  "notification": {
    "required": true,
    "send": {
      "status": "PENDING",
      "receipt_id": null,
      "occurred_at": null,
      "evidence": []
    },
    "delivery": {
      "status": "PENDING",
      "receipt_id": null,
      "occurred_at": null,
      "evidence": []
    },
    "acknowledgement": {
      "status": "PENDING",
      "receipt_id": null,
      "occurred_at": null,
      "evidence": []
    }
  },
  "model_identity": {
    "runtime": "CODEX_CLI",
    "requested_model": null,
    "served_model": null,
    "status": "UNVERIFIABLE",
    "response_evidence": []
  },
  "correction": {
    "required": true,
    "status": "IN_PROGRESS",
    "snapshots": []
  },
  "reaudit": {
    "required": true,
    "status": "PENDING",
    "audited_at": null,
    "auditor": null,
    "test": null,
    "evidence": []
  },
  "refutation": {
    "status": "NOT_APPLICABLE",
    "test": null,
    "evidence": []
  },
  "human_review": {
    "status": "PENDING",
    "reviewer": null,
    "reviewed_at": null,
    "checklist": {
      "governing_prompt_and_scope": false,
      "evidence_semantics_and_provenance": false,
      "mutation_boundary": false,
      "notification_delivery_and_ack": false,
      "model_identity": false,
      "mandate_timing_and_owner_stop": false,
      "counter_case_and_impact": false,
      "disclosure_safety": false
    },
    "limitations": [
      "Deterministic validation cannot prove semantic evidence closure."
    ]
  }
}
```

## Scope

This is a freshly dated reproduction of MB20-F002, staged for root review and canonical
promotion. The five-hour math-brain readiness mandate began at 07:22:41 UTC and remains
active until 12:22:41 UTC; this does not terminate the parent twenty-hour mandate.

The old PARTIAL_PROOF_SCOPE.md binding referred to SHA-256
7113814b6188046a7c30586151525f89a4d3c3aa044521722cf0764fceddc22f.
Those report bytes, its original selected-row snapshots and the full proof archives
have not been recovered. This report proposes to supersede the missing binding with
new evidence, while preserving the old evidence-loss history. It is not a byte-identical
restoration and must never be labeled with the old hash.

## Pinned evidence

The authorized native transcript is
`<HOME>/.codex/sessions/<ROLLOUT>`.
Its one-based record 8691, timestamp 2026-09-08T03:06:30.816Z, has normalized complete-line
SHA-256 aed598506b8da3bc6723c4fe3a270aa4387e95f22ff1532677894f765fd68702.
It contains the two complete selected row objects, printed from proofs.jsonl and
proofs_v2.jsonl at historical archive line 2701 in each.

Record 8152, timestamp 2026-09-08T02:09:10.589Z, has normalized complete-line SHA-256
04b3e77541511cda086d37cbf6887e21d110b35f7d79a14901fb9e1a3f28550d.
That earlier separately captured object equals the old row exactly. The newer row differs
only by its added proof_opt field. These are two captures by the original investigator,
not two independent mathematical reviewers. The hashes cover complete transcript lines
after universal-newline decoding; the private tool envelopes are not copied or published.

The original capture command parsed each archive line and printed JSON with a 7,800-character
cap. Both recovered strings are complete parseable objects below that cap. This recovers
object content, not the original archive whitespace, newline bytes or full-archive hashes.
Fresh public-source DOM fragments and the unchanged frozen extractor provide distinct
corroboration. The full downloaded HTML had three key-like scanner matches and remains
private; only separately scanned theorem/proof fragments are proposed for publication.

## Reproduction

The content digest 2dc1a24f5f9372bc independently recomputes from the statement and steps
using the frozen extractor's normalization. Both captured archive objects mark the row
accepted. Their statements and three proof steps agree exactly. The statement includes
dimensions four and five; the supplied proof explicitly finishes only dimension four.
The v2 heading identifies the same restriction. The original heading predicate does not
flag it; the isolated candidate returns QUALIFIED_HEADING_REQUIRES_SCOPE_REVIEW.

The fresh public paper confirms the scope directly: Theorem 1.3 covers both dimensions,
while the selected proof element S3.5 is explicitly for dimension four. The paper discusses
the five-dimensional case elsewhere, including an appendix sketch. This is an observation
about the packaged excerpt, not an accusation that the paper's theorem is false.
Source: https://arxiv.org/html/2608.23135v1#S1.Thmdfn3 and
https://arxiv.org/html/2608.23135v1#S3.5.

Eight controls pass: old-row capture agreement, recomputed digest, changed-statement
digest mismatch, original qualifier miss, candidate review routing, missing-heading
withholding, ordinary empty-heading preservation, and a matching qualified statement
still being routed only to review. The last control is a counter-case: the heading guard
does not itself determine whether a statement and proof have matching mathematical scope.

## Impact

The recovered historical extraction admits a proof excerpt narrower than its paired
claim. Such packaging can make a later first-error exercise ambiguous independently
of any subsequent mutation. One observed occurrence does not establish prevalence,
an accuracy gain, a score adjustment, or the correctness of either historical model answer.
No keys, solver answers, current thirty-five-item inputs or locked evaluation prompts
were read for this recovery. The actual historical full corpus remains unavailable.

## Strongest counter-case

A restricted proof heading is appropriate when the paired claim has the same restriction.
Successful extraction or a heading flag alone cannot establish mathematical invalidity.
Here the specific statement includes two dimensions and the actual selected proof ends
in one. Arguments elsewhere in the paper do not add steps to this packaged excerpt.
The fresh source confirms this narrow discrepancy; it does not justify rejecting every
qualified proof or changing benchmark keys automatically.

## Required correction

Root should review and promote this newly dated evidence, create a new report-bound
occurrence node that supersedes the missing binding, and retain the unrecovered-original
status. The old row objects must not be installed as fabricated complete archives.
Future admission must preserve heading and notation, compare supplied proof scope with
the statement, and review missing or qualified metadata before presenting a complete-proof
task. This recovery did not change a live extractor or certify production correction.

## Re-audit criteria

Replay the two captured objects and direct source-fragment checks against the pinned bytes.
Independently inspect matching restricted claims as negatives and broader claims paired
with restricted proofs as positives. Verify production callers use any eventual admission
repair. Corpus-level claims require the missing full archives or a separately documented
new corpus. Root must rerun report validation after path promotion, then use the registrar
for real node binding, BM25/salience/graph and analogous recall/reflex controls. No fake
node hash or passed retrieval certificate is provided by this draft.

## Recurrence prevention

Reuse [[gate_incomplete_is_not_a_pass_2026_07_16]] and compiled reflex
green_names_what_it_checked: a screen does not certify an unexamined dimension.
Link the recovered occurrence to the existing mutation-bank mechanism
[[mutation_bank_items_keyed_flawed_but_effectively_clean_2026_09_06]]. Preserve the earlier
occurrence audit_partial_proof_scope_recurrence_2026_09_08 through explicit supersession.
The sidecar supplied here is a registration draft, not an authoritative audit-node binding.

## Human semantic review

Pending. This recovery investigator independently read transcript objects and fresh
primary-source fragments, but reused the root-authored heading guard. No whole-proof
verification, independent production re-audit or human closure is claimed. Formal
notification receipts are pending; parent chat delivery is not fabricated into that ledger.
The report remains OPEN. Own brain self-care remains degraded/unverified for correction
ingestion and stale orientation coverage; this packet does not certify credential rotation.
Initial parser and capture-label mistakes were caught by assertions, corrected explicitly,
and preserved with the scan exclusions in the recovery packet.
