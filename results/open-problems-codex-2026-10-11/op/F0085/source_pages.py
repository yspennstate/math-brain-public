from pathlib import Path
import pymupdf
p=Path('source.pdf');d=pymupdf.open(p)
for needle in ['Theorem 4 (Phases)','Theorem 5 (Geometry','Theorem 6 (In','Theorem 7 (Critical','Theorem 24 (Canonical','Proposition 21 (Monotonicity','Proposition 22 (Monotonicity']:
 print(needle,[i+1 for i,pg in enumerate(d) if needle in pg.get_text()])
