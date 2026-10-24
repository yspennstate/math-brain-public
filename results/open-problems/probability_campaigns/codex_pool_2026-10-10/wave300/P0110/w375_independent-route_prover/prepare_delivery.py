"""Prepare this worker's own labeled concept draft; never integrate a live store."""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w375')


def source(lemma):
    return {
        'source_id': f'owner-probability-campaign:w375:P0110:{lemma}',
        'url': 'file:///~/brain_workers/w375/PROVED_LEMMAS.md',
        'revision': 'author-proof-2026-10-10-designated-referee-pending',
        'license': 'owner-own-work (campaign author proof; referee pending)',
        'excerpt': None,
    }


payload = {
    'spec': 'mathbrain-draft-v1',
    'author_agent': 'w375',
    'bundle_slug': 'p0110-directed-reduction-obstruction-w375-001',
    'entries': [
        {
            'key': 'axial-linear-gap',
            'namespace': 'probability.fpp',
            'logical_name': 'bounded-iid-fpp-linear-axial-directed-gap',
            'kind': 'concept',
            'title': 'DRAFT: a linear axial gap between unrestricted and directed iid FPP',
            'statement': 'Author-proved draft; w376 scoped KEEP, designated referee pending. On Z^d, d>=2, let undirected nearest-neighbor edge weights be iid, nondegenerate, and satisfy 0<r<=t_e<=R<infinity. Let T be the unrestricted minimum passage time and mu=E t_e. Choose two separated support sets of positive masses, with weights at most a on the lower set and at least b on the higher set, and an integer k with k*b>(k+2)*a. Let S_k be the sum on a k-edge axial path, and H_k the sum on its edge-disjoint height-one (k+2)-edge detour. Then delta=E[(S_k-H_k)_+]>0, E T(0,n*e1)<=n*mu-floor(n/(k+1))*delta, and almost surely limsup T(0,n*e1)/n<=mu-delta/(k+1). The directed axial path has passage-time ratio tending to mu, giving a strictly positive raw linear gap. For any per-n coupling of the two marginal laws and any 0<c<delta/(k+1), P((T_directed-T)/n>=c) tends to one. Different centering may still permit a comparison. This result supplies no fluctuation or wandering exponent and does not solve P0110.',
            'proof_text': None,
            'assumptions': ['d>=2', 'iid undirected nearest-neighbor edge weights', 'nondegenerate law with strictly positive bounded support', 'deterministic two-support-set choice with positive masses', 'raw passage times, not centered fluctuations'],
            'domain': 'probability theory',
            'source': source('L2'),
        },
        {
            'key': 'diagonal-detour',
            'namespace': 'probability.fpp',
            'logical_name': 'iid-fpp-diagonal-all-monotone-detour-obstruction',
            'kind': 'concept',
            'title': 'DRAFT: an iid FPP detour beats every monotone diagonal competitor',
            'statement': 'Author-proved draft; w376 scoped KEEP, designated referee pending. For iid nonnegative nearest-neighbor edge weights on Z^d, d>=2, suppose disjoint positive-mass support sets satisfy I_low subset [ell,a] and I_high subset [b,infinity), with 0<=ell<=a<b. Let p_low and p_high be their probabilities. If integer k>=1 satisfies k*(b+ell-2*a)>2*a, then with probability at least p_high^(2*k^2+k)*p_low^(2*k+2), unrestricted passage time from 0 to k*(e1+e2) is strictly smaller than the minimum over all coordinate-monotone paths between those endpoints. The event puts all horizontal edges of [0,k]^2 and all its vertical edges with x<k in I_high, the right boundary column in I_low, and a bottom detour at y=-1 with two vertical connectors in I_low. Every monotone competitor costs at least k*b+k*ell; the detour costs at most (2*k+2)*a. The event uses disjoint deterministic edge sets. It is a finite event, not an asymptotic diagonal gap or a typical wandering bound.',
            'proof_text': None,
            'assumptions': ['d>=2', 'iid nonnegative undirected nearest-neighbor edge weights', 'two disjoint support sets of positive mass', 'k*(b+ell-2*a)>2*a', 'coordinate-monotone means no negative movement in e1/e2 and no other-coordinate movement'],
            'domain': 'probability theory',
            'source': source('L3'),
        },
    ],
    'relations': [
        {'from_key': 'axial-linear-gap', 'to_key': 'diagonal-detour', 'kind': 'semantic_association',
         'rationale': 'Both are reductions obstructed by finite deterministic low-edge detours, but the axial result is asymptotic and the diagonal result is finite only.'},
        {'from_key': 'axial-linear-gap', 'to_existing_logical': 'math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation', 'kind': 'semantic_association',
         'rationale': 'The P0110 source asks for a concrete iid FPP law with chi=2xi-1; a raw directed-path transfer is one proposed route that this drift gap restricts. No KPZ conclusion follows.'},
        {'from_key': 'diagonal-detour', 'to_existing_logical': 'math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation', 'kind': 'semantic_association',
         'rationale': 'This supplies a nonaxial finite obstruction to an exact directed reduction used in a proposed exponent-transfer route, not a refutation of the existential target.'},
    ],
}


