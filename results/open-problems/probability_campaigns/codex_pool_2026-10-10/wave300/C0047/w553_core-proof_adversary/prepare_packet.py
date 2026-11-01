"""Prepare scoped proof receipts, a ledger annotation patch, and draft checks."""
from pathlib import Path
from fractions import Fraction
import difflib
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parent
def save(name, data):
    (ROOT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

bundle = json.loads((ROOT / 'bundle_001.draft.json').read_text(encoding='utf-8'))
claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
keys = {entry['key'] for entry in bundle['entries']}
assert len(keys) == len(bundle['entries'])
assert bundle['spec'] == 'mathbrain-draft-v1'
allowed = {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
for entry in bundle['entries']:
    assert entry['kind'] in {'definition','concept'}, 'Unreviewed drafts must not be promoted'
    assert entry['proof_text'] is None
    assert entry['source']['license'].startswith('owner-own-work')
    assert all(term not in entry['statement'].lower() for term in ('c:/', 'c:\\', 'w553', 'w552', 'w554'))
for edge in bundle['relations']:
    assert edge['from_key'] in keys and edge['kind'] in allowed
    assert ('to_key' in edge) != ('to_existing_logical' in edge)
    if 'to_key' in edge:
        assert edge['to_key'] in keys
required = {'statement','assumptions','source','proof_or_counterexample','independent_reviewer','remaining_gap','status'}
for claim in claims:
    assert required <= claim.keys()
assert len({claim['claim_id'] for claim in claims}) == len(claims)

gate_path = Path('~/.claude/compute/compute_state.json')
gate = json.loads(gate_path.read_text(encoding='utf-8-sig'))
gate_record = {key: gate.get(key) for key in ('ts','mode','status','reasons','cpu_pct','mem_avail_mb','commit_eff_avail_mb','commit_eff_used_pct')}
gate_record['age_seconds'] = time.time() - gate_path.stat().st_mtime
gate_record['scope'] = 'Scalar rational arithmetic and artifact validation only; no enumeration, simulation, models, GPU or build.'
light_ok = (gate_record['age_seconds'] <= 60 and gate.get('status') != 'distress'
            and gate.get('mode') not in {'pause','stop','distress'}
            and (gate.get('mem_avail_mb') or 0) > 4096
            and (gate.get('commit_eff_avail_mb') or 0) > 16384
            and (gate.get('commit_eff_used_pct') or 100) < 85
            and (gate.get('cpu_pct') or 100) < 90)
gate_record['light_arithmetic_allowed'] = light_ok
gate_record['heavy_experiments_allowed'] = False
save('MEASUREMENT_GATE.json', gate_record)
checks = {'structural': {'draft_entries':len(bundle['entries']), 'supported_relations':len(bundle['relations']), 'claim_rows':len(claims), 'unreviewed_theorem_promotions':0}, 'gate':gate_record, 'arithmetic':[]}
if light_ok:
    cpu_start = time.process_time()
    p = Fraction(3,4)
    for radius in (1,2,4,8,16):
        direct = 1 + 4*p*p*sum((3*p*p)**j for j in range(radius))
        closed = 1 + Fraction(36,11)*(Fraction(27,16)**radius - 1)
        assert direct == closed
        checks['arithmetic'].append({'case':'tree_squared_row', 'radius':radius, 'exact':str(direct), 'decimal':float(direct), 'pass':True})
    assert Fraction(1,12)<1<Fraction(4,3)
    checks['arithmetic'].append({'case':'spectral_degree_factor','old_rho_pc_squared':'1/12','correct_d_rho_pc_squared':'4/3','old_test_accepts':True,'correct_test_accepts':False,'pass':True})
    joint = Fraction(1,2)**4
    product = Fraction(1,2)**6
    assert joint == 4*product
    checks['arithmetic'].append({'case':'two_paths_shared_two_edges','joint':str(joint),'marginal_product':str(product),'ratio':4,'pass':True})
    assert Fraction(17,13) < Fraction(4,3)
    checks['arithmetic'].append({'case':'p_zero_sprinkling_tree_control','epsilon':'1/16','schur_bound':'17/13','sprinkling_bound':'4/3','pass':True})
    checks['arithmetic_cpu_seconds'] = time.process_time()-cpu_start
else:
    checks['arithmetic_status'] = 'DEFERRED_BY_FRESH_LOCAL_GATE; symbolic derivations remain in ATTEMPT.md'
save('CHECKS.json', checks)

ledger = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl')
replacement = ('The cited Benjamini-Schramm Theorem 4 requires k*rho*p<1 at a percolating parameter p, '
               'where k is maximal degree and rho is the simple-random-walk spectral radius. '
               'Thus k*rho*pc<1 is sufficient for pc<pu; for a d-regular Cayley graph this is pc*||A||<1. '
               'Nonamenability gives rho<1 but does not supply this sufficient condition for every fixed generating set. '
               'The universal target is not proved by this source correction.')
for line_number, line in enumerate(ledger.open(encoding='utf-8'), 1):
    if 'C0047-A001' not in line:
        continue
    original = json.loads(line)
    if original.get('attempt_id') != 'C0047-A001':
        continue
    annotated = dict(original)
    annotated['correction_note'] = 'DRAFT source normalization FIX: the attributed SRW criterion omits maximal degree k. Preserve the original attempt as historical text; use the checked replacement after review.'
    annotated['source_checked_replacement'] = replacement
    annotated['correction_source'] = 'https://emis.de/ft/41630, Theorem 4, printed p.76; nonplanar bond extension printed p.72'
    annotated['correction_status'] = 'draft_pending_required_independent_source_review'
    new_line = json.dumps(annotated,ensure_ascii=False,sort_keys=True)+'\n'
    relative = '<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl'
    patch = ''.join(difflib.unified_diff([line],[new_line],fromfile='a/'+relative,tofile='b/'+relative,n=0))
    patch = patch.replace('@@ -1 +1 @@',f'@@ -{line_number} +{line_number} @@')
    (ROOT/'patches').mkdir(exist_ok=True)
    (ROOT/'patches/01_c0047_spectral_source_annotation.diff').write_text(patch,encoding='utf-8')
    save('SOURCE_ROW_CORRECTION.json', {'status':'DRAFT','verdict':'FIX','live_file':str(ledger),'line':line_number,'attempt_id':'C0047-A001','original_row_sha256':hashlib.sha256(line.encode('utf-8')).hexdigest(),'replacement':replacement,'source_quote':'rho(G)kp < 1','existing_store_card':'claim_77d417df1817eac0893d67dcfcf0d7140581f4e26ce07c31919403d44d301960','existing_logical':'math:probability.statmech:attempt-c0047-benjamini-schramm-conjecture-p-c-p-u-if-and-only-if-the-group-is-non-a','preserve_history':True,'review_gate':'Required independent source review and coordinator store revision; no store mutation by this worker'})
    break
else:
    raise RuntimeError('Exact named prior row not found')

receipt = []
for path in (ROOT/'ATTEMPT.md', ROOT/'PROVER_AUDIT.md', ROOT/'PRIOR_WORK_CORRECTION.md', Path('~/brain_workers/w552/ATTEMPT.md')):
    data = path.read_bytes()
    receipt.append({'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'purpose':'artifact identity only, not proof validation'})
save('REVIEW_ARTIFACT_RECEIPT.json', receipt)
print(json.dumps({'structural':checks['structural'],'exact_arithmetic_checks':len(checks['arithmetic']),'arithmetic_cpu_seconds':checks.get('arithmetic_cpu_seconds'),'light_gate':light_ok,'patch':'patches/01_c0047_spectral_source_annotation.diff'},ensure_ascii=False))
