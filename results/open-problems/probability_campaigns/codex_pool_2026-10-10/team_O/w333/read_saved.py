import json
from pathlib import Path
root = Path(__file__).resolve().parent
cards = json.loads((root / 'evidence/store_cards.json').read_text(encoding='utf-8'))
for pid in ['P0189','P0390','P0031','P0242','C0011','C0070','C0105','C0153','P0025']:
    print('\nPROBLEM', pid)
    for card in cards[pid]:
        if card['kind'] != 'claim':
            continue
        if 'Attempt on' in card['title'] or 'Resolved:' in card['title'] or pid=='P0390':
            print(json.dumps({'title': card['title'], 'body': card['body'], 'logical_id': card['metadata'].get('logical_id'), 'source_id': card['metadata'].get('source_id')}, ensure_ascii=False))
