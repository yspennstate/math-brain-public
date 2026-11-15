#!/usr/bin/env python3
import os,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from iterate import run
if os.getpriority(os.PRIO_PROCESS,0)<10: os.nice(10)
for m in (2,3):
    for law in ('two2','two5','geom','power2.5','power3','power3.5','power4'):
        out=f'data/m{m}_{law}.csv'
        if not Path(out).exists(): run(m,law,10000,10128,out)
