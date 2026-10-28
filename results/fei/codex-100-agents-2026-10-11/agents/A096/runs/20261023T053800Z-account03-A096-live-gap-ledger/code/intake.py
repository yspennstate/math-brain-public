"""Use own full-report intake, with this stage's source locators."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
old=ROOT.parents[1]/'runs/20261023T010221Z-account03-A096-live-gap-ledger/code/intake.py'
s=old.read_text(encoding='utf-8')
s=s.replace("'20261021T232544Z-account03-A097-cross-route-transfer'","'20261023T021120Z-account03-A097-cross-route-transfer'")
s=s.replace("'20261022T234859Z-account03-A085-certificate-adversary'","'20261023T043959Z-account03-A085-certificate-adversary'")
s=s.replace("'20261022T232833Z-account03-A050-repair-with-scope'","'20261023T042019Z-account03-A050-repair-with-scope'")
s=s.replace("for packet,run in critical.items():","critical.update({'A079':'20261023T034945Z-account03-A079-correlated-auxiliaries','A003':'20261023T021528Z-account03-A003-minimal-target-formulation'})\nfor packet,run in critical.items():")
exec(compile(s,str(Path(__file__).resolve()),'exec'),globals())
