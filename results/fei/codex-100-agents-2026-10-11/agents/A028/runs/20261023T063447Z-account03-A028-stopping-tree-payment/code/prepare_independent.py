from pathlib import Path
R=Path(__file__).resolve().parents[1];old=R.parent/'20261023T023055Z-account03-A028-stopping-tree-payment/code/independent.py'
text=old.read_text(encoding='utf-8')
prefix=text[:text.index('\ndef state(')]
(R/'code/independent_base.py').write_text(prefix,encoding='utf-8',newline='')
print('Independent direct-character arithmetic and conditional-erasure utilities copied; old state/tree excluded')
