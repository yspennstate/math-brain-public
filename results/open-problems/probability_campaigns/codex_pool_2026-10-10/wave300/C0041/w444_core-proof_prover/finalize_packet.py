import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()

def save(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

status = {
    'candidate_id': 'C0041', 'checked_at': now, 'worker': 'w444', 'reviewer': 'w446',
    'current_openness': 'UNKNOWN', 'parent_problem_solved': False,
    'exact_primary_statement': {
        'status': 'RECOVERED', 'source_id': 'drewitz_ramirez_rwre_2014',
        'url': 'https://arxiv.org/pdf/1309.2589',
        'locator': 'Open Question 2.20, PDF page 24 (zero-based 23), printed page 22',
        'intake_locator': 'Open question 2.20, p. 24',
        'assumptions': ['d>=2', 'nearest-neighbor RWRE on Z^d', 'sampled-once iid site transition rows', 'a deterministic kappa>0 lower bound on every allowed transition almost surely', 'fixed unit ell', 'annealed P_0(X_n dot ell -> +infinity)=1'],
        'conclusion': 'P_0(liminf_n (X_n dot ell)/n>0)=1',
        'source_quote': 'Is the RWRE necessarily ballistic in direction l?',
        'corroboration': {'url': 'https://arxiv.org/html/1212.4020v3', 'locator': 'Conjecture 1.1 and immediately preceding definitions'},
    },
    'prior_attempt_digest': {
        'id': 'C0041-A001', 'date': '2026-09-07',
        'path': '~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl',
        'line': 32, 'method': 'Planar directional zero-one law plus regeneration structure',
        'result': 'Unsolved; regeneration-time integrability remained unproved',
        'gap': 'Qualitative iid trap rarity did not give an integrable regeneration-duration tail',
        'current_delta': 'Explicit inward-row entropy, weighted box exit moments, adaptive union bound, and a future-dependent-time radius-to-duration reduction with a separate extra radius assumption',
    },
    'bounded_historical_checks': {
        'H_20260912': 'No C0041-specific hit from the named bounded search',
        'I_20260914': 'No C0041-specific hit from the named bounded search',
        'lean_20260908': 'Annotated ranking only; no C0041 formal proof receipt found',
        'team_O': 'No C0041 row in the cited board',
        'population_store': 'Read-only title lookup found the dated open-question card and an unverified private reduction',
        'global_owner_solved_retired_status': 'UNKNOWN; these checks are not exhaustive and the separate canonical research-store path was not verified',
        'evidence': ['REPORT_SOURCE_RECORDS.json', 'REPORT_STORE_CHECK.json'],
    },
    'recent_primary_claim': {
        'url': 'https://github.com/openai/math/blob/main/lean/docs/220.md',
        'paper_url': 'https://github.com/openai/math/blob/main/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf',
        'announcement': 'Claims a full resolution for sampled-once iid uniformly elliptic nearest-neighbor RWRE, d>=2',
        'comparator_url': 'https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DirectionalBallisticity.lean',
        'comparator_observation': 'The main theorem declaration ends in sorry (file lines 87-88 as read)',
        'receipt_class': 'STATEMENT_ONLY_COMPARATOR; not an audited kernel proof',
        'actual_proof_and_trusted_axioms': 'NOT_VERIFIED; delegated narrowly to w446',
        'disposition': 'The comparator placeholder neither certifies nor refutes any separate proof; no current openness or novelty claim is made',
    },
    'memory_scar': {'slug': 'perceptron_proof_open_gaps_fleet_2026_07_12', 'recall': 'TIMEOUT_60S', 'fallback': 'Read the exact named scar after targeted index grep'},
    'hardest_remaining_lemma': 'E_{P_0(.|D^ell=infinity)}[tau_1]<infinity for genuine time-valued regeneration under only the original hypotheses',
    'brain_state': json.loads((ROOT / 'SUBMISSION_STATUS.json').read_text(encoding='utf-8')),
}
save('SOURCE_STATUS.json', status)
store = json.loads((ROOT / 'REPORT_STORE_CHECK.json').read_text(encoding='utf-8'))
target = next(row for row in store['matched_nodes'] if 'Open problem:' in row['title'])
edge = {
    'from_key': 'remaining-gap',
    'to_existing_logical': 'math:probability.randomenvironment:open-problem-c0041-transience-in-a-direction-implies-ballisticity-for-uniformly-elliptic',
    'kind': 'semantic_association', 'status': 'DRAFT; independent review pending',
    'from_quote': next(entry['statement'] for entry in json.loads((ROOT / 'bundle_001.json').read_text(encoding='utf-8'))['entries'] if entry['key'] == 'remaining-gap'),
    'to_quote': target['body_excerpt'], 'to_node_id': target['id'],
    'source': 'Drewitz-Ramirez Open Question 2.20 and the read-only captured card',
    'remaining_gap': 'Association identifies the target only; it is not an implication closing the unproved input.',
}
(ROOT / 'RELATION_EVIDENCE.jsonl').write_text(json.dumps(edge, ensure_ascii=False) + '\n', encoding='utf-8')
files = ['ATTEMPT.md', 'CLAIMS.jsonl', 'SOURCE_STATUS.json', 'AUTHOR_MODEL_EVIDENCE.json', 'REVIEW_PACKET.md', 'REPORT.md']
save('REVIEW_HASHES.json', {
    'created_at': now, 'purpose': 'Byte identity for mathematical review only; not a proof receipt or bundle manifest',
    'files': [{'path': str(ROOT / name), 'sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest()} for name in files],
})
print(json.dumps({'source_statement': 'RECOVERED', 'openness': 'UNKNOWN', 'review_files_frozen': len(files), 'parent_solved': False}))
