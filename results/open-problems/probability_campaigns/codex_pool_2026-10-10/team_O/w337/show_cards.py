from pathlib import Path
import json
import sys
cards=json.loads((Path(__file__).resolve().parent/'evidence'/'store_cards.json').read_text(encoding='utf-8'))
for c in cards:
    if c['problem_id'] in sys.argv[1:]:
        print(json.dumps({k:c[k] for k in ['problem_id','title','body']},ensure_ascii=False))
