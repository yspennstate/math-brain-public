import json
from pathlib import Path

path = Path(__file__).with_name('CLAIMS.jsonl')
existing = {json.loads(line)['id'] for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()}
rows = [
    {
        'id': 'P0043-w434-winding-core',
        'statement': 'Let a triangulated disk carry a projective line at each vertex. If neighboring lines differ by less than pi/8 in projective angle, their doubled-angle boundary winding is zero. In particular, this is incompatible with boundary lines within pi/16 of a minor-axis line rotating once in projective angle along the boundary, provided the boundary mesh is fine enough to track that rotation.',
        'assumptions': ['finite triangulation of a disk', 'edge projective-angle differences less than pi/8', 'boundary closeness and mesh as stated'],
        'source': {'paper': 'OpenAI 2026-09-24 P0043 preprint, Proposition 8.1 no-strip case', 'own_proof': '~/brain_workers/w434/ATTEMPT.md, Independent attempt on Proposition 8.1'},
        'proof_or_counterexample': 'Double the projective angles. Principal edge increments have magnitude less than pi/4. Their sum around each triangular face is a multiple of 2pi of magnitude less than 3pi/4, hence zero; interior edges cancel. The boundary is consequently zero-winding, whereas closeness to the rotating minor axis and a fine boundary mesh give winding one.',
        'independent_reviewer': 'w437 requested; verdict pending',
        'remaining_gap': 'This combinatorial core does not establish boundary localization, the strip case, endpoint constants, fixed-seed parameter order, or full Proposition 8.1.',
        'status': 'proved special case'
    },
    {
        'id': 'P0043-w434-conditional-exploration',
        'statement': 'In the paper\'s adaptive exploration, assume the incoming and both outgoing corridors are fresh as required by Lemma 9.1, the parent prediction is at least 1-delta, and each of L+1 relay pairs has hit-and-next-miss probability at most kappa. Then each tested site has conditional failure probability at most delta+2(L+1)kappa/delta. Assuming the paper\'s oriented-boundary geometry, if this is at most epsilon and sum over ell>=1 of 4^ell epsilon^(ell/4) is below 1, an infinite good set has positive probability.',
        'assumptions': ['Proposition 8.1 directional inputs', 'Lemma 9.1 fresh corridor geometry', 'Proposition 9.2 transfer bound', 'finite seed and the oriented-boundary count'],
        'source': {'paper': 'OpenAI 2026-09-24 P0043 preprint, Proposition 9.3', 'own_proof': '~/brain_workers/w434/ATTEMPT.md, Conditional audit of the adaptive exploration'},
        'proof_or_counterexample': 'First hit followed by final miss has an adjacent hit/miss relay pair, so a union bound gives (L+1)kappa. Conditional expectation over the fresh outgoing corridor, Markov at delta, and two children give the one-site bound. Iterating conditional bounds for specified failed sites gives epsilon^k; a finite good set forces a root boundary trail of length ell with at least ell/4 distinct failures, and there are at most 4^ell trails.',
        'independent_reviewer': 'w437 requested; verdict pending',
        'remaining_gap': 'The fresh-corridor geometry and upstream directional and contact-shell transfer premises are unverified here; this is a conditional reduction, not a P0043 proof.',
        'status': 'proved special case'
    }
]
with path.open('a', encoding='utf-8', newline='\n') as out:
    for row in rows:
        if row['id'] not in existing:
            out.write(json.dumps(row, ensure_ascii=False) + '\n')
print(f'claims={sum(1 for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip())}; new={sum(row["id"] not in existing for row in rows)}')
