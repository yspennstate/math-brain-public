"""Select only the ten assigned IDs from cited ledgers and a read-only store."""
import json
import pathlib
import sqlite3

root = pathlib.Path(__file__).resolve().parent
research = pathlib.Path('~/<private-repo>/06_math_research')
ids = ['P0174', 'P0389', 'C0089', 'P0030', 'P0234', 'C0010', 'C0068', 'C0101', 'C0148', 'P0022']
topics = {'P0174':'support-diameter threshold', 'P0389':'mesoscopic hyperuniformity', 'C0089':'walk on the vacant set', 'P0030':'forward and backward Brownian', 'P0234':'extended initial color seeds', 'C0010':'ergodic uniformly elliptic', 'C0068':'giant component above the scaling', 'C0101':'Maximal integer superharmonic', 'C0148':'Cayley graphs and soficity', 'P0022':'Percolation dimension'}
packets = {pid: {'id': pid, 'ledger_rows': [], 'store_cards': []} for pid in ids}
for folder in research.glob('probability_1000_intake_*'):
    for filename in ['problems.jsonl', 'attempts.jsonl']:
        path = folder / filename
        if not path.is_file():
            continue
        with path.open(encoding='utf-8-sig') as stream:
            for lineno, line in enumerate(stream, 1):
                matched = [pid for pid in ids if '"' + pid + '"' in line]
                if matched:
                    obj = json.loads(line)
                    for pid in matched:
                        packets[pid]['ledger_rows'].append({'path': str(path), 'line': lineno, 'record': obj})
con = sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro', uri=True)
con.row_factory = sqlite3.Row
for pid in ids:
    for row in con.execute("SELECT id, kind, title, body, metadata_json FROM nodes WHERE body LIKE ? OR title LIKE ? OR title LIKE ? LIMIT 12", ('%' + pid + '%', '%' + pid + '%', '%' + topics[pid] + '%')):
        packets[pid]['store_cards'].append(dict(row))
con.close()
out = root / 'reports'
out.mkdir(exist_ok=True)
for pid, packet in packets.items():
    (out / (pid + '_sources.json')).write_text(json.dumps(packet, indent=2, ensure_ascii=False), encoding='utf-8')
    print(pid, 'ledger_rows', len(packet['ledger_rows']), 'store_cards', len(packet['store_cards']))
source_ids = {'free_unimodality_2018', 'free_unimodality_journal_2018', 'heydenreich_hofstad_highd_2017', 'biskup_dgff_extrema_2020', 'levine_peres_sandpiles_2017', 'pete_pgg_notes'}
for folder in research.glob('probability_1000_intake_*'):
    path = folder/'sources.jsonl'
    if path.is_file():
        for line in path.open(encoding='utf-8-sig'):
            obj = json.loads(line)
            if obj.get('source_id') in source_ids:
                print('SOURCE', str(path), json.dumps(obj, ensure_ascii=False))
for pid in ids:
    for card in packets[pid]['store_cards']:
        if not card['title'].startswith('Attempt') and pid != 'P0174':
            print('MATCHED CARD', pid, card['title'], card['body'][:2200])
