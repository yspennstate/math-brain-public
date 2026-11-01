"""Write a fresh, explicitly unregistered F002 reproduction; never forge old bytes."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    out = HERE / 'report_draft'
    out.mkdir(exist_ok=False)
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    mutation = out / 'MUTATION_LOG.json'
    mutation.write_text(json.dumps({
        'as_of': now, 'audited_target_writes': 0, 'canonical_writes': 0,
        'scope': 'Recovery-only isolated snapshots, controls and fresh report drafting. No source archive, production extractor, key, solver answer, score, live node, or index mutation.',
        'history': 'Root authored the earlier candidate guard; this recovery investigator reused it and independently checked exact primary HTML elements. No whole-proof or independent production correction closure is claimed.',
    }, indent=2)+'\n', encoding='utf-8')
    contract = (Path.home()/'.codex/skills/audit-agent-fleet/references/report-contract.md').read_text(encoding='utf-8')
    metadata = json.loads(re.search(r'```audit-report\n(.*?)\n```', contract, re.S).group(1))
    metadata.update({
        'finding_id': 'MB20-F002',
        'title': 'Recovered source objects reproduce a proof-scope admission defect; original report evidence remains lost',
        'classification': 'CONFIRMED GATE/REPORTING DEFECT', 'severity': 'HIGH', 'state': 'OPEN',
        'audited_at': now, 'audit_started_at': '2026-09-08T07:22:41+00:00',
        'audit_deadline': '2026-09-08T12:22:41+00:00', 'mandate_status': 'ACTIVE',
        'auditor': 'codex-math-retrieval-5h-20260908', 'responsible_agent': 'UNKNOWN',
    })
    def pin(subject, evidence, locator, kind='SOURCE_SNAPSHOT', source_type='MUTABLE_TARGET'):
        return {'subject': subject, 'source_type': source_type, 'evidence': str(evidence),
                'sha256': sha(evidence.read_bytes()), 'observed_at': now,
                'locator': locator, 'kind': kind}
    transcript = str(Path.home()/'.codex/sessions/<ROLLOUT>')
    root = HERE.parent.parent/'math-brain-20h-20260907'
    metadata['snapshots'] = [
        pin(transcript, HERE/'recovered03/proofs.jsonl.captured-row.json', 'Transcript record 8691; first complete printed JSON object; historical proofs.jsonl line 2701. Object recovery only, not original archive bytes.'),
        pin(transcript, HERE/'recovered03/proofs_v2.jsonl.captured-row.json', 'Transcript record 8691; second complete printed JSON object; historical proofs_v2.jsonl line 2701. Object recovery only.'),
        pin(transcript, HERE/'recovered03/RECOVERY.json', 'Exact transcript path, one-based record indices, timestamps, normalized complete-record hashes, earlier old-row agreement and fresh eight-control reproduction.'),
        pin('https://arxiv.org/html/2608.23135v1#S1.Thmdfn3', HERE/'primary_theorem_fragment.html', 'Fresh HTML DOM serialization of exact theorem element; a bounded source fragment, not a complete paper copy.', source_type='IMMUTABLE_SOURCE'),
        pin('https://arxiv.org/html/2608.23135v1#S3.5', HERE/'primary_proof_fragment.html', 'Fresh HTML DOM serialization of the dimension-four proof; bounded source fragment.', source_type='IMMUTABLE_SOURCE'),
        pin('https://arxiv.org/html/2608.23135v1', HERE/'PRIMARY_SCOPE_CHECK.json', 'Independent direct HTML scope oracle, element hashes, complete-response hash and read-limit disclosure.', source_type='IMMUTABLE_SOURCE'),
        pin(str(root/'bank_baseline/extract_proofs.py'), HERE/'recovered03/extract_proofs.frozen.py', 'Existing frozen extractor matches original baseline hash; no original live extractor restoration.'),
        pin(str(root/'heading_scope_guard.py'), HERE/'recovered03/heading_scope_guard.py', 'Root-authored isolated review guard reused only for the stated controls.'),
        pin(str(HERE/'primary_source_2608.23135v1.html'), HERE/'PRIVATE_WEB_RESPONSE_SCAN_FINDING.json', 'Private full-response scan exclusion, not publication approval or credential-rotation evidence.'),
    ]
    metadata['mutation_boundary']['evidence'] = [pin(str(Path(__file__)), mutation, 'Isolated recovery write boundary', 'MUTATION_LOG')]
    metadata['notification']['required'] = True
    for field in ('send', 'delivery', 'acknowledgement'):
        metadata['notification'][field] = {'status': 'PENDING', 'receipt_id': None, 'occurred_at': None, 'evidence': []}
    metadata['model_identity'] = {'runtime': 'CODEX_CLI', 'requested_model': None, 'served_model': None, 'status': 'UNVERIFIABLE', 'response_evidence': []}
    metadata['correction'] = {'required': True, 'status': 'IN_PROGRESS', 'snapshots': []}
    metadata['reaudit'].update({'required': True, 'status': 'PENDING'})
    body = '''
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
'''
    report = out/'PARTIAL_PROOF_SCOPE_REPRODUCED_20260908.md'
    report.write_text('```audit-report\n'+json.dumps(metadata, indent=2)+'\n```\n'+body, encoding='utf-8')
    draft = {
        'schema': 'audit-node-link-DRAFT-NOT-REGISTERED', 'finding_id': 'MB20-F002',
        'report_path': str(report), 'report_sha256': sha(report.read_bytes()),
        'node_slug': 'audit_partial_proof_scope_recovered_2026_09_08',
        'node_path': None, 'node_sha256': None,
        'supersedes': 'audit_partial_proof_scope_recurrence_2026_09_08',
        'mechanism_node_slug': 'gate_incomplete_is_not_a_pass_2026_07_16',
        'reflex_id': 'green_names_what_it_checked',
        'fire_queries': ['An extracted argument covers only one case but the paired claim asks for both cases.',
                         'A screening check passed while an important part of the claimed scope was never examined.'],
        'recall_top_n': 8,
        'positive_fire_controls': ['The gate passed and we called every case checked, although one case was never inspected.',
                                   'A validation success was treated as complete coverage even though the scope was incomplete.'],
        'negative_fire_controls': ['A partial check is explicitly labeled as partial and the remaining cases are still pending.',
                                   'The argument and the claim are both restricted to the same dimension.'],
        'status': 'DRAFT_ONLY_ROOT_MUST_REGISTER_AND_TEST',
        'note': 'Control wording is proposed, not measured against the existing reflex. Do not rename this file to an authoritative sidecar. Registrar must generate real node hashes and current paths after canonical promotion.',
    }
    (out/'PARTIAL_PROOF_SCOPE_REPRODUCED_20260908.audit-node.DRAFT.json').write_text(json.dumps(draft, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'report': str(report), 'sha256': sha(report.read_bytes()), 'sidecar': 'DRAFT_NOT_REGISTERED'}))


if __name__ == '__main__':
    main()
