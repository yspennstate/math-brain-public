import json
from pathlib import Path
root = Path(__file__).resolve().parent
row = {'row_id': 'S1.O.w333.002', 'problem_id': 'P0189', 'result_type': 'lemma', 'label': 'proof; independent audit pending', 'statement': 'For q>=2, a primitive qth root omega, and c^q=-1, the cyclic rotation matrices U e_k=omega^k e_k and V e_k=c e_(k-1 mod q) satisfy det(zI-U-V)=z^q and (U+V)^q=0.', 'proof_path': (root / 'proofs/P0189.md').as_posix(), 'source_path': '~/<private-repo>/12_cognitive_architecture/audits/evidence/2026/09/09/probability-written-proofs/P0189_brown_measure_strong_convergence_counterexample_candidate.md', 'source_quote': 'The former contributes ... z^{q_j}-1 ... The latter contributes minus the product of the cyclic weights, namely -exp(pi*i)=+1.', 'audit_status': 'PENDING w347', 'scope': 'Finite algebra only; Brown-measure dependency not certified by this row.'}
with (root / 'results.jsonl').open('a', encoding='utf-8') as f:
    f.write(json.dumps(row, ensure_ascii=False) + '\n')
print(row['row_id'], 'saved')
