import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'20261014T040156Z-account05-A026-good-coordinate-erasure'/'code'))
import core as c
c.ROOT=ROOT
