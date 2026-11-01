"""Prepare worker-local drafts and a narrow source-row correction; no live writes."""
from pathlib import Path
import json
import re
import sqlite3

ROOT = Path(__file__).resolve().parent
LIVE = Path('~/<private-repo>/06_math_research/probability_1000_intake_D_20260908/attempts.jsonl')
TARGET = 'math:probability.core:open-problem-p0297-exact-hausdorff-dimension-of-liouville-quantum-gravity'


def save(name, value):
    path = ROOT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def entry(key, name, kind, title, statement, assumptions, proof=None):
    return {'key': key, 'namespace': 'probability.lqg', 'logical_name': name,
            'kind': kind, 'title': title, 'statement': statement, 'proof_text': proof,
            'assumptions': assumptions, 'domain': 'probability and metric geometry',
            'source': {'source_id': 'owner-own-work:w519:' + key,
                       'url': 'urn:probability-research:20261010:w519:' + key,
                       'revision': 'draft-unreviewed-20261010-v1',
                       'license': 'owner-own-work; attributed campaign derivation, no novelty claim, independent review pending',
                       'excerpt': None}}


def main():
    copies = ROOT / 'copies'
    patches = ROOT / 'patches'
    copies.mkdir(exist_ok=True)
    patches.mkdir(exist_ok=True)
    changed = []
    fixed_copy = copies / 'intake_D_attempts.corrected.jsonl'
    with LIVE.open('rb') as src, fixed_copy.open('wb') as dst:
        for line_number, raw in enumerate(src, 1):
            if b'D0049-A001' in raw:
                before = json.loads(raw)
                assert before['attempt_id'] == 'D0049-A001'
                fixed = raw.replace(b'd_gamma = 2Q/xi', b'd_gamma = gamma/xi')
                fixed = fixed.replace(b'd_gamma = 2 Q / xi', b'd_gamma = gamma / xi')
                after = json.loads(fixed)
                fields = [k for k in before if before[k] != after[k]]
                assert set(fields) == {'key_identity', 'method'}, fields
                assert all(before[k] == after[k] for k in before if k not in fields)
                assert raw.count(b'd_gamma = 2Q/xi') + raw.count(b'd_gamma = 2 Q / xi') == 2
                assert b'd_gamma = 2Q/xi' not in fixed and b'd_gamma = 2 Q / xi' not in fixed
                changed.append((line_number, raw.decode('utf-8').rstrip('\r\n'), fixed.decode('utf-8').rstrip('\r\n'), fields))
                dst.write(fixed)
            else:
                dst.write(raw)
    assert len(changed) == 1
    line_number, old, new, fields = changed[0]
    live_path = LIVE.as_posix()
    diff = f'--- a/{live_path}\n+++ b/{live_path}\n@@ -{line_number} +{line_number} @@\n-{old}\n+{new}\n'
    (patches / '01_intake_D_lqg_dimension_identity.diff').write_text(diff, encoding='utf-8')
    save('CORRECTION_MEASUREMENTS.json', {'source': live_path, 'row': line_number,
         'attempt_id': 'D0049-A001', 'bad_formula_occurrences_before': 2,
         'bad_formula_occurrences_after': 0, 'changed_fields': fields,
         'other_fields_preserved': True, 'live_source_changed': False,
         'counterexample': {'wrong': 10, 'correct': 4}})

    entries = [
      entry('local-mass', 'positive-local-mass-exponent', 'definition', 'Positive local mass exponent',
            'A positive Radon measure mu has finite positive local mass exponent a at x when mu(B_E(x,r))>0 for sufficiently small r and lim_{r->0} log(mu(B_E(x,r)))/log r=a with 0<a<infinity.',
            ['Euclidean balls', 'positive Radon measure near x']),
      entry('log-potential', 'logarithmic-disk-potential-local-exponent', 'lemma', 'Logarithmic disk potentials preserve positive local mass exponents',
            'Let mu be a positive Radon measure near x with finite positive local mass exponent a. The centered disk potential T(R)=(1/pi) integral_{B_E(x,R)} log(R/|x-y|) mu(dy) is finite and positive for sufficiently small R, and lim_{R->0} log(T(R))/log R=a. This is a Euclidean potential exponent, not a metric Hausdorff dimension or sample-path exit-time theorem.',
            ['mu positive Radon near x', 'mu(B_E(x,r))>0 eventually', 'finite local exponent a>0'],
            'The positive exponent excludes an atom at x. Tonelli gives pi*T(R)=integral_0^R mu(B_E(x,s)) ds/s. For every 0<eta<a, the mass is eventually between s^(a+eta) and s^(a-eta). Integration bounds pi*T(R) between R^(a+eta)/(a+eta) and R^(a-eta)/(a-eta). Taking log exponents and then eta->0 proves the claim.'),
      entry('clock-conversion', 'conditional-lqg-clock-distance-exponent-cancellation', 'lemma', 'Conditional clock-to-distance exponent cancellation',
            'Let gamma,xi>0 and Q>alpha. If mu has local Euclidean mass exponent gamma*(Q-alpha) and a positive distance observable delta(r) has log(delta(r))/log r -> xi*(Q-alpha), then its logarithmic disk potential T(r) satisfies log(T(r))/log(delta(r)) -> gamma/xi. The metric scaling law is an assumption: putting xi=gamma/d_gamma does not calculate d_gamma.',
            ['gamma,xi>0', 'Q>alpha', 'positive Radon mu with mass exponent gamma*(Q-alpha)', 'positive delta with the stated scale exponent'],
            'The logarithmic-potential lemma gives the numerator exponent gamma*(Q-alpha). Divide it by the assumed positive distance exponent xi*(Q-alpha); the common factor cancels. No independence or product of conditional bounds is used.'),
      entry('gmc-potential', 'subcritical-disk-gmc-logarithmic-potential-exponent', 'lemma', 'Subcritical disk GMC logarithmic potential exponent',
            'Fix 0<gamma<2. For the zero-boundary GFF on the unit disk, with covariance singularity log(1/|x-y|), let mu_gamma be the GMC of Lebesgue measure defined by the weak limit of 2^(-n*gamma^2/2) exp(gamma*h_{2^(-n)}(y))dy. Almost surely, for mu_gamma-almost every interior x, the centered logarithmic disk potential T_x(r) has log exponent 2-gamma^2/2. A strictly positive continuous local weight multiplying mu_gamma preserves this conclusion. This is a derived Euclidean-potential corollary, not an exact metric dimension formula.',
            ['unit disk', 'zero-boundary log-normalized GFF', '0<gamma<2', 'dyadic circle-average GMC normalization as stated', 'GMC-almost every interior x'],
            'Falconer--Jin, arXiv:1601.00556v4 Corollary 2.3, applies because the disk satisfies (A0), Lebesgue measure has exact dimension 2, and gamma^2/2<2. It gives positive mass exponent 2-gamma^2/2. Apply the logarithmic-potential lemma. A positive continuous weight is locally bounded above and below; hence weighted mass and potentials are bounded by constant multiples and the null sets agree. See LEMMA_GMC_COROLLARY.md for source and scope.'),
      entry('route-gap', 'lqg-euclidean-clock-route-missing-metric-exponent', 'concept', 'LQG Euclidean clock route: missing metric exponent',
            'DRAFT OPEN GAP, no solution of P0297: the Euclidean local GMC exponent 2-gamma^2/2 fixes a logarithmic-potential clock exponent but does not numerically fix the exponent converting Euclidean disks to actual strong-LQG metric radii. The candidate next step is an explicit noncircular evaluation of b_gamma=lim log D_h(x,partial B_E(x,r))/log r under an appropriate quantum-typical point law. Substituting xi=gamma/d_gamma into the distance scaling law merely returns the unknown d_gamma. Independent review of this route is pending.',
            ['0<gamma<2', 'actual strong LQG metric', 'a specified typical-point law', 'local metric-scale existence and value remain proof obligations']),
      entry('identity-correction', 'lqg-intake-d0049-dimension-identity-correction', 'concept', 'Proposed correction of the D0049 LQG dimension identity',
            'SOURCE CORRECTION PROPOSED, unlanded: D0049-A001 in probability_1000_intake_D_20260908/attempts.jsonl writes d_gamma=2Q/xi in two fields. For the standard metric parameter xi=gamma/d_gamma, the correct relation is d_gamma=gamma/xi. At the established Brownian-map value gamma=4/sqrt(6), xi=1/sqrt(6), Q=5/sqrt(6), the wrong expression is 10 and the correct one is 4. This refutes that recorded identity, not the general dimension problem. Primary support: Gwynne--Miller arXiv:1905.00383v3, equation (1.5) and Problem 7.1. Independent source-row review is pending.',
            ['0<gamma<2', 'standard gamma-LQG metric parameter xi=gamma/d_gamma', 'Q=2/gamma+gamma/2', 'two-field source patch has not been applied'])
    ]
    relations = [
      {'from_key': 'log-potential', 'to_key': 'local-mass', 'kind': 'depends_on', 'rationale': 'The lemma assumes the definition: a finite positive limit of log ball mass divided by log radius.'},
      {'from_key': 'clock-conversion', 'to_key': 'log-potential', 'kind': 'depends_on', 'rationale': 'Apply the potential exponent conclusion with a=gamma*(Q-alpha), then divide by the separately assumed distance exponent.'},
      {'from_key': 'gmc-potential', 'to_key': 'log-potential', 'kind': 'specializes', 'rationale': 'Subcritical disk GMC supplies the positive local exponent a=2-gamma^2/2 required by the deterministic lemma.'},
      {'from_key': 'route-gap', 'to_key': 'clock-conversion', 'kind': 'cites', 'rationale': 'The conditional ratio gamma/xi shows precisely why inserting the unknown xi does not evaluate a metric dimension.'},
      {'from_key': 'route-gap', 'to_key': 'gmc-potential', 'kind': 'cites', 'rationale': 'The known Euclidean potential exponent is the proved part of the route; the actual metric exponent remains missing.'},
      {'from_key': 'route-gap', 'to_existing_logical': TARGET, 'kind': 'cites', 'rationale': 'The route addresses the stored problem of computing the almost-sure Hausdorff dimension of the actual gamma-LQG metric.'},
      {'from_key': 'identity-correction', 'to_existing_logical': TARGET, 'kind': 'cites', 'rationale': 'The corrected parameter identity concerns the same d_gamma as the stored exact-dimension problem; no existing valid attempt card is refuted.'}
    ]
    bundle = {'spec': 'mathbrain-draft-v1', 'author_agent': 'w519',
              'bundle_slug': 'p0297-euclidean-clock-route-and-source-correction-w519-001',
              'entries': entries, 'relations': relations}
    save('bundle_001.json', bundle)
    keys = {e['key']: e for e in entries}
    assert len(keys) == len(entries) <= 200
    names = set()
    required = {'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
    for e in entries:
        assert required <= set(e)
        assert e['kind'] in {'definition','lemma','theorem','concept'}
        assert (isinstance(e['proof_text'],str) and bool(e['proof_text'])) if e['kind'] in {'lemma','theorem'} else e['proof_text'] is None
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
        assert e['logical_name'] not in names
        names.add(e['logical_name'])
        assert e['source']['license'].startswith('owner-own-work')
    graph = {key: [] for key in keys}
    for rel in relations:
        assert rel['from_key'] in keys
        assert rel['kind'] in {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
        if 'to_key' in rel:
            assert rel['to_key'] in keys
            if rel['kind'] == 'depends_on': graph[rel['from_key']].append(rel['to_key'])
    def visit(key, active, done):
        assert key not in active, 'cyclic depends_on'
        if key in done: return
        for child in graph[key]: visit(child, active | {key}, done)
        done.add(key)
    done = set()
    for key in keys: visit(key,set(),done)
    p = Path('~/math-brain-build/local/population/brain.sqlite3')
    conn = sqlite3.connect(p.as_uri()+'?mode=ro',uri=True,timeout=5)
    conn.execute('pragma query_only=ON')
    target = conn.execute("select body from nodes where json_extract(metadata_json,'$.logical_id')=?", (TARGET,)).fetchone()
    assert target is not None, 'unresolved cross-bundle target'
    logical_ids = ['math:'+e['namespace']+':'+e['logical_name'] for e in entries]
    prior = conn.execute("select count(*) from nodes where json_extract(metadata_json,'$.logical_id') in ("+','.join('?' for _ in logical_ids)+')', logical_ids).fetchone()[0]
    conn.close()
    save('PREFLIGHT.json', {'valid':True,'entry_count':len(entries),'relation_count':len(relations),
         'depends_on_acyclic':True,'existing_target_resolved':True,
         'planned_logical_ids_already_present':prior,'prepared_new_draft_entries':len(entries),
         'official_integrator_run':False,'mathematical_proof_certification':False,
         'live_store_writes':0,'excluded_duplicate':'snowflake metric card is left to w520/w521'})
    evidence = []
    for rel in relations:
        to_statement = keys[rel['to_key']]['statement'] if 'to_key' in rel else target[0]
        evidence.append({**rel,'from_statement_quote':keys[rel['from_key']]['statement'],
                         'to_statement_quote':to_statement,'review_state':'unreviewed draft'})
    (ROOT/'RELATION_EVIDENCE.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in evidence),encoding='utf-8')
    hook = {'id':'lqg-dimension-identity-w519-01','area':'math','event':'PreToolUse',
       'cue':'About to promote an identity d_gamma=2Q/xi as valid for the standard gamma-LQG metric, without a refutation or correction label.',
       'fire_when':'D0049-A001 key_identity or method is promoted as a correct relation d_gamma=2Q/xi.',
       'silent_when':'A correction quotes the wrong formula to refute it, or the valid defining relation d_gamma=gamma/xi is used without claiming an explicit gamma formula.',
       'text':'For standard LQG, xi=gamma/d_gamma. Check gamma=4/sqrt(6), xi=1/sqrt(6), Q=5/sqrt(6): 2Q/xi gives 10, while gamma/xi gives the established 4. This corrects an identity; it does not compute general d_gamma.',
       'evidence':'~/brain_workers/w519/CORRECTIONS.md W519-C2; CORRECTION_MEASUREMENTS.json: two bad occurrences -> zero; CHECK_RESULTS.json exact 10-versus-4 control.',
       'proposer':'w519'}
    assert len(hook['text']) <= 300
    hook_line = json.dumps(hook,ensure_ascii=False)+'\n'
    (ROOT/'HOOK_PROPOSAL.jsonl').write_text(hook_line,encoding='utf-8')
    hook_live = '~/primary_directive/hooks1000/proposals/math-w519.jsonl'
    (patches/'02_math_identity_hook_proposal.diff').write_text(f'--- a/{hook_live}\n+++ b/{hook_live}\n@@ -0,0 +1 @@\n+{hook_line}',encoding='utf-8')
    print(json.dumps({'source_patch_fields':fields,'bad_formula_before':2,'bad_formula_after':0,
                      'draft_entries':len(entries),'draft_relations':len(relations),'existing_target_resolved':True,'existing_planned_ids':prior}))


if __name__ == '__main__':
    main()
