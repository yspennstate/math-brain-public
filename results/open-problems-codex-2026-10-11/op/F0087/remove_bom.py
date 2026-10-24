from pathlib import Path
p=Path('HeightResidue.lean');p.write_text(p.read_text(encoding='utf-8-sig'),encoding='utf8')
