import json
from pathlib import Path
p=Path(r'~\brain_workers\FEI100_20261011\agents\A051\runs\20261011T233123Z-fleet05-A051-near-extremizer-definition')
for fn in ('AGGREGATE_CERTIFICATES.json','full_SUMMARY.json','SEEDED_FULL_SUMMARY.json'):
    x=json.loads((p/'out'/fn).read_text()); print(fn, str(x)[:4500])
for fn in ('full_case_0000.json','seed_Hod_g3.json'):
    x=json.loads((p/'out'/fn).read_text()); print(fn,'keys',list(x))
    print({k:(str(v)[:1400]) for k,v in x.items() if k!='blocks'})
