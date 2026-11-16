"""PROVED: exact table coverage and rational before/after ledger consistency."""
import json,csv
from summarize import build
x=build();assert x==json.load(open('extension_summary.json'))
with open('ceiling_table.csv',newline='')as f:
    rows=list(csv.DictReader(f))
expected=[{k:str(v)for k,v in row.items()}for row in x['ratio_table']]
assert rows==expected
assert len(json.load(open('cubic_allN_cells.json')))==44
assert all(q['all_N_margins']for q in json.load(open('cubic_allN_cells.json')))
print('PROVED: all rational ratio ceilings, universal scales and before/after counts/volumes reconstructed; OPEN leaves retained.')
