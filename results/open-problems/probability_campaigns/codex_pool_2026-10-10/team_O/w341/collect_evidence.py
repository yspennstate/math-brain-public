"""Read only the assigned ledger rows and matching live cards; save a local report."""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGETS = {
    'P0288': ['rank-two polynomial', 'Pollett Section 2'],
    'C0034': ['Coupling of determinantal', 'union marginal', 'union-marginal'],
    'C0151': ['Szegedy', 'Independent-set densities', 'Rahman'],
    'P0127': ['sampling of lattice trees', 'uniform sampling of lattice'],
    'P0456': ['fine connectivity window', 'bilateral preference'],
    'C0058': ['peeling algorithm exploring site', 'site-percolation peeling'],
    'C0082': ['first coefficient', 'first differing coefficient', 'coefficients a_i'],
    'C0126': ['oriented percolation in dimensions', 'oriented IIC'],
    'P0014': ['random circulant'],
    'P0042': ['characterization of amenable', 'bootstrap thresholds', 'bootstrap percolation characterize'],
}

def main():
    out = ROOT / 'reports'
    out.mkdir(exist_ok=True)
    con = sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro', uri=True)
    cards = {}
    for pid, terms in TARGETS.items():
        where = ' OR '.join('(title LIKE ? OR body LIKE ?)' for _ in terms)
        args = [v for term in terms for v in ('%'+term+'%', '%'+term+'%')]
        rows = con.execute('SELECT id,title,body,metadata_json FROM nodes WHERE kind=\'claim\' AND ('+where+') ORDER BY created_at DESC LIMIT 3', args).fetchall()
        selected = []
        for nid, title, body, raw in rows:
            meta = json.loads(raw)
            selected.append({'node_id': nid, 'title': title, 'body': body, 'logical_id': meta.get('logical_id'), 'source_id': meta.get('source_id'), 'source_revision': meta.get('source_revision'), 'truth_status': meta.get('truth_status'), 'proof_text': meta.get('proof_text')})
        cards[pid] = selected
        print(pid, 'cards', len(selected), flush=True)
        for r in selected:
            print(json.dumps({k:r[k] for k in ('logical_id','title','source_id','truth_status')}), flush=True)
            print(r['body'][:1450], flush=True)
    con.close()
    (out / 'existing_cards.json').write_text(json.dumps(cards, indent=2, ensure_ascii=False), encoding='utf-8')
    base = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
    ledger = {}
    for name in ('problems.jsonl', 'attempts.jsonl'):
        selected = []
        with (base/name).open(encoding='utf-8') as f:
            for line_no, line in enumerate(f,1):
                if not any(('"'+pid+'"') in line for pid in TARGETS):
                    continue
                row = json.loads(line)
                if row.get('problem_id') in TARGETS:
                    row['_path'] = str(base/name)
                    row['_line'] = line_no
                    selected.append(row)
        ledger[name] = selected
    (out/'assigned_ledger_rows.json').write_text(json.dumps(ledger, indent=2, ensure_ascii=False), encoding='utf-8')
    print('Saved targeted cards and ledger reports.', flush=True)

if __name__ == '__main__':
    main()
