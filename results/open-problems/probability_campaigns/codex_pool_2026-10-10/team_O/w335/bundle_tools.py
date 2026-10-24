import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
INBOX = pathlib.Path('~/math-brain-inbox/w335')

def emit(number, problem_id, entries, relations, proof_file, measurement_file):
    proof_path = ROOT / proof_file
    for entry in entries:
        entry['source'] = {
            'source_id': 'owner-work:w335:' + entry['key'],
            'url': proof_path.as_uri(),
            'revision': 'author-checked-20261010-pending-independent-w347',
            'license': 'owner-own-work',
            'excerpt': None,
        }
    bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w335', 'bundle_slug': 'w335-' + problem_id.lower() + '-20261010', 'entries': entries, 'relations': relations}
    # Only the task's explicitly named inbox exception is used outside ROOT.
    INBOX.mkdir(parents=True, exist_ok=True)
    local = ROOT / 'bundles'
    local.mkdir(exist_ok=True)
    for folder in (local, INBOX):
        final = folder / ('bundle_%03d.json' % number)
        part = final.with_suffix('.json.part')
        part.write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        part.replace(final)
    row = {'row_id': 'w335-' + problem_id + '-bundle-%03d' % number, 'problem_id': problem_id, 'bundle_path': str(INBOX / ('bundle_%03d.json' % number)), 'entries': len(entries), 'edges': len(relations), 'proof_path': str(proof_path), 'measurement_path': str(ROOT / measurement_file), 'audit_status': 'pending_w347', 'label': 'draft proofs or explicitly limited route; no full-problem solution claim', 'created': '2026-10-10'}
    with (ROOT / 'results.jsonl').open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(row, ensure_ascii=False) + '\n')
    with (ROOT / 'AUDIT_REQUEST.jsonl').open('a', encoding='utf-8') as stream:
        stream.write(json.dumps({'auditor': 'w347', 'problem_id': problem_id, 'bundle_path': row['bundle_path'], 'proof_path': str(proof_path), 'measurement_path': row['measurement_path'], 'request': 'Blindly check claims and return KEEP/FIX/DROP per entry; counts remain zero until KEEP.'}) + '\n')
    print(json.dumps(row), flush=True)
    return bundle

def entry(key, namespace, name, kind, title, statement, proof, assumptions):
    return {'key': key, 'namespace': namespace, 'logical_name': name, 'kind': kind, 'title': title + ' [draft; pending w347]', 'statement': statement, 'proof_text': proof, 'assumptions': assumptions, 'domain': 'probability theory'}

def existing_cards():
    return json.loads((ROOT / 'baseline_cards.json').read_text(encoding='utf-8'))

def edge_to_problem(problem_id, key, own_quote, kind='specializes'):
    card = next(card for card in existing_cards() if card['title'].startswith('Open problem:') and ('open-problem-' + problem_id.lower() + '-') in card['metadata_json'])
    return {'from_key': key, 'to_existing_logical': json.loads(card['metadata_json'])['logical_id'], 'kind': kind, 'rationale': 'New card: "' + own_quote + '"; existing card: "' + card['body'].split('. Source:')[0].split('). ')[-1][:280] + '". This result treats an explicitly stated special case or limitation; it does not certify a solution.'}

def edge_to_attempt(problem_id, key, own_quote, target_quote, kind='generalizes'):
    card = next((card for card in existing_cards() if card['title'].startswith('Attempt on') and ('attempt-' + problem_id.lower() + '-') in card['metadata_json']), None)
    if card is None:
        # The scoped read may find the source-ledger attempt but no matching
        # store card. Link the observed problem card rather than invent a target.
        return edge_to_problem(problem_id, key, own_quote, 'cites')
    assert target_quote in card['body']
    return {'from_key': key, 'to_existing_logical': json.loads(card['metadata_json'])['logical_id'], 'kind': kind, 'rationale': 'New card: "' + own_quote + '"; existing card: "' + target_quote + '".'}

if __name__ == '__main__':
    measurement = json.loads((ROOT / 'p0205_measurement.json').read_text(encoding='utf-8'))
    assert measurement['result'] == 'PASS'
    statement = 'Let G have order n>=2 and identity e. For 0<alpha<=1 let P(x,x)=1-alpha and P(x,y)=alpha/(n-1) for y!=x. Start P at e and stop at independent T with P(T=k)=p(1-p)^k, k>=0, 0<p<1. Put b=1-alpha*n/(n-1) and a=p/(1-(1-p)*b). The Metropolis kernel M with proposal P and target Law(X_T) has spectral-gap relaxation time tau(M)=tau(P)*(1+(n-1)*a), where tau(P)=(n-1)/(alpha*n). It is strictly increasing in p. With alpha=p=1/2 both kernels are lazy and tau(M)/[n*tau(P)] tends to 2/3 as n tends to infinity. This family has proposal degree n-1 and does not settle a fixed-degree variant or a differently parametrised monotonicity question.'
    proof = (ROOT / 'P0205_proof.md').read_text(encoding='utf-8').split('Proof. ',1)[1].split('\n\nConsequences.',1)[0] + ' Differentiating a=p/(1-b+b*p) gives a prime=(1-b)/(1-b+b*p)^2>0. For alpha=p=1/2, a=(n-1)/(3*n/2-1), so (1+(n-1)*a)/n tends to 2/3.'
    new = entry('p0205-complete-cayley-spectrum', 'probability.markov', 'complete-cayley-geometric-target-metropolis-spectrum', 'lemma', 'Exact complete-Cayley geometric-target Metropolis relaxation', statement, proof, ['Finite group order n>=2', 'Uniform nonidentity proposal with holding 1-alpha', 'Geo0 convention and inverse ordinary spectral gap'])
    emit(1, 'P0205', [new], [edge_to_problem('P0205', new['key'], 'This family has proposal degree n-1'), edge_to_attempt('P0205', new['key'], 'tau(M)=tau(P)*(1+(n-1)*a)', 'Monotone decrease is false already on the two-element Cayley group')], 'P0205_proof.md', 'p0205_measurement.json')
