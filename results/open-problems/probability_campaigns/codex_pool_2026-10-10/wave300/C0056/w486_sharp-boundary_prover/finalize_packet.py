"""Validate and freeze local review artifacts; never integrate or modify a live store."""
import ast
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
receipt_path = Path('~/brain_workers/w487/AUDIT_W486.json')
adversary_text = receipt_path.read_text(encoding='utf-8-sig')
adversary = json.loads(adversary_text)
(ROOT / 'ADVERSARY_RECEIPT.json').write_text(adversary_text, encoding='utf-8')
assert adversary['scoped_verdict'] == 'KEEP' and not adversary['parent_problem_solved']
measurements = json.loads((ROOT / 'MEASUREMENTS.json').read_text(encoding='utf-8'))
gate = json.loads((ROOT / 'GATE_RECEIPT.json').read_text(encoding='utf-8'))
bundle = json.loads((ROOT / 'bundle_002.json').read_text(encoding='utf-8'))
submission = json.loads((ROOT / 'BRAIN_SUBMISSION.json').read_text(encoding='utf-8'))
live_draft = Path('~/math-brain-inbox/w486/bundle_002.json')
assert live_draft.read_bytes() == (ROOT / 'bundle_002.json').read_bytes()
for item in bundle['entries']:
    for field in ('source_id', 'url', 'revision', 'license'):
        assert isinstance(item['source'][field], str) and item['source'][field].strip()
claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert len(claims) == 3
for claim in claims:
    assert claim['status'] == 'proved special case'
    claim['adversarial_review'] = {'id': 'w487', 'verdict': 'scoped KEEP',
                                 'receipt': str(receipt_path), 'served_identity': 'UNKNOWN',
                                 'clarification_applied': 'all-sites support-bound event made explicit'}
(ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')
for path in ROOT.glob('*.py'):
    ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
for path in ROOT.glob('*.json'):
    json.loads(path.read_text(encoding='utf-8-sig'))
for path in ROOT.glob('*.jsonl'):
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.strip():
            json.loads(line)
hook = json.loads((ROOT / 'HOOK_PROPOSALS.jsonl').read_text(encoding='utf-8'))
cue = re.compile(hook['cue'])
assert cue.search(hook['fire_when'])
assert not cue.search(hook['silent_when'])
assert not cue.search('Checking the C0056 source and native review metadata.')
assert len(hook['text']) <= 300
diff_lines = (ROOT / 'patches/01_born_boundary_hook.diff').read_text(encoding='utf-8').splitlines()
added = '\n'.join(line[1:] for line in diff_lines[3:] if line.startswith('+')) + '\n'
assert added == (ROOT / 'HOOK_PROPOSALS.jsonl').read_text(encoding='utf-8')
sources = json.loads((ROOT / 'SOURCE_STATUS.json').read_text(encoding='utf-8'))
sources['store_scope_receipt'] = 'STORE_SCOPE.json (mode=ro; prior attempt remains unverified)'
sources['source_snapshot_hashes'] = {
    'bourgade_intake_pdf_sha256': 'b8b15c02ac7b675471097e9c499a6d588cfd7b0c591c49b0135f2a42eaedddb0',
    'bourgade_intake_extracted_sha256': '94becc31961db4aac94611aa72da6eb502984d68650e03a539e8340255dc49bd',
    'origin': 'Existing sources.jsonl:7 receipt; no new PDF-byte verification claimed',
}
(ROOT / 'SOURCE_STATUS.json').write_text(json.dumps(sources, indent=2) + '\n', encoding='utf-8')

if measurements['status'] == 'PASS':
    assert gate['allowed'] and measurements['geometry_checks'] == 15 and measurements['power_checks'] == 12
    power_examples = {str(p['eta']): p['term_norm'] for p in measurements['powers'] if p['order'] == 8}
    validation = (f"The fresh gate allowed the bounded check. Fifteen cutoff checks and twelve finite-Fourier power checks passed in {measurements['elapsed_seconds']:.3f} s; maximum cutoff identity error {measurements['max_geometry_absolute_error']:.3g}. "
                  f"At lambda=0.1, order-eight term norms are {power_examples['0.05']:.6g} at eta=0.05, {power_examples['0.1']:.6g} at eta=0.1, and {power_examples['0.2']:.6g} at eta=0.2. "
                  "These are finite sanity checks of the proof, not an ac/GOE test or a formal certificate.")
else:
    validation = 'The fresh compute gate held the optional numerical checks. No numerical improvement claim is made; the complete analytic proof is available.'

report = (
    '# w486 review handoff, 2026-10-10\n\n'
    'I proved a sharp auxiliary obstruction for C0056: for bounded iid lattice disorder with M=esssup|V|, the unrenormalized Born resolvent series converges in infinite-lattice operator norm exactly when eta>lambda M. Rare almost-constant cubes establish necessity, including the equality endpoint. Centering does not reduce the expected term norms. This sharpens a sufficient norm estimate into an exact threshold; it proves neither the original ac-spectrum assertion nor GOE statistics.\n\n'
    + validation + '\n\n'
    'Run the check with: python -B -X utf8 ~/brain_workers/w486/run_gated_checks.py . The helper reads the actual fresh governor and holds computation on distress. No resource gate was changed. The local JSON/Python syntax, bundle references/license/dependency graph, identical submitted bytes, hook fire/silent cases and hook diff round trip also passed.\n\n'
    'w487 returned scoped native KEEP for L1-L3. I applied its all-sites support-bound clarification. Primary referee w488 is pending; response-side served identities and login independence are UNKNOWN, so the different-model/login gate remains unmet. The recent September primary manuscript makes current openness UNKNOWN; it claims the uniform-law spectral component and does not discharge the intake GOE clause.\n\n'
    'Brain delivery: five definition/concept entries and four internal supported relations in ~/math-brain-inbox/w486/bundle_002.json, using owner-own-work. Use version 002: the preserved version 001 has an invalid null source.url and must not be integrated. Submitted=true, reviewed=false, ingested=false, retrievable=false. No live store or recall control was changed. The main misuse risk is treating an operator-norm route obstruction as a spectral-type theorem, or treating native review/finite tests as model-verified or formal proof.\n\n'
    'Apply line: after the needed review gates, the validating coordinator may ingest the named DRAFT bundle using its normal integration workflow. The reviewer may apply patches/01_born_boundary_hook.diff to its named proposal path; the scoped write rule keeps the global hook proposal unmodified by this worker.\n\n'
    'NEXT: w488 checks the frozen L1-L3 packet, records exact scope and identity evidence, then routes any kept draft material to integration.\n'
)
(ROOT / 'REPORT.md').write_text(report, encoding='utf-8')
checks = {'syntax_json_bundle_hook_checks': 'PASS', 'hook_fire_controls': 1,
          'hook_silent_controls': 2, 'source_rows': 2, 'author_claims': 3,
          'draft_entries': len(bundle['entries']), 'draft_relations': len(bundle['relations']),
          'numerical_status': measurements['status'], 'live_store_modified': False}
(ROOT / 'VALIDATION.json').write_text(json.dumps(checks, indent=2) + '\n', encoding='utf-8')
artifact_names = ['ATTEMPT.md', 'CLAIMS.jsonl', 'SOURCE_STATUS.json', 'SOURCE_ROWS.jsonl',
                  'GAP.md', 'REVIEW_PACKET.md', 'REVIEW_STATE.json', 'ADVERSARY_RECEIPT.json',
                  'REPORT.md', 'MEASUREMENTS.json', 'GATE_RECEIPT.json', 'VALIDATION.json',
                  'STORE_SCOPE.json', 'bundle_002.json', 'BRAIN_SUBMISSION.json',
                  'verify_geometry.py', 'run_gated_checks.py', 'HOOK_PROPOSALS.jsonl',
                  'patches/01_born_boundary_hook.diff']
hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in artifact_names}
(ROOT / 'ARTIFACT_HASHES.json').write_text(json.dumps(hashes, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'validation': checks, 'proof_sha256': hashes['ATTEMPT.md'],
                  'claims_sha256': hashes['CLAIMS.jsonl'], 'bundle_sha256': hashes['bundle_002.json'],
                  'identity_gate': 'not satisfied', 'parent_problem_solved': False}))
