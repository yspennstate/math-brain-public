"""Reuse own read-only complete-report collector with current critical sources."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
old=ROOT.parents[1]/'runs/20261023T010221Z-account03-A096-live-gap-ledger/code/intake.py'
s=old.read_text(encoding='utf-8')
insert="""critical.update({'A096':'20261023T053800Z-account03-A096-live-gap-ledger','A085':'20261023T112613Z-account03-A085-certificate-adversary','A097':'20261023T062140Z-account03-A097-cross-route-transfer','A094':'20261023T110024Z-account03-A094-proof-chain-challenger'})
for packet in ('A003','A004','A079','A082','A090','A093','A098','A099','A011'):
 folders=[p for p in (BASE/'agents'/packet/'runs').iterdir() if p.is_dir() and (p/'REPORT.md').exists()]
 if folders:critical[packet]=max(folders,key=lambda p:p.name).name
"""
s=s.replace('for packet,run in critical.items():',insert+'\nfor packet,run in critical.items():')
exec(compile(s,str(Path(__file__).resolve()),'exec'),globals())
