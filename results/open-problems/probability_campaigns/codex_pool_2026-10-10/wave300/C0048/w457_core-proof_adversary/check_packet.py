"""Check final artifact consistency, not theorem truth or live-store ingestion."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))


def main():
    for name in ['STATUS.md','SOURCE_STATUS.json','ATTEMPT.md','CLAIMS.jsonl',
                 'REVIEW_PACKET.md','REPORT.md','AUDIT_w456.md','CUBIC_OBSTRUCTION.md',
                 'measurements.json','cumulant_measurements.json','SUBMISSION_STATES.json']:
        assert (ROOT/name).is_file(), name
    source = load('SOURCE_STATUS.json')
    assert source['current_openness'] == 'UNKNOWN' and source['novelty_claim'] is False
    assert source['formal_check'] is None
    claims = [json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    assert len(claims) == len({row['claim_id'] for row in claims}) == 9
    permitted_statuses = {'conjecture','numerical evidence','sketch','proved special case','independently checked proof'}
    for row in claims:
        for field in ['exact_statement','assumptions','source','proof_or_counterexample',
                      'independent_reviewer','remaining_gap','status']:
            assert row.get(field), (row['claim_id'],field)
        assert row['status'] in permitted_statuses
    audit = next(row for row in claims if row['claim_id']=='w457-C0048-AUDIT-w456')
    assert audit['parent_problem_verdict'] == 'NOT_PROVED'
    assert audit['kept_scope'] == 'finite and conditional results only'

    proof_receipt = load('review/provenance.json')
    snap = ROOT/'review/w456_ATTEMPT_snapshot.md'
    assert hashlib.sha256(snap.read_bytes()).hexdigest() == proof_receipt['snapshot_sha256']
    for name, expected in proof_receipt['independent_files'].items():
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == expected, name
    assert proof_receipt['independent_derivations_before_paired_read'] is True
    referee = load('review/w458_verdict_snapshot.json')
    assert referee['reviewer']=='w458' and len(referee['records'])==4
    assert all(row['verdict']=='KEEP' for row in referee['records'])

    bundle = load('draft_bundle.json')
    submitted = load('SUBMISSION_STATES.json')
    inbox_path = Path(submitted['bundle'])
    assert submitted['submitted']['state'] == 'complete'
    assert json.loads(inbox_path.read_text(encoding='utf-8')) == bundle
    assert len(bundle['entries']) == 4 and len(bundle['relations']) == 4
    by_key = {entry['key']:entry for entry in bundle['entries']}
    canonical = load('CANONICAL_CHECK.json')
    existing = {row['metadata']['logical_id']:row['body'] for row in canonical['targeted_nodes']}
    assert canonical['mode'] == 'ro' and canonical['lookup_count'] == 2
    for entry in bundle['entries']:
        assert entry['kind']=='concept' and entry['proof_text'] is None
        assert entry['statement'].startswith('DRAFT AUDIT CONCEPT;')
        assert entry['source']['license'].startswith('owner-own-work')
    for relation in bundle['relations']:
        start = by_key[relation['from_key']]['statement']
        end = by_key[relation['to_key']]['statement'] if 'to_key' in relation else existing[relation['to_existing_logical']]
        quoted_ends = re.findall(r'"([^\"]+)"',relation['rationale'])
        assert len(quoted_ends)==2, relation
        assert ((quoted_ends[0] in start and quoted_ends[1] in end)
                or (quoted_ends[0] in end and quoted_ends[1] in start)), relation

    measurements = load('measurements.json')
    cumulants = load('cumulant_measurements.json')
    assert measurements['conditionals_checked_total']==73856 and measurements['mismatches_total']==0
    assert cumulants['equalities_checked']==6 and cumulants['corrected_wrong_fourth_cumulants']==0
    assert cumulants['baseline_wrong_fourth_cumulants']==2
    hook = json.loads((ROOT/'hooks/math-w457.jsonl').read_text(encoding='utf-8'))
    assert len(hook['text'])<=300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
    assert '~/primary_directive/hooks1000/proposals/math-w457.jsonl' in (ROOT/'patches/01_cumulant_mixture_hook.diff').read_text(encoding='utf-8')

    paths = ['ATTEMPT.md','CUBIC_OBSTRUCTION.md','AUDIT_w456.md','CLAIMS.jsonl','SOURCE_STATUS.json',
             'REVIEW_PACKET.md','REPORT.md','draft_bundle.json','measurements.json','cumulant_measurements.json',
             'review/provenance.json','review/w456_ATTEMPT_snapshot.md','review/w458_verdict_snapshot.json','hooks/math-w457.jsonl',
             'patches/01_cumulant_mixture_hook.diff']
    hashes = {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in paths}
    hashes[str(inbox_path)] = hashlib.sha256(inbox_path.read_bytes()).hexdigest()
    receipt = {
        'command':'python -X utf8 check_packet.py', 'artifact_consistency':'PASS',
        'claim_rows':len(claims),'concept_entries':len(by_key),'relations_with_quoted_supporting_ends':4,
        'paired_snapshot_hash_matches':True,'original_independent_derivation_hashes_match':True,
        'referee_records_saved':4,'review_scope':'partial scoped KEEP; separate fourth-Legendre/numeric receipts pending',
        'mathematical_approval_scope':'Use the independent referee receipt; this check certifies artifact consistency only',
        'parent_problem':'NOT_PROVED','formal_check':None,
    }
    (ROOT/'PACKET_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    (ROOT/'REVIEW_HASHES.json').write_text(json.dumps(hashes,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt))


if __name__=='__main__':
    main()
