#!/usr/bin/env python3
import os,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from iterate import run as fft
from certified import run as cert
if os.getpriority(os.PRIO_PROCESS,0)<10:os.nice(10)
for m in (2,3):fft(m,'sparse',10000,10128,f'data/m{m}_sparse.csv')
for m in (2,3):cert(m,'sparse',10000,10128,f'data/cert_m{m}_sparse.csv')
