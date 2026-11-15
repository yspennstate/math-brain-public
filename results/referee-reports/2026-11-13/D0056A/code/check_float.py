#!/usr/bin/env python3
import os,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from iterate import run
if os.getpriority(os.PRIO_PROCESS,0)<10:os.nice(10)
for m,law in ((2,'two2'),(2,'power3'),(3,'two2'),(3,'power3')):
    run(m,law,10000,20128,f'data/check_m{m}_{law}.csv')
