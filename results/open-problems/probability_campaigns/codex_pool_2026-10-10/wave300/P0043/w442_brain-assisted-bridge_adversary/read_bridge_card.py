import json
import time
from pathlib import Path
from math_source_fallback import lookup

ROOT = Path(__file__).resolve().parent
node_id = 'claim_5df2b62b583a156268141fc66e8bdf6bca069daa8e9dcd6daf40af92ed7320a5'
result = lookup(Path('~/math-brain-build/local/population/brain.sqlite3'), [], node_id=node_id)
(ROOT/'BRIDGE_CARD.json').write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
receipt = json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
receipt['narrow_title_abstention'] = {'title_terms':['critical percolation','quasi-transitive'],
                                    'sql_budget_seconds':2.0, 'error':'sqlite3.OperationalError: interrupted',
                                    'exact_wall_seconds':None, 'hit_count':0}
receipt['exact_bridge_card'] = {k:v for k,v in result.items() if k!='hits'}
receipt['broad_query_limitation'] = 'Broad title lookup is unranked and returns FPP and generic decay candidates too; only the complete finite exploration-domination concept card is used for the bridge-hypothesis comparison.'
(ROOT/'MEASUREMENTS.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False))
