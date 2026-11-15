#!/usr/bin/env python3
import os, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from iterate import run
if os.getpriority(os.PRIO_PROCESS,0)<10: os.nice(10)
for m,law in ((2,'two2'),(2,'power3')):
    run(m,law,100000,100128,f'data/long_m{m}_{law}.csv')
