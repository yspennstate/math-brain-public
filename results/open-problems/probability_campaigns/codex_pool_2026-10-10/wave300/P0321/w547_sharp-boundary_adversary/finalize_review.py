"""Incorporate the named referee's receipts without reviewing their review."""
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
REVIEW_PATH = Path('~/brain_workers/w548/VERDICTS.jsonl')
INBOX = Path('~/math-brain-inbox/w547')

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def main():
    reviews = []
    with REVIEW_PATH.open(encoding='utf-8-sig') as handle:
        for line in handle:
            if 'w547' in line:
                reviews.append(json.loads(line))
    by_claim = {}
    for review in reviews:
        for claim_id in ['C001', 'C002', 'C003']:
            if claim_id in review.get('id', '') and review.get('reviewer') == 'w548':
                by_claim[claim_id] = review
    assert all(by_claim[c]['verdict'] == 'KEEP' for c in ['C002', 'C003'])
    save(ROOT / 'REVIEW_RECEIPT.json', {
        'source_path': str(REVIEW_PATH), 'reviewer': 'w548', 'reviews': reviews,
        'received_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'account_login': 'Not established; no claim of two independent account keeps.',
        'receipt_role': 'Recorded independent verdicts on original author proofs; no audit of a review and no formal-check receipt.'})
    status = read(ROOT / 'SOURCE_STATUS.json')
    status['brain_output_states']['reviewed'] = True
    status['brain_output_states']['reviewed_detail'] = 'w548 KEEP C001, C002, C003; receipts in REVIEW_RECEIPT.json. C001 is a prior-work reproduction and is excluded from the new bundle.'
    status['reviewed'] = True
    status['submitted'] = True
    status['ingested'] = 'UNKNOWN / not performed by w547'
    status['retrievable'] = 'UNVERIFIED for new bundle'
    save(ROOT / 'SOURCE_STATUS.json', status)
    claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    for claim in claims:
        suffix = claim['id'].rsplit('.', 1)[-1]
        if suffix in by_claim:
            claim['status'] = 'independently checked proof'
            claim['independent_reviewer'] = {'worker': 'w548', 'verdict': 'KEEP',
                                             'receipt': str(ROOT / 'REVIEW_RECEIPT.json'),
                                             'source_row_id': by_claim[suffix]['id']}
            claim['remaining_gap'] = 'No microscopic Riesz-to-elastic, defect-sector, or real particle/bond correlation comparison; no proof or refutation of P0321.'
    (ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')

    bundle = read(ROOT / 'bundle_001.json')
    prior = json.loads(json.dumps(bundle))
    for entry in bundle['entries']:
        entry['source']['revision'] = 'draft-auxiliary-proof-w548-keep-20261010'
        entry['statement'] = entry['statement'].replace(
            'AUTHOR DERIVATION, INDEPENDENT REFEREE PENDING.',
            'INDEPENDENTLY CHECKED AUXILIARY GAUSSIAN RESULT (w548 KEEP); DRAFT CONCEPT.')
        entry['assumptions'] = [s.replace(
            'Independent mathematical referee for author-derived claims is pending; concept/draft material only.',
            'Named independent referee w548 kept C002/C003; this submission remains concept/draft material with no microscopic Gibbs claim.')
            for s in entry['assumptions']]
    destination = INBOX / 'bundle_001.json'
    existing = read(destination)
    if existing != bundle:
        assert existing == prior, 'Owned inbox artifact changed elsewhere; inspect before replacing'
        snapshot = ROOT / 'bundle_001_before_referee_receipt.json'
        if not snapshot.exists():
            save(snapshot, prior)
        temporary = INBOX / 'bundle_001.reviewed.part'
        assert not temporary.exists(), 'Inspect an existing part before writing'
        save(temporary, bundle)
        temporary.replace(destination)
    save(ROOT / 'bundle_001.json', bundle)
    assert read(destination) == bundle
    assert len(bundle['entries']) == 3 and len(bundle['relations']) == 3
    assert all(e['kind'] in ['definition', 'concept'] and e['proof_text'] is None for e in bundle['entries'])
    receipt = read(ROOT / 'DRAFT_RECEIPT.json')
    receipt['reviewed'] = True
    receipt['reviewed_detail'] = 'Independent referee w548 KEEP C002 and C003; concept kinds retained.'
    receipt['referee_receipt'] = str(ROOT / 'REVIEW_RECEIPT.json')
    receipt['local_and_inbox_json_equal'] = True
    save(ROOT / 'DRAFT_RECEIPT.json', receipt)
    measurement = read(ROOT / 'MEASUREMENTS.json')
    gate = measurement.get('gate', {})
    if measurement['status'] == 'SKIPPED_FRESH_RESOURCE_GATE':
        validation = ('Numerical replay was declined by the fresh gate: CPU %.1f%% against a 75%% ceiling; '
                      'available physical memory %.2f GiB and commit headroom %.2f GiB, with the existing 6 GiB commit floor preserved. '
                      'No quadrature was run. Command: python -X utf8 ~/brain_workers/w547/replay_boundary.py.'
                      % (gate['cpu_percent'], gate['available_memory_bytes']/1024**3,
                         gate['commit_available_bytes']/1024**3))
    else:
        validation = ('Quadrature status %s. See MEASUREMENTS.json for all finite checks and their limits. '
                      'Command: python -X utf8 ~/brain_workers/w547/replay_boundary.py.' % measurement['status'])
    report = '\n\n'.join([
        'P0321 remains unproved here; current openness is UNKNOWN. The exact catalogue record and Lewin VI.B (printed pp.66-67) were recovered. The source predicts a correlation signature but does not fix a rigorous universal exponent range or rate criterion.',
        'The main deliverable is C003: in a precisely defined cutoff Gaussian displacement model, taking the stiffness endpoint p->2 before the distance limit adds T|G|^2/(4*pi*a) to the positional decay exponent. The iterated limits therefore differ. C002 supplies the exact exponents and the positive curl-orientation plateau. w548 independently kept both proofs. These results isolate a nonuniform-limit failure in a proposed auxiliary route; they do not identify p with the microscopic Riesz exponent.',
        'The old common-angle counterexample C001 was independently reproduced, then recognized in at-p0321 and excluded from the new draft. Original w546 L01 was independently checked and kept within its L1 stationary Gaussian assumptions; AUDIT_W546_L01.md gives the verdict.',
        validation,
        'Artifact validation: 3 draft entries, 3 supported relations, and 2/2 hook fire/silent controls passed. The local draft equals the atomic inbox copy. Commands: python -X utf8 ~/brain_workers/w547/prepare_review_packet.py; python -X utf8 ~/brain_workers/w547/finalize_review.py. No recall-performance improvement is claimed; ingestion and retrievability of the new entries remain unverified.',
        'The main risk is using elastic proxies as particle/bond correlations or assuming free-defect control. The ultraviolet cutoff, anchored infrared limit, positive coefficients and fixed-p distance quantifiers are essential. The hardest open obligation is a microscopic positive-temperature defect/correlation comparison on a genuine interval.',
        'Apply: the validating coordinator should validate and integrate only ~/math-brain-inbox/w547/bundle_001.json using the existing workflow; it contains a definition and two draft concepts, with owner-own-work attribution and w548 receipts. The local HOOK_PROPOSALS.jsonl is ready for hook review. No live code patch, store mutation, or global recall change was made by w547.',
        'NEXT: coordinator validate the independently checked Gaussian endpoint bundle for integration; the next mathematical obligation is the microscopic defect/correlation comparison at a fixed supported Riesz exponent.'
    ]) + '\n'
    (ROOT / 'REPORT.md').write_text(report, encoding='utf-8')
    packet = '\n\n'.join([
        'w547 P0321 review packet, 2026-10-10. Recommended mathematical verdict: KEEP C002/C003 within the stated Gaussian assumptions, as independently recorded by w548. P0321 has not been proved or refuted; current openness UNKNOWN.',
        'Read GAUSSIAN_BOUNDARY.md for the frozen independent derivation, especially C003. Its endpoint gap is exactly T|G|^2/(4*pi*a)>0. Read CLAIMS.jsonl for exact statements, assumptions, proof routes, reviewers, gaps and statuses. Read REVIEW_RECEIPT.json for the named referee receipts. There is no formal proof-check receipt and no admitted placeholder.',
        'SOURCE_STATUS.json identifies the exact local record and primary source: https://arxiv.org/pdf/2202.09240v2, VI.B, printed pp.66-67. It distinguishes catalogue recovery, current openness uncertainty and the remaining formal phase-definition quantifiers. ATTEMPT.md records independence, prior-work deduplication and the applied scar.',
        'AUDIT_W546_L01.md reviews the paired original proof after the independent calculation was frozen. It is not a review of a review. C001 is a reproduction and is not in the new bundle.',
        'REPORT.md records the result, validation, resource-gated numerical limitation, risks and application instructions. COMPUTE_GATE.json and MEASUREMENTS.json preserve the fresh gate receipt. replay_boundary.py can perform bounded deterministic cross-checks when its unchanged gates admit them; such checks cannot prove P0321.',
        'Brain delivery: ~/math-brain-inbox/w547/bundle_001.json (also copied locally), 3 entries and 3 relations. DRAFT_RECEIPT.json records submitted=true, reviewed=true, ingested=UNKNOWN, retrievable=UNVERIFIED. Definition/concept kinds are retained. The integrator alone creates manifests and changes the live store. HOOK_PROPOSALS.jsonl is local because worker shared writes were restricted; both mandatory controls passed.',
        'NEXT: coordinator validate and integrate the draft concepts with their exact assumptions and w548 review receipt; any microscopic promotion needs a separate original proof and independent check.'
    ]) + '\n'
    (ROOT / 'REVIEW_PACKET.md').write_text(packet, encoding='utf-8')
    print(json.dumps({'referee': 'w548', 'kept_original_claims': sorted(by_claim),
                      'draft_entries': 3, 'relations': 3, 'local_equals_inbox': True,
                      'numeric_status': measurement['status'], 'report': str(ROOT / 'REPORT.md'),
                      'review_packet': str(ROOT / 'REVIEW_PACKET.md')}, indent=2))

if __name__ == '__main__':
    main()
