"""Regenerate final window summaries only after every run is complete."""
import study as s
import numpy as np
from pathlib import Path
for L in (8,12,16,24):
    path=Path(f'window_L{L}_original_s{L*1000+7}.npz')
    z=np.load(path)
    assert len(z['data'])==32
    s.window_summary(path)
