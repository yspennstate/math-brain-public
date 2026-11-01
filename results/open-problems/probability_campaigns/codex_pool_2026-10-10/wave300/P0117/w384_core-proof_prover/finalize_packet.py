"""Validate and checkpoint the authored review artifacts; no math experiments."""
from __future__ import annotations

import ast
import difflib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w384/bundle_001.json')
ALLOWED_RELATIONS = {'depends_on', 'defines', 'proves', 'refutes', 'generalizes',
                     'specializes', 'analogous_to', 'cites', 'semantic_association'}
ALLOWED_STATUS = {'conjecture', 'numerical evidence', 'sketch', 'proved special case',
                  'independently checked proof'}


def main():
    rows = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
    assert len(rows) == 9 and len({x['id'] for x in rows}) == 9
    for row in rows:
        assert row['status'] in ALLOWED_STATUS
        assert row['statement'] and row['source'] and row['proof_or_counterexample']
        assert row['independent_reviewer'] and row['remaining_gap']
    bundle = json.loads((ROOT / 'bundle_001.json').read_text(encoding='utf-8'))
    assert bundle == json.loads(INBOX.read_text(encoding='utf-8'))
    assert bundle['spec'] == 'mathbrain-draft-v1' and bundle['author_agent'] == 'w384'
    assert len(bundle['entries']) == 7
    keys = {x['key'] for x in bundle['entries']}
    assert len(keys) == 7
    for ent in bundle['entries']:
        assert all(k in ent for k in ['key', 'namespace', 'logical_name', 'kind', 'title',
                                     'statement', 'proof_text', 'assumptions', 'domain', 'source'])
        assert ent['kind'] in {'definition', 'concept'}
        assert ent['proof_text'] is None
        assert ent['source']['license'].startswith('owner-own-work')
        assert ent['statement'] and ent['assumptions']
    dependencies = {k: [] for k in keys}
    for rel in bundle['relations']:
        assert rel['from_key'] in keys and rel['kind'] in ALLOWED_RELATIONS and rel['rationale']
        assert rel.get('to_key') in keys or rel.get('to_existing_logical')
        if rel['kind'] == 'depends_on':
            dependencies[rel['from_key']].append(rel['to_key'])
    seen, active = set(), set()
    def visit(k):
        assert k not in active, 'cyclic depends_on'
        if k in seen:
            return
        active.add(k)
        for v in dependencies[k]:
            visit(v)
        active.remove(k)
        seen.add(k)
    for key in keys:
        visit(key)
    for name in ['verify_threshold.py', 'build_bundle.py', 'finalize_packet.py']:
        ast.parse((ROOT / name).read_text(encoding='utf-8'), filename=name)
    hook_path = ROOT / 'hooks_proposal_math-w384.jsonl'
    hook_text = hook_path.read_text(encoding='utf-8')
    hook = json.loads(hook_text)
    assert len(hook['text']) <= 300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
    hook_diff = ''.join(difflib.unified_diff([], hook_text.splitlines(keepends=True),
                     fromfile='/dev/null',
                     tofile='b/~/primary_directive/hooks1000/proposals/math-w384.jsonl'))
    (ROOT / 'patches' / '02_math_scope_hook.diff').write_text(hook_diff, encoding='utf-8')
    validation = dict(status='PASS', scope='Artifact syntax and draft schema only; not mathematical proof',
                      checked_utc=datetime.now(timezone.utc).isoformat(), claims=9, entries=7,
                      relations=len(bundle['relations']), local_and_submitted_bundle_equal=True,
                      source_license_tags_valid=True, proof_claims_independently_checked=0,
                      command='python -X utf8 finalize_packet.py')
    (ROOT / 'ARTIFACT_CHECK.json').write_text(json.dumps(validation, indent=2), encoding='utf-8')
    measurements = json.loads((ROOT / 'MEASUREMENTS.json').read_text(encoding='utf-8'))
    if measurements['status'] != 'PASS':
        measurements.update(status='HELD', executed_graph_checks=0,
                            command='python -X utf8 verify_threshold.py --gate ~/.claude/compute/compute_state.json',
                            process_exit_code=1,
                            observed_fresh_gate=dict(ts='2026-10-10 08:22:43', status='distress', mode='throttle',
                              reasons=['memory_physical_pressure', 'process_critical'],
                              mem_avail_mb=1419, commit_avail_mb=7176, disk_free_gb=44.4, hung_windows=0),
                            scope='Gate held the first launch before graph computation; no numerical mathematical result.')
        (ROOT / 'MEASUREMENTS.json').write_text(json.dumps(measurements, indent=2), encoding='utf-8')
    source = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
    source['canonical_store_check'] = dict(path='~/math-brain-build/local/population/brain.sqlite3',
               open_mode='file:...?...mode=ro; uri=True', matching_original_nodes=2,
               receipt='canonical_nodes_p0117.json', observations='Existing problem and attempt are curated-secondary, unverified, dated 2026-09-07; no new proof closure is asserted.')
    source['single_remaining_gap'] = 'Exclude uniformly pinned bigeodesics; equivalently prove support collapse H_infinity<=essential infimum of F. Unproved in this packet.'
    (ROOT / 'SOURCE_STATUS.json').write_text(json.dumps(source, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    states = json.loads((ROOT / 'DELIVERY_STATE.json').read_text(encoding='utf-8'))
    states.update(reviewed=False, ingested=False, retrievable=False,
                  meaning='Positive review, ingestion and retrieval receipts have not been obtained.',
                  graph_verification=measurements['status'], artifact_validation='PASS',
                  referee_packet='REVIEW_PACKET.md', hook_proposal='Local draft and patch only; not published outside the worker folder.')
    (ROOT / 'DELIVERY_STATE.json').write_text(json.dumps(states, indent=2), encoding='utf-8')
    report = '''P0117 author packet is ready for independent mathematical review. The full no-bigeodesic conclusion is unproved in this packet; current literature openness and novelty remain UNKNOWN.

Recovered the original problem and anchoring attempt from two matching nodes in the read-only canonical population store. The primary survey locator is ADH Section 4.5, Question 31. The exact working specialization uses iid finite nonnegative nonatomic weights and a finite second moment for the minimum of four independent weights. A downloaded September 24, 2026 primary manuscript states the full result in this specialization; its whole proof has not been audited here. Its finite-minimizer prerequisite is also prior art. The old campaign registry path no longer exists, and its broader scope is not silently replaced by this specialization.

The proposed brain addition is one coherent edge-resampling route: moment-free properness; an exact deleted-edge metric formula; decreasing boundary capacities and anchored two-sided compactness; the conditional identity P(edge on bigeodesic | outside)=F(H_infinity); and preservation plus a uniform bypass penalty after one-edge lowering. ATTEMPT.md gives the proofs, the valid single-coordinate independence argument and the unsuccessful routes to support collapse. Constant weights and an adaptive-selector toy model delimit what those arguments establish.

The single hardest remaining input is to exclude a bigeodesic with a uniform positive bypass penalty, equivalently support collapse H_infinity<=the essential infimum. No argument closes it. The mathematical reductions are author-proved, not independently checked.

Measurements from commands actually run: targeted canonical-store query found two dated P0117 nodes; authoring produced nine claim rows and seven DRAFT entries. The initial worker-folder listing was empty; the local artifact check now counts nine claim rows and seven draft entries, with the identical seven-entry bundle staged in the inbox. This is an authoring count, not a measured live-brain improvement. python -X utf8 finalize_packet.py passed the artifact syntax/schema checks for nine rows, seven entries and seven relations. python -X utf8 verify_threshold.py --gate ~/.claude/compute/compute_state.json exited 1 at the governor check, before any graph computation. The fresh gate reported distress/throttle with physical memory pressure and process_critical; the follow-up read showed 1,419 MiB physical headroom. Zero graph checks ran. No source/hash or syntax receipt is counted as mathematical proof. No Lean theorem was checked.

The change is a review proposal until independently checked and ingested. Seven entries are staged at ~/math-brain-inbox/w384/bundle_001.json using definition/concept kinds and the accepted owner-own-work source tag. Submitted, reviewed, ingested and retrievable are separate fields in DELIVERY_STATE.json; only submission is confirmed. The local hook draft has a fire and silence case and an evidence slug, with a patch for the permitted reviewer to publish. Source notes copied from the memory/store remain in this worker's reports.

Apply patches/01_p0117_draft_bundle.diff to stage the draft if its identical inbox copy is absent; after independent review, the validating coordinator integrates the kept entries. Apply patches/02_math_scope_hook.diff only through the hook proposal/audit pipeline. This worker did not run integrate_drafts.py because the task reserves live-store integration to the validating coordinator.

Risks: the original card's broader scope is imperfectly pinned; the newer claimed resolution may preempt research novelty; an independent referee may find an error in a reduction; and the held finite verifier provides no numerical confirmation. Schema validation does not remove these risks. All conjectural inputs remain concept/draft material.

NEXT: w386 independently checks Proposition 4 and Lemma 5; rerun the bounded verifier after a fresh healthy gate, then keep the valid reduction and pursue a planar vanishing-bypass argument without assuming adaptive independence.
'''
    (ROOT / 'REPORT.md').write_text(report, encoding='utf-8')
    print(json.dumps(validation))


if __name__ == '__main__':
    main()