def main():
    required = {'key', 'namespace', 'logical_name', 'kind', 'title', 'statement', 'proof_text', 'assumptions', 'domain', 'source'}
    keys = {e['key'] for e in payload['entries']}
    for entry in payload['entries']:
        assert required <= set(entry)
        assert entry['kind'] == 'concept' and entry['proof_text'] is None
        assert entry['source']['license'].startswith('owner-own-work')
    for relation in payload['relations']:
        assert relation['from_key'] in keys and relation['kind'] == 'semantic_association'
        assert relation.get('to_key') in keys if 'to_key' in relation else bool(relation.get('to_existing_logical'))
    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + '\n'
    (ROOT / 'bundle_draft.json').write_text(serialized, encoding='utf-8')
    hook_path = ROOT / 'hooks/proposals/math-w375.jsonl'
    hook = json.loads(hook_path.read_text(encoding='utf-8'))
    assert len(hook['text']) <= 300 and hook['fire_when'] and hook['silent_when'] and hook['evidence']
    patches = ROOT / 'patches'
    patches.mkdir(exist_ok=True)
    live = '~/primary_directive/hooks1000/proposals/math-w375.jsonl'
    diff = f'--- a/{live}\n+++ b/{live}\n@@ -0,0 +1 @@\n+' + json.dumps(hook, ensure_ascii=False) + '\n'
    (patches / '01_fpp_directed_transfer_hook.diff').write_text(diff, encoding='utf-8')
    expected = Path('~/math-brain-inbox').resolve() / 'w375'
    assert INBOX.resolve() == expected
    INBOX.mkdir(exist_ok=True)
    number = 1
    while (INBOX / f'bundle_{number:03d}.json').exists() or (INBOX / f'bundle_{number:03d}.part').exists():
        number += 1
    part = INBOX / f'bundle_{number:03d}.part'
    final = INBOX / f'bundle_{number:03d}.json'
    assert part.resolve().parent == expected and final.resolve().parent == expected
    # The calling agent obtains and asserts the narrow inbox lease immediately before this command.
    with part.open('x', encoding='utf-8') as file:
        file.write(serialized)
    assert not final.exists()
    os.replace(part, final)
    receipt = {
        'prepared_at_utc': datetime.now(timezone.utc).isoformat(),
        'bundle_path': str(final), 'entry_count': 2, 'relation_count': 3,
        'all_entries_concepts': True, 'local_shape_check': 'PASS',
        'mathematical_check': 'w376 scoped KEEP; designated referee pending',
        'workflow_states': {'submitted': True, 'reviewed': False, 'ingested': False, 'retrievable': False},
        'shared_boundary_note': 'w378 independently has the support-threshold result; it is retained as a local supporting proof and omitted from this bundle to avoid duplicate promotion.',
    }
    (ROOT / 'DELIVERY_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    source_path = ROOT / 'SOURCE_STATUS.json'
    status = json.loads(source_path.read_text(encoding='utf-8'))
    status['workflow_states'] = receipt['workflow_states']
    status['draft_bundle_path'] = str(final)
    status['peer_review'] = {'agent': 'w376', 'verdict': 'scoped KEEP L1-L4', 'receipt': '~/brain_workers/w376/PEER_AUDIT.md', 'designated_referee': 'w377', 'designated_referee_status': 'pending'}
    status['shared_boundary_note'] = receipt['shared_boundary_note']
    source_path.write_text(json.dumps(status, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
