import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'out/CENSUS.json').read_text())
for row in d['rows']:
    if row['n']==3:
        print('p=',row['p'],'masks=',row['witness_masks'],'tables=',row['witness_child_tables'],'Walsh=',row['witness_integer_Walsh'])
        print('max=',row['max_debt']['display'],'excluded separation=',row['noncandidate_separation_lower'])
for w in d['real_witnesses']:print('real p=',w['p'],'x=',w['x'],'debt=',w['debt']['display'],'gap=',w['gap_above_Boolean_upper'])
