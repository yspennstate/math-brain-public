from pathlib import Path
R=Path(__file__).resolve().parents[1];old=R.parent/'20261023T063447Z-fleet03-A028-stopping-tree-payment/code/independent.py'
s=old.read_text(encoding='utf-8');s=s[:s.index('\ndef walk(')]
(R/'code/independent8.py').write_text(s,encoding='utf-8',newline='')
print('Pinned direct-character v8 state copied; old tree and main excluded')
