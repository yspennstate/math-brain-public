#!/usr/bin/env python3
import os,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from certified import run
if os.getpriority(os.PRIO_PROCESS,0)<10:os.nice(10)
for m in (2,3):
    run(m,'geom',10000,10128,f'data/cert_m{m}_geom.csv')
